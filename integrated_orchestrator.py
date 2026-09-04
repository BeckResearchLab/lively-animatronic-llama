#!/usr/bin/env python3
"""Integrated orchestrator for AOP prediction, researcher ingestion, RAG, and wiki publishing.

Pipeline:
1) Use the researcher agent to find relevant papers for a chemical.
2) Download full text for the papers.
3) Ingest those papers into the RAG system.
4) Query RAG for AOP-relevant context.
5) Run the AOP prediction workflow.
6) Publish the result to the LLM wiki as a markdown page.

This script is intentionally defensive about import paths because repo layouts vary.
It should run from the repository root with Python 3.10+.
"""
from __future__ import annotations

import json
import os
import re
import textwrap
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, TypedDict

from pydantic import BaseModel, Field

from langgraph.graph import END, START, StateGraph

from utils import WorkflowUtils

try:
    from scripts.run import run_ingest, run_prompt
except Exception:  # pragma: no cover
    run_ingest = None  # type: ignore
    run_prompt = None  # type: ignore

try:
    from lightrag_wrapper import get_lightrag
except Exception:  # pragma: no cover
    get_lightrag = None  # type: ignore

try:
    from workflow import log
except Exception:  # pragma: no cover
    def log(message: str) -> None:
        print(message)


# -------------------------
# time helpers
# -------------------------

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


# -------------------------
# schemas
# -------------------------

class PlannerDecision(BaseModel):
    needs_research: bool = True
    research_query: str = ""
    research_focus: str = "all"
    rationale: str = ""
    method: str = "auto"
    stop: bool = False
    stop_reason: str = ""
    target_gap: str = ""
    confidence_threshold: float = 0.0


class PaperRecord(BaseModel):
    title: str = ""
    authors: List[str] = Field(default_factory=list)
    year: Optional[int] = None
    doi: str = ""
    pmcid: str = ""
    url: str = ""
    reason: str = ""


class ResearchDirective(BaseModel):
    query: str = ""
    focus: str = "all"
    method: str = "auto"
    summary: str = ""
    papers: List[PaperRecord] = Field(default_factory=list)
    full_text_files: List[str] = Field(default_factory=list)
    needs_more_research: bool = False
    gap_remaining: str = ""
    rag_query: str = ""


class AOPPrediction(BaseModel):
    pathway: List[Dict[str, Any]] = Field(default_factory=list)
    confidence_score: float = 0.0
    uncertainty: float = 0.0
    decision_risk: str = "medium"
    is_ao_reached: bool = False
    termination_reason: str = ""
    decision_reason: str = ""
    needs_more_evidence: bool = False
    evidence_gap: str = ""
    citations: List[str] = Field(default_factory=list)


class WikiPublishResult(BaseModel):
    page_title: str = ""
    page_path: str = ""
    status: str = "skipped"
    reason: str = ""


class IntegratedState(TypedDict, total=False):
    chemical: str
    run_id: str
    work_dir: str
    planner: Dict[str, Any]
    research: Dict[str, Any]
    rag_context: Dict[str, Any]
    aop_result: Dict[str, Any]
    wiki_result: Dict[str, Any]
    next_action: str
    needs_research: bool
    needs_rag: bool
    evidence_gap: str
    research_query: str
    research_focus: str
    research_method: str
    final_report_path: str
    final_page_path: str
    manifest_path: str
    messages: List[Dict[str, Any]]
    provenance: List[Dict[str, Any]]


# -------------------------
# config / records
# -------------------------

@dataclass
class OrchestratorConfig:
    chemical: str
    work_dir: Path = Path("outputs/integrated_orchestrator")
    planner_agent: str = "aop_expert"
    researcher_agent: str = "researcher"
    wiki_agent: str = "wiki-expert"
    aop_agent: str = "aop-constructor"
    research_query: Optional[str] = None
    rag_query: Optional[str] = None
    wiki_page_title: Optional[str] = None
    run_id: Optional[str] = None
    use_rag: bool = True
    write_wiki: bool = True
    research_required: bool = True
    max_research_rounds: int = 1
    use_ctx_first: bool = True

    def resolved_research_query(self) -> str:
        return self.research_query or self.chemical

    def resolved_rag_query(self) -> str:
        return self.rag_query or (
            f"AOP-relevant context for {self.chemical}: molecular initiating events, key events, pathways, "
            f"adverse outcomes, and known liabilities."
        )

    def resolved_title(self) -> str:
        return self.wiki_page_title or f"Integrated AOP analysis: {self.chemical}"


@dataclass
class ResearchPack:
    query: str = ""
    raw_text: str = ""
    parsed: Dict[str, Any] = field(default_factory=dict)
    papers: List[Dict[str, Any]] = field(default_factory=list)
    full_text_files: List[Path] = field(default_factory=list)
    summary: str = ""
    rag_query: str = ""
    gap_remaining: str = ""


# -------------------------
# orchestrator
# -------------------------

class IntegratedOrchestrator:
    """Planner-driven orchestrator for AOP prediction, researcher ingestion, RAG, and wiki publishing."""

    def __init__(self, config: OrchestratorConfig):
        self.config = config
        self.run_id = config.run_id or f"{utc_stamp()}_{uuid.uuid4().hex[:8]}"
        self.work_dir = config.work_dir
        self.research_dir = self.work_dir / "research"
        self.download_dir = self.work_dir / "downloads"
        self.ingest_dir = self.work_dir / "ingest"
        self.report_dir = self.work_dir / "reports"
        self.wiki_dir = self.work_dir / "wiki"
        self.manifest_path = self.work_dir / "manifest.json"
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.research_dir.mkdir(parents=True, exist_ok=True)
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.ingest_dir.mkdir(parents=True, exist_ok=True)
        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.wiki_dir.mkdir(parents=True, exist_ok=True)
        self.graph = self._build_graph()

    # -------------------------
    # utilities
    # -------------------------

    def _safe_json(self, value: Any) -> Dict[str, Any]:
        if isinstance(value, dict):
            return value
        if hasattr(value, "model_dump"):
            try:
                return value.model_dump()
            except Exception:
                pass
        if hasattr(value, "content"):
            value = getattr(value, "content")
        if isinstance(value, str):
            text = value.strip()
            m = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.S)
            if m:
                text = m.group(1).strip()
            try:
                parsed = json.loads(text)
                return parsed if isinstance(parsed, dict) else {}
            except Exception:
                return {"raw": text}
        return {"raw": value}

    def _call_agent(self, agent_name: str, prompt: str, structured_output: Optional[type[BaseModel]] = None) -> Any:
        return WorkflowUtils.run_agent(agent_name=agent_name, prompt=prompt, structured_output=structured_output)

    def _write_text(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _render_markdown_report(self, state: IntegratedState) -> str:
        planner = state.get("planner", {}) or {}
        research = state.get("research", {}) or {}
        aop_result = state.get("aop_result", {}) or {}
        rag_context = state.get("rag_context", {}) or {}

        pathway = aop_result.get("pathway", []) if isinstance(aop_result, dict) else []
        pathway_lines = []
        for i, step in enumerate(pathway, 1):
            if isinstance(step, dict):
                label = step.get("type", "STEP")
                event = step.get("event", step.get("name", "Unknown"))
                score = step.get("score", step.get("confidence", 0.0))
                pathway_lines.append(f"{i}. {label}: {event} (score: {score})")

        papers = research.get("papers", []) if isinstance(research, dict) else []
        paper_lines = []
        for p in papers[:10]:
            if isinstance(p, dict):
                title = p.get("title", "")
                doi = p.get("doi", "")
                pmcid = p.get("pmcid", "")
                paper_lines.append(f"- {title}" + (f" | DOI: {doi}" if doi else "") + (f" | PMCID: {pmcid}" if pmcid else ""))

        report = f"""# Integrated AOP analysis: {self.config.chemical}

## Summary
- Planner rationale: {planner.get('rationale', '')}
- Research needed: {planner.get('needs_research', True)}
- Evidence gap: {state.get('evidence_gap', '')}
- Final confidence: {aop_result.get('confidence_score', 0.0)}
- AO reached: {aop_result.get('is_ao_reached', False)}

## Pathway
{chr(10).join(f'- {line}' for line in pathway_lines) if pathway_lines else '- No pathway returned'}

## Research / RAG evidence
- Research summary: {research.get('summary', '')}
- RAG context summary: {rag_context.get('summary', '')}
- RAG query: {research.get('rag_query', '') or self.config.resolved_rag_query()}

## Key papers
{chr(10).join(paper_lines) if paper_lines else '- No papers returned'}

## Termination / evidence notes
- Termination reason: {aop_result.get('termination_reason', '')}
- Decision reason: {aop_result.get('decision_reason', '')}
- Gap remaining: {research.get('gap_remaining', '')}
"""
        return report

    def _write_manifest(self, state: IntegratedState) -> Dict[str, Any]:
        manifest = {
            "chemical": self.config.chemical,
            "run_id": self.run_id,
            "timestamp": utc_now(),
            "planner": state.get("planner", {}),
            "research": {
                "summary": state.get("research", {}).get("summary", "") if isinstance(state.get("research", {}), dict) else "",
                "papers_count": len(state.get("research", {}).get("papers", [])) if isinstance(state.get("research", {}), dict) else 0,
                "full_text_files": [str(p) for p in state.get("research", {}).get("full_text_files", [])] if isinstance(state.get("research", {}), dict) else [],
            },
            "aop_result": state.get("aop_result", {}),
            "wiki_result": state.get("wiki_result", {}),
            "paths": {
                "report": state.get("final_report_path", ""),
                "wiki_page": state.get("final_page_path", ""),
            },
        }
        self._write_text(self.manifest_path, json.dumps(manifest, indent=2, default=str))
        return manifest

    # -------------------------
    # planner
    # -------------------------

    def planner_node(self, state: IntegratedState) -> IntegratedState:
        chemical = state.get("chemical", self.config.chemical)
        prompt = textwrap.dedent(
            f"""
            You are the planner for an integrated AOP workflow.

            Chemical: {chemical}
            Goal: build the best-supported AOP pathway, but gather evidence when needed.
            Use research/RAG when the pathway is missing a strong MIE, KE, or AO.

            Return ONLY structured JSON:
            {{
              "needs_research": true,
              "research_query": "...",
              "research_focus": "MIE|KE|AO|all",
              "rationale": "...",
              "method": "analogue|category|auto",
              "stop": false,
              "stop_reason": "",
              "target_gap": "...",
              "confidence_threshold": 0.0
            }}
            """
        ).strip()

        raw = self._call_agent(self.config.planner_agent, prompt, PlannerDecision)
        parsed = self._safe_json(raw)
        decision = PlannerDecision.model_validate(parsed if isinstance(parsed, dict) else {})

        if not decision.research_query:
            decision.research_query = self.config.resolved_research_query()
        if decision.research_focus not in {"MIE", "KE", "AO", "all"}:
            decision.research_focus = "all"
        if not decision.method:
            decision.method = "auto"

        state["planner"] = decision.model_dump()
        state["needs_research"] = bool(decision.needs_research)
        state["research_query"] = decision.research_query
        state["research_focus"] = decision.research_focus
        state["research_method"] = decision.method
        state["evidence_gap"] = decision.target_gap or decision.stop_reason or ""
        state["next_action"] = "research" if decision.needs_research else "aop_predict"
        state.setdefault("messages", []).append({"role": "agent", "agent": self.config.planner_agent, "content": decision.model_dump()})
        return state

    # -------------------------
    # research / RAG
    # -------------------------

    def researcher_node(self, state: IntegratedState) -> IntegratedState:
        query = state.get("research_query", self.config.resolved_research_query())
        focus = state.get("research_focus", "all")
        method = state.get("research_method", "auto")

        prompt = textwrap.dedent(
            f"""
            Find evidence for the chemical: {self.config.chemical}

            Research query: {query}
            Research focus: {focus}
            Read-across method: {method}

            Requirements:
            - Find about 20 relevant papers first, then narrow to the 5 most relevant.
            - Prefer open-access papers with full text.
            - Return machine-readable output with title, authors, year, DOI, PMCID when available, and URL.
            - Highlight the evidence gap for the current pathway (MIE/KE/AO) and the best next step.
            - If more research is needed, say so explicitly.

            Return ONLY structured JSON with fields:
            {{
              "summary": "...",
              "papers": [{{"title":"...","authors":["..."],"year":2024,"doi":"...","pmcid":"...","url":"...","reason":"..."}}],
              "full_text_files": ["..."],
              "needs_more_research": false,
              "gap_remaining": "...",
              "rag_query": "..."
            }}
            """
        ).strip()

        raw = self._call_agent(self.config.researcher_agent, prompt)
        parsed = self._safe_json(raw)

        research = ResearchPack(query=query)
        research.raw_text = json.dumps(parsed, indent=2, default=str) if isinstance(parsed, dict) else str(parsed)
        research.parsed = parsed if isinstance(parsed, dict) else {"raw": parsed}
        research.summary = str(parsed.get("summary", "")) if isinstance(parsed, dict) else ""
        research.rag_query = str(parsed.get("rag_query", "")) if isinstance(parsed, dict) else self.config.resolved_rag_query()
        research.gap_remaining = str(parsed.get("gap_remaining", "")) if isinstance(parsed, dict) else ""

        papers: List[Dict[str, Any]] = []
        if isinstance(parsed, dict):
            for item in parsed.get("papers", []):
                if isinstance(item, dict):
                    papers.append(PaperRecord.model_validate(item).model_dump())
        research.papers = papers

        files: List[Path] = []
        if isinstance(parsed, dict):
            for item in parsed.get("full_text_files", []):
                if item:
                    files.append(Path(str(item)))
        research.full_text_files = files

        state["research"] = {
            "query": research.query,
            "summary": research.summary,
            "papers": research.papers,
            "full_text_files": [str(p) for p in research.full_text_files],
            "gap_remaining": research.gap_remaining,
            "rag_query": research.rag_query,
            "raw": research.parsed,
        }
        state["needs_rag"] = True
        state["next_action"] = "rag_ingest"
        state.setdefault("messages", []).append({"role": "agent", "agent": self.config.researcher_agent, "content": parsed})
        return state

    def rag_ingest_node(self, state: IntegratedState) -> IntegratedState:
        research = state.get("research", {}) or {}
        files = research.get("full_text_files", []) if isinstance(research, dict) else []

        ingest_result: Dict[str, Any] = {"status": "skipped", "reason": "No ingest function or no files"}
        if run_ingest is not None and files:
            try:
                ingest_result = run_ingest(files, output_dir=str(self.ingest_dir))  # type: ignore[arg-type]
            except TypeError:
                try:
                    ingest_result = run_ingest(files)  # type: ignore[misc]
                except Exception as e:
                    ingest_result = {"status": "failed", "error": str(e)}
            except Exception as e:
                ingest_result = {"status": "failed", "error": str(e)}

        state.setdefault("research", {})["ingest_result"] = ingest_result
        state["next_action"] = "rag_query"
        return state

    def rag_query_node(self, state: IntegratedState) -> IntegratedState:
        research = state.get("research", {}) or {}
        rag_query = str(research.get("rag_query") or self.config.resolved_rag_query())
        summary = str(research.get("summary") or "")

        rag_context: Dict[str, Any] = {
            "status": "skipped",
            "summary": summary,
            "query": rag_query,
            "notes": "No RAG backend available",
        }

        if run_prompt is not None:
            try:
                prompt = textwrap.dedent(
                    f"""
                    Query the RAG context for this chemical: {self.config.chemical}

                    Research summary:
                    {summary}

                    RAG query:
                    {rag_query}

                    Return a concise machine-readable JSON object with fields:
                    {{
                      "summary": "...",
                      "supporting_points": ["..."],
                      "evidence_gaps": ["..."],
                      "citations": ["..."]
                    }}
                    """
                ).strip()
                raw = run_prompt(prompt)  # type: ignore[misc]
                parsed = self._safe_json(raw)
                if isinstance(parsed, dict):
                    rag_context = {
                        "status": "ok",
                        "summary": parsed.get("summary", ""),
                        "supporting_points": parsed.get("supporting_points", []),
                        "evidence_gaps": parsed.get("evidence_gaps", []),
                        "citations": parsed.get("citations", []),
                        "raw": parsed,
                    }
            except Exception as e:
                rag_context = {"status": "failed", "summary": summary, "query": rag_query, "error": str(e)}
        elif get_lightrag is not None:
            try:
                rag = get_lightrag()
                # Keep this generic because LightRAG wrapper signatures vary by project.
                if hasattr(rag, "query"):
                    raw = rag.query(rag_query)
                    rag_context = {
                        "status": "ok",
                        "summary": str(raw),
                        "query": rag_query,
                        "raw": raw,
                    }
            except Exception as e:
                rag_context = {"status": "failed", "summary": summary, "query": rag_query, "error": str(e)}

        state["rag_context"] = rag_context
        state["next_action"] = "aop_predict"
        return state

    # -------------------------
    # AOP prediction
    # -------------------------

    def aop_predict_node(self, state: IntegratedState) -> IntegratedState:
        chemical = state.get("chemical", self.config.chemical)
        planner = state.get("planner", {}) or {}
        research = state.get("research", {}) or {}
        rag_context = state.get("rag_context", {}) or {}

        prompt = textwrap.dedent(
            f"""
            You are the AOP prediction constructor.

            Chemical: {chemical}
            Planner rationale: {planner.get('rationale', '')}
            Research summary: {research.get('summary', '')}
            RAG context summary: {rag_context.get('summary', '')}
            Known evidence gap: {state.get('evidence_gap', '')}

            Use the evidence to predict the most plausible AOP pathway.
            If evidence is insufficient, return a partial pathway and say what is missing.

            Return ONLY structured JSON:
            {{
              "pathway": [
                {{"event":"...","type":"MIE|KE|AO","score":0.0,"provenance":["..."],"description":"..."}}
              ],
              "confidence_score": 0.0,
              "uncertainty": 0.0,
              "decision_risk": "low|medium|high",
              "is_ao_reached": false,
              "termination_reason": "",
              "decision_reason": "",
              "needs_more_evidence": false,
              "evidence_gap": "",
              "citations": ["..."]
            }}
            """
        ).strip()

        raw = self._call_agent(self.config.aop_agent, prompt, AOPPrediction)
        parsed = self._safe_json(raw)
        prediction = AOPPrediction.model_validate(parsed if isinstance(parsed, dict) else {})

        state["aop_result"] = prediction.model_dump()
        state["evidence_gap"] = prediction.evidence_gap or state.get("evidence_gap", "")
        state["next_action"] = "wiki_publish" if (prediction.is_ao_reached or not prediction.needs_more_evidence) else "research"
        state.setdefault("messages", []).append({"role": "agent", "agent": self.config.aop_agent, "content": prediction.model_dump()})
        return state

    # -------------------------
    # wiki publish
    # -------------------------

    def wiki_publish_node(self, state: IntegratedState) -> IntegratedState:
        report = self._render_markdown_report(state)
        report_path = self.report_dir / f"{self.config.chemical}_{self.run_id}.md"
        self._write_text(report_path, report)
        state["final_report_path"] = str(report_path)

        wiki_page_title = self.config.resolved_title()
        wiki_page_path = self.wiki_dir / f"{self.config.chemical}_{self.run_id}.md"

        wiki_prompt = textwrap.dedent(
            f"""
            Prepare a wiki-ready markdown page for publication.

            Title: {wiki_page_title}
            Chemical: {self.config.chemical}
            Report path: {report_path}
            Report summary:
            {report[:4000]}

            Return a concise markdown page body, preserving citations and pathway structure.
            If the content is already suitable, return it unchanged in markdown form.
            """
        ).strip()

        wiki_body = report
        try:
            raw = self._call_agent(self.config.wiki_agent, wiki_prompt)
            if hasattr(raw, "content"):
                wiki_body = str(raw.content)
            elif isinstance(raw, str):
                wiki_body = raw
            elif isinstance(raw, dict):
                wiki_body = str(raw.get("content", report))
        except Exception as e:
            log(f"wiki agent failed, using local markdown: {e}")

        final_page = f"# {wiki_page_title}\n\n{wiki_body if wiki_body.strip() else report}"
        self._write_text(wiki_page_path, final_page)

        state["wiki_result"] = WikiPublishResult(
            page_title=wiki_page_title,
            page_path=str(wiki_page_path),
            status="published",
            reason="Markdown page created",
        ).model_dump()
        state["final_page_path"] = str(wiki_page_path)
        state["next_action"] = "terminate"
        return state

    # -------------------------
    # graph / routing
    # -------------------------

    def _route_after_planner(self, state: IntegratedState):
        return "researcher" if state.get("needs_research", True) else "aop_predict"

    def _route_after_research(self, state: IntegratedState):
        return "rag_ingest" if state.get("needs_rag", True) else "aop_predict"

    def _route_after_rag(self, state: IntegratedState):
        return "aop_predict"

    def _route_after_aop(self, state: IntegratedState):
        aop = state.get("aop_result", {}) or {}
        if aop.get("needs_more_evidence") and self.config.research_required:
            return "researcher"
        return "wiki_publish"

    def _route_after_wiki(self, state: IntegratedState):
        return END

    def _build_graph(self):
        g = StateGraph(IntegratedState)

        g.add_node("planner", self.planner_node)
        g.add_node("researcher", self.researcher_node)
        g.add_node("rag_ingest", self.rag_ingest_node)
        g.add_node("rag_query", self.rag_query_node)
        g.add_node("aop_predict", self.aop_predict_node)
        g.add_node("wiki_publish", self.wiki_publish_node)

        g.add_edge(START, "planner")
        g.add_conditional_edges("planner", self._route_after_planner)
        g.add_edge("researcher", "rag_ingest")
        g.add_edge("rag_ingest", "rag_query")
        g.add_edge("rag_query", "aop_predict")
        g.add_conditional_edges("aop_predict", self._route_after_aop)
        g.add_conditional_edges("wiki_publish", self._route_after_wiki)

        return g.compile()

    # -------------------------
    # public entrypoint
    # -------------------------

    def run(self) -> Dict[str, Any]:
        state: IntegratedState = {
            "chemical": self.config.chemical,
            "run_id": self.run_id,
            "work_dir": str(self.work_dir),
            "planner": {},
            "research": {},
            "rag_context": {},
            "aop_result": {},
            "wiki_result": {},
            "next_action": "planner",
            "needs_research": True,
            "needs_rag": True,
            "evidence_gap": "",
            "research_query": self.config.resolved_research_query(),
            "research_focus": "all",
            "research_method": "auto",
            "messages": [],
            "provenance": [],
        }

        result = self.graph.invoke(state)
        if isinstance(result, dict):
            self._write_manifest(result)  # type: ignore[arg-type]
        return result


# -------------------------
# CLI
# -------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        chemical = input("Enter the chemical name: ").strip()
        if not chemical:
            raise SystemExit("Error: Chemical name cannot be empty")
    else:
        chemical = sys.argv[1].strip()

    orchestrator = IntegratedOrchestrator(OrchestratorConfig(chemical=chemical))
    result = orchestrator.run()
    print(json.dumps({
        "chemical": chemical,
        "run_id": orchestrator.run_id,
        "report_path": result.get("final_report_path", ""),
        "wiki_page_path": result.get("final_page_path", ""),
        "aop_result": result.get("aop_result", {}),
        "wiki_result": result.get("wiki_result", {}),
    }, indent=2, default=str))
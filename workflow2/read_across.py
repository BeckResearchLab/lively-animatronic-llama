#!/usr/bin/env python3
"""
Tox21-based read-across helper for the AOP workflow.


Expected local database columns are flexible. Common fields supported include:
- chemical/name/compound
- assay/assay_name/endpoint
- active/hit/outcome
- target_class
- mechanism_of_action
- known_targets
- liabilities
- evidence/summary/reasoning/source

Set TOX21_DB_FILE to a file or directory. If the path is missing, the module
returns a structured empty result instead of crashing.
"""

from __future__ import annotations

import csv
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

# Optional API support
try:
    from pubchem_api import load_tox21_records_from_api, PubChemAPIError as Tox21APIError
except ImportError:
    # Fallback stubs if pubchem_api is not available
    def load_tox21_records_from_api(chemical_id, api_url=None, api_key=None, cache_dir=None, use_cache=True):
        return []
    
    class Tox21APIError(Exception):
        pass

TOX21_DB_FILE = Path(os.environ.get("TOX21_DB_FILE", "tox21_database.csv"))
READ_ACROSS_TOP_K = int(os.environ.get("READ_ACROSS_TOP_K", "5"))
READ_ACROSS_MIN_SCORE = float(os.environ.get("READ_ACROSS_MIN_SCORE", "0.15"))

STOPWORDS = {
    "a", "an", "and", "of", "the", "to", "in", "for", "with", "via", "by", "from",
    "is", "are", "be", "as", "at", "or", "this", "that", "these", "those", "on",
    "chemical", "compound", "target", "profile", "assay", "endpoint", "effect",
}

TEXT_FIELDS = (
    "name", "chemical_name", "compound", "cas", "inchikey", "smiles",
    "target_class", "mechanism_of_action", "endpoint", "assay", "assay_name",
    "summary", "evidence", "reasoning", "source", "study", "notes",
)


def _normalize_text(value: Any) -> str:
    text = str(value or "").lower().strip()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _tokens(value: Any) -> set[str]:
    return {t for t in _normalize_text(value).split() if t and t not in STOPWORDS}


def _as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, tuple):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return []
        if s.startswith("[") and s.endswith("]"):
            try:
                parsed = json.loads(s)
                if isinstance(parsed, list):
                    return [str(v).strip() for v in parsed if str(v).strip()]
            except Exception:
                pass
        parts = re.split(r"[|;,]\s*", s)
        return [p.strip() for p in parts if p.strip()]
    return [str(value).strip()] if str(value).strip() else []


def _maybe_bool(value: Any) -> Optional[bool]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"1", "true", "t", "yes", "y", "active", "hit", "positive"}:
        return True
    if text in {"0", "false", "f", "no", "n", "inactive", "negative"}:
        return False
    return None


def _flatten_record_text(record: Dict[str, Any]) -> str:
    parts: List[str] = []
    for key in TEXT_FIELDS:
        if record.get(key):
            val = record.get(key)
            if isinstance(val, (list, tuple, set)):
                parts.extend(map(str, val))
            else:
                parts.append(str(val))
    return _normalize_text(" ".join(parts))


def _profile_text(target_profile: Dict[str, Any], mies: Sequence[Dict[str, Any]] | None = None) -> str:
    parts: List[str] = []
    if not isinstance(target_profile, dict):
        return ""

    props = target_profile.get("properties", {}) if isinstance(target_profile.get("properties", {}), dict) else {}
    for k, v in props.items():
        parts.append(str(k))
        if isinstance(v, (list, tuple, set)):
            parts.extend(map(str, v))
        else:
            parts.append(str(v))

    liabilities = target_profile.get("liabilities", [])
    parts.extend(_as_list(liabilities))

    if mies:
        for mie in mies:
            if isinstance(mie, dict):
                parts.append(str(mie.get("name", "")))
                parts.append(str(mie.get("reasoning", "")))

    return _normalize_text(" ".join(parts))


def _read_json_file(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _read_table_file(path: Path) -> List[Dict[str, Any]]:
    delim = "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","
    try:
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter=delim)
            return [dict(row) for row in reader]
    except Exception:
        return []


def _read_jsonl_file(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except Exception:
                    continue
                if isinstance(item, dict):
                    rows.append(item)
    except Exception:
        pass
    return rows


def _coerce_records(obj: Any) -> List[Dict[str, Any]]:
    if obj is None:
        return []
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    if isinstance(obj, dict):
        if isinstance(obj.get("records"), list):
            return [x for x in obj["records"] if isinstance(x, dict)]
        return [obj]
    return []


def _convert_pubchem_to_read_across_format(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert PubChem records to a format that works better with read-across scoring."""
    converted = []
    
    # Group records by endpoint/assay to create more meaningful analogs
    endpoint_groups = defaultdict(list)
    for record in records:
        endpoint = record.get("endpoint", "Unknown")
        endpoint_groups[endpoint].append(record)
    
    # Create aggregated records for each endpoint
    for endpoint, endpoint_records in endpoint_groups.items():
        # Count active/inactive records for this endpoint
        active_count = sum(1 for r in endpoint_records if r.get("active") is True)
        inactive_count = sum(1 for r in endpoint_records if r.get("active") is False)
        
        # Use the first record as base, but aggregate information
        base_record = endpoint_records[0]
        
        # Create a consolidated record for this endpoint
        consolidated = {
            "chemical_name": base_record.get("chemical_name", "Unknown"),
            "compound": base_record.get("compound", "Unknown"),
            "endpoint": endpoint,
            "assay_name": endpoint,  # Use endpoint as assay name
            "active": active_count > inactive_count if (active_count + inactive_count) > 0 else None,
            "source": "PubChem",
            "study": endpoint,
            "evidence": f"PubChem assay: {endpoint}. Active: {active_count}, Inactive: {inactive_count}",
            "target_class": base_record.get("target_class", ""),
            "mechanism_of_action": base_record.get("mechanism_of_action", ""),
            "known_targets": _as_list(base_record.get("known_targets", [])),
            "liabilities": _as_list(base_record.get("liabilities", [])),
        }
        
        # Add additional context from all records for this endpoint
        all_evidence = [r.get("evidence", "") for r in endpoint_records if r.get("evidence")]
        if all_evidence:
            consolidated["evidence"] = " | ".join(set(all_evidence))
        
        converted.append(consolidated)
    
    return converted


def load_tox21_records(source: Optional[Any] = None) -> List[Dict[str, Any]]:
    """Load Tox21-compatible records from the pubchem_api module or local files."""
    if source is None:
        source = TOX21_DB_FILE

    # Try API first if enabled and source is a chemical identifier
    if os.environ.get("TOX21_ENABLE_API", "false").lower() == "true":
        try:
            api_records = load_tox21_records_from_api(str(source))
            if api_records:
                # Convert PubChem records to a format that works better with read-across
                return _convert_pubchem_to_read_across_format(api_records)
        except Tox21APIError:
            # Fall through to local loading if API fails
            pass

    if isinstance(source, (list, tuple)):
        return [x for x in source if isinstance(x, dict)]

    if isinstance(source, dict):
        return _coerce_records(source)

    path = Path(source)
    if not path.exists():
        return []

    if path.is_dir():
        rows: List[Dict[str, Any]] = []
        for p in sorted(path.iterdir()):
            if p.suffix.lower() in {".csv", ".tsv", ".tab"}:
                rows.extend(_read_table_file(p))
            elif p.suffix.lower() == ".jsonl":
                rows.extend(_read_jsonl_file(p))
            elif p.suffix.lower() == ".json":
                rows.extend(_coerce_records(_read_json_file(p)))
        return rows

    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv", ".tab"}:
        return _read_table_file(path)
    if suffix == ".jsonl":
        return _read_jsonl_file(path)
    if suffix == ".json":
        return _coerce_records(_read_json_file(path))
    return []


def _chemical_name(record: Dict[str, Any]) -> str:
    for key in ("chemical_name", "name", "compound", "preferred_name", "title"):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return "unknown"


def _canonical_endpoint(record: Dict[str, Any]) -> str:
    for key in ("endpoint", "endpoint_name", "assay_name", "assay", "pathway", "effect"):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return ""


def _record_is_active(record: Dict[str, Any]) -> Optional[bool]:
    for key in ("active", "hit", "outcome", "result", "tox21_hit", "tox21_active"):
        b = _maybe_bool(record.get(key))
        if b is not None:
            return b
    text = _normalize_text(record.get("activity", ""))
    if text in {"active", "hit", "positive"}:
        return True
    if text in {"inactive", "negative"}:
        return False
    return None


def _aggregate_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for row in records:
        name = _chemical_name(row)
        g = grouped.setdefault(
            name,
            {
                "name": name,
                "records": [],
                "endpoints": set(),
                "assays": set(),
                "sources": set(),
                "target_classes": set(),
                "mechanisms": set(),
                "known_targets": set(),
                "liabilities": set(),
                "evidence": [],
                "active_count": 0,
                "inactive_count": 0,
            },
        )
        g["records"].append(row)
        endpoint = _canonical_endpoint(row)
        if endpoint:
            g["endpoints"].add(endpoint)
        assay = str(row.get("assay_name") or row.get("assay") or "").strip()
        if assay:
            g["assays"].add(assay)
        source = str(row.get("source") or row.get("study") or row.get("dataset") or "Tox21").strip()
        if source:
            g["sources"].add(source)
        for key in ("target_class", "mechanism_of_action"):
            val = str(row.get(key, "")).strip()
            if val:
                g[key + "es" if key.endswith("s") else key + "s"].add(val)
        for key in ("known_targets", "liabilities"):
            for item in _as_list(row.get(key)):
                g[key].add(item)
        evidence = " ".join(
            str(row.get(k, ""))
            for k in ("evidence", "summary", "reasoning", "notes", "endpoint", "assay_name", "assay")
        ).strip()
        if evidence:
            g["evidence"].append(evidence)
        active = _record_is_active(row)
        if active is True:
            g["active_count"] += 1
        elif active is False:
            g["inactive_count"] += 1

    analogs: List[Dict[str, Any]] = []
    for name, g in grouped.items():
        analogs.append(
            {
                "name": name,
                "endpoints": sorted(g["endpoints"]),
                "assays": sorted(g["assays"]),
                "sources": sorted(g["sources"]),
                "target_classes": sorted(g["target_classes"]),
                "mechanisms": sorted(g["mechanisms"]),
                "known_targets": sorted(g["known_targets"]),
                "liabilities": sorted(g["liabilities"]),
                "evidence": " | ".join(g["evidence"][:8]),
                "active_count": int(g["active_count"]),
                "inactive_count": int(g["inactive_count"]),
                "record_count": len(g["records"]),
                "raw_records": g["records"][:20],
            }
        )
    return analogs


def _score_overlap(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    union = a | b
    if not union:
        return 0.0
    return float(len(a & b) / len(union))


def _score_analog(target_profile: Dict[str, Any], mies: Sequence[Dict[str, Any]] | None, analog: Dict[str, Any]) -> Dict[str, Any]:
    props = target_profile.get("properties", {}) if isinstance(target_profile, dict) else {}
    target_class = _tokens(props.get("target_class", ""))
    target_mech = _tokens(props.get("mechanism_of_action", ""))
    target_targets = _tokens(props.get("known_targets", []))
    target_liabilities = _tokens(target_profile.get("liabilities", [])) if isinstance(target_profile, dict) else set()
    target_text = _profile_text(target_profile, mies)
    analog_text = _normalize_text(
        " ".join(
            [
                analog.get("name", ""),
                " ".join(analog.get("endpoints", [])),
                " ".join(analog.get("assays", [])),
                " ".join(analog.get("target_classes", [])),
                " ".join(analog.get("mechanisms", [])),
                " ".join(analog.get("known_targets", [])),
                " ".join(analog.get("liabilities", [])),
                analog.get("evidence", ""),
            ]
        )
    )

    analog_class = _tokens(analog.get("target_classes", []))
    analog_mech = _tokens(analog.get("mechanisms", []))
    analog_targets = _tokens(analog.get("known_targets", []))
    analog_liabilities = _tokens(analog.get("liabilities", []))
    analog_endpoints = _tokens(analog.get("endpoints", []))
    analog_text_tokens = _tokens(analog_text)
    target_text_tokens = _tokens(target_text)

    class_overlap = _score_overlap(target_class, analog_class)
    mech_overlap = _score_overlap(target_mech, analog_mech)
    target_overlap = _score_overlap(target_targets, analog_targets)
    liability_overlap = _score_overlap(target_liabilities, analog_liabilities | analog_endpoints)
    text_overlap = _score_overlap(target_text_tokens, analog_text_tokens)

    activity_boost = 0.0
    if analog.get("active_count", 0) > 0:
        activity_boost += min(0.12, 0.03 * analog.get("active_count", 0))
    if analog.get("inactive_count", 0) > 0 and analog.get("active_count", 0) == 0:
        activity_boost -= min(0.05, 0.01 * analog.get("inactive_count", 0))

    raw = (
        0.22 * class_overlap
        + 0.24 * mech_overlap
        + 0.22 * target_overlap
        + 0.18 * liability_overlap
        + 0.14 * text_overlap
        + activity_boost
    )
    score = float(np.clip(raw, 0.0, 1.0))

    reasons: List[str] = []
    if class_overlap:
        reasons.append("shared target class")
    if mech_overlap:
        reasons.append("shared mechanism text")
    if target_overlap:
        reasons.append("shared known targets")
    if liability_overlap:
        reasons.append("shared liability / endpoint terms")
    if text_overlap:
        reasons.append("text overlap with target profile")
    if analog.get("active_count", 0) > 0:
        reasons.append("active Tox21 signal")
    if not reasons:
        reasons.append("weak read-across support from Tox21 profile")

    match_terms = sorted(
        (target_class & analog_class)
        | (target_mech & analog_mech)
        | (target_targets & analog_targets)
        | (target_liabilities & (analog_liabilities | analog_endpoints))
        | (target_text_tokens & analog_text_tokens)
    )

    return {
        **analog,
        "score": score,
        "reasoning": "; ".join(reasons),
        "match_terms": match_terms,
    }


def enrich_read_across(
    chemical: str,
    *,
    target_profile: Optional[Dict[str, Any]] = None,
    mies: Optional[Sequence[Dict[str, Any]]] = None,
    records: Optional[List[Dict[str, Any]]] = None,
    source: Optional[Any] = None,
    top_k: Optional[int] = None,
) -> Dict[str, Any]:
    """Return a read-across evidence bundle scored from Tox21 records."""
    top_k = READ_ACROSS_TOP_K if top_k is None else int(top_k)
    target_profile = target_profile or {}
    mies = list(mies or [])

    db_records = records if records is not None else load_tox21_records(source)
    
    # If records came from PubChem API, convert them to a better format
    if records is not None and len(records) > 0 and records[0].get("source") == "PubChem":
        db_records = _convert_pubchem_to_read_across_format(db_records)
    if not db_records:
        return {
            "chemical": chemical,
            "status": "empty_library",
            "analogs": [],
            "supporting_evidence": [],
            "matched_endpoints": [],
            "confidence": 0.0,
            "summary": "No Tox21 records available.",
            "source": str(source or TOX21_DB_FILE),
        }

    analogs = _aggregate_records(db_records)
    scored = [_score_analog(target_profile, mies, analog) for analog in analogs]
    scored = [x for x in scored if float(x.get("score", 0.0)) >= READ_ACROSS_MIN_SCORE]
    scored.sort(key=lambda x: float(x.get("score", 0.0)), reverse=True)
    top = scored[:top_k]

    supporting_evidence: List[str] = []
    matched_endpoints: List[str] = []
    all_terms: set[str] = set()
    for item in top:
        if item.get("evidence"):
            supporting_evidence.append(f"{item['name']}: {item['evidence']}")
        matched_endpoints.extend(item.get("endpoints", []))
        all_terms.update(item.get("match_terms", []))

    confidence = float(np.clip(mean([float(x.get("score", 0.0)) for x in top]) if top else 0.0, 0.0, 1.0))
    summary = (
        f"Read-across found {len(top)} supported analog(s) from Tox21. "
        f"Top evidence centers on: {', '.join(sorted(set(matched_endpoints))[:5]) or 'no matched endpoints'}."
    )

    return {
        "chemical": chemical,
        "status": "ok" if top else "no_matches",
        "analogs": top,
        "supporting_evidence": supporting_evidence,
        "matched_endpoints": sorted(set(matched_endpoints)),
        "confidence": confidence,
        "summary": summary,
        "match_terms": sorted(all_terms),
        "source": str(source or TOX21_DB_FILE),
    }


def summarize_read_across(result: Dict[str, Any]) -> str:
    if not isinstance(result, dict):
        return ""
    if result.get("status") not in {"ok", "no_matches", "empty_library"}:
        return ""
    analogs = result.get("analogs", []) if isinstance(result.get("analogs", []), list) else []
    names = [a.get("name", "unknown") for a in analogs if isinstance(a, dict)]
    endpoints = result.get("matched_endpoints", []) if isinstance(result.get("matched_endpoints", []), list) else []
    if not analogs:
        return result.get("summary", "No read-across matches.")
    return (
        f"Read-across: {', '.join(names[:3])} "
        f"support {'; '.join(endpoints[:5]) if endpoints else 'no matched endpoints'}."
    )


def enrich_read_across_state(state: Dict[str, Any], *, source: Optional[Any] = None, top_k: Optional[int] = None) -> Dict[str, Any]:
    chemical = str(state.get("chemical", "")).strip()
    target_profile = state.get("data", {}).get("target_profile", {}) if isinstance(state.get("data", {}), dict) else {}
    mies = state.get("MIEs", []) if isinstance(state.get("MIEs", []), list) else []
    result = enrich_read_across(
        chemical,
        target_profile=target_profile,
        mies=mies,
        source=source,
        top_k=top_k,
    )
    state.setdefault("data", {})["read_across"] = result
    state.setdefault("messages", []).append({"role": "agent", "agent": "read_across", "content": result})
    return state


__all__ = [
    "TOX21_DB_FILE",
    "READ_ACROSS_TOP_K",
    "READ_ACROSS_MIN_SCORE",
    "load_tox21_records",
    "enrich_read_across",
    "enrich_read_across_state",
    "summarize_read_across",
]
from typing import Annotated, TypedDict, ClassVar, List, Dict, Any, Optional
from pathlib import Path
from unittest import result
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph import StateGraph, MessagesState, END, START, END
from langgraph.types import Command
import json
import os
import subprocess
from datetime import datetime, timezone

# Name file for Langsmith
os.environ["LANGCHAIN_PROJECT"] = "content-node.py"

from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model="devstral-small", temperature=0.1)

reference_files = {
    "categories": Path("./references/top-level-categories.md").read_text(),
    "specs": Path("./references/specs.md").read_text(),
    "page-template": Path("./references/page-template-examples.md").read_text(),
    "outline": Path("./wiki-seed-outline_GPT.md").read_text(),
    "overview": Path("./wiki-seed-overview_GPT.md").read_text(),
    "checklist": Path("./wiki-seed-checklist_GPT.md").read_text()
}

class PageItem(BaseModel):
    title: str
    category: str

class PagePlan(BaseModel):
    pages: List[PageItem]

class State(MessagesState):
    next: str
    pages_created: dict  # Changed from list to dict: {category: [pages...]}
    current_category: Optional[str] = None
    categories_processed: List[str] = []
    category_context: dict = Field(default_factory=dict)  # 
    pages_with_frontmatter: list[PageItem]
    pages_with_content: list[PageItem]
    categories_created: list[str]
    latest_europepmc: Optional[dict]
    completion_status: dict = Field(default_factory=lambda: {
        "frontmatter": False,
        "content": False,
        "category": False,
        "validation": False
    })
    validation_checklist: str           
    validation_inspection: str
    validation_summary: str
    validation_done: bool

@tool
def get_reference_files(file_key: str) -> str:
    """
    Get reference file content from the agent's context.
    Available file keys: "overview", "outline", "categories", "specs", "page-template"
    
    Args:
        file_key: The key of the reference file to retrieve
    
    Returns:
        The content of the requested reference file
    """
    return reference_files.get(file_key, "")

ROOT = Path("./wiki").resolve()
DOCS_ROOT = Path("./wiki/docs").resolve()
PREFIX = Path("wiki")
DOCS_PREFIX = Path("wiki/docs")

def _safe_path(relative_path: str, base: Path = ROOT) -> Path:
    rel = Path(relative_path)

    if rel.parts[:len(DOCS_PREFIX.parts)] == DOCS_PREFIX.parts:
        rel = Path(*rel.parts[len(DOCS_PREFIX.parts):])
        base = DOCS_ROOT
    elif rel.parts[:len(PREFIX.parts)] == PREFIX.parts:
        rel = Path(*rel.parts[len(PREFIX.parts):])
        base = ROOT

    path = (base / rel).resolve()

    if path != base and base not in path.parents:
        raise ValueError(f"Unsafe path: {relative_path}")

    return path

@tool
def create_folder(folder_path: str) -> str:
    """Create a folder under ./wiki/docs/."""
    path = _safe_path(folder_path)
    path.mkdir(parents=True, exist_ok=True)
    return f"Created folder: {path}"

@tool
def create_empty_page(file_path: str, claim: bool = False) -> str:
    """Create an empty markdown file for scaffold only."""
    path = _safe_path(file_path).with_name(Path(file_path).stem + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")
    result = {
        "status": "wrote_page",
        "title": path.name,
        "category": path.parent.name,
        "file_path": str(path.relative_to(ROOT)),
        "claim": claim,
    }
    print("create_page title:", result["title"], "-", result["category"])
    return json.dumps(result, ensure_ascii=False)

@tool
def create_page(file_path: str, content: str, claim: bool = False) -> str:
    """Create an empty markdown file."""
    path = _safe_path(file_path)
    path = path.with_name(path.stem + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    result = {
        "status": "wrote_page",
        "title": path.name,
        "category": path.parent.name,
        "file_path": str(path.relative_to(ROOT)),
        "claim": claim,
    }
    return json.dumps(result)

@tool
def create_text_file(file_path: str, content: str) -> str:
    """Create any text file under ./wiki/ or ./wiki/docs/."""
    path = _safe_path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return json.dumps({
        "status": "wrote_file",
        "file_path": str(path.relative_to(ROOT)),
        "title": path.name,
    })

@tool
def update_page_body(file_path: str, body: str) -> str:
    """Update the body of a markdown file, preserving frontmatter when present and writing body-only when absent."""
    path = _safe_path(file_path)
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    body = body.strip()

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            frontmatter = "---" + parts[1] + "---\n"
            new_content = frontmatter + "\n" + body + "\n"
        else:
            new_content = body + "\n"
    else:
        new_content = body + "\n"

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new_content, encoding="utf-8")
    return f"Updated body: {path}"

@tool
def search_europepmc(
    query: str,
    max_results: int = 10,
    result_type: str = "core",
    sort: str = "",
    output_file: str = "/tmp/europepmc_search_results.json"
) -> str:
    """
    Search Europe PMC for scientific literature using the europepmc_api.py script.

    Args:
        query: Search query using Europe PMC syntax
        max_results: Maximum number of results to return (default: 10)
        result_type: Result detail level - "core" or "lite" (default: "core")
        sort: Sort order (e.g., "CITED desc", "P_PDATE_D desc")
        output_file: Path to save search results (default: /tmp/europepmc_search_results.json)

    Returns:
        JSON string containing search results with hitCount, nextCursorMark, and results

    Example:
        search_europepmc("CRISPR cancer", max_results=5)
        search_europepmc("DOI:10.1038/s41586-021-03819-2")
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Build the command
    cmd = [
        "uv", "run",
        "skills/literature-search-europepmc/scripts/europepmc_api.py",
        "search",
        query,
        "--max_results", str(max_results),
        "--result_type", result_type,
        "--output", output_file
    ]

    if sort:
        cmd.extend(["--sort", sort])

    # Execute the command
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            cwd="/home/etaman/lively-animatronic-llama/python/wiki-seed"
        )

        # Read and return the results
        with open(output_file, 'r') as f:
            results = json.load(f)

        return json.dumps(results)

    except subprocess.CalledProcessError as e:
        error_msg = f"Error searching EuropePMC: {e.stderr}"
        return json.dumps({"error": error_msg, "command": " ".join(cmd)})
    except Exception as e:
        return json.dumps({"error": str(e)})

    

content_agent = create_agent(
    model=llm, 
    tools=[update_page_body, get_reference_files],
    system_prompt="""
    You fill in the content in the wiki pages. 
    Use the reference files to determine the correct page structure.

    References files:
    - Categories: list of top-level categories needed
    - Specs: Docusaurus structure specifications
    - Page-template: examples of page structure and content

    Task:
    1. Process ALL pages in the pages_created list
    2. For each page, use update_page_body to add content
    3. When ALL pages are processed, your final message MUST contain: "Content completion: ALL PAGES PROCESSED"
    4. Do not stop until all pages have content added
    """)


def content_node(state: State) -> Command:
    pages_created = state.get("pages_created", {}) or {}
    current_category = state.get("current_category")
    categories_processed = list(state.get("categories_processed", []) or [])
    category_context = dict(state.get("category_context", {}) or {})
    completion_status = dict(state.get("completion_status", {}) or {})

    all_categories = list(pages_created.keys())
    remaining_categories = [cat for cat in all_categories if cat not in categories_processed]

    if not remaining_categories:
        return Command(
            update={
                "completion_status": {**completion_status, "content": True},
                "current_category": None,
                "messages": [HumanMessage(content="All content completed for all categories.")],
            },
            goto=END,
        )

    if current_category is None or current_category in categories_processed:
        current_category = remaining_categories[0]

    pages_to_process = pages_created.get(current_category, [])

    instructions = f"""
Process ONLY this category: {current_category}

Pages to process:
{json.dumps(pages_to_process, indent=2)}

Do not process any other category.
When all pages in this category are processed, your final message MUST contain:
CATEGORY_{current_category}_COMPLETED
"""

    # IMPORTANT: send a clean message list so old AI/tool messages do not accumulate
    result = content_agent.invoke({
        "messages": [HumanMessage(content=instructions)],
        "pages_created": pages_created,
        "current_category": current_category,
        "categories_processed": categories_processed,
        "category_context": category_context,
        "completion_status": completion_status,
    })

    last_ai_message = result["messages"][-1].content if result.get("messages") else ""
    is_category_complete = f"CATEGORY_{current_category}_COMPLETED" in last_ai_message

    updated_categories_processed = (
        categories_processed + [current_category]
        if is_category_complete
        else categories_processed
    )
    remaining_after = [cat for cat in all_categories if cat not in updated_categories_processed]

    # Keep reference_files available globally, but drop finished category context
    cleaned_category_context = dict(category_context)
    if is_category_complete:
        cleaned_category_context.pop(current_category, None)
    else:
        cleaned_category_context[current_category] = {
            "reference_files": reference_files.copy(),
            "pages_processed": pages_to_process,
        }

    # Replace the full conversation with a single short summary message
    # so old AI/tool messages do not keep growing the context window.
    summary_message = HumanMessage(
        content=(
            f"Completed category: {current_category}"
            if is_category_complete
            else f"Processing category: {current_category}"
        )
    )

    return Command(
        update={
            "current_category": None if is_category_complete else current_category,
            "categories_processed": updated_categories_processed,
            "category_context": cleaned_category_context,
            "completion_status": {
                **completion_status,
                "content": len(remaining_after) == 0,
            },
            "messages": [summary_message],
        },
        goto="content" if remaining_after else END,
    )

content_builder = StateGraph(State)
content_builder.add_node("content", content_node)

content_builder.add_edge(START, "content")
content_builder.add_edge("content", END)

content_graph = content_builder.compile()
content_graph = content_graph.with_config({"run_name": "content - no ingestion, no europepmc"})

def load_scaffold_output():
    """Load scaffold output from file if it exists."""
    output_file = Path("./scaffold_output.json")
    if not output_file.exists():
        return None

    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, IOError):
        return None

def build_initial_state_from_scaffold():
    """Build initial state for content_node.py using scaffold output."""
    scaffold_data = load_scaffold_output()

    if scaffold_data is None:
        return {
            "messages": [{"role": "user", "content": "Seed a Docusaurus-compatible LLM research wiki."}],
            "next": "",
            "pages_created": {},
            "scaffold_files": [],
            "scaffold_done": False,
            "pages_with_frontmatter": [],
            "pages_with_content": [],
            "categories_created": [],
            "current_category": None,
            "categories_processed": [],
            "category_context": {},
            "completion_status": {
                "frontmatter": False,
                "content": False,
                "category": False,
                "validation": False
            },
            "validation_checklist": "",
            "validation_inspection": "",
            "validation_summary": "",
            "validation_done": False,
        }

     # Check if pages_created is already in category-based format (dict)
    pages_created_data = scaffold_data.get("pages_created", {})
    if isinstance(pages_created_data, dict):
        # Already in the correct format
        pages_by_category = pages_created_data
    else:
        # Convert flat list to category-based structure (backward compatibility)
        pages_by_category = {}
        for page in pages_created_data:
            category = page.get("category", "uncategorized")
            if category not in pages_by_category:
                pages_by_category[category] = []
            pages_by_category[category].append(page)

    return {
        "messages": [{"role": "user", "content": "Seed a Docusaurus-compatible LLM research wiki."}],
        "next": "",
        "pages_created": pages_by_category,
        "scaffold_files": scaffold_data.get("docusaurus_files", []),
        "scaffold_done": True,
        "pages_with_frontmatter": [],
        "pages_with_content": [],
        "categories_created": [],
        "current_category": None,
        "categories_processed": [],
        "category_context": {},
        "completion_status": {
            "frontmatter": False,
            "content": False,
            "category": False,
            "claim_content": False,
            "scaffold": scaffold_data.get("completion_status", {}).get("scaffold", True)
        },
        "validation_checklist": "",
        "validation_inspection": "",
        "validation_summary": "",
        "validation_done": False,
    }

initial_state = build_initial_state_from_scaffold()

content_output = content_graph.invoke(initial_state)
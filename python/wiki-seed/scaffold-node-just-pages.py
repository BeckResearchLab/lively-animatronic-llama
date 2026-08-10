from typing import Annotated, TypedDict, ClassVar, List, Dict, Any, Optional
from pathlib import Path
from unittest import result
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage, AIMessage
from langchain_core.tools import tool
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph import StateGraph, MessagesState, END, START, END
from langgraph.types import Command
import json
import re
import os

# Name file for Langsmith
os.environ["LANGCHAIN_PROJECT"] = "scaffold-node.py"

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

class State(MessagesState):
    next: str
    pages_created: list[dict]
    docusaurus_files: list[dict]
    category_json_files: list[dict]
    scaffold_plan: dict
    page_planner_done: bool
    scaffold_done: bool
    categories_created: list[str]
    completion_status: dict = Field(default_factory=lambda: {
        "scaffold": False,
        "frontmatter": False,
        "content": False,
        "category": False,
        "validation": False
    })

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
    print("created folder:", folder_path)
    return f"Created folder: {path}"

@tool
def create_file_batch(file_paths: List[str], content: str = "", overwrite: bool = True) -> str:
    """Create or overwrite multiple text files at safe paths in a single call."""
    results = []
    for file_path in file_paths:
        try:
            path = _safe_path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            if path.suffix.lower() == ".md":
                content = ""  # force scaffold markdown pages to stay empty

            if path.exists() and not overwrite:
                results.append({
                    "status": "exists",
                    "title": path.name,
                    "category": path.parent.name,
                    "file_path": str(path),
                })
            else:
                path.write_text(content, encoding="utf-8")
                results.append({
                    "status": "wrote_file",
                    "title": path.name,
                    "category": path.parent.name,
                    "file_path": str(path),
                })
        except Exception as e:
            results.append({
                "status": "error",
                "title": file_path,
                "error": str(e)
            })

    return json.dumps(results)

scaffold_agent = create_agent(
    model=llm,
    tools=[create_folder, create_file_batch, get_reference_files],
    system_prompt="""
    You create the Docusaurus-compatible skeleton for the wiki seeding.

    Use the reference files to determine the correct folder structure and naming conventions.

    Refer to the overview file first. Use the outline file when more information is required than what the overview file provides.
    When reading the Outline, focus on the sections discussing Docusarus structure as well as `## D5. Page Creation and Update Rules`.

    Leave content empty unless the file type requires boilerplate.

    Reference files:
    - Overview: high-level process
    - Outline: full workflow and category structure
    - Categories: list of top-level categories needed

    All wiki pages should be associated to a category.
    Required Docusaurus file are NOT associated to a category. 

    Task:
    - Create ALL category folders
    - Create any subfolders when categories need more organization
    - Create enough empty pages for the initial wiki-seeding
    - Create the additional files to make the wiki Docusaurus-compatible.
    - Use create_file_batch for creating multiple pages at once to avoid timeout issues
    """
)

def scaffold_node(state: State) -> Command:
    completion_status = dict(state.get("completion_status", {}))
    print("Starting scaffold_agent.invoke...")

    result = scaffold_agent.invoke(state)
    print("scaffold_agent.invoke completed.")

    pages_created = []
    docusaurus_files = []
    category_json_files = []

    for message in result["messages"]:
        if isinstance(message, ToolMessage):
            try:
                data = json.loads(message.content)
                print(f"Processing tool message: {data}")

                if isinstance(data, list):
                # Handle batch results
                    for item in data:
                        if item.get("status") != "wrote_file":
                            continue

                        file_path = Path(item["file_path"])
                        is_json = file_path.suffix.lower() == ".json"
                        is_md = file_path.suffix.lower() == ".md"

                    # Check if file is under a category folder
                    # Category folders are under wiki/docs/some-category/
                        try:
                            rel_path = file_path.relative_to(DOCS_ROOT)
                            has_category = len(rel_path.parts) > 1 and rel_path.parts[0] not in ['sidebars', 'docusaurus-config', '.docusaurus']
                        except ValueError:
                        # File is not under DOCS_ROOT, so no category
                            has_category = False

                        if is_md and has_category:
                            pages_created.append(item)
                        elif is_json:
                            category_json_files.append(item)
                        else:
                            docusaurus_files.append(item)
                else:
                # Handle single result
                    if data.get("status") != "wrote_file":
                        continue

                    item = {
                    "title": data.get("title"),
                    "file_path": data.get("file_path"),
                    "category": data.get("category")
                }

                    file_path = Path(data["file_path"])
                    is_json = file_path.suffix.lower() == ".json"
                    is_md = file_path.suffix.lower() == ".md"

                    # Check if file is under a category folder
                    try:
                        rel_path = file_path.relative_to(DOCS_ROOT)
                        has_category = len(rel_path.parts) > 1 and rel_path.parts[0] not in ['sidebars', 'docusaurus-config', '.docusaurus']
                    except ValueError:
                    # File is not under DOCS_ROOT, so no category
                        has_category = False

                    if is_md and has_category:
                        pages_created.append(item)
                    elif is_json:
                        category_json_files.append(item)
                    else:
                        docusaurus_files.append(item)

            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                continue

    print(f"Processed {len(pages_created)} pages, {len(docusaurus_files)} docusaurus files, and {len(category_json_files)} category JSON files.")
    print(f"Total files created: {len(pages_created) + len(docusaurus_files) + len(category_json_files)}")

    return Command(
        update = {
            "pages_created": pages_created,
            "docusaurus_files": docusaurus_files,
            "category_json_files": category_json_files,
            "completion_status": {**completion_status, "scaffold": True},
            "messages": [HumanMessage(content=(
                        f"Planned and created {len(pages_created)} pages, "
                        f"{len(docusaurus_files)} other files, and "
                        f"{len(category_json_files)} category JSON files."
                    ))],
        }
    )  

scaffold_builder = StateGraph(State)
scaffold_builder.add_node("scaffold", scaffold_node)

scaffold_builder.add_edge(START, "scaffold")
scaffold_builder.add_edge("scaffold", END)

scaffold_graph = scaffold_builder.compile()
scaffold_graph = scaffold_graph.with_config({"run_name": "2 nodes"})

initial_state = {
    "messages": [{"role": "user", "content": "Create the skeleton structure for a Docusaurus-compatible wiki."}],
    "pages_created": [],
    "docusaurus_files": [],
    "category_json_file": [],
    "page_planner_done": False,
    "scaffold_done": False,
    "scaffold_plan": {},
    "completion_status": {
        "scaffold": False,
        "frontmatter": False,
        "content": False,
        "category": False,
        "claim_content": False
    },
}

scaffold_result = scaffold_graph.invoke(initial_state)

def save_scaffold_output(state):
    """Save the scaffold output state to a file for content_node.py to load."""
    output_file = Path("./scaffold_output.json")

    # Group pages by category
    pages_by_category = {}
    pages_without_category = []

    for page in state.get("pages_created", []):
        category = page.get("category")
        if category:
            if category not in pages_by_category:
                pages_by_category[category] = []
            pages_by_category[category].append(page)
        else:
            pages_without_category.append(page)

    output_data = {
        "pages_created": pages_by_category,
        "pages_without_category": pages_without_category,
        "docusaurus_files": state.get("docusaurus_files", []),
        "category_json_files": state.get("category_json_files", []),
        "scaffold_done": True,
        "completion_status": state.get("completion_status", {})
    }

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Scaffold output saved to {output_file}")
    return output_data

save_scaffold_output(scaffold_result)

"""
png = scaffold_graph.get_graph().draw_mermaid_png()

with open("scaffold_graph.png", "wb") as f:
    f.write(png)

print("saved as scaffold_graph.png")"""
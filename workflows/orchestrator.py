#API Keys
from dotenv import load_dotenv
load_dotenv()

import json
import os
import operator
import datetime
from pathlib import Path
from typing import Annotated, TypedDict, Dict, List, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# --- LLM ---
llm = ChatOpenAI(
    model=os.environ.get("OPENAI_MODEL", "gemma-4-31b"),
    temperature=0.7,
    max_tokens=20048,
    api_key=os.environ.get("OPENAI_API_KEY"),
    timeout=4000,
    max_retries=3,
)

# --- Graph State ---
class AOPState(TypedDict):
    original_query: Annotated[str, lambda x, y: x]
    chemical: str
    messages: Annotated[List[BaseMessage], operator.add]
    data: Dict[str, Any]
    next_agent: str
    status: str
    reference_files: Dict[str, Any]
    AOP_guess: str
    MIE: str
    Candidates: str

# --- Initial State of Graph ---
initial_state: AOPState = {
    "original_query": "",
    "chemical": "",
    "messages": [],
    "data": {},
    "next_agent": "constructor",
    "status": "needs_admet",  # Initial status
    "reference_files": {
        "admet_mie": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/admet-mie.md")).read_text(),
        "aop_expert": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/aop-expert.md")).read_text(),
        "visuals_agent": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/visuals-agent.md")).read_text(),
        "constructor": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/aop-constructor.md")).read_text(),
    "AOP_guess": "",
    "MIE": "",
    "Candidates": ""
    },
}


# --- Nodes ---
def admet_mie_node(state: AOPState) -> AOPState:
    admet_mie = state.get("admet_mie", "")
    chemical = state.get("chemical", "")

    messages = [SystemMessage(content=f"""
    You are an expert in ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) and 
    MIE (Molecular Interaction Engineering). Your task is to analyze the provided chemical information and generate 
    a comprehensive ADMET profile for the given chemical: {chemical}.
    {admet_mie}
    """)]

    response = llm.invoke(messages)
    print("ADMET Analysis:", response.content)
    
    # Store the ADMET results in the state
    state["data"]["admet_results"] = response.content
    
    # Update status to indicate ADMET analysis is complete
    state["status"] = "needs_aop"

    return state


def aop_expert_node(state: AOPState) -> AOPState:
    aop_expert = state.get("aop_expert", "")
    chemical = state.get("chemical", "")
    admet_results = state["data"].get("admet_results", "")

    messages = [SystemMessage(content=f"""
    You are an expert in AOP (Adverse Outcome Pathways) and toxicology. Your task is to analyze the provided chemical 
    information and generate a comprehensive AOP profile for the given chemical: {chemical} by predicting potential key events and 
    adverse outcomes based on the chemical's properties and known biological interactions.
    
    ADMET Results: {admet_results}
    {aop_expert}
    """)]

    response = llm.invoke(messages)
    print("AOP Analysis:", response.content)
    
    # Store the AOP results in the state
    state["data"]["aop_results"] = response.content
    
    # Update status to indicate AOP analysis is complete
    state["status"] = "needs_visuals"

    return state


def visuals_agent_node(state: AOPState) -> AOPState:
    visuals_agent = state.get("visuals_agent", "")
    chemical = state.get("chemical", "")
    admet_results = state["data"].get("admet_results", "")
    aop_results = state["data"].get("aop_results", "")

    messages = [SystemMessage(content=f"""
    You are an expert in scientific visualization and data representation. Your task is to create visual representations of 
    the provided chemical information for {chemical}, ADMET profile, and AOP profile. Generate clear and informative visuals, specifically 
    focusing on topological maps.
    
    ADMET Results: {admet_results}
    AOP Results: {aop_results}
    {visuals_agent}
    """)]

    response = llm.invoke(messages)
    print("Visualization Results:", response.content)
    
    # Store the visualization results in the state
    state["data"]["visualization_results"] = response.content
    
    # Update status to indicate visualization is complete
    state["status"] = "complete"

    return state

# --- Supervisor Agent Node ---
def aop_constructor_supervisor(state: AOPState) -> AOPState:
    aop_constructor = state.get("aop_constructor", "")
    chemical = state.get("chemical", "")

    messages = [SystemMessage(content=f"""
    You are an expert in AOP (Adverse Outcome Pathways) construction and toxicology. Your task is to supervise the AOP 
    construction process by analyzing the provided chemical information for {chemical}, ADMET profile, and AOP profile. You will delegate 
    tasks to the appropriate agents (ADMET MIE, AOP Expert, and Visuals Agent) based on the current state of the workflow
    and serve as a supervisor to ensure the successful completion of the AOP construction process.
    {aop_constructor}
    """)]

    # Determine the next agent based on the state
    if state["status"] == "needs_admet":
        state["next_agent"] = "admet_mie"
    elif state["status"] == "needs_aop":
        state["next_agent"] = "aop_expert"
    elif state["status"] == "needs_visuals":
        state["next_agent"] = "visuals_agent"
    else:
        state["next_agent"] = "end"
    return state





def AOPGuess():


def mie():


def expand_KEs():


def find_candidates():


def find_similar_compounds():






workflow = StateGraph(AOPState)
    
# Add nodes to the graph
workflow.add_node("constructor", aop_constructor_supervisor)
workflow.add_node("admet_mie", admet_mie_node)
workflow.add_node("aop_expert", aop_expert_node)
workflow.add_node("visuals_agent", visuals_agent_node)

# Add edges to the graph, conditional edges 
workflow.add_edge(START, "constructor")
workflow.add_conditional_edges(
    "constructor",
    lambda state: state["next_agent"],
    {
        "admet_mie": "admet_mie",
        "aop_expert": "aop_expert",
        "visuals_agent": "visuals_agent",
        "end": END,
    },
)

workflow.add_edge("admet_mie", "constructor")
workflow.add_edge("aop_expert", "constructor")
workflow.add_edge("visuals_agent", "constructor")

#compile graph

chain = workflow.compile()

# Save results 
def save_results_to_files(result: AOPState):
    """Save the workflow results to files in the output directory."""
    output_dir = Path("/home/avam11/lively-animatronic-llama/output")
    output_dir.mkdir(exist_ok=True)
    
    chemical_name = result["chemical"].replace(" ", "_").lower()
    
    # Save ADMET results
    admet_file = output_dir / f"{chemical_name}_admet_results.json"
    with open(admet_file, "w") as f:
        json.dump({
            "chemical": chemical_name, 
            "admet_results": result["data"].get("admet_results", "N/A"),
            "generated_at": datetime.datetime.now().isoformat()
        }, f, indent=2)
    print(f"ADMET results saved to {admet_file}")
    
    # Save AOP results
    aop_file = output_dir / f"{chemical_name}_aop_results.json"
    with open(aop_file, "w") as f:
        json.dump({
            "chemical": chemical_name, 
            "aop_results": result["data"].get("aop_results", "N/A"),
            "generated_at": datetime.datetime.now().isoformat()
        }, f, indent=2)
    print(f"AOP results saved to {aop_file}")
    
    # Save visualization results
    visuals_file = output_dir / f"{chemical_name}_visualization_results.json"
    with open(visuals_file, "w") as f:
        json.dump({
            "chemical": chemical_name, 
            "visualization_results": result["data"].get("visualization_results", "N/A"),
            "generated_at": datetime.datetime.now().isoformat()
        }, f, indent=2)
    print(f"Visualization results saved to {visuals_file}")


# Prompt the user to enter a chemical name
chemical_name = input("Enter the name of the chemical: ")

# Update the initial state with the user-provided chemical name
initial_state["chemical"] = chemical_name

# Run the workflow
result = chain.invoke(initial_state)

# Save results to files
save_results_to_files(result)

#Print results
print("\n" + "="*80)
print("WORKFLOW COMPLETED SUCCESSFULLY!")
print("="*80)
print(f"\nChemical Analyzed: {result['chemical']}")
print(f"Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n" + "-"*80)
print("SUMMARY OF RESULTS:")
print("-"*80)
print(f"\nADMET Analysis: {'Available' if result['data'].get('admet_results') else 'N/A'}")
print(f"AOP Analysis: {'Available' if result['data'].get('aop_results') else 'N/A'}")
print(f"Visualization: {'Available' if result['data'].get('visualization_results') else 'N/A'}")
print("\n" + "-"*80)
print("FILES GENERATED:")
print("-"*80)
chemical_name = result["chemical"].replace(" ", "_").lower()
print(f"  - {chemical_name}_admet_results.json")
print(f"  - {chemical_name}_aop_results.json")
print(f"  - {chemical_name}_visualization_results.json")
print("\nAll results saved to: /home/avam11/lively-animatronic-llama/output/")
print("="*80 + "\n")
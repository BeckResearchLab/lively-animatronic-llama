#API Keys
from dotenv import load_dotenv
load_dotenv()

import json
import os
import operator
import datetime
from pathlib import Path
from typing import Annotated, TypedDict, Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# --- Structured Output Schemas --- REVIEW THIS
class MIE_Info(BaseModel):
    name: str = Field(description="The name of the Molecular Initiating Event")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0")
    reasoning: str = Field(description="Brief scientific reasoning for this MIE")

class Candidate_Info(BaseModel):
    name: str = Field(description="Name of the compound or event")
    type: str = Field(description="Type of node (MIE, KE, or AO)")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0")
    similarity: Optional[float] = Field(None, description="Similarity score to target chemical (0-1)")

class Candidate_List(BaseModel):
    candidates: List[Candidate_Info] = Field(description="List of generated candidates")

class ADMET_Profile(BaseModel):
    properties: Dict[str, Any] = Field(description="Key properties: LogP, MW, TPSA, Soulbility, etc. Include all properties")
    liabilities: List[str] = Field(description="List of chemical red flags or reactive moieties identified")

class MIE_Mapping(BaseModel):
    predictions: List[MIE_Info] = Field(description="List of MIEs mapped from the ADMET liabilities")


# --- LLM ---
llm = ChatOpenAI(
    model=os.environ.get("OPENAI_MODEL", "gemma-4-31b"),
    temperature=0.4,
    max_tokens=18048,
    api_key=os.environ.get("OPENAI_API_KEY"),
    timeout=4000,
    max_retries=3,
)

# --- Configuration ---
similarity_threshold = 0.5

# --- Define Graph State ---
class AOPState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add] #dictionary of messages input/output
    reference_files: Dict[str, Any] #references the agents
    AOP_pathways: List[List[Dict[str, Any]]] # List of paths, each path is a list of nodes (MIE -> KE -> AO)
    candidates: List[Dict[str, Any]] # Current set of compounds/events under consideration
    chemical: str #input chemical/target
    current_node_type: str # MIE, KE, or AO
    confidence_score: float #confidence of each step in pathway sum
    is_ao_reached: bool #yes or no - if yes, stop
    MIEs: List[MIE_Info] # List of predicted MIEs
    data: Dict[str, Any] # Storage for intermediate data like ADMET profiles


# --- Initial State of Graph ---
initial_state: AOPState = {
    "chemical": "",
    "messages": [],
    "reference_files": {
        "admet_mie": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/admet-mie.md")).read_text(),
        "aop_expert": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/aop-expert.md")).read_text(),
        "visuals_agent": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/visuals-agent.md")).read_text(),
        "constructor": (Path("/home/avam11/lively-animatronic-llama/.opencode/agents/aop-constructor.md")).read_text(),
    },
    "AOP_pathways": [],
    "MIEs": [],
    "candidates": [],
    "current_node_type": "MIE",
    "confidence_score": 0.0,
    "is_ao_reached": False,
    "data": {}
}


# --- Nodes ---
# ADMET_node    AOP_node    candidate_gen_node  expand_and_prune_node   visualize_node

def ADMET_node(state: AOPState) -> AOPState:
    chemical = state.get("chemical", "")
    admet_instructions = state.get("reference_files", {}).get("admet_mie", "Default instructions here")

    if not state.get("MIEs"):
        # --- Call 1: Analyze ADMET of target chemical ---
        # LLM Only allowed to look at chemical properties
        analyst_llm = llm.with_structured_output(ADMET_Profile)
        analyst_prompt = (
            f"{admet_instructions}\n\n"
            f"Analyze chemical properties of {chemical}. "
            "Focus strictly on ADMET properties and identify any structural liabilities."
        )
        #Retrieve Data
        profile_response = analyst_llm.invoke([
            SystemMessage(content="You are a computational chemist specializing in ADMET profiling."),
            HumanMessage(content=analyst_prompt)
        ])
        # Store this profile in state["data"] so it's available for the rest of the graph
        state["data"]["target_profile"] = profile_response.dict()
        # --- CALL 2: MIE Prediction ---
        # This LLM takes the profile as input and maps it to biological events
        mapper_llm = llm.with_structured_output(MIE_Mapping)
    
        # IMPORTANT: We feed the result of Call 1 INTO the prompt for Call 2
        mapper_prompt = (
            f"Based on the following ADMET profile: {json.dumps(profile_response.dict())}\n\n"
            f"Identify the most probable Molecular Initiating Events (MIEs) for {chemical}. "
            "Your predictions must be justified by the liabilities found in the profile."
        )
        mie_response = mapper_llm.invoke([
            SystemMessage(content="You are a toxicologist specializing in AOP MIE mapping."),
            HumanMessage(content=mapper_prompt)
        ])
        # Save the final mapping to state
        state["MIEs"] = mie_response.predictions
        state["current_node_type"] = "MIE"
        
    else:
        # Subsequent analysis: Run ADMET on all current candidates to find most similar to target
        candidates = state.get("candidates", [])
        if not candidates:
            return state #Nothing to compare, skip to next node

        #data generator for structured output/objects, so LLM can read output
        structured_llm = llm.with_structured_output(Candidate_List)  

        prompt = (f"{admet_instructions}\n\n"
            f"Target Chemical: {chemical}\n"
            f"Current Candidates: {json.dumps(candidates)}\n\n"
            "Compare these candidates against the target chemical using ADMET profiles. Assign a similarity score between 0.0 and 1.0 "
            "based on their pharmacokinetic and toxicological overlap. Return a structured list of all candidates with their scores. "
            "ONLY INCLUDE CANDIDATES WITH A SCORE OF {similarity_threshold} OR HIGHER.")
        
        response = structured_llm.invoke([SystemMessage(content="You are an expert in ADMET and similarity scoring"), 
                                          HumanMessage(content=prompt)])
        
        # response is now a Candidate_List object, so we convert its candidates to a list of dicts
        state["candidates"] = [c.dict() for c in response.candidates]
        # Log the action to messages for transparency
        state["messages"].append(AIMessage(content=f"Ranked {len(state['candidates'])} candidates by similarity to {chemical}."))


        #     **HERE MAY NEED TO CREATE SIMILARITY SCORING SKILL!!**
    return state



def candidate_gen_node(state: AOPState) -> AOPState:
    current_type = state.get("current_node_type")
    chemical = state.get("chemical", "")
    aop_instructions = state.get("reference_files", {}).get("aop_expert", "You are an AOP expert.")

    # Get the last event in the current pathway to use as context
    last_event = "None"
    if state.get("AOP_pathways") and state["AOP_pathways"][-1]:
        last_event = state["AOP_pathways"][-1][-1].get("event", "None")
    elif state.get("MIEs"):
        # If no pathway yet, use the first predicted MIE
        last_event = state["MIEs"][0].name if state["MIEs"] else "None"

    # If candidates are empty, generate new ones based on current path/MIE
    if not state.get("candidates"):
        structured_llm = llm.with_structured_output(Candidate_List)
        
        prompt = (
            f"{aop_instructions}\n\n"
            f"Target Chemical: {chemical}\n"
            f"Current Pathway State: {state.get('AOP_pathways')}\n"
            f"Last Event ({current_type}): {last_event}\n\n"
            "Based on the target chemical and the last event in the pathway, predict the most likely "
            "next biological steps. If the current event is an MIE, suggest Key Events (KE). "
            "If it is a KE, suggest further KEs or the final Adverse Outcome (AO).\n\n"
            "Provide multiple candidates with scientific reasoning and a confidence score (0.0 to 1.0)."
        )
        
        response = structured_llm.invoke([
            SystemMessage(content="You are a toxicologist specializing in AOP pathway construction."),
            HumanMessage(content=prompt)
        ])
        
        # Store candidates as dicts for the expand_and_prune_node
        state["candidates"] = [c.dict() for c in response.candidates]
        state["messages"].append(AIMessage(content=f"Generated {len(state['candidates'])} potential next steps for {last_event}."))
    
    return state


def expand_and_prune_node(state: AOPState) -> AOPState:
    candidates = state.get("candidates", [])
    if not candidates:
        return state
        
    # Logic: Find highest average similarity, prune losers, keep tied nodes
    # Simplified mock: pick the best candidate based on a simulated 'similarity' or 'confidence'
    best_candidate = max(candidates, key=lambda x: x.get("confidence", 0.5))
    
    # Update path
    current_path = state["AOP_pathways"][-1] if state["AOP_pathways"] else []
    new_node = {"event": best_candidate["name"], "type": best_candidate["type"], "score": best_candidate.get("confidence")}
    
    if not state["AOP_pathways"]:
        state["AOP_pathways"].append([new_node])
    else:
        state["AOP_pathways"][-1].append(new_node)
        
    state["current_node_type"] = best_candidate["type"]
    if best_candidate["type"] == "AO":
        state["is_ao_reached"] = True
        
    return state


def visualize(state: AOPState) -> AOPState:
    vis_instructions = state.get("reference_files", {}).get("visuals_agent", "Generate a topological map of the pathway.")
    prompt = f"{vis_instructions}\n\nGenerate topological map for path: {state.get('AOP_guess')}"
    response = llm.invoke([SystemMessage(content=prompt), HumanMessage(content=state.get('chemical'))])
    state["messages"].append(response)
    return state


def save_results_to_files(result: AOPState):
    output = {
        "chemical": result["chemical"],
        "pathway": result["AOP_guess"],
        "final_ao": result["is_ao_reached"]
    }
    with open("aop_results.json", "w") as f:
        json.dump(output, f, indent=4)
workflow = StateGraph(AOPState)
    
# Define routing logic
def route_expansion(state: AOPState):
    if state.get("is_ao_reached"):
        return "visualize"
    # Loop back to ADMET to refine based on new candidates
    return "ADMET"

# Add nodes to the graph
workflow.add_node("ADMET", ADMET_node)
workflow.add_node("AOP", AOP_node)
workflow.add_node("candidate_gen", candidate_gen_node)
workflow.add_node("expand", expand_and_prune_node)
workflow.add_node("visualize", visualize)

# Add edges
workflow.add_edge(START, "ADMET")
workflow.add_edge("ADMET", "AOP")
workflow.add_edge("AOP", "candidate_gen")
workflow.add_edge("candidate_gen", "expand")
workflow.add_conditional_edges("expand", route_expansion)
workflow.add_edge("visualize", END)


# compile graph
chain = workflow.compile()

# Save results 


# Prompt the user to enter a chemical name
chemical_name = input("Enter the name of the chemical: ")

# Update the initial state with the user-provided chemical name
initial_state["chemical"] = chemical_name

# Run the workflow
result = chain.invoke(initial_state)

# Save results to files
save_results_to_files(result)
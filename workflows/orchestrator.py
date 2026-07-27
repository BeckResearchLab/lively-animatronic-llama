from __future__ import annotations

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import os
from typing import Annotated, List, Dict, Any
import json
import re
import asyncio

# IMPORTANT: ORCHESTRATOR DESIGN PRINCIPLE
# The orchestrator MUST NEVER create topological maps itself. ALL map generation is delegated to the visuals-agent.

# Load agent instructions
with open('/home/avam11/lively-animatronic-llama/.opencode/agents/admet-mie.md', 'r') as f:
    admet_mie_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/aop-constructor.md', 'r') as f:
    aop_constructor_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/aop-expert.md', 'r') as f:
    aop_expert_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/visuals-agent.md', 'r') as f:
    visuals_agent_instructions = f.read()

# Initialize LLM with better configuration
llm = ChatOpenAI(
    model="gemma-4-31b", 
    temperature=0.7, 
    max_tokens=2048,  # Increased token limit for better responses
    api_key=os.environ.get("OPENAI_API_KEY"),
    timeout=4000,
    max_retries=3  # Increased max retries
)

def extract_potential_miess(molecule: str, admet_analysis: str) -> list:
    """
    Extract potential MIEs from ADMET analysis using structured parsing.
    """
    try:
        # Extract ADMET predictions from the analysis text
        admet_predictions = extract_admet_predictions(admet_analysis)
        
        # Create a simple MIE mapping based on ADMET properties
        potential_miess = []
        
        # Map common ADMET issues to potential MIEs
        if admet_predictions.get('toxicity'):
            toxicity_data = admet_predictions['toxicity']
            for key, value in toxicity_data.items():
                if 'high' in value.lower() or 'positive' in value.lower():
                    potential_miess.append({
                        'mie_id': f'TOX-{key.upper()}',
                        'description': f'High {key} toxicity identified',
                        'severity': 'high',
                        'confidence': 0.8
                    })
        
        if admet_predictions.get('metabolism'):
            metabolism_data = admet_predictions['metabolism']
            for key, value in metabolism_data.items():
                if 'poor' in value.lower() or 'unstable' in value.lower():
                    potential_miess.append({
                        'mie_id': f'MET-{key.upper()}',
                        'description': f'Poor {key} metabolism identified',
                        'severity': 'medium',
                        'confidence': 0.7
                    })
        
        return potential_miess
    except Exception as e:
        print(f"Error extracting potential MIEs: {e}")
        return []


def extract_key_events(molecule: str, admet_analysis: str) -> list:
    """
    Extract key events from ADMET analysis.
    """
    try:
        # Extract ADMET predictions from the analysis text
        admet_predictions = extract_admet_predictions(admet_analysis)
        
        # Create a simple key event mapping based on ADMET properties
        key_events = []
        
        # Map common ADMET issues to key events
        if admet_predictions.get('toxicity'):
            toxicity_data = admet_predictions['toxicity']
            for key, value in toxicity_data.items():
                if 'high' in value.lower() or 'positive' in value.lower():
                    key_events.append({
                        'ke_id': f'KE-TOX-{key.upper()}',
                        'description': f'Toxic effect: {key} toxicity leads to cellular damage',
                        'biological_plausibility': 'high',
                        'confidence': 0.8
                    })
        
        if admet_predictions.get('metabolism'):
            metabolism_data = admet_predictions['metabolism']
            for key, value in metabolism_data.items():
                if 'poor' in value.lower() or 'unstable' in value.lower():
                    key_events.append({
                        'ke_id': f'KE-MET-{key.upper()}',
                        'description': f'Metabolic issue: {key} metabolism leads to accumulation',
                        'biological_plausibility': 'medium',
                        'confidence': 0.7
                    })
        
        return key_events
    except Exception as e:
        print(f"Error extracting key events: {e}")
        return []


def extract_admet_predictions(admet_analysis: str) -> dict:
    """
    Extract structured ADMET predictions from analysis text.
    """
    try:
        # This is a simplified extraction - in a real implementation
        # this would use proper NLP or structured parsing
        predictions = {}
        
        # Simple pattern matching for ADMET properties
        lines = admet_analysis.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Detect section headers
            if line.lower().startswith('absorption:'):
                current_section = 'absorption'
                predictions['absorption'] = {}
            elif line.lower().startswith('distribution:'):
                current_section = 'distribution'
                predictions['distribution'] = {}
            elif line.lower().startswith('metabolism:'):
                current_section = 'metabolism'
                predictions['metabolism'] = {}
            elif line.lower().startswith('excretion:'):
                current_section = 'excretion'
                predictions['excretion'] = {}
            elif line.lower().startswith('toxicity:'):
                current_section = 'toxicity'
                predictions['toxicity'] = {}
            elif line.lower().startswith('drug-likeness:'):
                current_section = 'drug_likeness'
                predictions['drug_likeness'] = {}
            
            # Extract values from lines
            if current_section:
                if ':' in line and not line.startswith('*') and not line.startswith('-'):
                    key, value = line.split(':', 1)
                    key = key.strip().lower().replace(' ', '_')
                    value = value.strip()
                    if current_section == 'drug_likeness':
                        predictions['drug_likeness'][key] = value
                    else:
                        predictions[current_section][key] = value
        
        return predictions
    except Exception as e:
        print(f"Error extracting ADMET predictions: {e}")
        return {}


# Define tools for agentic workflow
@tool
async def run_admet_secondary_scoring(admet_predictions: str) -> str:
    """
    Run ADMET secondary scoring on predictions using the admet-secondary-scoring skill.
    
    Args:
        admet_predictions: JSON string containing ADMET predictions
        
    Returns:
        JSON string containing secondary scoring results
    """
    try:
        # Import the secondary scoring functions directly from local files
        import sys
        sys.path.append('/home/avam11/lively-animatronic-llama/important-info')
        from score_admet_secondary_buckets import analyze_record, load_json
        from admet_secondary_bucket_mapping import load_config
        
        # Load the predictions and configuration
        predictions = json.loads(admet_predictions)
        cfg = load_config()
        
        # Call the scoring function directly
        result = analyze_record(predictions, cfg)
        return json.dumps({"success": True, "results": [result]})
        
    except Exception as e:
        return json.dumps({"error": str(e), "success": False})


@tool
async def identify_potential_miess_tool(molecule: str, admet_analysis: str) -> str:
    """
    Identify potential MIEs from ADMET analysis using structured parsing.
    
    Args:
        molecule: Name of the molecule being analyzed
        admet_analysis: Text analysis of ADMET properties
        
    Returns:
        JSON string containing identified potential MIEs
    """
    try:
        # Import the MIE mapping functions directly from local files
        import sys
        sys.path.append('/home/avam11/lively-animatronic-llama/important-info')
        from admet_ai_mie_to_aopwiki_map import load_mapping_files, map_to_miess
        
        # Extract ADMET predictions from the analysis text (simplified parsing)
        # In a real implementation, this would use proper NLP or structured parsing
        admet_predictions = extract_admet_predictions(admet_analysis)
        
        # Load MIE mappings
        mie_mapping, aop_mapping = load_mapping_files()
        
        # Map to potential MIEs
        result = map_to_miess(admet_predictions, mie_mapping)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e), "success": False})


@tool
async def extract_admet_predictions_tool(admet_analysis: str) -> str:
    """
    Extract structured ADMET predictions from analysis text.
    
    Args:
        admet_analysis: Text analysis of ADMET properties
        
    Returns:
        JSON string containing extracted ADMET predictions
    """
    try:
        # Use the internal extraction function as a fallback
        # In a real implementation, this would use the admet-extraction skill
        result = extract_admet_predictions(admet_analysis)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e), "success": False})


async def admet_mie_agent(state: Annotated[dict, "State"]) -> Annotated[dict, "State"]:
    """ADMET and MIE analysis agent with confidence scoring and looping"""
    molecule = state["molecule"]
    
    try:
        # Import confidence scoring and similarity comparison
        from confidence_scoring import confidence_scorer
        from similar_molecule_comparison import similarity_comparator
        
        # Create system message
        system_message = SystemMessage(content=admet_mie_instructions)
        
        # Get ADMET analysis from LLM
        response = llm.invoke([
            system_message, 
            f"Analyze the molecule {molecule} for ADMET properties and potential molecular initiating events. "
            f"Provide a comprehensive analysis including absorption, distribution, metabolism, excretion, and toxicity. "
            f"Identify specific molecular initiating events (MIEs) that this molecule may trigger. "
            f"Include detailed analysis of the following:"
            f"1. Absorption: intestinal absorption, skin permeability, blood-brain barrier penetration"
            f"2. Distribution: plasma protein binding, volume of distribution, tissue specificity"
            f"3. Metabolism: cytochrome P450 interactions, metabolic stability, phase I and II metabolism"
            f"4. Excretion: renal clearance, biliary excretion, half-life"
            f"5. Toxicity: genotoxicity, carcinogenicity, hepatotoxicity, cardiotoxicity, nephrotoxicity"
            f"6. Drug-likeness: Lipinski's rule of five, QED score, synthetic accessibility"
            f"7. Pharmacokinetic properties: bioavailability, clearance rate, steady-state volume"
            f"8. Potential off-target effects and drug-drug interactions"
            f"9. Environmental impact and ecological toxicity"
            f"10. Confidence levels for each prediction based on data availability"
        ])
        
        # Identify potential MIEs using the internal function
        potential_miess = extract_potential_miess(molecule, response.content)
        
        # Find and compare similar molecules
        similar_molecules = similarity_comparator.find_similar_molecules(molecule)
        comparison_result = similarity_comparator.compare_mie_profiles(potential_miess, similar_molecules)
        
        # Calculate confidence scores
        confidence_scores = {}
        for mie in potential_miess:
            confidence_scores[mie.get('mie_id', 'unknown')] = confidence_scorer.calculate_mie_confidence(mie)
        
        return {
            "admet_analysis": response.content,
            "potential_miess": potential_miess,
            "similar_molecule_comparison": {
                "similar_molecules": [{
                    "name": mol.name,
                    "smiles": mol.smiles,
                    "similarity": mol.similarity_score,
                    "known_miess": mol.known_miess
                } for mol in similar_molecules],
                "comparison_result": {
                    "mie_consistency_score": comparison_result.mie_consistency_score,
                    "adjusted_confidence": comparison_result.adjusted_confidence,
                    "notes": comparison_result.comparison_notes
                }
            },
            "confidence_scores": confidence_scores
        }
    except Exception as e:
        error_msg = f"Error in ADMET/MIE analysis: {str(e)}"
        print(error_msg)
        return {"admet_analysis": error_msg, "potential_miess": [], "confidence_scores": {}}

async def ke_processing_agent(state: Annotated[dict, "State"]) -> Annotated[dict, "State"]:
    """Key Event processing agent with ADMET validation and confidence scoring"""
    molecule = state["molecule"]
    admet_analysis = state["admet_analysis"]
    potential_miess = state.get("potential_miess", [])
    confidence_scores = state.get("confidence_scores", {})
    
    try:
        # Import confidence scoring
        from confidence_scoring import confidence_scorer
        
        # Create system message
        system_message = SystemMessage(content=aop_expert_instructions)
        
        # Get KE analysis from LLM
        response = llm.invoke([
            system_message, 
            f"Based on this comprehensive ADMET analysis for {molecule} and potential MIEs: {admet_analysis}, "
            f"identify and validate Key Events (KEs) that follow from the Molecular Initiating Events. "
            f"Include detailed information about the biological plausibility and confidence for each KE. "
            f"Format the response clearly with proper section headers. "
            f"Pay special attention to the toxicity profiles and metabolic pathways identified in the ADMET analysis. "
            f"Use the following potential MIEs as starting points: "
            f"{json.dumps(potential_miess, indent=2)}"
        ])
        
        # Parse and structure KE data using the internal function
        key_events = extract_key_events(molecule, response.content)
        
        # Calculate KE confidence scores
        ke_confidence_scores = {}
        for ke in key_events:
            ke_confidence_scores[ke.get('ke_id', 'unknown')] = confidence_scorer.calculate_ke_confidence(ke)
        
        return {
            "key_events": key_events,
            "ke_confidence_scores": ke_confidence_scores,
            "aop_analysis": response.content,
            "admet_analysis": admet_analysis,
            "potential_miess": potential_miess,
            "confidence_scores": confidence_scores
        }
    except Exception as e:
        error_msg = f"Error in KE processing: {str(e)}"
        print(error_msg)
        return {
            "key_events": [],
            "ke_confidence_scores": {},
            "aop_analysis": error_msg,
            "admet_analysis": admet_analysis,
            "potential_miess": potential_miess,
            "confidence_scores": confidence_scores
        }





async def aop_expert_agent(state: Annotated[dict, "State"]) -> Annotated[dict, "State"]:
    """AOP expert agent with confidence-based AO determination"""
    molecule = state["molecule"]
    admet_analysis = state["admet_analysis"]
    key_events = state.get("key_events", [])
    ke_confidence_scores = state.get("ke_confidence_scores", {})
    
    try:
        # Import confidence scoring
        from confidence_scoring import confidence_scorer
        
        # Create system message
        system_message = SystemMessage(content=aop_expert_instructions)
        
        # Get AO analysis from LLM
        response = llm.invoke([
            system_message, 
            f"Based on this comprehensive ADMET analysis for {molecule} and Key Events: {admet_analysis}, "
            f"identify potential adverse outcomes (AOs). Include detailed information about "
            f"the biological plausibility and confidence for each AO. "
            f"Format the response clearly with proper section headers. "
            f"Pay special attention to the toxicity profiles and metabolic pathways identified in the ADMET analysis. "
            f"Use the following Key Events as starting points: "
            f"{json.dumps(key_events, indent=2)}"
        ])
        
        # Parse and structure AO data
        adverse_outcomes = parse_adverse_outcomes(response.content, key_events, ke_confidence_scores)
        
        # Calculate AO confidence scores
        ao_confidence_scores = {}
        for ao in adverse_outcomes:
            ao_confidence_scores[ao.get('ao_id', 'unknown')] = confidence_scorer.calculate_ao_confidence(ao)
        
        # Calculate overall confidence
        overall_confidence = confidence_scorer.calculate_overall_confidence({
            "potential_miess": state.get("potential_miess", []),
            "key_events": key_events,
            "adverse_outcomes": adverse_outcomes
        })
        
        return {
            "adverse_outcomes": adverse_outcomes,
            "ao_confidence_scores": ao_confidence_scores,
            "overall_confidence": overall_confidence,
            "aop_analysis": response.content,
            "admet_analysis": admet_analysis,
            "key_events": key_events,
            "ke_confidence_scores": ke_confidence_scores
        }
    except Exception as e:
        error_msg = f"Error in AOP expert analysis: {str(e)}"
        print(error_msg)
        return {
            "adverse_outcomes": [],
            "ao_confidence_scores": {},
            "overall_confidence": 0.0,
            "aop_analysis": error_msg,
            "admet_analysis": admet_analysis,
            "key_events": key_events,
            "ke_confidence_scores": ke_confidence_scores
        }

async def visuals_agent(state: Annotated[dict, "State"]):
    """Visualization agent - EXCLUSIVELY handles all topological map generation
    
    CRITICAL: This function is the ONLY place where topological maps are created.
    The orchestrator must NEVER create maps itself - all map generation goes through this agent.
    """
    molecule = state["molecule"]
    aop_analysis = state["aop_analysis"]
    potential_miess = state.get("potential_miess", [])
    key_events = state.get("key_events", [])
    adverse_outcomes = state.get("adverse_outcomes", [])
    
    try:
        # Create system message
        system_message = SystemMessage(content=visuals_agent_instructions)
        
        # Generate visualizations
        response = llm.invoke([
            system_message, 
            f"Create visualizations for this AOP analysis of {molecule}. "
            f"Generate a topological map showing the AOP network with nodes for Stressors, MIEs, KEs, and AOs. "
            f"Save the topological map as {molecule.lower()}_aop_map.png and reference it in your output. "
            f"Include network analysis identifying critical pathways and intervention points. "
            f"Consider the enhanced ADMET analysis to highlight key toxicity pathways and metabolic interactions."
        ])
        
        # Set default map file name
        map_file = f"{molecule.lower()}_aop_map.png"
        
        # Extract map file reference from response if present
        if response.content:
            map_match = re.search(r'([a-zA-Z0-9_-]+\.png|[a-zA-Z0-9_-]+\.jpg|[a-zA-Z0-9_-]+\.jpeg)', response.content)
            if map_match:
                map_file = map_match.group(1)
        
        return {"visualizations": response.content, "map_file": map_file}
    except Exception as e:
        error_msg = f"Error in visualization generation: {str(e)}"
        print(error_msg)
        return {"visualizations": error_msg}

async def aop_constructor_supervisor(state: AgentState) -> AgentState:
    """
    The Agentic Supervisor (AOP Constructor as true supervisor)
    Analyzes state and decides the next agent to invoke.
    """
    molecule = state["molecule"]
    
    # Prepare a summary of current progress for the LLM
    progress = {
        "admet_analysis_complete": bool(state.get("admet_analysis")),
        "miess_identified": len(state.get("potential_miess", [])),
        "key_events_identified": len(state.get("key_events", [])),
        "adverse_outcomes_identified": len(state.get("adverse_outcomes", [])),
        "visualizations_complete": bool(state.get("visualizations")),
        "confidence_scores": state.get("confidence_scores", {}),
        "similarity_consistency": state.get("similar_molecule_comparison", {}).get("comparison_result", {}).get("mie_consistency_score", "N/A")
    }

    system_message = SystemMessage(content=f"{aop_constructor_instructions}\n\n"
                                           "You are the AOP Constructor Supervisor. Your job is to orchestrate the workflow. "
                                           "Analyze the state for biological consistency, logical flow (MIE -> KE -> AO), and confidence levels. "
                                           "If you identify contradictions, low consistency scores from similar molecules, or missing biological links, "
                                           "you MUST route the workflow back to the relevant agent ('admet_mie' or 'ke_processing') for refinement. "
                                           "Respond ONLY with the name of the next node: "
                                           "'admet_mie', 'ke_processing', 'aop_expert', 'visuals', or 'report'. "
                                           "Only respond with 'report' when the entire pathway is biologically plausible, consistent, and high-confidence.")

    user_message = f"Current Progress for {molecule}: {json.dumps(progress)}\n\n" \
                   f"Current AOP Analysis: {state.get('aop_analysis', 'Not started')[:500]}..."

    response = llm.invoke([system_message, user_message])
    next_step = response.content.strip().lower()
    
    # Validate LLM response and use fallback if needed
    valid_nodes = ["admet_mie", "ke_processing", "aop_expert", "visuals", "report"]
    if next_step not in valid_nodes:
        if not state.get("admet_analysis"): next_step = "admet_mie"
        elif not state.get("key_events"): next_step = "ke_processing"
        elif not state.get("adverse_outcomes"): next_step = "aop_expert"
        elif not state.get("visualizations"): next_step = "visuals"
        else: next_step = "report"

    return {"next_step": next_step}

async def visuals_report_agent(state: Annotated[dict, "State"]):
    """Final Report Generator - Visuals Agent creates comprehensive report with visualizations"""
    molecule = state["molecule"]
    admet_analysis = state["admet_analysis"]
    aop_analysis = state["aop_analysis"]
    visualizations = state.get("visualizations", "")
    
    try:
        # Create system message
        system_message = SystemMessage(content=visuals_agent_instructions)
        
        # Generate final report
        response = llm.invoke([
            system_message, 
            f"Create a comprehensive final report for {molecule} using:\n\n" +
            f"**Molecule Information:**\n- Name: {molecule}\n\n" +
            f"**DETAILED ADMET Analysis (ADMET-AI Scoring):**\n" +
            f"Provide an in-depth analysis of ADMET properties including:\n" +
            f"- Absorption: intestinal absorption, skin permeability, blood-brain barrier penetration\n" +
            f"- Distribution: plasma protein binding, volume of distribution, tissue specificity\n" +
            f"- Metabolism: cytochrome P450 interactions, metabolic stability, phase I and II metabolism\n" +
            f"- Excretion: renal clearance, biliary excretion, half-life\n" +
            f"- Toxicity: genotoxicity, carcinogenicity, hepatotoxicity, cardiotoxicity, nephrotoxicity\n" +
            f"- Drug-likeness: Lipinski's rule of five, QED score, synthetic accessibility\n" +
            f"- Pharmacokinetic properties: bioavailability, clearance rate, steady-state volume\n" +
            f"- Potential off-target effects and drug-drug interactions\n" +
            f"- Environmental impact and ecological toxicity\n" +
            f"- Confidence levels for each prediction\n\n" +
            f"{admet_analysis}\n\n" +
            f"**SECONDARY ADMET SCORING ANALYSIS:**\n" +
            f"{secondary_report}\n\n" +
            f"**COMBINED MIE IDENTIFICATION:**\n" +
            f"This analysis combines results from both ADMET-AI scoring and secondary ADMET scoring to identify all probable molecular initiating events (MIEs). " +
            f"The secondary scoring helps identify MIEs that may not be captured by primary ADMET-AI scoring alone. " +
            f"By using both scoring systems in parallel, we ensure comprehensive coverage of potential MIEs for accurate AOP construction.\n\n" +
            f"**AOP Analysis:**\n{aop_analysis}\n\n" +
            f"**Visualizations:**\n{visualizations if visualizations else 'Visualizations are being generated in parallel.'}\n\n" +
            f"Format this as a professional markdown report with clear sections, tables, and proper formatting. " +
            f"Save the final report as {molecule.lower()}_aop_analysis.md. " +
            f"Ensure the ADMET section is comprehensive and well-organized with subsections for each ADMET property. " +
            f"Include both primary ADMET-AI scoring results and secondary ADMET scoring results to find all probable MIEs. " +
            f"Include the topological map image using markdown syntax: `![Topological Map]({molecule.lower()}_aop_map.png)`."
        ])
        
        # Save report to file
        report_filename = f"{molecule.lower()}_aop_analysis.md"
        
        # Add visualization note if available
        if visualizations:
            response.content += f"\n\n**Visualizations:**\nThe visuals agent has generated comprehensive visualizations including topological maps.\n"
        
        with open(report_filename, 'w') as f:
            f.write(response.content)
        
        # Return results
        result = {"final_report": response.content, "report_file": report_filename, "admet_analysis": admet_analysis, "aop_analysis": aop_analysis}
        
        return result
    except Exception as e:
        error_msg = f"Error in report generation: {str(e)}"
        print(error_msg)
        return {"final_report": error_msg, "admet_analysis": admet_analysis, "aop_analysis": aop_analysis}

# Define state
class AgentState(TypedDict):
    molecule: str
    admet_analysis: str
    potential_miess: list
    validated_miess: list
    key_events: list
    adverse_outcomes: list
    confidence_scores: dict
    similar_molecule_comparison: dict
    aop_analysis: str
    visualizations: str
    final_report: str
    report_file: str
    map_file: str
    next_step: str # Added for agentic routing

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("supervisor", aop_constructor_supervisor)
workflow.add_node("admet_mie", admet_mie_agent)
workflow.add_node("ke_processing", ke_processing_agent)
workflow.add_node("aop_expert", aop_expert_agent)
workflow.add_node("visuals", visuals_agent)
workflow.add_node("report", visuals_report_agent)

# Add ToolNode for secondary scoring and other tools
tools = [
    run_admet_secondary_scoring,
    identify_potential_miess_tool,
    extract_admet_predictions_tool
]
workflow.add_node("tools", ToolNode(tools))

# Define agentic routing logic
def route_decision(state: AgentState):
    return state["next_step"]

workflow.set_entry_point("supervisor")

# Supervisor routes to any worker
workflow.add_conditional_edges(
    "supervisor", 
    route_decision, 
    {
        "admet_mie": "admet_mie",
        "ke_processing": "ke_processing",
        "aop_expert": "aop_expert",
        "visuals": "visuals",
        "report": "report"
    }
)

# All workers report back to the supervisor for the next decision
workflow.add_edge("admet_mie", "supervisor")
workflow.add_edge("ke_processing", "supervisor")
workflow.add_edge("aop_expert", "supervisor")
workflow.add_edge("visuals", "supervisor")

# Tools node is used by agents for structured data processing
# Tools are called internally by agents, no direct routing needed
# workflow.add_edge("admet_mie", "tools")
# workflow.add_edge("tools", "admet_mie")

# Final report is the end of the line
workflow.add_edge("report", END)

# Compile the workflow
app = workflow.compile()

if __name__ == "__main__":
    # Get molecule name from user
    molecule_name = input("Enter the name of the chemical/molecule to analyze: ")
    
    # Run workflow
    inputs = {"molecule": molecule_name}
    final_state = app.ainvoke(inputs)
    final_state = asyncio.run(final_state)
    
    # Print completion summary
    print(f"\n{'='*60}")
    print(f"WORKFLOW COMPLETE!")
    print(f"{'='*60}")
    
    # Get file paths
    report_file = final_state.get('report_file', 'N/A')
    map_file = final_state.get('map_file', 'N/A')
    
    print(f"\n📄 MARKDOWN REPORT: {report_file}")
    print(f"🗺️  TOPOLOGICAL MAP: {map_file} (generated by visuals agent)")
    
    # Check file existence
    import os
    if report_file != 'N/A' and os.path.exists(report_file):
        print(f"✅ Markdown report successfully created")
    else:
        print(f"❌ Markdown report NOT found")
    
    if map_file != 'N/A' and os.path.exists(map_file):
        print(f"✅ Topological map created")
        print(f"   File size: {os.path.getsize(map_file)} bytes")
    else:
        print(f"❌ Topological map NOT found")
    
    print(f"\n{'='*60}")
    print("TROUBLESHOOTING:")
    print(f"{'='*60}")
    
    if map_file != 'N/A' and not os.path.exists(map_file):
        print("🔧 Map generation issues:")
        print("   1. Check visuals agent output")
        print("   2. Verify permissions")
        print("   3. Check disk space")
        print("   4. Review error messages")
        print("   5. See TROUBLESHOOTING.md")
    
    print(f"\n{'='*60}")
    print("FINAL REPORT CONTENT:")
    print(f"{'='*60}")
    print(f"\n{final_state['final_report']}")
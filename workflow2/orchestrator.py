from __future__ import annotations

import os
import time
import asyncio
from typing import Any, Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor

from langgraph.graph import END, START, StateGraph

from workflow import (
    AOPState,
    Initial_ADMET_node,
    candidate_gen_node,
    critic_node,
    expand_and_prune_node,
    initial_state,
    visualize,
)
from read_across import enrich_read_across_state
from similarity_scoring import similarity_scoring_node


class WorkflowMonitor:
    """Basic monitoring for workflow execution"""
    
    def __init__(self):
        self.metrics = {
            'node_execution_times': {},
            'node_success_rates': {},
            'total_start_time': None,
            'total_end_time': None,
            'node_call_counts': {}
        }
        self.reset_metrics()
    
    def reset_metrics(self):
        """Reset metrics for a new workflow run"""
        self.metrics['node_execution_times'] = {}
        self.metrics['node_success_rates'] = {}
        self.metrics['node_call_counts'] = {}
        self.metrics['total_start_time'] = time.time()
    
    def track_node_execution(self, node_name: str, execution_time: float, success: bool):
        """Track node performance metrics"""
        # Update execution time (moving average)
        current_time = self.metrics['node_execution_times'].get(node_name, 0)
        count = self.metrics['node_call_counts'].get(node_name, 0) + 1
        self.metrics['node_execution_times'][node_name] = (
            current_time + execution_time
        ) / count
        
        # Update call count
        self.metrics['node_call_counts'][node_name] = count
        
        # Update success rate
        success_count = self.metrics['node_success_rates'].get(node_name, {}).get('success', 0)
        if success:
            success_count += 1
        self.metrics['node_success_rates'][node_name] = {
            'success': success_count,
            'total': count,
            'rate': success_count / count if count > 0 else 0
        }
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current monitoring metrics"""
        self.metrics['total_end_time'] = time.time()
        self.metrics['total_execution_time'] = (
            self.metrics['total_end_time'] - self.metrics['total_start_time']
        )
        return self.metrics
    
    def print_summary(self):
        """Print monitoring summary"""
        metrics = self.get_metrics()
        print("\n" + "="*60)
        print("WORKFLOW MONITORING SUMMARY")
        print("="*60)
        print(f"Total Execution Time: {metrics['total_execution_time']:.2f} seconds")
        print(f"\nNode Performance:")
        for node_name in sorted(metrics['node_execution_times'].keys()):
            exec_time = metrics['node_execution_times'][node_name]
            success_rate = metrics['node_success_rates'][node_name]['rate']
            call_count = metrics['node_call_counts'][node_name]
            print(f"  {node_name:20s} | Time: {exec_time:.3f}s | Success: {success_rate:.1%} | Calls: {call_count}")
        print("="*60 + "\n")


def parallel_candidate_generation(state: AOPState) -> AOPState:
    """Generate candidates in parallel using multiple approaches"""
    def run_candidate_gen(approach_name: str, state_copy: AOPState) -> Tuple[str, AOPState]:
        """Run candidate generation with a specific approach"""
        start_time = time.time()
        try:
            result = candidate_gen_node(state_copy)
            execution_time = time.time() - start_time
            return approach_name, (result, execution_time, True)
        except Exception as e:
            execution_time = time.time() - start_time
            return approach_name, (state_copy, execution_time, False)
    
    # Create copies of state for parallel execution
    state_copies = [state.copy() for _ in range(2)]  # Can extend this number
    
    # Execute in parallel
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(run_candidate_gen, f"approach_{i}", copy)
            for i, copy in enumerate(state_copies)
        ]
        results = [future.result() for future in futures]
    
    # Merge results - take the best candidate list
    best_state = state
    best_confidence = 0
    
    for approach_name, (result_state, exec_time, success) in results:
        if success:
            candidates = result_state.get('candidates', [])
            current_confidence = sum(c.get('confidence', 0) for c in candidates) / max(len(candidates), 1)
            
            if current_confidence > best_confidence:
                best_confidence = current_confidence
                best_state = result_state
    
    return best_state


def enrich_read_across_node(state: AOPState) -> AOPState:
    # Get the chemical from state
    chemical = str(state.get("chemical", "")).strip()
    
    # Create target profile from existing data
    target_profile = state.get("data", {}).get("target_profile", {}) if isinstance(state.get("data", {}), dict) else {}
    mies = state.get("MIEs", []) if isinstance(state.get("MIEs", []), list) else []
    
    # Use a comprehensive database or multiple chemicals for read-across
    # Instead of using just the current chemical's CID, use a broader database
    source = os.environ.get("TOX21_DB_FILE", "tox21_database.csv")
    
    # If no database file exists, try to use the API with a broader approach
    if not os.path.exists(source):
        # For now, use an empty source to get empty results rather than self-matching
        source = None
    
    enrich_read_across_state(
        state,
        source=source,
        top_k=int(os.environ.get("READ_ACROSS_TOP_K", "5"))
    )
    return state


def adaptive_route_after_critic(state: AOPState):
    """Enhanced routing logic based on confidence, pathway state, and complexity"""
    pathway = state.get("AOP_pathways", [])
    confidence = state.get("confidence_score", 0)
    iteration_count = state.get("iteration_count", 0)
    pathway_length = len(pathway)
    
    # Termination conditions
    if state.get("is_ao_reached"):
        return "visualize" if pathway else END
    if state.get("next_action") == "terminate":
        return "visualize" if pathway else END
    if state.get("no_candidate_cycles", 0) >= int(os.environ.get("AOP_NO_CANDIDATE_LIMIT", "2")):
        state["termination_reason"] = state.get("termination_reason") or "No candidates generated after fallback"
        return "visualize" if pathway else END
    if state.get("no_progress_cycles", 0) >= int(os.environ.get("AOP_NO_PROGRESS_LIMIT", "2")):
        state["termination_reason"] = state.get("termination_reason") or "No meaningful pathway progress"
        return "visualize" if pathway else END
    if iteration_count >= int(os.environ.get("AOP_MAX_ITERATIONS", "10")):
        state["termination_reason"] = state.get("termination_reason") or "Maximum iterations reached"
        return "visualize" if pathway else END
    
    # Adaptive routing based on confidence and pathway state
    if confidence > 0.9 and pathway_length >= 5:
        # High confidence with substantial pathway - consider visualization
        return "visualize"
    elif confidence < 0.5 and iteration_count > 3:
        # Low confidence after several iterations - need more data
        return "candidate_gen"
    elif pathway_length < 3 and iteration_count < 2:
        # Early stage - skip similarity scoring for efficiency
        return "candidate_gen"
    elif confidence > 0.7 and pathway_length >= 3:
        # Good confidence with reasonable pathway - can be more selective
        return "candidate_gen"
    else:
        # Default path
        return "candidate_gen"


class AOPOrchestrator:
    def __init__(self, enable_monitoring: bool = True):
        self.graph = self._build_graph()
        self.monitor = WorkflowMonitor() if enable_monitoring else None
        self.enable_monitoring = enable_monitoring

    def _build_graph(self):
        w = StateGraph(AOPState)
        
        # Add nodes with monitoring wrappers if enabled
        if hasattr(self, 'enable_monitoring') and self.enable_monitoring:
            w.add_node("Initial_ADMET", self._monitored_node(Initial_ADMET_node, "Initial_ADMET"))
            w.add_node("read_across", self._monitored_node(enrich_read_across_node, "read_across"))
            w.add_node("candidate_gen", self._monitored_node(parallel_candidate_generation, "candidate_gen"))
            w.add_node("Similarity_Scoring", self._monitored_node(similarity_scoring_node, "Similarity_Scoring"))
            w.add_node("expand", self._monitored_node(expand_and_prune_node, "expand"))
            w.add_node("critic", self._monitored_node(critic_node, "critic"))
            w.add_node("visualize", self._monitored_node(visualize, "visualize"))
        else:
            w.add_node("Initial_ADMET", Initial_ADMET_node)
            w.add_node("read_across", enrich_read_across_node)
            w.add_node("candidate_gen", parallel_candidate_generation)
            w.add_node("Similarity_Scoring", similarity_scoring_node)
            w.add_node("expand", expand_and_prune_node)
            w.add_node("critic", critic_node)
            w.add_node("visualize", visualize)

        w.add_edge(START, "Initial_ADMET")
        w.add_edge("Initial_ADMET", "read_across")
        w.add_edge("read_across", "candidate_gen")
        w.add_edge("candidate_gen", "Similarity_Scoring")
        w.add_edge("Similarity_Scoring", "expand")
        w.add_edge("expand", "critic")
        w.add_conditional_edges("critic", adaptive_route_after_critic)
        w.add_edge("visualize", END)
        return w.compile()
    
    def _monitored_node(self, node_func, node_name: str):
        """Wrapper to monitor node execution"""
        def wrapper(state: AOPState) -> AOPState:
            start_time = time.time()
            try:
                result = node_func(state)
                execution_time = time.time() - start_time
                if self.monitor:
                    self.monitor.track_node_execution(node_name, execution_time, True)
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                if self.monitor:
                    self.monitor.track_node_execution(node_name, execution_time, False)
                raise e
        return wrapper

    def _print_results_summary(self, result: Dict[str, Any]):
        """Print a summary of the AOP results"""
        print("\n" + "="*60)
        print("AOP WORKFLOW RESULTS SUMMARY")
        print("="*60)
        print(f"Chemical: {result.get('chemical', 'Unknown')}")
        print(f"Adverse Outcome Reached: {result.get('is_ao_reached', False)}")
        print(f"Confidence Score: {result.get('confidence_score', 0.0):.3f}")
        print(f"Uncertainty: {result.get('uncertainty', 0.0):.3f}")
        print(f"Decision Risk: {result.get('decision_risk', 'medium').upper()}")
        print(f"Next Action: {result.get('next_action', 'expand')}")
        print(f"Termination Reason: {result.get('termination_reason', 'Unknown')}")
        print(f"Iteration Count: {result.get('iteration_count', 0)}")
        
        pathway = result.get('AOP_pathways', [])
        print(f"\nPathway Length: {len(pathway)}")
        if pathway:
            print("\nPathway Steps:")
            for i, step in enumerate(pathway, 1):
                print(f"  {i}. {step.get('description', 'No description')}")
        
        visualization_path = result.get('data', {}).get('visualization_path', '')
        if visualization_path:
            print(f"\nVisualization saved to: {visualization_path}")
        
        print("="*60 + "\n")

    def run(self, chemical: str) -> Dict[str, Any]:
        if self.enable_monitoring:
            self.monitor.reset_metrics()
        
        state = initial_state()
        state["chemical"] = chemical.strip()
        result = self.graph.invoke(state)
        
        # Save results to files
        from workflow import save_results_to_files
        save_results_to_files(result)
        
        # Print summary of results
        self._print_results_summary(result)
        
        if self.enable_monitoring and self.monitor:
            self.monitor.print_summary()
        
        return result


if __name__ == "__main__":
    import sys
    
    # Check if chemical name is provided as argument
    if len(sys.argv) < 2:
        # Prompt user for chemical name
        chemical = input("Enter the chemical name: ").strip()
        if not chemical:
            print("Error: Chemical name cannot be empty")
            sys.exit(1)
    else:
        chemical = sys.argv[1]
    
    orchestrator = AOPOrchestrator()
    try:
        result = orchestrator.run(chemical)
        print(f"Workflow completed for {chemical}")
    except Exception as e:
        print(f"Error during workflow execution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
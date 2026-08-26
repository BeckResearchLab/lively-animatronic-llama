import os
from dotenv import load_dotenv
from graph import app

os.environ["LANGCHAIN_PROJECT"] = "Multi agent researcher"

def check_api_keys():
    openai_key = os.environ.get("OPENAI_API_KEY")

    if not openai_key:
        print("API key NOT found. Please set OPENAI_API_KEY in your .env file.")
        return False

    return True

def main():
    # Load environment variables
    load_dotenv()

    # Check API keys
    if not check_api_keys():
        return

    print("Multi-Agent Research Assistant CLI")
    print("=" * 50)

    # Get user input
    topic = input("\nEnter your research topic: ").strip()
    if not topic:
        print("Please enter a research topic.")
        return

    max_iterations = input("Enter max workflow iterations (default 15): ").strip()
    max_iterations = int(max_iterations) if max_iterations.isdigit() else 15
    print(f"\n Starting research on: '{topic}'")
    print(f"Max iterations: {max_iterations}\n")

    # Initial state
    initial_state = {
        "main_task": topic,
        "research_findings": [],
        "citations": [],
        "draft": "",
        "critique_notes": "",
        "revision_number": 0,
        "next_step": "",
        "current_sub_task": ""
    }

    # Configuration
    config = {"recursion_limit": max_iterations}

    # Run the workflow
    step_count = 0
    final_state = None
    node_name = None

    all_states = []  # Track all state updates

    try:
        for step in app.stream(initial_state, config=config):
            step_count += 1
            node_name = list(step.keys())[0]  # Define node_name early in loop
            node_output = step[node_name]
            progress = min(step_count / max_iterations, 1.0)
            print(f"\n Progress: {progress:.0%} ({step_count}/{max_iterations})")

            # Store the complete state at each step
            citations = node_output.get('citations', [])
            all_states.append({
                'step': step_count,
                'node': node_name,
                'state': node_output.copy(),  # Store a copy of the node output
                'citations': citations 
            })

            # Keep the most recent complete state
            if final_state is None:
                final_state = node_output
            else:
                final_state.update(node_output)

            # Get node name and output
            node_name = list(step.keys())[0]
            node_output = step[node_name]
            # Store the complete state
            if final_state is None:
                final_state = node_output
            else:
                # Merge the node output into the existing state
                final_state.update(node_output)
            print(f"\n--- Step{step_count}: {node_name.upper()} ---")

            if node_name == "supervisor":
                next_step = node_output.get('next_step', 'N/A')
                task = node_output.get('current_sub_task', 'N/A')
                print(f"Decision: {next_step}")
                print(f"Task: {task}")

            elif node_name == "researcher":
                findings = node_output.get('research_findings', [])
                citations = node_output.get('citations', [])
                if findings:
                    print("Research completed")
                    print(f"Finding: {findings[-1][:200]}...")
                    if citations:
                        print(f"Citations found: {len(citations)}")
                        for cit in citations[:2]:  # Show first 2 citations
                            print(f"  - [{cit.get('citation_id', 'N/A')}] {cit.get('title', 'N/A')[:80]}...")

            elif node_name == "writer":
                draft = node_output.get('draft', '')
                revision = node_output.get('revision_number', 0)
                print(f"Draft {revision} generated ({len(draft)} chars)")
                print(f"Preview: {draft[:200]}...")

            elif node_name == "critiquer":
                critique = node_output.get('critique_notes', '')
                if "APPROVED" in critique.upper():
                    print("Draft APPROVED")
                else:
                    print("Revisions requested")
                print(f"Critique: {critique[:200]}...")

    except Exception as e:
        print(f"\n Error occurred: {str(e)}")
        if node_name:  # Check if node_name is defined
            print(f"Error occurred during: {node_name}")
        # Add more debug info here
        return

    # Display final report - IMPROVED LOGIC
    print("\n" + "=" * 50)
    print("FINAL RESEARCH REPORT EXTRACTION")
    print("=" * 50)

    # Try to get the draft from multiple possible locations
    final_draft = None
    final_citations = []

    # First try final_state
    if final_state and isinstance(final_state, dict):
        final_draft = final_state.get("draft", "")
        final_citations = final_state.get("citations", [])
        print(f"Draft from final_state: {len(final_draft) if final_draft else 0} chars")

        # If draft is just an error message, try to find research findings instead
        if final_draft and ("Error" in final_draft or len(final_draft.strip()) < 100):
            research_findings = final_state.get("research_findings", [])
            if research_findings:
                final_draft = "\n\n".join(research_findings)
                print(f"Using research findings instead: {len(final_draft)} chars")

    # If no draft in final_state, search through all states for the longest draft
    if not final_draft or len(final_draft.strip()) < 100:
        print("Searching for draft in all states...")
        best_draft = None
        best_length = 0
        best_citations = []

        for state_record in reversed(all_states):
            state = state_record['state']
            if isinstance(state, dict):
                # Check for draft in multiple possible fields
                for field in ["draft", "output", "research_findings"]:
                    if field in state:
                        draft_candidate = state[field]
                        if isinstance(draft_candidate, str) and len(draft_candidate.strip()) > best_length:
                            # Skip error messages
                            if "Error" not in draft_candidate and "Please try again" not in draft_candidate:
                                best_draft = draft_candidate
                                best_length = len(draft_candidate)
                                best_citations = state.get("citations", [])
                                print(f"Found better draft in step {state_record['step']} ({state_record['node']}): {best_length} chars")

        if best_draft:
            final_draft = best_draft
            final_citations = best_citations

    if final_draft and len(final_draft.strip()) > 50:
        print("\n" + "=" * 50)
        print("FINAL RESEARCH REPORT")
        print("=" * 50)
        print(final_draft)

        # Statistics
        print("\n" + "=" * 50)
        print("REPORT STATISTICS")
        print("=" * 50)
        print(f"Revisions: {final_state.get('revision_number', 0) if isinstance(final_state, dict) else 0}")
        print(f"Research Sources: {len(final_state.get('research_findings', [])) if isinstance(final_state, dict) else 0}")
        print(f"Word Count: {len(final_draft.split())}")
        print(f"Character Count: {len(final_draft)}")
        print(f"Citations: {len(final_citations)}")

        # Save to file
        filename = f"research_report_{topic.replace(' ', '_')}.md"
        with open(filename, 'w') as f:
            f.write(final_draft)
        print(f"\nReport saved to: {filename}")

    else:
        print("\n❌ No report was generated")
        print(f"Final state: {final_state}")
        print(f"All states recorded: {len(all_states)}")
        # Debug: show all states to help diagnose
        for i, state_record in enumerate(all_states[-5:], 1):  # Show last 5 states
            print(f"\nState {len(all_states) - i + 1}:")
            print(f"  Node: {state_record['node']}")
            print(f"  Keys: {list(state_record['state'].keys())}")
            for key, value in state_record['state'].items():
                if isinstance(value, str) and len(value) > 0:
                    print(f"  {key}: {len(value)} chars - {value[:100]}...")

if __name__ == "__main__":
    main()


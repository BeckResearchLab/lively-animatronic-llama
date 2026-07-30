import numpy as np
import json
import argparse
from typing import Dict, List, Any

def calculate_weighted_cosine_similarity(v1: np.ndarray, v2: np.ndarray, weights: np.ndarray) -> float:
    """Calculates the weighted cosine similarity between two vectors."""
    # Apply weights to vectors
    wv1 = v1 * weights
    wv2 = v2 * weights
    
    norm1 = np.linalg.norm(wv1)
    norm2 = np.linalg.norm(wv2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(wv1, wv2) / (norm1 * norm2)

def compare_admet_profiles(target_profile: Dict[str, float], candidates: List[Dict[str, Any]], weights_dict: Dict[str, float] = None) -> List[Dict[str, Any]]:
    """
    Compares a target ADMET profile against a list of candidate profiles with optional weighting.
    """
    results = []
    for cand in candidates:
        cand_profile = cand['profile']
        
        common_keys = sorted(list(set(target_profile.keys()) & set(cand_profile.keys())))
        
        if not common_keys:
            results.append({
                "id": cand.get("id") or cand.get("name") or cand.get("smiles"),
                "similarity": 0.0,
                "top_divergence": [],
                "note": "No overlapping ADMET endpoints"
            })
            continue
            
        target_vec = np.array([target_profile[k] for k in common_keys])
        cand_vec = np.array([cand_profile[k] for k in common_keys])
        
        # Create weight vector for the common keys
        if weights_dict:
            weights_vec = np.array([weights_dict.get(k, 1.0) for k in common_keys])
            similarity = calculate_weighted_cosine_similarity(target_vec, cand_vec, weights_vec)
        else:
            # Fallback to standard cosine similarity (all weights = 1.0)
            weights_vec = np.ones(len(common_keys))
            similarity = calculate_weighted_cosine_similarity(target_vec, cand_vec, weights_vec)
        
        diffs = {k: abs(target_profile[k] - cand_profile[k]) for k in common_keys}
        top_divergence = sorted(diffs.items(), key=lambda x: x[1], reverse=True)[:3]
        
        results.append({
            "id": cand.get("id") or cand.get("name") or cand.get("smiles"),
            "similarity": float(similarity),
            "top_divergence": top_divergence,
            "common_endpoints_count": len(common_keys)
        })
    
    return sorted(results, key=lambda x: x["similarity"], reverse=True)

def main():
    parser = argparse.ArgumentParser(description="Compare ADMET score similarity between chemicals.")
    parser.add_argument("--target", required=True, help="JSON file containing the target ADMET profile")
    parser.add_argument("--candidates", required=True, help="JSON file containing a list of candidate profiles")
    parser.add_argument("--output", help="Output JSON file for results")
    parser.add_argument("--profile", default="default", help="Weight profile to use (e.g., default, safety, pharmacokinetics)")
    parser.add_argument("--weights-file", default=".opencode/skills/similarity-scoring/config/weights.json", help="Path to weights configuration file")
    
    args = parser.parse_args()
    
    # Load weights
    try:
        with open(args.weights_file, 'r') as f:
            all_weights = json.load(f)
            selected_weights = all_weights.get(args.profile, all_weights.get("default", {}))
    except FileNotFoundError:
        print(f"Warning: Weights file not found at {args.weights_file}. Using uniform weights.")
        selected_weights = {}

    with open(args.target, 'r') as f:
        target_profile = json.load(f)
        
    with open(args.candidates, 'r') as f:
        candidates = json.load(f)
        if candidates and not isinstance(candidates[0], dict) or 'profile' not in candidates[0]:
             candidates = [{"id": f"cand_{i}", "profile": p} for i, p in enumerate(candidates)]

    results = compare_admet_profiles(target_profile, candidates, selected_weights)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

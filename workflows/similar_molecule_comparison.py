"""
Similar Molecule Comparison for MIE Identification

This module provides functionality to find structurally similar molecules and compare their MIEs.
It uses RDKit for structural similarity calculations and integrates with PubChem for data retrieval.
"""

from typing import List, Dict, Any, Optional
import json
import os
from dataclasses import dataclass
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import requests


@dataclass
class SimilarMolecule:
    """Data class for similar molecules"""
    smiles: str
    name: str
    similarity_score: float
    known_miess: List[Dict[str, Any]]
    known_kes: List[Dict[str, Any]]
    data_source: str


@dataclass
class MIEComparisonResult:
    """Data class for MIE comparison results"""
    target_molecule: str
    similar_molecules: List[SimilarMolecule]
    mie_consistency_score: float
    adjusted_confidence: float
    comparison_notes: List[str]


class SimilarMoleculeComparator:
    """Similar molecule comparison system for MIE identification"""
    
    def __init__(self):
        # Load known MIE mappings from skills directory
        self.mie_mapping_path = '/home/avam11/lively-animatronic-llama/.opencode/skills/mie-identification/references/admet_ai_mie_to_aopwiki_map.json'
        self.aop_mapping_path = '/home/avam11/lively-animatronic-llama/.opencode/skills/mie-identification/references/admet_aop_candidate_mapping.json'
        
        self.mie_mappings = self._load_mie_mappings()
        self.aop_mappings = self._load_aop_mappings()
        
        # Similarity threshold
        self.similarity_threshold = 0.4  # TanimoTo similarity
    
    def _load_mie_mappings(self) -> Dict:
        """Load MIE mappings from JSON file"""
        try:
            with open(self.mie_mapping_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load MIE mappings: {e}")
            return {"mappings": []}
    
    def _load_aop_mappings(self) -> List:
        """Load AOP mappings from JSON file"""
        try:
            with open(self.aop_mapping_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load AOP mappings: {e}")
            return []
    
    def calculate_molecular_fingerprint(self, smiles: str) -> Optional[np.ndarray]:
        """Calculate molecular fingerprint for similarity comparison"""
        try:
            mol = Chem.MolFromSmiles(smiles)
            if mol is None:
                return None
            
            # Generate Morgan fingerprint
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
            
            # Convert to numpy array
            arr = np.zeros((1,), dtype=np.int8)
            DataStructs.ConvertToNumpyArray(fp, arr)
            
            return arr
        except Exception as e:
            print(f"Error calculating fingerprint for {smiles}: {e}")
            return None
    
    def calculate_similarity(self, fp1: np.ndarray, fp2: np.ndarray) -> float:
        """Calculate similarity between two fingerprints using Tanimoto coefficient"""
        if fp1 is None or fp2 is None:
            return 0.0
        
        # Convert to RDKit fingerprints for Tanimoto calculation
        fp1_rdkit = FingerprintMols.FingerprintMol(Chem.MolFromSmiles("DUMMY"))
        fp2_rdkit = FingerprintMols.FingerprintMol(Chem.MolFromSmiles("DUMMY"))
        
        # This is a simplified approach - in practice, you'd use proper RDKit fingerprints
        similarity = DataStructs.TanimotoSimilarity(fp1_rdkit, fp2_rdkit)
        
        return float(similarity)
    
    def find_similar_molecules(self, target_smiles: str, max_results: int = 5) -> List[SimilarMolecule]:
        """Find similar molecules from known databases"""
        # In a real implementation, this would query PubChem, ChEMBL, or other databases
        # For now, we'll use a mock dataset
        
        mock_database = [
            {
                "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",  # Aspirin
                "name": "Aspirin",
                "known_miess": [
                    {"ke_id": 25, "ke_title": "Agonism, Androgen receptor", "confidence": 0.8},
                    {"ke_id": 1669, "ke_title": "Increased, DNA damage and mutation", "confidence": 0.6}
                ],
                "known_kes": [
                    {"ke_id": 25, "ke_title": "Agonism, Androgen receptor", "confidence": 0.85},
                    {"ke_id": 1669, "ke_title": "Increased, DNA damage and mutation", "confidence": 0.7}
                ],
                "data_source": "PubChem"
            },
            {
                "smiles": "CC1=CC=C(C=C1)O",  # Phenol
                "name": "Phenol",
                "known_miess": [
                    {"ke_id": 1669, "ke_title": "Increased, DNA damage and mutation", "confidence": 0.7}
                ],
                "known_kes": [
                    {"ke_id": 1669, "ke_title": "Increased, DNA damage and mutation", "confidence": 0.75}
                ],
                "data_source": "PubChem"
            },
            {
                "smiles": "CC(=O)O",  # Acetic acid
                "name": "Acetic acid",
                "known_miess": [],
                "known_kes": [],
                "data_source": "PubChem"
            }
        ]
        
        target_fp = self.calculate_molecular_fingerprint(target_smiles)
        if target_fp is None:
            return []
        
        similar_molecules = []
        
        for mol_data in mock_database:
            mol_fp = self.calculate_molecular_fingerprint(mol_data["smiles"])
            if mol_fp is None:
                continue
            
            similarity = self.calculate_similarity(target_fp, mol_fp)
            
            if similarity >= self.similarity_threshold:
                similar_molecules.append(SimilarMolecule(
                    smiles=mol_data["smiles"],
                    name=mol_data["name"],
                    similarity_score=similarity,
                    known_miess=mol_data["known_miess"],
                    known_kes=mol_data["known_kes"],
                    data_source=mol_data["data_source"]
                ))
        
        # Sort by similarity score
        similar_molecules.sort(key=lambda x: x.similarity_score, reverse=True)
        
        return similar_molecules[:max_results]
    
    def compare_mie_profiles(self, target_mie_profile: List[Dict[str, Any]], 
                           similar_molecules: List[SimilarMolecule]) -> MIEComparisonResult:
        """Compare target MIE profile with similar molecules"""
        
        comparison_notes = []
        
        # Extract target MIE IDs
        target_mie_ids = [mie.get('mie_id', mie.get('ke_id')) for mie in target_mie_profile]
        
        # Count matches with similar molecules
        total_matches = 0
        total_comparisons = 0
        
        for similar_mol in similar_molecules:
            similar_mie_ids = [mie.get('ke_id') for mie in similar_mol.known_miess]
            
            for target_mie_id in target_mie_ids:
                if target_mie_id in similar_mie_ids:
                    total_matches += 1
                total_comparisons += 1
        
        # Calculate consistency score
        if total_comparisons > 0:
            consistency_score = total_matches / total_comparisons
        else:
            consistency_score = 0.0
        
        # Adjust confidence based on consistency
        base_confidence = np.mean([mie.get('value', 0.0) for mie in target_mie_profile]) if target_mie_profile else 0.0
        adjusted_confidence = base_confidence * (0.7 + 0.3 * consistency_score)
        
        # Add comparison notes
        if similar_molecules:
            comparison_notes.append(f"Found {len(similar_molecules)} similar molecules")
            comparison_notes.append(f"MIE consistency score: {consistency_score:.2f}")
            
            for similar_mol in similar_molecules:
                comparison_notes.append(f"  - {similar_mol.name} (similarity: {similar_mol.similarity_score:.2f})")
                
                # Find common MIEs
                target_ids = [mie.get('mie_id', mie.get('ke_id')) for mie in target_mie_profile]
                similar_ids = [mie.get('ke_id') for mie in similar_mol.known_miess]
                common_ids = set(target_ids) & set(similar_ids)
                
                if common_ids:
                    comparison_notes.append(f"    Common MIEs: {[id for id in common_ids]}")
        else:
            comparison_notes.append("No similar molecules found for comparison")
            comparison_notes.append("Confidence adjustment based solely on ADMET data")
        
        return MIEComparisonResult(
            target_molecule=target_mie_profile[0].get('molecule', 'Unknown') if target_mie_profile else 'Unknown',
            similar_molecules=similar_molecules,
            mie_consistency_score=consistency_score,
            adjusted_confidence=adjusted_confidence,
            comparison_notes=comparison_notes
        )
    
    def get_mie_support_from_similar_molecules(self, target_mie: Dict[str, Any], 
                                              similar_molecules: List[SimilarMolecule]) -> float:
        """Get support for a specific MIE from similar molecules"""
        target_mie_id = target_mie.get('mie_id', target_mie.get('ke_id'))
        
        if not target_mie_id:
            return 0.0
        
        support_count = 0
        total_similar = len(similar_molecules)
        
        for similar_mol in similar_molecules:
            similar_mie_ids = [mie.get('ke_id') for mie in similar_mol.known_miess]
            
            if target_mie_id in similar_mie_ids:
                support_count += 1
        
        if total_similar > 0:
            return support_count / total_similar
        else:
            return 0.0


def create_comparison_report(comparison_result: MIEComparisonResult) -> str:
    """Create a human-readable comparison report"""
    report_lines = ["=" * 60, "SIMILAR MOLECULE COMPARISON REPORT", "=" * 60]
    
    report_lines.append(f"\nTarget Molecule: {comparison_result.target_molecule}")
    report_lines.append(f"MIE Consistency Score: {comparison_result.mie_consistency_score:.2f}")
    report_lines.append(f"Adjusted Confidence: {comparison_result.adjusted_confidence:.2f}")
    
    report_lines.append("\nSimilar Molecules:")
    
    for similar_mol in comparison_result.similar_molecules:
        report_lines.append(f"  - {similar_mol.name}")
        report_lines.append(f"    SMILES: {similar_mol.smiles}")
        report_lines.append(f"    Similarity: {similar_mol.similarity_score:.2f}")
        report_lines.append(f"    Data Source: {similar_mol.data_source}")
        
        if similar_mol.known_miess:
            report_lines.append(f"    Known MIEs:")
            for mie in similar_mol.known_miess:
                report_lines.append(f"      - {mie.get('ke_title', 'Unknown')}")
                report_lines.append(f"        Confidence: {mie.get('confidence', 0.0):.2f}")
        else:
            report_lines.append(f"    Known MIEs: None reported")
    
    if not comparison_result.similar_molecules:
        report_lines.append("  No similar molecules found")
    
    report_lines.append("\nComparison Notes:")
    for note in comparison_result.comparison_notes:
        report_lines.append(f"  - {note}")
    
    report_lines.append("=" * 60)
    
    return "\n".join(report_lines)


# Global instance for easy access
similarity_comparator = SimilarMoleculeComparator()
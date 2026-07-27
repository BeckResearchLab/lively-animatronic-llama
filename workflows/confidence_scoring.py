"""
Confidence Scoring System for AOP Workflow

This module provides centralized confidence scoring functionality for the AOP workflow.
It handles confidence calculation, threshold management, and decision making based on confidence scores.
"""

from typing import List, Dict, Any, Optional
import json
import os
from dataclasses import dataclass
from enum import Enum


class ConfidenceLevel(Enum):
    """Confidence level enumeration"""
    LOW = 0.3
    MEDIUM = 0.6
    HIGH = 0.8
    VERY_HIGH = 0.9


@dataclass
class ConfidenceScore:
    """Data class for confidence scores"""
    value: float
    level: ConfidenceLevel
    description: str
    
    def __init__(self, value: float, description: str = ""):
        self.value = max(0.0, min(1.0, value))  # Clamp between 0 and 1
        self.level = self._determine_level()
        self.description = description
    
    def _determine_level(self) -> ConfidenceLevel:
        """Determine confidence level based on value"""
        if self.value >= ConfidenceLevel.VERY_HIGH.value:
            return ConfidenceLevel.VERY_HIGH
        elif self.value >= ConfidenceLevel.HIGH.value:
            return ConfidenceLevel.HIGH
        elif self.value >= ConfidenceLevel.MEDIUM.value:
            return ConfidenceLevel.MEDIUM
        else:
            return ConfidenceLevel.LOW
    
    def is_above_threshold(self, threshold: float) -> bool:
        """Check if confidence is above threshold"""
        return self.value >= threshold


class ConfidenceScorer:
    """Centralized confidence scoring system"""
    
    def __init__(self):
        self.confidence_thresholds = {
            'mie_identification': 0.7,
            'mie_validation': 0.6,
            'ke_identification': 0.7,
            'ke_validation': 0.6,
            'ao_identification': 0.6,
            'overall_workflow': 0.5
        }
        
        # Load confidence weights from configuration
        self.confidence_weights = self._load_confidence_weights()
    
    def _load_confidence_weights(self) -> Dict[str, float]:
        """Load confidence weights from configuration file"""
        default_weights = {
            'admet_data': 0.4,
            'similar_molecule_comparison': 0.3,
            'mapping_confidence': 0.2,
            'experimental_data': 0.5,  # If available
            'literature_support': 0.2
        }
        
        config_path = 'workflows/confidence_weights.json'
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print(f"Warning: Could not load confidence weights from {config_path}")
        
        return default_weights
    
    def calculate_mie_confidence(self, mie_data: Dict[str, Any]) -> ConfidenceScore:
        """Calculate confidence score for a Molecular Initiating Event"""
        admet_probability = mie_data.get('value', 0.0)
        mapping_confidence = mie_data.get('confidence', 1.0)
        similar_molecule_support = mie_data.get('similar_molecule_support', 1.0)
        
        # Weighted combination
        weighted_score = (
            self.confidence_weights['admet_data'] * admet_probability +
            self.confidence_weights['mapping_confidence'] * mapping_confidence +
            self.confidence_weights['similar_molecule_comparison'] * similar_molecule_support
        )
        
        description = f"MIE confidence based on ADMET probability ({admet_probability:.2f}), mapping confidence ({mapping_confidence:.2f}), and similar molecule support ({similar_molecule_support:.2f})"
        
        return ConfidenceScore(weighted_score, description)
    
    def calculate_ke_confidence(self, ke_data: Dict[str, Any]) -> ConfidenceScore:
        """Calculate confidence score for a Key Event"""
        mie_confidence = ke_data.get('mie_confidence', 0.0)
        admet_support = ke_data.get('admet_support', 0.0)
        biological_plausibility = ke_data.get('biological_plausibility', 0.8)
        
        # Weighted combination
        weighted_score = (
            0.5 * mie_confidence +  # MIE confidence is most important
            0.3 * admet_support +    # ADMET support
            0.2 * biological_plausibility  # Biological plausibility
        )
        
        description = f"KE confidence based on MIE confidence ({mie_confidence:.2f}), ADMET support ({admet_support:.2f}), and biological plausibility ({biological_plausibility:.2f})"
        
        return ConfidenceScore(weighted_score, description)
    
    def calculate_ao_confidence(self, ao_data: Dict[str, Any]) -> ConfidenceScore:
        """Calculate confidence score for an Adverse Outcome"""
        ke_confidences = ao_data.get('ke_confidences', [])
        biological_plausibility = ao_data.get('biological_plausibility', 0.7)
        
        if not ke_confidences:
            return ConfidenceScore(0.0, "No KE support for AO")
        
        # Average KE confidence
        avg_ke_confidence = sum(ke_confidences) / len(ke_confidences)
        
        # Weighted combination
        weighted_score = 0.7 * avg_ke_confidence + 0.3 * biological_plausibility
        
        description = f"AO confidence based on average KE confidence ({avg_ke_confidence:.2f}) and biological plausibility ({biological_plausibility:.2f})"
        
        return ConfidenceScore(weighted_score, description)
    
    def calculate_overall_confidence(self, workflow_results: Dict[str, Any]) -> ConfidenceScore:
        """Calculate overall confidence score for the entire workflow"""
        mie_confidences = [self.calculate_mie_confidence(mie).value 
                          for mie in workflow_results.get('potential_miess', [])]
        ke_confidences = [self.calculate_ke_confidence(ke).value 
                         for ke in workflow_results.get('key_events', [])]
        ao_confidences = [self.calculate_ao_confidence(ao).value 
                         for ao in workflow_results.get('adverse_outcomes', [])]
        
        if not mie_confidences:
            return ConfidenceScore(0.0, "No MIE data available")
        
        # Weighted average of all confidence scores
        avg_mie_conf = sum(mie_confidences) / len(mie_confidences) if mie_confidences else 0
        avg_ke_conf = sum(ke_confidences) / len(ke_confidences) if ke_confidences else 0
        avg_ao_conf = sum(ao_confidences) / len(ao_confidences) if ao_confidences else 0
        
        # Overall confidence is weighted by importance
        overall_score = (
            0.4 * avg_mie_conf +  # MIEs are foundational
            0.3 * avg_ke_conf +    # KEs build on MIEs
            0.2 * avg_ao_conf +    # AOs are the final outcome
            0.1 * self._assess_workflow_completeness(workflow_results)  # Completeness bonus
        )
        
        description = f"Overall confidence: MIE ({avg_mie_conf:.2f}), KE ({avg_ke_conf:.2f}), AO ({avg_ao_conf:.2f})"
        
        return ConfidenceScore(overall_score, description)
    
    def _assess_workflow_completeness(self, workflow_results: Dict[str, Any]) -> float:
        """Assess workflow completeness as a confidence factor"""
        completeness_score = 0.0
        
        # Check if we have data at each stage
        if workflow_results.get('potential_miess'):
            completeness_score += 0.3
        if workflow_results.get('key_events'):
            completeness_score += 0.3
        if workflow_results.get('adverse_outcomes'):
            completeness_score += 0.3
        if workflow_results.get('similar_molecule_comparison'):
            completeness_score += 0.1
        
        return completeness_score
    
    def should_loop_mie(self, current_confidence: float) -> bool:
        """Determine if MIE-ADMET loop should continue"""
        return current_confidence < self.confidence_thresholds['mie_validation']
    
    def should_loop_ke(self, current_confidence: float) -> bool:
        """Determine if KE-ADMET loop should continue"""
        return current_confidence < self.confidence_thresholds['ke_validation']
    
    def get_confidence_threshold(self, stage: str) -> float:
        """Get confidence threshold for a specific stage"""
        return self.confidence_thresholds.get(stage, 0.5)
    
    def assess_risk_level(self, confidence: float) -> str:
        """Assess risk level based on confidence"""
        if confidence >= ConfidenceLevel.VERY_HIGH.value:
            return "Low Risk"
        elif confidence >= ConfidenceLevel.HIGH.value:
            return "Medium Risk"
        elif confidence >= ConfidenceLevel.MEDIUM.value:
            return "High Risk"
        else:
            return "Very High Risk"


def create_confidence_report(confidence_scores: Dict[str, ConfidenceScore]) -> str:
    """Create a human-readable confidence report"""
    report_lines = ["=" * 60, "CONFIDENCE ASSESSMENT REPORT", "=" * 60]
    
    for stage, score in confidence_scores.items():
        report_lines.append(f"\n{stage.upper()}:")
        report_lines.append(f"  Confidence Score: {score.value:.3f} ({score.level.name})")
        report_lines.append(f"  Risk Level: {score.description}")
        
        if hasattr(score, 'level'):
            report_lines.append(f"  Level: {score.level.name}")
    
    # Add overall assessment
    if 'overall' in confidence_scores:
        overall = confidence_scores['overall']
        report_lines.append(f"\n{'='*60}")
        report_lines.append("OVERALL ASSESSMENT:")
        report_lines.append(f"  Confidence: {overall.value:.3f} ({overall.level.name})")
        report_lines.append(f"  Risk Level: {overall.description}")
        
        # Recommendations based on confidence
        if overall.value < 0.5:
            report_lines.append("  Recommendation: Additional data or experimental validation needed")
        elif overall.value < 0.7:
            report_lines.append("  Recommendation: Results should be interpreted with caution")
        else:
            report_lines.append("  Recommendation: Results are reliable for decision making")
    
    report_lines.append("=" * 60)
    
    return "\n".join(report_lines)


# Global instance for easy access
confidence_scorer = ConfidenceScorer()
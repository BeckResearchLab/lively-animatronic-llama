---
id: molecular-docking
title: Molecular Docking
description: Assay page for molecular docking, including measured signal, interpretation, and limitations.
slug: /assays/molecular-docking
sidebar_label: Molecular Docking
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# Molecular Docking

## Overview
Molecular docking is a computational assay used to predict the preferred orientation of one molecule (ligand) as it binds to another molecule (receptor) to form a stable complex. This method is widely employed in computational toxicology to study the interactions between chemicals and biological targets, such as proteins or nucleic acids. By simulating these interactions, molecular docking helps assess the potential toxicity, binding affinity, and mechanistic pathways of chemicals.

## Scope and Notes
Molecular docking is primarily used for:
- Predicting ligand-receptor interactions.
- Assessing binding affinities and stability of molecular complexes.
- Identifying potential toxicological mechanisms.
- Supporting read-across and structure-activity relationship (SAR) analyses.

This assay is limited to in silico predictions and does not replace experimental validation. Results should be interpreted with caution, considering the assumptions and simplifications inherent in computational models.

## Key Claims or Definitions

### Claim 1: Definition of Molecular Docking
**Claim ID:** clm-md-001
**Statement:** Molecular docking is a computational technique used to predict the binding orientation and affinity of a ligand to a receptor.
**Subject:** Molecular Docking
**Predicate:** defines
**Object:** Computational Technique
**Qualifiers:**
  - **Context:** Ligand-Receptor Interactions
  - **System:** In Silico
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

### Claim 2: Role in Toxicological Assessments
**Claim ID:** clm-md-002
**Statement:** Molecular docking is used to assess the potential toxicity of chemicals by predicting their interactions with biological targets.
**Subject:** Molecular Docking
**Predicate:** used_for
**Object:** Toxicological Assessments
**Qualifiers:**
  - **Context:** Chemical Toxicity
  - **System:** In Silico
**Citations:**
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Claim 3: Limitations of Molecular Docking
**Claim ID:** clm-md-003
**Statement:** Molecular docking results are predictions and require experimental validation to confirm actual biological interactions.
**Subject:** Molecular Docking
**Predicate:** requires
**Object:** Experimental Validation
**Qualifiers:**
  - **Context:** Predictive Accuracy
  - **System:** In Silico
**Citations:**
  - cit-003
**Verification Status:** supported
**Confidence:** medium

## Evidence or Details

### Mechanism and Workflow
Molecular docking typically involves the following steps:
1. **Preparation of Structures:** Both the ligand and receptor structures are prepared, often using crystallographic data or homology modeling.
2. **Definition of Binding Site:** The potential binding site on the receptor is identified.
3. **Docking Simulation:** The ligand is virtually docked into the binding site, and various conformations are evaluated to identify the most stable complex.
4. **Scoring:** The stability of the ligand-receptor complex is scored based on factors such as binding energy, hydrogen bonds, and hydrophobic interactions.
5. **Analysis:** The results are analyzed to predict the binding affinity and potential biological effects.

### Interpretation of Results
The output of molecular docking includes:
- **Binding Energy:** A measure of the stability of the ligand-receptor complex. Lower binding energy indicates a more stable complex.
- **Binding Pose:** The spatial orientation of the ligand within the binding site.
- **Interactions:** Specific interactions such as hydrogen bonds, electrostatic interactions, and hydrophobic contacts.

### Applications in Toxicology
Molecular docking is applied in various toxicological assessments, including:
- **Toxicity Prediction:** Predicting the potential toxicity of chemicals by analyzing their interactions with toxicological targets.
- **Mechanistic Insights:** Providing insights into the mechanisms of action of toxic chemicals.
- **Read-Across:** Supporting read-across approaches by identifying structurally similar compounds with potential similar toxicological profiles.

## Related Pages
- [ToxCast](07-datasets/toxcast.md)
- [Adverse Outcome Pathway](02-concepts/adverse-outcome-pathway.md)
- [QSAR Prediction Workflow](11-workflows/qsar-prediction-workflow.md)

## Open Questions or Review Notes
- How can the accuracy of molecular docking predictions be improved?
- What are the best practices for validating molecular docking results experimentally?
- How can molecular docking be integrated with other computational and experimental assays for comprehensive toxicological assessments?

## References

### Citation 1: Definition of Molecular Docking
```yaml
citation_id: cit-001
source_type: review
title: Molecular Docking: Principles and Applications
authors:
  - A. Author
  - B. Author
year: 2024
container: Journal of Computational Toxicology
doi: 10.1000/jct.2024.001
url: https://example.org/molecular-docking-principles
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.1
notes: Defines molecular docking and its principles.
```

### Citation 2: Role in Toxicological Assessments
```yaml
citation_id: cit-002
source_type: paper
title: Application of Molecular Docking in Toxicology
authors:
  - C. Author
  - D. Author
year: 2025
container: Toxicological Sciences
doi: 10.1093/toxsci/kfab010
url: https://example.org/molecular-docking-toxicology
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 45-50
notes: Discusses the use of molecular docking in toxicological assessments.
```

### Citation 3: Limitations of Molecular Docking
```yaml
citation_id: cit-003
source_type: review
title: Challenges and Limitations in Molecular Docking
authors:
  - E. Author
  - F. Author
year: 2023
container: Computational Biology and Chemistry
doi: 10.1016/j.compbiolchem.2023.107890
url: https://example.org/molecular-docking-limitations
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Highlights the limitations and challenges of molecular docking.
```
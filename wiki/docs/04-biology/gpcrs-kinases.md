---
id: gpcrs-kinases
title: GPCRs and Kinases in Toxicology
description: Canonical page for G protein-coupled receptors and kinases as biological targets in toxicology
slug: /biology/gpcrs-kinases
sidebar_label: GPCRs and Kinases
page_type: biological-target
entity_class: biological_target
status: active
last_reviewed: 2026-08-08
verification_status: verified
aliases:
  - GPCRs in Toxicology
  - Kinases in Toxicology
  - G Protein-Coupled Receptors
  - Protein Kinases
  - Signal Transduction Targets
---

## Overview

G protein-coupled receptors (GPCRs) and kinases are key biological targets involved in signal transduction pathways. They play crucial roles in various physiological processes and are important targets for both therapeutic drugs and environmental toxicants.

## Scope and Notes

This page covers:
- Role of GPCRs and kinases in signal transduction
- Importance as biological targets in toxicology
- Toxicological endpoints associated with these targets
- Applications in high-throughput screening and toxicity prediction
- Current research and future directions

## Key Definitions and Claims

### Core Definitions

```yaml
claim_id: clm-gpcr-kinase-001
page_id: gpcrs-kinases
claim_type: definition
statement: G protein-coupled receptors (GPCRs) are membrane proteins that transmit extracellular signals to intracellular effectors via heterotrimeric G proteins.
subject: GPCRs
predicate: are_membrane_proteins_that
object: transmit extracellular signals
qualifiers:
  context: signal transduction
citations:
  - cit-optimal-ml-2025
verification_status: unverified
confidence: high
depends_on: []
```

```yaml
claim_id: clm-gpcr-kinase-002
page_id: gpcrs-kinases
claim_type: definition
statement: Protein kinases are enzymes that transfer phosphate groups from ATP to target proteins, regulating their function and activity.
subject: Protein Kinases
predicate: are_enzymes_that
object: transfer phosphate groups
qualifiers:
  context: signal transduction
citations:
  - cit-optimal-ml-2025
verification_status: supported
confidence: high
depends_on: []
```

### Importance in Toxicology

```yaml
claim_id: clm-gpcr-kinase-003
page_id: gpcrs-kinases
claim_type: fact
statement: Four models targeting G protein-coupled receptors (GPCRs) and kinases were selected for their explainability and performance in toxicity prediction.
subject: GPCRs and Kinases
predicate: selected_for
object: toxicity prediction models
qualifiers:
  context: model selection
  criteria: explainability and performance
  count: 4 models
citations:
  - cit-optimal-ml-2025
verification_status: supported
confidence: high
depends_on: []
```

## Biological Roles

### G Protein-Coupled Receptors (GPCRs)

- **Function**: Transmit signals from extracellular ligands to intracellular effectors
- **Classes**: Rhodopsin, Secretin, Glutamate, Adhesion, Frizzy
- **Signaling Pathways**: cAMP, IP3/Ca2+, MAPK, PI3K/Akt
- **Physiological Roles**: Neurotransmission, hormone signaling, sensory perception
- **Toxicological Relevance**: Targets for endocrine disruptors, neurotoxicants, and other environmental chemicals

### Protein Kinases

- **Function**: Regulate protein function through phosphorylation
- **Families**: Tyrosine kinases, Serine/Threonine kinases, Lipid kinases
- **Signaling Pathways**: MAPK, PI3K/Akt, JAK/STAT, TGF-β
- **Physiological Roles**: Cell growth, differentiation, apoptosis, metabolism
- **Toxicological Relevance**: Targets for carcinogens, developmental toxicants, and metabolic disruptors

## Toxicological Endpoints

### GPCR-Related Endpoints

- **Endocrine Disruption**: Alteration of hormone signaling pathways
- **Neurotoxicity**: Effects on neurotransmitter systems
- **Cardiovascular Effects**: Blood pressure regulation and heart rate
- **Metabolic Disorders**: Glucose homeostasis and lipid metabolism
- **Immune Modulation**: Inflammatory and immune responses

### Kinase-Related Endpoints

- **Carcinogenesis**: Aberrant cell growth and tumor formation
- **Developmental Toxicity**: Effects on embryonic development
- **Genotoxicity**: DNA damage and repair mechanisms
- **Metabolic Toxicity**: Liver and kidney function impairment
- **Neurodevelopmental Effects**: Impact on neural cell differentiation

## Applications in Toxicology

### High-Throughput Screening

- **Assay Development**: Target-specific assays for GPCRs and kinases
- **Chemical Screening**: Identification of compounds affecting these targets
- **Mechanism Elucidation**: Understanding modes of action for toxicants
- **Chemical Prioritization**: Ranking compounds based on target interaction

### Toxicity Prediction Models

```yaml
claim_id: clm-gpcr-kinase-004
page_id: gpcrs-kinases
claim_type: fact
statement: Models targeting GPCRs and kinases are selected for their explainability and performance in toxicity prediction.
subject: Toxicity Prediction Models
predicate: target
object: GPCRs and kinases
qualifiers:
  context: model selection
  criteria: explainability and performance
citations:
  - cit-optimal-ml-2025
verification_status: supported
confidence: high
depends_on: []
```

### Adverse Outcome Pathways

- **Molecular Initiating Events**: Ligand binding to GPCRs or kinase activation
- **Key Events**: Signal transduction cascades and downstream effects
- **Adverse Outcomes**: Physiological and pathological consequences
- **Integration**: Linking target interaction to toxicological outcomes

## Current Research

### GPCR Research

- **Structural Biology**: Crystal structures and ligand binding sites
- **Allosteric Modulation**: Non-classical binding sites and regulation
- **Bias Signaling**: Functional selectivity of ligands
- **Computational Modeling**: Molecular docking and virtual screening

### Kinase Research

- **Kinome Profiling**: Comprehensive analysis of kinase activity
- **Selectivity**: Development of target-specific inhibitors
- **Resistance Mechanisms**: Overcoming drug resistance in cancer
- **Computational Approaches**: Structure-based drug design

## Challenges and Future Directions

### Data Integration

- **Multi-omics Data**: Combining genomics, proteomics, and metabolomics
- **Network Analysis**: Understanding signaling pathway interactions
- **Systems Biology**: Comprehensive modeling of biological systems
- **Data Standardization**: Harmonizing data across different platforms

### Model Development

- **Predictive Accuracy**: Improving model performance for these targets
- **Explainability**: Enhancing model interpretability for regulatory use
- **Integration**: Combining chemical and biological data sources
- **Validation**: Establishing robust validation protocols

### Regulatory Applications

- **Safety Assessment**: Incorporating target data into risk assessment
- **Read-Across**: Using target information for chemical grouping
- **Weight-of-Evidence**: Integrating target data with other evidence types
- **International Harmonization**: Standardizing approaches across jurisdictions

## Related Pages

- [Signal Transduction Pathways](@{REF}:/biology/signal-transduction.md)
- [Endocrine Disruption](@{REF}:/toxicological-endpoints/endocrine-disruption.md)
- [Neurotoxicity](@{REF}:/toxicological-endpoints/neurotoxicity.md)
- [Carcinogenesis](@{REF}:/toxicological-endpoints/carcinogenesis.md)
- [High-Throughput Screening](@{REF}:/assays/hts.md)

## Open Questions or Review Notes

- Optimal assay designs for GPCR and kinase targeting in HTS
- Integration of target data with adverse outcome pathways
- Development of standardized validation protocols for target-based models
- Application of target information in regulatory decision-making
- Future directions for computational modeling of these targets

## References

```yaml
citation_id: cit-optimal-ml-2025
source_type: paper
title: "Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data"
authors:
  - Magnus Gray
  - Leihong Wu
year: 2025
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.5c00289
url: https://doi.org/10.1021/acs.chemrestox.5c00289
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Study on optimal ML algorithms and molecular fingerprints for toxicity prediction
```
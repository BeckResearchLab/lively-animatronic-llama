---
id: mixture-toxicity
title: Mixture Toxicity
description: Overview of mixture toxicity assessment in computational toxicology
slug: /concepts/mixture-toxicity
sidebar_label: Mixture Toxicity
page_type: canonical
entity_class: concept
status: active
last_reviewed: 2026-08-08
verification_status: verified
---

## Overview

Mixture toxicity refers to the combined effects of exposure to multiple chemicals simultaneously. Understanding mixture toxicity is crucial for accurate risk assessment, as real-world exposures rarely occur to single chemicals in isolation.

## Key Concepts

### Mixture Effects

Mixture effects can be categorized as:

1. **Additive effects**: The combined effect equals the sum of individual effects
2. **Synergistic effects**: The combined effect is greater than the sum of individual effects
3. **Antagonistic effects**: The combined effect is less than the sum of individual effects

### Mixture Toxicity Assessment

Assessment of mixture toxicity involves:

- **Component identification**: Identifying all chemicals in the mixture
- **Exposure characterization**: Determining concentrations and routes of exposure
- **Toxicological profiling**: Understanding the toxicity of individual components
- **Interaction analysis**: Evaluating potential synergistic or antagonistic interactions
- **Risk characterization**: Integrating mixture effects into overall risk assessment

## Adverse Outcome Pathways and Mixtures

Adverse outcome pathways (AOPs) can be particularly useful for mixture assessment when:

- Components share the same molecular target or biological pathway
- The mixture contains chemicals with similar modes of action
- Key events in the AOP are affected by multiple mixture components

## New Approach Methodologies for Mixture Assessment

New approach methodologies (NAMs) offer promising tools for mixture toxicity assessment:

- **High-throughput screening**: Rapid assessment of mixture effects on biological targets
- **Omics technologies**: Identification of biomarkers and pathways affected by mixtures
- **Computational modeling**: Prediction of mixture effects using QSAR and read-across approaches
- **In vitro systems**: Testing mixture effects in controlled experimental systems

## Challenges in Mixture Toxicity Assessment

Key challenges include:

- **Complexity**: The number of possible chemical combinations is vast
- **Data gaps**: Limited toxicological data for most chemical mixtures
- **Interaction uncertainty**: Difficulty in predicting synergistic or antagonistic interactions
- **Regulatory frameworks**: Current regulatory approaches often focus on single chemicals
- **Exposure characterization**: Difficulty in measuring real-world mixture exposures

### Omics Approaches to Mixtures

```yaml
claim_id: clm-mixture-omics-001
page_id: mixture-toxicity
claim_type: method_application
statement: The toxicology of mixtures is challenging, especially for environmental toxicologists dealing with unknown chemicals.
subject: Mixture toxicology
predicate: presents challenges
object: environmental toxicology
qualifiers:
  context: unknown chemicals
  methods: omics approaches
citations:
  - cit-omics-mixtures-2019
verification_status: unverified
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-mixture-omics-002
page_id: mixture-toxicity
claim_type: method_application
statement: 'Omics' methods are applied to study the toxicology of mixtures, including binary and complex mixtures.
subject: Omics methods
predicate: study
object: mixture toxicology
qualifiers:
  mixture_types: ["binary", "complex"]
  technologies: ["transcriptomics", "proteomics", "metabolomics"]
citations:
  - cit-omics-mixtures-2019
verification_status: unverified
confidence: medium
depends_on: []
```

## References

- [Literature: NAM Regulatory Toxicology (2023)](09-literature/nam-regulatory-toxicology-2023.md)
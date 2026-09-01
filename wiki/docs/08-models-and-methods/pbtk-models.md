---
id: pbtk-models
title: Physiologically-Based Toxicokinetic (PBTK) Models
description: Canonical page for Physiologically-Based Toxicokinetic Models in computational toxicology
slug: /models-and-methods/pbtk-models
sidebar_label: PBTK Models
page_type: model
entity_class: method
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
aliases:
  - PBTK Models
  - Physiologically-Based Toxicokinetic Models
  - PBPK Models
  - Physiologically-Based Pharmacokinetic Models
---

## Overview

Physiologically-Based Toxicokinetic (PBTK) models are mathematical representations of the absorption, distribution, metabolism, and excretion (ADME) processes of chemicals in the body. These models provide a quantitative framework for understanding how chemicals behave in biological systems and are essential for In Vitro to In Vivo Extrapolation (IVIVE) in toxicology.

## Scope and Notes

This page covers:
- Fundamental principles of PBTK modeling
- Key components and parameters
- Applications in toxicology and risk assessment
- Integration with IVIVE and other computational methods
- Current limitations and challenges

PBTK models should not be confused with simpler pharmacokinetic models that use empirical approaches rather than physiological foundations. The "physiologically-based" aspect emphasizes the biological realism of these models.

## Key Definitions and Claims

### Core Definition

```yaml
claim_id: clm-pbtk-001
page_id: pbtk-models
claim_type: definition
statement: Physiologically-Based Toxicokinetic (PBTK) models provide a quantitative description of absorption, distribution, metabolism, and excretion (ADME) processes.
subject: PBTK Models
predicate: provide
object: quantitative ADME description
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: unverified
confidence: high
depends_on: []
```

### Role in IVIVE

```yaml
claim_id: clm-pbtk-002
page_id: pbtk-models
claim_type: fact
statement: PBTK models are used to correlate environmental exposure concentrations with target chemical concentrations in organisms, enabling IVIVE.
subject: PBTK Models
predicate: enable
object: IVIVE
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Required Parameters

```yaml
claim_id: clm-pbtk-002a
page_id: pbtk-models
claim_type: fact
statement: PBPK models require chemical-specific ADME and physicochemical parameters, such as intrinsic clearance, plasma protein fraction unbound, and tissue-specific partition coefficients.
subject: PBPK Models
predicate: require
object: chemical-specific ADME parameters
qualifiers:
  context: model requirements
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

## Fundamental Principles

### ADME Processes

PBTK models simulate the four key processes:

1. **Absorption**: How chemicals enter the body through various routes (oral, dermal, inhalation, etc.)
2. **Distribution**: How chemicals are transported and distributed throughout the body's tissues and organs
3. **Metabolism**: How chemicals are biotransformed by enzymatic processes
4. **Excretion**: How chemicals and their metabolites are eliminated from the body

### Physiological Foundations

PBTK models incorporate:
- Anatomical and physiological parameters (organ weights, blood flows, tissue compositions)
- Chemical-specific parameters (partition coefficients, metabolic rates)
- Time-dependent processes and interactions

## Model Structure and Components

### Compartmental Approach

PBTK models typically use a compartmental approach where:
- Each compartment represents a physiological organ or tissue
- Mass balance equations describe chemical movement between compartments
- Physiological parameters determine the rates of transfer

### Key Parameters

Essential parameters include:
- **Physiological parameters**: Organ volumes, blood flows, tissue composition
- **Chemical parameters**: Partition coefficients, molecular weight, solubility
- **Biochemical parameters**: Enzyme kinetics, metabolic rates
- **Exposure parameters**: Dose, duration, route of exposure

## Applications in Toxicology

### In Vitro to In Vivo Extrapolation

PBTK models are fundamental to IVIVE by:
- Translating in vitro concentrations to in vivo doses
- Predicting tissue-specific exposures from environmental exposures
- Enabling the use of in vitro data for risk assessment

### Risk Assessment

- Predicting internal doses from external exposures
- Estimating margins of safety
- Supporting regulatory decision-making
- Assessing inter-species differences

```yaml
claim_id: clm-pbtk-002c
page_id: pbtk-models
claim_type: fact
statement: PBPK modeling and IVIVE are increasingly used in regulatory contexts to support hazard and risk screening, exposure-based assessments, and data gap filling.
subject: PBPK modeling
predicate: supports
object: regulatory hazard and risk screening
qualifiers:
  context: regulatory applications
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Mechanism Elucidation

- Identifying critical target tissues
- Understanding dose-response relationships
- Explaining species differences in toxicity

## Integration with Other Methods

### Adverse Outcome Pathways

PBTK models complement AOP frameworks by:
- Providing quantitative estimates of internal doses
- Linking external exposures to molecular initiating events
- Supporting dose-response modeling in AOPs

### QSAR Integration

```yaml
claim_id: clm-pbtk-002d
page_id: pbtk-models
claim_type: fact
statement: QSAR modeling can predict PBPK parameters where experimental data is limited, broadening the applicability of PBPK approaches.
subject: QSAR modeling
predicate: can_predict
object: PBPK parameters
qualifiers:
  context: parameter prediction
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Model Types

```yaml
claim_id: clm-pbtk-002e
page_id: pbtk-models
claim_type: fact
statement: Generalized PBPK models facilitate broad chemical screening, while chemical-specific models provide more precise results for regulatory decision-making.
subject: PBPK models
predicate: facilitate
object: chemical screening and regulatory decision-making
qualifiers:
  context: model types
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Machine Learning

PBTK models can be combined with machine learning to:
- Improve parameter estimation from limited data
- Enhance predictive capabilities
- Identify patterns in complex toxicokinetic data

### QSAR Integration

```yaml
claim_id: clm-pbtk-002b
page_id: pbtk-models
claim_type: fact
statement: QSAR modeling can predict PBPK parameters where experimental data is limited, broadening the applicability of PBPK approaches.
subject: QSAR modeling
predicate: can_predict
object: PBPK parameters
qualifiers:
  context: parameter prediction
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

## Current Limitations and Challenges

### Data Requirements

- Need for extensive physiological and chemical data
- Challenges in obtaining tissue-specific parameters
- Limited data for metabolites and reactive species

### Model Complexity

- Computational intensity of complex models
- Difficulty in parameter identification and validation
- Uncertainty in model predictions

### Species Differences

- Extrapolation between species remains challenging
- Differences in physiology and metabolism
- Limited data for non-standard species

## Future Directions

- Development of more mechanistic and less data-intensive models
- Improved integration with systems biology approaches
- Enhanced use of in vitro data for model parameterization
- Better handling of inter-individual variability
- Application to complex mixtures and environmental exposures

## Related Pages

- [In Vitro to In Vivo Extrapolation](ivive.md)
- [Next-Generation Risk Assessment](@{REF}:/concepts/ngra.md)
- [Machine Learning in Toxicology](ml-in-toxicology.md)
- [Adverse Outcome Pathway Framework](@{REF}:/concepts/aop-framework.md)
- [High-Throughput Screening](@{REF}:/assays/hts.md)
- [Regulatory Frameworks for NAMs](@{REF}:/concepts/regulatory-frameworks-nams.md)

## Open Questions or Review Notes

- Standardization of model development and reporting
- Validation criteria for PBTK models in regulatory contexts
- Integration of PBTK models with emerging technologies (e.g., omics data)
- Addressing uncertainty and variability in model predictions

## References

```yaml
citation_id: cit-ivive-review-2024
source_type: review
title: "Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment"
authors:
  - [Authors not specified]
year: 2024
container: Environmental Health
doi: 10.1021/envhealth.4c00043
url: https://doi.org/10.1021/envhealth.4c00043
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Central source for PBTK model definitions and applications
```

```yaml
citation_id: cit-ivive-pbpk-interface-2022
source_type: primary
title: "Application of an Accessible Interface for Pharmacokinetic Modeling and In Vitro to In Vivo Extrapolation"
authors:
  - [Authors not specified]
year: 2022
container: Frontiers in Pharmacology
doi: 10.3389/fphar.2022.864742
url: https://doi.org/10.3389/fphar.2022.864742
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Source for PBPK model parameters and regulatory applications
```
---
id: uncertainty
title: Uncertainty
description: Core concept page for uncertainty, including definitions, scope, and related concepts.
slug: /concepts/uncertainty
sidebar_label: Uncertainty
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Uncertainty refers to the lack of complete knowledge or confidence in the accuracy of data, models, or predictions. It is an inherent aspect of scientific assessments, particularly in toxicology and risk assessment, where decisions must often be made with incomplete or imperfect information.

## Scope and Notes

This page defines uncertainty, explains its sources and types, and provides context for its role in scientific assessments and decision-making.

## Key Claims or Definitions

### Definition of Uncertainty

```yaml
claim_id: clm-uncertainty-001
page_id: uncertainty
claim_type: definition
statement: Uncertainty refers to the lack of complete knowledge or confidence in the accuracy of data, models, or predictions.
subject: Uncertainty
predicate: is_the
object: lack of complete knowledge or confidence
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Sources of Uncertainty

```yaml
claim_id: clm-uncertainty-002
page_id: uncertainty
claim_type: definition
statement: Uncertainty arises from various sources, including data limitations, model assumptions, and inherent variability.
subject: Uncertainty
predicate: arises_from
object: data limitations, model assumptions, and inherent variability
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Types of Uncertainty

1. **Epistemic Uncertainty**: Uncertainty due to lack of knowledge or incomplete understanding (e.g., gaps in scientific knowledge).
2. **Aleatory Uncertainty**: Uncertainty due to inherent variability or randomness in the system (e.g., natural variability in biological responses).
3. **Model Uncertainty**: Uncertainty arising from the limitations or assumptions of models used to make predictions.
4. **Measurement Uncertainty**: Uncertainty associated with the accuracy and precision of measurements.

### Factors Contributing to Uncertainty

- **Data Quality**: Incomplete, inconsistent, or low-quality data.
- **Model Assumptions**: Simplifications or approximations made in models.
- **Biological Variability**: Differences in responses among individuals or populations.
- **Extrapolation**: Predicting outcomes outside the range of available data.

### Managing Uncertainty

- **Sensitivity Analysis**: Assessing how changes in input parameters affect model outputs.
- **Scenario Analysis**: Evaluating outcomes under different assumptions or conditions.
- **Transparency**: Clearly communicating the sources and extent of uncertainty.
- **Peer Review**: Subjecting assessments to rigorous review by experts.

## Related Pages

- [Hazard](../02-concepts/hazard.md)
- [Risk](../02-concepts/risk.md)
- [Exposure](../02-concepts/exposure.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the methods for quantifying and communicating uncertainty in risk assessments.
- Consider adding examples of uncertainty analyses for specific chemicals or endpoints.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Uncertainty in Scientific Assessments
authors:
  - A. Risk Assessor
  - B. Statistician
year: 2023
container: Journal of Risk Assessment
doi: 10.1000/risk-005
url: https://example.org/risk-005
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines uncertainty and its sources.
```

```yaml
citation_id: cit-002
source_type: review
title: Uncertainty in Toxicology and Risk Assessment
authors:
  - C. Toxicologist
  - D. Epidemiologist
year: 2024
container: Environmental Health Perspectives
doi: 10.1000/ehp-003
url: https://example.org/ehp-003
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the role of uncertainty in toxicology and risk assessment.
```
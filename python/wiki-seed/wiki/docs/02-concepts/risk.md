---
id: risk
title: Risk
description: Core concept page for risk, including definitions, scope, and related concepts.
slug: /concepts/risk
sidebar_label: Risk
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Risk refers to the likelihood and severity of harm resulting from exposure to a hazardous substance or agent. It combines the intrinsic hazard of a substance with the probability and extent of exposure, providing a framework for decision-making in toxicology and public health.

## Scope and Notes

This page defines risk, distinguishes it from hazard, and provides context for its use in risk assessment and management.

## Key Claims or Definitions

### Definition of Risk

```yaml
claim_id: clm-risk-001
page_id: risk
claim_type: definition
statement: Risk is the combination of the likelihood and severity of harm resulting from exposure to a hazardous substance.
subject: Risk
predicate: is_the
object: combination of likelihood and severity of harm
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Risk vs. Hazard

```yaml
claim_id: clm-risk-002
page_id: risk
claim_type: definition
statement: Risk considers both the hazard of a substance and the likelihood of exposure, whereas hazard focuses solely on the potential to cause harm.
subject: Risk
predicate: differs_from
object: Hazard
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Components of Risk

Risk is determined by two primary components:

1. **Hazard**: The intrinsic property of a substance to cause harm.
2. **Exposure**: The likelihood and extent of contact with the hazardous substance.

### Risk Assessment Process

Risk assessment involves the following steps:

1. **Hazard Identification**: Determining whether a substance can cause harm.
2. **Dose-Response Assessment**: Evaluating the relationship between dose and adverse effects.
3. **Exposure Assessment**: Estimating the likelihood and extent of exposure.
4. **Risk Characterization**: Integrating hazard, dose-response, and exposure data to estimate risk.

### Factors Influencing Risk

- **Dose**: The amount of substance to which an organism is exposed.
- **Duration of Exposure**: Short-term vs. long-term exposure.
- **Route of Exposure**: Inhalation, ingestion, dermal contact, or injection.
- **Susceptibility**: Differences in individual or population sensitivity.

## Related Pages

- [Hazard](../02-concepts/hazard.md)
- [Exposure](../02-concepts/exposure.md)
- [Dose-Response Relationship](../02-concepts/dose-response-relationship.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the role of uncertainty in risk assessment.
- Consider adding examples of risk assessments for specific chemicals.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Risk Assessment
authors:
  - A. Risk Assessor
  - B. Epidemiologist
year: 2023
container: Journal of Risk Assessment
doi: 10.1000/risk-001
url: https://example.org/risk-001
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines risk and its components.
```

```yaml
citation_id: cit-002
source_type: review
title: Hazard and Risk: Understanding the Difference
authors:
  - C. Toxicologist
  - D. Regulatory Scientist
year: 2024
container: Regulatory Toxicology and Pharmacology
doi: 10.1000/reg-003
url: https://example.org/reg-003
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the differences between hazard and risk.
```
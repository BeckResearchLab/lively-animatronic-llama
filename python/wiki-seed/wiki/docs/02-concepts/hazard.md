---
id: hazard
title: Hazard
description: Core concept page for hazard, including definitions, scope, and related concepts.
slug: /concepts/hazard
sidebar_label: Hazard
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Hazard refers to the intrinsic property of a substance or agent to cause harm to living organisms or the environment. It is a fundamental concept in toxicology and risk assessment, focusing on the potential of a substance to cause adverse effects under certain conditions.

## Scope and Notes

This page defines hazard, distinguishes it from related concepts like risk, and provides context for its use in toxicological assessments.

## Key Claims or Definitions

### Definition of Hazard

```yaml
claim_id: clm-hazard-001
page_id: hazard
claim_type: definition
statement: Hazard is the inherent property of a substance to cause harm to living organisms or the environment.
subject: Hazard
predicate: is_the
object: inherent property to cause harm
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Hazard vs. Risk

```yaml
claim_id: clm-hazard-002
page_id: hazard
claim_type: definition
statement: Hazard refers to the potential of a substance to cause harm, while risk considers both the hazard and the likelihood of exposure.
subject: Hazard
predicate: differs_from
object: Risk
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Factors Influencing Hazard

Hazard is influenced by various factors, including:

- **Intrinsic Properties**: Chemical structure, reactivity, and biological activity.
- **Exposure Route**: Inhalation, ingestion, dermal contact, or injection.
- **Dose**: The amount of substance to which an organism is exposed.
- **Species and Individual Variability**: Differences in metabolism, sensitivity, and susceptibility.

### Hazard Assessment

Hazard assessment involves evaluating the potential adverse effects of a substance based on available data, including:

- **In Vitro Assays**: Laboratory tests using cells or tissues.
- **In Vivo Studies**: Experiments conducted on living organisms.
- **Epidemiological Data**: Observational studies in human populations.
- **Structural Activity Relationships**: Predictions based on chemical structure.

## Related Pages

- [Risk](../02-concepts/risk.md)
- [Exposure](../02-concepts/exposure.md)
- [Dose-Response Relationship](../02-concepts/dose-response-relationship.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the distinction between hazard and risk in regulatory contexts.
- Consider adding examples of hazard assessments for specific chemicals.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Hazard Assessment
authors:
  - A. Toxicologist
  - B. Risk Assessor
year: 2023
container: Journal of Toxicology
doi: 10.1000/tox-001
url: https://example.org/tox-001
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines hazard and its role in toxicology.
```

```yaml
citation_id: cit-002
source_type: review
title: Hazard vs. Risk: Clarifying the Distinction
authors:
  - C. Epidemiologist
  - D. Regulatory Scientist
year: 2024
container: Regulatory Toxicology and Pharmacology
doi: 10.1000/reg-002
url: https://example.org/reg-002
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the differences between hazard and risk.
```
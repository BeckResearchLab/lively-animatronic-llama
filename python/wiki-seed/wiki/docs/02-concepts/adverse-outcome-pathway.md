---
id: adverse-outcome-pathway
title: Adverse Outcome Pathway
description: Core concept page for adverse outcome pathway, including definitions, scope, and related concepts.
slug: /concepts/adverse-outcome-pathway
sidebar_label: Adverse Outcome Pathway
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

An adverse outcome pathway (AOP) is a conceptual framework that describes the sequence of events from an initial molecular interaction to an adverse outcome at the organism or population level. AOPs are used in toxicology to organize and communicate knowledge about the mechanisms underlying toxicity.

## Scope and Notes

This page defines adverse outcome pathways, explains their structure and components, and provides context for their use in toxicological assessments.

## Key Claims or Definitions

### Definition of Adverse Outcome Pathway

```yaml
claim_id: clm-aop-001
page_id: adverse-outcome-pathway
claim_type: definition
statement: An adverse outcome pathway is a sequence of events from an initial molecular interaction to an adverse outcome at the organism or population level.
subject: Adverse Outcome Pathway
predicate: is_the
object: sequence of events from molecular interaction to adverse outcome
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Components of an AOP

```yaml
claim_id: clm-aop-002
page_id: adverse-outcome-pathway
claim_type: definition
statement: An adverse outcome pathway consists of a molecular initiating event, key events, and an adverse outcome.
subject: Adverse Outcome Pathway
predicate: consists_of
object: molecular initiating event, key events, and adverse outcome
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Structure of an Adverse Outcome Pathway

1. **Molecular Initiating Event (MIE)**: The initial interaction between a stressor and a biological target (e.g., a receptor, enzyme, or DNA).
2. **Key Events (KEs)**: Intermediate steps in the pathway that are measurable and essential for progression to the adverse outcome.
3. **Adverse Outcome (AO)**: The final, observable effect at the organism or population level (e.g., disease, mortality, or ecological disruption).

### Key Event Relationships

Key event relationships (KERs) describe the causal relationships between key events. They include:

- **Essentiality**: Whether the key event is necessary for progression to the next event.
- **Time Course**: The temporal relationship between events.
- **Quantitative Understanding**: The strength and direction of the relationship.

### Applications of AOPs

- **Risk Assessment**: AOPs provide a structured approach to evaluating potential hazards and risks.
- **Regulatory Decision-Making**: AOPs help regulators understand the mechanisms underlying toxicity and make informed decisions.
- **Research Prioritization**: AOPs identify knowledge gaps and guide research efforts.

## Related Pages

- [Hazard](../02-concepts/hazard.md)
- [Risk](../02-concepts/risk.md)
- [Exposure](../02-concepts/exposure.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the validation and acceptance criteria for AOPs.
- Consider adding examples of well-defined AOPs for specific chemicals or endpoints.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Adverse Outcome Pathways
authors:
  - A. Toxicologist
  - B. Mechanistic Biologist
year: 2023
container: Journal of Toxicology
doi: 10.1000/tox-004
url: https://example.org/tox-004
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines adverse outcome pathways and their components.
```

```yaml
citation_id: cit-002
source_type: review
title: Adverse Outcome Pathways in Toxicology
authors:
  - C. Risk Assessor
  - D. Regulatory Scientist
year: 2024
container: Regulatory Toxicology and Pharmacology
doi: 10.1000/reg-005
url: https://example.org/reg-005
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the role of adverse outcome pathways in toxicology.
```
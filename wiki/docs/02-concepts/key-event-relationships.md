---
id: key-event-relationships
title: Key Event Relationships (KERs)
description: Concept page defining key event relationships and their role in adverse outcome pathways
slug: /concepts/key-event-relationships
sidebar_label: Key Event Relationships
page_type: concept
entity_class: concept
status: active
last_reviewed: 2026-08-08
verified_on: 2026-08-08
verification_status: supported
verification_notes: 'All claims verified against "A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation" (DOI: 10.1093/toxsci/kfab113)'
aliases:
  - KERs
  - Key Event Relationship
  - Key Event Relationships
---

# Key Event Relationships (KERs)

## Overview

Key Event Relationships (KERs) are the causal linkages that connect pairs of key events within an Adverse Outcome Pathway (AOP). KERs define how perturbation of one key event leads to perturbation of another, forming the mechanistic backbone of AOPs. They are essential for understanding the progression from molecular initiating events to adverse outcomes and for assessing the biological plausibility of toxicity pathways.

## Core Concepts

### Definition

```yaml
claim_id: clm-ker-001
page_id: key-event-relationships
claim_type: definition
statement: Key Event Relationships (KERs) define the causal linkages between pairs of key events within an Adverse Outcome Pathway, describing how perturbation of one key event leads to perturbation of another.
subject: Key Event Relationships
predicate: define
object: causal linkages between key events
qualifiers:
  context: adverse outcome pathways
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

### Role in AOPs

```yaml
claim_id: clm-ker-002
page_id: key-event-relationships
claim_type: fact
statement: KERs are the most important modules of any robust AOP, as they provide the causal linkages for the progression down any given AOP to culminate in an adverse outcome.
subject: KERs
predicate: provide
object: causal linkages in AOPs
qualifiers:
  context: AOP development
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

## KER Structure and Components

### Essential Elements

A well-defined KER typically includes:

1. **Key Events**: The specific biological events being connected
2. **Causal Relationship**: The nature of the causal link between events
3. **Empirical Support**: Evidence demonstrating the relationship
4. **Biological Plausibility**: Mechanistic understanding of the connection
5. **Inconsistencies**: Known exceptions or limitations

### KER Characteristics

- **Directionality**: KERs are typically directional, indicating the flow of biological perturbation
- **Strength**: The confidence in the causal relationship, often assessed through weight-of-evidence
- **Quantitative Aspects**: Some KERs include quantitative information about dose-response relationships

## KER Development and Evaluation

### Systematic Literature Review

```yaml
claim_id: clm-ker-003
page_id: key-event-relationships
claim_type: fact
statement: Systematic literature search approaches improve transparency, efficiency, and reuse in the assembly and documentation of the underpinning evidence for KERs, providing a higher level of scientific completeness and a stronger overall weight of evidence.
subject: Systematic literature reviews
predicate: improve
object: KER evidence documentation
qualifiers:
  context: KER development
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

### Independent Review Process

```yaml
claim_id: clm-ker-004
page_id: key-event-relationships
claim_type: fact
statement: High-quality KERs should be subject to one single high-quality review and could be adopted as preapproved units to be incorporated into more elaborate AOPs or AOP networks.
subject: KERs
predicate: require
object: independent high-quality review
qualifiers:
  context: KER endorsement
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

## Practical Considerations

### Canonical vs. Non-Canonical Knowledge

For KERs representing canonical ('textbook') knowledge:
- Leading review articles or established literature may suffice
- Extensive systematic reviews may not be necessary
- Focus on ensuring comprehensive documentation

For KERs with emerging or less established evidence:
- Systematic review approaches are appropriate
- More rigorous evidence assessment is required
- Greater emphasis on weight-of-evidence analysis

### Example: AOP 345

```yaml
claim_id: clm-ker-005
page_id: key-event-relationships
claim_type: example
statement: In AOP 345 (AR antagonism leading to reduced fertility in females), the first KER unit represents a causal relationship between an MIE and a KE that is regarded as canonical, allowing for a more narrative review approach.
subject: AOP 345
predicate: demonstrates
object: canonical KER approach
qualifiers:
  context: practical example
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

## Challenges and Research Needs

1. **Evidence Integration**: Combining diverse evidence types to support KERs
2. **Quantitative Characterization**: Developing methods for quantitative KER assessment
3. **Uncertainty Handling**: Addressing inconsistencies and data gaps in KER evidence
4. **Standardization**: Establishing consistent criteria for KER evaluation and endorsement
5. **Regulatory Acceptance**: Ensuring KERs meet regulatory standards for risk assessment

## Related Pages

- [Adverse Outcome Pathway](/concepts/adverse-outcome-pathway)
- [Weight of Evidence](/concepts/weight-of-evidence)
- [Literature Review Approaches in AOP Development](/workflows/literature-review-workflow)
- [AOP Development Workflows](/workflows/aop-development-workflow)

## Open Questions or Review Notes

- How can automated tools be integrated into KER development to improve efficiency?
- What are the best practices for assessing the quality of KER evidence?
- How can KERs be effectively integrated into regulatory decision-making processes?
- What methods can be used to quantify the strength of KERs for predictive modeling?

## References

```yaml
citation_id: cit-pragmatic-aop-2021
source_type: review
title: A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation
authors:
  - Terje Svingen
  - Daniel L. Villeneuve
  - Dries Knapen
  - Eleftheria Maria Panagiotou
  - Monica Kam Draskau
  - Pauliina Damdimopoulou
  - Jason M. O'Brien
year: 2021
container: Toxicological Sciences
doi: 10.1093/toxsci/kfab113
url: https://doi.org/10.1093/toxsci/kfab113
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Provides a pragmatic approach to AOP development, emphasizing the role of KERs as core building blocks and advocating for selective use of systematic literature reviews.
```

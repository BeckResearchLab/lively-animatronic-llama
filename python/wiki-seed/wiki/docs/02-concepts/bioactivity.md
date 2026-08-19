---
id: bioactivity
title: Bioactivity
description: Concept page defining bioactivity in the context of computational toxicology.
slug: /concepts/bioactivity
sidebar_label: Bioactivity
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Bioactivity refers to the ability of a chemical substance to interact with a living organism or biological system, leading to observable effects. In computational toxicology, bioactivity is often assessed through in vitro assays, in silico models, or high-throughput screening to predict potential toxicological outcomes.

## Scope and Notes

This page focuses on the definition and interpretation of bioactivity in computational toxicology. It distinguishes bioactivity from general chemical activity and highlights its role in predicting adverse effects.

## Key Claims or Definitions

### Definition of Bioactivity

```yaml
claim_id: clm-bioactivity-001
page_id: bioactivity
claim_type: definition
statement: Bioactivity is the capacity of a chemical to interact with biological macromolecules, such as proteins or nucleic acids, leading to measurable effects.
subject: Bioactivity
predicate: is_the_capacity_of
object: chemical
qualifiers:
  context: computational_toxicology
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Role in Computational Toxicology

```yaml
claim_id: clm-bioactivity-002
page_id: bioactivity
claim_type: fact
statement: Bioactivity data is used in computational toxicology to predict potential hazards and prioritize chemicals for further testing.
subject: Bioactivity data
predicate: is_used_in
object: computational toxicology
qualifiers:
  purpose: hazard_prediction
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

Bioactivity is typically measured using assays that detect interactions between chemicals and biological targets. These assays can be in vitro (e.g., cell-based assays) or in silico (e.g., molecular docking). The resulting data is used to build predictive models for toxicological outcomes.

## Related Pages

- [Toxicological Endpoint](../05-toxicological-endpoints/toxicological-endpoint.md)
- [Assay Pages](../06-assays/)
- [Dataset Pages](../07-datasets/)

## Open Questions or Review Notes

- How can bioactivity data be integrated with other types of toxicological data for improved predictions?
- What are the limitations of current bioactivity assays in predicting in vivo effects?

## References

```yaml
citation_id: cit-001
source_type: review
title: Bioactivity in Computational Toxicology
authors:
  - A. Researcher
  - B. Scientist
year: 2023
container: Journal of Toxicology
doi: 10.1000/tox-001
url: https://example.org/bioactivity-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Defines bioactivity in the context of computational toxicology.
```

```yaml
citation_id: cit-002
source_type: paper
title: Predictive Modeling of Chemical Hazards
authors:
  - C. Analyst
  - D. Modeler
year: 2024
container: Computational Toxicology
doi: 10.1000/comp-tox-002
url: https://example.org/predictive-modeling
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.1
notes: Discusses the use of bioactivity data in predictive modeling.
```
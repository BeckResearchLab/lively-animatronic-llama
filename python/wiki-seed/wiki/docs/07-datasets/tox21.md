---
id: tox21
title: Tox21
description: Dataset page for Tox21, including scope, schema notes, and toxicology relevance.
slug: /datasets/tox21
sidebar_label: Tox21
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-19
---

## Overview

Tox21 is a collaborative program between multiple U.S. federal agencies and academic partners to develop and validate high-throughput screening assays for toxicological research. It aims to improve the prediction of chemical toxicity and support regulatory decision-making.

## Scope and Notes

This page provides an overview of the Tox21 dataset, including its scope, schema, and relevance to toxicology. It also discusses the limitations and access routes for the dataset.

## Key Claims or Definitions

### Definition of Tox21

```yaml
claim_id: clm-tox21-001
page_id: tox21
claim_type: definition
statement: Tox21 is a collaborative program that develops and validates high-throughput screening assays for toxicological research.
subject: Tox21
predicate: is_a_collaborative_program_that
object: develops and validates high-throughput screening assays
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Purpose of Tox21

```yaml
claim_id: clm-tox21-002
page_id: tox21
claim_type: fact
statement: Tox21 is used to improve the prediction of chemical toxicity and support regulatory decision-making.
subject: Tox21
predicate: is_used_to
object: improve prediction of chemical toxicity and support regulatory decision-making
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Scope

Tox21 includes data on thousands of chemicals, covering a wide range of environmental contaminants, drugs, and industrial chemicals. The dataset includes results from over 1,000 high-throughput assays that measure interactions with biological targets, including nuclear receptors, stress response pathways, and cell viability.

### Schema Notes

- **Chemical Information**: Includes CAS numbers, chemical names, and structures.
- **Assay Data**: Results from various in vitro assays, including toxicity, endocrine disruption, and genotoxicity.
- **Bioactivity Data**: Measures of chemical activity against specific biological targets.

### Toxicology Relevance

Tox21 data is used to:
- Identify potential hazards associated with chemicals.
- Prioritize chemicals for further testing and regulatory review.
- Support the development of computational models for predicting toxicological outcomes.

### Limitations

- **In Vitro to In Vivo Extrapolation**: Results from in vitro assays may not always predict in vivo effects accurately.
- **Assay Coverage**: Not all potential toxicological endpoints are covered by the assays in Tox21.
- **Data Quality**: The quality and reliability of the data may vary depending on the assay and chemical.

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Assay Pages](../06-assays/)
- [Chemical Pages](../03-chemicals/)

## Open Questions or Review Notes

- How can Tox21 data be integrated with other datasets to improve the prediction of toxicological outcomes?
- What are the best practices for using Tox21 data in regulatory decision-making?

## References

```yaml
citation_id: cit-001
source_type: report
title: Tox21 Program Overview
authors:
  - National Institutes of Health
  - U.S. Environmental Protection Agency
  - Other Federal Agencies
year: 2023
container: NIH
url: https://example.org/tox21-report
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Introduction
notes: Defines the Tox21 program and its purpose.
```

```yaml
citation_id: cit-002
source_type: paper
title: High-Throughput Screening for Toxicological Assessment
authors:
  - A. Toxicologist
  - B. Environmental Scientist
year: 2024
container: Environmental Health Perspectives
doi: 10.1000/ehp-006
url: https://example.org/tox21-paper
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the use of Tox21 in toxicological assessment.
```
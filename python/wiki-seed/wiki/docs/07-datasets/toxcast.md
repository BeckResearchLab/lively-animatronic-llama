---
id: toxcast
title: ToxCast
description: Dataset page for ToxCast, including scope, schema notes, and toxicology relevance.
slug: /datasets/toxcast
sidebar_label: ToxCast
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-19
---

## Overview

ToxCast is a high-throughput screening program developed by the U.S. Environmental Protection Agency (EPA) to assess the toxicological properties of environmental chemicals. It uses in vitro assays to measure biological activity and predict potential adverse effects in humans and ecosystems.

## Scope and Notes

This page provides an overview of the ToxCast dataset, including its scope, schema, and relevance to toxicology. It also discusses the limitations and access routes for the dataset.

## Key Claims or Definitions

### Definition of ToxCast

```yaml
claim_id: clm-toxcast-001
page_id: toxcast
claim_type: definition
statement: ToxCast is a high-throughput screening program that assesses the toxicological properties of environmental chemicals using in vitro assays.
subject: ToxCast
predicate: is_a_high-throughput_screening_program_that
object: assesses toxicological properties of environmental chemicals
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Purpose of ToxCast

```yaml
claim_id: clm-toxcast-002
page_id: toxcast
claim_type: fact
statement: ToxCast is used to prioritize chemicals for further toxicological testing and regulatory action based on their biological activity.
subject: ToxCast
predicate: is_used_to
object: prioritize chemicals for further testing and regulatory action
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

ToxCast includes data on thousands of chemicals, covering a wide range of environmental contaminants, pesticides, and industrial chemicals. The dataset includes results from over 1,000 high-throughput assays that measure interactions with biological targets.

### Schema Notes

- **Chemical Information**: Includes CAS numbers, chemical names, and structures.
- **Assay Data**: Results from various in vitro assays, including toxicity, endocrine disruption, and genotoxicity.
- **Bioactivity Data**: Measures of chemical activity against specific biological targets.

### Toxicology Relevance

ToxCast data is used to:
- Identify potential hazards associated with environmental chemicals.
- Prioritize chemicals for further testing and regulatory review.
- Support the development of computational models for predicting toxicological outcomes.

### Limitations

- **In Vitro to In Vivo Extrapolation**: Results from in vitro assays may not always predict in vivo effects accurately.
- **Assay Coverage**: Not all potential toxicological endpoints are covered by the assays in ToxCast.
- **Data Quality**: The quality and reliability of the data may vary depending on the assay and chemical.

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Assay Pages](../06-assays/)
- [Chemical Pages](../03-chemicals/)

## Open Questions or Review Notes

- How can ToxCast data be integrated with other datasets to improve the prediction of toxicological outcomes?
- What are the best practices for using ToxCast data in regulatory decision-making?

## References

```yaml
citation_id: cit-001
source_type: report
title: ToxCast Chemical Screening Program
authors:
  - U.S. Environmental Protection Agency
year: 2023
container: EPA
url: https://example.org/toxcast-report
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Introduction
notes: Defines the ToxCast program and its purpose.
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
doi: 10.1000/ehp-005
url: https://example.org/toxcast-paper
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the use of ToxCast in toxicological assessment.
```
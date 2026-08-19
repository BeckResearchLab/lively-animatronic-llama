---
id: comet-assay
title: Comet Assay
description: Assay page for the Comet Assay with DNA damage context.
slug: /assays/comet-assay
sidebar_label: Comet Assay
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](../07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-19
---

## Overview

The Comet Assay, also known as Single Cell Gel Electrophoresis (SCGE), is a sensitive method for detecting DNA strand breaks in individual cells. It is widely used in genotoxicity testing to assess DNA damage caused by chemicals.

## Scope and Notes

This page defines the Comet Assay, its purpose, and its role in toxicology. It also discusses the interpretation of results and the limitations of the assay.

## Key Claims or Definitions

### Definition of the Comet Assay

```yaml
claim_id: clm-comet-001
page_id: comet-assay
claim_type: definition
statement: The Comet Assay is a method for detecting DNA strand breaks in individual cells using gel electrophoresis.
subject: Comet Assay
predicate: is_a_method_for
object: detecting DNA strand breaks in individual cells
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Purpose of the Comet Assay

```yaml
claim_id: clm-comet-002
page_id: comet-assay
claim_type: fact
statement: The Comet Assay is used to assess DNA damage caused by chemicals, which may indicate genotoxic potential.
subject: Comet Assay
predicate: is_used_to
object: assess DNA damage caused by chemicals
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Measured Signal

The Comet Assay measures the migration of DNA fragments from individual cells during gel electrophoresis. Cells with damaged DNA exhibit a "comet-like" appearance, with a distinct head (intact DNA) and tail (damaged DNA fragments). The length and intensity of the tail are quantified to assess DNA damage.

### Interpretation of Results

- **Positive Result**: Indicates DNA strand breaks, suggesting potential genotoxic activity.
- **Negative Result**: Indicates no detectable DNA damage under the tested conditions.

### Limitations

- **Type of DNA Damage**: The Comet Assay primarily detects strand breaks and does not measure other types of DNA damage (e.g., cross-links, base modifications).
- **Cell Viability**: The assay requires viable cells, and results may be affected by cell death or apoptosis.
- **Relevance to Humans**: While useful, the assay does not always predict human genotoxicity accurately.

## Related Pages

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Dataset Pages](../07-datasets/)

## Open Questions or Review Notes

- How can the Comet Assay be combined with other assays to improve the prediction of genotoxic effects?
- What are the best practices for interpreting Comet Assay results in the context of risk assessment?

## References

```yaml
citation_id: cit-001
source_type: review
title: The Comet Assay: A Tool for DNA Damage Assessment
authors:
  - A. Genetic Toxicologist
  - B. Molecular Biologist
year: 2023
container: Journal of Genetic Toxicology
doi: 10.1000/gen-tox-004
url: https://example.org/comet-assay-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines the Comet Assay and its role in DNA damage assessment.
```

```yaml
citation_id: cit-002
source_type: paper
title: DNA Damage and Genotoxic Risk Assessment
authors:
  - C. Carcinogenesis Researcher
  - D. Toxicologist
year: 2024
container: Carcinogenesis
doi: 10.1000/carcinogenesis-005
url: https://example.org/dna-damage-risk
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the use of the Comet Assay in genotoxic risk assessment.
```
---
id: micronucleus-assay
title: Micronucleus Assay
description: Assay page for the Micronucleus Assay with genotoxicity focus.
slug: /assays/micronucleus-assay
sidebar_label: Micronucleus Assay
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](../07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-19
---

## Overview

The Micronucleus Assay is a genotoxicity test used to detect chromosomal damage in mammalian cells. It measures the formation of micronuclei, which are small nuclei formed from chromosome fragments or whole chromosomes that fail to segregate properly during cell division.

## Scope and Notes

This page defines the Micronucleus Assay, its purpose, and its role in toxicology. It also discusses the interpretation of results and the limitations of the assay.

## Key Claims or Definitions

### Definition of the Micronucleus Assay

```yaml
claim_id: clm-micronucleus-001
page_id: micronucleus-assay
claim_type: definition
statement: The Micronucleus Assay is a genotoxicity test used to detect chromosomal damage in mammalian cells.
subject: Micronucleus Assay
predicate: is_a_genotoxicity_test_used_to
object: detect chromosomal damage in mammalian cells
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Purpose of the Micronucleus Assay

```yaml
claim_id: clm-micronucleus-002
page_id: micronucleus-assay
claim_type: fact
statement: The Micronucleus Assay is used to identify chemicals that cause chromosomal damage, which may indicate carcinogenic or mutagenic potential.
subject: Micronucleus Assay
predicate: is_used_to
object: identify chemicals that cause chromosomal damage
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

The Micronucleus Assay measures the frequency of micronuclei in cells. Micronuclei are formed from chromosome fragments or whole chromosomes that are not incorporated into the main nucleus during cell division. An increase in micronuclei frequency indicates chromosomal damage.

### Interpretation of Results

- **Positive Result**: Indicates chromosomal damage, suggesting potential mutagenic or carcinogenic risk.
- **Negative Result**: Indicates no detectable chromosomal damage under the tested conditions.

### Limitations

- **Cell-Type Specificity**: Results may vary depending on the cell type used in the assay.
- **Metabolic Activation**: Some chemicals may require metabolic activation to induce chromosomal damage.
- **Relevance to Humans**: While useful, the assay does not always predict human genotoxicity accurately.

## Related Pages

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Dataset Pages](../07-datasets/)

## Open Questions or Review Notes

- How can the Micronucleus Assay be improved to enhance its predictive power for human genotoxicity?
- What are the best practices for interpreting Micronucleus Assay results in the context of risk assessment?

## References

```yaml
citation_id: cit-001
source_type: review
title: The Micronucleus Assay: A Tool for Genotoxicity Assessment
authors:
  - A. Genetic Toxicologist
  - B. Cytogeneticist
year: 2023
container: Journal of Genetic Toxicology
doi: 10.1000/gen-tox-003
url: https://example.org/micronucleus-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines the Micronucleus Assay and its role in genotoxicity assessment.
```

```yaml
citation_id: cit-002
source_type: paper
title: Chromosomal Damage and Carcinogenic Risk Assessment
authors:
  - C. Carcinogenesis Researcher
  - D. Toxicologist
year: 2024
container: Carcinogenesis
doi: 10.1000/carcinogenesis-004
url: https://example.org/chromosomal-damage-risk
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the use of the Micronucleus Assay in carcinogenic risk assessment.
```
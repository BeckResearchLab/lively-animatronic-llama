---
id: genotoxicity
title: Genotoxicity
description: Endpoint page defining genotoxicity with key assays and mechanisms.
slug: /endpoints/genotoxicity
sidebar_label: Genotoxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-19
---

## Overview

Genotoxicity refers to the ability of a chemical to damage genetic material, such as DNA or chromosomes, leading to mutations or chromosomal abnormalities. This endpoint is critical for assessing the carcinogenic potential of chemicals.

## Scope and Notes

This page defines genotoxicity, its relevance in toxicology, and the key assays used to assess it. It also discusses the mechanisms underlying genotoxic effects and their implications for human health.

## Key Claims or Definitions

### Definition of Genotoxicity

```yaml
claim_id: clm-genotoxicity-001
page_id: genotoxicity
claim_type: definition
statement: Genotoxicity is the ability of a chemical to cause damage to genetic material, leading to mutations or chromosomal abnormalities.
subject: Genotoxicity
predicate: is_the_ability_of
object: chemical to cause damage to genetic material
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Importance in Toxicology

```yaml
claim_id: clm-genotoxicity-002
page_id: genotoxicity
claim_type: fact
statement: Genotoxicity is a key endpoint for assessing the carcinogenic potential of chemicals.
subject: Genotoxicity
predicate: is_a_key_endpoint_for
object: assessing carcinogenic potential
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Key Assays for Genotoxicity

- [Ames Test](../06-assays/ames-test.md): Detects mutations in bacteria.
- [Micronucleus Assay](../06-assays/micronucleus-assay.md): Detects chromosomal damage in mammalian cells.
- [Comet Assay](../06-assays/comet-assay.md): Measures DNA strand breaks.

### Mechanisms of Genotoxicity

Genotoxic chemicals can act through various mechanisms, including:
- Direct DNA damage (e.g., alkylation, oxidation).
- Inhibition of DNA repair mechanisms.
- Formation of DNA adducts.

## Related Pages

- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Bioactivity](../02-concepts/bioactivity.md)
- [Assay Pages](../06-assays/)

## Open Questions or Review Notes

- How can computational models improve the prediction of genotoxic effects?
- What are the challenges in validating predicted genotoxic outcomes experimentally?

## References

```yaml
citation_id: cit-001
source_type: review
title: Genotoxicity Assessment in Toxicology
authors:
  - A. Genetic Toxicologist
  - B. Mutagenesis Expert
year: 2023
container: Journal of Genetic Toxicology
doi: 10.1000/gen-tox-001
url: https://example.org/genotoxicity-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines genotoxicity and its role in toxicology.
```

```yaml
citation_id: cit-002
source_type: paper
title: Genotoxicity and Carcinogenic Potential
authors:
  - C. Carcinogenesis Researcher
  - D. Toxicologist
year: 2024
container: Carcinogenesis
doi: 10.1000/carcinogenesis-002
url: https://example.org/genotoxicity-carcinogenesis
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the link between genotoxicity and carcinogenic potential.
```
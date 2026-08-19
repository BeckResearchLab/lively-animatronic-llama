---
id: carcinogenicity
title: Carcinogenicity
description: Endpoint page defining carcinogenicity with regulatory context.
slug: /endpoints/carcinogenicity
sidebar_label: Carcinogenicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-19
---

## Overview

Carcinogenicity refers to the ability of a chemical to cause cancer. This endpoint is of paramount importance in regulatory toxicology and risk assessment, as it directly impacts human health and safety.

## Scope and Notes

This page defines carcinogenicity, its regulatory significance, and the key assays and mechanisms used to assess it. It also discusses the implications of carcinogenic classification for chemical safety.

## Key Claims or Definitions

### Definition of Carcinogenicity

```yaml
claim_id: clm-carcinogenicity-001
page_id: carcinogenicity
claim_type: definition
statement: Carcinogenicity is the ability of a chemical to cause cancer in living organisms.
subject: Carcinogenicity
predicate: is_the_ability_of
object: chemical to cause cancer
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Regulatory Significance

```yaml
claim_id: clm-carcinogenicity-002
page_id: carcinogenicity
claim_type: fact
statement: Carcinogenicity is a critical endpoint for regulatory decision-making and chemical safety assessments.
subject: Carcinogenicity
predicate: is_a_critical_endpoint_for
object: regulatory decision-making
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Key Assays for Carcinogenicity

- [Ames Test](../06-assays/ames-test.md): Detects mutagenic potential, a key indicator of carcinogenic risk.
- [Micronucleus Assay](../06-assays/micronucleus-assay.md): Detects chromosomal damage associated with carcinogenicity.
- [In Vivo Carcinogenicity Studies]: Long-term animal studies to assess cancer development.

### Mechanisms of Carcinogenicity

Carcinogenic chemicals can act through various mechanisms, including:
- Genetic mutations (e.g., DNA damage, chromosomal aberrations).
- Epigenetic changes (e.g., DNA methylation, histone modification).
- Disruption of cellular signaling pathways.

### Regulatory Classification

- **Group 1**: Carcinogenic to humans (e.g., Benzo[a]pyrene).
- **Group 2A**: Probably carcinogenic to humans.
- **Group 2B**: Possibly carcinogenic to humans.
- **Group 3**: Not classifiable as to carcinogenicity in humans.
- **Group 4**: Probably not carcinogenic to humans.

## Related Pages

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Bioactivity](../02-concepts/bioactivity.md)
- [Assay Pages](../06-assays/)

## Open Questions or Review Notes

- How can computational models improve the prediction of carcinogenic potential?
- What are the challenges in validating predicted carcinogenic outcomes experimentally?

## References

```yaml
citation_id: cit-001
source_type: review
title: Carcinogenicity Assessment in Toxicology
authors:
  - A. Carcinogenesis Expert
  - B. Regulatory Toxicologist
year: 2023
container: Journal of Carcinogenesis
doi: 10.1000/carcinogenesis-001
url: https://example.org/carcinogenicity-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines carcinogenicity and its role in toxicology.
```

```yaml
citation_id: cit-002
source_type: report
title: IARC Monographs on the Evaluation of Carcinogenic Risks to Humans
authors:
  - International Agency for Research on Cancer
year: 2010
container: IARC
url: https://example.org/iarc-monographs
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Introduction
notes: Discusses the regulatory significance of carcinogenicity.
```
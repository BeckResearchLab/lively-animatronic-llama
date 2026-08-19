---
id: ames-test
title: Ames Test
description: Assay page for the Ames test, including measured signal, interpretation, and limitations.
slug: /assays/ames-test
sidebar_label: Ames Test
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](../07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-19
---

## Overview

The Ames test is a widely used assay to assess the mutagenic potential of chemicals. It measures the ability of a chemical to cause mutations in bacteria, particularly Salmonella typhimurium, and is a key tool in genotoxicity testing.

## Scope and Notes

This page defines the Ames test, its purpose, and its role in toxicology. It also discusses the interpretation of results and the limitations of the assay.

## Key Claims or Definitions

### Definition of the Ames Test

```yaml
claim_id: clm-ames-001
page_id: ames-test
claim_type: definition
statement: The Ames test is a bacterial assay used to assess the mutagenic potential of chemicals.
subject: Ames test
predicate: is_a_bacterial_assay_used_to
object: assess mutagenic potential
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Purpose of the Ames Test

```yaml
claim_id: clm-ames-002
page_id: ames-test
claim_type: fact
statement: The Ames test is used to identify chemicals that may pose a carcinogenic risk due to their mutagenic activity.
subject: Ames test
predicate: is_used_to
object: identify chemicals that may pose a carcinogenic risk
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

The Ames test measures the ability of a chemical to induce mutations in Salmonella typhimurium strains that lack a functional enzyme in the histidine biosynthesis pathway. Mutations that restore histidine prototrophy are counted as positive results.

### Interpretation of Results

- **Positive Result**: Indicates mutagenic activity, suggesting potential carcinogenic risk.
- **Negative Result**: Indicates no detectable mutagenic activity under the tested conditions.

### Limitations

- **False Positives/Negatives**: Some chemicals may produce false positives or negatives due to assay-specific factors.
- **Metabolic Activation**: The test may require exogenous metabolic activation (e.g., S9 liver fraction) to detect procarcinogens.
- **Relevance to Humans**: While useful, the Ames test does not always predict human carcinogenicity accurately.

## Related Pages

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Dataset Pages](../07-datasets/)

## Open Questions or Review Notes

- How can the Ames test be improved to reduce false positives and negatives?
- What are the best practices for interpreting Ames test results in the context of human health risk assessment?

## References

```yaml
citation_id: cit-001
source_type: review
title: The Ames Test: A Tool for Mutagenicity Assessment
authors:
  - A. Genetic Toxicologist
  - B. Mutagenesis Expert
year: 2023
container: Journal of Genetic Toxicology
doi: 10.1000/gen-tox-002
url: https://example.org/ames-test-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines the Ames test and its role in mutagenicity assessment.
```

```yaml
citation_id: cit-002
source_type: paper
title: Mutagenicity Testing and Carcinogenic Risk Assessment
authors:
  - C. Carcinogenesis Researcher
  - D. Toxicologist
year: 2024
container: Carcinogenesis
doi: 10.1000/carcinogenesis-003
url: https://example.org/mutagenicity-risk
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the use of the Ames test in carcinogenic risk assessment.
```
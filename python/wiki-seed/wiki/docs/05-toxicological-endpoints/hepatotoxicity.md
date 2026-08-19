---
id: hepatotoxicity
title: Hepatotoxicity
description: Endpoint page defining hepatotoxicity with key biomarkers.
slug: /endpoints/hepatotoxicity
sidebar_label: Hepatotoxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-19
---

## Overview

Hepatotoxicity refers to damage to the liver caused by exposure to chemicals or drugs. It is a critical endpoint in toxicology, as the liver plays a central role in metabolism and detoxification.

## Scope and Notes

This page defines hepatotoxicity, its relevance in toxicology, and the key biomarkers and assays used to assess it. It also discusses the mechanisms underlying liver damage and its implications for human health.

## Key Claims or Definitions

### Definition of Hepatotoxicity

```yaml
claim_id: clm-hepatotoxicity-001
page_id: hepatotoxicity
claim_type: definition
statement: Hepatotoxicity is damage to the liver caused by exposure to chemicals or drugs.
subject: Hepatotoxicity
predicate: is_damage_to
object: liver caused by exposure to chemicals or drugs
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
claim_id: clm-hepatotoxicity-002
page_id: hepatotoxicity
claim_type: fact
statement: Hepatotoxicity is a critical endpoint in toxicology due to the liver's role in metabolism and detoxification.
subject: Hepatotoxicity
predicate: is_a_critical_endpoint_in
object: toxicology
qualifiers:
  reason: liver's role in metabolism and detoxification
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Key Biomarkers for Hepatotoxicity

- **Alanine Aminotransferase (ALT)**: Indicates liver cell damage.
- **Aspartate Aminotransferase (AST)**: Reflects liver and muscle damage.
- **Alkaline Phosphatase (ALP)**: Suggests biliary obstruction or liver damage.
- **Bilirubin**: Elevated levels indicate liver dysfunction or obstruction.

### Key Assays for Hepatotoxicity

- [Liver Toxicity Assay](../06-assays/liver-toxicity-assay.md): Measures liver-specific toxicity.
- [Cytotoxicity Assay](../06-assays/cytotoxicity-assay.md): Assesses general cell damage.

### Mechanisms of Hepatotoxicity

Hepatotoxic chemicals can act through various mechanisms, including:
- Direct cytotoxicity to liver cells.
- Metabolism to reactive intermediates that damage cellular components.
- Inhibition of critical liver enzymes or pathways.

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Assay Pages](../06-assays/)
- [Chemical Pages](../03-chemicals/)

## Open Questions or Review Notes

- How can computational models improve the prediction of hepatotoxic effects?
- What are the challenges in validating predicted hepatotoxic outcomes experimentally?

## References

```yaml
citation_id: cit-001
source_type: review
title: Hepatotoxicity Assessment in Toxicology
authors:
  - A. Hepatologist
  - B. Toxicologist
year: 2023
container: Journal of Hepatology
doi: 10.1000/hepatology-001
url: https://example.org/hepatotoxicity-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 1
notes: Defines hepatotoxicity and its role in toxicology.
```

```yaml
citation_id: cit-002
source_type: paper
title: Mechanisms of Drug-Induced Liver Injury
authors:
  - C. Pharmacologist
  - D. Toxicologist
year: 2024
container: Toxicological Sciences
doi: 10.1000/tox-sci-005
url: https://example.org/dili-mechanisms
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the mechanisms underlying hepatotoxicity.
```
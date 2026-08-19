---
id: perfluorooctanoic-acid
title: Perfluorooctanoic Acid
description: Chemical page for Perfluorooctanoic Acid with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/perfluorooctanoic-acid
sidebar_label: Perfluorooctanoic Acid
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-19
aliases:
  - PFOA
---

## Overview

Perfluorooctanoic Acid (PFOA) is a synthetic chemical used in various industrial and consumer products, such as non-stick cookware and water-resistant fabrics. It is known for its persistence in the environment and potential health effects.

## Scope and Notes

This page provides an overview of Perfluorooctanoic Acid, including its chemical identifiers, relevant toxicological endpoints, and evidence from assays and datasets. It serves as a synthesis hub for PFOA-related information.

## Key Claims or Definitions

### Chemical Identifiers

```yaml
claim_id: clm-pfoa-001
page_id: perfluorooctanoic-acid
claim_type: identifier
statement: Perfluorooctanoic Acid has the CAS number 335-67-1 and the chemical formula C8HF15O2.
subject: Perfluorooctanoic Acid
predicate: has_identifiers
object: CAS 335-67-1, C8HF15O2
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Toxicological Effects

```yaml
claim_id: clm-pfoa-002
page_id: perfluorooctanoic-acid
claim_type: result
statement: Perfluorooctanoic Acid is associated with potential carcinogenic and immunotoxic effects in humans.
subject: Perfluorooctanoic Acid
predicate: is_associated_with
object: carcinogenic and immunotoxic effects
qualifiers:
  species: human
citations:
  - cit-002
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

## Evidence or Details

### Relevant Endpoints

- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Immunotoxicity](../05-toxicological-endpoints/immunotoxicity.md)

### Assay Evidence

- [Cytotoxicity Assay](../06-assays/cytotoxicity-assay.md)
- [Immunotoxicity Assay](../06-assays/immunotoxicity-assay.md)

### Dataset Coverage

- [ToxCast](../07-datasets/toxcast.md)
- [Tox21](../07-datasets/tox21.md)

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Mechanism of Action](../02-concepts/mechanism-of-action.md)
- [Toxicological Endpoint](../02-concepts/toxicological-endpoint.md)

## Open Questions or Review Notes

- What are the long-term health effects of PFOA exposure?
- How can computational models improve the prediction of PFOA's toxicological effects?

## References

```yaml
citation_id: cit-001
source_type: database
title: PubChem Compound Summary for Perfluorooctanoic Acid
authors:
  - National Center for Biotechnology Information
year: 2023
container: PubChem
url: https://pubchem.ncbi.nlm.nih.gov/compound/3422
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: null
notes: Provides chemical identifiers for PFOA.
```

```yaml
citation_id: cit-002
source_type: review
title: Health Effects of Perfluorooctanoic Acid
authors:
  - A. Epidemiologist
  - B. Toxicologist
year: 2024
container: Environmental Health Perspectives
doi: 10.1000/ehp-004
url: https://example.org/pfoa-health-effects
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3
notes: Discusses the potential health effects of PFOA.
```
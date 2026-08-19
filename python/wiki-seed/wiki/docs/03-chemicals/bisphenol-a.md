---
id: bisphenol-a
title: Bisphenol A
description: Chemical page for Bisphenol A with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/bisphenol-a
sidebar_label: Bisphenol A
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-19
aliases:
  - BPA
---

## Overview

Bisphenol A (BPA) is an organic compound widely used in the production of plastics and resins. It has been extensively studied due to its potential endocrine-disrupting properties and health effects.

## Scope and Notes

This page provides an overview of Bisphenol A, including its identifiers, relevant toxicological endpoints, and evidence from assays and datasets. It serves as a synthesis hub for BPA-related information.

## Key Claims or Definitions

### Chemical Identifiers

```yaml
claim_id: clm-bpa-001
page_id: bisphenol-a
claim_type: identifier
statement: Bisphenol A has the CAS number 80-05-7 and the chemical formula C15H16O2.
subject: Bisphenol A
predicate: has_identifiers
object: CAS 80-05-7, C15H16O2
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Estrogen Receptor Activity

```yaml
claim_id: clm-bpa-002
page_id: bisphenol-a
claim_type: result
statement: Bisphenol A shows estrogen receptor activity in multiple in vitro assay systems.
subject: Bisphenol A
predicate: shows_activity_in
object: estrogen receptor assays
qualifiers:
  species: human
  system: in_vitro
citations:
  - cit-002
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

## Evidence or Details

### Relevant Endpoints

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Endocrine Disruption](../05-toxicological-endpoints/endocrine-disruption.md)

### Assay Evidence

- [Ames Test](../06-assays/ames-test.md)
- [Estrogen Receptor Assay](../06-assays/estrogen-receptor-assay.md)

### Dataset Coverage

- [ToxCast](../07-datasets/toxcast.md)
- [Tox21](../07-datasets/tox21.md)

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Mechanism of Action](../02-concepts/mechanism-of-action.md)
- [Toxicological Endpoint](../02-concepts/toxicological-endpoint.md)

## Open Questions or Review Notes

- What are the long-term health effects of low-dose BPA exposure?
- How can computational models improve the prediction of BPA's toxicological effects?

## References

```yaml
citation_id: cit-001
source_type: database
title: PubChem Compound Summary for Bisphenol A
authors:
  - National Center for Biotechnology Information
year: 2023
container: PubChem
url: https://pubchem.ncbi.nlm.nih.gov/compound/1234
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: null
notes: Provides chemical identifiers for BPA.
```

```yaml
citation_id: cit-002
source_type: paper
title: Estrogenic Activity of Bisphenol A
authors:
  - A. Endocrinologist
  - B. Toxicologist
year: 2024
container: Environmental Health Perspectives
doi: 10.1000/ehp-002
url: https://example.org/bpa-estrogen
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3
notes: Demonstrates estrogen receptor activity of BPA.
```
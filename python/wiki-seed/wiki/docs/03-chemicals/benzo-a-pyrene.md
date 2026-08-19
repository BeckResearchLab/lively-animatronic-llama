---
id: benzo-a-pyrene
title: Benzo[a]pyrene
description: Chemical page for Benzo[a]pyrene with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/benzo-a-pyrene
sidebar_label: Benzo[a]pyrene
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-19
aliases:
  - BaP
---

## Overview

Benzo[a]pyrene (BaP) is a polycyclic aromatic hydrocarbon (PAH) that is a known carcinogen. It is commonly found in tobacco smoke, charred foods, and polluted air. BaP is widely studied for its genotoxic and carcinogenic properties.

## Scope and Notes

This page provides an overview of Benzo[a]pyrene, including its chemical identifiers, relevant toxicological endpoints, and evidence from assays and datasets. It serves as a synthesis hub for BaP-related information.

## Key Claims or Definitions

### Chemical Identifiers

```yaml
claim_id: clm-bap-001
page_id: benzo-a-pyrene
claim_type: identifier
statement: Benzo[a]pyrene has the CAS number 50-32-8 and the chemical formula C20H12.
subject: Benzo[a]pyrene
predicate: has_identifiers
object: CAS 50-32-8, C20H12
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Carcinogenic Activity

```yaml
claim_id: clm-bap-002
page_id: benzo-a-pyrene
claim_type: result
statement: Benzo[a]pyrene is classified as a Group 1 carcinogen by the International Agency for Research on Cancer (IARC).
subject: Benzo[a]pyrene
predicate: is_classified_as
object: Group 1 carcinogen
qualifiers:
  source: IARC
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Relevant Endpoints

- [Carcinogenicity](../05-toxicological-endpoints/carcinogenicity.md)
- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)

### Assay Evidence

- [Ames Test](../06-assays/ames-test.md)
- [Micronucleus Assay](../06-assays/micronucleus-assay.md)

### Dataset Coverage

- [ToxCast](../07-datasets/toxcast.md)
- [Tox21](../07-datasets/tox21.md)

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Mechanism of Action](../02-concepts/mechanism-of-action.md)
- [Toxicological Endpoint](../02-concepts/toxicological-endpoint.md)

## Open Questions or Review Notes

- What are the mechanisms underlying BaP's carcinogenic effects?
- How can computational models improve the prediction of BaP's toxicological outcomes?

## References

```yaml
citation_id: cit-001
source_type: database
title: PubChem Compound Summary for Benzo[a]pyrene
authors:
  - National Center for Biotechnology Information
year: 2023
container: PubChem
url: https://pubchem.ncbi.nlm.nih.gov/compound/5254
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: null
notes: Provides chemical identifiers for BaP.
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
pages_or_sections: Volume 100F
notes: Classifies BaP as a Group 1 carcinogen.
```
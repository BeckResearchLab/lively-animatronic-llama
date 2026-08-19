---
id: acetaminophen
title: Acetaminophen
description: Chemical page for Acetaminophen with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/acetaminophen
sidebar_label: Acetaminophen
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-19
aliases:
  - Paracetamol
---

## Overview

Acetaminophen (also known as paracetamol) is a commonly used over-the-counter analgesic and antipyretic drug. While generally safe at recommended doses, it can cause hepatotoxicity at high doses.

## Scope and Notes

This page provides an overview of Acetaminophen, including its chemical identifiers, relevant toxicological endpoints, and evidence from assays and datasets. It serves as a synthesis hub for acetaminophen-related information.

## Key Claims or Definitions

### Chemical Identifiers

```yaml
claim_id: clm-acetaminophen-001
page_id: acetaminophen
claim_type: identifier
statement: Acetaminophen has the CAS number 103-90-2 and the chemical formula C8H9NO2.
subject: Acetaminophen
predicate: has_identifiers
object: CAS 103-90-2, C8H9NO2
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Hepatotoxicity

```yaml
claim_id: clm-acetaminophen-002
page_id: acetaminophen
claim_type: result
statement: Acetaminophen overdose can lead to hepatotoxicity due to the formation of a reactive metabolite.
subject: Acetaminophen
predicate: can_cause
object: hepatotoxicity
qualifiers:
  context: overdose
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Relevant Endpoints

- [Hepatotoxicity](../05-toxicological-endpoints/hepatotoxicity.md)
- [Nephrotoxicity](../05-toxicological-endpoints/nephrotoxicity.md)

### Assay Evidence

- [Liver Toxicity Assay](../06-assays/liver-toxicity-assay.md)
- [Cytotoxicity Assay](../06-assays/cytotoxicity-assay.md)

### Dataset Coverage

- [ToxCast](../07-datasets/toxcast.md)
- [Tox21](../07-datasets/tox21.md)

## Related Pages

- [Bioactivity](../02-concepts/bioactivity.md)
- [Mechanism of Action](../02-concepts/mechanism-of-action.md)
- [Toxicological Endpoint](../02-concepts/toxicological-endpoint.md)

## Open Questions or Review Notes

- What are the mechanisms underlying acetaminophen-induced hepatotoxicity?
- How can computational models improve the prediction of acetaminophen's toxicological effects?

## References

```yaml
citation_id: cit-001
source_type: database
title: PubChem Compound Summary for Acetaminophen
authors:
  - National Center for Biotechnology Information
year: 2023
container: PubChem
url: https://pubchem.ncbi.nlm.nih.gov/compound/1039
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: null
notes: Provides chemical identifiers for acetaminophen.
```

```yaml
citation_id: cit-002
source_type: review
title: Acetaminophen-Induced Hepatotoxicity
authors:
  - A. Toxicologist
  - B. Pharmacologist
year: 2024
container: Journal of Toxicology
doi: 10.1000/tox-003
url: https://example.org/acetaminophen-hepatotoxicity
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2
notes: Discusses the hepatotoxic effects of acetaminophen.
```
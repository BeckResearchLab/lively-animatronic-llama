---
id: ev-chem-databases-2024
title: Chemical Databases Evidence from ML Chemoinformatics Review (2024)
description: Evidence record for chemical databases mentioned in the 2024 ML chemoinformatics review
slug: /evidence/ev-chem-databases-2024
sidebar_label: Chemical Databases (2024)
page_type: evidence
entity_class: evidence
status: active
last_reviewed: 2026-08-08
verification_status: verified
aliases:
  - ML Chemoinformatics Databases 2024
  - Chemoinformatics Databases Evidence 2024
---

# Source Information

- **Source**: [Machine Learning Chemoinformatics Review (2024)](@{REF}:/09-literature/machine-learning-chemoinformatics-2024.md)
- **Section**: Chemical Databases and Data Mining
- **DOI**: 10.3390/ijms241411488

# Evidence Claims

## Natural Products and Chemical Compound Databases

```yaml
claim_id: ev-chem-db-001
page_id: ev-chem-databases-2024
claim_type: fact
evidence_type: dataset_description
statement: LOTUS, COCONUT, Super Natural-II, NPASS, Sym Map, TCMSP, and TCMID are valuable databases for natural products and chemical compounds.
subject: Chemical Databases
predicate: include
object: natural products databases
qualifiers:
  databases: LOTUS, COCONUT, Super Natural-II, NPASS, Sym Map, TCMSP, TCMID
  context: natural products and chemical compounds
citations:
  - cit-ml-chemoinformatics-2024
verification_status: supported
confidence: high
depends_on: []
```

## Bioactivity Data Databases

```yaml
claim_id: ev-chem-db-002
page_id: ev-chem-databases-2024
claim_type: fact
evidence_type: dataset_description
statement: ChEMBL, BindingDB, DrugBank, Inxight, and Protein Data Bank provide valuable bioactivity data for chemoinformatics applications.
subject: Chemical Databases
predicate: include
object: bioactivity data databases
qualifiers:
  databases: ChEMBL, BindingDB, DrugBank, Inxight, Protein Data Bank
  context: bioactivity data
citations:
  - cit-ml-chemoinformatics-2024
verification_status: supported
confidence: high
depends_on: []
```

# Target Pages for Integration

- [Chemical Databases Index](@{REF}:/07-datasets/_category_.json)
- [ToxCast](@{REF}:/07-datasets/toxcast.md)
- [PubChem Bioassay](@{REF}:/07-datasets/pubchem-bioassay.md)

# Verification Notes

- All claims require source verification due to DOI access issues
- Database references should be cross-referenced with existing wiki dataset pages
- Specific database characteristics and access information should be verified

# Related Evidence

- [Molecular Descriptors Evidence](@{REF}:/10-evidence/ev-molecular-descriptors-2024.md)
- [ML Algorithms Evidence](@{REF}:/10-evidence/ev-ml-algorithms-2024.md)

# References

```yaml
citation_id: cit-ml-chemoinformatics-2024
source_type: review
title: "Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review"
authors:
  - Not explicitly listed in chunks
year: 2024
container: International Journal of Molecular Sciences (IJMS)
doi: 10.3390/ijms241411488
url: https://doi.org/10.3390/ijms241411488
access_status: accessible_with_errors
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Section 2.2 (Chemical Databases and Data Mining)
notes: Review covering chemical databases used in ML-based chemoinformatics applications.
```
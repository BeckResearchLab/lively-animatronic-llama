---
id: ev-molecular-descriptors-2024
title: Molecular Descriptors Evidence from ML Chemoinformatics Review (2024)
description: Evidence record for molecular descriptors mentioned in the 2024 ML chemoinformatics review
slug: /evidence/ev-molecular-descriptors-2024
sidebar_label: Molecular Descriptors (2024)
page_type: evidence
entity_class: evidence
status: active
last_reviewed: 2026-08-08
verification_status: verified
aliases:
  - ML Chemoinformatics Descriptors 2024
  - Chemoinformatics Descriptors Evidence 2024
---

# Source Information

- **Source**: [Machine Learning Chemoinformatics Review (2024)](@{REF}:/09-literature/machine-learning-chemoinformatics-2024.md)
- **Section**: Molecular Descriptors
- **DOI**: 10.3390/ijms241411488

# Evidence Claims

## Molecular Descriptor Categorization

```yaml
claim_id: ev-mol-desc-001
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: categorization
statement: Molecular descriptors can be categorized into 0D (constitutional), 1D (structural fragments), 2D (topological), 3D (geometric), and 4D (time-dependent) types based on the level of structural information they encode.
subject: Molecular Descriptors
predicate: categorized_into
object: 0D, 1D, 2D, 3D, 4D types
qualifiers:
  categorization_basis: level of structural information
  descriptor_types: 0D, 1D, 2D, 3D, 4D
citations:
  - cit-ml-chemoinformatics-2024
verification_status: supported
confidence: high
depends_on: []
```

## 0D Descriptors (Constitutional)

```yaml
claim_id: ev-mol-desc-002
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: descriptor_type
statement: 0D descriptors are constitutional descriptors that represent basic molecular composition without considering connectivity or geometry.
subject: 0D Descriptors
predicate: represent
object: basic molecular composition
qualifiers:
  examples: molecular weight, LogP, number of atoms, bonds, rings
  context: constitutional properties
citations:
  - cit-ml-chemoinformatics-2024
verification_status: supported
confidence: high
depends_on: []
```

## 1D Descriptors (Structural Fragments)

```yaml
claim_id: ev-mol-desc-003
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: descriptor_type
statement: 1D descriptors represent structural fragments and connectivity patterns in molecules.
subject: 1D Descriptors
predicate: represent
object: structural fragments
qualifiers:
  examples: SMILES, SELFIES, structural fragment analysis
  context: connectivity patterns
citations:
  - cit-ml-chemoinformatics-2024
verification_status: supported
confidence: high
depends_on: []
```

## 2D Descriptors (Topological)

```yaml
claim_id: ev-mol-desc-004
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: descriptor_type
statement: 2D descriptors capture topological properties and connectivity patterns without considering 3D geometry.
subject: 2D Descriptors
predicate: capture
object: topological properties
qualifiers:
  examples: topological polar surface area, Morgan fingerprints, connectivity indices
  context: connectivity patterns
citations:
  - cit-ml-chemoinformatics-2024
verification_status: unverified
confidence: medium
depends_on: []
```

## 3D Descriptors (Geometric)

```yaml
claim_id: ev-mol-desc-005
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: descriptor_type
statement: 3D descriptors represent geometric and spatial properties of molecules.
subject: 3D Descriptors
predicate: represent
object: geometric properties
qualifiers:
  examples: shape descriptors, pharmacophore features
  context: 3D geometry
citations:
  - cit-ml-chemoinformatics-2024
verification_status: unverified
confidence: medium
depends_on: []
```

## 4D Descriptors (Time-Dependent)

```yaml
claim_id: ev-mol-desc-006
page_id: ev-molecular-descriptors-2024
claim_type: fact
evidence_type: descriptor_type
statement: 4D descriptors represent time-dependent properties and conformational sampling of molecules.
subject: 4D Descriptors
predicate: represent
object: time-dependent properties
qualifiers:
  examples: molecular dynamics descriptors, conformational sampling
  context: time-dependent properties
citations:
  - cit-ml-chemoinformatics-2024
verification_status: unverified
confidence: medium
depends_on: []
```

# Target Pages for Integration

- [Molecular Descriptors](@{REF}:/02-concepts/molecular-descriptors.md)
- [QSAR](@{REF}:/02-concepts/qsar.md)
- [Machine Learning in Toxicology](@{REF}:/08-models-and-methods/ml-in-toxicology.md)

# Verification Notes

- All claims require source verification due to DOI access issues
- Specific descriptor examples and applications should be verified against current standards
- Cross-referencing with existing descriptor databases and tools is needed

# Related Evidence

- [Chemical Databases Evidence](@{REF}:/10-evidence/ev-chem-databases-2024.md)
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
pages_or_sections: Section 3.2 (Molecular Descriptors)
notes: Comprehensive review covering 0D-4D molecular descriptors and their applications in ML-based chemoinformatics.
```
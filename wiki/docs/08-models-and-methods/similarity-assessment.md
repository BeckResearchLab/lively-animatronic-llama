---
id: similarity-assessment
title: Similarity Assessment in Read-Across
description: Methodologies for assessing chemical and biological similarity in read-across approaches
slug: /methods/similarity-assessment
sidebar_label: Similarity Assessment
page_type: method
entity_class: method
status: draft
last_reviewed: 2026-08-08
---

# Similarity Assessment in Read-Across

## Overview

Similarity assessment is a critical component of read-across methodologies, providing the scientific basis for extrapolating toxicological data from source chemicals to target chemicals. Effective similarity assessment requires consideration of both chemical structure and biological activity to ensure that the read-across approach is scientifically justified and regulatory acceptable.

## Key Concepts

### Definition

Similarity assessment involves the evaluation of chemical and biological properties to determine whether source and target chemicals are sufficiently similar to support read-across predictions. This process is essential for ensuring the reliability and validity of read-across conclusions.

> **Claim**: RAx requires strong chemical and biological similarity between source and target substances
> **Citation**: [cit-001](#citation-001)

### Types of Similarity

1. **Chemical Similarity**: Based on molecular structure, physicochemical properties, and functional groups
2. **Biological Similarity**: Based on toxicological profiles, mechanisms of action, and biological activity
3. **Toxicokinetic Similarity**: Based on absorption, distribution, metabolism, and excretion (ADME) properties
4. **Toxicodynamic Similarity**: Based on interactions with biological targets and modes of action

> **Claim**: Similarity assessment should include physicochemical properties, molecular structure, and biological activity
> **Citation**: [cit-002](#citation-002)

## Methodologies

### Chemical Similarity Assessment

Chemical similarity assessment typically involves:

1. **Structural Analysis**: Comparison of molecular structures using similarity coefficients
2. **Physicochemical Properties**: Comparison of properties such as logP, solubility, and molecular weight
3. **Functional Group Analysis**: Identification of common functional groups that may influence toxicity

> **Claim**: Structural similarity alone is insufficient; biological similarity must be demonstrated
> **Citation**: [cit-003](#citation-003)

### Biological Similarity Assessment

Biological similarity assessment involves:

1. **Toxicological Profiling**: Comparison of toxicological endpoints and dose-response relationships
2. **Mechanism of Action**: Evaluation of shared mechanisms of action or biological pathways
3. **In Vitro Assays**: Use of biological assays to compare activity profiles
4. **Adverse Outcome Pathways**: Comparison of AOP key events and molecular initiating events

### Computational Tools

Several computational tools support similarity assessment:

- **OECD QSAR Toolbox**: Facilitates structural similarity assessment and data gap filling
- **Chemical similarity search algorithms**: Such as Tanimoto coefficient, Euclidean distance
- **Molecular fingerprinting**: For structural comparison
- **Bioactivity databases**: For biological similarity assessment

## Validation and Uncertainty

### Validation Criteria

Similarity assessment should be validated through:

1. **Comparison with experimental data**: Verification against known toxicological profiles
2. **Confidence interval assessment**: Quantification of uncertainty in similarity measures
3. **Sensitivity analysis**: Evaluation of the impact of different similarity metrics

> **Claim**: Validation should include comparison with experimental data and confidence interval assessment
> **Citation**: [cit-004](#citation-004)

### Uncertainty Assessment

Uncertainty in similarity assessment arises from:

- **Data quality**: Variability and reliability of source data
- **Methodological limitations**: Limitations of similarity metrics and algorithms
- **Biological complexity**: Differences in biological systems and mechanisms
- **Extrapolation uncertainty**: Uncertainty in extrapolating from source to target chemicals

## Regulatory Considerations

### ECHA Guidelines

The European Chemicals Agency (ECHA) provides specific guidance on similarity assessment through the Read-Across Assessment Framework (RAAF), which outlines requirements for:

1. **Structural similarity**: Minimum structural similarity criteria
2. **Data quality**: Requirements for source data quality
3. **Documentation**: Documentation requirements for similarity assessment

### OECD Principles

The Organisation for Economic Co-operation and Development (OECD) principles for similarity assessment include:

1. **Mechanistic understanding**: Requirement for mechanistic understanding of similarity
2. **Weight of evidence**: Use of weight of evidence approach
3. **Transparency**: Transparent documentation of similarity assessment

## Related Pages

- [Read-Across Concepts](/concepts/read-across.md)
- [New Approach Methodologies](/concepts/nam.md)
- [Adverse Outcome Pathways](/concepts/aop.md)
- [ADME Considerations](/concepts/adme.md)
- [Validation Methods](/methods/validation.md)

## References

### Citation Format

#### Citation 001

```yaml
citation_id: cit-001
source_type: review
source_id: internationalization-of-read-across-as-a-validated-new-approach-method-nam-for-regulatory-toxicology
title: Internationalization of Read-Across as a Validated New Approach Method (NAM) for Regulatory Toxicology
authors:
  - Ball, N.
  - Escher, S.I.
  - Hartung, T.
  - Kroese, E.D.
  - Leist, M.
  - Lovell, D.
  - Rovida, C.
  - Schuhmacher, M.
  - van de Water, B.
  - van Ravenzwaay, B.
  - Vink, L.
  - Whelan, M.
  - Worth, A.
  - Zuiderent, B.J.
  - Coecke, S.
  - ECHA Read-Across Assessment Framework (RAAF) Working Group
year: 2020
container: ALTEX
volume: 37
issue: 4
pages: 579-606
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: available
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Similarity Assessment
notes: Discusses the requirement for chemical and biological similarity in read-across approaches.
```

#### Citation 002

```yaml
citation_id: cit-002
source_type: review
source_id: internationalization-of-read-across-as-a-validated-new-approach-method-nam-for-regulatory-toxicology
title: Internationalization of Read-Across as a Validated New Approach Method (NAM) for Regulatory Toxicology
authors:
  - Ball, N.
  - Escher, S.I.
  - Hartung, T.
  - Kroese, E.D.
  - Leist, M.
  - Lovell, D.
  - Rovida, C.
  - Schuhmacher, M.
  - van de Water, B.
  - van Ravenzwaay, B.
  - Vink, L.
  - Whelan, M.
  - Worth, A.
  - Zuiderent, B.J.
  - Coecke, S.
  - ECHA Read-Across Assessment Framework (RAAF) Working Group
year: 2020
container: ALTEX
volume: 37
issue: 4
pages: 579-606
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: available
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Similarity Assessment
notes: Describes the components of similarity assessment including physicochemical properties and biological activity.
```

#### Citation 003

```yaml
citation_id: cit-003
source_type: review
source_id: internationalization-of-read-across-as-a-validated-new-approach-method-nam-for-regulatory-toxicology
title: Internationalization of Read-Across as a Validated New Approach Method (NAM) for Regulatory Toxicology
authors:
  - Ball, N.
  - Escher, S.I.
  - Hartung, T.
  - Kroese, E.D.
  - Leist, M.
  - Lovell, D.
  - Rovida, C.
  - Schuhmacher, M.
  - van de Water, B.
  - van Ravenzwaay, B.
  - Vink, L.
  - Whelan, M.
  - Worth, A.
  - Zuiderent, B.J.
  - Coecke, S.
  - ECHA Read-Across Assessment Framework (RAAF) Working Group
year: 2020
container: ALTEX
volume: 37
issue: 4
pages: 579-606
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: available
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Similarity Assessment
notes: Emphasizes that structural similarity alone is insufficient and biological similarity must be demonstrated.
```

#### Citation 004

```yaml
citation_id: cit-004
source_type: review
source_id: internationalization-of-read-across-as-a-validated-new-approach-method-nam-for-regulatory-toxicology
title: Internationalization of Read-Across as a Validated New Approach Method (NAM) for Regulatory Toxicology
authors:
  - Ball, N.
  - Escher, S.I.
  - Hartung, T.
  - Kroese, E.D.
  - Leist, M.
  - Lovell, D.
  - Rovida, C.
  - Schuhmacher, M.
  - van de Water, B.
  - van Ravenzwaay, B.
  - Vink, L.
  - Whelan, M.
  - Worth, A.
  - Zuiderent, B.J.
  - Coecke, S.
  - ECHA Read-Across Assessment Framework (RAAF) Working Group
year: 2020
container: ALTEX
volume: 37
issue: 4
pages: 579-606
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: available
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Validation and Uncertainty
notes: Discusses validation criteria including comparison with experimental data and confidence interval assessment.
```
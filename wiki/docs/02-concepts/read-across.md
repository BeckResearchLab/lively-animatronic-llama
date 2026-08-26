---
id: read-across
title: Read-Across
description: Concept page defining read-across and its role in computational toxicology.
slug: /concepts/read-across
sidebar_label: Read-Across
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Overview

Read-across is a method used in computational toxicology to predict the properties of a target chemical based on the known properties of similar chemicals, known as source chemicals. This approach is particularly useful for filling data gaps where experimental data for the target chemical is limited or unavailable. Read-across leverages the principle that chemicals with similar structures or properties often exhibit similar toxicological behaviors.

# Key Concepts

## Definition

Read-across is defined as the use of data from one or more source chemicals to predict the properties of a target chemical. This method relies on the identification of structural or mechanistic similarities between the source and target chemicals. The process involves several steps, including the identification of suitable source chemicals, the assessment of similarity, and the justification of the read-across approach.

> **Claim**: Read-across is a method used to predict the toxicological properties of a target chemical based on the properties of similar source chemicals.
> **Citation**: [cit-001](#citation-001)

## Methodology

The read-across methodology involves the following key steps:

1. **Problem Formulation**: Define the purpose of the read-across, including the target chemical, the endpoint of interest, and the intended use of the data.

2. **Target Substance Characterization**: Identify existing data for the target substance and define the data gaps that need to be filled.

3. **Source Substance Identification**: Identify potential source substances that are structurally or mechanistically similar to the target substance.

4. **Similarity Assessment**: Evaluate the similarity between the target and source substances, considering structural, physicochemical, toxicokinetic (TK), and toxicodynamic (TD) properties.

5. **Data Gap Filling**: Use data from the source substances to fill the identified data gaps for the target substance.

6. **Uncertainty Assessment**: Assess the uncertainties associated with the read-across process and ensure that they are within acceptable limits for the intended use.

7. **Documentation and Reporting**: Document the entire read-across process, including the rationale for the selection of source substances, the assessment of similarity, and the justification of the read-across approach.

> **Claim**: The read-across methodology involves problem formulation, target substance characterization, source substance identification, similarity assessment, data gap filling, uncertainty assessment, and documentation.
> **Citation**: [cit-002](#citation-002)

## Applications

Read-across is widely used in regulatory toxicology and chemical safety assessment. Some key applications include:

- **Regulatory Risk Assessment**: Read-across is used to support regulatory decisions by providing data for chemicals where experimental data is limited.

- **Data Gap Filling**: It helps fill data gaps for chemicals that lack sufficient experimental data, enabling a more comprehensive safety assessment.

- **Chemical Categorization**: Read-across is used to group chemicals into categories based on their structural or mechanistic similarities, facilitating the assessment of their toxicological properties.

- **Integration with New Approach Methods (NAMs)**: Read-across is often combined with other NAMs, such as in silico models, in vitro assays, and physiologically based pharmacokinetic (PBPK) models, to enhance the reliability of predictions.

> **Claim**: Read-across is used in regulatory risk assessment, data gap filling, chemical categorization, and integration with other new approach methods.
> **Citation**: [cit-003](#citation-003)

## Uncertainty Assessment

Uncertainty assessment is a critical component of the read-across process. It involves identifying and characterizing the uncertainties associated with each step of the read-across, including the selection of source substances, the assessment of similarity, and the extrapolation of data. Uncertainties can arise from various sources, such as:

- **Structural Similarity**: Differences in the chemical structure between the target and source substances.

- **Data Quality**: The quality and reliability of the data used from the source substances.

- **Mechanistic Understanding**: The extent to which the mechanism of action is understood for the endpoint of interest.

- **Extrapolation**: The extrapolation of data from the source substances to the target substance.

> **Claim**: Uncertainty assessment in read-across involves identifying and characterizing uncertainties related to structural similarity, data quality, mechanistic understanding, and extrapolation.
> **Citation**: [cit-004](#citation-004)

## Computational Tools

Several computational tools and databases support the read-across process, including:

- **OECD QSAR Toolbox**: A software application that facilitates the identification of potential source substances and the assessment of similarity.

- **EPA's Generalized Read Across (GenRA)**: A tool that uses similarity-weighted activity to predict the properties of target chemicals.

- **Danish QSAR Database**: A database containing information on over 600,000 chemicals, which can be used to facilitate read-across groupings based on chemical similarity.

> **Claim**: Computational tools such as the OECD QSAR Toolbox, EPA's GenRA, and the Danish QSAR Database support the read-across process.
> **Citation**: [cit-005](#citation-005)

# Related Pages

- [Hazard](hazard.md)
- [Risk Assessment](risk-assessment.md)
- [QSAR Models](qsar-models.md)
- [ToxCast](toxcast.md)

# References

## Citation Format

### Citation 001

```yaml
citation_id: cit-001
source_type: review
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Introduction
notes: Defines read-across and its application in chemical safety assessment.
```

### Citation 002

```yaml
citation_id: cit-002
source_type: review
title: Internationalization of read-across as a validated new approach method (NAM) for regulatory toxicology
authors:
  - C. Rovida
  - G. Patlewicz
  - M. Crittenden
  - et al.
year: 2020
container: ALTEX
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Methodology
notes: Describes the methodology and steps involved in the read-across process.
```

### Citation 003

```yaml
citation_id: cit-003
source_type: review
title: Mechanistic read-across comes of age: a comparative appraisal of EFSA 2025 guidance, ECHA’s RAAF, and good read-across practice
authors:
  - G. Patlewicz
  - M. Crittenden
  - C. Rovida
  - et al.
year: 2025
container: Frontiers in Toxicology
doi: 10.3389/ftox.2025.1690491
url: https://doi.org/10.3389/ftox.2025.1690491
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Applications
notes: Discusses the applications of read-across in regulatory toxicology and chemical safety assessment.
```

### Citation 004

```yaml
citation_id: cit-004
source_type: review
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Uncertainty Assessment
notes: Describes the process of uncertainty assessment in read-across.
```

### Citation 005

```yaml
citation_id: cit-005
source_type: review
title: Internationalization of read-across as a validated new approach method (NAM) for regulatory toxicology
authors:
  - C. Rovida
  - G. Patlewicz
  - M. Crittenden
  - et al.
year: 2020
container: ALTEX
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Computational Tools
notes: Discusses computational tools and databases that support the read-across process.
```
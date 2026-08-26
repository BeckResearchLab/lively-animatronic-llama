---
id: comptox-chemicals-dashboard
title: CompTox Chemicals Dashboard
description: Dataset page for the CompTox Chemicals Dashboard, including scope, schema notes, and toxicology relevance.
slug: /datasets/comptox-chemicals-dashboard
sidebar_label: CompTox Chemicals Dashboard
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-25
---

# CompTox Chemicals Dashboard

## Overview

The CompTox Chemicals Dashboard is a publicly accessible web-based application developed by the U.S. Environmental Protection Agency (EPA). It provides comprehensive access to chemistry, toxicity, and exposure information for approximately 900,000 chemicals. This resource is widely used in computational toxicology for assembling data on physicochemical properties, environmental fate, exposure parameters, and health effects. The Dashboard integrates data from various sources, including the EPA's computational toxicology research databases and other public domain databases, making it a valuable tool for human health risk assessment and chemical evaluation. [^1][^2][^3]

## Scope and Notes

The CompTox Chemicals Dashboard serves as a central repository for chemical data, supporting a wide range of applications in toxicology, environmental science, and regulatory assessments. It is particularly useful for:

- **Data Assembly**: Gathering information on physicochemical properties, environmental fate, and exposure parameters.
- **Health Effects Identification**: Accessing data on cancer and non-cancer health effects from human and experimental animal studies.
- **Mechanistic Information**: Providing insights into adverse outcome pathways and other mechanistic data.
- **In Silico Predictions**: Offering tools for structure-activity relationship (SAR) and read-across analyses.

The Dashboard is increasingly recognized as a critical resource for assessors tasked with evaluating potential human health risks associated with chemical exposures. It facilitates systematic literature searching, review, and evidence-based decision-making. [^1][^2]

## Key Claims or Definitions

### Claim 1: Data Coverage

**Statement**: The CompTox Chemicals Dashboard provides access to chemistry, toxicity, and exposure information for approximately 900,000 chemicals.

**Subject**: CompTox Chemicals Dashboard
**Predicate**: provides_access_to
**Object**: chemistry, toxicity, and exposure information
**Qualifiers**: 
  - Number of chemicals: ~900,000
**Citations**: [^1][^2]
**Verification Status**: supported
**Confidence**: high

### Claim 2: Data Sources

**Statement**: The CompTox Chemicals Dashboard integrates data from the EPA's computational toxicology research databases and other public domain databases.

**Subject**: CompTox Chemicals Dashboard
**Predicate**: integrates_data_from
**Object**: EPA's computational toxicology research databases, public domain databases
**Citations**: [^1][^3]
**Verification Status**: supported
**Confidence**: high

### Claim 3: Functionalities

**Statement**: The CompTox Chemicals Dashboard supports searching, exporting, and downloading MS-Ready structures.

**Subject**: CompTox Chemicals Dashboard
**Predicate**: supports_functionalities
**Object**: searching, exporting, downloading MS-Ready structures
**Citations**: [^4]
**Verification Status**: supported
**Confidence**: high

## Evidence or Details

### Data Integration and Access

The CompTox Chemicals Dashboard is compiled from a variety of sources, including the EPA's computational toxicology research databases and other public domain databases. It serves as a centralized platform for accessing diverse chemical data, which is essential for conducting comprehensive risk assessments. The Dashboard's ability to integrate data from multiple sources ensures that users can access a wide range of information, including physicochemical properties, environmental fate, exposure parameters, and health effects. [^1][^3]

### Applications in Toxicology

The Dashboard is widely used for:

1. **Assembling Information**: Users can gather data on physicochemical properties, environmental fate, and exposure parameters for chemicals of interest.
2. **Identifying Health Effects**: The Dashboard provides access to data on cancer and non-cancer health effects, derived from human and experimental animal studies.
3. **Mechanistic Insights**: It offers mechanistic information that can aid in the analysis of traditional toxicology evidence bases or serve as the primary basis for informing hazard identification and dose-response when traditional bioassay data are lacking.
4. **In Silico Predictions**: The Dashboard includes tools for conducting structure-activity or read-across analyses, which are crucial for predicting the toxicity of chemicals without extensive experimental data. [^1][^2]

### Technical Features

The CompTox Chemicals Dashboard provides several technical features that enhance its usability and functionality:

- **Search Functionality**: Users can search for chemicals using various identifiers, such as CAS numbers, chemical names, or SMILES strings.
- **Batch Download**: The Dashboard supports batch downloads of chemical data, which is particularly useful for large-scale analyses.
- **API Access**: Programmatic access to the Dashboard's data is available through its API, enabling integration with other computational tools and workflows.
- **Data Visualization**: The Dashboard includes visualization tools for exploring chemical structures, toxicity data, and exposure information. [^4]

## Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [QSAR Prediction Workflow](11-workflows/qsar-prediction-workflow.md)
- [Read-Across](02-concepts/read-across.md)

## Open Questions or Review Notes

- The Dashboard's data quality and completeness for less-studied chemicals could be further evaluated.
- Potential biases in the data sources integrated into the Dashboard should be assessed.
- The usability of the Dashboard's API and batch download features for large-scale analyses could be improved.

## References

[^1]: Williams AJ, Lambert JC, Thayer K, Dorne JCM. Sourcing data on chemical properties and hazard data from the US-EPA CompTox Chemicals Dashboard: A practical guide for human risk assessment. *Environment International*. 2021;154:106566. doi: [10.1016/j.envint.2021.106566](https://doi.org/10.1016/j.envint.2021.106566)

[^2]: Sinclair G, Thillainadarajah I, Meyer B, Samano V, Sivasupramaniam S, Adams L, Willighagen EL, Richard AM, Walker M, Williams AJ. Wikipedia on the CompTox Chemicals Dashboard: Connecting Resources to Enrich Public Chemical Data. *Journal of Chemical Information and Modeling*. 2022;62(20):4888-4905. doi: [10.1021/acs.jcim.2c00886](https://doi.org/10.1021/acs.jcim.2c00886)

[^3]: Internationalization of read-across as a validated new approach method (NAM) for regulatory toxicology. *ALTEX*. 2020;37(2):187-200. doi: [10.14573/altex.1912181](https://doi.org/10.14573/altex.1912181)

[^4]: Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling. *Journal of Cheminformatics*. 2021;13(1):1-15. doi: [10.1186/s13321-021-00517-3](https://doi.org/10.1186/s13321-021-00517-3)
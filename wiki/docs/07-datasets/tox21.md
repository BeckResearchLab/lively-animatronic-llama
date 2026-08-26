---
id: tox21
title: Tox21
description: Dataset page for Tox21, including scope, schema notes, and toxicology relevance.
slug: /datasets/tox21
sidebar_label: Tox21
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-25
---

# Tox21

## Overview

The Toxicology in the 21st Century (Tox21) dataset is a collaborative effort between multiple federal agencies, including the National Institutes of Health (NIH), the Environmental Protection Agency (EPA), and the Food and Drug Administration (FDA). It aims to develop and validate high-throughput screening (HTS) assays to assess the toxicity of environmental chemicals and drugs. The Tox21 dataset provides a comprehensive resource for computational toxicology, enabling the prediction of chemical toxicity through in vitro assays and machine learning models.

## Scope and Notes

The Tox21 dataset includes bioactivity data from over 10,000 chemicals tested across hundreds of assays. These assays target various biological pathways and endpoints, such as nuclear receptors, stress response pathways, and developmental toxicity. The dataset is designed to support the development of predictive models for chemical toxicity, facilitating risk assessment and regulatory decision-making.

### Key Features

- **High-Throughput Screening (HTS)**: The dataset leverages HTS assays to evaluate chemical bioactivity efficiently.
- **Diverse Chemical Space**: It includes a wide range of chemicals, from environmental pollutants to pharmaceutical compounds.
- **Multiple Endpoints**: Assays cover various toxicological endpoints, including genotoxicity, endocrine disruption, and developmental toxicity.
- **Machine Learning Readiness**: The dataset is structured to support the training and validation of machine learning models for toxicity prediction.

## Key Claims or Definitions

### Claim 1: Tox21 Dataset Structure

**Claim ID**: clm-tox21-001
**Statement**: The Tox21 dataset includes bioactivity data from over 10,000 chemicals tested across hundreds of assays targeting various biological pathways.
**Subject**: Tox21 Dataset
**Predicate**: includes_data_from
**Object**: 10,000+ chemicals and 100+ assays
**Qualifiers**: 
  - Endpoints: nuclear receptors, stress response pathways, developmental toxicity
  - Data Type: High-throughput screening (HTS)
**Citations**: 
  - cit-001
  - cit-002
**Verification Status**: supported
**Confidence**: high

### Claim 2: Tox21 Data Access

**Claim ID**: clm-tox21-002
**Statement**: The Tox21 dataset is publicly accessible and includes standardized annotations to improve data reusability and interoperability.
**Subject**: Tox21 Dataset
**Predicate**: is_accessible_as
**Object**: Public dataset with standardized annotations
**Qualifiers**: 
  - Access: Public
  - Annotations: Standardized for FAIR (Findable, Accessible, Interoperable, Reusable) compliance
**Citations**: 
  - cit-001
**Verification Status**: supported
**Confidence**: high

### Claim 3: Tox21 Assay Validation

**Claim ID**: clm-tox21-003
**Statement**: Tox21 assays undergo rigorous validation to ensure reliability and reproducibility, including the removal of false positives caused by cytotoxicity.
**Subject**: Tox21 Assays
**Predicate**: undergo_validation_process
**Object**: Rigorous validation for reliability and reproducibility
**Qualifiers**: 
  - Validation: Removal of false positives due to cytotoxicity
  - Method: Standard Z-score classification
**Citations**: 
  - cit-002
**Verification Status**: supported
**Confidence**: high

## Evidence or Details

### Data Structure

The Tox21 dataset is organized into multiple tiers, including:

1. **Primary Data**: Raw assay results for individual chemicals.
2. **Aggregated Data**: Processed and curated datasets with standardized annotations.
3. **Signatures**: Benchmarked chemical reference signatures for activity, cytotoxicity, and selective reporter gene activity.

The dataset is annotated using controlled vocabularies to ensure compliance with FAIR principles, enhancing its utility for computational toxicology research.

### Assay Types

Tox21 assays are categorized based on their target pathways and endpoints:

- **Nuclear Receptors**: Assays targeting estrogen, androgen, and thyroid receptors.
- **Stress Response Pathways**: Assays for oxidative stress, DNA damage, and apoptosis.
- **Developmental Toxicity**: Assays evaluating effects on embryonic development.

### Data Access Methods

The Tox21 dataset is publicly available through various platforms, including:

- **Tox21 Data Portal**: Official repository for dataset downloads and documentation.
- **Programmatic Access**: APIs and bulk download options for large-scale data retrieval.
- **Standardized Packages**: Pre-processed dataset packages for ease of use in machine learning workflows.

## Related Pages

- **[ToxCast](toxcast.md)**: Related dataset for high-throughput toxicity screening.
- **[Quantitative Structure-Activity Relationship (QSAR)](qsar.md)**: Methodology for toxicity prediction using chemical structure.
- **[High-Throughput Screening](high-throughput-screening.md)**: Overview of HTS assays and their role in toxicology.

## Open Questions or Review Notes

- **Data Curation**: Continuous efforts are needed to improve data curation and annotation standards.
- **Assay Expansion**: Potential for expanding the dataset to include additional assays and endpoints.
- **Model Validation**: Ongoing validation of machine learning models trained on Tox21 data.

## References

```yaml
citation_id: cit-001
source_type: paper
title: Improving the Utility of the Tox21 Dataset by Deep Metadata Annotations and Constructing Reusable Benchmarked Chemical Reference Signatures
authors:
  - Daniel J Cooper
  - Stephan Schürer
year: 2019
container: Molecules
doi: 10.3390/molecules24081604
url: https://doi.org/10.3390/molecules24081604
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes the annotation and curation of the Tox21 dataset for improved reusability.

citation_id: cit-002
source_type: paper
title: Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data
authors:
  - Magnus Gray
  - Leihong Wu
year: 2025
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.5c00289
url: https://doi.org/10.1021/acs.chemrestox.5c00289
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the validation and use of Tox21 data in machine learning models for toxicity prediction.
```
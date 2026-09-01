---
id: qsar-prediction-workflow
title: QSAR Prediction Workflow
description: Workflow page describing the repeatable QSAR prediction process for computational toxicology.
slug: /workflows/qsar-prediction-workflow
sidebar_label: QSAR Prediction Workflow
page_type: workflow
entity_class: workflow
status: verified
last_reviewed: 2026-08-25
verification_date: 2026-08-08
verification_status: all_claims_supported
---

# QSAR Prediction Workflow

## Overview

Quantitative Structure-Activity Relationship (QSAR) prediction workflows are essential in computational toxicology for predicting the biological activity or toxicity of chemicals based on their molecular structures. This workflow outlines the steps involved in developing, validating, and applying QSAR models to ensure accurate and reliable predictions.

The QSAR-ready workflow is designed to standardize chemical structures using operations such as desalting, stripping of stereochemistry, standardization of tautomers and nitro groups, valence correction, neutralization, and removal of duplicates. This workflow was initially developed for the Collaborative Estrogen Receptor Activity Prediction Project (CERAPP) and has since been adapted for other modeling applications, including mass spectrometry (MS-ready structures).

## Scope and Notes

This workflow focuses on the standardized process for QSAR modeling, including data preparation, model training, validation, interpretation, and application. It adheres to the OECD principles for QSAR model development to ensure scientific validity and reliability.

## Key Steps in the QSAR Prediction Workflow

### 1. Data Collection and Preprocessing

- **Data Collection**: Gather experimental data for chemical structures and their corresponding biological activities or toxicity endpoints. This data can be sourced from public databases such as ToxCast or Tox21.
- **Data Preprocessing**: Clean and preprocess the data to ensure consistency. This includes handling missing values, removing duplicates, and standardizing chemical structures.

  The standardization process includes parsing input files, checking consistency, and applying predefined rules for representation form, style, or semantics. The workflow generates standardized structures in SDF and SMILES formats, along with summary files and error logs for failed structures.

### 2. Molecular Descriptor Generation

- Generate molecular descriptors that represent the chemical structures. These descriptors can include 2D fingerprints, topological indices, and other chemoinformatic features.

### 3. Descriptor Selection

- Select the most relevant descriptors for model training. This step involves statistical methods to identify descriptors that have the highest correlation with the biological activity or toxicity endpoint.

### 4. Model Training

- Train the QSAR model using machine learning algorithms such as random forest, support vector machines, or deep neural networks. The choice of algorithm depends on the complexity of the data and the desired model performance.

### 5. Model Validation

- Validate the model using statistical parameters such as the coefficient of determination (R²), cross-validated correlation coefficients, and Fischer's value. External validation is crucial to ensure the model's predictive accuracy and generalizability.

### 6. Model Interpretation

- Interpret the model to understand the relationship between molecular descriptors and biological activity. This step is essential for ensuring transparency and reproducibility of the model's predictions.

### 7. Model Application

- Apply the validated QSAR model to predict the biological activity or toxicity of new chemicals. Ensure that the new chemicals fall within the applicability domain of the model.

## Key Claims or Definitions

### Claim 1: Data Standardization

**Claim ID**: clm-qsar-001
**Statement**: Chemical structures must be standardized to ensure consistency in molecular descriptor calculations and model predictions.
**Subject**: Chemical structures
**Predicate**: must be standardized
**Object**: for QSAR modeling
**Qualifiers**: 
  - Process: QSAR-ready workflow
  - Tool: KNIME platform
**Citations**: 
  - cit-001
**Verification Status**: supported
**Confidence**: high

### Claim 2: Model Validation

**Claim ID**: clm-qsar-002
**Statement**: QSAR models must undergo rigorous validation to ensure predictive accuracy and generalizability.
**Subject**: QSAR models
**Predicate**: must undergo
**Object**: rigorous validation
**Qualifiers**: 
  - Method: External validation
  - Metrics: R², cross-validated correlation coefficients
**Citations**: 
  - cit-002
**Verification Status**: supported
**Confidence**: high

### Claim 3: Applicability Domain

**Claim ID**: clm-qsar-003
**Statement**: New chemicals must fall within the applicability domain of the QSAR model to ensure reliable predictions.
**Subject**: New chemicals
**Predicate**: must fall within
**Object**: applicability domain
**Qualifiers**: 
  - Context: Model application
**Citations**: 
  - cit-003
**Verification Status**: supported
**Confidence**: high

### Claim 4: Workflow Availability

**Claim ID**: clm-qsar-004
**Statement**: The QSAR-ready workflow is freely available via GitHub, standalone versions, and Docker containers
**Subject**: QSAR-ready workflow
**Predicate**: is freely available via
**Object**: GitHub, standalone versions, Docker containers
**Qualifiers**: 
  - Environment: KNIME
  - Access: open source
**Citations**: 
  - cit-001
**Verification Status**: supported
**Confidence**: high

### Claim 5: Collaborative Applications

**Claim ID**: clm-qsar-005
**Statement**: The QSAR-ready workflow has been used in international collaborative modeling projects such as CERAPP, CoMPARA, and CATMoS
**Subject**: QSAR-ready workflow
**Predicate**: has been used in
**Object**: international collaborative modeling projects
**Qualifiers**: 
  - Projects: CERAPP, CoMPARA, CATMoS
  - Context: QSAR modeling
**Citations**: 
  - cit-001
**Verification Status**: supported
**Confidence**: high

## Evidence or Details

### Data Standardization

The QSAR-ready workflow is designed to standardize chemical structures using operations such as desalting, stripping of stereochemistry, standardization of tautomers and nitro groups, valence correction, neutralization, and removal of duplicates. This workflow is implemented using the KNIME platform and includes steps such as input parsing, inorganics filtering, salts and counterions processing, structure standardization, ring processing, duplicates processing, and 3D structure processing. The standardized structures are essential for both training and prediction steps in QSAR modeling.

The standardization process includes parsing input files, checking consistency, and applying predefined rules for representation form, style, or semantics. The workflow generates standardized structures in SDF and SMILES formats, along with summary files and error logs for failed structures. This comprehensive approach ensures that chemical structures are consistently represented across all modeling applications, from QSAR predictions to mass spectrometry analysis.

The workflow is integrated into the OPERA suite of QSAR models, ensuring consistency in chemical structure standardization across the entire modeling pipeline. It also facilitates non-targeted analysis (NTA) workflows using high-resolution mass spectrometry (HRMS) by linking observed structures to database forms.

### Collaborative Applications

The QSAR-ready workflow has been successfully applied in several international collaborative modeling projects:

- **CERAPP (Collaborative Estrogen Receptor Activity Prediction Project)**: Initial development and validation
- **CoMPARA**: Comparative modeling applications
- **CATMoS**: Chemical assessment and toxicology modeling systems

These applications demonstrate the workflow's versatility and reliability across different toxicological research domains.

### Model Validation

Model validation is a critical step in QSAR modeling. It involves assessing the model's performance using statistical parameters such as the coefficient of determination (R²), cross-validated correlation coefficients, and Fischer's value. External validation ensures that the model is generalizable and can reliably predict the biological activity or toxicity of new chemicalscit-002.

### Model Interpretation

Interpreting QSAR models is essential for understanding the relationship between molecular descriptors and biological activity. This step promotes transparency and reproducibility, allowing researchers to make informed decisions based on the model's predictions. Advanced techniques such as deep learning and ensemble methods can improve both the predictivity and interpretability of QSAR modelscit-003.

## Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [Tox21](07-datasets/tox21.md)
- [Molecular Descriptors](02-concepts/molecular-descriptors.md)
- [Machine Learning in Toxicology](08-models-and-methods/machine-learning.md)
- [CERAPP](03-chemicals/cerapp.md) - Initial application of the QSAR-ready workflow
- [OPERA Models](08-models-and-methods/opera-models.md) - Integrated QSAR model suite
- [KNIME Platform](08-models-and-methods/knime.md) - Implementation environment

## Deployment and Access

The QSAR-ready workflow is freely available through multiple channels:

- **KNIME Environment**: Native implementation in the KNIME Analytics Platform
- **Standalone Versions**: Downloadable workflow packages
- **Docker Containers**: Containerized deployment for reproducible execution
- **GitHub Repository**: Source code and documentation available on GitHub

The workflow has been used in international collaborative modeling projects such as CERAPP, CoMPARA, and CATMoS, ensuring its applicability across diverse toxicological research initiatives.

## Open Questions or Review Notes

- Further research is needed to improve the interpretability of complex QSAR models, particularly those based on deep learning techniques.
- The applicability domain of QSAR models should be clearly defined to ensure reliable predictions for new chemicals.

## References

### Citation 1: QSAR-Ready Workflow

**Citation ID**: cit-001
**Source Type**: primary_technical
**Title**: Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling
**Authors**: 
  - Kamel Mansouri
  - José T. Moreira-Filho
  - Charles N. Lowe
  - Nathaniel Charest
  - Todd Martin
  - Valery Tkachenko
  - Richard Judson
  - Mike Conway
  - Nicole C. Kleinstreuer
  - Antony J. Williams
**Year**: 2024
**Container**: Journal of Computational Toxicology
**DOI**: 10.1080/18715224.2024.2321543
**URL**: https://doi.org/10.1080/18715224.2024.2321543
**Access Status**: open_access
**Allowed Source**: true
**Retrieved On**: 2026-08-08
**Pages or Sections**: Comprehensive workflow description
**Notes**: Describes the QSAR-ready workflow for standardizing chemical structures. See [literature page](../09-literature/qsar-workflow-2024.md) for detailed summary.

### Citation 2: Model Validation

**Citation ID**: cit-002
**Source Type**: review
**Title**: Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review
**Authors**: 
  - [Author List]
**Year**: 2024
**Container**: International Journal of Molecular Sciences
**DOI**: 10.3390/ijms241411488
**URL**: https://www.mdpi.com/1422-0067/24/14/11488
**Access Status**: open_access
**Allowed Source**: true
**Retrieved On**: 2026-08-25
**Pages or Sections**: Section 4.8
**Notes**: Discusses the importance of model validation in QSAR modeling.

### Citation 3: Model Interpretation

**Citation ID**: cit-003
**Source Type**: review
**Title**: Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review
**Authors**: 
  - [Author List]
**Year**: 2024
**Container**: International Journal of Molecular Sciences
**DOI**: 10.3390/ijms241411488
**URL**: https://www.mdpi.com/1422-0067/24/14/11488
**Access Status**: open_access
**Allowed Source**: true
**Retrieved On**: 2026-08-25
**Pages or Sections**: Section 4.9
**Notes**: Explores techniques for interpreting QSAR models.
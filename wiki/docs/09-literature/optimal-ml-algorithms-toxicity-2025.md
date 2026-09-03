---
id: optimal-ml-algorithms-toxicity-2025
title: "Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data"
description: Literature page for the study on optimal ML algorithms and molecular fingerprints for toxicity prediction
year: 2025
slug: /literature/optimal-ml-algorithms-toxicity-2025
sidebar_label: Optimal ML Algorithms for Toxicity (2025)
page_type: literature
entity_class: source
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
---

## Overview

This primary technical paper titled "Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data" focuses on identifying the most effective machine learning algorithms and molecular fingerprints for developing explainable toxicity prediction models using ToxCast/Tox21 bioassay data.

## Citation Metadata

- **Title**: Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data
- **Authors**: Magnus Gray, Leihong Wu
- **Year**: 2025
- **Journal**: Chemical Research in Toxicology
- **DOI**: 10.1021/acs.chemrestox.5c00289
- **URL**: https://doi.org/10.1021/acs.chemrestox.5c00289
- **Access Status**: Accessible
- **Retrieved On**: 2026-08-08
- **Source Type**: Primary technical paper

## Scope and Source Notes

This study focuses on:
- Identifying optimal machine learning algorithms for toxicity prediction
- Evaluating molecular fingerprints for chemical representation
- Developing explainable toxicity prediction models
- Using ToxCast/Tox21 bioassay data for model training and validation
- Balancing predictivity and interpretability in ML models

## Extracted Key Claims

### Central Claims (Consensus)

1. **Model Performance**: The MACCS and Morgan fingerprints paired with Random Forest (RF) demonstrated robust performance for toxicity prediction.

2. **Data Preprocessing**: ToxCast/Tox21 data were curated to remove inorganic compounds, salts, and chemicals without SMILES codes. Only positive data with a Z-score of three or higher were used to avoid false positives caused by cytotoxicity.

3. **Assay Selection**: 1092 assays with biological targets were selected from 1473 assays. The data set exhibited high structural diversity among chemicals, with a mean Tanimoto coefficient of 0.085 ± 0.058.

4. **Machine Learning Algorithms**: Decision tree-based models (e.g., RF, GBT) were the most prevalent among the 35 selected models. RF models are advantageous for interpreting active chemicals and identifying descriptors used for predictions.

5. **Molecular Fingerprints**: MACCS and Morgan fingerprints were the most represented, followed by RDKit, pattern, and layered fingerprints. MACCS fingerprints are pattern-based and can capture specific structural features or patterns in chemical compounds.

6. **Explainability and Predictivity**: The study highlights the importance of balancing predictivity and interpretability in toxicity prediction models. Simple models like RF-MACCS combinations are recommended for developing explainable toxicity prediction models.

### Supporting Claims (Consensus)

7. **Target Selection**: Four models targeting G protein-coupled receptors (GPCRs) and kinases were selected for their explainability and performance.

8. **Limitations**: The study only considered chemical feature-based models, and future work should explore biological descriptors.

9. **Future Directions**: Quantitative or qualitative metrics for interpretability should be developed to enhance model explainability.

## Target Pages

The extracted claims have been mapped to the following canonical pages:

- [Machine Learning Algorithms in Toxicology](08-models-and-methods/ml-in-toxicology.md) - Random Forest performance
- [Molecular Fingerprints](08-models-and-methods/molecular-fingerprints.md) - MACCS and Morgan fingerprints
- [ToxCast/Tox21 Data](07-datasets/tox21.md) and [ToxCast](07-datasets/toxcast.md) - Assay selection and data preprocessing
- [Explainable AI in Toxicology](08-models-and-methods/explainable-ai.md) - Balancing predictivity and interpretability
- [GPCRs and Kinases in Toxicology](04-biology/gpcrs-kinases.md) - Biological targets

## Open Questions or Review Notes

1. How do the selected models perform in predicting in vivo toxic effects compared to in vitro assays?
2. What are the potential trade-offs between using chemical feature-based models and biological descriptor-based models?
3. How can interpretability metrics be quantitatively or qualitatively measured to enhance model explainability?

## Review Needs

1. Verify the performance metrics (e.g., F1 score, accuracy) of the selected models against other studies.
2. Assess the generalizability of the MACCS-RF combination to other data sets or toxicity endpoints.
3. Evaluate the structural diversity of the ToxCast/Tox21 data set and its impact on model performance.

## References

- DOI: 10.1021/acs.chemrestox.5c00289
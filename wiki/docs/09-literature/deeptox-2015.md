---
id: deeptox-2015
title: "DeepTox: Toxicity Prediction Using Deep Learning (2015)"
description: Literature page for the original DeepTox paper describing a deep learning-based pipeline for toxicity prediction.
slug: /literature/deeptox-2015
sidebar_label: DeepTox (2015)
page_type: literature
entity_class: literature
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
---

# DeepTox: Toxicity Prediction Using Deep Learning (2015)

## Overview

This literature page documents the original DeepTox paper by Mayr et al. (2015), which describes a deep learning-based pipeline for toxicity prediction that won the Tox21 Data Challenge.

## Source Metadata

- **Title**: DeepTox: Toxicity Prediction Using Deep Learning
- **Authors**: Andreas Mayr, Günter Klambauer, Thomas Unterthiner, Sepp Hochreiter
- **Year**: 2015
- **Journal**: Frontiers in Environmental Science
- **DOI**: 10.3389/fenvs.2015.00080
- **URL**: https://doi.org/10.3389/fenvs.2015.00080
- **Access Status**: Open access
- **Source Type**: Primary/Technical Paper
- **Ingestion Strategy**: C (Mechanism or Case Extraction)

## Scope and Notes

This paper presents DeepTox, a deep learning pipeline that achieved state-of-the-art performance in the Tox21 Data Challenge. The paper describes the model architecture, training process, performance evaluation, and biological interpretation of the learned features.

### Key Contributions

1. **Deep Learning Architecture**: Introduction of deep neural networks for toxicity prediction
2. **Multi-task Learning**: Simultaneous prediction of multiple toxic effects
3. **Ensemble Methods**: Combination of DNNs with traditional machine learning algorithms
4. **Performance**: Winning results in the Tox21 Data Challenge
5. **Interpretability**: Analysis of toxicophore representations learned by the model

## Extracted Claims and Target Pages

### Extracted Claims

1. **DeepTox Pipeline**: DeepTox is a deep learning-based pipeline for toxicity prediction that won the Tox21 Data Challenge.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

2. **Multi-task Learning**: DeepTox uses multi-task learning to predict multiple toxic effects simultaneously, improving performance over single-task learning.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

3. **Hierarchical Features**: DeepTox constructs hierarchical chemical features using deep neural networks (DNNs), which outperform traditional methods like SVMs and random forests.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

4. **Dataset Description**: The Tox21 challenge dataset includes 12,707 chemical compounds and 12 toxic effects, with high-throughput screening assay measurements.
   - **Target Page**: `datasets/tox21.md`
   - **Claim Type**: Novel

5. **Data Processing**: DeepTox employs data cleaning, feature engineering (static and dynamic descriptors), and model evaluation using cluster cross-validation.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

6. **GPU Acceleration**: DeepTox uses GPU acceleration for training DNNs, achieving significant speedups over CPU implementations.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

7. **Ensemble Learning**: DeepTox constructs ensembles of models, including DNNs, SVMs, random forests, and elastic nets, to improve predictive performance.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

8. **Toxicophore Learning**: DeepTox learns toxicophore representations in hidden layers of DNNs, which correlate with known toxicophores and improve toxicity prediction.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

9. **Challenge Performance**: DeepTox achieved the highest performance in the Tox21 challenge, winning the grand challenge, nuclear receptor panel, stress response panel, and six single assays.
   - **Target Page**: `models/deeptox.md`
   - **Claim Type**: Novel

10. **Probabilistic Calibration**: DeepTox uses Platt scaling to calibrate model predictions into probabilistic outputs for ensemble learning.
    - **Target Page**: `models/deeptox.md`
    - **Claim Type**: Novel

## Related Pages

- **[DeepTox Model](../../08-models-and-methods/deeptox.md)**: Canonical page for the DeepTox model
- **[Tox21 Dataset](../../07-datasets/tox21.md)**: Dataset used in the Tox21 Data Challenge
- **[Machine Learning in Toxicology](../../08-models-and-methods/ml-in-toxicology.md)**: Overview of ML applications in toxicology

## Open Questions or Review Notes

- **Methodological Details**: Verify the specific architecture details of the deep neural networks used
- **Performance Metrics**: Confirm the exact performance metrics achieved in the Tox21 challenge
- **Reproducibility**: Assess whether the DeepTox implementation is available for independent validation
- **Extensions**: Investigate whether DeepTox has been extended or updated since the original publication

## References

```yaml
citation_id: lit-deeptox-001
source_type: paper
title: DeepTox: Toxicity Prediction Using Deep Learning
authors:
  - Andreas Mayr
  - Günter Klambauer
  - Thomas Unterthiner
  - Sepp Hochreiter
year: 2015
container: Frontiers in Environmental Science
doi: 10.3389/fenvs.2015.00080
url: https://doi.org/10.3389/fenvs.2015.00080
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Original source document for DeepTox model description and Tox21 challenge results.
```
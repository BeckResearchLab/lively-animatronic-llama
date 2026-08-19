---
id: qsar
title: QSAR
description: Concept page explaining the principles and applications of QSAR in computational toxicology.
slug: /concepts/qsar
sidebar_label: QSAR
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Quantitative Structure-Activity Relationship (QSAR) is a computational method used to predict the biological activity or toxicity of chemicals based on their molecular structure. QSAR models are widely used in computational toxicology to assess the potential hazards of chemicals.

## Scope and Notes

This page defines the principles and applications of QSAR. It does not cover the development or implementation of QSAR models, which are addressed in separate pages.

## Key Claims or Definitions

### Definition of QSAR

QSAR is a method that:

1. Uses mathematical models to relate the chemical structure of compounds to their biological activity or toxicity.
2. Relies on descriptors that quantify molecular properties (e.g., lipophilicity, molecular weight).
3. Predicts the activity or toxicity of new compounds based on their structural similarity to known compounds.

### Key Components of QSAR

1. **Molecular Descriptors**: Numerical representations of molecular properties.
2. **Training Data**: Experimental data used to build the QSAR model.
3. **Model**: The mathematical relationship between descriptors and biological activity.
4. **Validation**: Assessment of the model's performance and reliability.
5. **Prediction**: Use of the model to predict the activity or toxicity of new compounds.

## Evidence or Details

### Principles of QSAR

1. **Similarity Principle**: Compounds with similar structures are likely to have similar biological activities.
2. **Descriptor Selection**: Choosing relevant molecular descriptors that capture the key properties influencing activity.
3. **Model Building**: Developing a mathematical model that relates descriptors to activity.
4. **Model Validation**: Assessing the model's performance using appropriate metrics (e.g., R-squared, RMSE).
5. **Prediction**: Applying the model to predict the activity or toxicity of new compounds.

### Applications of QSAR

- **Toxicity Prediction**: Predicting the toxicity of chemicals based on their structure.
- **Drug Discovery**: Identifying potential drug candidates with desired properties.
- **Regulatory Assessment**: Supporting regulatory decisions by predicting chemical hazards.
- **Risk Assessment**: Evaluating the potential risks of chemicals to human health and the environment.

## Related Pages

- [Computational Models](../08-models-and-methods/computational-models.md)
- [Molecular Descriptors](../02-concepts/molecular-descriptors.md)
- [Model Validation](model-validation.md)

## Open Questions or Review Notes

- How should QSAR models be validated when experimental data is limited?
- What role should human experts play in the interpretation of QSAR predictions?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

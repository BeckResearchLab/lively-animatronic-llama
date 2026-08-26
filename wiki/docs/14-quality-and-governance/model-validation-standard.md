---
id: model-validation-standard
title: Model Validation Standard
description: Define the standard for validating models used in the wiki.
slug: /quality/model-validation-standard
sidebar_label: Model Validation Standard
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Model Validation Standard

This standard defines the criteria and procedures for validating models used in the wiki. It ensures that models are reliable, accurate, and appropriate for their intended use.

## Purpose

The purpose of this standard is to establish a structured approach for validating models. It helps ensure that the wiki's content is based on models that are robust and trustworthy.

## Scope

This standard applies to all models used in the wiki, including predictive models, simulation models, and analytical models. It covers the validation of model inputs, processes, and outputs.

## Validation Criteria

### Model Inputs

1. **Data Quality**: Are the inputs to the model of high quality and appropriate for the model's purpose?
   - **High Quality**: Inputs are accurate, complete, and relevant.
   - **Moderate Quality**: Inputs are generally accurate but may have some limitations.
   - **Low Quality**: Inputs are inaccurate, incomplete, or irrelevant.

2. **Data Sources**: Are the data sources reliable and well-documented?
   - **Reliable**: Data sources are reputable and well-documented.
   - **Moderately Reliable**: Data sources are generally reliable but may lack some documentation.
   - **Unreliable**: Data sources are not reputable or lack documentation.

### Model Processes

1. **Algorithmic Soundness**: Is the model's algorithm sound and well-justified?
   - **Sound**: The algorithm is mathematically sound and well-justified.
   - **Moderately Sound**: The algorithm is generally sound but may have some limitations.
   - **Unsound**: The algorithm is not mathematically sound or justified.

2. **Assumptions**: Are the model's assumptions reasonable and well-documented?
   - **Reasonable**: Assumptions are reasonable and well-documented.
   - **Moderately Reasonable**: Assumptions are generally reasonable but may lack some documentation.
   - **Unreasonable**: Assumptions are not reasonable or lack documentation.

### Model Outputs

1. **Accuracy**: Are the model's outputs accurate and consistent with expected results?
   - **Accurate**: Outputs are accurate and consistent with expected results.
   - **Moderately Accurate**: Outputs are generally accurate but may have some inconsistencies.
   - **Inaccurate**: Outputs are inaccurate or inconsistent with expected results.

2. **Uncertainty**: Is the model's uncertainty well-quantified and communicated?
   - **Well-Quantified**: Uncertainty is well-quantified and communicated.
   - **Moderately Quantified**: Uncertainty is generally quantified but may lack some communication.
   - **Poorly Quantified**: Uncertainty is not well-quantified or communicated.

## Validation Procedures

1. **Internal Validation**: Validate the model using internal data or simulations.

2. **External Validation**: Validate the model using external data or independent sources.

3. **Sensitivity Analysis**: Assess the model's sensitivity to changes in inputs or assumptions.

4. **Peer Review**: Submit the model for peer review to ensure its validity and reliability.

## Documentation

- Document all validation procedures, including the criteria, methods, and results.
- Maintain a log of all validations, including the date, validator, and outcome.

## Examples

### Model Validation Example

```yaml
validation_id: val-model-001
model_id: model-example-001
validated_on: 2026-08-19
validated_by: "reviewer@example.com"
inputs:
  data_quality: high
  data_sources: reliable
processes:
  algorithmic_soundness: sound
  assumptions: reasonable
outputs:
  accuracy: accurate
  uncertainty: well_quantified
validation_methods:
  - internal_validation
  - external_validation
  - sensitivity_analysis
  - peer_review
outcome: "Model is validated and reliable for its intended use."
```

## Related Pages

- [Dataset Quality Standard](#)
- [Evidence Standards](#)
- [Quality and Governance](#)

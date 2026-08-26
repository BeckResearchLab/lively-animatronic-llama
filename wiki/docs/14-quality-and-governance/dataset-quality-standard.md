---
id: dataset-quality-standard
title: Dataset Quality Standard
description: Define the standard for assessing the quality of datasets used in the wiki.
slug: /quality/dataset-quality-standard
sidebar_label: Dataset Quality Standard
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Dataset Quality Standard

This standard defines the criteria and procedures for assessing the quality of datasets used in the wiki. It ensures that datasets are reliable, accurate, and appropriate for their intended use.

## Purpose

The purpose of this standard is to establish a structured approach for assessing dataset quality. It helps ensure that the wiki's content is based on datasets that are robust and trustworthy.

## Scope

This standard applies to all datasets used in the wiki, including experimental data, observational data, and derived data. It covers the assessment of data accuracy, completeness, consistency, and relevance.

## Quality Criteria

### Accuracy

1. **Data Correctness**: Are the data values correct and free from errors?
   - **High Accuracy**: Data values are correct and free from errors.
   - **Moderate Accuracy**: Data values are generally correct but may have minor errors.
   - **Low Accuracy**: Data values contain significant errors.

2. **Measurement Quality**: Are the measurements or observations of high quality?
   - **High Quality**: Measurements or observations are precise and reliable.
   - **Moderate Quality**: Measurements or observations are generally precise but may have some limitations.
   - **Low Quality**: Measurements or observations are imprecise or unreliable.

### Completeness

1. **Data Coverage**: Does the dataset cover all required variables and observations?
   - **Complete**: Dataset covers all required variables and observations.
   - **Partially Complete**: Dataset covers most required variables and observations but may lack some.
   - **Incomplete**: Dataset lacks significant variables or observations.

2. **Missing Data**: Is the amount of missing data minimal and handled appropriately?
   - **Minimal Missing Data**: Missing data is minimal and handled appropriately.
   - **Moderate Missing Data**: Missing data is moderate and handled with some limitations.
   - **Significant Missing Data**: Missing data is significant and not handled appropriately.

### Consistency

1. **Internal Consistency**: Are the data internally consistent and free from contradictions?
   - **Consistent**: Data is internally consistent and free from contradictions.
   - **Moderately Consistent**: Data is generally consistent but may have minor contradictions.
   - **Inconsistent**: Data contains significant contradictions.

2. **External Consistency**: Are the data consistent with external sources or expectations?
   - **Consistent**: Data is consistent with external sources or expectations.
   - **Moderately Consistent**: Data is generally consistent but may have minor discrepancies.
   - **Inconsistent**: Data is inconsistent with external sources or expectations.

### Relevance

1. **Purpose Alignment**: Are the data relevant to the intended purpose or analysis?
   - **Highly Relevant**: Data is highly relevant to the intended purpose or analysis.
   - **Moderately Relevant**: Data is generally relevant but may have some limitations.
   - **Irrelevant**: Data is not relevant to the intended purpose or analysis.

2. **Timeliness**: Is the data up-to-date and appropriate for the intended use?
   - **Up-to-Date**: Data is up-to-date and appropriate for the intended use.
   - **Moderately Up-to-Date**: Data is generally up-to-date but may be slightly outdated.
   - **Outdated**: Data is outdated and not appropriate for the intended use.

## Assessment Procedures

1. **Data Profiling**: Profile the dataset to assess its quality characteristics.

2. **Validation Checks**: Perform validation checks to ensure data accuracy and consistency.

3. **Comparison with External Sources**: Compare the dataset with external sources to assess consistency.

4. **Documentation Review**: Review the dataset's documentation to ensure completeness and clarity.

## Documentation

- Document all quality assessments, including the criteria, methods, and results.
- Maintain a log of all assessments, including the date, assessor, and outcome.

## Examples

### Dataset Quality Assessment Example

```yaml
assessment_id: ass-dataset-001
dataset_id: dataset-example-001
assessed_on: 2026-08-19
assessed_by: "reviewer@example.com"
accuracy:
  data_correctness: high
  measurement_quality: high
completeness:
  data_coverage: complete
  missing_data: minimal
consistency:
  internal_consistency: consistent
  external_consistency: consistent
relevance:
  purpose_alignment: highly_relevant
  timeliness: up_to_date
assessment_methods:
  - data_profiling
  - validation_checks
  - external_comparison
  - documentation_review
outcome: "Dataset is of high quality and suitable for its intended use."
```

## Related Pages

- [Model Validation Standard](#)
- [Evidence Standards](#)
- [Quality and Governance](#)

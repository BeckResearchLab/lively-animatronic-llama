---
id: risk-of-bias-rubric
title: Risk of Bias Rubric
description: Provide a rubric for assessing the risk of bias in studies cited in the wiki.
slug: /quality/risk-of-bias-rubric
sidebar_label: Risk of Bias Rubric
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Risk of Bias Rubric

This rubric provides guidelines for assessing the risk of bias in studies cited in the wiki. It ensures that the wiki's content is based on studies with minimal bias.

## Purpose

The purpose of this rubric is to establish a standardized approach for evaluating the risk of bias in studies. It helps ensure that the wiki's content is based on unbiased and reliable evidence.

## Scope

This rubric applies to all studies cited in the wiki, including primary research, reviews, and meta-analyses. It covers the assessment of potential sources of bias in study design, methodology, and reporting.

## Assessment Criteria

### Selection Bias

1. **Participant Selection**: Were participants selected in a way that minimizes selection bias?
   - **Low Risk**: Participants were selected randomly or through a well-justified method.
   - **Moderate Risk**: Participants were selected through a method that may introduce some bias.
   - **High Risk**: Participants were selected in a way that introduces significant bias.

2. **Exclusion Criteria**: Were exclusion criteria applied consistently and transparently?
   - **Low Risk**: Exclusion criteria were applied consistently and transparently.
   - **Moderate Risk**: Exclusion criteria were applied but may lack consistency or transparency.
   - **High Risk**: Exclusion criteria were not applied consistently or transparently.

### Performance Bias

1. **Blinding**: Were participants and researchers blinded to the study conditions where applicable?
   - **Low Risk**: Participants and researchers were blinded to the study conditions.
   - **Moderate Risk**: Blinding was attempted but may have been incomplete.
   - **High Risk**: Blinding was not applied.

2. **Intervention Administration**: Were interventions administered consistently across groups?
   - **Low Risk**: Interventions were administered consistently across groups.
   - **Moderate Risk**: Interventions were generally consistent but may have some variability.
   - **High Risk**: Interventions were not administered consistently.

### Detection Bias

1. **Outcome Assessment**: Were outcomes assessed in a way that minimizes detection bias?
   - **Low Risk**: Outcomes were assessed using objective measures or blinded assessors.
   - **Moderate Risk**: Outcomes were assessed using measures that may introduce some bias.
   - **High Risk**: Outcomes were assessed in a way that introduces significant bias.

2. **Data Collection**: Were data collected consistently across groups?
   - **Low Risk**: Data were collected consistently across groups.
   - **Moderate Risk**: Data collection was generally consistent but may have some variability.
   - **High Risk**: Data were not collected consistently.

### Attrition Bias

1. **Dropout Rate**: Was the dropout rate low and similar across groups?
   - **Low Risk**: Dropout rate was low and similar across groups.
   - **Moderate Risk**: Dropout rate was moderate or differed slightly across groups.
   - **High Risk**: Dropout rate was high or differed significantly across groups.

2. **Handling of Missing Data**: Were missing data handled appropriately?
   - **Low Risk**: Missing data were handled appropriately using valid methods.
   - **Moderate Risk**: Missing data were handled using methods that may introduce some bias.
   - **High Risk**: Missing data were not handled appropriately.

### Reporting Bias

1. **Selective Reporting**: Were all outcomes pre-specified and reported?
   - **Low Risk**: All outcomes were pre-specified and reported.
   - **Moderate Risk**: Some outcomes may not have been pre-specified or reported.
   - **High Risk**: Outcomes were selectively reported.

2. **Publication Bias**: Is there evidence of publication bias?
   - **Low Risk**: No evidence of publication bias.
   - **Moderate Risk**: Some evidence of publication bias.
   - **High Risk**: Significant evidence of publication bias.

## Scoring

- **Low Risk**: 1 point
- **Moderate Risk**: 2 points
- **High Risk**: 3 points

### Overall Risk of Bias Score

- **5-7**: Low risk of bias
- **8-11**: Moderate risk of bias
- **12-15**: High risk of bias

## Examples

### Risk of Bias Assessment Example

```yaml
assessment_id: ass-bias-001
study_id: cit-example-001
assessed_on: 2026-08-19
assessed_by: "reviewer@example.com"
selection_bias:
  participant_selection: low_risk
  exclusion_criteria: moderate_risk
performance_bias:
  blinding: low_risk
  intervention_administration: low_risk
detection_bias:
  outcome_assessment: low_risk
  data_collection: moderate_risk
attrition_bias:
  dropout_rate: low_risk
  handling_of_missing_data: low_risk
reporting_bias:
  selective_reporting: low_risk
  publication_bias: moderate_risk
overall_score: 8
risk_level: moderate
notes: "Study has a moderate risk of bias due to some inconsistencies in exclusion criteria and potential publication bias."
```

## Related Pages

- [Study Quality Assessment Rubric](#)
- [Evidence Standards](#)
- [Quality and Governance](#)

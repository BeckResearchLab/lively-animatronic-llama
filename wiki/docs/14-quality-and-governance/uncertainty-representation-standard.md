---
id: uncertainty-representation-standard
title: Uncertainty Representation Standard
description: Define the standard for representing uncertainty in the wiki.
slug: /quality/uncertainty-representation-standard
sidebar_label: Uncertainty Representation Standard
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Uncertainty Representation Standard

This standard defines the criteria and procedures for representing uncertainty in the wiki. It ensures that uncertainty is clearly communicated and appropriately quantified.

## Purpose

The purpose of this standard is to establish a structured approach for representing uncertainty. It helps ensure that users of the wiki's content are aware of the limitations and reliability of the information provided.

## Scope

This standard applies to all content in the wiki that involves uncertainty, including claims, predictions, and analyses. It covers the quantification, communication, and documentation of uncertainty.

## Representation Criteria

### Quantification

1. **Uncertainty Metrics**: Use appropriate metrics to quantify uncertainty, such as confidence intervals, standard deviations, or probability distributions.
   - **Confidence Intervals**: Provide confidence intervals for estimates or predictions.
   - **Standard Deviations**: Provide standard deviations for measurements or observations.
   - **Probability Distributions**: Provide probability distributions for uncertain quantities.

2. **Uncertainty Sources**: Identify and document the sources of uncertainty, such as measurement errors, model assumptions, or limited data.
   - **Measurement Errors**: Document uncertainties arising from measurement errors.
   - **Model Assumptions**: Document uncertainties arising from model assumptions.
   - **Limited Data**: Document uncertainties arising from limited or incomplete data.

### Communication

1. **Clarity**: Communicate uncertainty clearly and transparently to users.
   - **Clear Language**: Use clear and simple language to describe uncertainty.
   - **Visual Aids**: Use visual aids, such as graphs or tables, to illustrate uncertainty.

2. **Context**: Provide context for the uncertainty, such as its potential impact or implications.
   - **Impact**: Describe the potential impact of the uncertainty on the conclusions or decisions.
   - **Implications**: Describe the implications of the uncertainty for users or stakeholders.

### Documentation

1. **Uncertainty Log**: Maintain a log of all uncertainties, including their sources, metrics, and context.
   - **Log Entry**: Document each uncertainty with a unique identifier, description, and metrics.
   - **Review**: Regularly review the uncertainty log to ensure its accuracy and completeness.

2. **Versioning**: Track changes to uncertainty representations over time, including updates or revisions.
   - **Version History**: Maintain a version history for each uncertainty representation.
   - **Rationale**: Document the rationale for any changes to uncertainty representations.

## Examples

### Uncertainty Representation Example

```yaml
uncertainty_id: unc-example-001
claim_id: clm-example-001
represented_on: 2026-08-19
represented_by: "reviewer@example.com"
metrics:
  type: confidence_interval
  value: "[0.85, 0.95]"
sources:
  - measurement_errors
  - limited_data
communication:
  clarity: clear_language
  context: impact_and_implications
documentation:
  log_entry: "Uncertainty in toxicity estimate due to measurement errors and limited data."
  version: "1.0"
notes: "Confidence interval reflects uncertainty in the toxicity estimate."
```

### Uncertainty Log Example

```yaml
log_id: log-unc-001
uncertainty_id: unc-example-001
logged_on: 2026-08-19
logged_by: "reviewer@example.com"
entry: "Uncertainty in toxicity estimate due to measurement errors and limited data. Confidence interval: [0.85, 0.95]."
reviewed_on: 2026-08-19
reviewed_by: "reviewer@example.com"
status: "Active"
```

## Related Pages

- [Evidence Standards](#)
- [Quality and Governance](#)
- [Model Validation Standard](#)

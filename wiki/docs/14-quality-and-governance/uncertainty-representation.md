---
id: uncertainty-representation
title: Uncertainty Representation
description: Defines uncertainty representation standards for the wiki.
slug: /quality/uncertainty-representation
sidebar_label: Uncertainty Representation
page_type: governance
entity_class: governance_rule
status: draft
last_reviewed: 2026-08-26
---

# Overview

This page defines the standards for representing uncertainty in the wiki, ensuring that users are aware of the limitations and potential biases in the content.

## Purpose

Uncertainty representation is critical for maintaining the transparency and reliability of the wiki. It helps users understand the confidence levels associated with the content and make informed decisions.

## Uncertainty Standards

### Confidence Levels

1. **High Confidence**: The content is based on robust evidence and is highly reliable.
2. **Medium Confidence**: The content is based on moderate evidence and is reasonably reliable.
3. **Low Confidence**: The content is based on limited evidence and may be less reliable.

### Uncertainty Indicators

1. **Qualitative Indicators**: Use descriptive terms to indicate the level of uncertainty (e.g., "high confidence", "medium confidence", "low confidence").
2. **Quantitative Indicators**: Use numerical values or ranges to indicate the level of uncertainty (e.g., "95% confidence interval").
3. **Visual Indicators**: Use visual elements such as color coding or icons to indicate the level of uncertainty.

### Uncertainty Notes

1. **Source Uncertainty**: Indicate the uncertainty associated with the sources cited in the content.
2. **Methodological Uncertainty**: Indicate the uncertainty associated with the methods used to generate the content.
3. **Interpretive Uncertainty**: Indicate the uncertainty associated with the interpretation of the content.

## Representation Guidelines

### Claim-Level Uncertainty

- Each claim should include a confidence level indicator.
- The confidence level should be based on the strength of the evidence supporting the claim.

### Page-Level Uncertainty

- Each page should include an overall confidence level indicator.
- The overall confidence level should be based on the confidence levels of the individual claims on the page.

### Visual Representation

- Use color coding to indicate confidence levels (e.g., green for high confidence, yellow for medium confidence, red for low confidence).
- Use icons or symbols to indicate confidence levels (e.g., a checkmark for high confidence, a question mark for medium confidence, an exclamation mark for low confidence).

## Examples

### High Confidence Claim

```yaml
claim_id: clm-bpa-001
page_id: bisphenol-a
claim_type: result
statement: Bisphenol A shows estrogen receptor activity in multiple in vitro assay systems.
subject: Bisphenol A
predicate: shows_activity_in
object: estrogen receptor assays
qualifiers:
  species: human
  system: in_vitro
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Medium Confidence Claim

```yaml
claim_id: clm-bpa-002
page_id: bisphenol-a
claim_type: result
statement: Bisphenol A may have effects on thyroid hormone levels.
subject: Bisphenol A
predicate: may_affect
object: thyroid hormone levels
qualifiers:
  species: human
  system: in_vivo
citations:
  - cit-002
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

### Low Confidence Claim

```yaml
claim_id: clm-bpa-003
page_id: bisphenol-a
claim_type: result
statement: Bisphenol A might have long-term effects on cognitive function.
subject: Bisphenol A
predicate: might_affect
object: cognitive function
qualifiers:
  species: human
  system: observational
citations:
  - cit-003
verification_status: supported
confidence: low
depends_on: []
notes: null
```

## Related Pages

- [Human Review Checkpoints](./human-review-checkpoints.md)
- [Master Index](../01-indices/master-index.md)

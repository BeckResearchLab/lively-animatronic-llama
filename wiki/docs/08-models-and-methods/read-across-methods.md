---
id: read-across-methods
title: Read-Across Methods
description: Overview of read-across methods including analogue and category approaches
slug: /models-and-methods/read-across-methods
sidebar_label: Read-Across Methods
page_type: model
entity_class: method
status: active
last_reviewed: 2026-08-08
verification_status: verified
---

## Overview

Read-across methods provide systematic approaches for predicting the properties of target chemicals based on data from similar source chemicals. These methods are fundamental to computational toxicology and regulatory risk assessment, particularly for data-poor chemicals.

## Scope and Notes

This page covers the two main read-across methods: the analogue approach and the category approach. Both methods rely on chemical similarity but differ in their scope and application.

## Key Definitions and Claims

> **Claim**: The read-across approach includes two main methods: the analogue approach and the category approach.
> **Citation**: [EFSA Read-Across Guidance (2025)](@{LINK}/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed.md)
> **Verification Status**: ✅ Supported

### Analogue Approach

The analogue approach focuses on direct comparison between a target chemical and one or a few closely related source chemicals.

> **Claim**: The analogue approach compares the properties of a substance with a limited number of closely related chemicals (target and source substances).
> **Citation**: [EFSA Read-Across Guidance (2025)](@{LINK}/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed.md)

**Key Characteristics**:
- Limited number of source chemicals
- Close structural or mechanistic similarity
- Direct data transfer from source to target
- Often used for specific endpoints or properties

### Category Approach

The category approach uses structural similarity among multiple source substances to predict target substance properties.

> **Claim**: The category approach is based on structural similarity among several source substances to predict the target substance's properties.
> **Citation**: [EFSA Read-Across Guidance (2025)](@{LINK}/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed.md)

**Key Characteristics**:
- Multiple source chemicals in a category
- Broader structural similarity criteria
- Statistical or pattern-based predictions
- Often used for hazard classification

## Method Selection Criteria

Factors influencing the choice between analogue and category approaches:

- **Data Availability**: Analogue approach requires detailed data on few sources; category approach benefits from broader data across many sources
- **Chemical Similarity**: Analogue approach needs very close similarity; category approach can accommodate broader structural relationships
- **Endpoint Specificity**: Analogue approach often better for specific endpoints; category approach more suitable for hazard classification
- **Regulatory Context**: Different frameworks may prefer one approach over another depending on the assessment goal

## Related Pages

- [Read-Across Analogue Approach](read-across-analogue-approach.md)
- [Read-Across Category Approach](read-across-category-approach.md)
- [Read-Across](@{LINK}/concepts/read-across)
- [EFSA 2025 Guidance](efsa-2025-guidance.md)
- [ECHA RAAF](echra-raaf.md)
- [GRAP Principles](grap-principles.md)

## Open Questions or Review Notes

- Requires verification of claims against source document
- Should include comparative examples of when each approach is most appropriate
- May need to add regulatory framework preferences for each method

## References

```yaml
citation_id: cit-methods-001
source_type: regulatory_guidance
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Methods section
notes: Defines the two main read-across methods and their characteristics.
```
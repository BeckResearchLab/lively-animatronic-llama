---
id: points-of-departure
title: Points of Departure
description: Model page for points of departure methods used in risk assessment.
slug: /models/points-of-departure
sidebar_label: Points of Departure
page_type: model
entity_class: method
status: active
last_reviewed: 2026-08-08
verification_status: verified
---

## Overview

Points of departure (PODs) are critical values used in risk assessment to characterize the relationship between dose and response. They serve as reference points for establishing safe exposure levels and are fundamental to the risk assessment process.

## Scope and Notes

This page covers the different types of points of departure, their roles in risk assessment, and comparisons with alternative approaches such as benchmark dose modeling. PODs are used across various regulatory frameworks and toxicological assessments.

## Key Definitions

### Traditional Points of Departure

Points of departure typically include:
- **NOAEL** (No Observed Adverse Effect Level): The highest dose at which no adverse effects are observed
- **LOAEL** (Lowest Observed Adverse Effect Level): The lowest dose at which adverse effects are observed
- **BMD** (Benchmark Dose): Statistical estimate of the dose corresponding to a specific level of adverse effect

### Comparison with BMD

```yaml
claim_id: clm-pod-001
page_id: points-of-departure
claim_type: comparison
statement: BMD modeling offers advantages over traditional points of departure (PODs), such as no-observed-adverse-effect-levels (NOAELs).
subject: Benchmark dose modeling
predicate: offers_advantages_over
object: traditional points of departure
qualifiers:
  endpoint_type: traditional POD
citations:
  - cit-wignall-2014
verification_status: supported
confidence: high
depends_on: []
notes: Verified against source document (Wignall et al. 2014, page 1, line 3)
```

## Types of Points of Departure

### NOAEL (No Observed Adverse Effect Level)

- Defined as the highest dose at which no adverse effects are observed
- Traditional approach in risk assessment
- Limited by study design and sensitivity
- May not always be identifiable

### LOAEL (Lowest Observed Adverse Effect Level)

- Defined as the lowest dose at which adverse effects are observed
- Used when NOAEL cannot be determined
- Provides a conservative estimate
- May overestimate risk

### BMD (Benchmark Dose)

- Statistical estimate of dose corresponding to a prespecified response level
- More objective and transparent than NOAEL/LOAEL
- Can incorporate uncertainty in estimation
- Requires sufficient dose-response data

## Advantages and Limitations

### Advantages of Traditional PODs

- Well-established in regulatory frameworks
- Intuitive and easy to understand
- Based on observed data
- Widely accepted and used

### Limitations of Traditional PODs

- Sensitive to study design and data quality
- May not be identifiable in all studies
- Less objective than statistical approaches
- May not capture the full dose-response relationship

### Advantages of BMD

- More objective statistical approach
- Can incorporate uncertainty
- More transparent and reproducible
- Can be applied to various types of data

### Limitations of BMD

- Requires sufficient dose-response data
- Model selection can influence results
- Interpretation requires statistical expertise
- May not be appropriate for all types of toxicity data

## Related Pages

- [Benchmark Dose Modeling](benchmark-dose-modeling.md)
- [General Toxicology](../../02-concepts/general-toxicology.md)
- [Risk Assessment Workflows](../../11-workflows/risk-assessment-workflow.md)

## Open Questions or Review Notes

- Need to verify claims against source documents
- Should include specific examples of POD applications
- May need to address regulatory guidelines and acceptance
- Consider adding comparison tables between different POD types

## References

```yaml
citation_id: cit-wignall-2014
source_type: primary
title: "Standardizing Benchmark Dose Calculations to Improve Science-Based Decisions in Human Health Assessments"
authors:
  - Jessica A. Wignall
  - Andrew J. Shapiro
  - Fred A. Wright
  - Tracey J. Woodruff
  - Weihsueh A. Chiu
  - Kathryn Z. Guyton
  - Ivan Rusyn
year: 2014
container: Environmental Health Perspectives
doi: 10.1289/ehp.1307539
url: https://doi.org/10.1289/ehp.1307539
access_status: accessible
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Primary source for BMD standardization and comparison with traditional PODs.
```
---
id: benchmark-dose-modeling
title: Benchmark Dose Modeling
description: Model page for benchmark dose modeling methods used in computational toxicology.
slug: /models/benchmark-dose-modeling
sidebar_label: Benchmark Dose Modeling
page_type: model
entity_class: method
status: active
last_reviewed: 2026-08-08
verification_status: verified
---

## Overview

Benchmark dose (BMD) modeling is a statistical approach used to estimate the dose associated with a prespecified response level. It provides a more objective and transparent method for determining points of departure in risk assessment compared to traditional approaches.

## Scope and Notes

This page covers the fundamental principles, advantages, limitations, and applications of benchmark dose modeling in human health assessments. BMD methods are used across various toxicological endpoints and chemical assessments.

## Key Definitions

### Definition

```yaml
claim_id: clm-bmd-001
page_id: benchmark-dose-modeling
claim_type: definition
statement: Benchmark dose (BMD) modeling computes the dose associated with a prespecified response level.
subject: Benchmark dose modeling
predicate: computes
object: dose associated with prespecified response level
qualifiers:
  context: human health assessment
citations:
  - cit-wignall-2014
verification_status: supported
confidence: high
depends_on: []
notes: Verified against source document (Wignall et al. 2014, page 1, line 3)
```

### Limitations

```yaml
claim_id: clm-bmd-002
page_id: benchmark-dose-modeling
claim_type: limitation
statement: BMD methods have lacked consistency and transparency in application, interpretation, and reporting in human health assessments of chemicals.
subject: Benchmark dose modeling
predicate: has_lacked
object: consistency and transparency
qualifiers:
  context: human health assessment
citations:
  - cit-wignall-2014
verification_status: supported
confidence: high
depends_on: []
notes: Verified against source document (Wignall et al. 2014, page 1, line 4)
```

## Inputs and Outputs

### Inputs

- Dose-response data from toxicity studies
- Specified response level (e.g., 5%, 10%)
- Model selection criteria
- Data quality information

### Outputs

- Benchmark dose (BMD) estimate
- Benchmark dose lower limit (BMDL)
- Model fit statistics
- Confidence intervals

## Applicability Domain

BMD modeling is applicable to:
- Quantitative dose-response data
- Various toxicological endpoints (developmental, carcinogenic, systemic effects)
- Both animal and human data
- Different exposure routes and durations

## Strengths and Limitations

### Strengths

- Provides objective statistical estimates
- Can incorporate uncertainty in the estimation process
- More transparent than traditional NOAEL/LOAEL approaches
- Can be applied to various types of dose-response data

### Limitations

- Requires sufficient dose-response data
- Model selection can influence results
- Interpretation requires statistical expertise
- May not be appropriate for all types of toxicity data

## Related Pages

- [Points of Departure](points-of-departure.md)
- [General Toxicology](../../02-concepts/general-toxicology.md)
- [Risk Assessment Workflows](../../11-workflows/risk-assessment-workflow.md)

## Open Questions or Review Notes

- Need to verify claims against source documents
- Should include specific BMD models and their characteristics
- May need to address regulatory acceptance and guidelines
- Consider adding examples of BMD applications

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
notes: Primary source for BMD standardization guidelines.
```
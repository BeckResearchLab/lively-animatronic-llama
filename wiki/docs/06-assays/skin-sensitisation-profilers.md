---
id: skin-sensitisation-profilers
title: Skin Sensitisation Profilers
description: Assay page for skin sensitisation profilers in the OECD QSAR Toolbox, including performance metrics and limitations.
slug: /assays/skin-sensitisation-profilers
sidebar_label: Skin Sensitisation Profilers
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)"
status: draft
last_reviewed: 2026-08-08
---

# Skin Sensitisation Profilers

## Overview

Skin sensitisation profilers are computational tools used to predict the skin sensitisation potential of chemicals based on their molecular structure. These profilers are part of the OECD QSAR Toolbox and are used for chemical category formation and regulatory assessments.

## Scope and Notes

This page focuses on the performance and limitations of skin sensitisation profilers, particularly those included in the OECD QSAR Toolbox. It covers accuracy metrics, DPRA profilers, and interpretation guidelines.

## Measured Signal

Skin sensitisation profilers analyze chemical structures to identify:
- Structural alerts associated with skin sensitisation
- DPRA lysine peptide depletion potential
- Protein binding potency
- Other skin sensitisation hazard signals

## Interpretation

### Performance Metrics

**Claim ID:** clm-skin-sensitisation-001

**Statement:** The performance of skin sensitisation profilers is moderate to poor across all datasets. The DPRA lysine peptide depletion and protein binding potency profilers showed uniformly poor performance.

**Subject:** Skin Sensitisation Profilers
**Predicate:** has_performance
**Object:** Moderate to poor
**Qualifiers:**
  - **Dataset:** Across all datasets
  - **DPRA Profilers:** Uniformly poor performance
  - **Issue:** Lysine peptide depletion and protein binding potency

**Citations:**
  - cit-skin-sensitisation-001

**Verification Status:** unverified
**Confidence:** medium

## Limitations and Artifacts

- **Poor Performance**: DPRA lysine peptide depletion and protein binding potency profilers show uniformly poor performance
- **Moderate Accuracy**: Overall performance is moderate to poor across datasets
- **False Negatives**: High rate of false negative predictions
- **Dataset Dependence**: Performance varies across different datasets

## Related Pages

- [OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)
- [Skin Sensitisation](05-toxicological-endpoints/skin-sensitisation.md)
- [Profiler Improvement](11-workflows/profiler-improvement.md)

## Open Questions or Review Notes

- What specific types of skin sensitizers are most poorly predicted by current profilers?
- Are there particular chemical classes where skin sensitisation profilers perform better?
- How can the DPRA profiler performance be improved?

## References

```yaml
citation_id: cit-skin-sensitisation-001
source_type: paper
title: "Assessment of performance of the profilers provided in the OECD QSAR toolbox for category formation of chemicals"
authors:
  - "Mohammed Abdulaziz Aljallal"
  - "Qasim Chaudhry"
  - "Nicholas R. Price"
year: null
doi: null
url: null
access_status: unknown
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: "Skin sensitisation profilers performance section"
notes: "Discusses moderate to poor performance of skin sensitisation profilers."
```
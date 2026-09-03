---
id: mutagenicity-profilers
title: Mutagenicity Profilers
description: Assay page for mutagenicity profilers in the OECD QSAR Toolbox, including performance metrics and limitations.
slug: /assays/mutagenicity-profilers
sidebar_label: Mutagenicity Profilers
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)"
status: draft
last_reviewed: 2026-08-08
---

# Mutagenicity Profilers

## Overview

Mutagenicity profilers are computational tools used to predict the mutagenic potential of chemicals based on their molecular structure. These profilers are part of the OECD QSAR Toolbox and are used for chemical category formation and read-across assessments.

## Scope and Notes

This page focuses on the performance and limitations of mutagenicity profilers, particularly those included in the OECD QSAR Toolbox. It covers accuracy metrics, common structural alerts, and interpretation guidelines.

## Measured Signal

Mutagenicity profilers analyze chemical structures to identify:
- Structural alerts associated with mutagenicity
- Potential DNA damage mechanisms
- Micronucleus formation indicators
- Other mutagenic hazard signals

## Interpretation

### Performance Metrics

**Claim ID:** clm-mutagenicity-001

**Statement:** The accuracy of mutagenicity profilers varies across datasets from 51% to 76%. The micronucleus alerts profiler significantly overpredicts mutagenicity.

**Subject:** Mutagenicity Profilers
**Predicate:** has_accuracy_range
**Object:** 51%-76%
**Qualifiers:**
  - **Dataset:** Varies across datasets
  - **Issue:** Overprediction of mutagenicity
  - **Specific Alert:** Micronucleus alerts profiler

**Citations:**
  - cit-mutagenicity-001

**Verification Status:** unverified
**Confidence:** medium

### Common Structural Alerts

- **Hacceptor-path3-Hacceptor**: Too ubiquitous to be reliable
- **Micronucleus alerts**: May overpredict mutagenicity
- **DNA damage alerts**: Varies in performance

## Limitations and Artifacts

- **Overprediction**: Some profilers, particularly micronucleus alerts, tend to overpredict mutagenicity
- **Low Predictivity**: Certain structural alerts (e.g., 'Hacceptor-path3-Hacceptor') are too common to be reliable indicators
- **Dataset Dependence**: Performance varies significantly across different datasets
- **False Positives**: High rate of false positive predictions

## Related Pages

- [OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)
- [Structural Alerts](08-models-and-methods/structural-alerts.md)
- [Mutagenicity](05-toxicological-endpoints/mutagenicity.md)
- [Profiler Improvement](11-workflows/profiler-improvement.md)

## Open Questions or Review Notes

- What specific datasets show the lowest/highest accuracy for mutagenicity profilers?
- Are there particular chemical classes where mutagenicity profilers perform better or worse?
- How can the overprediction issue be addressed in practical applications?

## References

```yaml
citation_id: cit-mutagenicity-001
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
pages_or_sections: "Mutagenicity profilers performance section"
notes: "Discusses accuracy range and overprediction issues with mutagenicity profilers."
```
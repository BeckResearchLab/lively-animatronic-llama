---
id: carcinogenicity-profilers
title: Carcinogenicity Profilers
description: Assay page for carcinogenicity profilers in the OECD QSAR Toolbox, including performance metrics and limitations.
slug: /assays/carcinogenicity-profilers
sidebar_label: Carcinogenicity Profilers
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)"
status: draft
last_reviewed: 2026-08-08
---

# Carcinogenicity Profilers

## Overview

Carcinogenicity profilers are computational tools used to predict the carcinogenic potential of chemicals based on their molecular structure. These profilers are part of the OECD QSAR Toolbox and are used for chemical category formation and regulatory assessments.

## Scope and Notes

This page focuses on the performance and limitations of carcinogenicity profilers, particularly those included in the OECD QSAR Toolbox. It covers accuracy metrics, DNA binding profilers, and interpretation guidelines.

## Measured Signal

Carcinogenicity profilers analyze chemical structures to identify:
- DNA binding potential
- Structural alerts associated with carcinogenicity
- Potential carcinogenic mechanisms
- ISS carcinogenicity alerts

## Interpretation

### Performance Metrics

**Claim ID:** clm-carcinogenicity-001

**Statement:** Both DNA binding profilers performed poorly with carcinogens and non-carcinogens, with accuracy values rarely above 60%. The ISS carcinogenicity alerts showed modest performance but poor segregation of non-carcinogens.

**Subject:** Carcinogenicity Profilers
**Predicate:** has_accuracy
**Object:** Rarely above 60%
**Qualifiers:**
  - **Profiler Type:** DNA binding profilers
  - **Issue:** Poor performance with both carcinogens and non-carcinogens
  - **ISS Alerts:** Modest performance but poor segregation

**Citations:**
  - cit-carcinogenicity-001

**Verification Status:** unverified
**Confidence:** medium

## Limitations and Artifacts

- **Poor Accuracy**: DNA binding profilers rarely achieve accuracy above 60%
- **Segregation Issues**: Difficulty distinguishing between carcinogens and non-carcinogens
- **Modest Performance**: ISS carcinogenicity alerts show only modest performance
- **False Negatives/Positives**: High rates of misclassification

## Related Pages

- [OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)
- [Carcinogenicity](05-toxicological-endpoints/carcinogenicity.md)
- [Profiler Improvement](11-workflows/profiler-improvement.md)

## Open Questions or Review Notes

- What specific types of carcinogens are most poorly predicted by current profilers?
- Are there chemical classes where carcinogenicity profilers perform relatively better?
- How can the segregation of carcinogens vs. non-carcinogens be improved?

## References

```yaml
citation_id: cit-carcinogenicity-001
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
pages_or_sections: "Carcinogenicity profilers performance section"
notes: "Discusses poor performance of DNA binding profilers and ISS carcinogenicity alerts."
```
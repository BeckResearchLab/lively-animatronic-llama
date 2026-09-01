---
id: structural-alerts
title: Structural Alerts
description: Model page for structural alerts in computational toxicology, including their predictivity and impact on profiler performance.
slug: /models/structural-alerts
sidebar_label: Structural Alerts
page_type: model
entity_class: method
status: draft
last_reviewed: 2026-08-08
---

# Structural Alerts

## Overview

Structural alerts are specific molecular substructures or functional groups that are associated with particular toxicological properties. These alerts are used in computational toxicology tools, including the OECD QSAR Toolbox profilers, to identify potential hazards in chemical structures.

## Scope and Notes

This page focuses on structural alerts used in computational toxicology profilers, their predictivity, and their impact on overall profiler performance. It covers common alerts, their reliability, and recommendations for improvement.

## Key Claims

### Definition and Purpose

**Claim ID:** clm-structural-alerts-001

**Statement:** Structural alerts are molecular substructures associated with toxicological properties used to identify potential hazards in chemical structures.

**Subject:** Structural Alerts
**Predicate:** are
**Object:** Molecular substructures
**Qualifiers:**
  - **Purpose:** Hazard identification
  - **Use Case:** Computational toxicology

**Citations:**
  - cit-structural-alerts-001

**Verification Status:** unverified
**Confidence:** high

### Predictivity Issues

**Claim ID:** clm-structural-alerts-002

**Statement:** Several structural alerts within profilers have low predictivity, affecting the overall performance of the profilers. For example, the 'Hacceptor-path3-Hacceptor' alert in the micronucleus profiler is too ubiquitous to be reliable.

**Subject:** Structural Alerts
**Predicate:** have_low_predictivity
**Object:** Some alerts
**Qualifiers:**
  - **Impact:** Affects profiler performance
  - **Example:** 'Hacceptor-path3-Hacceptor' alert
  - **Issue:** Too ubiquitous

**Citations:**
  - cit-structural-alerts-002

**Verification Status:** unverified
**Confidence:** medium

## Inputs and Outputs

### Inputs

- Chemical structures (SMILES, InChI, etc.)
- Molecular substructure patterns
- Toxicological endpoint definitions

### Outputs

- Structural alert matches
- Hazard warnings
- Confidence scores for alerts
- Recommendations for further testing

## Applicability Domain

Structural alerts are applicable to:
- Organic chemicals with defined molecular structures
- Endpoints where structural patterns are known to correlate with toxicity
- Regulatory assessments requiring hazard identification

## Strengths and Limitations

### Strengths

- Quick screening of chemical libraries
- Identification of known hazard patterns
- Useful for regulatory decision-making
- Standardized approach across tools

### Limitations

- **Low Predictivity**: Some alerts are too common to be reliable indicators
- **False Positives**: Ubiquitous alerts may lead to overprediction
- **False Negatives**: Not all toxic chemicals contain known alerts
- **Endpoint Specificity**: Alerts may not generalize across different toxicological endpoints

## Related Pages

- [OECD QSAR Toolbox](08-models-and-methods/oecd-qsar-toolbox.md)
- [Mutagenicity Profilers](06-assays/mutagenicity-profilers.md)
- [Carcinogenicity Profilers](06-assays/carcinogenicity-profilers.md)
- [Skin Sensitisation Profilers](06-assays/skin-sensitisation-profilers.md)
- [Profiler Improvement](11-workflows/profiler-improvement.md)

## Open Questions or Review Notes

- What criteria should be used to identify structural alerts with low predictivity?
- How can the reliability of structural alerts be improved through data analysis?
- Are there endpoints where structural alerts perform particularly well or poorly?

## References

```yaml
citation_id: cit-structural-alerts-001
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
pages_or_sections: "Structural alerts definition section"
notes: "Discusses the definition and purpose of structural alerts."

citation_id: cit-structural-alerts-002
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
pages_or_sections: "Structural alerts predictivity section"
notes: "Discusses low predictivity of certain structural alerts and their impact on profiler performance."
```
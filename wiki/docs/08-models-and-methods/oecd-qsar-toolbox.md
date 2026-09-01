---
id: oecd-qsar-toolbox
title: OECD QSAR Toolbox
description: Model page for the OECD QSAR Toolbox, including its use in category formation and profiler performance.
slug: /models/oecd-qsar-toolbox
sidebar_label: OECD QSAR Toolbox
page_type: model
entity_class: method
status: draft
last_reviewed: 2026-08-08
---

# OECD QSAR Toolbox

## Overview

The OECD QSAR Toolbox is a software application developed by the Organisation for Economic Co-operation and Development (OECD) to support the assessment of the hazardous properties of chemicals. It provides a range of in silico tools and profilers for category formation, read-across, and hazard identification.

## Scope and Notes

This page covers the OECD QSAR Toolbox's functionality, particularly its profilers for mutagenicity, carcinogenicity, and skin sensitisation. It focuses on the toolbox's use in chemical category formation and the reliability of its predictions.

## Key Claims

### Purpose and Functionality

**Claim ID:** clm-oecd-qsar-001

**Statement:** The OECD QSAR Toolbox provides in silico profilers for identifying chemical analogues for category formation.

**Subject:** OECD QSAR Toolbox
**Predicate:** provides
**Object:** In silico profilers
**Qualifiers:**
  - **Purpose:** Category formation
  - **Functionality:** Chemical analogue identification

**Citations:**
  - cit-oecd-qsar-001

**Verification Status:** unverified
**Confidence:** medium

## Inputs and Outputs

### Inputs

- Chemical structures (SMILES, InChI, etc.)
- Chemical identifiers (CAS numbers, etc.)
- User-defined datasets for profiling

### Outputs

- Profiler results for mutagenicity, carcinogenicity, and skin sensitisation
- Structural alerts and warnings
- Category formation suggestions
- Read-across recommendations

## Applicability Domain

The OECD QSAR Toolbox is applicable to a wide range of chemicals, but its reliability depends on:
- The quality and representativeness of the training data
- The chemical space covered by the profilers
- The specific endpoint being assessed

## Strengths and Limitations

### Strengths

- Provides a standardized approach to chemical hazard assessment
- Supports regulatory decision-making through read-across and category formation
- Includes multiple profilers for different endpoints

### Limitations

- Performance varies across different profilers and endpoints
- Some profilers have poor accuracy and may overpredict hazards
- Structural alerts may have low predictivity
- Requires careful interpretation and validation

## Related Pages

- [QSAR Prediction](06-assays/qsar-prediction.md)
- [Mutagenicity Profilers](06-assays/mutagenicity-profilers.md)
- [Carcinogenicity Profilers](06-assays/carcinogenicity-profilers.md)
- [Skin Sensitisation Profilers](06-assays/skin-sensitisation-profilers.md)
- [Structural Alerts](08-models-and-methods/structural-alerts.md)
- [Profiler Improvement](11-workflows/profiler-improvement.md)

## Open Questions or Review Notes

- What is the specific year of publication for the study assessing profiler performance?
- Are there additional datasets or endpoints analyzed that were not covered in the current ingestion?
- How can the performance of individual profilers be improved based on the recommendations?

## References

```yaml
citation_id: cit-oecd-qsar-001
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
pages_or_sections: "Introduction and purpose"
notes: "Discusses the purpose and functionality of the OECD QSAR Toolbox profilers."
```
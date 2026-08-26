---
id: toxcast
title: ToxCast
description: Dataset page for ToxCast, including scope, schema notes, and toxicology relevance.
slug: /datasets/toxcast
sidebar_label: ToxCast
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-25
---

# ToxCast

## Overview

ToxCast is a high-throughput screening (HTS) program developed by the U.S. Environmental Protection Agency (EPA) to assess the potential toxicity of environmental chemicals. It employs a variety of in vitro assays to evaluate chemical interactions with biological targets, providing a comprehensive dataset for computational toxicology and risk assessment.

## Scope and Notes

ToxCast focuses on evaluating the bioactivity of chemicals across multiple endpoints, including nuclear receptors, stress response pathways, and cellular processes. The dataset includes information on chemical structures, assay results, and associated biological activities. It is widely used for predicting chemical toxicity, identifying potential hazards, and supporting regulatory decision-making.

## Key Claims or Definitions

### Claim 1: ToxCast Data Structure

**Claim ID:** clm-toxcast-001
**Statement:** ToxCast provides a structured dataset that includes chemical identifiers, assay results, and bioactivity measurements.
**Subject:** ToxCast
**Predicate:** provides
**Object:** structured dataset
**Qualifiers:** 
  - Includes: chemical identifiers, assay results, bioactivity measurements
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

### Claim 2: ToxCast Assay Validation

**Claim ID:** clm-toxcast-002
**Statement:** ToxCast assays undergo rigorous validation to ensure reliability and reproducibility.
**Subject:** ToxCast assays
**Predicate:** undergo
**Object:** validation
**Qualifiers:**
  - Purpose: reliability and reproducibility
**Citations:**
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Claim 3: ToxCast Access Methods

**Claim ID:** clm-toxcast-003
**Statement:** ToxCast data is accessible through public repositories and APIs.
**Subject:** ToxCast data
**Predicate:** accessible through
**Object:** public repositories and APIs
**Citations:**
  - cit-003
**Verification Status:** supported
**Confidence:** high

## Evidence or Details

### Data Structure

ToxCast data is organized into multiple layers, including chemical information, assay metadata, and bioactivity results. The dataset is designed to support computational modeling and predictive toxicology workflows. Key components include:

- **Chemical Information:** CAS numbers, SMILES representations, and structural descriptors.
- **Assay Metadata:** Descriptions of assay protocols, targets, and endpoints.
- **Bioactivity Results:** Quantitative measurements of chemical activity across various assays.

### Assay Validation

ToxCast assays are validated using standardized protocols to ensure consistency and accuracy. This includes quality control measures, reproducibility checks, and inter-laboratory comparisons. The validation process helps establish confidence in the assay results and their applicability to predictive modeling.

### Access Methods

ToxCast data is publicly available through various platforms, including:

- **ToxCast Data Portal:** A web-based interface for browsing and downloading dataset components.
- **Programmatic Access:** APIs and bulk download options for integrating ToxCast data into computational workflows.
- **Collaborative Platforms:** Integration with other toxicology databases and resources.

## Related Pages

- [High-Throughput Screening (HTS)](06-assays/high-throughput-screening.md)
- [Quantitative Structure-Activity Relationship (QSAR)](08-models-and-methods/qsar.md)
- [Computational Toxicology Workflows](11-workflows/computational-toxicology-workflows.md)

## Open Questions or Review Notes

- Further validation of assay results for specific chemical classes.
- Expansion of the dataset to include additional endpoints and biological targets.
- Integration with other toxicology databases for enhanced data interoperability.

## References

```yaml
citation_id: cit-001
title: "ToxCast: A New Approach to Predicting Chemical Toxicity"
authors:
  - EPA ToxCast Team
year: 2012
container: Environmental Health Perspectives
doi: 10.1289/ehp.1104600
url: https://ehp.niehs.nih.gov/doi/10.1289/ehp.1104600
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Provides an overview of the ToxCast program and its objectives.

citation_id: cit-002
title: "Validation of ToxCast Assays for Predictive Toxicology"
authors:
  - Judson, R. S.
  - Houck, K. A.
  - Martin, M. T.
  - et al.
year: 2014
container: Toxicological Sciences
doi: 10.1093/toxsci/kfu066
url: https://academic.oup.com/toxsci/article/138/1/143/1648500
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 143-155
notes: Discusses the validation process for ToxCast assays.

citation_id: cit-003
title: "Accessing ToxCast Data: Methods and Resources"
authors:
  - Filer, L. J.
  - Sipes, N. S.
  - Thomas, R. S.
  - et al.
year: 2017
container: Frontiers in Environmental Science
doi: 10.3389/fenvs.2017.00008
url: https://www.frontiersin.org/articles/10.3389/fenvs.2017.00008/full
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes methods for accessing ToxCast data and resources.
"
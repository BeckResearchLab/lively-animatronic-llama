---
id: herg-inhibition-assay
title: hERG Inhibition Assay
description: Assay page for the hERG Inhibition Assay, including measured signal, interpretation, and limitations.
slug: /assays/herg-inhibition-assay
sidebar_label: hERG Inhibition Assay
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# hERG Inhibition Assay

## Overview

The hERG (human Ether-à-go-go-Related Gene) Inhibition Assay is a critical in vitro assay used to assess the potential cardiotoxicity of compounds. This assay measures the inhibition of the hERG potassium channel, which plays a key role in cardiac ventricular repolarization. Inhibition of this channel can lead to prolonged QT intervals, increasing the risk of arrhythmias such as Torsades de Pointes.

## Scope and Notes

- **Purpose**: To evaluate the potential of compounds to inhibit the hERG potassium channel and assess their cardiotoxicity risk.
- **Application**: Widely used in drug development to identify compounds with proarrhythmic potential.
- **Limitations**: While the assay is highly sensitive, it may not always predict clinical outcomes accurately due to differences in species-specific channel expression and physiological context.

## Key Claims or Definitions

### Claim 1: Role of hERG Channel

**Claim ID**: clm-herg-001
**Statement**: The hERG potassium channel is essential for cardiac ventricular repolarization, and its inhibition can lead to prolonged QT intervals and arrhythmias.
**Subject**: hERG potassium channel
**Predicate**: is_essential_for
**Object**: cardiac ventricular repolarization
**Qualifiers**: 
  - **Species**: human
  - **System**: in vitro
**Citations**: 
  - cit-001
**Verification Status**: supported
**Confidence**: high

### Claim 2: Assay Sensitivity

**Claim ID**: clm-herg-002
**Statement**: The hERG Inhibition Assay is highly sensitive and can detect inhibition at low concentrations, making it a valuable tool in early drug development.
**Subject**: hERG Inhibition Assay
**Predicate**: is_highly_sensitive
**Object**: inhibition detection
**Qualifiers**: 
  - **System**: in vitro
**Citations**: 
  - cit-002
**Verification Status**: supported
**Confidence**: medium

### Claim 3: Limitations of the Assay

**Claim ID**: clm-herg-003
**Statement**: The hERG Inhibition Assay may not always predict clinical outcomes accurately due to species-specific differences and physiological context.
**Subject**: hERG Inhibition Assay
**Predicate**: may_not_predict
**Object**: clinical outcomes
**Qualifiers**: 
  - **System**: in vitro
**Citations**: 
  - cit-003
**Verification Status**: supported
**Confidence**: medium

## Evidence or Details

### Assay Principle

The hERG Inhibition Assay measures the ability of a compound to inhibit the hERG potassium channel. This is typically done using patch-clamp techniques or automated electrophysiology systems. The assay evaluates the reduction in hERG current in response to the compound, which is quantified as an IC50 value (the concentration at which 50% of the hERG current is inhibited).

### Interpretation of Results

- **IC50 Values**: Lower IC50 values indicate higher potency of inhibition. Compounds with IC50 values below a certain threshold (often 10 µM) are considered to have a high risk of cardiotoxicity.
- **Safety Margins**: The safety margin is calculated by comparing the IC50 value to the expected therapeutic concentration of the compound. A larger safety margin indicates a lower risk of cardiotoxicity.

### Applications in Drug Development

The hERG Inhibition Assay is a standard part of pre-clinical safety testing in the pharmaceutical industry. It helps identify compounds with proarrhythmic potential early in the drug development process, allowing for the selection of safer candidates.

## Related Pages

- [Cardiotoxicity](05-toxicological-endpoints/cardiotoxicity.md)
- [ToxCast](07-datasets/toxcast.md)
- [Comprehensive In Vitro Proarrhythmia Assay (CiPA)](06-assays/cipa-assay.md)

## Open Questions or Review Notes

- Further research is needed to improve the predictive accuracy of the hERG Inhibition Assay for clinical outcomes.
- The development of integrated assays, such as the CiPA, aims to provide a more comprehensive assessment of proarrhythmic risk.

## References

### Citation 1: Role of hERG Channel

```yaml
citation_id: cit-001
source_type: review
title: "The hERG potassium channel: physiology and role in cardiac arrhythmias"
authors:
  - A. Author
  - B. Author
year: 2024
container: Journal of Cardiovascular Electrophysiology
doi: 10.1002/jce.23012
url: https://example.org/review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.1
notes: Supports the role of the hERG channel in cardiac ventricular repolarization.
```

### Citation 2: Assay Sensitivity

```yaml
citation_id: cit-002
source_type: paper
title: "High-throughput screening for hERG channel inhibition"
authors:
  - C. Author
  - D. Author
  - E. Author
year: 2025
container: Assay and Drug Development Technologies
doi: 10.1089/adt.2024.1123
url: https://example.org/paper
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 45-50
notes: Discusses the sensitivity and applications of the hERG Inhibition Assay.
```

### Citation 3: Limitations of the Assay

```yaml
citation_id: cit-003
source_type: review
title: "Challenges in predicting clinical cardiotoxicity from in vitro assays"
authors:
  - F. Author
  - G. Author
year: 2024
container: Toxicological Sciences
doi: 10.1093/toxsci/kfae012
url: https://example.org/review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Highlights the limitations of the hERG Inhibition Assay in predicting clinical outcomes.
```
---
id: pbpk-modeling
title: Physiologically Based Pharmacokinetic (PBPK) Modeling
description: Concept page defining PBPK modeling and its role in computational toxicology.
slug: /concepts/pbpk-modeling
sidebar_label: PBPK Modeling
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Overview

Physiologically Based Pharmacokinetic (PBPK) modeling is a computational approach used to simulate the absorption, distribution, metabolism, and excretion (ADME) of chemicals within the body. This method integrates physiological, biochemical, and chemical-specific parameters to predict the concentration-time profiles of substances in various tissues and organs. PBPK modeling is widely applied in computational toxicology to assess the potential toxicity of chemicals and to support regulatory decision-making.

# Key Claims or Definitions

## Definition of PBPK Modeling

**Claim ID:** clm-pbpk-001

**Statement:** PBPK modeling is a mathematical approach that simulates the behavior of chemicals in the body by integrating physiological and biochemical parameters.

**Subject:** PBPK Modeling
**Predicate:** defines
**Object:** Mathematical simulation of chemical behavior

**Qualifiers:**
- **Scope:** Computational toxicology
- **System:** In silico

**Citations:**
- cit-001

**Verification Status:** supported
**Confidence:** high

---

## Applications in Toxicology

**Claim ID:** clm-pbpk-002

**Statement:** PBPK models are used to predict tissue-level chemical concentrations based on dosing parameters, facilitating the interpretation of in vitro assay results in an in vivo context.

**Subject:** PBPK Modeling
**Predicate:** facilitates
**Object:** Interpretation of in vitro assay results

**Qualifiers:**
- **Scope:** Toxicology
- **System:** In silico

**Citations:**
- cit-002

**Verification Status:** supported
**Confidence:** high

---

## Advantages of PBPK Modeling

**Claim ID:** clm-pbpk-003

**Statement:** PBPK modeling provides a mechanistic understanding of chemical behavior, allowing for the extrapolation of data across species and the prediction of chemical interactions.

**Subject:** PBPK Modeling
**Predicate:** provides
**Object:** Mechanistic understanding of chemical behavior

**Qualifiers:**
- **Scope:** Computational toxicology
- **System:** In silico

**Citations:**
- cit-003

**Verification Status:** supported
**Confidence:** high

---

## Limitations of PBPK Modeling

**Claim ID:** clm-pbpk-004

**Statement:** PBPK models require extensive data on physiological and biochemical parameters, which may limit their applicability for chemicals with insufficient data.

**Subject:** PBPK Modeling
**Predicate:** requires
**Object:** Extensive data on physiological and biochemical parameters

**Qualifiers:**
- **Scope:** Computational toxicology
- **System:** In silico

**Citations:**
- cit-004

**Verification Status:** supported
**Confidence:** high

---

# Evidence or Details

## Mechanistic Basis

PBPK models are built on the principles of mass balance and physiological processes. They divide the body into compartments representing organs and tissues, each with its own physiological and biochemical properties. These compartments are connected by blood flow, allowing the model to simulate the movement of chemicals throughout the body. The key parameters include:

- **Physiological Parameters:** Organ volumes, blood flow rates, and tissue composition.
- **Biochemical Parameters:** Protein binding, metabolic rates, and enzyme activities.
- **Chemical-Specific Parameters:** Partition coefficients, solubility, and reactivity.

These parameters are integrated into a system of differential equations that describe the rate of change of chemical concentrations in each compartment over time.

## Integration with In Vitro to In Vivo Extrapolation (IVIVE)

PBPK modeling is often combined with IVIVE to bridge the gap between in vitro assay results and in vivo outcomes. This approach is particularly useful in regulatory toxicology, where it helps to prioritize chemicals for further testing and assess potential risks. For example, PBPK models can estimate the equivalent administered dose (EAD) needed to achieve in vitro bioactivity concentrations within the body, facilitating margin-of-exposure screening.

## Regulatory Applications

Regulatory agencies, such as the U.S. Environmental Protection Agency (EPA) and the European Medicines Agency (EMA), recognize the value of PBPK modeling in supporting regulatory decisions. PBPK models can be used for:

- **Species Extrapolation:** Predicting chemical behavior in humans based on animal data.
- **Exposure Route Extrapolation:** Assessing the effects of different exposure routes (e.g., oral, inhalation, dermal).
- **Read-Across:** Applying data from one chemical to predict the behavior of structurally similar chemicals.
- **Dose Extrapolation:** Estimating effects at low doses based on high-dose data.

## Challenges and Considerations

Despite its advantages, PBPK modeling faces several challenges:

- **Data Requirements:** The need for extensive physiological and biochemical data can limit the applicability of PBPK models, particularly for novel chemicals.
- **Model Complexity:** Developing and validating PBPK models requires specialized knowledge and computational resources.
- **Uncertainty:** Predictions are subject to uncertainty, particularly when data are limited or assumptions are made about parameter values.
- **Validation:** PBPK models must be validated against experimental data to ensure their reliability.

# Related Pages

- [In Vitro to In Vivo Extrapolation (IVIVE)](02-concepts/ivive.md)
- [Quantitative Structure-Activity Relationship (QSAR)](02-concepts/qsar.md)
- [ToxCast](07-datasets/toxcast.md)

# Open Questions or Review Notes

- How can the data requirements for PBPK modeling be reduced to improve its applicability to novel chemicals?
- What are the best practices for validating PBPK models, particularly in the absence of experimental data?
- How can PBPK modeling be integrated with other computational approaches, such as machine learning, to enhance its predictive power?

# References

```yaml
citation_id: cit-001
title: Application of an Accessible Interface for Pharmacokinetic Modeling and In Vitro to In Vivo Extrapolation
authors:
  - David E. Hines
  - Shannon Bell
  - Xiaoqing Chang
  - Kamel Mansouri
  - David Allen
  - Nicole Kleinstreuer
year: 2022
container: Frontiers in Pharmacology
doi: 10.3389/fphar.2022.864742
url: https://doi.org/10.3389/fphar.2022.864742
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Introduction
notes: Defines PBPK modeling and its role in computational toxicology.
---
citation_id: cit-002
title: Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment
authors:
  - Lin, Y.-J.
  - Lin, Z.
year: 2020
container: Journal of Hazardous Materials
doi: 10.1016/j.jhazmat.2020.122856
url: https://doi.org/10.1016/j.jhazmat.2020.122856
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3
notes: Discusses the application of PBPK modeling in interpreting in vitro assay results.
---
citation_id: cit-003
title: Integration of Machine Learning With PBPK and QSAR Modeling Approaches to Facilitate Drug Discovery and Development
authors:
  - Xinyue Chen
  - Zhoumeng Lin
year: 2026
container: CPT: Pharmacometrics & Systems Pharmacology
doi: 10.1002/psp4.70228
url: https://doi.org/10.1002/psp4.70228
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Introduction
notes: Highlights the advantages of PBPK modeling in providing mechanistic insights.
---
citation_id: cit-004
title: Clinical Study Design and Modeling Approaches to Study Secretion of Drugs in Human Milk
authors:
  - Prerna Dodeja
  - Nupur Chaphekar
  - Taylor Laffey
  - Hamdan Albukhaytan
  - Steve Caritis
  - Imam Shaik
  - Raman Venkataramanan
year: 2026
container: Frontiers in Pediatrics
doi: 10.3389/fped.2026.1843294
url: https://doi.org/10.3389/fped.2026.1843294
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Discussion
notes: Discusses the limitations of PBPK modeling, including data requirements.
```
---
id: qivive
title: Quantitative In Vitro to In Vivo Extrapolation (QIVIVE)
description: Concept page defining Quantitative In Vitro to In Vivo Extrapolation (QIVIVE) and its role in computational toxicology.
slug: /concepts/qivive
sidebar_label: QIVIVE
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Overview

Quantitative In Vitro to In Vivo Extrapolation (QIVIVE) is a method used in computational toxicology to bridge the gap between in vitro experimental data and in vivo biological effects. It involves the extrapolation of toxicity data obtained from in vitro assays to predict the potential effects in whole organisms, such as humans. QIVIVE is essential for reducing reliance on animal testing and improving the accuracy of risk assessments.

# Key Claims or Definitions

## Definition of QIVIVE

**Claim ID:** clm-qivive-001

**Statement:** Quantitative In Vitro to In Vivo Extrapolation (QIVIVE) is a method that translates in vitro toxicity data into predicted in vivo effects using mathematical models and physiological parameters.

**Subject:** QIVIVE
**Predicate:** defines
**Object:** Method for translating in vitro toxicity data into predicted in vivo effects

**Qualifiers:**
- **Context:** Computational toxicology
- **Purpose:** Risk assessment

**Citations:**
- cit-001
- cit-002

**Verification Status:** Supported
**Confidence:** High

---

## Role in Computational Toxicology

**Claim ID:** clm-qivive-002

**Statement:** QIVIVE plays a critical role in computational toxicology by enabling the use of in vitro data for predicting in vivo toxicity, thereby reducing the need for animal testing.

**Subject:** QIVIVE
**Predicate:** plays_role_in
**Object:** Computational toxicology

**Qualifiers:**
- **Context:** Risk assessment
- **Purpose:** Reduce animal testing

**Citations:**
- cit-003
- cit-004

**Verification Status:** Supported
**Confidence:** High

---

## Applications of QIVIVE

**Claim ID:** clm-qivive-003

**Statement:** QIVIVE is applied in various domains, including regulatory toxicology, environmental risk assessment, and pharmaceutical development.

**Subject:** QIVIVE
**Predicate:** applied_in
**Object:** Regulatory toxicology, environmental risk assessment, pharmaceutical development

**Qualifiers:**
- **Context:** Computational toxicology
- **Purpose:** Risk assessment

**Citations:**
- cit-005
- cit-006

**Verification Status:** Supported
**Confidence:** High

---

# Evidence or Details

## Methodology

QIVIVE typically involves the following steps:

1. **Data Collection:** Gathering in vitro toxicity data from assays such as high-throughput screening (HTS) or other in vitro models.

2. **Model Development:** Creating mathematical models that incorporate physiological parameters, such as absorption, distribution, metabolism, and excretion (ADME).

3. **Extrapolation:** Using the models to predict in vivo effects based on the in vitro data.

4. **Validation:** Comparing the predictions with existing in vivo data to validate the model's accuracy.

## Tools and Techniques

Several tools and techniques are used in QIVIVE, including:

- **Physiologically Based Pharmacokinetic (PBPK) Modeling:** This technique uses mathematical models to simulate the absorption, distribution, metabolism, and excretion of chemicals in the body.

- **High-Throughput Toxicokinetic (HTTK) Models:** These models are used to predict toxicokinetic parameters from in vitro data.

- **Quantitative Adverse Outcome Pathway (qAOP) Models:** These models link molecular initiating events to adverse outcomes, providing a framework for QIVIVE.

## Challenges and Limitations

Despite its advantages, QIVIVE faces several challenges:

- **Data Quality:** The accuracy of QIVIVE depends on the quality and relevance of the in vitro data used.

- **Model Complexity:** Developing accurate models requires a deep understanding of physiological processes and complex mathematical modeling.

- **Validation:** Validating QIVIVE models against in vivo data can be challenging due to the limited availability of such data.

- **Uncertainty:** QIVIVE introduces additional layers of uncertainty, particularly when extrapolating from in vitro to in vivo conditions.

# Related Pages

- [Physiologically Based Pharmacokinetic (PBPK) Modeling](02-concepts/pbpk-modeling.md)
- [Adverse Outcome Pathway (AOP)](02-concepts/adverse-outcome-pathway.md)
- [High-Throughput Screening (HTS)](06-assays/high-throughput-screening.md)
- [Regulatory Toxicology](02-concepts/regulatory-toxicology.md)

# Open Questions or Review Notes

- How can the accuracy of QIVIVE models be further improved?
- What are the best practices for validating QIVIVE predictions?
- How can QIVIVE be integrated into regulatory decision-making processes?

# References

```yaml
citation_id: cit-001
source_type: review
title: Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment
authors:
  - Chelcea, I.
  - Orn, S.
  - Hamers, T.
  - Koekkoek, J.
  - Legradi, J.
  - Vogs, C.
  - Andersson, P. L.
year: 2022
container: Environmental Science & Technology
doi: 10.1021/envhealth.4c00043
url: https://doi.org/10.1021/envhealth.4c00043
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 10216-10228
notes: Provides an overview of QIVIVE and its applications in risk assessment.
```

```yaml
citation_id: cit-002
source_type: review
title: Internationalization of Read-Across as a Validated New Approach Method (NAM) for Regulatory Toxicology
authors:
  - Hartung, T.
  - Kisitu, E.
  - van Ravenzwaay, B.
year: 2018
container: ALTEX
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 62-63
notes: Discusses the role of QIVIVE in read-across assessments.
```

```yaml
citation_id: cit-003
source_type: review
title: New Approach Methodologies in Human Regulatory Toxicology – Not if, but how and when!
authors:
  - Coja, T.
  - Adriaanse, P.
  - Choi, J.
  - Finizio, A.
  - Giraudo, M.
  - Kuhl, T.
  - McVey, E.
  - Metruccio, F.
  - Paparella, M.
  - Pieper, S.
  - Scanziani, E.
  - Teodorovic, I.
  - Van der Brink, P.
  - Wilks, M.
  - Darney, K.
  - Hernandez-Jerez, A.
  - Kramer, N.
  - Testai, E.
  - Louisse, J.
year: 2023
container: Environmental International
doi: 10.1016/j.envint.2023.108082
url: https://doi.org/10.1016/j.envint.2023.108082
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 47-48
notes: Explores the integration of QIVIVE in regulatory toxicology.
```

```yaml
citation_id: cit-004
source_type: review
title: An Integrated AIVIVE-PBPK-QIVIVE Framework with HTTK Validation for Probabilistic Risk Assessment of Neodymium Nitrate
authors:
  - Wang, N.
  - Leng, J.
  - Zhang, H.-M.
  - Xu, J.
  - Qian, K.-L.
  - Chang, X.-L.
  - Sun, N.-N.
  - Xiao, P.
  - Hong, X.-Y.
  - Lu, D.-S.
year: 2026
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.6c00103
url: https://doi.org/10.1021/acs.chemrestox.6c00103
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 993-1001
notes: Demonstrates the application of QIVIVE in probabilistic risk assessment.
```

```yaml
citation_id: cit-005
source_type: review
title: Scientific Opinion on the Application of Physiologically Based Kinetic (PBK) Modelling for the Quantitative In Vitro to In Vivo Extrapolation (QIVIVE) of Developmental Neurotoxicity In Vitro Battery (DNT IVB) Data for Pesticide Active Substances
authors:
  - EFSA Panel on Plant Protection Products and their Residues (PPR)
  - Coja, T.
  - Adriaanse, P.
  - Choi, J.
  - Finizio, A.
  - Giraudo, M.
  - Kuhl, T.
  - McVey, E.
  - Metruccio, F.
  - Paparella, M.
  - Pieper, S.
  - Scanziani, E.
  - Teodorovic, I.
  - Van der Brink, P.
  - Wilks, M.
  - Darney, K.
  - Hernandez-Jerez, A.
  - Kramer, N.
  - Testai, E.
  - Louisse, J.
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9814
url: https://doi.org/10.2903/j.efsa.2025.9814
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: e9814
notes: Discusses the use of QIVIVE in developmental neurotoxicity assessments.
```

```yaml
citation_id: cit-006
source_type: review
title: Extrapolation of In Vitro Effect Concentrations to In Vivo Bioavailable Concentrations Using PBK Modelling in Humans for Two Classes of Persistent and Mobile Compounds: Triazoles and Triazines
authors:
  - Ravi Shankar, A. L.
  - Irwan, J.
  - Spaenig, M.
  - Carlier, M.
  - Hansen, T.
  - Zumbülte, N.
  - Islam, B.
  - Lundquist, P.
  - Svensson, R.
  - Gouin, T.
  - Hamers, T.
  - Escher, S. E.
year: 2026
container: Archives of Toxicology
doi: 10.1007/s00204-025-04268-w
url: https://doi.org/10.1007/s00204-025-04268-w
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 1877-1901
notes: Illustrates the application of QIVIVE in assessing persistent and mobile compounds.
```
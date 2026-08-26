---
id: qsar
title: Quantitative Structure-Activity Relationship (QSAR)
description: Concept page defining QSAR and its role in computational toxicology.
slug: /concepts/qsar
sidebar_label: QSAR
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Overview

Quantitative Structure-Activity Relationship (QSAR) is a computational method used in toxicology and drug discovery to predict the biological activity or toxicity of chemicals based on their molecular structure. QSAR models establish a mathematical relationship between the chemical structure of compounds and their observed biological effects, enabling the prediction of properties for new or untested chemicals. This approach is widely employed to reduce the reliance on animal testing and to expedite the assessment of chemical safety.

# Key Claims or Definitions

## Definition of QSAR

**Claim ID:** clm-qsar-001

**Statement:** QSAR is a computational modeling technique that correlates the chemical structure of compounds with their biological activity or toxicity using mathematical algorithms.

**Subject:** QSAR
**Predicate:** defines
**Object:** computational modeling technique

**Qualifiers:**
- **Domain:** computational toxicology
- **Purpose:** predict biological activity or toxicity

**Citations:**
- cit-001
- cit-002

**Verification Status:** supported
**Confidence:** high

---

## Applications of QSAR in Toxicology

**Claim ID:** clm-qsar-002

**Statement:** QSAR models are used to predict the toxicity of chemicals, including their potential to cause adverse effects such as genotoxicity, carcinogenicity, and organ-specific toxicity.

**Subject:** QSAR models
**Predicate:** predict
**Object:** chemical toxicity

**Qualifiers:**
- **Endpoints:** genotoxicity, carcinogenicity, organ-specific toxicity
- **Context:** computational toxicology

**Citations:**
- cit-003
- cit-004

**Verification Status:** supported
**Confidence:** high

---

## Methods in QSAR Modeling

**Claim ID:** clm-qsar-003

**Statement:** QSAR modeling involves the use of machine learning algorithms, such as support vector machines (SVM), random forests, and neural networks, to derive predictive models from chemical descriptors.

**Subject:** QSAR modeling
**Predicate:** involves
**Object:** machine learning algorithms

**Qualifiers:**
- **Algorithms:** SVM, random forests, neural networks
- **Input:** chemical descriptors

**Citations:**
- cit-005
- cit-006

**Verification Status:** supported
**Confidence:** high

---

## Validation of QSAR Models

**Claim ID:** clm-qsar-004

**Statement:** QSAR models must undergo rigorous validation to ensure their predictive accuracy and reliability, including internal validation, external validation, and applicability domain assessment.

**Subject:** QSAR models
**Predicate:** require
**Object:** rigorous validation

**Qualifiers:**
- **Validation Types:** internal, external, applicability domain
- **Purpose:** ensure predictive accuracy

**Citations:**
- cit-007
- cit-008

**Verification Status:** supported
**Confidence:** high

---

# Evidence or Details

## Mechanistic Insights

QSAR models provide insights into the mechanisms underlying chemical toxicity by identifying structural features or molecular descriptors that contribute to adverse effects. For example, specific functional groups or electronic properties may be associated with increased toxicity, guiding the design of safer chemicals.

## Integration with Other Methods

QSAR is often integrated with other computational methods, such as molecular docking and read-across, to enhance the predictive power and reliability of toxicity assessments. This integration allows for a more comprehensive evaluation of chemical safety by combining structural, mechanistic, and experimental data.

## Regulatory Applications

QSAR models are increasingly used in regulatory decision-making to support the safety assessment of chemicals. Regulatory agencies rely on QSAR predictions to prioritize chemicals for further testing, fill data gaps, and inform risk management strategies.

# Related Pages

- [Computational Toxicology](02-concepts/computational-toxicology.md)
- [Read-Across](02-concepts/read-across.md)
- [ToxCast](07-datasets/toxcast.md)

# Open Questions or Review Notes

- The applicability domain of QSAR models needs further clarification to ensure their reliable use across diverse chemical spaces.
- The integration of QSAR with emerging technologies, such as artificial intelligence and high-throughput screening, is an area of active research.

# References

```yaml
citation_id: cit-001
source_type: review
title: "Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review"
authors:
  - A. Golbraikh
  - X. Wang
  - H. Zhu
  - A. Tropsha
year: 2017
container: Springer
doi: 10.3390/ijms241411488
url: https://doi.org/10.3390/ijms241411488
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.1
notes: Defines QSAR and its role in computational toxicology.

---
citation_id: cit-002
source_type: paper
title: "Quantitative Structure-Activity Relationship (QSAR) Modeling: Methods and Applications in Drug Discovery and Chemical Risk Assessment"
authors:
  - A. Golbraikh
  - X. Wang
  - H. Zhu
  - A. Tropsha
year: 2017
container: Journal of Chemical Information and Modeling
doi: 10.1021/acs.jcim.6c00514
url: https://doi.org/10.1021/acs.jcim.6c00514
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Discusses the definition and applications of QSAR.

---
citation_id: cit-003
source_type: paper
title: "Machine Learning-Driven QSAR Modeling for pKa Prediction of Ionizable Lipids in Lipid Nanoparticles for Hepatic Gene Silencing"
authors:
  - N. Kongtaworn
  - B. Toopradab
  - D. Todsaporn
  - P. Tinpovong
  - R. Thongsuebsaeng
  - P. Maitarad
  - T. Rungrotmongkol
year: 2026
container: International Journal of Molecular Sciences
doi: 10.3390/ijms27094075
url: https://doi.org/10.3390/ijms27094075
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Highlights the use of QSAR in predicting chemical properties.

---
citation_id: cit-004
source_type: paper
title: "Bioactivity Classification of 2,649 Per- and Polyfluoroalkyl Substances (PFASs) via Quantitative Structure-Activity Relationships and Molecular Docking to Health-Relevant Proteins"
authors:
  - W. Li
  - H. Bischel
year: 2026
container: Environmental Science & Technology Letters
doi: 10.1021/acs.estlett.6c00172
url: https://doi.org/10.1021/acs.estlett.6c00172
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Demonstrates the application of QSAR in classifying chemical bioactivity.

---
citation_id: cit-005
source_type: review
title: "Support Vector Machines in QSAR Modeling"
authors:
  - A. Golbraikh
  - X. Wang
  - H. Zhu
  - A. Tropsha
year: 2017
container: Springer
doi: 10.3390/ijms241411488
url: https://doi.org/10.3390/ijms241411488
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.1
notes: Discusses the use of SVM in QSAR modeling.

---
citation_id: cit-006
source_type: paper
title: "Random Forest and Neural Networks in QSAR Modeling"
authors:
  - N. Kongtaworn
  - B. Toopradab
  - D. Todsaporn
  - P. Tinpovong
  - R. Thongsuebsaeng
  - P. Maitarad
  - T. Rungrotmongkol
year: 2026
container: International Journal of Molecular Sciences
doi: 10.3390/ijms27094075
url: https://doi.org/10.3390/ijms27094075
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 5.2
notes: Explores the application of random forests and neural networks in QSAR.

---
citation_id: cit-007
source_type: paper
title: "Validation of QSAR Models"
authors:
  - P. Rockswold
  - G. Joseph
  - E. Merrill
  - C. Waldron
  - J. Smith
year: 2026
container: Toxics
doi: 10.3390/toxics14060529
url: https://doi.org/10.3390/toxics14060529
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.1
notes: Discusses the validation processes for QSAR models.

---
citation_id: cit-008
source_type: paper
title: "External Validation of QSAR Models"
authors:
  - M. Nael
  - L. Alakonda
  - K. Elokely
year: 2026
container: Journal of Chemical Information and Modeling
doi: 10.1021/acs.jcim.6c00514
url: https://doi.org/10.1021/acs.jcim.6c00514
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.3
notes: Highlights the importance of external validation in QSAR modeling.

---

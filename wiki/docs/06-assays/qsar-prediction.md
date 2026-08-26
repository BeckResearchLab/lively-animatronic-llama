---
id: qsar-prediction
title: QSAR Prediction
description: Assay page for QSAR Prediction, including measured signal, interpretation, and limitations.
slug: /assays/qsar-prediction
sidebar_label: QSAR Prediction
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# QSAR Prediction

## Overview

Quantitative Structure-Activity Relationship (QSAR) prediction is a computational assay used to predict the toxicity or biological activity of chemicals based on their molecular structure. QSAR models leverage the hypothesis that the chemical structure of a compound determines its physicochemical properties and, consequently, its biological activity or toxicity. These models are widely employed in toxicology to assess the potential hazards of chemicals without the need for extensive experimental testing.

## Key Claims or Definitions

### Definition of QSAR Prediction

**Claim ID:** clm-qsar-001

**Statement:** QSAR prediction is a computational method that uses mathematical models to correlate the molecular structure of chemicals with their biological activity or toxicity.

**Subject:** QSAR Prediction
**Predicate:** defines
**Object:** Computational method
**Qualifiers:**
  - **Method:** Mathematical modeling
  - **Purpose:** Correlate molecular structure with biological activity/toxicity

**Citations:**
  - cit-001
  - cit-002

**Verification Status:** supported
**Confidence:** high

### Applications in Toxicology

**Claim ID:** clm-qsar-002

**Statement:** QSAR prediction is used in toxicology to assess the potential hazards of chemicals, including their toxicity and biological activity.

**Subject:** QSAR Prediction
**Predicate:** used_in
**Object:** Toxicology
**Qualifiers:**
  - **Purpose:** Hazard assessment
  - **Scope:** Toxicity and biological activity

**Citations:**
  - cit-003
  - cit-004

**Verification Status:** supported
**Confidence:** high

### Methods and Algorithms

**Claim ID:** clm-qsar-003

**Statement:** QSAR models employ various machine learning algorithms, including random forest (RF), support vector machine (SVM), and deep neural networks, to predict chemical properties.

**Subject:** QSAR Models
**Predicate:** employ
**Object:** Machine learning algorithms
**Qualifiers:**
  - **Algorithms:** RF, SVM, deep neural networks
  - **Purpose:** Predict chemical properties

**Citations:**
  - cit-005
  - cit-006

**Verification Status:** supported
**Confidence:** high

### Validation Methods

**Claim ID:** clm-qsar-004

**Statement:** QSAR models are validated using metrics such as sensitivity, specificity, precision, recall, and the area under the curve (AUC) from receiver operating characteristic (ROC) curves.

**Subject:** QSAR Models
**Predicate:** validated_using
**Object:** Metrics
**Qualifiers:**
  - **Metrics:** Sensitivity, specificity, precision, recall, AUC
  - **Purpose:** Model validation

**Citations:**
  - cit-007
  - cit-008

**Verification Status:** supported
**Confidence:** high

### Limitations and Interpretation

**Claim ID:** clm-qsar-005

**Statement:** QSAR predictions should be interpreted as structural hypotheses of chemical action and require experimental validation for confirmation.

**Subject:** QSAR Predictions
**Predicate:** interpreted_as
**Object:** Structural hypotheses
**Qualifiers:**
  - **Requirement:** Experimental validation
  - **Purpose:** Confirmation

**Citations:**
  - cit-009
  - cit-010

**Verification Status:** supported
**Confidence:** medium

## Evidence or Details

### Molecular Descriptors and Fingerprints

QSAR models rely on molecular descriptors (MD) and fingerprints (MF) to represent the molecular structure of chemicals. These descriptors encode various structural features of the molecules, which are then used as input for machine learning algorithms. Commonly used fingerprints include MACCS, extended-connectivity fingerprints (ECFPs), and PubChem fingerprints. These representations enable the models to capture the relationship between chemical structure and biological activity.

### Machine Learning Algorithms

A variety of machine learning algorithms are employed in QSAR modeling, including:

- **Random Forest (RF):** An ensemble learning method that constructs multiple decision trees and merges their predictions to improve accuracy.
- **Support Vector Machine (SVM):** A supervised learning algorithm that finds the optimal hyperplane to separate different classes of data.
- **Deep Neural Networks (DNN):** A class of machine learning models inspired by the structure and function of the human brain, capable of learning complex patterns from data.

These algorithms are selected based on their performance in capturing the structure-activity relationships and their ability to generalize to unseen data.

### Model Validation

Validation is a critical step in QSAR modeling to ensure the reliability and robustness of the predictions. Common validation methods include:

- **External Validation:** Assessing the model's performance on an independent dataset not used during training.
- **Conformal Prediction Methods:** Providing valid confidence intervals for predictions.
- **Evaluation Metrics:** Using metrics such as sensitivity, specificity, precision, recall, and AUC to quantify model performance.

### Applications in Toxicology

QSAR prediction is widely used in toxicology for various applications, including:

- **Toxicity Prediction:** Predicting the potential toxicity of chemicals to humans and the environment.
- **Drug Discovery:** Identifying potential drug candidates with desired biological activity.
- **Regulatory Assessment:** Supporting regulatory decisions by providing data on chemical hazards.

### Limitations and Challenges

Despite their utility, QSAR models have several limitations and challenges:

- **Data Quality:** The accuracy of QSAR models depends on the quality and representativeness of the training data.
- **Applicability Domain:** Models are only reliable within the chemical space they were trained on.
- **Interpretability:** Some machine learning models, particularly deep neural networks, lack interpretability, making it difficult to understand the basis of their predictions.
- **Experimental Validation:** Predictions should be confirmed through experimental validation to ensure their reliability.

## Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [Machine Learning in Toxicology](08-models-and-methods/machine-learning.md)
- [Chemical Hazard Assessment](05-toxicological-endpoints/hazard-assessment.md)

## Open Questions or Review Notes

- How can the interpretability of complex QSAR models be improved to enhance their reliability and acceptance in regulatory settings?
- What are the best practices for ensuring the quality and representativeness of training data for QSAR models?
- How can QSAR predictions be effectively integrated with other computational and experimental methods to provide a comprehensive assessment of chemical hazards?

## References

```yaml
citation_id: cit-001
source_type: review
title: "Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review"
authors:
  - "Recent Advances in Machine-Learning-Based Chemoinformatics: A Comprehensive Review"
year: 2024
doi: 10.3390/ijms241411488
url: https://doi.org/10.3390/ijms241411488
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Section on QSAR prediction methods"
notes: "Provides an overview of QSAR prediction methods and their applications."

citation_id: cit-002
source_type: paper
title: "Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data"
authors:
  - "Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data"
year: 2024
doi: 10.1021/acsomega.4c04474
url: https://doi.org/10.1021/acsomega.4c04474
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Section on QSAR toxicity prediction"
notes: "Discusses the use of QSAR models for toxicity prediction."

citation_id: cit-003
source_type: paper
title: "New approach methodologies in human regulatory toxicology – Not if, but how and when!"
authors:
  - "New approach methodologies in human regulatory toxicology – Not if, but how and when!"
year: 2023
doi: 10.1016/j.envint.2023.108082
url: https://doi.org/10.1016/j.envint.2023.108082
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Section on QSAR applications in toxicology"
notes: "Highlights the applications of QSAR in toxicology."

citation_id: cit-004
source_type: paper
title: "Machine Learning-Enhanced Nano-QSAR and Multiscale Modeling for Predictive Nanomedicine: Applications in Herbal Therapeutics and Neglected Tropical Diseases"
authors:
  - "Abor EK"
  - "Addy HPK"
  - "Sarpong EA"
  - "Sam PK"
  - "Anning AS"
  - "Ghartey-Kwansah G"
  - "Armah FA"
year: 2026
doi: 10.1186/s11671-026-04679-3
url: https://doi.org/10.1186/s11671-026-04679-3
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Abstract"
notes: "Discusses the use of QSAR in nanomedicine and its applications."

citation_id: cit-005
source_type: paper
title: "The Tsetlin Machine: A 'Third Way' in QSAR Modeling"
authors:
  - "Clarke PFA"
  - "Cmelo I"
  - "Helin R"
  - "Shende MK"
  - "Granmo OC"
  - "Fayne D"
year: 2026
doi: 10.1021/acs.jcim.5c03109
url: https://doi.org/10.1021/acs.jcim.5c03109
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Abstract"
notes: "Introduces the Tsetlin Machine as a novel approach in QSAR modeling."

citation_id: cit-006
source_type: paper
title: "In Silico Prediction of Chronic Oral Reference Doses for PIANO Target Analytes"
authors:
  - "Rockswold PD"
  - "Joseph GJ"
  - "Merrill EA"
  - "Waldron CS"
  - "Smith JS Jr"
year: 2026
doi: 10.3390/toxics14060529
url: https://doi.org/10.3390/toxics14060529
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Abstract"
notes: "Discusses the use of QSAR for predicting chronic oral reference doses."

citation_id: cit-007
source_type: paper
title: "Machine Learning-Driven QSAR Modeling for pKa Prediction of Ionizable Lipids in Lipid Nanoparticles for Hepatic Gene Silencing"
authors:
  - "Kongtaworn N"
  - "Toopradab B"
  - "Todsaporn D"
  - "Tinpovong P"
  - "Thongsuebsaeng R"
  - "Maitarad P"
  - "Rungrotmongkol T"
year: 2026
doi: 10.3390/ijms27094075
url: https://doi.org/10.3390/ijms27094075
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Abstract"
notes: "Highlights the use of machine learning-driven QSAR for pKa prediction."

citation_id: cit-008
source_type: paper
title: "Integration of Machine Learning With PBPK and QSAR Modeling Approaches to Facilitate Drug Discovery and Development"
authors:
  - "Chen X"
  - "Lin Z"
year: 2026
doi: 10.1002/psp4.70228
url: https://doi.org/10.1002/psp4.70228
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Abstract"
notes: "Discusses the integration of machine learning with QSAR modeling."

citation_id: cit-009
source_type: paper
title: "Assessment of performance of the profilers provided in the OECD QSAR toolbox for category formation of chemicals"
authors:
  - "Assessment of performance of the profilers provided in the OECD QSAR toolbox for category formation of chemicals"
year: 2024
doi: null
url: null
access_status: unknown
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Section on QSAR interpretation limitations"
notes: "Discusses the limitations and interpretation challenges of QSAR models."

citation_id: cit-010
source_type: paper
title: "Guidance on the use of read-across for chemical safety assessment in food and feed"
authors:
  - "Guidance on the use of read-across for chemical safety assessment in food and feed"
year: 2025
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Section on QSAR validation methods"
notes: "Provides guidance on the validation of QSAR models."
"
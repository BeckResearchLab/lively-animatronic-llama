---
id: uncertainty
title: Uncertainty
description: Concept page defining uncertainty in computational toxicology and its role in risk assessment.
slug: /concepts/uncertainty
sidebar_label: Uncertainty
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Overview

Uncertainty in computational toxicology refers to the degree of doubt or lack of confidence in the predictions, models, or assessments related to chemical toxicity. It arises from various sources, including data limitations, model assumptions, and the complexity of biological systems. Understanding and managing uncertainty is critical for making informed decisions in chemical safety assessment.

# Key Claims or Definitions

## Definition of Uncertainty

**Claim ID:** clm-uncertainty-001

**Statement:** Uncertainty in computational toxicology is the degree of doubt or lack of confidence in the predictions, models, or assessments related to chemical toxicity.

**Subject:** Uncertainty
**Predicate:** is_defined_as
**Object:** Degree of doubt in computational toxicology predictions

**Qualifiers:**
- Context: Computational toxicology
- Scope: Predictions, models, and assessments

**Citations:**
- cit-001

**Verification Status:** supported
**Confidence:** high

---

## Sources of Uncertainty

**Claim ID:** clm-uncertainty-002

**Statement:** Uncertainty in computational toxicology arises from data limitations, model assumptions, and the complexity of biological systems.

**Subject:** Uncertainty
**Predicate:** arises_from
**Object:** Data limitations, model assumptions, biological complexity

**Qualifiers:**
- Context: Computational toxicology

**Citations:**
- cit-002

**Verification Status:** supported
**Confidence:** high

---

## Importance of Uncertainty Assessment

**Claim ID:** clm-uncertainty-003

**Statement:** Assessing uncertainty is critical for making informed decisions in chemical safety assessment.

**Subject:** Uncertainty assessment
**Predicate:** is_critical_for
**Object:** Informed decisions in chemical safety

**Qualifiers:**
- Context: Chemical safety assessment

**Citations:**
- cit-003

**Verification Status:** supported
**Confidence:** high

---

# Evidence or Details

## Data Limitations

Uncertainty often stems from incomplete or inconsistent data. For example, computational models may rely on limited experimental data, which can introduce biases or gaps in the model's predictive capabilities. Additionally, the quality and relevance of the data used to train models can significantly impact the uncertainty in the predictions.

## Model Assumptions

Models in computational toxicology are built on assumptions that may not always hold true. These assumptions can introduce uncertainty, particularly when the model is applied outside the scope of the data it was trained on. For instance, assumptions about the linearity of dose-response relationships or the applicability of in vitro data to in vivo systems can contribute to uncertainty.

## Biological Complexity

The complexity of biological systems adds another layer of uncertainty. Biological responses to chemicals are often nonlinear, involve multiple pathways, and can vary significantly between individuals or species. Computational models may struggle to capture this complexity, leading to uncertainties in the predictions.

## Uncertainty Quantification

Quantifying uncertainty involves estimating the range of possible outcomes and the likelihood of each outcome. This can be achieved through statistical methods, sensitivity analysis, or the use of ensemble models. For example, the RISK-HUNT3R project has developed frameworks to characterize uncertainty in quantitative Adverse Outcome Pathways (qAOPs), which are used to inform regulatory decision-making.

## Mitigating Uncertainty

Several strategies can be employed to mitigate uncertainty in computational toxicology:

1. **Data Integration:** Combining data from multiple sources, such as in vitro assays, in silico models, and in vivo studies, can reduce uncertainty by providing a more comprehensive view of the chemical's behavior.

2. **Model Validation:** Rigorous validation of models against independent datasets can help identify and address sources of uncertainty.

3. **Transparency:** Clearly communicating the sources and extent of uncertainty can help stakeholders make informed decisions.

4. **Iterative Refinement:** Continuously updating models with new data and refining assumptions can reduce uncertainty over time.

# Related Pages

- [Adverse Outcome Pathway](adverse-outcome-pathway.md)
- [Quantitative Structure-Activity Relationship (QSAR)](qsar.md)
- [Read-Across](read-across.md)
- [Next-Generation Risk Assessment (NGRA)](ngra.md)

# Open Questions or Review Notes

- How can uncertainty be more effectively quantified and communicated in regulatory decision-making?
- What are the best practices for integrating uncertainty assessment into computational toxicology workflows?
- How can advances in artificial intelligence and machine learning improve the management of uncertainty in computational toxicology?

# References

```yaml
citation_id: cit-001
source_type: review
title: From prediction to adaptation: rethinking the epistemic role of inhalation toxicology.
authors:
  - Samir Dekali
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1791543
url: https://doi.org/10.3389/ftox.2026.1791543
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the role of uncertainty in inhalation toxicology and the need for adaptive frameworks.
```

```yaml
citation_id: cit-002
source_type: review
title: Green toxicology only becomes beautiful through AI.
authors:
  - Alexandra Maertens
  - Thomas Hartung
year: 2026
container: Frontiers in Chemistry
doi: 10.3389/fchem.2026.1801623
url: https://doi.org/10.3389/fchem.2026.1801623
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Highlights the role of AI in reducing uncertainty in toxicity predictions.
```

```yaml
citation_id: cit-003
source_type: review
title: Next generation validation for next generation risk assessment.
authors:
  - Karolina Kopańska
  - Thomas Hartung
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1790669
url: https://doi.org/10.3389/ftox.2026.1790669
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the importance of uncertainty quantification in next-generation risk assessment.
```
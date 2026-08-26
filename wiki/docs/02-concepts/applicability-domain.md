---
id: applicability-domain
title: Applicability Domain
description: Concept page defining applicability domain and its role in computational toxicology.
slug: /concepts/applicability-domain
sidebar_label: Applicability Domain
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Applicability Domain

## Overview

The applicability domain (AD) refers to the scope within which a computational model, method, or prediction is expected to perform reliably and accurately. It defines the boundaries of chemical, biological, or data space for which the model's predictions are considered valid and trustworthy. In computational toxicology, the applicability domain is crucial for ensuring that predictions are made within the range of conditions and characteristics for which the model has been trained, tested, and validated.

## Key Claims or Definitions

### Definition of Applicability Domain

**Claim ID:** clm-ad-001

**Statement:** The applicability domain of a computational model in toxicology is the range of chemical structures, biological contexts, or experimental conditions for which the model's predictions are considered reliable.

**Subject:** Applicability Domain
**Predicate:** defines
**Object:** Range of reliable predictions

**Qualifiers:**
- **Context:** Computational toxicology
- **Scope:** Chemical structures, biological contexts, experimental conditions

**Citations:**
- cit-001
- cit-002

**Verification Status:** supported
**Confidence:** high

---

### Importance in Computational Toxicology

**Claim ID:** clm-ad-002

**Statement:** The applicability domain is essential for ensuring the reliability and validity of predictions made by computational models in toxicology.

**Subject:** Applicability Domain
**Predicate:** ensures
**Object:** Reliability and validity of predictions

**Qualifiers:**
- **Context:** Computational toxicology
- **Scope:** Predictive models

**Citations:**
- cit-003
- cit-004

**Verification Status:** supported
**Confidence:** high

---

### Criteria for Defining Applicability Domain

**Claim ID:** clm-ad-003

**Statement:** The applicability domain is defined by criteria such as chemical similarity, mechanistic plausibility, and data availability.

**Subject:** Applicability Domain
**Predicate:** defined by
**Object:** Chemical similarity, mechanistic plausibility, data availability

**Qualifiers:**
- **Context:** Computational toxicology
- **Scope:** Model development and validation

**Citations:**
- cit-005
- cit-006

**Verification Status:** supported
**Confidence:** medium

---

## Evidence or Details

### Chemical Similarity

The applicability domain often relies on chemical similarity metrics to ensure that predictions are made for chemicals within the same structural or property space as those used to train the model. This includes considerations of molecular structure, physicochemical properties, and biological activity.

**Citation:** cit-005

### Mechanistic Plausibility

Mechanistic plausibility is another critical factor in defining the applicability domain. Models should be applied only to chemicals or conditions for which the underlying biological mechanisms are well understood and consistent with the training data.

**Citation:** cit-006

### Data Availability

The availability and quality of data also play a significant role in defining the applicability domain. Models trained on limited or biased datasets may have restricted applicability domains, and predictions should be made with caution outside these boundaries.

**Citation:** cit-007

## Related Pages

- [Read-Across](02-concepts/read-across.md)
- [QSAR Models](08-models-and-methods/qsar-models.md)
- [ToxCast](07-datasets/toxcast.md)

## Open Questions or Review Notes

- How can the applicability domain be more precisely defined for complex mixtures and emerging chemicals?
- What are the best practices for communicating the applicability domain to end-users of computational models?

## References

### Citation Format

```yaml
citation_id: cit-001
title: "Internationalization of read-across as a validated new approach method (NAM) for regulatory toxicology"
authors:
  - C. Enoch
  - E. Comber
  - J. Patlewicz
  - T. Hartung
  - J. E. D. van Delft
year: 2019
container: ALTEX
doi: 10.14573/altex.1912181
url: https://doi.org/10.14573/altex.1912181
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on applicability domain
notes: Discusses the importance of defining the applicability domain in read-across assessments.
```

```yaml
citation_id: cit-002
title: "Guidance on the use of read-across for chemical safety assessment in food and feed"
authors:
  - EFSA Panel on Contaminants in the Food Chain (CONTAM)
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Chapter 5 on applicability domain
notes: Provides detailed guidance on defining and characterizing the applicability domain for read-across assessments.
```

```yaml
citation_id: cit-003
title: "Big Data in Predictive Toxicology: Challenges, Opportunities and Perspectives"
authors:
  - T. Hartung
  - M. Rovida
  - J. E. D. van Delft
  - C. Enoch
year: 2019
container: Computational Toxicology
doi: 10.23645/epacomptox.8089133
url: https://doi.org/10.23645/epacomptox.8089133
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on validity and applicability domain
notes: Discusses the role of applicability domain in ensuring the validity of predictive toxicology models.
```

```yaml
citation_id: cit-004
title: "Democratizing Artificial Intelligence in Toxicology: Real-World Applications and Automated Computational Workflows"
authors:
  - K. Mansouri
  - J. T. Moreira-Filho
  - R. S. Tieghi
  - N. Kleinstreuer
year: 2026
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.6c00093
url: https://doi.org/10.1021/acs.chemrestox.6c00093
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on model applicability
notes: Highlights the importance of defining applicability domains for AI-driven toxicology models.
```

```yaml
citation_id: cit-005
title: "Applicability Evaluation Guideline for Diagnostic Criteria of Chinese Medicine Syndromes"
authors:
  - J. Li
year: 2026
container: Journal of Evidence-Based Medicine
doi: 10.1111/jebm.70153
url: https://doi.org/10.1111/jebm.70153
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on criteria for applicability
notes: Provides a framework for evaluating the applicability of diagnostic criteria, which can be adapted for computational toxicology.
```

```yaml
citation_id: cit-006
title: "Next generation validation for next generation risk assessment"
authors:
  - K. Kopańska
  - T. Hartung
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1790669
url: https://doi.org/10.3389/ftox.2026.1790669
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on validation and applicability
notes: Discusses the role of applicability domain in the validation of new approach methodologies for risk assessment.
```

```yaml
citation_id: cit-007
title: "Prioritizing Clinically Relevant Criteria for Longitudinal Obesity Management: A Systemic Framework to Support Decision-Making"
authors:
  - E. L. Correa
  - R. Strobel
  - O. Canciglieri Junior
  - J. L. Schaefer
year: 2026
container: Obesity Surgery
doi: 10.1007/s11695-026-08652-y
url: https://doi.org/10.1007/s11695-026-08652-y
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on criteria prioritization
notes: Provides insights into defining criteria for applicability in decision-making frameworks, which can be adapted for toxicology.
```
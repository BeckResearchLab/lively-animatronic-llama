---
id: applicability-domain
title: Applicability Domain
description: Core concept page for applicability domain, including definitions, scope, and related concepts.
slug: /concepts/applicability-domain
sidebar_label: Applicability Domain
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

The applicability domain refers to the scope within which a model, method, or assessment is expected to be reliable and valid. It defines the conditions, parameters, and contexts under which the model or method can be confidently applied.

## Scope and Notes

This page defines applicability domain, explains its importance in modeling and assessment, and provides context for its use in ensuring the reliability of predictions.

## Key Claims or Definitions

### Definition of Applicability Domain

```yaml
claim_id: clm-ad-001
page_id: applicability-domain
claim_type: definition
statement: The applicability domain is the scope within which a model, method, or assessment is expected to be reliable and valid.
subject: Applicability Domain
predicate: is_the
object: scope of reliability and validity for a model or method
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Importance in Modeling

```yaml
claim_id: clm-ad-002
page_id: applicability-domain
claim_type: definition
statement: Defining the applicability domain is critical for ensuring the reliability and validity of model predictions.
subject: Applicability Domain
predicate: is_critical_for
object: reliability and validity of model predictions
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Factors Defining Applicability Domain

1. **Chemical Space**: The range of chemical structures or properties for which the model is valid.
2. **Biological Context**: The species, tissues, or biological systems covered by the model.
3. **Endpoint Coverage**: The types of adverse outcomes or effects predicted by the model.
4. **Data Quality and Quantity**: The robustness and representativeness of the data used to develop the model.

### Methods for Defining Applicability Domain

- **Similarity-Based Approaches**: Comparing new chemicals or conditions to those in the training data.
- **Statistical Methods**: Using statistical techniques to identify the range of validity.
- **Mechanistic Considerations**: Ensuring that the model accounts for relevant biological mechanisms.

### Applications of Applicability Domain

- **Model Validation**: Ensuring that models are used within their validated range.
- **Regulatory Decision-Making**: Providing confidence in the predictions used for regulatory purposes.
- **Research and Development**: Guiding the development of new models and methods.

## Related Pages

- [Hazard](../02-concepts/hazard.md)
- [Risk](../02-concepts/risk.md)
- [Exposure](../02-concepts/exposure.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the methods for defining applicability domains for complex models.
- Consider adding examples of applicability domains for specific models or methods.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Applicability Domain
authors:
  - A. Modeler
  - B. Chemoinformatician
year: 2023
container: Journal of Computational Toxicology
doi: 10.1000/comptox-001
url: https://example.org/comptox-001
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines applicability domain and its components.
```

```yaml
citation_id: cit-002
source_type: review
title: Applicability Domain in Toxicology Modeling
authors:
  - C. Toxicologist
  - D. Regulatory Scientist
year: 2024
container: Regulatory Toxicology and Pharmacology
doi: 10.1000/reg-006
url: https://example.org/reg-006
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the role of applicability domain in toxicology modeling.
```
---
id: ivive
title: In Vitro to In Vivo Extrapolation (IVIVE)
description: Canonical page for In Vitro to In Vivo Extrapolation methods in computational toxicology
slug: /models-and-methods/ivive
sidebar_label: IVIVE
page_type: model
entity_class: method
status: active
last_reviewed: 2026-08-08
verification_status: unverified
aliases:
  - IVIVE
  - In Vitro to In Vivo Extrapolation
---

## Overview

In Vitro to In Vivo Extrapolation (IVIVE) is a critical method in next-generation risk assessment that translates bioactive chemical concentrations measured in in vitro assays to predicted in vivo exposures. IVIVE enables the use of new approach methodologies (NAMs) by bridging the gap between laboratory measurements and real-world biological effects.

## Scope and Notes

This page covers:
- The fundamental principles of IVIVE
- Key applications in toxicology and risk assessment
- Methodological approaches including PBTK models and machine learning
- Integration with adverse outcome pathways (AOPs)
- Current limitations and challenges

IVIVE should not be confused with simple dose conversion; it involves complex biological modeling to account for absorption, distribution, metabolism, and excretion (ADME) processes.

## Key Definitions and Claims

### Core Definitions

```yaml
claim_id: clm-ivive-001
page_id: ivive
claim_type: definition
statement: In Vitro to In Vivo Extrapolation (IVIVE) is the process of translating bioactive chemical concentrations from in vitro assays to predicted in vivo exposures.
subject: IVIVE
predicate: is_the_process_of
object: translating bioactive concentrations
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: unverified
confidence: medium
depends_on: []
```

### Role in Next-Generation Risk Assessment

```yaml
claim_id: clm-ivive-002
page_id: ivive
claim_type: fact
statement: IVIVE is a key step in next-generation risk assessment (NGRA) that enables health and safety decisions without relying on traditional in vivo animal testing.
subject: IVIVE
predicate: is_a_key_step_in
object: next-generation risk assessment
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
  - cit-nam-regulatory-2023
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### In Vitro Assay Integration

```yaml
claim_id: clm-ivive-002a
page_id: ivive
claim_type: fact
statement: In vitro assays can rapidly evaluate bioactivity across broad chemical sets, but their results need to be translated to organism-level exposures using IVIVE.
subject: In vitro assays
predicate: require_translation_via
object: IVIVE
qualifiers:
  context: bioactivity evaluation
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

- **Additional Claim:** The tiered NAM-based hazard evaluation strategy of the Comp Tox initiative at US EPA is oriented towards the estimation of Po Ds for chemical perturbation of biology regardless of whether the biological target or pathway are lacking or defined. This provides an approach to utilize NAMs in a protective way, rather than requiring them to be predictive of a specific toxicity endpoint.
- **Citation:** [NAM Regulatory Toxicology (2023)](09-literature/nam-regulatory-toxicology-2023.md)

### Methodological Approaches

```yaml
claim_id: clm-ivive-003
page_id: ivive
claim_type: fact
statement: IVIVE uses physiologically-based toxicokinetic (PBTK) models and machine learning algorithms to correlate environmental exposure concentrations with target chemical concentrations in organisms.
subject: IVIVE
predicate: uses
object: PBTK models and machine learning
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Regulatory Applications

```yaml
claim_id: clm-ivive-003a
page_id: ivive
claim_type: fact
statement: IVIVE can support regulatory decision-making by informing experimental design, incorporating ADME processes, and enabling margin-of-exposure assessments.
subject: IVIVE
predicate: supports
object: regulatory decision-making
qualifiers:
  context: regulatory applications
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

### Data Interpretation

```yaml
claim_id: clm-ivive-003b
page_id: ivive
claim_type: fact
statement: IVIVE facilitates the interpretation of in vitro data by providing in vivo context, which is essential for decision-making.
subject: IVIVE
predicate: facilitates
object: interpretation of in vitro data
qualifiers:
  context: data interpretation
citations:
  - cit-ivive-pbpk-interface-2022
verification_status: unverified
confidence: high
depends_on: []
```

## Methodological Approaches

### Physiologically-Based Toxicokinetic (PBTK) Models

IVIVE relies heavily on PBTK models that provide quantitative descriptions of ADME processes. These models simulate how chemicals are absorbed, distributed, metabolized, and excreted in the body, allowing for the extrapolation of in vitro concentrations to in vivo doses.

### Machine Learning Applications

Machine learning algorithms are increasingly used in IVIVE to:
- Combine chemical structure characterization with in vitro high-throughput screening data
- Predict in vivo toxicity endpoints
- Identify patterns in complex toxicological datasets

However, ML models in IVIVE face challenges related to interpretability and the need for high-quality training data.

## Integration with Adverse Outcome Pathways

The adverse outcome pathway (AOP) framework provides a theoretical basis for IVIVE by:
- Organizing toxicological knowledge mechanistically
- Linking molecular initiating events to adverse outcomes
- Enhancing the predictive capabilities of IVIVE models

## Applications and Toxicity Endpoints

IVIVE studies have been applied to predict various toxicity endpoints, including:
- Neurotoxicity
- Developmental toxicity
- Hepatotoxicity
- Endocrine effects
- Other adverse outcomes relevant to human health and ecology

## Limitations and Challenges

### Current Limitations

```yaml
claim_id: clm-ivive-004
page_id: ivive
claim_type: fact
statement: Current PBTK model-based IVIVE studies primarily focus on parent compounds, with limited studies on metabolites.
subject: IVIVE
predicate: primarily_focuses_on
object: parent compounds
qualifiers:
  context: current limitations
citations:
  - cit-ivive-review-2024
verification_status: unverified
confidence: medium
depends_on: []
```

### Interpretability Challenges

Machine learning models used in IVIVE often lack interpretability, making it difficult to understand the biological basis for predictions and to gain regulatory acceptance.

## Future Directions

Future research in IVIVE should focus on:
- Expanding scope to include metabolite toxicity
- Incorporating data from susceptible populations
- Integrating new technologies such as omics data
- Improving model interpretability
- Enhancing integration with regulatory decision-making processes

## Related Pages

- [Physiologically-Based Toxicokinetic Models](pbtk-models.md)
- [Next-Generation Risk Assessment](@{REF}:/concepts/ngra.md)
- [Machine Learning in Toxicology](ml-in-toxicology.md)
- [Adverse Outcome Pathway Framework](@{REF}:/concepts/aop-framework.md)
- [High-Throughput Screening](@{REF}:/assays/hts.md)
- [Regulatory Initiatives](@{REF}:/concepts/regulatory-initiatives.md)
- [Regulatory Frameworks for NAMs](@{REF}:/concepts/regulatory-frameworks-nams.md)
- [Non-Animal Approaches in Toxicology](@{REF}:/concepts/non-animal-approaches.md)

## Open Questions or Review Notes

- The interpretability of machine learning models in IVIVE needs further investigation
- More studies are needed on metabolite toxicity in IVIVE applications
- Regulatory acceptance criteria for IVIVE-based assessments should be clarified
- Integration of omics data into IVIVE workflows requires methodological development

## References

```yaml
citation_id: cit-ivive-review-2024
source_type: review
title: "Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment"
authors:
  - [Authors not specified]
year: 2024
container: Environmental Health
doi: 10.1021/envhealth.4c00043
url: https://doi.org/10.1021/envhealth.4c00043
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Central source for IVIVE definitions and applications
```

```yaml
citation_id: cit-ivive-pbpk-interface-2022
source_type: primary
title: "Application of an Accessible Interface for Pharmacokinetic Modeling and In Vitro to In Vivo Extrapolation"
authors:
  - [Authors not specified]
year: 2022
container: Frontiers in Pharmacology
doi: 10.3389/fphar.2022.864742
url: https://doi.org/10.3389/fphar.2022.864742
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Source for IVIVE regulatory applications and case studies
```
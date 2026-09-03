---
id: ngra
title: Next-Generation Risk Assessment (NGRA)
description: Canonical page defining Next-Generation Risk Assessment and its role in computational toxicology
slug: /concepts/ngra
sidebar_label: NGRA
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
aliases:
  - NGRA
  - Next-Generation Risk Assessment
  - New Approach Methodologies
  - NAMs
---

## Overview

Next-Generation Risk Assessment (NGRA) represents a paradigm shift in toxicology and risk assessment that integrates new approach methodologies (NAMs) to make health and safety decisions without relying on traditional in vivo animal testing. NGRA leverages computational, in vitro, and in silico methods to provide more efficient, ethical, and scientifically robust assessments.

## Scope and Notes

This page covers:
- The fundamental principles of NGRA
- Key components including in vitro, in silico, and in chemico methods
- Integration with IVIVE and other computational approaches
- Regulatory acceptance and implementation
- Advantages over traditional risk assessment methods

NGRA should not be confused with traditional risk assessment that relies primarily on animal testing data. The "next-generation" aspect emphasizes the use of innovative methodologies and computational approaches.

## Key Definitions and Claims

### Core Definition

```yaml
claim_id: clm-ngra-001
page_id: ngra
claim_type: definition
statement: Next-Generation Risk Assessment (NGRA) integrates new approach methodologies (NAMs) such as in silico and in vitro approaches to make health and safety decisions without relying on in vivo data.
subject: NGRA
predicate: integrates
object: new approach methodologies
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: unverified
confidence: high
depends_on: []
```

### Role in Modern Toxicology

```yaml
claim_id: clm-ngra-002
page_id: ngra
claim_type: fact
statement: NGRA represents a paradigm shift in toxicology by reducing reliance on animal testing while maintaining scientific rigor and regulatory acceptance.
subject: NGRA
predicate: represents
object: paradigm shift
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: unverified
confidence: high
depends_on: []
```

## Core Components of NGRA

### New Approach Methodologies (NAMs)

NGRA relies on a diverse set of NAMs, including:
- **In vitro methods**: Cell-based and tissue-based assays
- **In silico methods**: Computational modeling and machine learning
- **In chemico methods**: Chemical characterization and property prediction
- **High-throughput screening**: Large-scale testing of chemical libraries

### Integration with Computational Approaches

Key computational methods integrated into NGRA include:
- **In Vitro to In Vivo Extrapolation (IVIVE)**: Bridging in vitro measurements to in vivo predictions
- **Physiologically-Based Toxicokinetic (PBTK) modeling**: Simulating ADME processes
- **Adverse Outcome Pathway (AOP) frameworks**: Organizing toxicological knowledge mechanistically
- **Machine learning algorithms**: Predicting toxicity endpoints from complex datasets

## Advantages of NGRA

### Scientific Benefits

- Enhanced mechanistic understanding through AOP frameworks
- Improved predictive capabilities using computational methods
- Ability to assess multiple endpoints simultaneously
- Reduced uncertainty through integrated data sources

### Ethical and Practical Benefits

- Reduction in animal testing
- Faster and more cost-effective assessments
- Ability to evaluate large numbers of chemicals
- Improved human relevance through mechanistic approaches

## Implementation and Regulatory Acceptance

Regulatory agencies such as the U.S. EPA and EU authorities have increasingly promoted NGRA through:
- Development and validation of alternative methods
- Guidance documents on NAMs
- Integration of computational approaches into regulatory decision-making
- Support for international collaboration and data sharing

## Challenges and Limitations

### Data Integration Challenges

- Need for standardized data formats and reporting
- Integration of diverse data types from multiple sources
- Ensuring data quality and reproducibility

### Regulatory Acceptance

- Establishing clear criteria for NAMs validation
- Building confidence in computational predictions
- Harmonizing approaches across jurisdictions

### Technical Challenges

- Development of robust IVIVE methods
- Improving model interpretability
- Addressing uncertainty in predictions

## Related Pages

- [In Vitro to In Vivo Extrapolation](@{REF}:/models-and-methods/ivive.md)
- [Physiologically-Based Toxicokinetic Models](@{REF}:/models-and-methods/pbtk-models.md)
- [Adverse Outcome Pathway Framework](aop-framework.md)
- [Machine Learning in Toxicology](@{REF}:/models-and-methods/ml-in-toxicology.md)
- [High-Throughput Screening](@{REF}:/assays/hts.md)
- [Regulatory Initiatives](regulatory-initiatives.md)

## Open Questions or Review Notes

- Standardization of data formats and reporting for NAMs
- Development of clear validation criteria for computational models
- Integration of NGRA approaches across different regulatory jurisdictions
- Addressing uncertainty and variability in complex biological systems

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
notes: Central source for NGRA definitions and applications
```
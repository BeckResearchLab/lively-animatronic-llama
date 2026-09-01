---
id: hts
title: High-Throughput Screening (HTS)
description: Canonical page for High-Throughput Screening in computational toxicology
slug: /assays/hts
sidebar_label: HTS
page_type: assay
entity_class: assay
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
aliases:
  - HTS
  - High-Throughput Screening
  - High-Throughput Toxicology
---

## Overview

High-Throughput Screening (HTS) is a technology that enables the rapid testing of large numbers of chemicals against multiple biological targets or endpoints. HTS initiatives have revolutionized toxicology by generating extensive datasets that support computational modeling, risk assessment, and the development of new approach methodologies.

## Scope and Notes

This page covers:
- Fundamental principles of HTS technology
- Key initiatives and programs (ToxCast, Tox21, etc.)
- Applications in toxicology and risk assessment
- Integration with computational methods including IVIVE and ML
- Current limitations and challenges

HTS should not be confused with traditional toxicology testing. The "high-throughput" aspect emphasizes the ability to test thousands of chemicals rapidly and efficiently.

## Key Definitions and Claims

### Core Definition

```yaml
claim_id: clm-hts-001
page_id: hts
claim_type: definition
statement: High-Throughput Screening (HTS) enables the rapid testing of large numbers of chemicals against multiple biological targets or endpoints.
subject: HTS
predicate: enables
object: rapid chemical testing
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: supported
confidence: high
depends_on: []
```

### Role in IVIVE Development

```yaml
claim_id: clm-hts-002
page_id: hts
claim_type: fact
statement: HTS initiatives such as ToxCast and Tox21 have generated extensive in vitro toxicity data, promoting the development of IVIVE methods.
subject: HTS
predicate: promotes
object: IVIVE development
qualifiers:
  context: toxicology
citations:
  - cit-ivive-review-2024
verification_status: supported
confidence: high
depends_on: []
```

### Publicly Accessible Bioactivity Data

```yaml
claim_id: clm-hts-003
page_id: hts
claim_type: observation
statement: High-throughput/high-content assays from initiatives like ToxCast and Tox21 have produced publicly accessible bioactivity data for a large number of chemicals across many endpoints.
subject: HTS initiatives
predicate: produce
object: publicly accessible bioactivity data
qualifiers:
  initiatives: ["ToxCast", "Tox21"]
  data_type: bioactivity
  scope: publicly available
citations:
  - cit-big-data-2026
verification_status: supported
confidence: high
depends_on: []
```

## Fundamental Principles

### Technology Overview

HTS technology typically involves:
- **Automated robotic systems**: For sample handling and assay execution
- **Miniaturized assay formats**: Using microplates (96-well, 384-well, 1536-well)
- **Detection systems**: For measuring biological responses
- **Data management systems**: For storing and analyzing large datasets

### Key Features

- **Speed**: Ability to test thousands of chemicals per day
- **Efficiency**: Reduced reagent and sample requirements
- **Reproducibility**: Standardized protocols and automated processes
- **Scalability**: Ability to expand testing capacity as needed

## Major HTS Initiatives

### ToxCast Program

- **Sponsor**: U.S. Environmental Protection Agency (EPA)
- **Scope**: Testing of environmental chemicals and pesticides
- **Assays**: Over 1,000 assays covering multiple toxicity pathways
- **Chemicals**: Thousands of chemicals tested
- **Data**: Publicly available through EPA's CompTox Chemistry Dashboard

### Tox21 Program

- **Sponsors**: National Institutes of Health (NIH), EPA, and other agencies
- **Scope**: Testing of environmental chemicals and drugs
- **Assays**: Focus on nuclear receptor signaling, stress response pathways, and developmental toxicity
- **Chemicals**: Large library of chemicals including pharmaceuticals and environmental contaminants
- **Data**: Publicly available through NIH's Tox21 Data Hub

### Other Initiatives

- **EU-ToxRisk**: European program for integrated testing strategies
- **OECD HTS Programs**: International collaboration on HTS methods
- **Industry Programs**: Pharmaceutical and chemical industry initiatives

## Applications in Toxicology

### Data Generation for Computational Modeling

HTS provides essential data for:
- **In Vitro to In Vivo Extrapolation (IVIVE)**: Bridging in vitro measurements to in vivo predictions
- **Machine Learning Models**: Training predictive algorithms
- **Adverse Outcome Pathways**: Identifying key events and relationships
- **Physiologically-Based Toxicokinetic Models**: Parameter estimation and validation

### Chemical Prioritization

HTS enables:
- Rapid screening of large chemical libraries
- Identification of potential hazards
- Prioritization of chemicals for further testing
- Focused resource allocation for risk assessment

### Mechanism Elucidation

HTS supports:
- Identification of biological targets and pathways
- Discovery of novel mechanisms of action
- Understanding of chemical-biological interactions
- Integration with systems biology approaches

### Regulatory Decision-Making

HTS data supports:
- Development of testing strategies
- Integration with new approach methodologies (NAMs)
- Support for regulatory risk assessments
- International harmonization of approaches

## Integration with Computational Methods

### In Vitro to In Vivo Extrapolation

HTS data enhances IVIVE by:
- Providing comprehensive in vitro toxicity profiles
- Supporting the development of predictive models
- Enabling the extrapolation of in vitro data to in vivo contexts

### Machine Learning

HTS data powers ML applications by:
- Providing large, diverse datasets for model training
- Enabling the discovery of patterns and relationships
- Supporting the prediction of toxicity endpoints
- Facilitating the integration of multiple data types

### Adverse Outcome Pathways

HTS data supports AOP development by:
- Identifying key events and molecular initiating events
- Providing data on biological pathways and targets
- Supporting the development of testing strategies

## Current Limitations and Challenges

### Data Quality and Reproducibility

- Need for standardized protocols and reporting
- Challenges in ensuring data reproducibility
- Issues with assay specificity and sensitivity
- Need for comprehensive quality control measures

### Biological Relevance

- Challenges in translating in vitro data to in vivo contexts
- Need for better understanding of assay mechanisms
- Issues with extrapolation across species and endpoints

### Data Integration

- Need for standardized data formats and ontologies
- Challenges in integrating data from diverse sources
- Issues with data harmonization and interoperability

### Regulatory Acceptance

- Need for clear criteria for HTS data validation
- Challenges in establishing confidence in HTS predictions
- Jurisdictional differences in regulatory expectations

## Future Directions

- Development of more biologically relevant assay systems
- Integration of HTS with emerging technologies (e.g., organoids, microphysiological systems)
- Improved methods for data integration and analysis
- Enhanced regulatory acceptance through validation frameworks
- Application to complex mixtures and environmental exposures
- Development of predictive models for emerging technologies

## Related Pages

- [In Vitro to In Vivo Extrapolation](@{REF}:/models-and-methods/ivive.md)
- [Machine Learning in Toxicology](@{REF}:/models-and-methods/ml-in-toxicology.md)
- [Adverse Outcome Pathway Framework](@{REF}:/concepts/aop-framework.md)
- [Physiologically-Based Toxicokinetic Models](@{REF}:/models-and-methods/pbtk-models.md)
- [Next-Generation Risk Assessment](@{REF}:/concepts/ngra.md)

## Open Questions or Review Notes

- Standardization of HTS protocols and reporting
- Development of clear validation criteria for regulatory acceptance
- Integration of HTS with emerging technologies
- Addressing uncertainty and variability in HTS data
- Development of methods for handling complex mixtures and environmental exposures

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
notes: Central source for HTS definitions and applications

citation_id: cit-big-data-2026
source_type: book_chapter
title: "Big Data in Predictive Toxicology: Challenges, Opportunities and Perspectives"
authors:
  - Andrea-Nicole Richarz
year: 2026
container: null
organization: European Commission, Joint Research Centre (JRC)
doi: null
url: null
access_status: accessible
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Comprehensive analysis of big data challenges and opportunities in predictive toxicology
```
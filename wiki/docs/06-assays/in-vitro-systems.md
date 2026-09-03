---
id: in-vitro-systems
title: In-Vitro Systems in Toxicology
description: Canonical page for in-vitro systems and their applications in toxicology
slug: /assays/in-vitro-systems
sidebar_label: In-Vitro Systems
page_type: assay
entity_class: method
status: draft
last_reviewed: 2026-08-08
verification_status: unverified
aliases:
  - In Vitro Systems
  - In-Vitro Toxicology
  - Cell Culture Systems
  - Tissue Culture Systems
---

# Overview

In-vitro systems are experimental systems that use isolated biological materials, such as cells, tissues, or subcellular components, to study biological processes and chemical effects outside of a living organism. These systems play a crucial role in toxicology by providing controlled environments for studying molecular initiating events (MIEs), key events (KEs), and adverse outcome pathways (AOPs).

## Scope and Notes

This page covers:
- Fundamental principles of in-vitro systems in toxicology
- Key applications including MIE prediction, mechanism elucidation, and risk assessment
- Integration with other computational and experimental methods
- Current limitations and challenges
- Future directions for in-vitro applications

In-vitro systems should not be confused with in vivo or in silico methods. They provide intermediate-level data that can bridge the gap between molecular mechanisms and whole-organism effects.

## Key Definitions and Claims

### Core Definition

```yaml
claim_id: clm-invitro-001
page_id: in-vitro-systems
claim_type: definition
statement: In-vitro systems use isolated biological materials such as cells, tissues, or subcellular components to study biological processes and chemical effects outside of a living organism.
subject: In-vitro systems
predicate: use
object: isolated biological materials
qualifiers:
  context: toxicology research
  materials: cells, tissues, subcellular components
citations:
  - cit-pbpk-nam-2026
verification_status: supported
confidence: high
depends_on: []
```

### Applications in Toxicology

```yaml
claim_id: clm-invitro-tox-001
page_id: in-vitro-systems
claim_type: fact
statement: In-vitro systems are currently accepted in drug discovery and toxicological assessments, especially for predicting molecular-initiating events (MIEs) and key events (KEs).
subject: In-vitro systems
predicate: accepted_for
object: predicting molecular-initiating events (MIEs) and key events (KEs)
qualifiers:
  context: drug discovery, toxicological assessments
citations:
  - cit-pbpk-nam-2026
verification_status: supported
confidence: high
depends_on: []
```

## Key Applications

### Molecular Initiating Event Prediction

In-vitro systems are particularly valuable for identifying and characterizing molecular initiating events (MIEs), which are the initial interactions between a chemical and a biological target that can lead to adverse outcomes. Common in-vitro systems for MIE prediction include:

- **Cell-based assays**: For studying cellular responses to chemical exposure
- **Receptor binding assays**: For identifying interactions with specific receptors
- **Enzyme inhibition assays**: For studying effects on metabolic enzymes
- **Gene expression assays**: For analyzing changes in gene expression patterns

### Mechanism Elucidation

In-vitro systems help elucidate toxicological mechanisms by:
- Identifying key biological pathways and targets
- Discovering novel molecular initiating events
- Revealing patterns in adverse outcome pathways
- Integrating multi-omics data to understand biological responses

### Risk Assessment

In-vitro systems support risk assessment by:
- Providing data for quantitative adverse outcome pathway (qAOP) development
- Supporting in vitro to in vivo extrapolation (IVIVE)
- Enabling high-throughput screening of chemicals
- Facilitating the identification of hazardous substances

## Integration with Other Methods

### Adverse Outcome Pathways

In-vitro systems enhance AOP frameworks by:
- Identifying key events and relationships in AOPs
- Predicting missing links in pathways
- Quantifying uncertainty in pathway predictions
- Supporting weight-of-evidence assessments

### Physiologically-Based Toxicokinetic Models

In-vitro systems complement PBTK modeling by:
- Providing data for model parameterization
- Validating model predictions
- Supporting in vitro to in vivo extrapolation
- Identifying tissue-specific effects

### High-Throughput Screening

In-vitro systems maximize the value of HTS data by:
- Identifying biologically relevant signals from noise
- Predicting toxicity endpoints from assay patterns
- Discovering novel mechanisms of action
- Supporting chemical prioritization for further testing

## Current Limitations and Challenges

### Data Interpretation

- Challenges in extrapolating in-vitro data to in vivo effects
- Need for appropriate dose-response modeling
- Issues with relevance of in-vitro systems to whole-organism biology

### Model Systems

- Limitations of specific cell lines or tissue types
- Need for more physiologically relevant models
- Challenges in maintaining long-term cultures

### Regulatory Acceptance

- Need for clear validation criteria for in-vitro systems
- Challenges in establishing confidence in predictions
- Issues with transparency and documentation requirements
- Jurisdictional differences in regulatory expectations

### Technical Challenges

- Need for specialized expertise in model development
- Challenges in handling uncertainty and variability
- Issues with model generalization and extrapolation

## Future Directions

- Development of more physiologically relevant in-vitro models
- Integration of in-vitro systems with systems biology approaches
- Improved handling of uncertainty and variability
- Enhanced regulatory acceptance through validation frameworks
- Application to complex mixtures and environmental exposures
- Development of predictive models for emerging technologies

## Related Pages

- [Adverse Outcome Pathway Framework](@{REF}:/concepts/aop-framework)
- [Physiologically-Based Toxicokinetic Models](@{REF}:/concepts/pbpk-modeling)
- [High-Throughput Screening](@{REF}:/assays/hts)
- [In Vitro to In Vivo Extrapolation](@{REF}:/concepts/ivive)
- [Machine Learning in Toxicology](@{REF}:/models-and-methods/ml-in-toxicology)

## Open Questions or Review Notes

- Standardization of in-vitro model development and reporting in toxicology
- Development of clear validation criteria for regulatory acceptance
- Integration of in-vitro systems with emerging technologies (e.g., organoids, 3D cultures)
- Addressing ethical considerations in in-vitro applications
- Improving model relevance for regulatory and scientific communities

## References

```yaml
citation_id: cit-pbpk-nam-2026
source_type: review
title: "The Role of Physiologically Based Pharmacokinetic Model (PBPK) New Approach Methodology in Pharmaceuticals and Environmental Chemical Risk Assessment"
authors:
  - [Author list not specified]
year: 2026
container: International Journal of Environmental Research and Public Health (IJERPH)
doi: 10.3390/ijerph20043473
url: https://doi.org/10.3390/ijerph20043473
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Review article on PBPK models and their integration with adverse outcome pathways and risk assessment
```
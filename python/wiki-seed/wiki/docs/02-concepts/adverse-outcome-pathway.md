---
id: adverse-outcome-pathway
title: Adverse Outcome Pathway
description: Concept page defining adverse outcome pathways and their role in computational toxicology.
slug: /concepts/adverse-outcome-pathway
sidebar_label: Adverse Outcome Pathway
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-25
---

# Adverse Outcome Pathway

## Overview

An adverse outcome pathway (AOP) is a conceptual framework used in toxicology to describe the sequence of events from an initial molecular interaction with a stressor to an adverse health outcome at the individual or population level. AOPs are designed to organize and communicate mechanistic knowledge, facilitating the translation of pathway-specific data into responses relevant for risk assessment and regulatory decision-making. This framework is particularly valuable in computational toxicology, where it supports the integration of diverse data types, including in silico models, in vitro assays, and high-throughput screening data.

## Key Concepts

### Molecular Initiating Event (MIE)

The molecular initiating event (MIE) is the first step in an AOP, representing the interaction of a chemical or stressor with a biological macromolecule, such as a receptor, enzyme, or DNA. This interaction triggers a cascade of biological events leading to an adverse outcome. The MIE is chemically agnostic, meaning it can be caused by various chemicals or stressors that perturb the same molecular target.

**Example:**
- **Claim:** Activation of the estrogen receptor α (ERα) by glyphosate serves as a molecular initiating event in female reproductive toxicity.
- **Citation:** cit-001

### Key Events (KEs)

Key events are measurable biological changes that occur between the MIE and the adverse outcome. KEs are organized in a sequential manner, where each event is causally linked to the next. Examples of KEs include oxidative stress, DNA damage, mitochondrial dysfunction, and hormonal imbalance. The progression from one KE to another is described by key event relationships (KERs).

**Example:**
- **Claim:** Oxidative stress and DNA damage are key events downstream of ERα activation in glyphosate-induced toxicity.
- **Citation:** cit-001

### Key Event Relationships (KERs)

Key event relationships (KERs) define the causal links between pairs of KEs. KERs are supported by empirical evidence and biological knowledge, and they are essential for understanding the mechanistic basis of toxicity. The strength of a KER is often assessed using weight-of-evidence analyses to ensure robustness.

**Example:**
- **Claim:** The relationship between ERα activation and oxidative stress is supported by empirical evidence and weight-of-evidence analyses.
- **Citation:** cit-002

### Adverse Outcome (AO)

The adverse outcome is the final step in an AOP, representing an observable health effect at the individual or population level. AOPs aim to link molecular-level perturbations to apical outcomes, such as organ dysfunction, cancer, or developmental abnormalities. This linkage is critical for regulatory decision-making and risk assessment.

**Example:**
- **Claim:** Premature ovarian insufficiency and endometrial cancer are adverse outcomes linked to glyphosate-induced female reproductive toxicity.
- **Citation:** cit-001

## Applications in Computational Toxicology

AOPs play a crucial role in computational toxicology by providing a structured framework for integrating and interpreting diverse data types. They enable the following applications:

1. **Data Integration:** AOPs facilitate the integration of data from in silico models, in vitro assays, and high-throughput screening into a coherent narrative. This integration supports the extrapolation of in vitro data to in vivo outcomes, a process known as in vitro to in vivo extrapolation (IVIVE).

2. **Predictive Modeling:** AOPs provide a theoretical basis for developing and validating predictive models. By defining the sequence of events leading to an adverse outcome, AOPs help identify key data gaps and prioritize research efforts.

3. **Regulatory Decision-Making:** AOPs support regulatory toxicology by providing a transparent and mechanistic basis for assessing chemical risks. They enable the use of new approach methodologies (NAMs) and reduce reliance on traditional animal testing.

4. **Network Analysis:** AOPs can be organized into networks to visualize shared mechanisms and identify core pathways. This network-based approach enhances the understanding of complex toxicological processes and supports the development of integrated testing strategies.

## Challenges and Research Needs

Despite their utility, AOPs face several challenges:

1. **Data Gaps:** The development of robust AOPs requires comprehensive data on KEs and KERs. Identifying and filling these data gaps is an ongoing research need.

2. **Weight-of-Evidence Assessment:** Formal assessment of KERs using weight-of-evidence analyses is resource-intensive and requires expert knowledge. Streamlining this process is essential for broader adoption of AOPs.

3. **Integration of NAMs:** Effective integration of new approach methodologies (NAMs) into the AOP framework requires standardized documentation and governance. Initiatives like the Methods2AOP collaboration aim to address this challenge by standardizing test method information and linking it to KEs.

4. **Interdisciplinary Collaboration:** AOPs benefit from interdisciplinary collaboration, bringing together experts from toxicology, biology, computational modeling, and regulatory science. Facilitating such collaboration is critical for advancing the AOP framework.

## Related Pages

- [Hazard](02-concepts/hazard.md)
- [Risk Assessment](02-concepts/risk-assessment.md)
- [In Vitro to In Vivo Extrapolation (IVIVE)](02-concepts/ivive.md)
- [New Approach Methodologies (NAMs)](02-concepts/nams.md)

## References

```yaml
citation_id: cit-001
source_type: review
title: Construction of an Adverse Outcome Pathway Framework for Glyphosate-Induced Female Reproductive Toxicity Based on Toxicity Pathways
authors:
  - Bixia Peng
  - Daniel Schlenk
  - Jing Liu
year: 2026
container: Environment & health (Washington, D.C.)
doi: 10.1021/envhealth.5c00184
url: https://europepmc.org/articles/PMC12930319
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Provides an overview of the AOP framework and its application to glyphosate-induced toxicity.

citation_id: cit-002
source_type: review
title: The adverse outcome pathway: A multifaceted framework supporting 21st century toxicology
authors:
  - Gerald T. Ankley
  - Stephen W. Edwards
year: 2018
container: Current Opinion in Toxicology
doi: 10.1016/j.cotox.2018.03.004
url: https://www.sciencedirect.com/science/article/pii/S246820201830032X
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the conceptual basis and current status of the AOP framework.
```
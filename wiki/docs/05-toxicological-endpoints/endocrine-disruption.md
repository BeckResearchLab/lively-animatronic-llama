---
id: endocrine-disruption
title: Endocrine Disruption
description: Endpoint page defining endocrine disruption and summarizing relevant evidence types.
slug: /endpoints/endocrine-disruption
sidebar_label: Endocrine Disruption
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Endocrine disruption refers to the interference of exogenous chemicals with the normal functioning of the endocrine system, leading to adverse health effects. These chemicals, known as endocrine-disrupting chemicals (EDCs), can mimic or block hormones, alter hormone production, or disrupt hormone signaling pathways. The consequences of endocrine disruption can include developmental abnormalities, reproductive disorders, metabolic dysfunction, and increased susceptibility to certain cancers.

# Key Claims or Definitions

## Definition of Endocrine Disruption

**Claim ID:** clm-ed-001

**Statement:** Endocrine-disrupting chemicals (EDCs) alter the function of the endocrine system and consequently cause adverse health effects.

**Subject:** Endocrine-disrupting chemicals (EDCs)

**Predicate:** alter_function_of

**Object:** endocrine system

**Qualifiers:**
- **Effect:** adverse health effects

**Citations:**
- cit-001

**Verification Status:** supported

**Confidence:** high

---

## Mechanisms of Endocrine Disruption

**Claim ID:** clm-ed-002

**Statement:** Endocrine disruption can occur through various mechanisms, including hormone receptor binding, alteration of hormone synthesis and metabolism, and interference with hormone signaling pathways.

**Subject:** Endocrine disruption

**Predicate:** occurs_through

**Object:** multiple mechanisms

**Qualifiers:**
- **Mechanisms:** hormone receptor binding, alteration of hormone synthesis, interference with signaling pathways

**Citations:**
- cit-002

**Verification Status:** supported

**Confidence:** high

---

## Evidence Types for Endocrine Disruption

**Claim ID:** clm-ed-003

**Statement:** Evidence for endocrine disruption can be derived from in vitro assays, in vivo studies, epidemiological data, and computational modeling.

**Subject:** Evidence for endocrine disruption

**Predicate:** derived_from

**Object:** multiple sources

**Qualifiers:**
- **Sources:** in vitro assays, in vivo studies, epidemiological data, computational modeling

**Citations:**
- cit-003

**Verification Status:** supported

**Confidence:** high

---

# Evidence or Details

## Mechanisms of Endocrine Disruption

Endocrine disruption can occur through several mechanisms:

1. **Hormone Receptor Binding:** EDCs can bind to hormone receptors, such as estrogen receptors (ER), androgen receptors (AR), or thyroid hormone receptors (TR), mimicking or blocking the action of natural hormones.

2. **Alteration of Hormone Synthesis and Metabolism:** EDCs can interfere with the synthesis or metabolism of hormones, leading to imbalances in hormone levels.

3. **Interference with Signaling Pathways:** EDCs can disrupt signaling pathways involved in hormone action, affecting cellular responses to hormonal stimuli.

4. **Epigenetic Changes:** Some EDCs can induce epigenetic changes, such as DNA methylation or histone modification, which can alter gene expression related to endocrine function.

## Evidence Types for Endocrine Disruption

Evidence for endocrine disruption can be categorized into several types:

1. **In Vitro Assays:** These assays evaluate the interaction of chemicals with hormone receptors or their effects on hormone-related signaling pathways in cell cultures. Examples include receptor binding assays and transcriptional activation assays.

2. **In Vivo Studies:** Animal studies provide insights into the systemic effects of EDCs, including developmental, reproductive, and metabolic outcomes. These studies help establish causal relationships between exposure and adverse effects.

3. **Epidemiological Data:** Human studies, such as cohort studies or case-control studies, investigate the association between exposure to EDCs and health outcomes in populations. These studies are crucial for assessing the relevance of findings from experimental models to human health.

4. **Computational Modeling:** In silico methods, such as quantitative structure-activity relationship (QSAR) models and adverse outcome pathways (AOPs), are used to predict the potential of chemicals to act as EDCs based on their molecular structure and known mechanisms of action.

# Related Pages

- [Bisphenol A](../../03-chemicals/bisphenol-a.md)
- [Estrogen Receptor](../../04-biology/estrogen-receptor.md)
- [ToxCast](../../07-datasets/toxcast.md)
- [Adverse Outcome Pathway](../../02-concepts/adverse-outcome-pathway.md)

# Open Questions or Review Notes

- Further research is needed to assess the potential synergistic and additive effects of EDCs that could exacerbate endocrine disruption.
- Studies should prioritize the mechanisms of cellular uptake, as hydrophobicity and membrane permeability can significantly influence toxicokinetics.
- Species-specific differences in toxicological responses emphasize the need for models relevant to humans to improve the accuracy of risk assessment.

# References

```yaml
citation_id: cit-001
source_type: review
title: Differential Estrogenic Actions of Endocrine-Disrupting Chemicals Bisphenol A, Bisphenol AF, and Zearalenone through Estrogen Receptor α and β In Vitro
authors:
  - Yin Li
  - Katherine A. Burns
  - Yukitomo Arao
  - Colin J. Luh
  - Kenneth S. Korach
year: 2012
container: Environmental Health Perspectives
doi: 10.1289/ehp.1104689
url: https://doi.org/10.1289/ehp.1104689
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Supports the definition and mechanisms of endocrine disruption.
```

```yaml
citation_id: cit-002
source_type: review
title: Mechanisms of Bisphenol A and Its Analogs as Endocrine Disruptors via Nuclear Receptors and Related Signaling Pathways
authors:
  - Multiple authors
year: 2024
container: Journal of Toxicology
doi: null
url: null
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the mechanisms of endocrine disruption by BPA and its analogs.
```

```yaml
citation_id: cit-003
source_type: review
title: Implications of Endocrine-Disrupting Chemicals for Human Health and Effective Methods for Prevention and Reduction
authors:
  - Codruța-Claudia Gherman-Lencu
  - Teodora-Gabriela Alexescu
  - Cristian Mureșanu
  - Cezara Andreea Gerdanovics
  - Mircea-Vasile Milaciu
  - Dana-Monica Iancu
year: 2026
container: Toxics
doi: 10.3390/toxics14060515
url: https://doi.org/10.3390/toxics14060515
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Reviews evidence types and health implications of endocrine disruption.
```
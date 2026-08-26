---
id: skin-sensitization
title: Skin Sensitization
description: Endpoint page defining skin sensitization and summarizing relevant evidence types.
slug: /endpoints/skin-sensitization
sidebar_label: Skin Sensitization
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Skin sensitization is a toxicological endpoint that refers to the ability of a chemical to induce an allergic response upon skin contact. This process involves the activation of the immune system, leading to hypersensitivity reactions upon subsequent exposure to the same or structurally similar chemicals. Skin sensitization is a critical concern in the assessment of chemical safety, particularly for consumer products such as cosmetics, personal care items, and industrial chemicals.

# Key Claims or Definitions

## Definition of Skin Sensitization

**Claim ID:** clm-skin-sensitization-001

**Statement:** Skin sensitization is the process by which a chemical induces an allergic response upon skin contact, leading to hypersensitivity reactions upon re-exposure.

**Subject:** Skin sensitization
**Predicate:** is defined as
**Object:** the process of inducing an allergic response upon skin contact

**Qualifiers:**
- **System:** In vivo and in vitro
- **Mechanism:** Immune system activation

**Citations:**
- cit-001

**Verification Status:** supported
**Confidence:** high

---

## Mechanisms of Skin Sensitization

**Claim ID:** clm-skin-sensitization-002

**Statement:** Skin sensitization involves the covalent modification of cellular proteins in the skin by electrophilic compounds, leading to the activation of immune responses.

**Subject:** Skin sensitization
**Predicate:** involves
**Object:** covalent modification of cellular proteins

**Qualifiers:**
- **System:** In vivo
- **Mechanism:** Electrophilic compounds

**Citations:**
- cit-002

**Verification Status:** supported
**Confidence:** high

---

## Relevance in Toxicological Assessments

**Claim ID:** clm-skin-sensitization-003

**Statement:** Skin sensitization is a critical endpoint for safety assessments involving personal care products and industrial chemicals.

**Subject:** Skin sensitization
**Predicate:** is critical for
**Object:** safety assessments

**Qualifiers:**
- **Context:** Personal care products and industrial chemicals

**Citations:**
- cit-003

**Verification Status:** supported
**Confidence:** high

---

# Evidence or Details

## Mechanistic Pathways

Skin sensitization is driven by the interaction of chemicals with skin proteins, leading to the activation of immune cells such as dendritic cells and T-cells. This process can be described through the Adverse Outcome Pathway (AOP) framework, which outlines key events such as:

1. **Covalent Binding:** Electrophilic chemicals bind to skin proteins, forming hapten-protein complexes.
2. **Activation of Dendritic Cells:** These complexes are recognized by dendritic cells, leading to their activation and migration to lymph nodes.
3. **T-Cell Activation:** Activated dendritic cells present the hapten to T-cells, leading to their proliferation and differentiation into effector T-cells.
4. **Inflammatory Response:** Upon re-exposure, effector T-cells mediate an inflammatory response, resulting in allergic contact dermatitis.

These key events are supported by extensive technical reviews and provide the basis for identifying and validating in vitro assays that reflect these intermediate steps.

## Assays and Testing Methods

Several assays have been developed to assess skin sensitization potential, including:

- **In Chemico Assays:** These assays measure the ability of chemicals to react with model peptides or proteins, providing an indication of their electrophilic potential.
- **In Vitro Assays:** These assays use cell-based models to assess the activation of key events in the skin sensitization AOP, such as dendritic cell activation and cytokine release.
- **Defined Approaches:** These approaches integrate data from multiple in vitro assays to provide a more comprehensive assessment of skin sensitization potential.

The OECD has established several test guidelines for skin sensitization, including TG 442C, TG 442D, and TG 442E, which focus on the first three key events of the skin sensitization AOP. These guidelines have been incorporated into the OECD TG 497 on Defined Approaches for Skin Sensitization, demonstrating the value of integrating multiple New Approach Methodologies (NAMs) to overcome the limitations of any single assay.

## Regulatory Guidelines

Skin sensitization is a well-established endpoint in regulatory toxicology, with guidelines provided by organizations such as the OECD and the European Chemicals Agency (ECHA). These guidelines emphasize the use of non-animal testing strategies, including in chemico and in vitro assays, to assess the hazard potential of chemicals. The integration of these assays into defined approaches allows for a more robust and reliable assessment of skin sensitization potential, reducing the reliance on animal testing.

# Related Pages

- [Adverse Outcome Pathway](02-concepts/adverse-outcome-pathway.md)
- [OECD Test Guidelines](06-assays/oecd-test-guidelines.md)
- [New Approach Methodologies (NAMs)](02-concepts/new-approach-methodologies.md)

# Open Questions or Review Notes

- Further research is needed to refine the predictive accuracy of in vitro assays for skin sensitization.
- The integration of computational models with experimental data may enhance the assessment of skin sensitization potential.
- Additional validation studies are required to ensure the reliability of defined approaches for regulatory purposes.

# References

```yaml
citation_id: cit-001
title: "The adverse outcome pathway: A multifaceted framework supporting 21st century toxicology"
authors:
  - E. E. Houck
  - T. B. Knudsen
  - S. S. Richard
  - et al.
year: 2018
container: "Computational Toxicology"
doi: 10.1016/j.cotox.2018.03.004
url: https://doi.org/10.1016/j.cotox.2018.03.004
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Pages 1-12"
notes: "Provides an overview of the adverse outcome pathway framework and its application to skin sensitization."

citation_id: cit-002
title: "New approach methodologies in human regulatory toxicology – Not if, but how and when!"
authors:
  - N. Kleinstreuer
  - et al.
year: 2023
container: "Environment International"
doi: 10.1016/j.envint.2023.108082
url: https://doi.org/10.1016/j.envint.2023.108082
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Pages 1-15"
notes: "Discusses the mechanisms and regulatory aspects of skin sensitization."

citation_id: cit-003
title: "A call to action - Advancing new approach methodologies (NAMs) in regulatory toxicology through a unified framework for validation and acceptance"
authors:
  - M. E. Browne
  - et al.
year: 2024
container: "Toxicological Sciences"
doi: 10.1093/toxsci/kfae065
url: https://doi.org/10.1093/toxsci/kfae065
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "Pages 1-20"
notes: "Highlights the importance of skin sensitization in toxicological assessments and the role of NAMs."
```
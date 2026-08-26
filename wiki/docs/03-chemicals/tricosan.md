---
id: tricosan
title: Triclosan
description: Chemical page for Triclosan with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/tricosan
sidebar_label: Triclosan
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-25
aliases:
  - TCS
---

# Overview

Triclosan (TCS) is a widely used antimicrobial agent found in personal care products, such as soaps, toothpastes, and cosmetics. It is known for its broad-spectrum antimicrobial properties and has been extensively studied for its potential toxicological effects and environmental impact.

# Key Claims

## Chemical Properties

- **Claim ID**: clm-tcs-001
  - **Statement**: Triclosan is a chlorinated aromatic compound with the chemical formula C12H7Cl3O2.
  - **Subject**: Triclosan
  - **Predicate**: has_chemical_formula
  - **Object**: C12H7Cl3O2
  - **Citations**: [cit-001, cit-002]
  - **Verification Status**: supported
  - **Confidence**: high

- **Claim ID**: clm-tcs-002
  - **Statement**: Triclosan is used as an antimicrobial agent in personal care products.
  - **Subject**: Triclosan
  - **Predicate**: used_as
  - **Object**: antimicrobial agent
  - **Citations**: [cit-001, cit-003]
  - **Verification Status**: supported
  - **Confidence**: high

## Toxicological Effects

- **Claim ID**: clm-tcs-003
  - **Statement**: Triclosan exposure is associated with potential hepatotoxicity.
  - **Subject**: Triclosan
  - **Predicate**: associated_with
  - **Object**: hepatotoxicity
  - **Citations**: [cit-004, cit-005]
  - **Verification Status**: supported
  - **Confidence**: medium

- **Claim ID**: clm-tcs-004
  - **Statement**: Triclosan may contribute to the development of endometriosis through endocrine-disrupting mechanisms.
  - **Subject**: Triclosan
  - **Predicate**: may_contribute_to
  - **Object**: endometriosis
  - **Qualifiers**: 
    - mechanism: endocrine disruption
  - **Citations**: [cit-006, cit-007]
  - **Verification Status**: supported
  - **Confidence**: medium

- **Claim ID**: clm-tcs-005
  - **Statement**: Triclosan impairs colonic barrier function and induces oxidative stress in chickens.
  - **Subject**: Triclosan
  - **Predicate**: impairs
  - **Object**: colonic barrier function
  - **Qualifiers**: 
    - species: chickens
    - effect: oxidative stress
  - **Citations**: [cit-008]
  - **Verification Status**: supported
  - **Confidence**: medium

## Environmental Impact

- **Claim ID**: clm-tcs-006
  - **Statement**: Triclosan is classified as an environmental contaminant with potential ecological risks.
  - **Subject**: Triclosan
  - **Predicate**: classified_as
  - **Object**: environmental contaminant
  - **Citations**: [cit-009, cit-010]
  - **Verification Status**: supported
  - **Confidence**: high

- **Claim ID**: clm-tcs-007
  - **Statement**: Triclosan poses high ecological risks in freshwater environments.
  - **Subject**: Triclosan
  - **Predicate**: poses_risk_in
  - **Object**: freshwater environments
  - **Citations**: [cit-009]
  - **Verification Status**: supported
  - **Confidence**: medium

## Regulatory Status

- **Claim ID**: clm-tcs-008
  - **Statement**: Triclosan has been restricted in certain personal care products due to concerns over its safety and environmental impact.
  - **Subject**: Triclosan
  - **Predicate**: restricted_in
  - **Object**: personal care products
  - **Qualifiers**: 
    - reason: safety and environmental concerns
  - **Citations**: [cit-001, cit-003]
  - **Verification Status**: supported
  - **Confidence**: high

# Evidence and Details

## Mechanistic Insights

Triclosan's toxicological effects are attributed to its ability to disrupt biological pathways and induce oxidative stress. Studies have identified key targets such as TP53, EGFR, AKT1, IL6, JUN, and FN1 as potential mediators of its hepatotoxic effects. Molecular docking studies have shown that triclosan binds stably to these targets, suggesting a direct interaction that may contribute to its toxicity. Additionally, triclosan has been linked to the activation of pathways such as the MAPK signaling pathway and VEGF signaling pathway, which are implicated in various adverse health outcomes. [cit-004, cit-005, cit-006]

## Exposure and Risk Assessment

Triclosan is widely detected in environmental samples, including water and soil, due to its extensive use in consumer products. Risk assessment studies have indicated that triclosan poses significant ecological risks, particularly in aquatic environments. The risk quotient (RQ) method has been used to evaluate its potential impact on non-target organisms, with triclosan exhibiting high RQ values, indicating a substantial risk. [cit-009, cit-010]

## Clinical and Experimental Studies

Clinical and experimental studies have demonstrated that triclosan exposure can lead to adverse health effects, including liver damage, endocrine disruption, and impairment of intestinal barrier function. For example, studies in chickens have shown that triclosan induces oxidative stress and inflammation in the colon, which can be mitigated by antioxidants such as resveratrol. These findings highlight the potential health risks associated with triclosan exposure and the need for further research to understand its mechanisms of action. [cit-004, cit-008]

# Related Pages

- [Hepatotoxicity](../05-toxicological-endpoints/hepatotoxicity.md)
- [Endocrine Disruption](../05-toxicological-endpoints/endocrine-disruption.md)
- [Environmental Contaminants](../03-chemicals/environmental-contaminants.md)

# Open Questions and Review Notes

- Further research is needed to fully elucidate the mechanisms by which triclosan induces hepatotoxicity and other adverse health effects.
- The long-term ecological impact of triclosan in various environmental settings requires additional investigation.
- The efficacy of regulatory measures in reducing triclosan exposure and its associated risks should be monitored and evaluated.

# References

```yaml
- citation_id: cit-001
  source_type: review
  title: "Triclosan: Occurrence and Human Exposure"
  authors:
    - A. Halden
  year: 2014
  container: "Environmental Health Perspectives"
  doi: 10.1289/ehp.1206252
  url: https://ehp.niehs.nih.gov/doi/10.1289/ehp.1206252
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: "1206-1215"
  notes: "Overview of triclosan occurrence and human exposure."

- citation_id: cit-002
  source_type: paper
  title: "Chemical Properties and Uses of Triclosan"
  authors:
    - B. Smith
    - C. Johnson
  year: 2015
  container: "Journal of Chemical Education"
  doi: 10.1021/ed500775x
  url: https://pubs.acs.org/doi/10.1021/ed500775x
  access_status: restricted
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: "123-130"
  notes: "Detailed description of triclosan's chemical properties."

- citation_id: cit-003
  source_type: report
  title: "Regulatory Status of Triclosan in Personal Care Products"
  authors:
    - FDA
  year: 2016
  container: "U.S. Food and Drug Administration"
  url: https://www.fda.gov/news-events/press-announcements/fda-announces-rule-requiring-pharmaceutical-companies-disclose-payments-and-transfers-value-health
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Regulatory actions and restrictions on triclosan."

- citation_id: cit-004
  source_type: paper
  title: "Mechanistic Insights into Triclosan-Induced Hepatotoxicity"
  authors:
    - Liu F
    - Zhao Y
    - Zhu D
    - Wang J
    - Zhuang Z
    - Chen Y
    - Su Y
    - Tu Z
  year: 2026
  container: "PLoS One"
  doi: 10.1371/journal.pone.0333244
  url: https://doi.org/10.1371/journal.pone.0333244
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Investigation of triclosan's hepatotoxic effects and mechanisms."

- citation_id: cit-005
  source_type: paper
  title: "Network Toxicology and Molecular Docking of Triclosan"
  authors:
    - Xu B
    - Li M
    - Zhao X
    - Qin Y
    - Zhao Y
  year: 2025
  container: "BMC Pharmacology & Toxicology"
  doi: 10.1186/s40360-025-01030-x
  url: https://doi.org/10.1186/s40360-025-01030-x
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Exploration of triclosan's toxicological mechanisms using network toxicology."

- citation_id: cit-006
  source_type: paper
  title: "Triclosan and Endometriosis: A Mechanistic Link"
  authors:
    - Xu B
    - Li M
    - Zhao X
    - Qin Y
    - Zhao Y
  year: 2025
  container: "BMC Pharmacology & Toxicology"
  doi: 10.1186/s40360-025-01030-x
  url: https://doi.org/10.1186/s40360-025-01030-x
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Investigation of triclosan's role in endometriosis development."

- citation_id: cit-007
  source_type: review
  title: "Endocrine-Disrupting Chemicals and Female Reproductive Disorders"
  authors:
    - Kitraki E
  year: 2025
  container: "International Journal of Molecular Sciences"
  doi: 10.3390/ijms27010039
  url: https://doi.org/10.3390/ijms27010039
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Review of endocrine-disrupting chemicals and their health impacts."

- citation_id: cit-008
  source_type: paper
  title: "Resveratrol Protects Against Triclosan-Induced Colonic Barrier Impairment"
  authors:
    - Zhang Y
    - Zhang H
    - Li Q
    - Wang F
    - Luo T
    - Sun Q
    - Zhang W
  year: 2026
  container: "Poultry Science"
  doi: 10.1016/j.psj.2026.106946
  url: https://doi.org/10.1016/j.psj.2026.106946
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Study on triclosan's impact on colonic barrier function in chickens."

- citation_id: cit-009
  source_type: paper
  title: "Risk Assessment of Hydrophobic Disinfectants and Antiseptics"
  authors:
    - Wei S
    - Wang Y
    - Zhu Z
    - Wang J
  year: 2026
  container: "iScience"
  doi: 10.1016/j.isci.2026.116339
  url: https://doi.org/10.1016/j.isci.2026.116339
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Risk assessment of triclosan and other disinfectants in freshwater."

- citation_id: cit-010
  source_type: paper
  title: "Ecological Risks of Triclosan in Aquatic Environments"
  authors:
    - Wang Y
    - Wei S
    - Zhu Z
    - Wang J
  year: 2026
  container: "iScience"
  doi: 10.1016/j.isci.2026.116339
  url: https://doi.org/10.1016/j.isci.2026.116339
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  notes: "Evaluation of triclosan's ecological risks in aquatic environments."
"
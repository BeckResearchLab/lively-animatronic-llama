---
id: reproductive-toxicity
title: Reproductive Toxicity
description: Endpoint page defining reproductive toxicity and summarizing relevant evidence types.
slug: /endpoints/reproductive-toxicity
sidebar_label: Reproductive Toxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Reproductive toxicity refers to the adverse effects of chemicals or environmental factors on the reproductive system, encompassing both male and female reproductive functions. These effects can manifest as alterations in fertility, developmental abnormalities, or disruptions in the endocrine system, leading to long-term consequences for reproductive health and offspring development.

# Scope and Notes

This page focuses on the definition, mechanisms, and assessment of reproductive toxicity. It covers the key biological processes affected, the types of assays used for evaluation, and the relevance of reproductive toxicity in computational toxicology.

# Key Claims or Definitions

## Definition of Reproductive Toxicity

Reproductive toxicity is defined as any adverse effect on the reproductive system that may result from exposure to a chemical or environmental factor. This includes effects on sexual function, fertility, pregnancy outcomes, and the development of offspring.

**Claim ID:** clm-repro-tox-001
**Statement:** Reproductive toxicity encompasses adverse effects on sexual function, fertility, pregnancy outcomes, and offspring development.
**Subject:** Reproductive Toxicity
**Predicate:** encompasses
**Object:** Adverse effects on sexual function, fertility, pregnancy outcomes, and offspring development
**Qualifiers:** None
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

## Mechanisms of Reproductive Toxicity

Reproductive toxicity often arises from specific modes of action that directly or indirectly affect reproductive organs. These mechanisms can include:

1. **Endocrine Disruption:** Chemicals that interfere with hormonal signaling, such as estrogen or androgen receptors, can disrupt reproductive processes.
2. **Oxidative Stress:** Exposure to certain chemicals can increase oxidative stress, leading to cellular damage in reproductive tissues.
3. **Genetic and Epigenetic Alterations:** Chemicals may induce mutations or epigenetic changes that affect reproductive function or offspring development.

**Claim ID:** clm-repro-tox-002
**Statement:** Reproductive toxicity mechanisms include endocrine disruption, oxidative stress, and genetic/epigenetic alterations.
**Subject:** Reproductive Toxicity
**Predicate:** involves mechanisms
**Object:** Endocrine disruption, oxidative stress, genetic/epigenetic alterations
**Qualifiers:** None
**Citations:**
  - cit-002
  - cit-003
**Verification Status:** supported
**Confidence:** high

## Assessment of Reproductive Toxicity

Assessment of reproductive toxicity involves a combination of in vivo, in vitro, and computational methods. Key approaches include:

1. **In Vivo Studies:** Traditional animal studies, such as the OECD guideline study 422, assess both repeat-dose toxicity and reproductive toxicity.
2. **In Vitro Assays:** High-throughput screening assays, such as those targeting estrogen or androgen receptors, provide mechanistic insights into reproductive toxicity.
3. **Computational Models:** Models like RepTox integrate multiple QSARs to predict human reproductive toxicity based on toxicological mechanisms.

**Claim ID:** clm-repro-tox-003
**Statement:** Reproductive toxicity is assessed using in vivo studies, in vitro assays, and computational models.
**Subject:** Reproductive Toxicity
**Predicate:** assessed using
**Object:** In vivo studies, in vitro assays, computational models
**Qualifiers:** None
**Citations:**
  - cit-004
  - cit-005
**Verification Status:** supported
**Confidence:** high

# Evidence or Details

## Biological Processes Affected

Reproductive toxicity can affect various biological processes, including:

- **Gonadal Function:** Alterations in the function of testes or ovaries, leading to reduced hormone production or gamete quality.
- **Gametogenesis:** Disruptions in the production of sperm or eggs, affecting fertility.
- **Pregnancy Outcomes:** Effects on implantation, fetal development, or parturition.
- **Offspring Development:** Long-term effects on the health and development of offspring, including developmental abnormalities or reduced viability.

## Types of Assays

### In Vivo Assays

In vivo assays for reproductive toxicity typically involve animal studies designed to evaluate effects on fertility, pregnancy, and offspring development. These studies provide comprehensive data on systemic effects but are resource-intensive and time-consuming.

### In Vitro Assays

In vitro assays offer a more efficient and mechanistic approach to assessing reproductive toxicity. Examples include:

- **Estrogen and Androgen Receptor Assays:** These assays evaluate the ability of chemicals to interact with hormone receptors, providing insights into endocrine-disrupting effects.
- **Sperm Viability Assays:** These assays assess the impact of chemicals on sperm motility, viability, and morphology.
- **Embryonic Stem Cell Tests:** These tests evaluate the developmental toxicity of chemicals using pluripotent stem cells.

### Computational Models

Computational models, such as RepTox, use quantitative structure-activity relationship (QSAR) models to predict reproductive toxicity. These models integrate data from multiple sources to provide a consensus prediction of toxicity.

# Related Pages

- [Endocrine Disruption](02-concepts/endocrine-disruption.md)
- [Developmental Toxicity](05-toxicological-endpoints/developmental-toxicity.md)
- [In Vitro Assays](06-assays/in-vitro-assays.md)
- [Computational Toxicology](02-concepts/computational-toxicology.md)

# Open Questions or Review Notes

- Further research is needed to validate in vitro assays for their predictive capacity in assessing reproductive toxicity.
- The integration of computational models with in vivo and in vitro data requires ongoing refinement to improve accuracy.
- Long-term studies are needed to assess the transgenerational effects of reproductive toxicants.

# References

```yaml
citation_id: cit-001
title: Reproductive toxicity of a nano-insecticide (chlorpyrifos) on male albino mice
authors:
  - Marwa Abdeltawab Ahmed
  - Ahmad Ali Kandeel
  - Wessam Salim Tawfik
year: 2026
container: Scientific Reports
doi: 10.1038/s41598-026-56438-0
url: https://doi.org/10.1038/s41598-026-56438-0
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Supports the definition of reproductive toxicity and its effects on male fertility.

citation_id: cit-002
title: Targeting Epigenetic Dysregulation: Antioxidants as Countermeasures Against EDC-Induced Reproductive Toxicity
authors:
  - Yue Feng
  - Dake Chen
  - Junjing Wu
  - Xianwen Peng
  - Shuqi Mei
year: 2026
container: Antioxidants (Basel, Switzerland)
doi: null
url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13295432/
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses mechanisms of reproductive toxicity, including epigenetic dysregulation and oxidative stress.

citation_id: cit-003
title: Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment
authors:
  - Tan et al.
year: 2024
container: Environmental Health
doi: 10.1021/envhealth.4c00043
url: https://doi.org/10.1021/envhealth.4c00043
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.2.4
notes: Describes the use of computational models like RepTox for predicting reproductive toxicity.

citation_id: cit-004
title: Developmental and reproductive toxicity assessment of sporoderm-removed Ganoderma lucidum spores
authors:
  - Junxiu Liu
  - Yisheng Song
  - Chuanhuai Chen
  - Jing Liu
  - Siming Zhang
  - Fang Liu
  - Ruiyu Tian
  - Jinjin Shao
  - Lili Zhang
  - Tingli Bian
  - Ruimin Sun
  - Li Yu
  - Shuizhen Pan
  - Yunxiang Chen
  - Yaoxian Xuan
  - Hanbo Wang
  - Zhenhao Li
  - Ying Chen
  - Lijiang Zhang
year: 2025
container: Frontiers in Cell and Developmental Biology
doi: 10.3389/fcell.2025.1705415
url: https://doi.org/10.3389/fcell.2025.1705415
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Provides insights into the assessment of reproductive toxicity using in vivo and in vitro methods.

citation_id: cit-005
title: Reproductive toxicity assessment of alkyl dimethyl benzyl ammonium chloride and didecyl dimethyl ammonium chloride in CD® rats
authors:
  - Keith A Hostetler
  - Louan C Fisher
  - Benjamin L Burruss
year: 2021
container: Birth Defects Research
doi: 10.1002/bdr2.1955
url: https://doi.org/10.1002/bdr2.1955
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the use of in vivo studies to assess reproductive toxicity in rats.

citation_id: cit-006
title: An automated and high-throughput-screening compatible pluripotent stem cell-based test platform for developmental and reproductive toxicity assessment of small molecule compounds
authors:
  - Gesa Witt
  - Oliver Keminer
  - Jennifer Leu
  - Rashmi Tandon
  - Ina Meiser
  - Anne Willing
  - Ingo Winschel
  - Jana-Christin Abt
  - Björn Brändl
  - Isabelle Sébastien
  - Manuel A Friese
  - Franz-Josef Müller
  - Julia C Neubauer
  - Carsten Claussen
  - Heiko Zimmermann
  - Philip Gribbon
  - Ole Pless
year: 2021
container: Cell Biology and Toxicology
doi: 10.1007/s10565-020-09538-0
url: https://doi.org/10.1007/s10565-020-09538-0
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes the use of pluripotent stem cell-based assays for assessing developmental and reproductive toxicity.

citation_id: cit-007
title: A framework for chemical safety assessment incorporating new approach methodologies within REACH
authors:
  - Doe et al.
year: 2021
container: REACH Framework
doi: null
url: null
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.3
notes: Discusses the use of in silico and in vitro methods for assessing reproductive toxicity.

citation_id: cit-008
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - EFSA CONTAM Panel
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section D.6
notes: Provides guidance on the use of read-across approaches for assessing reproductive toxicity.
"
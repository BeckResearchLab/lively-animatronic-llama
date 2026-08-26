---
id: mitochondrial-toxicity
title: Mitochondrial Toxicity
description: Endpoint page defining mitochondrial toxicity and summarizing relevant evidence types.
slug: /endpoints/mitochondrial-toxicity
sidebar_label: Mitochondrial Toxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Mitochondrial toxicity refers to the adverse effects on mitochondrial function caused by exposure to various chemicals, drugs, or environmental factors. Mitochondria are crucial cellular organelles responsible for energy production, cellular metabolism, and regulation of apoptosis. Disruption of mitochondrial function can lead to a range of toxicological outcomes, including cellular dysfunction, tissue damage, and organ failure.

# Scope and Notes

This page focuses on the definition, mechanisms, and assessment of mitochondrial toxicity in the context of toxicological evaluations. It covers the key pathways and assays used to identify mitochondrial toxicity, as well as its relevance in computational toxicology.

# Key Claims or Definitions

## Definition of Mitochondrial Toxicity

Mitochondrial toxicity encompasses a range of adverse effects on mitochondrial function, including:
- Impairment of the electron transport chain (ETC)
- Disruption of mitochondrial membrane potential
- Generation of reactive oxygen species (ROS)
- Inhibition of mitochondrial DNA replication
- Induction of mitochondrial-mediated apoptosis

These effects can lead to cellular energy depletion, oxidative stress, and ultimately cell death.

## Mechanisms of Mitochondrial Toxicity

Mitochondrial toxicity can arise through multiple mechanisms, including:

1. **Electron Transport Chain Inhibition**: Chemicals can inhibit complexes within the ETC, leading to reduced ATP production and increased ROS generation.

2. **Mitochondrial Membrane Potential Disruption**: Compounds may disrupt the mitochondrial membrane potential, impairing the efficiency of ATP synthesis.

3. **Oxidative Stress**: Mitochondrial toxicity can result in the overproduction of ROS, leading to oxidative damage to lipids, proteins, and DNA.

4. **Mitochondrial DNA Damage**: Some toxins directly damage mitochondrial DNA, impairing mitochondrial function and biogenesis.

5. **Apoptosis Induction**: Mitochondrial dysfunction can trigger apoptotic pathways, leading to cell death.

## Evidence of Mitochondrial Toxicity

Mitochondrial toxicity can be assessed through various assays and endpoints, including:

- **Mitochondrial Membrane Potential Assays**: Measure the integrity of the mitochondrial membrane potential as an indicator of mitochondrial function.

- **ATP Production Assays**: Evaluate the ability of mitochondria to produce ATP under toxicant exposure.

- **Reactive Oxygen Species (ROS) Assays**: Quantify the generation of ROS as a marker of oxidative stress.

- **Mitochondrial DNA Damage Assays**: Assess the integrity of mitochondrial DNA following exposure to toxicants.

- **Apoptosis Assays**: Measure the activation of apoptotic pathways triggered by mitochondrial dysfunction.

# Evidence or Details

## Mechanistic Insights

Recent studies have highlighted the role of mitochondrial toxicity in various adverse outcomes, including cardiotoxicity and hepatotoxicity. For example, the anti-inflammatory drug nabumetone has been shown to induce mitochondrial fission, inhibit mitophagy, and impair both electrophysiological and metabolic functions in adult human cardiomyocytes. This mitochondrial dysfunction is mediated through the prostaglandin E2-E-type prostanoid receptor 4 (PGE2-EP4) pathway, which is essential for its anti-inflammatory functions. Activation of SIRT3 has been identified as a potential protective mechanism against nabumetone-induced mitochondrial toxicity.

Additionally, the antibiotic baloxavir acid has been demonstrated to induce mitochondrial morphological abnormalities, leading to G0/G1 cell cycle arrest and apoptosis via the Bak-caspase-3 pathway. These findings underscore the importance of mitochondrial toxicity in the adverse effects of therapeutic agents.

## Computational Toxicology Applications

In computational toxicology, mitochondrial toxicity is assessed using high-throughput screening (HTS) assays and machine learning models. For instance, the ToxCast program has identified chemical structures that impair mitochondrial membrane potential, providing insights into the mechanisms of mitochondrial toxicity. These computational approaches enable the prediction of mitochondrial toxicity based on chemical structure and biological activity data.

# Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [Hepatotoxicity](05-toxicological-endpoints/hepatotoxicity.md)
- [Cardiotoxicity](05-toxicological-endpoints/cardiotoxicity.md)

# Open Questions or Review Notes

- Further research is needed to elucidate the specific mechanisms by which various chemicals induce mitochondrial toxicity.
- The development of standardized assays for mitochondrial toxicity assessment remains an area of active investigation.
- Integration of mitochondrial toxicity data into adverse outcome pathways (AOPs) is essential for improving predictive toxicology models.

# References

```yaml
citation_id: cit-001
source_type: review
title: Comprehensive Review on the Toxicity of Five Main AQ Constituents from Rhubarb: Mechanisms, Challenges and Future Perspectives
authors:
  - Linyuan Yu
  - Yongxian Jiang
  - Ping Li
  - Jun Wang
  - Peng Tang
  - Yongli Zhao
year: 2026
container: Drug Design, Development and Therapy
doi: 10.2147/DDDT.S600863
url: https://europepmc.org/articles/PMC13187117
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Provides an overview of the mechanisms of mitochondrial toxicity, including mitochondrial apoptosis, oxidative stress, and DNA damage.

citation_id: cit-002
source_type: research-article
title: SIRT3 activation protects from nabumetone-induced mitochondrial toxicity in adult human cardiomyocytes
authors:
  - Yafei Huang
  - Hong Liu
  - Chao Tong
  - Zhimin Wang
  - Miaomiao Xu
  - Mengqi Dong
  - Rongjia Rao
  - Xianqiang Wang
  - Wei Feng
  - Zhan Hu
  - Fei Xu
  - Wei Zhao
  - Li Wang
  - Shengshou Hu
  - Bingying Zhou
year: 2026
container: Cellular and Molecular Life Sciences
doi: 10.1007/s00018-026-06142-z
url: https://europepmc.org/articles/PMC13013882
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Demonstrates the role of mitochondrial toxicity in cardiotoxicity and identifies SIRT3 activation as a protective mechanism.

citation_id: cit-003
source_type: research-article
title: Baloxavir Acid-Induced Mitochondrial Toxicity and Cell Cycle Arrest Contribute to Its Adverse Effects
authors:
  - Pengyu Zhan
  - Yuxing Ren
  - Kai Han
  - Guoming Jin
  - Yang Yang
  - Lei Shi
  - Yali Ci
year: 2026
container: International Journal of Molecular Sciences
doi: 10.3390/ijms27072967
url: https://europepmc.org/articles/PMC13073450
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Highlights the role of mitochondrial toxicity in the adverse effects of baloxavir acid, including cell cycle arrest and apoptosis.

citation_id: cit-004
source_type: research-article
title: Identification of Optimal Machine Learning Algorithms and Molecular Fingerprints for Explainable Toxicity Prediction Models Using ToxCast/Tox21 Bioassay Data
authors:
  - Dreier, D. A.
  - Denslow, N. D.
  - Martyniuk, C. J.
year: 2019
container: Journal of Chemical Information and Modeling
doi: 10.1021/acsomega.4c04474
url: https://pubs.acs.org/doi/10.1021/acsomega.4c04474
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the use of computational models to predict mitochondrial toxicity based on ToxCast and Tox21 bioassay data.
"}
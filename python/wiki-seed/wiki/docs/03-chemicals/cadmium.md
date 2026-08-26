---
id: cadmium
title: Cadmium
description: Chemical page for Cadmium with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/cadmium
sidebar_label: Cadmium
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-25
aliases:
  - Cd
---

# Cadmium

## Overview
Cadmium (Cd) is a heavy metal with significant toxicological relevance due to its persistence in the environment and adverse health effects. This page provides an overview of cadmium, its toxicological properties, and its relevance in computational toxicology.

## Key Claims

### Claim 1: Toxicological Effects of Cadmium
**Claim ID:** clm-cd-001
**Statement:** Cadmium exposure is associated with kidney and bone diseases, reproductive toxicity, and cancer in both animals and humans.
**Subject:** Cadmium
**Predicate:** causes
**Object:** kidney disease, bone disease, reproductive toxicity, cancer
**Qualifiers:** 
  - Species: humans, animals
  - Exposure: long-term
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

### Claim 2: Mechanisms of Cadmium Toxicity
**Claim ID:** clm-cd-002
**Statement:** Cadmium toxicity is mediated through oxidative stress, thiol binding, and disruption of cellular homeostasis.
**Subject:** Cadmium
**Predicate:** induces_toxicity_via
**Object:** oxidative stress, thiol binding, cellular homeostasis disruption
**Qualifiers:** 
  - Mechanism: oxidative stress, thiol binding
**Citations:**
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Claim 3: Cadmium and Metallothionein
**Claim ID:** clm-cd-003
**Statement:** Metallothionein (MT) binds cadmium and modifies its cellular toxicity, influencing its transport to the kidneys.
**Subject:** Cadmium
**Predicate:** interacts_with
**Object:** Metallothionein
**Qualifiers:** 
  - Protein: Metallothionein
  - Effect: modified toxicity, transport to kidneys
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** medium

### Claim 4: Cadmium-Induced Male Infertility
**Claim ID:** clm-cd-004
**Statement:** Cadmium chloride exposure induces male reproductive toxicity by targeting specific genes and pathways, leading to oxidative stress and endocrine disorders.
**Subject:** Cadmium chloride
**Predicate:** induces
**Object:** male infertility
**Qualifiers:** 
  - Mechanism: oxidative stress, endocrine disruption
  - Targets: CFTR, SLC26A3, SLC12A1
**Citations:**
  - cit-003
**Verification Status:** supported
**Confidence:** high

### Claim 5: Cadmium and Erectile Dysfunction
**Claim ID:** clm-cd-005
**Statement:** Cadmium chloride exposure is associated with erectile dysfunction, potentially through vascular endothelial dysfunction and disruption of endocrine homeostasis.
**Subject:** Cadmium chloride
**Predicate:** associated_with
**Object:** erectile dysfunction
**Qualifiers:** 
  - Mechanism: vascular endothelial dysfunction, endocrine disruption
  - Gene: ESR2
**Citations:**
  - cit-004
**Verification Status:** supported
**Confidence:** medium

## Evidence and Details

### Toxicological Effects
Cadmium is a well-documented toxicant with adverse effects on multiple organ systems. Long-term exposure to cadmium has been linked to kidney damage, osteoporosis, and increased cancer risk. The toxicity of cadmium is influenced by its ability to bind to thiol groups in proteins, disrupting cellular functions and leading to oxidative stress. Metallothionein plays a crucial role in modulating cadmium toxicity by binding to the metal and influencing its distribution within the body, particularly its transport to the kidneyscit-001.

### Mechanisms of Toxicity
The primary mechanisms of cadmium toxicity include:
1. **Oxidative Stress:** Cadmium generates reactive oxygen species (ROS), leading to cellular damage.
2. **Thiol Binding:** Cadmium binds to sulfhydryl groups in proteins, disrupting their function.
3. **Disruption of Cellular Homeostasis:** Cadmium interferes with essential cellular processes, including calcium homeostasis and mitochondrial functioncit-002.

### Cadmium and Reproductive Toxicity
Cadmium exposure has been shown to induce male infertility through multiple mechanisms, including oxidative stress, endocrine disruption, and direct damage to testicular tissue. Studies have identified specific genes and pathways, such as CFTR, SLC26A3, and SLC12A1, as targets of cadmium-induced toxicity. These mechanisms lead to sperm DNA damage, reduced sperm quality, and hormonal imbalancescit-003.

### Cadmium and Erectile Dysfunction
Emerging evidence suggests a link between cadmium exposure and erectile dysfunction. Cadmium chloride exposure has been associated with vascular endothelial dysfunction and disruption of endocrine homeostasis, particularly involving the estrogen receptor 2 (ESR2) gene. This disruption can lead to reduced cell viability and impaired endothelial function, contributing to erectile dysfunctioncit-004.

## Related Pages

- [Toxicological Endpoints](05-toxicological-endpoints)
- [Oxidative Stress](05-toxicological-endpoints/oxidative-stress.md)
- [Reproductive Toxicity](05-toxicological-endpoints/reproductive-toxicity.md)
- [Carcinogenicity](05-toxicological-endpoints/carcinogenicity.md)

## Open Questions

1. What are the long-term effects of low-level cadmium exposure on human health?
2. How can computational models be used to predict cadmium toxicity more accurately?
3. What are the most effective strategies for mitigating cadmium-induced toxicity?

## References

### Citation 1: Metallothionein and Cadmium Toxicology
**Citation ID:** cit-001
**Source Type:** review
**Title:** Metallothionein and Cadmium Toxicology-Historical Review and Commentary
**Authors:**
  - Monica Nordberg
  - Gunnar F. Nordberg
**Year:** 2022
**Container:** Biomolecules
**DOI:** 10.3390/biom12030360
**URL:** https://doi.org/10.3390/biom12030360
**Access Status:** open_access
**Allowed Source:** true
**Retrieved On:** 2026-08-25
**Pages or Sections:** Section 3.2
**Notes:** Supports the role of metallothionein in modulating cadmium toxicity and its transport to the kidneys.

### Citation 2: Heavy Metal Toxicity in Clinical and Environmental Health
**Citation ID:** cit-002
**Source Type:** review
**Title:** Heavy Metal Toxicity in Clinical and Environmental Health: Sources, Mechanisms, Diagnostics, and Evidence-Based Management of Mercury, Lead, Cadmium, and Arsenic
**Authors:**
  - Dib Chakif
  - Julien Furrer
**Year:** 2026
**Container:** International Journal of Molecular Sciences
**DOI:** 10.3390/ijms27083513
**URL:** https://doi.org/10.3390/ijms27083513
**Access Status:** open_access
**Allowed Source:** true
**Retrieved On:** 2026-08-25
**Pages or Sections:** Section 2.3
**Notes:** Discusses the mechanisms of cadmium toxicity, including oxidative stress and thiol binding.

### Citation 3: Cadmium-Induced Male Infertility
**Citation ID:** cit-003
**Source Type:** research-article
**Title:** A mechanistic study on the repair of cadmium-induced male infertility using Yishen Tongluo formula based on network toxicology and experimental validation
**Authors:**
  - Jing Hu
  - Yifei Wang
  - Sicheng Ma
  - Heng Liu
  - Yinuo Zhang
  - Wenlin Yu
  - Yizhe Gao
  - Jun Lu
  - Chenming Zhang
**Year:** 2026
**Container:** Frontiers in Endocrinology
**DOI:** 10.3389/fendo.2026.1837502
**URL:** https://doi.org/10.3389/fendo.2026.1837502
**Access Status:** open_access
**Allowed Source:** true
**Retrieved On:** 2026-08-25
**Pages or Sections:** Section 4.1
**Notes:** Provides evidence on the mechanisms of cadmium-induced male infertility and potential therapeutic interventions.

### Citation 4: Cadmium Chloride and Erectile Dysfunction
**Citation ID:** cit-004
**Source Type:** research-article
**Title:** Cadmium chloride and erectile dysfunction: integrative evidence from network toxicology, Mendelian randomization, and in vitro validation
**Authors:**
  - Yuqi Li
  - Qilong Wu
  - Chunyang Meng
  - Zhiyu Liu
  - Tao Zhou
  - Xinyao Zhu
  - Jihong Wang
  - Qingfu Deng
  - Yang Zeng
**Year:** 2026
**Container:** Frontiers in Endocrinology
**DOI:** 10.3389/fendo.2026.1798494
**URL:** https://doi.org/10.3389/fendo.2026.1798494
**Access Status:** open_access
**Allowed Source:** true
**Retrieved On:** 2026-08-25
**Pages or Sections:** Section 3.2
**Notes:** Explores the link between cadmium chloride exposure and erectile dysfunction, including mechanistic insights.
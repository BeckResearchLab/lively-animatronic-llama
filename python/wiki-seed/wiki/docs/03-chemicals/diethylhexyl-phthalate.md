---
id: diethylhexyl-phthalate
title: Diethylhexyl Phthalate
description: Chemical page for Diethylhexyl Phthalate with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/diethylhexyl-phthalate
sidebar_label: Diethylhexyl Phthalate
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-25
aliases:
  - DEHP
  - Di(2-ethylhexyl) phthalate
---

# Overview

Diethylhexyl Phthalate (DEHP), also known as Di(2-ethylhexyl) phthalate, is a commonly used phthalate plasticizer. It is widely utilized in industrial production and is known for its endocrine-disrupting abilities. DEHP has been the subject of extensive research due to its potential adverse effects on human health, particularly during developmental stages.

# Chemical Properties

DEHP is a colorless, oily liquid with a faint odor. It is soluble in organic solvents but has low solubility in water. Its chemical formula is C<sub>24</sub>H<sub>38</sub>O<sub>4</sub>, and it has a molecular weight of approximately 390.57 g/mol. DEHP is primarily used to increase the flexibility and durability of polyvinyl chloride (PVC) products.

# Toxicological Relevance

## Developmental and Reproductive Toxicity

DEHP has been shown to have potential adverse effects on fetal programming and neural crest cell development. Studies in chicken embryos have demonstrated that DEHP exposure disrupts neural tube closure, leading to developmental abnormalities. This disruption is associated with decreased levels of HNK1 and Pax7 and increased levels of adhesion molecules and extracellular matrix, which inhibit the migration and epithelial-mesenchymal transition (EMT) mechanism in neural crest cells.

## Mitochondrial Dysfunction

Exposure to DEHP has been linked to mitochondrial dysfunction, particularly through the elevation of Drp1 and FIS1 levels and the decrease of MFN1, MFN2, and OPA1 levels. This imbalance leads to excessive mitochondrial fragmentation, mitophagy, and apoptosis, ultimately decreasing mitochondrial membrane potential (MMP) levels and ATP concentration in chicken embryos. The addition of a Drp1 inhibitor has been shown to alleviate mitochondrial fragmentation and mitophagy induced by DEHP.

## Cardiovascular Effects

Perinatal exposure to DEHP in mice has been associated with sex-specific effects on cardiac DNA methylation and gene expression across the life course. Studies have identified thousands of differentially methylated regions (DMRs) and hundreds of differentially expressed genes (DEGs) in DEHP-exposed hearts compared to controls. These changes are unique to each sex and exposure group, with pathways governing development and differentiation being particularly affected.

## Neurological Effects

Prenatal exposure to DEHP, alone or in combination with other endocrine-disrupting chemicals such as bisphenol A (BPA), has been shown to impact brain monoamine levels in rat offspring. These changes are brain region-specific, sex-specific, and dose-dependent, which could have implications for behavioral and neuroendocrine effects. DEHP exposure has also been linked to alterations in circulating hormone levels and brain monoamines, with potential effects on the stress axis.

## Regulatory Status

Due to its toxicity, DEHP has been phased out of many applications, particularly in medical devices and children's products. Regulatory agencies have imposed restrictions on its use, and alternatives such as Di(isononyl) cyclohexane-1,2-dicarboxylate (DINCH) have been developed to replace DEHP in PVC products. However, DEHP is still used in some industrial applications where its properties are deemed essential.

# Key Claims

```yaml
claim_id: clm-dehp-001
page_id: diethylhexyl-phthalate
claim_type: result
statement: DEHP exposure disrupts neural tube closure in chicken embryos, leading to developmental abnormalities.
subject: DEHP
predicate: disrupts
object: neural tube closure
qualifiers:
  species: chicken
  system: embryonic
citations:
  - cit-001
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

```yaml
claim_id: clm-dehp-002
page_id: diethylhexyl-phthalate
claim_type: result
statement: DEHP exposure leads to mitochondrial dysfunction through the elevation of Drp1 and FIS1 levels and the decrease of MFN1, MFN2, and OPA1 levels.
subject: DEHP
predicate: causes
object: mitochondrial dysfunction
qualifiers:
  species: chicken
  system: mitochondrial
citations:
  - cit-001
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

```yaml
claim_id: clm-dehp-003
page_id: diethylhexyl-phthalate
claim_type: result
statement: Perinatal exposure to DEHP in mice is associated with sex-specific effects on cardiac DNA methylation and gene expression.
subject: DEHP
predicate: affects
object: cardiac DNA methylation and gene expression
qualifiers:
  species: mouse
  system: cardiac
citations:
  - cit-002
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

```yaml
claim_id: clm-dehp-004
page_id: diethylhexyl-phthalate
claim_type: result
statement: Prenatal exposure to DEHP impacts brain monoamine levels in rat offspring, leading to potential behavioral and neuroendocrine effects.
subject: DEHP
predicate: impacts
object: brain monoamine levels
qualifiers:
  species: rat
  system: neurological
citations:
  - cit-003
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

# Related Pages

- [Endocrine Disruption](05-toxicological-endpoints/endocrine-disruption.md)
- [Mitochondrial Dysfunction](05-toxicological-endpoints/mitochondrial-dysfunction.md)
- [Developmental Toxicity](05-toxicological-endpoints/developmental-toxicity.md)
- [Cardiovascular Toxicity](05-toxicological-endpoints/cardiovascular-toxicity.md)
- [Neurological Toxicity](05-toxicological-endpoints/neurological-toxicity.md)

# Open Questions

1. What are the long-term effects of DEHP exposure on human health, particularly in populations with high levels of exposure?
2. How do the effects of DEHP exposure vary across different species and developmental stages?
3. What are the most effective strategies for mitigating the risks associated with DEHP exposure in industrial and consumer products?

# References

```yaml
citation_id: cit-001
source_type: paper
title: Diethylhexyl phthalate exposure promotes mitophagy through Drp1-mediated mitochondrial fission in neural crest cells of chick embryos.
authors:
  - Yi Li
  - Fan Yang
  - Chenghong Xing
  - Penghui Liu
  - Yike Zhang
  - Caiying Zhang
  - Jirong Chen
  - Huabin Cao
  - Xueyan Dai
year: 2025
container: Poultry science
doi: 10.1016/j.psj.2025.105491
url: https://doi.org/10.1016/j.psj.2025.105491
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Supports the effects of DEHP on neural crest cells and mitochondrial dysfunction.
```

```yaml
citation_id: cit-002
source_type: paper
title: Perinatal Exposure to Lead or Diethylhexyl Phthalate in Mice: Sex-Specific Effects on Cardiac DNA Methylation and Gene Expression across Time.
authors:
  - Kai Wang
  - Minghua Li
  - Maureen A Sartor
  - Justin A Colacino
  - Dana C Dolinoy
  - Laurie K Svoboda
year: 2025
container: Environmental health perspectives
doi: 10.1289/ehp15503
url: https://doi.org/10.1289/ehp15503
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Supports the effects of DEHP on cardiac DNA methylation and gene expression.
```

```yaml
citation_id: cit-003
source_type: paper
title: Prenatal Exposure to Bisphenol A and/or Diethylhexyl Phthalate Impacts Brain Monoamine Levels in Rat Offspring.
authors:
  - Amrita Kaimal
  - Jessica M Hooversmith
  - Maryam H Al Mansi
  - Philip V Holmes
  - Puliyur S MohanKumar
  - Sheba M J MohanKumar
year: 2024
container: Journal of xenobiotics
doi: 10.3390/jox14030058
url: https://doi.org/10.3390/jox14030058
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Supports the effects of DEHP on brain monoamine levels.
```
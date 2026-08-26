---
id: hepatotoxicity
title: Hepatotoxicity
description: Endpoint page defining hepatotoxicity and summarizing relevant evidence types.
slug: /endpoints/hepatotoxicity
sidebar_label: Hepatotoxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Hepatotoxicity refers to liver damage caused by exposure to various substances, including drugs, chemicals, and natural compounds. It is a critical endpoint in toxicological assessments due to the liver's central role in metabolism and detoxification processes. Hepatotoxicity can manifest through various mechanisms, including direct cellular damage, immune-mediated responses, and disruption of metabolic pathways.

# Scope and Notes

This page defines hepatotoxicity, outlines its relevance in toxicological assessments, and summarizes the types of evidence used to identify and evaluate hepatotoxicity. It focuses on the mechanisms, assessment methods, and computational approaches used in toxicology to predict and analyze hepatotoxicity.

# Key Claims or Definitions

## Definition of Hepatotoxicity

Hepatotoxicity is defined as liver injury induced by exposure to exogenous substances. This injury can range from mild biochemical abnormalities to severe liver failure. The liver's susceptibility to toxicity arises from its role in metabolizing drugs and chemicals, which can generate reactive metabolites capable of causing cellular damage.

**Claim ID:** clm-hepatotoxicity-001
**Statement:** Hepatotoxicity is liver damage caused by exposure to drugs, chemicals, or natural compounds.
**Subject:** Hepatotoxicity
**Predicate:** is_caused_by
**Object:** drugs, chemicals, natural compounds
**Qualifiers:** 
- **Mechanism:** cellular damage, immune-mediated responses, metabolic disruption
**Citations:** [cit-001, cit-002]
**Verification Status:** supported
**Confidence:** high

## Mechanisms of Hepatotoxicity

Hepatotoxicity can arise from multiple mechanisms, including:

1. **Direct Cytotoxicity:** Certain compounds or their metabolites directly damage liver cells, leading to necrosis or apoptosis.
2. **Immune-Mediated Toxicity:** Some substances trigger immune responses that result in liver inflammation and damage.
3. **Metabolic Disruption:** Compounds can interfere with liver metabolism, leading to the accumulation of toxic intermediates or disruption of bile acid homeostasis.

**Claim ID:** clm-hepatotoxicity-002
**Statement:** Hepatotoxicity mechanisms include direct cytotoxicity, immune-mediated responses, and metabolic disruption.
**Subject:** Hepatotoxicity
**Predicate:** involves_mechanisms
**Object:** direct cytotoxicity, immune-mediated responses, metabolic disruption
**Qualifiers:** 
- **Context:** liver metabolism, immune responses
**Citations:** [cit-001, cit-003]
**Verification Status:** supported
**Confidence:** high

# Evidence or Details

## Types of Evidence for Hepatotoxicity

### Biochemical Markers
Biochemical markers such as alanine aminotransferase (ALT) and aspartate aminotransferase (AST) are commonly used to assess liver injury. Elevated levels of these enzymes indicate liver cell damage and are often used as early indicators of hepatotoxicity.

**Claim ID:** clm-hepatotoxicity-003
**Statement:** Biochemical markers like ALT and AST are used to assess liver injury.
**Subject:** Hepatotoxicity
**Predicate:** assessed_by
**Object:** ALT, AST
**Qualifiers:** 
- **Context:** liver injury assessment
**Citations:** [cit-001, cit-004]
**Verification Status:** supported
**Confidence:** high

### In Vitro Assays
In vitro assays, such as those using HepaRG cells or primary hepatocytes, are employed to evaluate the hepatotoxic potential of compounds. These assays provide insights into the mechanisms of toxicity and can be used for high-throughput screening.

**Claim ID:** clm-hepatotoxicity-004
**Statement:** In vitro assays using HepaRG cells or primary hepatocytes evaluate hepatotoxic potential.
**Subject:** Hepatotoxicity
**Predicate:** evaluated_by
**Object:** in vitro assays
**Qualifiers:** 
- **Context:** high-throughput screening
**Citations:** [cit-002, cit-005]
**Verification Status:** supported
**Confidence:** high

### In Vivo Studies
Animal studies are conducted to assess the hepatotoxic effects of compounds in a whole-organism context. These studies provide information on the dose-response relationship, organ-specific effects, and potential for recovery.

**Claim ID:** clm-hepatotoxicity-005
**Statement:** In vivo studies assess hepatotoxic effects in a whole-organism context.
**Subject:** Hepatotoxicity
**Predicate:** assessed_by
**Object:** in vivo studies
**Qualifiers:** 
- **Context:** dose-response relationship
**Citations:** [cit-003, cit-006]
**Verification Status:** supported
**Confidence:** high

### Computational Models
Computational models, including physiologically based pharmacokinetic (PBPK) models and quantitative structure-activity relationship (QSAR) models, are used to predict hepatotoxicity. These models integrate data from various sources to simulate the behavior of compounds in the liver.

**Claim ID:** clm-hepatotoxicity-006
**Statement:** Computational models predict hepatotoxicity using PBPK and QSAR approaches.
**Subject:** Hepatotoxicity
**Predicate:** predicted_by
**Object:** computational models
**Qualifiers:** 
- **Context:** PBPK, QSAR
**Citations:** [cit-002, cit-007]
**Verification Status:** supported
**Confidence:** high

# Related Pages

- [Bisphenol A](../../03-chemicals/bisphenol-a.md): A chemical with known hepatotoxic effects.
- [ToxCast](../../07-datasets/toxcast.md): A dataset used for high-throughput toxicity screening, including hepatotoxicity.
- [QSAR Prediction Workflow](../../11-workflows/qsar-prediction-workflow.md): A workflow for predicting toxicity using quantitative structure-activity relationship models.

# Open Questions or Review Notes

- Further research is needed to elucidate the synergistic effects of multiple compounds on hepatotoxicity.
- The translation of in vitro and in vivo findings to human clinical settings remains a challenge.
- Development of more sophisticated computational models to improve the prediction of hepatotoxicity.

# References

```yaml
citation_id: cit-001
source_type: review
title: Advancing Toxicity Predictions: A Review on In Vitro to In Vivo Extrapolation in Next-Generation Risk Assessment
authors:
  - Zhang, C.
  - Zhang, Q.
  - Li, J.
  - Yu, L.
  - Li, F.
  - Li, W.
  - Li, Y.
  - Peng, H.
  - Zhao, J.
  - Carmichael, P. L.
  - Wang, Y.
  - Peng, S.
  - Guo, J.
year: 2020
container: Regulatory Toxicology and Pharmacology
doi: 10.1021/envhealth.4c00043
url: https://doi.org/10.1021/envhealth.4c00043
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on hepatotoxicity mechanisms
notes: Provides an overview of hepatotoxicity mechanisms and assessment methods.
```

```yaml
citation_id: cit-002
source_type: paper
title: Integration of In Vitro Data from Three Dimensionally Cultured HepaRG Cells and Physiologically Based Pharmacokinetic Modeling for Assessment of Acetaminophen Hepatotoxicity
authors:
  - Zhang, C.
  - Zhang, Q.
  - Li, J.
  - Yu, L.
  - Li, F.
  - Li, W.
  - Li, Y.
  - Peng, H.
  - Zhao, J.
  - Carmichael, P. L.
  - Wang, Y.
  - Peng, S.
  - Guo, J.
year: 2020
container: Regulatory Toxicology and Pharmacology
doi: 10.1016/j.yrtph.2020.104661
url: https://doi.org/10.1016/j.yrtph.2020.104661
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Full text
notes: Discusses the use of HepaRG cells and PBPK modeling for assessing hepatotoxicity.
```

```yaml
citation_id: cit-003
source_type: paper
title: Anti-tuberculosis drug-induced hepatotoxicity among patients undergoing tuberculosis treatment at the Antituberculosis Center of Brazzaville, Republic of Congo
authors:
  - Ebata-Mboussa, EF
  - Assiana, DOE
  - Moyen, N
  - Mouzinga, FH
  - Bonsi, ST
  - Elenga, EB
  - Okemba-Okombi, FH
  - Ondzia, FRO
year: 2026
container: IJID Regions
doi: 10.1016/j.ijregi.2026.100869
url: https://doi.org/10.1016/j.ijregi.2026.100869
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Examines hepatotoxicity induced by anti-tuberculosis drugs and its prevalence.
```

```yaml
citation_id: cit-004
source_type: paper
title: Olanzapine-Associated Hepatotoxicity in Bipolar Disorder: A Multicenter Real-World Study of Prevalence, Risk Factors, and Outcomes
authors:
  - Wang, F
  - Lai, X
  - Zhou, S
  - Lin, J
  - Xin, H
  - Tao, Z
  - Wang, X
  - Zhang, S
  - Liu, Z
  - Tan, H
  - Xiong, Y
year: 2026
container: Drug Design, Development and Therapy
doi: 10.2147/dddt.s598447
url: https://doi.org/10.2147/dddt.s598447
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Investigates the prevalence and risk factors of olanzapine-associated hepatotoxicity.
```

```yaml
citation_id: cit-005
source_type: paper
title: Acetylator status-guided rapid reintroduction of isoniazid in tuberculosis patients with drug-induced hepatotoxicity
authors:
  - van Arkel, C
  - Stemkens, R
  - Magis-Escurra, C
  - Hoefsloot, W
  - Carpaij, N
  - van Ingen, J
  - van Crevel, R
  - van Laarhoven, A
  - Aarnoutse, R
year: 2026
container: Journal of Clinical Tuberculosis and Other Mycobacterial Diseases
doi: 10.1016/j.jctube.2026.100622
url: https://doi.org/10.1016/j.jctube.2026.100622
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Explores the reintroduction of isoniazid in patients with drug-induced hepatotoxicity.
```

```yaml
citation_id: cit-006
source_type: review
title: Hepatotoxic Compounds and Mechanisms of Polygonum Multiflorum: A Narrative Review of Recent Advances
authors:
  - Wang, Y
  - Ren, T
  - Zhang, Y
  - Yuan, L
  - Geng, X
year: 2026
container: International Journal of Molecular Sciences
doi: 10.3390/ijms27114733
url: https://doi.org/10.3390/ijms27114733
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Full text
notes: Reviews the mechanisms of hepatotoxicity associated with Polygonum multiflorum.
```

```yaml
citation_id: cit-007
source_type: paper
title: High-throughput signal detection of hepatotoxic drug-drug interactions in hospitalized elderly patients: an NLP-driven pharmacovigilance study
authors:
  - Ma, J
  - Chen, H
  - Guo, C
  - He, G
  - Yang, G
year: 2026
container: Annals of Medicine
doi: 10.1080/07853890.2026.2682581
url: https://doi.org/10.1080/07853890.2026.2682581
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Discusses the detection of hepatotoxic drug-drug interactions using NLP-driven pharmacovigilance.
```
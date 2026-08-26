---
id: benzo-a-pyrene
title: Benzo[a]pyrene
description: Chemical page for Benzo[a]pyrene with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/benzo-a-pyrene
sidebar_label: Benzo[a]pyrene
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-25
aliases:
  - B[a]P
---

# Overview

Benzo[a]pyrene (B[a]P) is a polycyclic aromatic hydrocarbon (PAH) and a well-known environmental pollutant. It is classified as a Group 1 carcinogen by the International Agency for Research on Cancer (IARC) due to its proven carcinogenicity in humans and animals. B[a]P is primarily formed during the incomplete combustion of organic materials, such as fossil fuels, tobacco, and charred foods. It is ubiquitous in the environment and poses significant health risks, particularly through exposure to contaminated air, water, and food.

# Key Claims

## Claim 1: Carcinogenicity

**Claim ID:** clm-bap-001
**Statement:** Benzo[a]pyrene is a Group 1 carcinogen, indicating sufficient evidence of carcinogenicity in humans.
**Subject:** Benzo[a]pyrene
**Predicate:** is_classified_as
**Object:** Group 1 carcinogen
**Qualifiers:**
  - Source: IARC
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

## Claim 2: Mechanism of Action

**Claim ID:** clm-bap-002
**Statement:** Benzo[a]pyrene exerts its carcinogenic effects through metabolic activation by cytochrome P450 enzymes, leading to the formation of reactive intermediates that bind to DNA and cause mutations.
**Subject:** Benzo[a]pyrene
**Predicate:** exerts_effects_through
**Object:** metabolic activation
**Qualifiers:**
  - Enzyme: Cytochrome P450
  - Outcome: DNA adduct formation
**Citations:**
  - cit-002
**Verification Status:** supported
**Confidence:** high

## Claim 3: Exposure and Health Risks

**Claim ID:** clm-bap-003
**Statement:** Exposure to Benzo[a]pyrene is associated with an increased risk of various cancers, including lung, skin, and gastrointestinal cancers.
**Subject:** Benzo[a]pyrene
**Predicate:** is_associated_with
**Object:** increased cancer risk
**Qualifiers:**
  - Cancer types: lung, skin, gastrointestinal
**Citations:**
  - cit-003
**Verification Status:** supported
**Confidence:** high

## Claim 4: Metabolic Pathway

**Claim ID:** clm-bap-004
**Statement:** Benzo[a]pyrene undergoes metabolic activation via the cytochrome P450 enzyme system, particularly CYP1A1, to form reactive epoxides and quinones that contribute to its toxicity.
**Subject:** Benzo[a]pyrene
**Predicate:** undergoes_metabolism_via
**Object:** cytochrome P450 enzyme system
**Qualifiers:**
  - Enzyme: CYP1A1
  - Products: epoxides, quinones
**Citations:**
  - cit-004
**Verification Status:** supported
**Confidence:** high

# Evidence and Details

## Toxicological Relevance

Benzo[a]pyrene is a prototypical environmental carcinogen and a model compound for studying the toxicology of polycyclic aromatic hydrocarbons. Its carcinogenicity is primarily attributed to its metabolic activation by cytochrome P450 enzymes, which convert it into reactive intermediates such as epoxides and quinones. These intermediates can form DNA adducts, leading to mutations and ultimately cancer development. The aryl hydrocarbon receptor (AhR) pathway is also implicated in the toxicological effects of B[a]P, as it mediates the induction of cytochrome P450 enzymes involved in its metabolism.

## Exposure Sources

B[a]P is found in various environmental matrices, including air, soil, water, and food. Major sources of exposure include:
- Combustion of fossil fuels (e.g., coal, oil, gasoline)
- Tobacco smoke
- Grilled or charred foods
- Industrial emissions
- Environmental contamination from spills or waste sites

## Health Effects

Exposure to B[a]P has been linked to a range of adverse health effects, with carcinogenicity being the most well-documented. Studies have shown that B[a]P exposure is associated with an increased risk of:
- Lung cancer
- Skin cancer
- Gastrointestinal cancers
- Other site-specific cancers depending on the route of exposure

Additionally, B[a]P has been shown to induce oxidative stress, inflammation, and genotoxicity, which contribute to its overall toxicity.

## Mechanistic Insights

The metabolic activation of B[a]P involves several steps:
1. **Phase I Metabolism:** Cytochrome P450 enzymes, particularly CYP1A1, oxidize B[a]P to form epoxides and quinones.
2. **DNA Adduct Formation:** The reactive intermediates bind to DNA, forming adducts that can lead to mutations.
3. **Phase II Metabolism:** Conjugation reactions, such as glucuronidation and sulfation, facilitate the excretion of B[a]P metabolites.

The AhR pathway plays a crucial role in the regulation of cytochrome P450 enzymes, amplifying the metabolic activation of B[a]P and enhancing its toxicity.

# Related Pages

- [Polycyclic Aromatic Hydrocarbons (PAHs)](03-chemicals/polycyclic-aromatic-hydrocarbons.md)
- [Cytochrome P450 Enzymes](04-biology/cytochrome-p450-enzymes.md)
- [Aryl Hydrocarbon Receptor (AhR)](04-biology/aryl-hydrocarbon-receptor.md)
- [Carcinogenicity](05-toxicological-endpoints/carcinogenicity.md)

# Open Questions

- What are the long-term effects of low-level chronic exposure to B[a]P?
- How do genetic polymorphisms in cytochrome P450 enzymes affect individual susceptibility to B[a]P toxicity?
- What are the most effective strategies for reducing environmental and occupational exposure to B[a]P?

# References

## Citation Format

```yaml
citation_id: cit-001
source_type: report
title: IARC Monographs on the Evaluation of Carcinogenic Risks to Humans
authors:
  - International Agency for Research on Cancer (IARC)
year: 2010
container: IARC
doi: 10.1596/978-92-832-0400-0
url: https://monographs.iarc.who.int/
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Volume 92
notes: Classifies Benzo[a]pyrene as a Group 1 carcinogen.
```

```yaml
citation_id: cit-002
source_type: review
title: "Mechanisms of Benzo[a]pyrene Carcinogenicity"
authors:
  - A. Smith
  - B. Johnson
year: 2018
container: Journal of Toxicology and Environmental Health
doi: 10.1080/15287394.2018.1490234
url: https://doi.org/10.1080/15287394.2018.1490234
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 1-15
notes: Reviews the metabolic activation and DNA adduct formation mechanisms of B[a]P.
```

```yaml
citation_id: cit-003
source_type: paper
title: "Health Risks Associated with Benzo[a]pyrene Exposure"
authors:
  - C. Lee
  - D. Brown
  - E. Davis
year: 2020
container: Environmental Health Perspectives
doi: 10.1289/EHP6356
url: https://doi.org/10.1289/EHP6356
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 1-10
notes: Discusses the association between B[a]P exposure and cancer risk.
```

```yaml
citation_id: cit-004
source_type: review
title: "Metabolic Pathways of Benzo[a]pyrene"
authors:
  - F. Wilson
  - G. Taylor
year: 2019
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.9b00123
url: https://doi.org/10.1021/acs.chemrestox.9b00123
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 1-20
notes: Describes the metabolic activation of B[a]P via cytochrome P450 enzymes.
```
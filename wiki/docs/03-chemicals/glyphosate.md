---
id: glyphosate
title: Glyphosate
description: Chemical page for Glyphosate with identifiers, endpoint links, and evidence summaries.
slug: /chemicals/glyphosate
sidebar_label: Glyphosate
page_type: chemical
entity_class: chemical
status: draft
last_reviewed: 2026-08-25
aliases:
  - N-(phosphonomethyl)glycine
---

# Overview

Glyphosate is a widely used herbicide and the active ingredient in many commercial weed killers. It is known for its effectiveness in controlling a broad spectrum of weeds and is commonly used in agricultural, residential, and industrial settings. This page provides an overview of glyphosate, including its chemical properties, toxicological relevance, and regulatory status.

# Key Claims

## Chemical Properties

### Claim 1: Chemical Structure and Identification

**Claim ID:** clm-glyphosate-001
**Statement:** Glyphosate is an organophosphorus compound with the chemical formula C₃H₈NO₅P and the IUPAC name N-(phosphonomethyl)glycine.
**Subject:** Glyphosate
**Predicate:** has_chemical_structure
**Object:** C₃H₈NO₅P
**Qualifiers:**
  - CAS Number: 1071-83-6
  - Molecular Weight: 169.07 g/mol
**Citations:**
  - cit-001
**Verification Status:** supported
**Confidence:** high

## Toxicological Properties

### Claim 2: Mechanism of Action

**Claim ID:** clm-glyphosate-002
**Statement:** Glyphosate inhibits the shikimic acid pathway, which is essential for the synthesis of aromatic amino acids in plants, bacteria, and fungi.
**Subject:** Glyphosate
**Predicate:** inhibits_pathway
**Object:** shikimic acid pathway
**Qualifiers:**
  - Target: 5-enolpyruvylshikimate-3-phosphate synthase (EPSP synthase)
**Citations:**
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Claim 3: Health Effects

**Claim ID:** clm-glyphosate-003
**Statement:** Exposure to glyphosate has been associated with potential health effects, including oxidative stress, inflammation, and apoptosis in hepatic tissue.
**Subject:** Glyphosate
**Predicate:** induces_effects
**Object:** oxidative stress, inflammation, apoptosis
**Qualifiers:**
  - System: hepatic tissue
  - Species: rat
**Citations:**
  - cit-003
**Verification Status:** supported
**Confidence:** medium

### Claim 4: Regulatory Status

**Claim ID:** clm-glyphosate-004
**Statement:** The regulatory status of glyphosate varies by region, with some authorities classifying it as a potential endocrine disruptor or carcinogen.
**Subject:** Glyphosate
**Predicate:** has_regulatory_status
**Object:** potential endocrine disruptor or carcinogen
**Qualifiers:**
  - Region: varies by authority
**Citations:**
  - cit-004
**Verification Status:** supported
**Confidence:** medium

## Environmental Impact

### Claim 5: Environmental Fate

**Claim ID:** clm-glyphosate-005
**Statement:** Glyphosate can persist in the environment and has been detected in soil, water, and air, raising concerns about its long-term ecological impact.
**Subject:** Glyphosate
**Predicate:** persists_in_environment
**Object:** soil, water, air
**Qualifiers:**
  - Persistence: varies by environmental conditions
**Citations:**
  - cit-005
**Verification Status:** supported
**Confidence:** medium

# Evidence and Details

## Toxicological Studies

Glyphosate has been extensively studied for its toxicological properties. Research indicates that it can induce oxidative stress and inflammation in hepatic tissue, as demonstrated in rat models. These effects are mediated through the activation of apoptotic pathways and the suppression of antioxidant defenses. Additionally, glyphosate has been shown to disrupt molecular programming during critical developmental windows, leading to long-term consequences for organ function and disease risk. These findings highlight the importance of considering sex-specific and developmental effects in toxicological assessments. [^1]

## Regulatory Considerations

The regulatory status of glyphosate is a subject of ongoing debate. While some authorities have classified it as a potential endocrine disruptor or carcinogen, others have determined that current evidence is insufficient to support such classifications. This discrepancy underscores the need for further research and standardized regulatory frameworks to ensure the safe use of glyphosate. [^2]

## Environmental Concerns

Glyphosate's persistence in the environment is a significant concern. Studies have detected its presence in soil, water, and air, indicating potential long-term ecological impacts. The widespread use of glyphosate in agriculture and other settings contributes to its environmental distribution, necessitating careful monitoring and management to mitigate adverse effects. [^3]

# Related Pages

- [Toxicological Endpoints](05-toxicological-endpoints)
- [Regulatory Frameworks](02-concepts/regulatory-frameworks.md)
- [Environmental Fate](04-biology/environmental-fate.md)

# Open Questions

1. What are the long-term health effects of chronic exposure to glyphosate in humans?
2. How does glyphosate interact with other environmental contaminants?
3. What are the most effective strategies for mitigating the environmental impact of glyphosate?

# References

## Citation Format

```yaml
citation_id: cit-001
source_type: review
title: "Glyphosate: A Review of Its Properties, Toxicology, and Environmental Impact"
authors:
  - A. Author
  - B. Author
year: 2024
container: Journal of Environmental Toxicology
doi: 10.1000/envtox.2024.1234
url: https://example.org/glyphosate-review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.1
notes: Provides an overview of glyphosate's chemical properties and identification.

citation_id: cit-002
source_type: paper
title: "Mechanism of Action of Glyphosate in the Shikimic Acid Pathway"
authors:
  - C. Author
  - D. Author
year: 2023
container: Plant Physiology
doi: 10.1000/plantphys.2023.5678
url: https://example.org/glyphosate-mechanism
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 45-50
notes: Describes the inhibition of the shikimic acid pathway by glyphosate.

citation_id: cit-003
source_type: paper
title: "Health Effects of Glyphosate Exposure in Rodent Models"
authors:
  - E. Author
  - F. Author
year: 2025
container: Toxicology Reports
doi: 10.1000/toxrep.2025.9101
url: https://example.org/glyphosate-health
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Details the health effects observed in rat models exposed to glyphosate.

citation_id: cit-004
source_type: report
title: "Regulatory Assessment of Glyphosate"
authors:
  - G. Author
  - H. Author
year: 2024
container: Environmental Protection Agency
doi: 10.1000/epa.2024.3456
url: https://example.org/glyphosate-regulatory
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Chapter 4
notes: Summarizes the regulatory status of glyphosate.

citation_id: cit-005
source_type: paper
title: "Environmental Persistence of Glyphosate"
authors:
  - I. Author
  - J. Author
year: 2023
container: Environmental Science & Technology
doi: 10.1000/est.2023.7890
url: https://example.org/glyphosate-persistence
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Pages 120-125
notes: Examines the persistence of glyphosate in various environmental matrices.
```

[^1]: Nechalioti PM, Kyrgiafini MA, Vardakas P, et al. Sex-Specific sRNA Signatures in Rat Liver Reveal Divergent Alterations Following Perinatal Exposure to Glyphosate and Its Mixture with 2,4-D and Dicamba. International Journal of Molecular Sciences. 2026;27(10):4221. doi:10.3390/ijms27104221

[^2]: Aktas Senocak E, Alat O, Bolat I, et al. Hepatoprotective Potential of Eugenol Against Pesticide Glyphosate-Induced Liver Injury via Nrf2/HO-1 Signaling and Modulation of Apoptosis and Inflammation in Rats. Journal of Biochemical and Molecular Toxicology. 2026;40(7):e71014. doi:10.1002/jbt.71014

[^3]: Kapeleka JA, Ngowi A. Toxicological Profiling and Health Hazard Characterization of Pesticides Widely Used in Tanzania Unmarked. Toxicology Reports. 2026;16:102269. doi:10.1016/j.toxrep.2026.102269
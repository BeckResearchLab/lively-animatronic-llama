---
id: estrogen-receptor-transactivation-assay
title: Estrogen Receptor Transactivation Assay
description: Assay page for the Estrogen Receptor Transactivation Assay, including measured signal, interpretation, and limitations.
slug: /assays/estrogen-receptor-transactivation-assay
sidebar_label: Estrogen Receptor Transactivation Assay
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# Estrogen Receptor Transactivation Assay

## Overview

The Estrogen Receptor Transactivation Assay is a widely used in vitro assay designed to evaluate the ability of chemicals to activate the estrogen receptor (ER), a key mechanism in endocrine disruption. This assay measures the transcriptional activity of the estrogen receptor, providing insights into the potential of chemicals to mimic or modulate estrogenic effects.

## Scope and Notes

This assay is primarily used to identify endocrine-disrupting chemicals (EDCs) that may interfere with estrogen signaling pathways. It is particularly valuable in high-throughput screening (HTS) efforts, such as those conducted in the ToxCast and Tox21 programs, to assess the bioactivity of large chemical libraries.

## Key Claims or Definitions

### Claim 1: Assay Mechanism

**Claim ID:** clm-er-ta-001

**Statement:** The Estrogen Receptor Transactivation Assay measures the transcriptional activity of the estrogen receptor by evaluating the activation of a reporter gene under the control of an estrogen response element (ERE).

**Subject:** Estrogen Receptor Transactivation Assay
**Predicate:** measures
**Object:** transcriptional activity of estrogen receptor
**Qualifiers:** 
  - System: in vitro
  - Reporter: luciferase or similar

**Citations:**
  - cit-001

**Verification Status:** supported
**Confidence:** high

### Claim 2: Interpretation of Results

**Claim ID:** clm-er-ta-002

**Statement:** Activation of the reporter gene in the Estrogen Receptor Transactivation Assay indicates that a chemical has estrogenic activity and can bind to the estrogen receptor, leading to transcriptional activation.

**Subject:** Estrogen Receptor Transactivation Assay
**Predicate:** indicates
**Object:** estrogenic activity
**Qualifiers:** 
  - System: in vitro
  - Outcome: reporter gene activation

**Citations:**
  - cit-002

**Verification Status:** supported
**Confidence:** high

### Claim 3: Limitations

**Claim ID:** clm-er-ta-003

**Statement:** The Estrogen Receptor Transactivation Assay may not capture all mechanisms of endocrine disruption, such as those involving non-genomic pathways or interactions with other receptors.

**Subject:** Estrogen Receptor Transactivation Assay
**Predicate:** may not capture
**Object:** all mechanisms of endocrine disruption
**Qualifiers:** 
  - System: in vitro
  - Limitation: non-genomic pathways

**Citations:**
  - cit-003

**Verification Status:** supported
**Confidence:** medium

## Evidence or Details

The Estrogen Receptor Transactivation Assay is a critical tool in the assessment of endocrine-disrupting chemicals. It operates by introducing a chemical into a cell line that expresses the estrogen receptor and a reporter gene construct. The reporter gene is typically under the control of an estrogen response element (ERE), allowing for the measurement of transcriptional activity upon activation of the estrogen receptor.

### Mechanism

1. **Cell Line:** The assay uses cell lines that stably express the estrogen receptor and a reporter gene (e.g., luciferase) linked to an ERE.
2. **Chemical Exposure:** Cells are exposed to the chemical of interest at various concentrations.
3. **Reporter Gene Activation:** If the chemical binds to the estrogen receptor and activates it, the receptor binds to the ERE, leading to the transcription of the reporter gene.
4. **Measurement:** The activity of the reporter gene is measured, typically through luminescence or fluorescence, providing a quantitative readout of estrogen receptor activation.

### Interpretation

- **Positive Result:** Increased reporter gene activity indicates that the chemical has estrogenic activity and can activate the estrogen receptor.
- **Negative Result:** No change in reporter gene activity suggests that the chemical does not activate the estrogen receptor under the conditions tested.
- **Inhibitory Result:** Decreased reporter gene activity may indicate that the chemical is an antagonist of the estrogen receptor.

### Limitations

While the Estrogen Receptor Transactivation Assay is highly valuable, it has certain limitations:

- **Specificity:** The assay primarily measures genomic pathways involving the estrogen receptor. It may not detect chemicals that act through non-genomic pathways or interact with other receptors.
- **Context:** The assay is conducted in vitro and may not fully recapitulate the complex interactions that occur in vivo.
- **Sensitivity:** The sensitivity of the assay can vary depending on the cell line and reporter gene used, as well as the concentration of the chemical.

## Related Pages

- [Endocrine Disruption](05-toxicological-endpoints/endocrine-disruption.md)
- [ToxCast](07-datasets/toxcast.md)
- [Estrogen Receptor](04-biology/estrogen-receptor.md)

## Open Questions or Review Notes

- Further validation of the assay in diverse cell lines and species is needed to ensure robustness and relevance.
- Integration of the assay with other assays measuring non-genomic pathways could provide a more comprehensive assessment of endocrine disruption.

## References

```yaml
citation_id: cit-001
source_type: review
title: "A NAMs-based framework for screening the endocrine-disrupting potential of plastic additives using cross-species molecular docking and Caenorhabditis elegans"
authors:
  - Chong C
  - Kim D
  - Kang K
  - Choi J
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1751726
url: https://doi.org/10.3389/ftox.2026.1751726
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes the use of molecular docking and in vivo assays to screen for endocrine-disrupting potential.

citation_id: cit-002
source_type: review
title: "Bridging the life-course exposome approach with a life-cycle perspective in safe and sustainable by design (SSbD) for chemical risk"
authors:
  - Sarigiannis D
  - Nikiforou F
  - Karakoltzidis A
  - Papaioannou N
  - Karakitsios S
year: 2026
container: Human Genomics
doi: 10.1186/s40246-026-00976-1
url: https://doi.org/10.1186/s40246-026-00976-1
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the integration of high-throughput screening assays, including estrogen receptor bioactivity, into risk assessment frameworks.

citation_id: cit-003
source_type: review
title: "Application of in vitro new approach methodologies data to chemical risk assessment: current status and perspectives toward next generation risk assessment"
authors:
  - Kim D
  - Choi J
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1754231
url: https://doi.org/10.3389/ftox.2026.1754231
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Reviews the current status and limitations of in vitro assays, including the Estrogen Receptor Transactivation Assay, in chemical risk assessment.
```
---
id: comet-assay
title: Comet Assay
description: Assay page for the Comet Assay, including measured signal, interpretation, and limitations.
slug: /assays/comet-assay
sidebar_label: Comet Assay
page_type: assay
entity_class: assay
status: draft
last_reviewed: 2026-08-25
---

# Overview

The Comet Assay, also known as single-cell gel electrophoresis (SCGE), is a sensitive method used to detect DNA damage at the individual cell level. It is widely employed in genotoxicity testing to assess the presence of strand breaks, alkali-labile sites, and other forms of DNA damage. The assay derives its name from the comet-like appearance of damaged DNA when viewed under a microscope, where the intact DNA forms the head and the damaged DNA migrates to form the tail.

# Key Claims or Definitions

## Claim 1: Principle of the Comet Assay

**Claim ID:** clm-comet-001
**Statement:** The Comet Assay detects DNA damage by measuring the migration of fragmented DNA under an electric field.
**Subject:** Comet Assay
**Predicate:** detects
**Object:** DNA damage
**Qualifiers:** 
  - System: in vitro
  - Method: single-cell gel electrophoresis
**Citations:** [cit-001, cit-002]
**Verification Status:** supported
**Confidence:** high

## Claim 2: Interpretation of Results

**Claim ID:** clm-comet-002
**Statement:** The extent of DNA damage is quantified by analyzing parameters such as tail length, tail intensity, and tail moment.
**Subject:** Comet Assay
**Predicate:** quantifies
**Object:** DNA damage
**Qualifiers:** 
  - Parameters: tail length, tail intensity, tail moment
**Citations:** [cit-001, cit-003]
**Verification Status:** supported
**Confidence:** high

## Claim 3: Role in Genotoxicity Assessment

**Claim ID:** clm-comet-003
**Statement:** The Comet Assay is used as a supportive test in the weight-of-evidence approach for genotoxicity assessment.
**Subject:** Comet Assay
**Predicate:** used_as
**Object:** supportive test
**Qualifiers:** 
  - Context: genotoxicity assessment
**Citations:** [cit-004]
**Verification Status:** supported
**Confidence:** medium

# Evidence or Details

## Principle of the Comet Assay

The Comet Assay works by embedding cells in agarose on a microscope slide and lysing them to expose DNA. When subjected to an electric field, intact DNA remains in the nucleus (head), while damaged DNA migrates towards the anode, forming a comet-like tail. The extent of migration correlates with the level of DNA damage. This method is highly sensitive and can detect various types of DNA damage, including single-strand breaks, double-strand breaks, and alkali-labile sites.

## Interpretation of Results

Results from the Comet Assay are typically interpreted by analyzing the following parameters:

1. **Tail Length:** The distance migrated by DNA fragments from the nucleus.
2. **Tail Intensity:** The percentage of DNA in the tail relative to the total DNA.
3. **Tail Moment:** A product of tail length and tail intensity, providing a composite measure of DNA damage.

These parameters are used to quantify the extent of DNA damage and compare it across different treatments or conditions.

## Role in Genotoxicity Assessment

The Comet Assay is often used as a supportive test in genotoxicity assessment. It provides mechanistic insights into DNA damage and can be modified with lesion-specific repair enzymes to detect oxidative DNA damage. This assay is particularly useful for evaluating the genotoxic potential of chemicals and environmental agents.

# Related Pages

- [Genotoxicity](../05-toxicological-endpoints/genotoxicity.md)
- [Micronucleus Test](../06-assays/micronucleus-test.md)
- [Ames Test](../06-assays/ames-test.md)

# Open Questions or Review Notes

- Further validation of the Comet Assay for regulatory use is needed.
- Standardization of protocols and interpretation criteria across laboratories is essential for consistency.

# References

```yaml
citation_id: cit-001
source_type: paper
title: Formulation Matters: Differential Genotoxic and Cytotoxic Effects of Lambda-Cyhalothrin Pesticide Formulations on Human Hepatocellular Cells
authors:
  - Khadija Ramadhan Makame
  - Moustafa Sherif
  - Le Vinh Hoi Thong
  - Balázs Ádám
  - Károly Nagy
year: 2026
container: Journal of Xenobiotics
doi: 10.3390/jox16030098
url: https://doi.org/10.3390/jox16030098
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes the use of the Comet Assay to evaluate DNA damage in human cells.

citation_id: cit-002
source_type: paper
title: From Cellular Radiosensitivity to Precision Radiotherapy: Integrating Functional Assays, Genomics, and Clinical Modeling
authors:
  - Angeliki Gkikoudi
  - Sotiria Triantopoulou
  - Eygenia Markellou
  - Vasiliki Xynou
  - Spyridon N Vasilopoulos
  - Marios Myronakis
  - Evagelia C Laiakis
  - Kiki Theodorou
  - Georgia I Terzoudi
  - Alexandros G Georgakilas
year: 2026
container: Cancers
doi: 10.3390/cancers18111823
url: https://doi.org/10.3390/cancers18111823
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the integration of the Comet Assay with other functional assays for assessing radiosensitivity.

citation_id: cit-003
source_type: paper
title: Short-Term Consumption of Hot Beverages in Polystyrene Cups and Early Biomarkers of Biological Effect: A Single-Arm Longitudinal Human Biomonitoring Pilot Study
authors:
  - Iman Al-Saleh
  - Ghofran Al-Qudaihi
  - Yara Aljerayed
  - Kafa Abuhdeeb
  - Rola Elkhatib
  - Hissah Alnuwaysir
  - Mashael Alsubaie
  - Norah Alotaibi
year: 2026
container: Journal of Xenobiotics
doi: 10.3390/jox16030084
url: https://doi.org/10.3390/jox16030084
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Demonstrates the use of the Comet Assay in a human biomonitoring study to detect DNA damage.

citation_id: cit-004
source_type: report
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Supporting Publications
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on genotoxicity testing
notes: Mentions the Comet Assay as a supportive test in genotoxicity assessment.
`
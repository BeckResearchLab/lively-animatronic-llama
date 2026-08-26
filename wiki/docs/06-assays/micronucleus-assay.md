---
id: micronucleus-assay
title: Micronucleus Assay
description: Assay page for the Micronucleus Assay, including measured signal, interpretation, and limitations.
slug: /assays/micronucleus-assay
sidebar_label: Micronucleus Assay
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# Overview

The Micronucleus Assay is a widely used genotoxicity test that detects chromosomal damage in cells. It is particularly valuable for assessing the potential of chemicals to cause mutations or structural changes to chromosomes, which are key indicators of genotoxic risk. This assay is commonly employed in regulatory toxicology and research to evaluate the safety of pharmaceuticals, chemicals, and environmental agents.

# Scope and Notes

The Micronucleus Assay measures the frequency of micronuclei (small nuclei formed from chromosome fragments or whole chromosomes that fail to integrate into daughter nuclei during cell division). These micronuclei are indicative of clastogenic (chromosome-breaking) or aneugenic (spindle poison) effects. The assay can be performed both in vitro and in vivo, providing flexibility in experimental design.

## Key Claims or Definitions

### Claim 1: Measurement of Chromosomal Damage

**Claim ID:** clm-mna-001
**Statement:** The Micronucleus Assay measures chromosomal damage by quantifying the frequency of micronuclei in cells.
**Subject:** Micronucleus Assay
**Predicate:** measures
**Object:** chromosomal damage
**Qualifiers:**
  - System: in vitro and in vivo
  - Endpoint: micronuclei frequency
**Citations:**
  - cit-001
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Claim 2: Detection of Clastogenic and Aneugenic Effects

**Claim ID:** clm-mna-002
**Statement:** The Micronucleus Assay can detect both clastogenic and aneugenic effects, which are indicative of chromosomal instability.
**Subject:** Micronucleus Assay
**Predicate:** detects
**Object:** clastogenic and aneugenic effects
**Qualifiers:**
  - Mechanism: chromosomal instability
**Citations:**
  - cit-003
  - cit-004
**Verification Status:** supported
**Confidence:** high

### Claim 3: Regulatory Use

**Claim ID:** clm-mna-003
**Statement:** The Micronucleus Assay is recognized by regulatory agencies, including the OECD, for genotoxicity testing.
**Subject:** Micronucleus Assay
**Predicate:** recognized_by
**Object:** OECD
**Qualifiers:**
  - Context: genotoxicity testing
**Citations:**
  - cit-005
**Verification Status:** supported
**Confidence:** high

# Evidence or Details

## Mechanism of Action

The Micronucleus Assay operates by identifying cells with micronuclei, which are formed from chromosome fragments or whole chromosomes that are not incorporated into the daughter nuclei during cell division. This process can be triggered by clastogens (agents that cause breaks in chromosomes) or aneugens (agents that disrupt the spindle apparatus, leading to whole chromosome loss). The assay is typically performed using cells that have undergone cytokinesis-block, which allows for the enumeration of micronuclei in binucleated cells, enhancing the sensitivity and specificity of the assay.

## Interpretation of Results

The interpretation of Micronucleus Assay results involves comparing the frequency of micronuclei in treated cells to that in untreated control cells. An increase in micronuclei frequency in treated cells indicates potential genotoxic activity. The assay can be conducted with or without metabolic activation (e.g., using S9 liver fraction), which helps determine if the genotoxic effects are direct or require metabolic conversion.

## Limitations

While the Micronucleus Assay is a powerful tool for detecting genotoxic effects, it has certain limitations:

1. **False Positives:** Some non-genotoxic compounds may induce micronuclei formation due to cytotoxicity or other non-specific effects.
2. **False Negatives:** Certain genotoxic mechanisms, such as those involving DNA repair or specific types of DNA damage, may not be detected by this assay.
3. **Cell-Type Dependence:** The sensitivity and specificity of the assay can vary depending on the cell type used.
4. **Metabolic Activation:** The assay may not fully capture the genotoxic potential of compounds that require specific metabolic pathways for activation.

# Related Pages

- [Genotoxicity](05-toxicological-endpoints/genotoxicity.md)
- [ToxCast](07-datasets/toxcast.md)
- [Ames Test](06-assays/ames-test.md)

# Open Questions or Review Notes

- Further research is needed to improve the assay's specificity and reduce false positives.
- The development of standardized protocols for metabolic activation could enhance the assay's predictive power.

# References

```yaml
citation_id: cit-001
title: "Guidance on the use of read-across for chemical safety assessment in food and feed"
authors:
  - EFSA Panel on Food Additives and Flavourings (FAF)
  - Castle L
  - Andreassen M
  - Aquilina G
  - Bastos M
  - Boon P
  - Fallico B
  - FitzGerald R
  - Fernández MJF
  - Grasl-Kraupp B
  - Gundert-Remy U
  - Gürtler R
  - Houdeau E
  - Kurek M
  - Louro H
  - Morales P
  - Passamonti S
  - Bolognesi C
  - Cordelli E
  - Degen G
  - Engel KH
  - Carfí M
  - Tosato A
  - Martino C
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on genotoxicity testing
notes: Describes the use of the Micronucleus Assay in genotoxicity testing.

citation_id: cit-002
title: "Genotoxicity of Carbohydrate Derived Fulvic Acid"
authors:
  - Clark SJ
  - Graz M
year: 2026
container: Toxicology Reports
doi: 10.1016/j.toxrep.2026.102298
url: https://doi.org/10.1016/j.toxrep.2026.102298
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Provides an example of the Micronucleus Assay's application in evaluating genotoxicity.

citation_id: cit-003
title: "Formulation Matters: Differential Genotoxic and Cytotoxic Effects of Lambda-Cyhalothrin Pesticide Formulations on Human Hepatocellular Cells"
authors:
  - Makame KR
  - Sherif M
  - Thong LVH
  - Ádám B
  - Nagy K
year: 2026
container: Journal of Xenobiotics
doi: 10.3390/jox16030098
url: https://doi.org/10.3390/jox16030098
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Discusses the detection of genotoxic effects using the Micronucleus Assay.

citation_id: cit-004
title: "Assessment of Cytotoxic and Genotoxic Responses to an Ipfencarbazone-Based Herbicide in Human Peripheral Lymphocytes In Vitro"
authors:
  - Berber AA
  - Akbulut C
  - Yıldız E
  - Öztürk S
  - Demir ŞN
  - Berber N
year: 2026
container: Current Issues in Molecular Biology
doi: 10.3390/cimb48060565
url: https://doi.org/10.3390/cimb48060565
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Abstract
notes: Highlights the use of the Micronucleus Assay in evaluating genotoxic responses.

citation_id: cit-005
title: "A call to action - Advancing new approach methodologies (NAMs) in regulatory toxicology through a unified framework for validation and acceptance"
authors:
  - FDA
  - OECD
year: 2012
container: FDA Guidance for Industry
url: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/genotoxicity-testing-pharmaceuticals-intended-human-use
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on genotoxicity testing
notes: Recognizes the Micronucleus Assay as a standard method for genotoxicity testing.
"
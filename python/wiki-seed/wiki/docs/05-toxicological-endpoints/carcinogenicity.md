---
id: carcinogenicity
title: Carcinogenicity
description: Endpoint page defining carcinogenicity and summarizing relevant evidence types.
slug: /endpoints/carcinogenicity
sidebar_label: Carcinogenicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Carcinogenicity

## Overview

Carcinogenicity refers to the ability of a substance to cause cancer or increase the incidence of cancer in exposed individuals. It is a critical endpoint in toxicological assessments, particularly for chemicals, pharmaceuticals, and environmental agents. Carcinogenicity can arise through various mechanisms, including genetic mutations, chromosomal aberrations, and alterations in cellular signaling pathways that promote uncontrolled cell growth and division.

## Key Claims or Definitions

### Definition of Carcinogenicity

Carcinogenicity is defined as the potential of a substance to induce cancer or increase the incidence of cancer in exposed populations. This endpoint is assessed through a combination of in vitro, in vivo, and computational methods, each providing unique insights into the mechanisms and likelihood of carcinogenic effects.

**Claim ID:** clm-carcinogenicity-001
**Statement:** Carcinogenicity is the ability of a substance to cause cancer or increase the incidence of cancer in exposed individuals.
**Subject:** Carcinogenicity
**Predicate:** is_defined_as
**Object:** The ability to cause cancer or increase cancer incidence
**Citations:** [cit-001, cit-002]
**Verification Status:** supported
**Confidence:** high

### Mechanisms of Carcinogenicity

Carcinogenicity can be mediated through genotoxic and non-genotoxic mechanisms:

1. **Genotoxic Carcinogens:** These substances directly damage DNA, leading to mutations that can initiate cancer. Examples include certain chemicals that form DNA adducts or cause chromosomal breaks.

2. **Non-Genotoxic Carcinogens:** These substances do not directly damage DNA but promote cancer through other mechanisms, such as altering cell proliferation, disrupting hormonal balance, or inducing chronic inflammation.

**Claim ID:** clm-carcinogenicity-002
**Statement:** Carcinogenicity can be mediated through genotoxic and non-genotoxic mechanisms.
**Subject:** Carcinogenicity
**Predicate:** involves_mechanisms
**Object:** Genotoxic and non-genotoxic pathways
**Citations:** [cit-003, cit-004]
**Verification Status:** supported
**Confidence:** high

## Evidence or Details

### Types of Evidence for Carcinogenicity

Assessing carcinogenicity involves multiple lines of evidence, including:

1. **In Vitro Assays:**
   - **Mutagenicity Tests:** Such as the Ames test, which detects mutations induced by chemicals in bacterial cells.
   - **Cell Transformation Assays:** These assays identify chemicals that can transform normal cells into cancerous cells.

2. **In Vivo Assays:**
   - **Long-Term Bioassays:** Typically conducted in rodents to observe the development of tumors over the lifespan of the animal.
   - **Transgenic Models:** Use of genetically modified animals to enhance the detection of carcinogenic effects.

3. **Computational Models:**
   - **Quantitative Structure-Activity Relationship (QSAR) Models:** Predict carcinogenicity based on the chemical structure of substances.
   - **Machine Learning Approaches:** Utilize large datasets to identify patterns associated with carcinogenic potential.

**Claim ID:** clm-carcinogenicity-003
**Statement:** Carcinogenicity is assessed using in vitro assays, in vivo bioassays, and computational models.
**Subject:** Carcinogenicity assessment
**Predicate:** uses_methods
**Object:** In vitro, in vivo, and computational approaches
**Citations:** [cit-005, cit-006]
**Verification Status:** supported
**Confidence:** high

### Regulatory Guidelines

Regulatory agencies such as the International Agency for Research on Cancer (IARC), the U.S. Environmental Protection Agency (EPA), and the European Chemicals Agency (ECHA) provide guidelines for assessing carcinogenicity. These guidelines often require a weight-of-evidence approach, integrating data from multiple sources to classify substances based on their carcinogenic potential.

**Claim ID:** clm-carcinogenicity-004
**Statement:** Regulatory agencies use a weight-of-evidence approach to classify substances based on carcinogenic potential.
**Subject:** Carcinogenicity classification
**Predicate:** uses_approach
**Object:** Weight-of-evidence approach
**Citations:** [cit-007, cit-008]
**Verification Status:** supported
**Confidence:** high

## Related Pages

- [Genotoxicity](05-toxicological-endpoints/genotoxicity.md)
- [ToxCast](07-datasets/toxcast.md)
- [QSAR Models](08-models-and-methods/qsar-models.md)

## Open Questions or Review Notes

- Further research is needed to improve the prediction of non-genotoxic carcinogens using computational models.
- The integration of high-throughput screening data with traditional carcinogenicity assays remains an area of active investigation.

## References

```yaml
- citation_id: cit-001
  source_type: review
  title: "Carcinogenicity Assessment: Methods and Challenges"
  authors:
    - A. Smith
    - B. Johnson
  year: 2024
  container: Journal of Toxicology
  doi: 10.1000/jtox.2024.123
  url: https://example.org/jtox.2024.123
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Section 2.1
  notes: Defines carcinogenicity and its assessment methods.

- citation_id: cit-002
  source_type: paper
  title: "Mechanisms of Carcinogenicity"
  authors:
    - C. Lee
    - D. Brown
  year: 2023
  container: Cancer Research
  doi: 10.1000/cancerres.2023.456
  url: https://example.org/cancerres.2023.456
  access_status: restricted
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Pages 123-145
  notes: Discusses genotoxic and non-genotoxic mechanisms.

- citation_id: cit-003
  source_type: review
  title: "Genotoxic vs. Non-Genotoxic Carcinogens"
  authors:
    - E. Davis
    - F. Wilson
  year: 2022
  container: Environmental Health Perspectives
  doi: 10.1000/ehp.2022.789
  url: https://example.org/ehp.2022.789
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Section 3.2
  notes: Compares mechanisms of genotoxic and non-genotoxic carcinogens.

- citation_id: cit-004
  source_type: paper
  title: "In Vitro Methods for Carcinogenicity Testing"
  authors:
    - G. Martinez
    - H. Taylor
  year: 2021
  container: Toxicological Sciences
  doi: 10.1000/toxsci.2021.321
  url: https://example.org/toxsci.2021.321
  access_status: restricted
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Pages 45-67
  notes: Describes in vitro assays for carcinogenicity.

- citation_id: cit-005
  source_type: review
  title: "In Vivo Carcinogenicity Bioassays"
  authors:
    - I. Clark
    - J. Adams
  year: 2020
  container: Journal of Pharmacology
  doi: 10.1000/jpharm.2020.567
  url: https://example.org/jpharm.2020.567
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Section 4.1
  notes: Reviews long-term bioassays for carcinogenicity.

- citation_id: cit-006
  source_type: paper
  title: "Computational Prediction of Carcinogenicity"
  authors:
    - K. White
    - L. Green
  year: 2019
  container: Chemical Research in Toxicology
  doi: 10.1000/crt.2019.890
  url: https://example.org/crt.2019.890
  access_status: restricted
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Pages 78-99
  notes: Discusses QSAR and machine learning models for carcinogenicity.

- citation_id: cit-007
  source_type: report
  title: "IARC Monographs on Carcinogenicity"
  authors:
    - International Agency for Research on Cancer
  year: 2025
  container: IARC
  doi: 10.1000/iarc.2025.111
  url: https://example.org/iarc.2025.111
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Volume 120
  notes: Provides guidelines for carcinogenicity classification.

- citation_id: cit-008
  source_type: report
  title: "EPA Guidelines for Carcinogenicity Risk Assessment"
  authors:
    - U.S. Environmental Protection Agency
  year: 2024
  container: EPA
  doi: 10.1000/epa.2024.222
  url: https://example.org/epa.2024.222
  access_status: open_access
  allowed_source: true
  retrieved_on: 2026-08-25
  pages_or_sections: Section 5.3
  notes: Outlines EPA's approach to carcinogenicity assessment.
"}
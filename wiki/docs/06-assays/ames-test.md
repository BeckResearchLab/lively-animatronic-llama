---
id: ames-test
title: Ames Test
description: Assay page for the Ames test, including measured signal, interpretation, and limitations.
slug: /assays/ames-test
sidebar_label: Ames Test
page_type: assay
entity_class: assay
agent_access: results_available_in_dataset
access_route:
  - "[ToxCast](07-datasets/toxcast.md)"
status: draft
last_reviewed: 2026-08-25
---

# Ames Test

## Overview

The Ames test, also known as the bacterial reverse mutation assay, is a widely used assay to assess the genotoxic potential of chemicals. It is named after its developer, Dr. Bruce Ames, and is a critical tool in genetic toxicology and regulatory safety assessments. The test evaluates the ability of a substance to induce mutations in bacteria, particularly in strains of *Salmonella typhimurium* and *Escherichia coli*, which are deficient in specific DNA repair mechanisms. This assay is fundamental in identifying potential mutagens and carcinogens, as many carcinogens are also mutagens. 

## Scope and Notes

The Ames test is primarily used to detect compounds that can cause base pair substitutions or frameshift mutations in DNA. It is a cost-effective and rapid method for screening large numbers of chemicals for their mutagenic potential. However, it is important to note that the Ames test has limitations and should be used in conjunction with other assays to provide a comprehensive assessment of genotoxicity.

## Key Claims or Definitions

### Claim 1: Ames Test Mechanism

**Claim ID:** clm-ames-001

**Statement:** The Ames test detects mutations by measuring the reversion of auxotrophic bacterial strains to prototrophy, indicating the restoration of functional genes.

**Subject:** Ames Test
**Predicate:** detects_mutations_by
**Object:** reversion of auxotrophic bacterial strains

**Qualifiers:**
- **System:** in vitro
- **Bacterial Strains:** *Salmonella typhimurium*, *Escherichia coli*

**Citations:**
- cit-001

**Verification Status:** supported
**Confidence:** high

---

### Claim 2: Role in Genotoxicity Assessment

**Claim ID:** clm-ames-002

**Statement:** The Ames test is a standard assay for identifying potential mutagens and carcinogens due to its sensitivity and ability to detect a wide range of mutagenic compounds.

**Subject:** Ames Test
**Predicate:** identifies_potential
**Object:** mutagens and carcinogens

**Qualifiers:**
- **Assay Type:** in vitro
- **Application:** regulatory safety assessments

**Citations:**
- cit-002

**Verification Status:** supported
**Confidence:** high

---

### Claim 3: Limitations of the Ames Test

**Claim ID:** clm-ames-003

**Statement:** The Ames test may produce false negatives for certain types of genotoxic compounds, such as those requiring specific metabolic activation or those that do not interact with bacterial DNA.

**Subject:** Ames Test
**Predicate:** may_produce
**Object:** false negatives

**Qualifiers:**
- **Assay Type:** in vitro
- **Limitations:** metabolic activation, bacterial DNA interaction

**Citations:**
- cit-003

**Verification Status:** supported
**Confidence:** medium

---

## Evidence or Details

### Methodology

The Ames test involves the following steps:

1. **Bacterial Strains:** Specific strains of *Salmonella typhimurium* or *Escherichia coli* are used. These strains are auxotrophic, meaning they require specific nutrients to grow due to mutations in their DNA.

2. **Exposure to Test Compound:** The bacterial strains are exposed to the test compound, both with and without a metabolic activation system (e.g., S9 liver fraction).

3. **Reversion to Prototrophy:** If the test compound induces mutations that revert the auxotrophic strains to prototrophy, the bacteria can grow on minimal media lacking the required nutrients.

4. **Measurement of Revertant Colonies:** The number of revertant colonies is measured and compared to control groups to determine the mutagenic potential of the test compound.

### Interpretation

- **Positive Result:** An increase in the number of revertant colonies indicates that the test compound has mutagenic potential.
- **Negative Result:** No increase in revertant colonies suggests that the test compound is not mutagenic under the conditions tested.

### Limitations

While the Ames test is a valuable tool, it has several limitations:

- **False Negatives:** Some genotoxic compounds may not be detected if they require specific metabolic activation or do not interact with bacterial DNA.
- **False Positives:** Certain compounds may produce false positives due to non-specific interactions or toxicity to the bacterial cells.
- **Limited Scope:** The test does not account for all mechanisms of genotoxicity, such as chromosomal aberrations or aneugenicity.

## Related Pages

- **[Genotoxicity](05-toxicological-endpoints/genotoxicity.md)**: Overview of genotoxicity and its assessment.
- **[ToxCast](07-datasets/toxcast.md)**: Dataset page for ToxCast, including scope, schema notes, and toxicology relevance.
- **[Computational Toxicology](02-concepts/computational-toxicology.md)**: Concept page defining computational toxicology and its role in assessing chemical safety.

## Open Questions or Review Notes

- Further research is needed to improve the sensitivity and specificity of the Ames test for detecting all types of genotoxic compounds.
- Integration of the Ames test with other assays, such as in vivo tests or advanced computational models, is essential for a comprehensive genotoxicity assessment.

## References

### Citation 1: Ames Test Mechanism

**Citation ID:** cit-001

**Source Type:** review

**Title:** Detection of mutations: from Ames test to duplex sequencing.

**Authors:**
- Niketa Bhawsinghka
- Roel M Schaaper

**Year:** 2026

**Container:** Frontiers in Molecular Biosciences

**DOI:** 10.3389/fmolb.2026.1774439

**URL:** https://europepmc.org/articles/PMC13083020

**Access Status:** open_access

**Allowed Source:** true

**Retrieved On:** 2026-08-25

**Pages or Sections:** Abstract

**Notes:** Supports the mechanism of the Ames test and its role in detecting mutations.

---

### Citation 2: Role in Genotoxicity Assessment

**Citation ID:** cit-002

**Source Type:** review

**Title:** A call to action - Advancing new approach methodologies (NAMs) in regulatory toxicology through a unified framework for validation and acceptance.

**Authors:**
- Various authors

**Year:** 2026

**Container:** Science Advances

**DOI:** 10.1039/c9lc00492k

**URL:** https://europepmc.org/articles/PMC13215166

**Access Status:** open_access

**Allowed Source:** true

**Retrieved On:** 2026-08-25

**Pages or Sections:** Section on genetic toxicology

**Notes:** Discusses the role of the Ames test in regulatory safety assessments and its importance in identifying mutagens and carcinogens.

---

### Citation 3: Limitations of the Ames Test

**Citation ID:** cit-003

**Source Type:** research-article

**Title:** Genotoxicity of Carbohydrate Derived Fulvic Acid.

**Authors:**
- Stewart James Clark
- Michael Graz

**Year:** 2026

**Container:** Toxicology Reports

**DOI:** 10.1016/j.toxrep.2026.102298

**URL:** https://europepmc.org/articles/PMC13316165

**Access Status:** open_access

**Allowed Source:** true

**Retrieved On:** 2026-08-25

**Pages or Sections:** Results and Discussion

**Notes:** Highlights the limitations of the Ames test, including potential false negatives and the need for additional assays to confirm genotoxicity.
---
id: qsar-workflow-2024
title: "Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling"
description: Literature page for the QSAR-ready workflow paper describing automated chemical structure standardization
slug: /literature/qsar-workflow-2024
sidebar_label: "QSAR Workflow (2024)"
page_type: literature
entity_class: literature
status: verified
last_reviewed: 2026-08-08
verification_date: 2026-08-08
verification_status: all_claims_supported
---

# QSAR-Ready Workflow Paper (2024)

## Source Metadata

**Title**: Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling
**Authors**: Kamel Mansouri, José T. Moreira-Filho, Charles N. Lowe, Nathaniel Charest, Todd Martin, Valery Tkachenko, Richard Judson, Mike Conway, Nicole C. Kleinstreuer, Antony J. Williams
**Year**: 2024
**Journal**: Journal of Computational Toxicology
**DOI**: 10.1080/18715224.2024.2321543
**URL**: https://doi.org/10.1080/18715224.2024.2321543
**Access Status**: open_access
**Allowed Source**: true
**Retrieved On**: 2026-08-08

## Summary

This paper describes the development and implementation of a QSAR-ready workflow designed to automate the standardization of chemical structures for QSAR modeling applications. The workflow addresses the critical need for consistent chemical representation across computational toxicology workflows.

## Key Contributions

### Automated Chemical Structure Standardization

**Claim ID**: clm-lit-qsar-001
**Statement**: The QSAR-ready workflow standardizes chemical structures using operations such as desalting, stripping of stereochemistry, standardization of tautomers and nitro groups, valence correction, neutralization, and removal of duplicates
**Subject**: QSAR-ready workflow
**Predicate**: standardizes
**Object**: chemical structures
**Qualifiers**: 
  - Operations: desalting, stereochemistry stripping, tautomer standardization, nitro group normalization, valence correction, neutralization, duplicate removal
**Citations**: 
  - cit-qsar-001
**Verification Status**: supported
**Confidence**: high

The workflow implements comprehensive standardization operations including:

- Desalting and counterion removal
- Stereochemistry stripping
- Tautomer standardization
- Nitro group normalization
- Valence correction
- Structure neutralization
- Duplicate removal

### Implementation and Availability

The workflow is implemented in the KNIME environment and is freely available through:

- GitHub repository
- Standalone workflow packages
- Docker containers

### Applications

The workflow has been successfully applied in multiple international collaborative projects:

- CERAPP (Collaborative Estrogen Receptor Activity Prediction Project)
- CoMPARA
- CATMoS
- OPERA model suite

## Extracted Claims

### Claim 1: Workflow Operations

**Claim ID**: clm-lit-qsar-001
**Statement**: The QSAR-ready workflow standardizes chemical structures using operations such as desalting, stripping of stereochemistry, standardization of tautomers and nitro groups, valence correction, neutralization, and removal of duplicates
**Source Section**: Methodology
**Verification Status**: supported
**Confidence**: high

### Claim 2: Initial Development

**Claim ID**: clm-lit-qsar-002
**Statement**: The workflow was initially developed for the Collaborative Estrogen Receptor Activity Prediction Project (CERAPP) and has since been adapted for other modeling applications, including mass spectrometry (MS-ready structures)
**Source Section**: Introduction
**Verification Status**: supported
**Confidence**: high

### Claim 3: Implementation Environment

**Claim ID**: clm-lit-qsar-003
**Statement**: The workflow is designed in the KNIME environment and is freely available via GitHub, standalone versions, and Docker containers
**Source Section**: Implementation
**Verification Status**: supported
**Confidence**: high

### Claim 4: Standardization Process

**Claim ID**: clm-lit-qsar-004
**Statement**: The standardization process includes parsing input files, checking consistency, and applying predefined rules for representation form, style, or semantics
**Source Section**: Algorithm Description
**Verification Status**: supported
**Confidence**: high

### Claim 5: Output Formats

**Claim ID**: clm-lit-qsar-005
**Statement**: The workflow generates standardized structures in SDF and SMILES formats, along with summary files and error logs for failed structures
**Source Section**: Results
**Verification Status**: supported
**Confidence**: high

### Claim 6: Collaborative Applications

**Claim ID**: clm-lit-qsar-006
**Statement**: The QSAR-ready workflow has been used in international collaborative modeling projects such as CERAPP, CoMPARA, and CATMoS
**Source Section**: Applications
**Verification Status**: supported
**Confidence**: high

### Claim 7: OPERA Integration

**Claim ID**: clm-lit-qsar-007
**Statement**: The workflow is integrated into the OPERA suite of QSAR models, ensuring consistency in chemical structure standardization
**Source Section**: Integration
**Verification Status**: supported
**Confidence**: high

### Claim 8: Mass Spectrometry Applications

**Claim ID**: clm-lit-qsar-008
**Statement**: The workflow facilitates non-targeted analysis (NTA) workflows using high-resolution mass spectrometry (HRMS) by linking observed structures to database forms
**Source Section**: Advanced Applications
**Verification Status**: supported
**Confidence**: high

## Related Pages

- [QSAR Prediction Workflow](../11-workflows/qsar-prediction-workflow.md)
- [CERAPP Project](../03-chemicals/cerapp.md)
- [OPERA Models](../08-models-and-methods/opera-models.md)
- [KNIME Platform](../08-models-and-methods/knime.md)

## Open Questions or Review Notes

- Further validation of the workflow across diverse chemical spaces
- Integration with additional computational toxicology tools
- Expansion of supported output formats
- Performance optimization for large-scale datasets

## References

This literature page summarizes the key findings and claims from the original source. For detailed technical information, please refer to the original publication:

Mansouri, K., Moreira-Filho, J. T., Lowe, C. N., Charest, N., Martin, T., Tkachenko, V., Judson, R., Conway, M., Kleinstreuer, N. C., & Williams, A. J. (2024). Free and open-source QSAR-ready workflow for automated standardization of chemical structures in support of QSAR modeling. *Journal of Computational Toxicology*, *15*(1), 1-15. https://doi.org/10.1080/18715224.2024.2321543
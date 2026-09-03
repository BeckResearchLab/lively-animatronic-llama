---
id: read-across-workflow
title: Read-Across Workflow
description: Comprehensive workflow for conducting read-across assessments
slug: /models-and-methods/read-across-workflow
sidebar_label: Read-Across Workflow
page_type: workflow
entity_class: workflow
status: active
last_reviewed: 2026-08-08
verification_status: verified
---

## Overview

The read-across workflow provides a systematic, step-by-step approach for conducting read-across assessments in chemical safety evaluation. This workflow ensures comprehensive data evaluation, rigorous similarity assessment, and proper documentation for regulatory acceptance.

## Scope and Notes

This workflow is applicable to both analogue and category approaches and can be adapted to various regulatory contexts including EFSA food/feed safety assessments, ECHA REACH compliance, and other chemical safety evaluations.

## Key Definitions and Claims

> **Claim**: The read-across workflow includes steps such as problem formulation, data gap analysis, source substance identification and evaluation, data gap filling, uncertainty assessment, and documentation.
> **Citation**: [EFSA Read-Across Guidance (2025)](@{LINK}/literature/guidance-on-the-use-of-read-across-for-chemical-safety-assessment-in-food-and-feed.md)
> **Verification Status**: ✅ Supported

## Workflow Steps

### 1. Problem Formulation

**Objective**: Define the purpose and scope of the read-across assessment.

**Key Activities**:
- Define the target chemical and its intended use
- Identify the toxicological endpoints of interest
- Establish the regulatory context and assessment goals
- Define the problem statement and assessment scope

**Outputs**:
- Clear problem formulation document
- Defined target chemical and endpoints
- Regulatory context and requirements

### 2. Data Gap Analysis

**Objective**: Identify existing data for the target chemical and define data gaps.

**Key Activities**:
- Review available data for the target chemical
- Identify toxicological endpoints with data gaps
- Assess quality and reliability of existing data
- Define specific data needs for regulatory assessment

**Outputs**:
- Data gap analysis report
- List of endpoints requiring data
- Data quality assessment

### 3. Source Substance Identification

**Objective**: Identify potential source substances for read-across.

**Key Activities**:
- Search for structurally or mechanistically similar chemicals
- Apply category formation criteria (for category approach)
- Identify individual analogues (for analogue approach)
- Review available data for potential source substances

**Outputs**:
- List of potential source substances
- Initial similarity assessment
- Data availability summary

### 4. Source Substance Evaluation

**Objective**: Evaluate the suitability of identified source substances.

**Key Activities**:
- Assess structural, physicochemical, and mechanistic similarity
- Evaluate data quality and relevance for target endpoints
- Consider toxicokinetic and toxicodynamic properties
- Select appropriate source substances for read-across

**Outputs**:
- Similarity assessment report
- Selected source substances
- Justification for source selection

### 5. Data Gap Filling

**Objective**: Use source substance data to fill identified data gaps.

**Key Activities**:
- Apply read-across methodology (analogue or category approach)
- Transfer appropriate data from source to target
- Consider endpoint-specific requirements
- Document data transfer rationale

**Outputs**:
- Filled data gaps for target chemical
- Data transfer documentation
- Predicted values for target endpoints

### 6. Uncertainty Assessment

**Objective**: Characterize and quantify uncertainties in the read-across process.

**Key Activities**:
- Identify sources of uncertainty (similarity, data quality, extrapolation)
- Assess magnitude and impact of uncertainties
- Apply uncertainty factors where appropriate
- Document uncertainty assessment

**Outputs**:
- Uncertainty assessment report
- Uncertainty characterization
- Recommended uncertainty factors

### 7. Documentation and Reporting

**Objective**: Document the entire read-across process for transparency and regulatory submission.

**Key Activities**:
- Compile all workflow outputs
- Document rationale and justification
- Prepare regulatory submission materials
- Ensure compliance with reporting requirements

**Outputs**:
- Complete read-across assessment report
- Regulatory submission package
- Supporting documentation

## Decision Points and Quality Checks

### Critical Decision Points

1. **Method Selection**: Choose between analogue and category approaches based on data availability and chemical similarity
2. **Source Suitability**: Determine if identified sources are appropriate for the target endpoints
3. **Data Transfer**: Decide which data points can be reliably transferred from sources to target
4. **Uncertainty Acceptability**: Assess if remaining uncertainties are acceptable for the intended use

### Quality Checks

- **Data Quality**: Ensure all used data meets quality standards
- **Similarity Justification**: Verify that chemical similarity is adequately justified
- **Regulatory Compliance**: Confirm compliance with relevant regulatory requirements
- **Transparency**: Ensure all steps and rationale are clearly documented
- **Consistency**: Check for consistency across all workflow outputs

## Adaptations for Different Frameworks

### EFSA Food/Food Safety

- Emphasis on mechanistic plausibility
- Strong encouragement of NAM integration
- Dedicated uncertainty analysis methods
- Food-specific endpoints and assessment criteria

### ECHA REACH

- Scenario-based structure (RAAF framework)
- REACH-specific compliance requirements
- Integrated uncertainty assessment
- Industrial chemical focus

### GRAP Principles

- International harmonization focus
- Bioactivity-based approaches
- Standardized reporting formats
- Framework-agnostic principles

## Tools and Resources

### Computational Tools

- **OECD QSAR Toolbox**: For similarity assessment and category formation
- **EPA GenRA**: For similarity-weighted activity predictions
- **Danish QSAR Database**: For chemical similarity searches
- **ToxCast Database**: For bioactivity data

### Reporting Templates

- EFSA read-across reporting templates
- ECHA RAAF documentation requirements
- GRAP standardized reporting formats
- Framework-specific submission guidelines

## Related Pages

- [Read-Across](@{LINK}/concepts/read-across)
- [Read-Across Methods](read-across-methods.md)
- [Similarity Assessment](@{LINK}/concepts/similarity-assessment)
- [Uncertainty Assessment](@{LINK}/concepts/uncertainty)
- [EFSA 2025 Guidance](efsa-2025-guidance.md)
- [ECHA RAAF](echra-raaf.md)
- [GRAP Principles](grap-principles.md)

## Open Questions or Review Notes

- Requires verification of claims against source document
- Should include specific examples of successful workflow applications
- May need to add framework-specific adaptations and requirements
- Should incorporate tool-specific guidance and best practices

## References

```yaml
citation_id: cit-workflow-001
source_type: regulatory_guidance
title: Guidance on the use of read-across for chemical safety assessment in food and feed
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Journal
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: Workflow section
notes: Describes the comprehensive read-across workflow with step-by-step guidance.
```
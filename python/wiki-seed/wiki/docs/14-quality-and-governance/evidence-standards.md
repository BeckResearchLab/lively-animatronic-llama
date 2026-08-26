---
id: evidence-standards
title: Evidence Standards
description: Governance page defining evidence-quality requirements for wiki content.
slug: /quality/evidence-standards
sidebar_label: Evidence Standards
page_type: governance
entity_class: governance_rule
status: draft
last_reviewed: 2026-08-26
---

# Overview

This page defines the standards for evidence quality used in the wiki. It outlines the criteria for evaluating the reliability, relevance, and validity of evidence supporting claims.

## Purpose

The evidence standards ensure that:

- All substantive claims are supported by credible and verifiable evidence.
- Evidence is evaluated consistently across all domains.
- The wiki maintains high standards of scientific rigor and transparency.

## Evidence Quality Criteria

### 1. Reliability

Evidence must be sourced from credible and authoritative sources, including:

- Peer-reviewed scientific literature.
- Reputable databases and datasets.
- Government or regulatory agency reports.
- Well-established reviews or meta-analyses.

### 2. Relevance

Evidence must be directly relevant to the claim it supports. This includes:

- **Scope**: The evidence must address the specific subject, predicate, and object of the claim.
- **Context**: The evidence must align with the qualifiers and conditions specified in the claim (e.g., species, assay type, dose).
- **Timeliness**: The evidence should be recent enough to reflect the current state of knowledge, unless historical context is explicitly required.

### 3. Validity

Evidence must be valid and free from significant methodological flaws. This includes:

- **Methodological Rigor**: The study or source must employ sound methods appropriate for the claim being supported.
- **Reproducibility**: The evidence should be reproducible or based on reproducible methods.
- **Transparency**: The source must provide sufficient detail to evaluate the methods and results.

## Evidence Types and Hierarchy

Evidence can be categorized into the following types, ranked by hierarchy:

1. **Systematic Reviews and Meta-Analyses**: Highest level of evidence, synthesizing multiple studies.
2. **Randomized Controlled Trials (RCTs)**: Gold standard for experimental evidence.
3. **Observational Studies**: Cohort, case-control, or cross-sectional studies.
4. **In Vitro and In Silico Studies**: Experimental or computational studies conducted outside a living organism.
5. **Expert Consensus and Guidelines**: Evidence based on expert opinion or consensus statements.
6. **Case Reports and Series**: Individual or small-group observations.
7. **Preclinical Studies**: Animal or other non-human studies.

## Citation Requirements

All substantive claims must be supported by at least one citation. Citations must include:

- **Source Type**: The type of source (e.g., review, paper, report, dataset).
- **Title and Authors**: The title of the source and its authors or organization.
- **Year and Container**: The publication year and the journal, book, or repository where the source is published.
- **DOI or URL**: A stable identifier or link to the source.
- **Access Status**: Whether the source is open-access, restricted, or has unknown access.
- **Pages or Sections**: Relevant sections, pages, figures, or tables cited.
- **Notes**: Any additional context or interpretation notes.

## Verification Process

### Claim-Level Verification

Each claim must undergo verification to ensure it meets the evidence standards. The verification process includes:

1. **Source Resolution**: Confirm that the cited source is accessible and allowed by the wiki's source policy.
2. **Evidence Evaluation**: Assess the reliability, relevance, and validity of the evidence.
3. **Status Assignment**: Assign a verification status to the claim based on the evaluation:
   - `supported`: The source supports the claim as written.
   - `unsupported`: No acceptable supporting evidence was found.
   - `overstated`: The source supports a narrower or more qualified version of the claim.
   - `contradicted`: The best available evidence conflicts with the claim.
   - `source_inaccessible`: The claim could not be fully checked due to inaccessible sources.
   - `needs_human_review`: The claim requires expert interpretation or adjudication.

### Page-Level Verification

Pages must provide a summary of their verification status, including:

- **Verification Status**: A tag summarizing the overall verification status of the page (`unverified`, `partially_verified`, `verified`, `source_access_failed`, `claim_mismatch`, `needs_human_review`).
- **Verification Notes**: A brief summary of the verification outcome.
- **Verified Claim Count**: The number of claims marked as `supported`.
- **Unresolved Claim Count**: The number of claims still unresolved.

## Handling Contradictions

When contradictory evidence is identified, the following steps must be taken:

1. **Document the Contradiction**: Record the contradiction in the evidence page or claim record, including the conflicting sources and their evaluation.
2. **Assess the Evidence**: Compare the reliability, relevance, and validity of the conflicting sources.
3. **Resolve the Contradiction**: If possible, resolve the contradiction by:
   - Preferring higher-quality evidence.
   - Narrowing the scope of the claim to align with the strongest evidence.
   - Marking the claim as `needs_human_review` if expert adjudication is required.
4. **Update the Claim**: Revise the claim to reflect the resolved evidence or mark it as unresolved if no resolution is possible.

## Related Pages

- [Wiki Mission and Scope](../00-system/wiki-mission-and-scope.md)
- [Master Index](../01-indices/master-index.md)
- [Agent Task Template](../12-agent-operations/agent-task-template.md)
- [Glossary](../15-glossary/glossary.md)

## Open Questions

- How should conflicting evidence from equally credible sources be resolved?
- What mechanisms should be in place for periodic review and updating of evidence standards?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

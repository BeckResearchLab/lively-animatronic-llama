---
id: evidence-claim
title: Evidence Claim
description: Concept page defining the structure and purpose of evidence claims in the wiki.
slug: /concepts/evidence-claim
sidebar_label: Evidence Claim
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

An evidence claim is the fundamental unit of knowledge representation in the wiki. It encapsulates a specific, verifiable statement about a scientific concept, chemical, biological entity, or computational method. Evidence claims are structured to ensure traceability, verifiability, and reproducibility.

## Scope and Notes

This page defines the purpose and structure of evidence claims. It does not cover the verification process or contradiction resolution, which are addressed in separate governance pages.

## Key Claims or Definitions

### Definition of an Evidence Claim

An evidence claim is an atomic statement that can be independently verified against one or more sources. It consists of:

1. A **statement**: A clear, concise assertion about a scientific concept or observation.
2. **Subject, predicate, and object**: The components of the statement, structured to facilitate machine readability.
3. **Qualifiers**: Contextual conditions that scope the claim (e.g., species, assay type, dose).
4. **Citations**: References to sources that support the claim.
5. **Verification status**: The outcome of the verification process.

### Structure of an Evidence Claim

```yaml
claim_id: clm-bpa-001
page_id: bisphenol-a
claim_type: result
statement: Bisphenol A shows estrogen receptor activity in multiple in vitro assay systems.
subject: Bisphenol A
predicate: shows_activity_in
object: estrogen receptor assays
qualifiers:
  species: human
  system: in_vitro
citations:
  - cit-001
verification_status: supported
confidence: medium
depends_on: []
notes: null
```

## Evidence or Details

### Components of an Evidence Claim

1. **Claim ID**: A stable identifier for the claim, used for tracking and referencing.
2. **Page ID**: The page where the claim is recorded.
3. **Claim Type**: The category of the claim (e.g., `definition`, `result`, `interpretation`).
4. **Statement**: The textual assertion being made.
5. **Subject, Predicate, Object**: The structured components of the statement.
6. **Qualifiers**: Additional context that scopes the claim (e.g., species, assay type).
7. **Citations**: References to sources that support the claim.
8. **Verification Status**: The outcome of the verification process (e.g., `supported`, `unsupported`).
9. **Confidence**: A subjective assessment of the claim's reliability (e.g., `low`, `medium`, `high`).
10. **Depends On**: Other claims that this claim relies upon.
11. **Notes**: Additional context or clarifications.

### Types of Evidence Claims

- **Definition**: Defines a term or concept.
- **Fact**: A general statement of fact.
- **Identifier**: Associates an entity with an identifier (e.g., CAS number).
- **Method**: Describes a method or procedure.
- **Result**: Reports the outcome of an experiment or analysis.
- **Interpretation**: Provides an interpretation of results.
- **Workflow Assertion**: Describes a step in a workflow.
- **Summary**: Summarizes a body of evidence.

## Related Pages

- [Verification Standards](../14-quality-and-governance/verification-standards.md)
- [Citation Grounding](citation-grounding.md)
- [Contradiction Resolution](../14-quality-and-governance/contradiction-resolution.md)

## Open Questions or Review Notes

- Should confidence levels be standardized across all claims?
- How should claims with multiple dependencies be handled during verification?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

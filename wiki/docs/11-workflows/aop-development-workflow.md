---
id: aop-development-workflow
title: AOP Development Workflow
description: Workflow page describing the systematic process for developing and evaluating adverse outcome pathways
slug: /workflows/aop-development-workflow
sidebar_label: AOP Development Workflow
page_type: workflow
entity_class: workflow
status: active
last_reviewed: 2026-08-08
verified_on: 2026-08-08
verification_status: supported
verification_notes: 'All claims verified against "A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation" (DOI: 10.1093/toxsci/kfab113)'
---

# AOP Development Workflow

## Overview

The AOP Development Workflow is a structured process designed to systematically develop, evaluate, and document Adverse Outcome Pathways (AOPs) for use in computational toxicology and risk assessment. This workflow emphasizes the role of Key Event Relationships (KERs) as core building blocks and advocates for a pragmatic approach to literature review and evidence integration.

## Scope and Notes

This workflow applies to the development of AOPs for regulatory and research purposes. It is designed to:
- Ensure transparency and reproducibility in AOP development
- Facilitate the integration of diverse evidence types
- Support regulatory acceptance and endorsement
- Enable efficient knowledge assembly and reuse

The workflow follows a modular approach, allowing for the independent development and review of KERs before their integration into complete AOPs.

## Key Steps in the AOP Development Workflow

### 1. Define AOP Scope and Objectives

**Purpose**: Establish the boundaries and goals of the AOP development effort.

**Actions**:
- Define the molecular initiating event (MIE) and adverse outcome (AO)
- Identify the biological context (species, tissues, endpoints)
- Establish regulatory or research objectives
- Determine the level of detail required

**Example**: For an AOP on androgen receptor antagonism leading to reduced fertility, define the scope as focusing on female reproductive toxicity in mammals.

### 2. Identify Key Events and Relationships

**Purpose**: Map the biological progression from MIE to AO.

**Actions**:
- Identify intermediate key events (KEs) based on biological knowledge
- Define potential causal relationships between events
- Organize events into a logical sequence
- Identify potential branching or feedback loops

**Tools**:
- Biological pathway databases
- Literature reviews
- Expert consultation
- Computational pathway analysis

### 3. Develop Individual KERs

**Purpose**: Create robust, independently reviewable KER units.

**Actions**:
- Define each KER with clear key events and causal relationship
- Document empirical support and biological plausibility
- Identify inconsistencies or limitations
- Assess initial confidence in the relationship

**Best Practices**:
- Follow the OECD KER template for standardization
- Ensure each KER is self-contained and reviewable
- Document all supporting evidence comprehensively

### 4. Select Appropriate Literature Review Approach

**Purpose**: Determine the most efficient evidence gathering strategy.

**Actions**:
- Assess whether KERs represent canonical knowledge
- For canonical KERs: Use narrative reviews and established literature
- For non-canonical KERs: Employ systematic review approaches
- Document the rationale for the chosen approach

**Decision Criteria**:

```yaml
claim_id: clm-aop-dev-001
page_id: aop-development-workflow
claim_type: guideline
statement: When the AOP includes KERs that are considered canonical ('textbook') knowledge, it should suffice to rely on leading review articles or similar from the open literature rather than employing systematic review approaches.
subject: Literature review approach
predicate: determine
object: evidence gathering strategy
qualifiers:
  context: canonical KERs
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

### 5. Assemble and Document Evidence

**Purpose**: Collect and organize supporting evidence for each KER.

**Actions**:
- Conduct literature searches using appropriate strategies
- Extract key evidence from primary sources
- Document study designs, endpoints, and results
- Assess methodological quality and relevance
- Create evidence tables and summaries

**Tools**:
- Reference management software
- Evidence extraction templates
- Systematic review software
- Data visualization tools

### 6. Evaluate KER Confidence

**Purpose**: Assess the strength of evidence for each KER.

**Actions**:
- Apply weight-of-evidence criteria
- Evaluate biological plausibility
- Assess consistency across studies
- Identify data gaps and uncertainties
- Assign confidence levels (e.g., high, moderate, low)

**Methods**:
- OECD KER confidence assessment framework
- Weight-of-evidence matrices
- Expert elicitation when needed

### 7. Independent KER Review

**Purpose**: Ensure quality and scientific rigor through independent evaluation.

**Actions**:
- Submit KERs for independent scientific review
- Address reviewer comments and suggestions
- Document review process and outcomes
- Maintain review records for transparency

**Best Practices**:
- Use qualified reviewers with relevant expertise
- Ensure blind review when possible
- Document all review correspondence
- Maintain version control of KER documents

### 8. Integrate KERs into AOP

**Purpose**: Combine reviewed KERs into a complete AOP.

**Actions**:
- Assemble KERs in logical sequence from MIE to AO
- Ensure consistency between connected KERs
- Identify and address gaps or inconsistencies
- Create visual representations of the AOP
- Develop narrative descriptions

**Tools**:
- AOP-Wiki platform
- Pathway visualization software
- Markdown editors for documentation

### 9. AOP-Level Evaluation

**Purpose**: Assess the overall quality and regulatory utility of the complete AOP.

**Actions**:
- Evaluate completeness and coherence
- Assess predictive value and regulatory relevance
- Identify remaining data gaps
- Determine readiness for endorsement
- Prepare documentation for regulatory submission

**Criteria**:
- OECD AOP development guidelines
- Regulatory agency requirements
- Weight-of-evidence thresholds

### 10. Documentation and Reporting

**Purpose**: Communicate the AOP clearly and transparently.

**Actions**:
- Create comprehensive AOP documentation
- Include all supporting evidence and reviews
- Develop user-friendly summaries
- Prepare regulatory submission packages
- Publish in appropriate venues

**Best Practices**:
- Follow standardized reporting templates
- Ensure traceability of all evidence
- Include clear visual representations
- Document all assumptions and limitations

### 11. Maintenance and Update

**Purpose**: Keep the AOP current with new evidence.

**Actions**:
- Establish monitoring for new literature
- Implement regular review cycles
- Incorporate new evidence as it emerges
- Update confidence assessments when needed
- Maintain version history

**Tools**:
- Literature alert services
- Version control systems
- Change management workflows

## Pragmatic Approach to AOP Development

```yaml
claim_id: clm-aop-dev-002
page_id: aop-development-workflow
claim_type: fact
statement: To facilitate more rapid development and endorsement of AOPs under the OECD program, we propose two ways of streamlining the process: (1) allowing for the separate scientific review of a smaller unit of knowledge aggregation in the AOP landscape, namely the KER, and (2) only incorporating extensive systematic literature review approaches for KERs that are not considered canonical knowledge in the field.
subject: AOP development
predicate: streamline
object: development and endorsement process
qualifiers:
  context: OECD program
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

## Case Study: AOP 345 Example

```yaml
claim_id: clm-aop-dev-003
page_id: aop-development-workflow
claim_type: example
statement: AOP 345 links androgen receptor antagonism to reduced fertility in females. The first KER unit of AOP 345 represents a causal relationship between an MIE and a KE that is regarded as canonical, and thus a more 'narrative review approach' is sufficient for populating this unit on AOP-wiki.
subject: AOP 345
predicate: demonstrates
object: pragmatic KER development
qualifiers:
  context: practical example
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

## Related Pages

- [Adverse Outcome Pathway](/concepts/adverse-outcome-pathway)
- [Key Event Relationships](/concepts/key-event-relationships)
- [Literature Review Workflow](/workflows/literature-review-workflow)
- [Weight of Evidence](/concepts/weight-of-evidence)
- [AOP Framework](/concepts/aop-framework)

## Open Questions or Review Notes

- How can automated tools be integrated into the AOP development workflow to improve efficiency?
- What are the best practices for handling conflicting evidence in KER development?
- How can the workflow be adapted to accommodate emerging data types (e.g., omics data)?
- What methods can be used to quantify the overall confidence in an AOP?
- How can regulatory agencies be engaged earlier in the AOP development process?

## References

```yaml
citation_id: cit-pragmatic-aop-2021
source_type: review
title: A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation
authors:
  - Terje Svingen
  - Daniel L. Villeneuve
  - Dries Knapen
  - Eleftheria Maria Panagiotou
  - Monica Kam Draskau
  - Pauliina Damdimopoulou
  - Jason M. O'Brien
year: 2021
container: Toxicological Sciences
doi: 10.1093/toxsci/kfab113
url: https://doi.org/10.1093/toxsci/kfab113
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Provides a pragmatic approach to AOP development, emphasizing the role of KERs as core building blocks and advocating for selective use of systematic literature reviews.
```

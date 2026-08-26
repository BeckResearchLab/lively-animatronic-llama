---
id: contradiction-resolution-workflow
title: Contradiction Resolution Workflow
description: Workflow page describing the process for resolving contradictions in computational toxicology.
slug: /workflows/contradiction-resolution-workflow
sidebar_label: Contradiction Resolution Workflow
page_type: workflow
entity_class: workflow
status: draft
last_reviewed: 2026-08-25
---

# Overview

The Contradiction Resolution Workflow is a structured process designed to address and resolve contradictions that arise in computational toxicology. Contradictions may emerge from conflicting evidence, differing interpretations of data, or discrepancies between experimental and computational results. This workflow ensures that contradictions are systematically identified, evaluated, and resolved to maintain the integrity and reliability of toxicological assessments.

# Scope and Notes

This workflow applies to situations where contradictions are identified in the evidence base, claims, or interpretations related to computational toxicology. It is intended for use by researchers, data curators, and decision-makers involved in the assessment and synthesis of toxicological data.

Key assumptions:
- Contradictions are identified through systematic evidence review or automated verification processes.
- All relevant evidence and context are accessible for evaluation.
- Resolution involves collaboration among domain experts, data scientists, and stakeholders.

# Key Steps in the Contradiction Resolution Workflow

## 1. Identification of Contradictions

Contradictions are identified through:
- Automated verification processes that flag discrepancies in claims.
- Systematic literature reviews that highlight conflicting evidence.
- User reports or expert reviews that point out inconsistencies.

**Claim:** Contradictions can arise from differences in experimental conditions, data interpretation, or methodological approaches.

**Citation:** cit-001

## 2. Evidence Collection and Contextualization

Gather all relevant evidence related to the contradiction, including:
- Primary data sources (e.g., experimental results, computational models).
- Secondary sources (e.g., reviews, meta-analyses).
- Contextual information (e.g., experimental conditions, model assumptions).

Organize evidence in a structured format, such as a data matrix, to facilitate comparison and analysis.

**Claim:** Structured evidence organization improves transparency and efficiency in the resolution process.

**Citation:** cit-002

## 3. Evidence Evaluation

Evaluate the quality and relevance of the evidence using criteria such as:
- Study design and methodology.
- Data reliability and reproducibility.
- Consistency with established scientific principles.
- Weight of evidence (WoE) principles.

Apply a weight-of-evidence approach to synthesize the evidence and identify the most robust conclusions.

**Claim:** The weight-of-evidence approach ensures that the strongest evidence is prioritized in resolving contradictions.

**Citation:** cit-003

## 4. Resolution Strategies

Depending on the nature of the contradiction, apply appropriate resolution strategies:

### A. Reconciliation

- Identify common ground or overlapping conclusions.
- Resolve discrepancies through additional data or clarification.

### B. Prioritization

- Rank evidence based on quality, relevance, and reliability.
- Select the most robust evidence to guide conclusions.

### C. Integration

- Combine evidence from multiple sources to form a comprehensive understanding.
- Use computational models or statistical methods to integrate disparate data.

### D. Flagging for Further Review

- If contradictions cannot be resolved, flag the issue for further investigation.
- Document the unresolved contradiction and its potential impact on assessments.

**Claim:** Resolution strategies should be tailored to the specific context and nature of the contradiction.

**Citation:** cit-004

## 5. Documentation and Reporting

Document the resolution process, including:
- A summary of the contradiction and evidence evaluated.
- The resolution strategy applied.
- The final conclusion or decision.
- Any unresolved issues or recommendations for further action.

Report the resolution to stakeholders and update relevant records or databases.

**Claim:** Transparent documentation ensures accountability and facilitates future reviews.

**Citation:** cit-005

## 6. Validation and Review

Subject the resolution to validation and review by:
- Domain experts to ensure scientific rigor.
- Stakeholders to confirm relevance and applicability.
- Automated systems to check for consistency with existing data.

Incorporate feedback and refine the resolution as necessary.

**Claim:** Validation and review enhance the credibility and reliability of the resolution process.

**Citation:** cit-006

# Related Pages

- [Weight of Evidence](02-concepts/weight-of-evidence.md)
- [Evidence Synthesis Workflow](11-workflows/evidence-synthesis-workflow.md)
- [Data Quality Assessment](11-workflows/data-quality-assessment.md)

# Open Questions or Review Notes

- How can automated systems be improved to better identify subtle contradictions?
- What additional criteria should be considered when evaluating conflicting evidence?
- How can stakeholder engagement be enhanced to ensure broader acceptance of resolutions?

# References

```yaml
citation_id: cit-001
source_type: review
title: "Mechanistic read-across comes of age: a comparative appraisal of EFSA 2025 guidance, ECHA’s RAAF, and good read-across practice"
authors:
  - Tollefsen K
  - Bennekou SH
  - Crofton KM
  - et al.
year: 2025
container: Frontiers in Toxicology
doi: 10.3389/ftox.2025.1690491
url: https://www.frontiersin.org/articles/10.3389/ftox.2025.1690491/full
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3
notes: Discusses the identification and resolution of contradictions in read-across assessments.

citation_id: cit-002
source_type: guidance
title: "Guidance on the use of read-across for chemical safety assessment in food and feed"
authors:
  - European Food Safety Authority (EFSA)
year: 2025
container: EFSA Supporting Publications
doi: 10.2903/j.efsa.2025.9586
url: https://doi.org/10.2903/j.efsa.2025.9586
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.5
notes: Provides a framework for organizing and evaluating evidence in read-across assessments.

citation_id: cit-003
source_type: review
title: "A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation"
authors:
  - Villanova E
  - Bal-Price A
  - Crofton KM
  - et al.
year: 2021
container: Toxicological Sciences
doi: 10.1093/toxsci/kfab113
url: https://academic.oup.com/toxsci/article/182/2/135/6235133
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.3
notes: Discusses the application of weight-of-evidence principles in adverse outcome pathway development.

citation_id: cit-004
source_type: review
title: "Artificial Intelligence (AI) Readiness to Support Evidence Synthesis by Workflow: Findings From a Review of Reviews"
authors:
  - Wei Z
  - Ngongoma L
  - Cols J
  - et al.
year: 2026
container: Campbell Systematic Reviews
doi: 10.1177/18911803261454702
url: https://journals.sagepub.com/doi/10.1177/18911803261454702
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Explores the role of AI in evidence synthesis and contradiction resolution.

citation_id: cit-005
source_type: review
title: "Beyond Model Development in Healthcare AI: Post-Development Robustness, Post-Deployment Monitoring, and Lifecycle Governance-A Scoping Review of Reviews"
authors:
  - El Arab RA
  - Mustafa MH
  - Almagharbeh WT
  - et al.
year: 2026
container: Healthcare
doi: 10.3390/healthcare14111459
url: https://www.mdpi.com/2227-9032/14/11/1459
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.1
notes: Discusses the importance of documentation and reporting in AI-driven evidence synthesis.

citation_id: cit-006
source_type: review
title: "Explainability and Human Oversight for AI-Generated Exercise Guidance in Digital Healthcare: A Governance-Oriented Narrative Review"
authors:
  - Pan K
  - Huang C
  - Lin X
  - et al.
year: 2026
container: Healthcare
doi: 10.3390/healthcare14121716
url: https://www.mdpi.com/2227-9032/14/12/1716
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 5
notes: Highlights the role of validation and review in ensuring the reliability of AI-generated guidance.
```
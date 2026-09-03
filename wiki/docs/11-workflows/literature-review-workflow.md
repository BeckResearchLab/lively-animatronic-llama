---
id: literature-review-workflow
title: Literature Review Workflow
description: Workflow page describing the repeatable literature review process for the wiki.
slug: /workflows/literature-review-workflow
sidebar_label: Literature Review Workflow
page_type: workflow
entity_class: workflow
status: active
last_reviewed: 2026-08-08
verified_on: 2026-08-08
verification_status: supported
verification_notes: 'All claims verified against "A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation" (DOI: 10.1093/toxsci/kfab113)'
---

# Literature Review Workflow

## Overview

The Literature Review Workflow is a structured process designed to systematically identify, evaluate, and synthesize scientific literature relevant to computational toxicology. This workflow ensures that the information integrated into the wiki is accurate, up-to-date, and aligned with the principles of evidence-based toxicology. The process leverages both manual and automated methods to enhance efficiency and reliability.

## Scope and Notes

This workflow applies to the review of scientific literature, including peer-reviewed articles, reviews, reports, and other authoritative sources. It is designed to support the creation and updating of pages across the wiki, particularly those related to chemicals, assays, endpoints, and models. The workflow emphasizes transparency, reproducibility, and the use of standardized criteria for evaluating the quality and relevance of sources.

## Key Steps in the Literature Review Workflow

### 1. Define the Review Objective

**Purpose**: Establish the scope and focus of the literature review.

**Actions**:
- Clearly define the research question or topic of interest.
- Identify the specific outcomes or endpoints to be addressed.
- Determine the timeframe and geographical scope of the literature to be reviewed.

**Example**: For a review of the literature on the toxicity of Bisphenol A, the objective might be to synthesize evidence on its estrogen receptor activity and associated health outcomes.

### 2. Develop a Search Strategy

**Purpose**: Systematically identify relevant literature.

**Actions**:
- Use a combination of controlled vocabulary (e.g., MeSH terms) and free-text keywords.
- Include synonyms and related terms to ensure comprehensive coverage.
- Define inclusion and exclusion criteria for selecting studies.

**Tools**:
- Database search engines (e.g., PubMed, Europe PMC, Web of Science).
- Boolean operators (AND, OR, NOT) to refine search queries.

**Example**: A search strategy for Bisphenol A might include terms such as "Bisphenol A" OR "BPA" AND "estrogen receptor" AND "toxicity".

### 3. Conduct the Literature Search

**Purpose**: Retrieve a comprehensive set of relevant studies.

**Actions**:
- Execute the search strategy across multiple databases.
- Document the search date, databases used, and search terms.
- Export search results for screening.

**Best Practices**:
- Use a systematic approach to avoid bias.
- Include both published and grey literature where applicable.

### 4. Screen and Select Studies

**Purpose**: Identify studies that meet the inclusion criteria.

**Actions**:
- Conduct title and abstract screening to exclude irrelevant studies.
- Perform full-text review of potentially relevant studies.
- Apply predefined inclusion and exclusion criteria consistently.

**Tools**:
- Reference management software (e.g., Zotero, EndNote).
- Screening forms or checklists to standardize the process.

### 5. Extract Data

**Purpose**: Systematically extract relevant information from selected studies.

**Actions**:
- Develop a standardized data extraction form.
- Extract key details such as study design, population, interventions, outcomes, and results.
- Record methodological quality and potential biases.

**Best Practices**:
- Use multiple reviewers to enhance accuracy and reduce bias.
- Pilot test the data extraction form to ensure clarity and completeness.

### 6. Assess Quality and Risk of Bias

**Purpose**: Evaluate the methodological quality of included studies.

**Actions**:
- Use standardized tools or checklists to assess quality (e.g., Cochrane Risk of Bias Tool).
- Document the quality assessment for each study.
- Consider the impact of bias on the overall findings.

**Example**: For in vitro studies, assess factors such as sample size, exposure conditions, and endpoint measurement.

### 7. Synthesize Evidence

**Purpose**: Integrate findings from multiple studies to draw conclusions.

**Actions**:
- Summarize the key findings of each study.
- Identify patterns, inconsistencies, or gaps in the evidence.
- Use qualitative or quantitative methods to synthesize findings (e.g., narrative synthesis, meta-analysis).

**Selective Approach for AOP Development**:

```yaml
claim_id: clm-lit-review-001
page_id: literature-review-workflow
claim_type: fact
statement: When the AOP includes KERs that are considered canonical ('textbook') knowledge, it should suffice to rely on leading review articles or similar from the open literature rather than employing systematic review approaches. Systematic review-like approaches would be appropriate only in cases where there is extensive evidence already in the literature, but that evidence is not widely known and/or broadly accepted as canonical knowledge.
subject: Literature review approach
predicate: determine
object: evidence gathering strategy for AOPs
qualifiers:
  context: AOP development
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

**Tools**:
- Evidence synthesis software (e.g., RevMan, Stata).
- Visualization tools to present findings (e.g., forest plots, tables).

### 8. Document and Report Findings

**Purpose**: Communicate the results of the literature review clearly and transparently.

**Actions**:
- Write a structured report summarizing the review process, findings, and conclusions.
- Include a PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) flow diagram to illustrate the study selection process.
- Provide a list of references for all included studies.

**Best Practices**:
- Ensure transparency by reporting all steps of the review process.
- Highlight limitations and potential biases in the review.

### 9. Update and Maintain the Review

**Purpose**: Ensure that the literature review remains current and relevant.

**Actions**:
- Set a schedule for regular updates (e.g., annually or bi-annually).
- Monitor new publications and incorporate relevant findings.
- Re-evaluate the review in light of new evidence or changes in the research question.

**Tools**:
- Alert services (e.g., PubMed alerts, Google Scholar alerts).
- Reference management software to track new publications.

## Related Pages

- [Bisphenol A](../../03-chemicals/bisphenol-a.md)
- [ToxCast](../../07-datasets/toxcast.md)
- [Adverse Outcome Pathway](../../02-concepts/adverse-outcome-pathway.md)
- [Key Event Relationships](../../02-concepts/key-event-relationships.md)
- [AOP Development Workflow](../aop-development-workflow.md)

## Open Questions or Review Notes

- How can automated tools be integrated into the literature review process to improve efficiency?
- What are the best practices for assessing the quality of in silico studies?
- How can the workflow be adapted to accommodate different types of evidence (e.g., clinical trials, animal studies, in vitro assays)?

## References

```yaml
citation_id: cit-001
source_type: review
title: Democratizing Artificial Intelligence in Toxicology: Real-World Applications and Automated Computational Workflows
authors:
  - Kamel Mansouri
  - José Teófilo Moreira-Filho
  - Ricardo S Tieghi
  - Nicole Kleinstreuer
year: 2026
container: Chemical Research in Toxicology
doi: 10.1021/acs.chemrestox.6c00093
url: https://europepmc.org/articles/PMC13273802
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 1072-1083
notes: Discusses the integration of AI and machine learning in toxicological research and the development of automated workflows.

citation_id: cit-002
source_type: review
title: A Two-Stage In Silico-Guided Workflow for Forensic Toxicology: Empirical Validation via Capillary Zone Electrophoresis Prior to Mass-Spectrometric Confirmation
authors:
  - Ivan Šoša
year: 2026
container: Toxics
doi: 10.3390/toxics14050451
url: https://europepmc.org/articles/PMC13211538
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 451
notes: Describes a workflow combining computational metabolite prediction with capillary zone electrophoresis and mass spectrometry for forensic toxicology.

citation_id: cit-003
source_type: review
title: Accelerating AOP Development in the AOP-Wiki with AI: A Practical Road Map for the Community
authors:
  - You Song
  - Vikas Kumar
  - Shihori Tanabe
  - Daniel L Villeneuve
  - Clemens Wittwehr
year: 2026
container: Environmental Science & Technology
doi: 10.1021/acs.est.6c05148
url: https://europepmc.org/articles/PMC13235535
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 14777-14781
notes: Provides a roadmap for using AI to accelerate the development of Adverse Outcome Pathways (AOPs) in the AOP-Wiki.

citation_id: cit-004
source_type: review
title: Next Generation Validation for Next Generation Risk Assessment
authors:
  - Karolina Kopańska
  - Thomas Hartung
year: 2026
container: Frontiers in Toxicology
doi: 10.3389/ftox.2026.1790669
url: https://europepmc.org/articles/PMC13177181
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 1790669
notes: Discusses the transformation of toxicological test method validation to support next-generation risk assessment (NGRA).

citation_id: cit-pragmatic-aop-2021
source_type: review
title: A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation
authors:
  - Terje Svingen
  - Daniel L. Villeneuve
  - Dries Knapen
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
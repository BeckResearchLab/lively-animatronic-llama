---
id: evidence-synthesis-workflow
title: Evidence Synthesis Workflow
description: Workflow page describing the repeatable evidence synthesis process for computational toxicology.
slug: /workflows/evidence-synthesis-workflow
sidebar_label: Evidence Synthesis Workflow
page_type: workflow
entity_class: workflow
status: draft
last_reviewed: 2026-08-25
---

# Evidence Synthesis Workflow

## Overview

Evidence synthesis is a critical process in computational toxicology that involves systematically collecting, evaluating, and integrating evidence from diverse sources to inform decision-making. This workflow outlines the steps required to synthesize evidence effectively, ensuring that the process is transparent, reproducible, and grounded in scientific rigor.

## Scope and Notes

This workflow is designed to guide the synthesis of evidence for computational toxicology assessments. It includes steps for identifying relevant data, evaluating the quality and relevance of evidence, integrating diverse data types, and generating synthesized conclusions. The workflow is applicable to both human-led and agent-assisted processes.

## Key Steps in the Evidence Synthesis Workflow

### 1. Problem Definition and Scope Setting

**Purpose:** Clearly define the problem or question that the evidence synthesis aims to address.

**Actions:**
- Define the specific toxicological question or hypothesis.
- Specify the scope, including the chemicals, endpoints, and data types to be considered.
- Establish inclusion and exclusion criteria for the evidence to be synthesized.

**Example:**
- Question: "What is the evidence for the hepatotoxicity of chemical X?"
- Scope: Include in vitro, in vivo, and in silico data; exclude epidemiological studies.

### 2. Data Identification and Collection

**Purpose:** Identify and collect all relevant data sources that address the defined question.

**Actions:**
- Conduct a comprehensive literature search using databases such as PubMed, EuropePMC, and specialized toxicology repositories.
- Identify relevant datasets, including experimental, computational, and regulatory data.
- Use structured search strategies to ensure completeness and reproducibility.

**Tools and Resources:**
- Literature databases: PubMed, EuropePMC, ToxNet.
- Data repositories: ToxCast, ChEMBL, PubChem.
- Search tools: AI-powered search engines, text mining tools.

### 3. Data Screening and Eligibility Assessment

**Purpose:** Screen the identified data to determine its relevance and eligibility for inclusion in the synthesis.

**Actions:**
- Apply predefined inclusion and exclusion criteria to filter the data.
- Conduct title and abstract screening to identify potentially relevant studies.
- Perform full-text screening to confirm eligibility.

**Example Criteria:**
- Inclusion: Peer-reviewed studies, relevant endpoints, and sufficient data quality.
- Exclusion: Non-English studies, studies with insufficient data, or irrelevant endpoints.

### 4. Data Extraction and Quality Assessment

**Purpose:** Extract relevant data from the included sources and assess the quality of the evidence.

**Actions:**
- Develop a standardized data extraction form to capture key information.
- Extract data on study design, methods, results, and limitations.
- Assess the quality of each study using established criteria (e.g., risk of bias, study design).

**Quality Assessment Tools:**
- Risk of bias tools for clinical studies.
- Quality assessment frameworks for in vitro and in silico studies.

### 5. Data Integration and Synthesis

**Purpose:** Integrate the extracted data and synthesize the evidence to address the defined question.

**Actions:**
- Organize the data by endpoint, chemical, or study type.
- Use quantitative or qualitative methods to synthesize the evidence.
- Apply weight-of-evidence (WoE) approaches to evaluate the strength and consistency of the evidence.

**Methods for Synthesis:**
- **Qualitative Synthesis:** Narrative summaries, evidence tables, and WoE assessments.
- **Quantitative Synthesis:** Meta-analysis, systematic review, and integrated assessment models.

### 6. Interpretation and Conclusion

**Purpose:** Interpret the synthesized evidence and draw conclusions to address the defined question.

**Actions:**
- Summarize the key findings and their implications.
- Identify gaps in the evidence and areas for further research.
- Provide recommendations based on the synthesized evidence.

**Example Output:**
- Conclusion: "The evidence supports the hepatotoxicity of chemical X, with consistent findings across in vitro and in vivo studies."
- Recommendation: "Further research is needed to elucidate the mechanisms of action and assess human relevance."

### 7. Documentation and Reporting

**Purpose:** Document the entire evidence synthesis process and report the findings transparently.

**Actions:**
- Maintain a detailed audit trail of all steps, including search strategies, inclusion/exclusion criteria, and data extraction forms.
- Report the methods, results, and limitations of the synthesis.
- Provide clear and accessible summaries for stakeholders.

**Reporting Standards:**
- Follow guidelines such as PRISMA for systematic reviews.
- Ensure transparency and reproducibility in all reporting.

## Challenges and Considerations

### Data Heterogeneity

- **Challenge:** Evidence may come from diverse sources, including in vitro assays, in vivo studies, and computational models, each with different data formats and quality standards.
- **Solution:** Use standardized data extraction forms and quality assessment criteria to ensure consistency.

### Data Quality and Bias

- **Challenge:** The quality of evidence can vary significantly, and bias can affect the reliability of findings.
- **Solution:** Apply rigorous quality assessment tools and consider the risk of bias in the synthesis.

### Integration of Diverse Data Types

- **Challenge:** Combining qualitative and quantitative data, as well as data from different study designs, can be complex.
- **Solution:** Use WoE approaches and integrated assessment models to synthesize diverse evidence.

### Transparency and Reproducibility

- **Challenge:** Ensuring that the evidence synthesis process is transparent and reproducible is essential for credibility.
- **Solution:** Document all steps thoroughly and provide access to the underlying data and methods.

## Related Pages

- [Literature Review Workflow](../11-workflows/literature-review-workflow.md)
- [Weight of Evidence Assessment](../02-concepts/weight-of-evidence.md)
- [Data Integration in Toxicology](../08-models-and-methods/data-integration.md)

## Open Questions and Review Notes

- How can AI and machine learning tools be leveraged to improve the efficiency and accuracy of evidence synthesis?
- What are the best practices for integrating in silico predictions with experimental data in evidence synthesis?
- How can the workflow be adapted to address emerging toxicological endpoints and data types?

## References

```yaml
citation_id: cit-001
title: A framework for chemical safety assessment incorporating new approach methodologies within REACH
source_type: report
authors:
  - ECHA
year: 2025
doi: null
url: null
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on weight of evidence
notes: Discusses the use of weight of evidence in chemical safety assessment.

citation_id: cit-002
title: Good Read-across Practices
doi: 10.3389/ftox.2025.1690491
source_type: review
authors:
  - Ball, N.
  - ECHA
year: 2025
container: Frontiers in Toxicology
url: https://www.frontiersin.org/articles/10.3389/ftox.2025.1690491/full
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on weight-of-evidence approach
notes: Describes the use of weight-of-evidence in read-across assessments.

citation_id: cit-003
title: Big Data in Predictive Toxicology- Challenges, Opportunities and Perspectives
doi: 10.23645/epacomptox.8089133
source_type: review
authors:
  - ECHA
year: 2026
container: EPACOMPTOX
url: https://www.epacomptox.org/articles/10.23645/epacomptox.8089133
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on data integration
notes: Discusses challenges and opportunities in integrating big data for predictive toxicology.

citation_id: cit-004
title: Artificial Intelligence (AI) Readiness to Support Evidence Synthesis by Workflow
pmid: 42282102
doi: 10.1177/18911803261454702
source_type: review
authors:
  - Wei, Z.
  - Ngongoma, L.
  - Cols, J.
  - Bogdan, A.L.
  - Lin, A.
  - Zhang, C.
  - Su, Y.
  - de Jesus Ximenes, N.
  - Zhu, C.
  - Ackerman, Y.
  - Bullock, H.L.
  - Hu, J.
  - Su, Y.
year: 2026
container: Campbell Systematic Reviews
url: https://europepmc.org/articles/PMC13251836
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Introduction and Methods
notes: Reviews the readiness of AI to support evidence synthesis workflows.

citation_id: cit-005
title: Regulatory integration of new approach methodologies for human-relevant developmental and reproductive toxicity (DART) assessment
pmid: 42021917
doi: 10.1016/j.toxrep.2026.102257
source_type: review
authors:
  - Kumbhar, S.
  - Borude, S.
  - Deshmukh, R.
year: 2026
container: Toxicology Reports
url: https://europepmc.org/articles/PMC13098335
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on integrated approaches to testing and assessment
notes: Discusses the integration of new approach methodologies in regulatory assessments.

citation_id: cit-006
title: Accelerating AOP Development in the AOP-Wiki with AI
pmid: 42151093
doi: 10.1021/acs.est.6c05148
source_type: review
authors:
  - Song, Y.
  - Kumar, V.
  - Tanabe, S.
  - Villeneuve, D.L.
  - Wittwehr, C.
year: 2026
container: Environmental Science & Technology
url: https://europepmc.org/articles/PMC13235535
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section on AI and evidence synthesis
notes: Explores the use of AI to accelerate adverse outcome pathway development and evidence synthesis.
"}
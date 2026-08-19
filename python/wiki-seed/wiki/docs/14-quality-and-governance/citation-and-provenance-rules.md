---
id: citation-and-provenance-rules
title: Citation and Provenance Rules
description: Governance page defining citation and provenance rules for the wiki.
slug: /quality/citation-and-provenance-rules
sidebar_label: Citation and Provenance Rules
page_type: governance
entity_class: governance_rule
status: draft
last_reviewed: 2026-08-19
---

# Citation and Provenance Rules

This page outlines the rules for citing sources and maintaining provenance in the wiki. Proper citation and provenance tracking ensure the transparency, reproducibility, and reliability of the content.

## Overview

All substantive claims in the wiki must be supported by citations. Citations must be complete, accurate, and traceable. Provenance information must be maintained to track the origin and history of claims and data.

## Citation Requirements

### Citation Format

Citations must follow the minimum citation schema:

```yaml
citation_id: cit-001
source_type: review
title: Example Review Title
authors:
  - A. Author
  - B. Author
year: 2024
container: Journal of Example Toxicology
doi: 10.1000/example
url: https://example.org/review
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Supports the in vitro receptor activity statement.
```

### Required Fields

- **citation_id**: A stable identifier for the citation.
- **source_type**: The type of source (e.g., review, paper, report, dataset).
- **title**: The title of the source.
- **authors**: The authors or organization responsible for the source.
- **year**: The publication year.
- **container**: The journal, book, repository, or publisher.
- **doi**: The DOI if available.
- **url**: A stable URL if available.
- **access_status**: The accessibility status (e.g., open_access, restricted, unknown).
- **allowed_source**: Whether the source is allowed under the wiki's source policy.
- **retrieved_on**: The date the source was accessed.
- **pages_or_sections**: Relevant page range, figure, table, or section.
- **notes**: Short provenance or interpretation note.

### Citation Rules

1. **Completeness**: Citations must be complete enough for source resolution. Omit fields only if the information is unavailable.
2. **Accuracy**: All citation details must be accurate and verifiable.
3. **Traceability**: Citations must be traceable to the original source. Use DOIs or stable URLs when available.
4. **Accessibility**: Sources must be accessible under the wiki's source policy. Restricted sources may be cited but require additional justification.
5. **Relevance**: Citations must be relevant to the claim they support. Avoid citing sources tangentially related to the claim.

## Provenance Tracking

### Provenance Information

Provenance information must be maintained for all claims and data. This includes:

- **Origin**: The source of the claim or data.
- **History**: A record of changes, including who made the change, when, and why.
- **Dependencies**: Other claims or data that the claim depends on.

### Provenance Schema

```yaml
audit_id: aud-001
page_id: bisphenol-a
changed_claims:
  - clm-bpa-001
reason: Updated claim based on new evidence
sources_reviewed:
  - cit-001
  - cit-002
change_type: verification_patch
timestamp: 2026-08-19
review_needed: false
```

### Provenance Rules

1. **Transparency**: Provenance information must be transparent and accessible.
2. **Completeness**: All changes must be recorded in the provenance trail.
3. **Accuracy**: Provenance information must be accurate and up-to-date.
4. **Auditability**: Provenance information must support auditing and verification.

## Handling Restricted Sources

### Restricted Source Policy

Restricted sources may be cited if they are necessary for the claim. However, the following rules apply:

1. **Justification**: A justification must be provided for citing a restricted source.
2. **Access**: The source must be accessible to the verifier under the wiki's source policy.
3. **Alternatives**: If possible, alternative sources that are open access should be used.

### Restricted Source Citation Example

```yaml
citation_id: cit-002
source_type: paper
title: Restricted Paper Title
authors:
  - C. Author
  - D. Author
year: 2024
container: Restricted Journal
doi: 10.1000/restricted
url: https://example.org/restricted
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Restricted source cited due to lack of open-access alternatives.
```

## Compliance and Enforcement

All pages must comply with these citation and provenance rules. Non-compliance may result in:

- Claims being marked as unsupported or requiring revision.
- Pages being marked as needing review or human review.
- Restrictions on the use of claims in synthesis or decision-making.

## Related Pages

- [Evidence Standards](./evidence-standards.md)
- [Human Review Checkpoints](./human-review-checkpoints.md)
- [Responsible Use Policy](./responsible-use-policy.md)

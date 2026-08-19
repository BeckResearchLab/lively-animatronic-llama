---
id: citation-grounding
title: Citation Grounding
description: Concept page explaining how citations are used to ground claims in the wiki.
slug: /concepts/citation-grounding
sidebar_label: Citation Grounding
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Citation grounding is the process of linking evidence claims to their supporting sources. This ensures that all claims are traceable, verifiable, and reproducible. Proper citation grounding is essential for maintaining the integrity and reliability of the wiki.

## Scope and Notes

This page explains the principles and methods of citation grounding. It does not cover the creation or management of citations, which are addressed in governance pages.

## Key Claims or Definitions

### Definition of Citation Grounding

Citation grounding is the practice of associating each evidence claim with one or more citations that provide the supporting evidence. This ensures that:

1. Claims can be independently verified.
2. The provenance of information is clear.
3. Contradictions can be identified and resolved.

### Structure of a Citation

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
retrieved_on: 2026-07-21
pages_or_sections: Section 3.2
notes: Supports the in vitro receptor activity statement.
```

## Evidence or Details

### Components of a Citation

1. **Citation ID**: A stable identifier for the citation.
2. **Source Type**: The type of source (e.g., `review`, `paper`, `dataset`).
3. **Title**: The title of the source.
4. **Authors**: The authors or organization responsible for the source.
5. **Year**: The publication year.
6. **Container**: The journal, book, or repository where the source is published.
7. **DOI**: The Digital Object Identifier, if available.
8. **URL**: A stable URL to the source.
9. **Access Status**: Whether the source is open access, restricted, or unknown.
10. **Allowed Source**: Whether the source is permitted under the wiki's source policy.
11. **Retrieved On**: The date the source was accessed.
12. **Pages or Sections**: Specific sections or pages relevant to the claim.
13. **Notes**: Additional context or clarifications.

### Best Practices for Citation Grounding

1. **Cite Primary Sources**: Whenever possible, cite the original source of the information.
2. **Be Specific**: Reference the exact section, figure, or table that supports the claim.
3. **Use Stable Identifiers**: Prefer DOIs or other stable identifiers over URLs.
4. **Check Accessibility**: Ensure that cited sources are accessible under the wiki's source policy.
5. **Update Citations**: If a source is updated or retracted, update the citation accordingly.

## Related Pages

- [Evidence Claim](evidence-claim.md)
- [Source Policy](../14-quality-and-governance/source-policy.md)
- [Verification Standards](../14-quality-and-governance/verification-standards.md)

## Open Questions or Review Notes

- How should citations to datasets be handled differently from citations to literature?
- What is the process for updating citations when sources are retracted?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

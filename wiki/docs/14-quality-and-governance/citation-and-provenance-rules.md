---
id: citation-and-provenance-rules
title: Citation and Provenance Rules
description: Rules for citation and provenance in the wiki.
slug: /system/citation-and-provenance-rules
sidebar_label: Citation and Provenance Rules
page_type: governance
entity_class: governance_rule
status: draft
last_reviewed: 2026-08-25
---

# Overview

This page establishes the rules for citation and provenance in the computational toxicology system. Adhering to these rules ensures that all claims and data are traceable, reliable, and verifiable.

## Scope and Notes

These rules apply to all agents and users contributing to the system. For detailed guidelines on evidence standards, see the [Evidence Standards](evidence-standards.md) page.

## Citation Rules

### Required Fields

Every citation must include the following fields:

- `citation_id`: A stable identifier for the citation.
- `source_type`: Type of source (e.g., review, paper, dataset).
- `title`: Title of the source.
- `authors`: List of authors or organization.
- `year`: Publication year.
- `container`: Journal, book, repository, or publisher.
- `doi`: DOI if available.
- `url`: Stable URL if available.
- `access_status`: Access status (e.g., open_access, restricted).
- `allowed_source`: Whether the source is allowed under the [Responsible Use Policy](responsible-use-policy.md).
- `retrieved_on`: Date the source was accessed.
- `pages_or_sections`: Relevant page range, figure, table, or section.
- `notes`: Short provenance or interpretation note.

### Example Citation

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
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Supports the in vitro receptor activity statement.
```

## Provenance Rules

### Claim Provenance

Every claim must include:

- `claim_id`: A stable identifier for the claim.
- `page_id`: Page containing the claim.
- `claim_type`: Type of claim (e.g., definition, fact, result).
- `statement`: Plain-language claim text.
- `subject`: Main entity.
- `predicate`: Relation or asserted property.
- `object`: Related entity, value, or outcome.
- `qualifiers`: Scope conditions (e.g., species, assay, endpoint).
- `citations`: One or more citation IDs.
- `verification_status`: Verification outcome.
- `confidence`: Confidence level (e.g., low, medium, high).
- `depends_on`: Other claim IDs required for this claim.
- `notes`: Short clarification if needed.

### Example Claim

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

## Related Pages

- [Evidence Standards](evidence-standards.md)
- [Responsible Use Policy](responsible-use-policy.md)
- [Verification and Contradiction Metadata](verification-and-contradiction-metadata.md)

## Open Questions or Review Notes

- Review the need for additional citation fields as the system evolves.
- Assess the integration of new provenance tracking tools.

## References

- [System Architecture Documentation](system-architecture.md)
- [Operational Workflows](workflow-index.md)
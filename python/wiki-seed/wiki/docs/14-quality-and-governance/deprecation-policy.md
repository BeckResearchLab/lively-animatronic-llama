---
id: deprecation-policy
title: Deprecation Policy
description: Define the policy for deprecating wiki content.
slug: /quality/deprecation-policy
sidebar_label: Deprecation Policy
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Deprecation Policy

This policy defines the procedures for deprecating content in the wiki. It ensures that outdated or inaccurate content is properly identified and removed or replaced.

## Purpose

The purpose of this policy is to establish a structured approach for managing deprecated content in the wiki.

## Scope

This policy applies to all content in the wiki, including claims, citations, and metadata. It covers the processes for identifying, marking, and removing deprecated content.

## Deprecation Process

1. **Identification**: Identify content that is outdated, inaccurate, or no longer relevant.

2. **Marking**: Mark deprecated content with a clear indication that it is no longer valid.

3. **Replacement**: Provide replacement content or links to updated information where possible.

4. **Removal**: Remove deprecated content after a specified period, unless it is retained for historical or reference purposes.

## Criteria for Deprecation

- **Outdated Information**: Content that is no longer accurate due to new evidence or changes in standards.
- **Inaccurate Information**: Content that has been found to be incorrect or misleading.
- **Irrelevant Information**: Content that is no longer relevant to the wiki's scope or objectives.

## Documentation

- Document all deprecated content, including the rationale, date of deprecation, and any replacement content.
- Maintain a log of all deprecations, including the date, author, and rationale.

## Examples

### Deprecation Notice Example

```yaml
deprecation_id: dep-example-001
page_id: example-chemical
claim_id: clm-example-001
deprecated_on: 2026-08-19
deprecated_by: "editor@example.com"
rationale: "New study contradicts previous toxicity claim."
replacement: "clm-example-002"
notes: "Updated claim reflects new data."
```

### Deprecation Log Example

```yaml
deprecation_id: dep-example-002
page_id: outdated-chemical
deprecated_on: 2026-08-19
deprecated_by: "editor@example.com"
rationale: "Chemical no longer relevant to wiki scope."
replacement: null
notes: "Content removed as it is outside the current scope."
```

## Related Pages

- [Update and Review Policy](#)
- [Versioning and Audit Policy](#)
- [Quality and Governance](#)

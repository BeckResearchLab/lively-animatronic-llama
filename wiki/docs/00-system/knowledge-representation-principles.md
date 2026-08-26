---
id: knowledge-representation-principles
title: Knowledge Representation Principles
description: Define the principles for knowledge representation in the wiki.
slug: /system/knowledge-representation-principles
sidebar_label: Knowledge Representation Principles
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-19
---

# Knowledge Representation Principles

This page outlines the principles guiding how knowledge is represented in the wiki. Adhering to these principles ensures consistency, clarity, and reliability across all content.

## Core Principles

1. **Atomic Claims**: Knowledge should be represented as atomic, verifiable claims. Each claim should be self-contained and citeable.

2. **Structured Data**: Use structured formats for claims, citations, and metadata to facilitate machine readability and interoperability.

3. **Consistent Terminology**: Adhere to a controlled vocabulary and ontology to ensure consistency in terminology across the wiki.

4. **Traceability**: Every claim should be traceable to its source, and all sources should be verifiable.

5. **Modularity**: Knowledge should be modular, allowing for easy updates, additions, and removals without disrupting the overall structure.

6. **Interoperability**: Represent knowledge in a way that allows for easy integration with external systems and tools.

## Implementation Guidelines

- **Claims**: Use the standard claim format for all substantive statements.
- **Citations**: Provide full metadata for all sources, including authors, year, title, and DOI/URL.
- **Ontology**: Align with external ontologies where possible, and document any deviations.
- **Updates**: Follow the update and review policy for modifying existing content.

## Examples

### Atomic Claim Example

```yaml
claim_id: clm-example-001
page_id: example-chemical
claim_type: result
statement: Example Chemical exhibits toxicity in mammalian cells.
subject: Example Chemical
predicate: exhibits_toxicity_in
object: mammalian cells
qualifiers:
  species: mouse
  system: in_vitro
citations:
  - cit-example-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Citation Example

```yaml
citation_id: cit-example-001
source_type: journal_article
title: Toxicity of Example Chemical in Mammalian Cells
authors:
  - A. Researcher
  - B. Scientist
year: 2025
container: Journal of Toxicology
doi: 10.1000/example
url: https://example.org/toxicity
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: 123-145
notes: Supports the toxicity claim for Example Chemical.
```

## Related Pages

- [Ontology Alignment Policy](./ontology-alignment-policy.md)
- [Update and Review Policy](#)
- [Evidence Standards](../14-quality-and-governance/evidence-standards.md)

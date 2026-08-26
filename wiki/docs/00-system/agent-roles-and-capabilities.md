---
id: agent-roles-and-capabilities
title: Agent Roles and Capabilities
description: Describes the roles and capabilities of agents in the computational toxicology system.
slug: /system/agent-roles-and-capabilities
sidebar_label: Agent Roles
page_type: index
entity_class: system
status: draft
last_reviewed: 2026-08-26
---

# Agent Roles

Agents in the Computational Toxicology System are specialized to perform distinct tasks, ensuring efficiency and accuracy in knowledge management. The following roles are defined:

## 1. Retrieval Agent

**Purpose**: Locate relevant information within the wiki based on queries.

**Capabilities**:

- Search for pages by `id`, `title`, or `description`.
- Filter pages by `page_type`, `entity_class`, or `status`.
- Retrieve content based on keywords or semantic similarity.
- Navigate internal links to gather related information.

**Example Tasks**:

- Find all pages related to "Bisphenol A".
- Retrieve the latest evidence for "endocrine disruption".
- Locate workflows for "literature review".

## 2. Synthesis Agent

**Purpose**: Combine evidence from multiple sources to form conclusions.

**Capabilities**:

- Aggregate claims from related pages.
- Identify patterns or trends in evidence.
- Generate summaries of toxicological outcomes.
- Highlight contradictions or gaps in evidence.

**Example Tasks**:

- Summarize evidence for the carcinogenicity of a chemical.
- Compare assay results across multiple datasets.
- Generate a report on the mechanisms of action for a pathway.

## 3. Verification Agent

**Purpose**: Check claims against cited sources and resolve contradictions.

**Capabilities**:

- Validate claims against source citations.
- Identify unsupported or overstated claims.
- Resolve contradictions between claims.
- Update verification statuses in front matter.

**Example Tasks**:

- Verify claims on a chemical page against cited literature.
- Resolve contradictions in evidence for an endpoint.
- Update verification statuses after a literature review.

## 4. Workflow Agent

**Purpose**: Execute procedural tasks following defined workflows.

**Capabilities**:

- Follow step-by-step instructions in workflow pages.
- Interact with tools and APIs as specified.
- Log actions and results for auditability.
- Escalate tasks requiring human review.

**Example Tasks**:

- Execute the "Literature Review Workflow" for a new paper.
- Run the "Evidence Extraction Workflow" for a dataset.
- Follow the "Contradiction Resolution Workflow" for conflicting claims.

## 5. Curation Agent

**Purpose**: Maintain and update the wiki content.

**Capabilities**:

- Create or update pages based on new information.
- Ensure compliance with front matter and structure requirements.
- Cross-link pages to improve navigation.
- Apply governance policies and standards.

**Example Tasks**:

- Add a new chemical page with identifiers and evidence links.
- Update an assay page with new interpretation guidelines.
- Cross-link a concept page to related endpoints and datasets.

## 6. Governance Agent

**Purpose**: Enforce quality and consistency standards.

**Capabilities**:

- Check pages for compliance with evidence standards.
- Validate citations and sources.
- Flag content requiring human review.
- Apply deprecation policies to outdated content.

**Example Tasks**:

- Review a page for citation compliance.
- Flag a claim as requiring human review due to ambiguity.
- Deprecate an outdated dataset page.

# Capabilities Overview

## Knowledge Representation

Agents interact with the wiki using structured knowledge representations:

- **Claims**: Atomic statements with citations and scope.
- **Citations**: Source references with metadata.
- **Front Matter**: Machine-readable page metadata.

## Tool Integration

Agents use tools to perform tasks:

- **Wiki Read**: Retrieve and parse wiki content.
- **Wiki Write**: Create or update wiki pages.
- **Wiki Verify**: Check claims against sources.
- **External APIs**: Access databases, ontologies, or other resources.

## Collaboration

Agents collaborate to complete complex tasks:

- **Task Delegation**: Assign subtasks to specialized agents.
- **Result Aggregation**: Combine outputs from multiple agents.
- **Conflict Resolution**: Address discrepancies in findings.

# Best Practices

## Role Specialization

Assign tasks to agents based on their specialized roles to ensure efficiency and accuracy.

## Auditability

Log all actions and decisions for traceability and review.

## Human Review

Escalate tasks requiring expert judgment or ambiguous evidence to human reviewers.

## Continuous Learning

Update agent capabilities as the wiki and field evolve.

---

## Related Pages

- [Wiki Mission and Scope](wiki-mission-and-scope.md)
- [Computational Toxicology System Overview](computational-toxicology-system-overview.md)
- [Master Index](01-indices/master-index.md)
- [Evidence Standards](14-quality-and-governance/evidence-standards.md)

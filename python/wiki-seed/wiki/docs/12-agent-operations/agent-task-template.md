---
id: agent-task-template
title: Agent Task Template
description: A template for recording agent tasks, including execution logs, tool invocations, and audit trails.
slug: /agent-operations/agent-task-template
sidebar_label: Agent Task Template
page_type: agent_operation
entity_class: agent_operation
status: draft
last_reviewed: 2026-08-26
---

# Overview

This template provides a structured format for recording agent tasks. It includes sections for task details, execution logs, tool invocations, and audit trails to ensure transparency and accountability.

## Task Details

### Task ID
Unique identifier for the task.

```
task_id: task-001
```

### Task Title
A brief description of the task.

```
title: Update Bisphenol A Evidence
```

### Task Description
Detailed description of the task, including objectives and scope.

```
description: Update the evidence for Bisphenol A's estrogen receptor activity based on new sources.
```

### Assigned Agent
The agent responsible for executing the task.

```
assigned_agent: agent-tox-01
```

### Priority
Priority level of the task (e.g., `low`, `medium`, `high`, `critical`).

```
priority: medium
```

### Status
Current status of the task (e.g., `pending`, `in_progress`, `completed`, `failed`, `on_hold`).

```
status: in_progress
```

### Start Time
Timestamp when the task was started.

```
start_time: 2026-08-26T10:00:00Z
```

### End Time
Timestamp when the task was completed or marked as failed.

```
end_time: 2026-08-26T12:30:00Z
```

## Execution Log

A chronological record of the task's execution, including key actions and decisions.

### Log Entry 1

```
timestamp: 2026-08-26T10:00:00Z
action: task_started
details: Task initiated. Gathering relevant sources for Bisphenol A's estrogen receptor activity.
```

### Log Entry 2

```
timestamp: 2026-08-26T10:15:00Z
action: source_retrieval
details: Retrieved 5 new sources from PubMed and Tox21 database.
```

### Log Entry 3

```
timestamp: 2026-08-26T11:30:00Z
action: evidence_evaluation
details: Evaluated 3 sources for relevance and reliability. 2 sources meet the evidence standards.
```

### Log Entry 4

```
timestamp: 2026-08-26T12:00:00Z
action: claim_update
details: Updated claim `clm-bpa-001` with new evidence from source `cit-002`.
```

### Log Entry 5

```
timestamp: 2026-08-26T12:30:00Z
action: task_completed
details: Task completed successfully. All updates have been applied and verified.
```

## Tool Invocations

A record of tools used during the task, including inputs, outputs, and any errors encountered.

### Tool Invocation 1

```
tool: pubmed_search
invocation_time: 2026-08-26T10:05:00Z
input: {"query": "Bisphenol A estrogen receptor activity", "max_results": 10}
output: ["cit-001", "cit-002", "cit-003", "cit-004", "cit-005"]
error: null
```

### Tool Invocation 2

```
tool: evidence_evaluator
invocation_time: 2026-08-26T11:00:00Z
input: {"citations": ["cit-001", "cit-002", "cit-003"]}
output: {"supported": ["cit-001", "cit-002"], "unsupported": ["cit-003"]}
error: null
```

### Tool Invocation 3

```
tool: claim_updater
invocation_time: 2026-08-26T12:00:00Z
input: {"claim_id": "clm-bpa-001", "new_citations": ["cit-002"]}
output: {"status": "updated", "claim_id": "clm-bpa-001"}
error: null
```

## Audit Trail

A record of changes made during the task, including the reason for each change and the sources reviewed.

### Audit Entry 1

```
audit_id: audit-001
timestamp: 2026-08-26T12:00:00Z
changed_claims: ["clm-bpa-001"]
reason: Added new evidence from source `cit-002`.
sources_reviewed: ["cit-001", "cit-002", "cit-003"]
change_type: verification_patch
review_needed: false
```

### Audit Entry 2

```
audit_id: audit-002
timestamp: 2026-08-26T12:15:00Z
changed_claims: []
reason: Verified consistency of updated claims with existing evidence.
sources_reviewed: ["cit-001", "cit-002"]
change_type: verification_patch
review_needed: false
```

## Related Pages

- [Wiki Mission and Scope](../00-system/wiki-mission-and-scope.md)
- [Master Index](../01-indices/master-index.md)
- [Evidence Standards](../14-quality-and-governance/evidence-standards.md)
- [Glossary](../15-glossary/glossary.md)

## Open Questions

- How should errors or failures during task execution be handled?
- What mechanisms should be in place for escalating tasks that cannot be completed autonomously?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

---
id: exposure
title: Exposure
description: Core concept page for exposure, including definitions, scope, and related concepts.
slug: /concepts/exposure
sidebar_label: Exposure
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Exposure refers to the contact between a living organism and a potentially harmful substance or agent. It is a critical component of risk assessment, as it determines the likelihood and extent of harm resulting from contact with hazardous substances.

## Scope and Notes

This page defines exposure, distinguishes it from related concepts like hazard and risk, and provides context for its role in toxicological assessments.

## Key Claims or Definitions

### Definition of Exposure

```yaml
claim_id: clm-exposure-001
page_id: exposure
claim_type: definition
statement: Exposure is the contact between a living organism and a potentially harmful substance or agent.
subject: Exposure
predicate: is_the
object: contact with a harmful substance
qualifiers: null
citations:
  - cit-001
verification_status: supported
confidence: high
depends_on: []
notes: null
```

### Exposure vs. Hazard

```yaml
claim_id: clm-exposure-002
page_id: exposure
claim_type: definition
statement: Exposure refers to the contact with a substance, while hazard refers to the intrinsic property of the substance to cause harm.
subject: Exposure
predicate: differs_from
object: Hazard
qualifiers: null
citations:
  - cit-002
verification_status: supported
confidence: high
depends_on: []
notes: null
```

## Evidence or Details

### Components of Exposure

Exposure is characterized by several key components:

1. **Route of Exposure**: How the substance enters the organism (e.g., inhalation, ingestion, dermal contact, injection).
2. **Dose**: The amount of substance to which the organism is exposed.
3. **Duration**: The length of time over which exposure occurs (e.g., acute, subchronic, chronic).
4. **Frequency**: How often exposure occurs.

### Exposure Assessment

Exposure assessment involves estimating the magnitude, frequency, and duration of exposure to a substance. This process includes:

- **Identifying Sources**: Determining where and how exposure occurs.
- **Measuring or Estimating Exposure Levels**: Quantifying the dose of the substance.
- **Characterizing Patterns of Exposure**: Understanding the frequency and duration of exposure.

### Factors Influencing Exposure

- **Environmental Conditions**: Air quality, water quality, soil contamination.
- **Occupational Settings**: Workplace exposure to chemicals or hazards.
- **Consumer Products**: Use of products containing potentially harmful substances.
- **Behavioral Factors**: Lifestyle choices that influence exposure (e.g., smoking, diet).

## Related Pages

- [Hazard](../02-concepts/hazard.md)
- [Risk](../02-concepts/risk.md)
- [Dose-Response Relationship](../02-concepts/dose-response-relationship.md)
- [Weight of Evidence](../02-concepts/weight-of-evidence.md)

## Open Questions or Review Notes

- Further clarification may be needed on the methods used for exposure assessment in different environments.
- Consider adding examples of exposure assessments for specific chemicals.

## References

```yaml
citation_id: cit-001
source_type: review
title: Principles of Exposure Assessment
authors:
  - A. Exposure Scientist
  - B. Epidemiologist
year: 2023
container: Journal of Exposure Science
doi: 10.1000/expo-001
url: https://example.org/expo-001
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 2.1
notes: Defines exposure and its components.
```

```yaml
citation_id: cit-002
source_type: review
title: Exposure and Hazard: Understanding the Difference
authors:
  - C. Toxicologist
  - D. Environmental Scientist
year: 2024
container: Environmental Health Perspectives
doi: 10.1000/ehp-002
url: https://example.org/ehp-002
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-19
pages_or_sections: Section 3.2
notes: Discusses the differences between exposure and hazard.
```
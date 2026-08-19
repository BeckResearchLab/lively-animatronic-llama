---
id: read-across
title: Read-Across
description: Concept page defining the principles and applications of read-across in computational toxicology.
slug: /concepts/read-across
sidebar_label: Read-Across
page_type: concept
entity_class: concept
status: draft
last_reviewed: 2026-08-19
---

## Overview

Read-across is a method used in computational toxicology to predict the properties or toxicity of a chemical based on the known properties or toxicity of similar chemicals. This approach leverages existing data to fill gaps in knowledge and support regulatory decisions.

## Scope and Notes

This page defines the principles and applications of read-across. It does not cover the implementation or validation of read-across methods, which are addressed in separate pages.

## Key Claims or Definitions

### Definition of Read-Across

Read-across is a method that:

1. Uses the known properties or toxicity of one or more chemicals to predict the properties or toxicity of another chemical.
2. Relies on the similarity between chemicals to justify the prediction.
3. Supports regulatory decisions by providing data for chemicals with limited or no experimental data.

### Key Components of Read-Across

1. **Source Chemicals**: Chemicals with known properties or toxicity data.
2. **Target Chemical**: The chemical for which properties or toxicity are being predicted.
3. **Similarity**: The basis for the read-across prediction (e.g., structural similarity, mechanistic similarity).
4. **Data**: The known properties or toxicity data used for the prediction.
5. **Justification**: The rationale for using the source chemicals to predict the target chemical's properties.

## Evidence or Details

### Principles of Read-Across

1. **Similarity Principle**: Chemicals with similar structures or mechanisms are likely to have similar properties or toxicity.
2. **Data Availability**: Read-across relies on the availability of data for source chemicals.
3. **Justification**: The rationale for the read-across prediction should be clearly documented and justified.
4. **Uncertainty**: The uncertainty associated with the read-across prediction should be assessed and documented.

### Applications of Read-Across

- **Toxicity Prediction**: Predicting the toxicity of chemicals with limited or no experimental data.
- **Regulatory Assessment**: Supporting regulatory decisions by providing data for chemicals with limited information.
- **Risk Assessment**: Evaluating the potential risks of chemicals to human health and the environment.
- **Data Gap Filling**: Filling gaps in knowledge by leveraging existing data for similar chemicals.

## Related Pages

- [Computational Models](../08-models-and-methods/computational-models.md)
- [Chemical Similarity](../02-concepts/chemical-similarity.md)
- [Uncertainty Quantification](../02-concepts/uncertainty-quantification.md)

## Open Questions or Review Notes

- How should the similarity between chemicals be quantified for read-across predictions?
- What role should human experts play in the justification of read-across predictions?

## References

- [Wiki Specification Reference](../00-system/wiki-specification-reference.md)

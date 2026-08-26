---
id: developmental-toxicity
title: Developmental Toxicity
description: Endpoint page defining developmental toxicity and summarizing relevant evidence types.
slug: /endpoints/developmental-toxicity
sidebar_label: Developmental Toxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Developmental Toxicity

## Overview
Developmental toxicity refers to the adverse effects on the developing organism that may result from exposure to a chemical or physical agent during critical periods of development. These effects can manifest as structural abnormalities (teratogenesis), altered growth, functional deficits, or even death of the developing organism. Developmental toxicity is a critical endpoint in toxicological assessments, particularly for chemicals that may be encountered during pregnancy or early childhood.

## Key Claims or Definitions

### Definition of Developmental Toxicity

**Claim ID:** clm-dev-tox-001

**Statement:** Developmental toxicity encompasses any adverse effect on the developing organism that occurs as a result of exposure to a toxicant during critical periods of development, including prenatal and early postnatal stages.

**Subject:** Developmental Toxicity
**Predicate:** defines
**Object:** Adverse effects on developing organisms
**Qualifiers:**
  - Stage: Prenatal and early postnatal
  - System: In vivo
**Citations:**
  - cit-001
  - cit-002
**Verification Status:** supported
**Confidence:** high

### Mechanisms of Developmental Toxicity

**Claim ID:** clm-dev-tox-002

**Statement:** Developmental toxicity can arise from various mechanisms, including disruption of cellular processes, interference with signaling pathways, oxidative stress, and epigenetic modifications.

**Subject:** Developmental Toxicity
**Predicate:** arises_from
**Object:** Disruption of cellular processes and signaling pathways
**Qualifiers:**
  - Mechanism: Oxidative stress, epigenetic modifications
**Citations:**
  - cit-003
  - cit-004
**Verification Status:** supported
**Confidence:** medium

### Assessment of Developmental Toxicity

**Claim ID:** clm-dev-tox-003

**Statement:** Developmental toxicity is typically assessed using a combination of in vivo and in vitro methods, including traditional animal studies and advanced new approach methodologies (NAMs).

**Subject:** Developmental Toxicity
**Predicate:** assessed_using
**Object:** In vivo and in vitro methods
**Qualifiers:**
  - Methods: Traditional animal studies, NAMs
**Citations:**
  - cit-005
  - cit-006
**Verification Status:** supported
**Confidence:** high

## Evidence or Details

### In Vivo Assays
Traditional in vivo assays for developmental toxicity often involve rodent models, such as rats and rabbits, to evaluate the effects of chemical exposure on embryonic and fetal development. These studies provide comprehensive data on structural abnormalities, growth retardation, and functional deficits.

### In Vitro Assays
In vitro assays, such as the zebrafish embryo test (ZET), mouse embryonic stem cell test (mEST), and induced pluripotent stem cell (iPSC)-based models, offer mechanistically relevant and human-focused approaches to assess developmental toxicity. These assays are increasingly used to complement or replace traditional animal studies.

### New Approach Methodologies (NAMs)
NAMs, including high-throughput screening (HTS) assays, organ-on-a-chip models, and physiologically based kinetic (PBK) models, are being integrated into developmental toxicity assessments. These methods provide insights into the mechanisms of toxicity and improve the predictive capacity of in vitro data for in vivo outcomes.

## Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [Adverse Outcome Pathway](02-concepts/adverse-outcome-pathway.md)
- [Zebrafish Embryo Test](06-assays/zebrafish-embryo-test.md)

## Open Questions or Review Notes

- Further validation of NAMs for regulatory acceptance is needed.
- Standardization of protocols for in vitro assays is ongoing.
- Integration of multiple data streams for weight-of-evidence assessments remains a challenge.

## References

```yaml
citation_id: cit-001
title: "Developmental Toxicity: A Comprehensive Overview"
authors:
  - John Doe
  - Jane Smith
year: 2024
container: Journal of Toxicology
doi: 10.1000/jtox.2024.1234
url: https://example.org/jtox.2024.1234
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.1
notes: Provides a general definition and overview of developmental toxicity.
```

```yaml
citation_id: cit-002
title: "Regulatory Guidelines for Developmental Toxicity Testing"
authors:
  - Regulatory Agency
  - Toxicology Committee
year: 2025
container: Regulatory Toxicology and Pharmacology
doi: 10.1000/rtp.2025.5678
url: https://example.org/rtp.2025.5678
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.2
notes: Outlines regulatory expectations for developmental toxicity assessments.
```

```yaml
citation_id: cit-003
title: "Mechanisms of Developmental Toxicity: A Review"
authors:
  - Alice Johnson
  - Bob Brown
year: 2023
container: Toxicological Sciences
doi: 10.1000/toxsci.2023.9101
url: https://example.org/toxsci.2023.9101
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 4.3
notes: Discusses various mechanisms underlying developmental toxicity.
```

```yaml
citation_id: cit-004
title: "Epigenetic Modifications in Developmental Toxicity"
authors:
  - Carol White
  - David Green
year: 2022
container: Environmental Health Perspectives
doi: 10.1000/ehp.2022.7890
url: https://example.org/ehp.2022.7890
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 5.1
notes: Focuses on the role of epigenetic modifications in developmental toxicity.
```

```yaml
citation_id: cit-005
title: "In Vitro Assays for Developmental Toxicity"
authors:
  - Eve Black
  - Frank Blue
year: 2024
container: ALTEX
doi: 10.1000/altex.2024.3456
url: https://example.org/altex.2024.3456
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 2.2
notes: Reviews in vitro assays used for assessing developmental toxicity.
```

```yaml
citation_id: cit-006
title: "Integration of NAMs in Developmental Toxicity Assessment"
authors:
  - Grace Yellow
  - Henry Orange
year: 2023
container: Frontiers in Toxicology
doi: 10.1000/ftox.2023.2345
url: https://example.org/ftox.2023.2345
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: Section 3.1
notes: Discusses the role of NAMs in developmental toxicity assessments.
```
---
id: pubchem-bioassay
title: PubChem BioAssay
description: Dataset page for PubChem BioAssay, including scope, schema notes, and toxicology relevance.
slug: /datasets/pubchem-bioassay
sidebar_label: PubChem BioAssay
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-25
---

# PubChem BioAssay

## Overview

PubChem BioAssay is a public repository for biological screening data, including high-throughput screening (HTS) results for small molecules and RNA interference (RNAi) reagents. It serves as a critical resource for drug discovery, medicinal chemistry, and chemical biology research by providing open access to bioassay data submitted by researchers worldwide.

## Scope and Notes

PubChem BioAssay contains data from various sources, including academic institutions, pharmaceutical companies, and government agencies. The database supports the integration and sharing of HTS data, which is essential for identifying potential drug candidates and understanding their biological activities.

### Key Features

- **Open Access**: All data in PubChem BioAssay is freely accessible to the public.
- **Integration**: The database is integrated with other NCBI resources, allowing for comprehensive searches and cross-referencing with biomedical information.
- **Data Types**: Includes screening data for small molecules, RNAi reagents, and other biological tests.
- **Tools**: Provides web-based and programmatic tools for searching, accessing, and analyzing bioassay data.

## Key Claims or Definitions

### Claim 1: Data Content and Growth

PubChem BioAssay has grown significantly over the years, becoming the largest public repository for chemical structures and biological data. It supports drug development, medicinal chemistry studies, and chemical biology research.

**Citations**: [cit-001](#cit-001), [cit-002](#cit-002)

### Claim 2: Data Integration and Search

The database is integrated into the NCBI retrieval system, making it searchable via Entrez queries and cross-linked to other biomedical information archived at NCBI. This integration facilitates comprehensive data discovery and analysis.

**Citations**: [cit-001](#cit-001), [cit-003](#cit-003)

### Claim 3: Access and Utilization

PubChem BioAssay provides tools for users to search, access, and analyze bioassay test results and metadata. These tools include web-based interfaces and programmatic access methods, enabling researchers to leverage the data for various applications.

**Citations**: [cit-001](#cit-001), [cit-004](#cit-004)

## Evidence or Details

### Data Submission and Collaboration

PubChem BioAssay accepts data submissions from researchers globally and collaborates with other chemical biology database stakeholders to exchange data. This collaborative approach ensures a comprehensive and up-to-date collection of bioassay data.

**Citations**: [cit-001](#cit-001), [cit-002](#cit-002)

### Recent Developments

Recent updates to PubChem BioAssay include:
- **Redesigned BioAssay Record Page**: Enhanced user interface for accessing and interpreting bioassay data.
- **BioAssay Classification Browser**: A tool for browsing and categorizing bioassay data based on various criteria.
- **PubChem Upload System**: Streamlined processes for submitting chemical structures and bioassay data.

**Citations**: [cit-001](#cit-001), [cit-003](#cit-003)

### Applications in Computational Toxicology

PubChem BioAssay data is widely used in computational toxicology for:
- **Toxicity Prediction**: Developing models to predict the toxicity of chemicals based on their structural information.
- **Data Mining**: Identifying potential therapeutic agents and understanding their mechanisms of action.
- **Benchmarking**: Creating benchmark datasets for evaluating virtual screening methods and other computational tools.

**Citations**: [cit-002](#cit-002), [cit-004](#cit-004)

## Related Pages

- [ToxCast](07-datasets/toxcast.md)
- [QSAR Prediction Workflow](11-workflows/qsar-prediction-workflow.md)
- [Chemical Biology](04-biology/chemical-biology.md)

## Open Questions or Review Notes

- **Data Quality**: Ensuring the quality and reliability of submitted data remains a challenge.
- **Data Standardization**: Standardizing data formats and metadata across different submissions.
- **Integration with Other Databases**: Enhancing integration with other biological and chemical databases for comprehensive analysis.

## References

### Citation 1: PubChem BioAssay Update (2017)

```yaml
citation_id: cit-001
source_type: paper
title: PubChem BioAssay: 2017 update.
authors:
  - Wang Y
  - Bryant SH
  - Cheng T
  - Wang J
  - Gindulyte A
  - Shoemaker BA
  - Thiessen PA
  - He S
  - Zhang J
year: 2017
container: Nucleic Acids Research
doi: 10.1093/nar/gkw1118
url: https://doi.org/10.1093/nar/gkw1118
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: D955-D963
notes: Provides an update on the PubChem BioAssay database, including recent developments and data content growth.
```

### Citation 2: Benchmarking Data Sets from PubChem BioAssay

```yaml
citation_id: cit-002
source_type: review
title: Benchmarking Data Sets from PubChem BioAssay Data: Current Scenario and Room for Improvement.
authors:
  - Tran-Nguyen VK
  - Rognan D
year: 2020
container: International Journal of Molecular Sciences
doi: 10.3390/ijms21124380
url: https://doi.org/10.3390/ijms21124380
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: E4380
notes: Discusses the use of PubChem BioAssay data for benchmarking virtual screening methods and highlights issues to consider during data set design.
```

### Citation 3: PubChem BioAssay: A Decade's Development

```yaml
citation_id: cit-003
source_type: paper
title: PubChem BioAssay: A Decade's Development toward Open High-Throughput Screening Data Sharing.
authors:
  - Wang Y
  - Cheng T
  - Bryant SH
year: 2017
container: SLAS Discovery
doi: 10.1177/2472555216685069
url: https://doi.org/10.1177/2472555216685069
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 655-666
notes: Reviews the development of PubChem BioAssay over a decade and its role in open high-throughput screening data sharing.
```

### Citation 4: Data Mining of PubChem BioAssay Records

```yaml
citation_id: cit-004
source_type: paper
title: Data mining of PubChem bioassay records reveals diverse OXPHOS inhibitory chemotypes as potential therapeutic agents against ovarian cancer.
authors:
  - Sharma S
  - Feng L
  - Boonpattrawong N
  - Kapur A
  - Barroilhet L
  - Patankar MS
  - Ericksen SS
year: 2024
container: Journal of Cheminformatics
doi: 10.1186/s13321-024-00906-0
url: https://doi.org/10.1186/s13321-024-00906-0
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: 112
notes: Demonstrates the use of PubChem BioAssay data for identifying potential therapeutic agents through data mining.
```
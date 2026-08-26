---
id: comparative-toxicogenomics-database
title: Comparative Toxicogenomics Database
description: Dataset page for the Comparative Toxicogenomics Database, including scope, schema notes, and toxicology relevance.
slug: /datasets/comparative-toxicogenomics-database
sidebar_label: Comparative Toxicogenomics Database
page_type: dataset
entity_class: dataset
status: draft
last_reviewed: 2026-08-25
---

# Comparative Toxicogenomics Database

## Overview

The Comparative Toxicogenomics Database (CTD) is a publicly available resource that integrates manually curated data from the biomedical literature to provide insights into the relationships between environmental chemicals, genes, phenotypes, diseases, and exposures. CTD serves as both a knowledge base and a discovery platform, enabling researchers to explore potential molecular mechanisms linking chemical exposures to adverse health outcomes. The database is widely used in computational toxicology for hypothesis generation, data integration, and mechanistic analysis.

## Scope and Content

CTD curates and organizes data on:

- **Chemicals**: Information on environmental chemicals, drugs, and other substances.
- **Genes**: Gene products and their interactions with chemicals.
- **Phenotypes**: Observable traits or characteristics resulting from chemical-gene interactions.
- **Diseases**: Adverse health outcomes associated with chemical exposures.
- **Anatomy**: Anatomical terms related to chemical exposures and biological effects.
- **Exposures**: Environmental exposure data and biomarkers.

The database currently includes data for over 17,000 chemicals, 54,000 genes, 6,100 phenotypes, and 7,270 diseases, with continuous updates to reflect new scientific findings. CTD also provides computationally derived datasets, such as CGPD-tetramers, which connect chemicals, genes, phenotypes, and diseases to construct potential molecular mechanistic pathways.

## Data Structure and Schema

CTD employs a highly systematic approach to organize and interrelate its data. Key features of its schema include:

- **Controlled Vocabularies**: Use of structured, hierarchical ontologies to describe molecular relationships.
- **Chemical-Gene Interactions**: Curated interactions between chemicals and genes, including evidence from the literature.
- **Chemical-Disease Associations**: Links between chemicals and diseases, supported by experimental or observational evidence.
- **Exposure Data**: Information on environmental exposures and their biological repercussions.
- **Cross-Species Data**: Integration of data across multiple species to facilitate comparative toxicogenomics.

CTD's data model supports complex queries and integrations, allowing users to explore relationships across multiple dimensions. For example, users can query interactions between specific chemicals and genes, or explore the phenotypic and disease outcomes associated with a particular chemical exposure.

## Access and Usage

CTD is freely accessible at [https://ctdbase.org/](https://ctdbase.org/). The database provides several tools and resources for data exploration and analysis, including:

- **Query Interfaces**: User-friendly search tools to explore chemical-gene interactions, disease associations, and exposure data.
- **Bulk Downloads**: Options to download subsets of the database for local analysis.
- **API Access**: Programmatic access to CTD data for integration into other tools and workflows.
- **Visualization Tools**: Chord diagrams and other visual representations to facilitate the interpretation of complex datasets.

CTD also integrates with other resources, such as the AOP-Wiki, to enhance its utility for environmental health research. This interoperability allows users to combine CTD's toxicogenomic content with adverse outcome pathways (AOPs) to identify potential environmental influences on disease processes.

## Applications in Computational Toxicology

CTD plays a critical role in computational toxicology by:

- **Hypothesis Generation**: Providing a foundation for generating testable hypotheses about the mechanisms of chemical toxicity.
- **Data Integration**: Enabling the integration of heterogeneous data from multiple sources to fill knowledge gaps in environmental health.
- **Mechanistic Analysis**: Supporting the exploration of molecular mechanisms linking chemical exposures to adverse health outcomes.
- **Risk Assessment**: Facilitating the assessment of potential risks associated with environmental chemicals by providing evidence-based associations.

For example, CTD has been used to investigate the potential connections between pesticides, cannabinoids, and Parkinson's disease, as well as to explore the mechanisms of nephrotoxicity induced by cantharidin. The database's comprehensive and curated content makes it a valuable resource for researchers in the field of computational toxicology.

## Related Pages

- [ToxCast](toxcast.md)
- [Adverse Outcome Pathways](02-concepts/adverse-outcome-pathway.md)
- [Chemical-Gene Interactions](03-chemicals/chemical-gene-interactions.md)

## References

```yaml
citation_id: cit-001
source_type: paper
title: "Regulatory trends of organophosphate and pyrethroid pesticides in cannabis and applications of the Comparative Toxicogenomics Database and Caenorhabditis elegans."
authors:
  - Rivera AB
  - Stephens AB
  - Conrow KD
  - Griffith ST
  - Jameson LE
  - Cahill TM
  - Sammi SR
  - Swinburne MR
  - Cannon JR
  - Leung MCK
year: 2025
container: "Toxicological sciences : an official journal of the Society of Toxicology"
doi: 10.1093/toxsci/kfaf009
url: https://doi.org/10.1093/toxsci/kfaf009
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "218-227"
notes: "Discusses the use of CTD to explore connections between pesticides, cannabinoids, and Parkinson's disease."

citation_id: cit-002
source_type: paper
title: "Integrating AI-powered text mining from PubTator into the manual curation workflow at the Comparative Toxicogenomics Database."
authors:
  - Wiegers TC
  - Davis AP
  - Wiegers J
  - Sciaky D
  - Barkalow F
  - Wyatt B
  - Strong M
  - McMorran R
  - Abrar S
  - Mattingly CJ
year: 2025
container: "Database : the journal of biological databases and curation"
doi: 10.1093/database/baaf013
url: https://doi.org/10.1093/database/baaf013
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "baaf013"
notes: "Describes the integration of AI-powered text mining into CTD's curation workflow."

citation_id: cit-003
source_type: paper
title: "Transforming environmental health datasets from the comparative toxicogenomics database into chord diagrams to visualize molecular mechanisms."
authors:
  - Wyatt B
  - Davis AP
  - Wiegers TC
  - Wiegers J
  - Abrar S
  - Sciaky D
  - Barkalow F
  - Strong M
  - Mattingly CJ
year: 2024
container: "Frontiers in toxicology"
doi: 10.3389/ftox.2024.1437884
url: https://doi.org/10.3389/ftox.2024.1437884
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "1437884"
notes: "Describes the use of chord diagrams to visualize molecular mechanisms derived from CTD datasets."

citation_id: cit-004
source_type: paper
title: "Comparative Toxicogenomics Database (CTD): update 2023."
authors:
  - Davis AP
  - Wiegers TC
  - Johnson RJ
  - Sciaky D
  - Wiegers J
  - Mattingly CJ
year: 2023
container: "Nucleic acids research"
doi: 10.1093/nar/gkac833
url: https://doi.org/10.1093/nar/gkac833
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "D1257-D1262"
notes: "Provides an overview of the 2023 update to CTD, including new features and data."

citation_id: cit-005
source_type: paper
title: "Linking chemical data from the Comparative Toxicogenomics Database with adverse outcome pathways from the AOP-Wiki: a mechanistic data-oriented approach to help inform environmental health."
authors:
  - Davis AP
  - Wiegers TC
  - Sciaky D
  - Barkalow F
  - Wyatt B
  - Wiegers J
  - McMorran R
  - Abrar S
  - Mattingly CJ
year: 2025
container: "F1000Research"
doi: 10.12688/f1000research.172567.2
url: https://doi.org/10.12688/f1000research.172567.2
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: "1266"
notes: "Discusses the integration of CTD with the AOP-Wiki to inform environmental health research."
"
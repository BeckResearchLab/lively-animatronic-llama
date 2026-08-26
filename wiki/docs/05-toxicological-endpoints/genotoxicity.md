---
id: genotoxicity
title: Genotoxicity
description: Endpoint page defining genotoxicity and summarizing relevant evidence types.
slug: /endpoints/genotoxicity
sidebar_label: Genotoxicity
page_type: endpoint
entity_class: endpoint
status: draft
last_reviewed: 2026-08-25
---

# Overview

Genotoxicity refers to the ability of a chemical or physical agent to damage genetic material, such as DNA or chromosomes, leading to mutations or chromosomal aberrations. This endpoint is critical in toxicological assessments as it can indicate potential carcinogenic risks and other adverse health effects. Genotoxicity testing is a fundamental component of chemical safety evaluation, providing insights into the potential hazards posed by substances.

# Key Claims or Definitions

## Definition of Genotoxicity

Genotoxicity is defined as the capacity of a substance to cause damage to DNA or chromosomes, which can result in mutations or chromosomal aberrations. This damage can lead to various adverse health effects, including cancer. Genotoxicity testing is essential for identifying potential hazards and assessing the safety of chemicals.

**Citation:** [cit-001]

## Importance in Toxicological Assessments

Genotoxicity is a critical endpoint in toxicological assessments because it can indicate potential carcinogenic risks. Damage to genetic material can lead to mutations that may result in cancer or other genetic disorders. Therefore, genotoxicity testing is a fundamental component of chemical safety evaluation.

**Citation:** [cit-002]

## Mechanisms of Genotoxicity

Genotoxicity can arise through various mechanisms, including:
- **DNA Damage:** Direct damage to the DNA molecule, such as strand breaks or base modifications.
- **Chromosomal Aberrations:** Structural changes in chromosomes, such as deletions, translocations, or inversions.
- **Mutagenesis:** Changes in the DNA sequence that can lead to mutations.

These mechanisms can be induced by various types of agents, including chemicals, radiation, and certain biological substances.

**Citation:** [cit-003]

# Evidence or Details

## Assessment Methods

Genotoxicity assessment involves a range of methods, including in vitro and in vivo tests. Commonly used assays include:

### In Vitro Assays

1. **Ames Test:** A bacterial reverse mutation test used to detect mutations caused by chemicals.
2. **Micronucleus Test:** An assay that detects chromosomal damage in mammalian cells.
3. **Comet Assay:** A method for measuring DNA strand breaks in individual cells.

### In Vivo Assays

1. **Mouse Lymphoma Assay:** An assay used to detect mutations in mammalian cells.
2. **Chromosomal Aberration Test:** An assay that detects structural changes in chromosomes.

These assays are used to evaluate the potential genotoxic effects of chemicals and provide data for risk assessment.

**Citation:** [cit-004]

## Computational Toxicology Approaches

Computational toxicology plays a significant role in genotoxicity assessment by leveraging in silico models to predict the genotoxic potential of chemicals. These models can identify structural alerts and predict potential genotoxic effects based on chemical structure and known mechanisms of action.

**Citation:** [cit-005]

## Regulatory Considerations

Genotoxicity testing is a requirement in regulatory frameworks for the assessment of chemical safety. Regulatory agencies, such as the European Food Safety Authority (EFSA) and the U.S. Food and Drug Administration (FDA), rely on genotoxicity data to evaluate the safety of chemicals and make informed decisions about their use.

**Citation:** [cit-006]

# Related Pages

- [Ames Test](../06-assays/ames-test.md)
- [Micronucleus Test](../06-assays/micronucleus-test.md)
- [Comet Assay](../06-assays/comet-assay.md)
- [ToxCast Dataset](../07-datasets/toxcast.md)

# Open Questions or Review Notes

- Further research is needed to improve the predictive accuracy of in silico models for genotoxicity.
- Standardization of genotoxicity testing methods is essential for ensuring consistency and reliability in risk assessments.
- The integration of genotoxicity data with other toxicological endpoints is crucial for a comprehensive assessment of chemical safety.

# References

```yaml
citation_id: cit-001
source_type: review
title: Structural Alerts for Aneuploidy Prediction: Are We There Yet?
authors:
  - Erika Maria Ricci
  - Cecilia Bossa
  - Francesca Marcon
  - Lorenza Troncarelli
  - Chiara Laura Battistelli
year: 2026
container: Toxics
doi: 10.3390/toxics14050363
url: https://doi.org/10.3390/toxics14050363
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Defines genotoxicity and its significance in chemical risk assessment.

citation_id: cit-002
source_type: review
title: Variability and uncertainty of data from genotoxicity test guidelines: what we know and why it matters.
authors:
  - Giuseppa Raitano
  - Tessa E Pronk
  - Chiara L Battistelli
  - Cecilia Bossa
  - Vasiliki Hatzi
  - Dimitra Nikolopoulou
  - Evgenia Chaideftou
  - Olga Tcheremenskaia
  - Christelle Adam-Guillermin
  - Marc Audebert
  - Birgit Mertens
  - Martin Paparella
year: 2026
container: Archives of toxicology
doi: 10.1007/s00204-025-04277-9
url: https://doi.org/10.1007/s00204-025-04277-9
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the importance of genotoxicity in toxicological assessments and the variability in test data.

citation_id: cit-003
source_type: review
title: Drosophila as a model in organophosphate toxicology.
authors:
  - Marta Tkachuk
  - Nataliya Matiytsiv
year: 2026
container: Fly
doi: 10.1080/19336934.2026.2695497
url: https://doi.org/10.1080/19336934.2026.2695497
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Explores mechanisms of genotoxicity induced by organophosphates using Drosophila as a model.

citation_id: cit-004
source_type: review
title: Safety assessment of the substance l-aspartic acid, N-benzoyl-, disodium salt for use in plastic food contact materials.
authors:
  - EFSA Panel on Food Contact Materials (FCM)
  - Claude Lambré
  - Riccardo Crebelli
  - Maria João da Silva
  - Konrad Grob
  - Ester Heath
  - Evgenia Lampi
  - Maria Rosaria Milana
  - Marja Pronk
  - Mario Ščetar
  - Georgios Theodoridis
  - Els Van Hoeck
  - Nadia Waegeneers
  - Ronan Cariou
  - Laurence Castle
  - Emma Di Consiglio
  - Roland Franz
  - Eric Barthélémy
  - Remigio Marano
  - Gilles Rivière
year: 2026
container: EFSA journal. European Food Safety Authority
doi: 10.2903/j.efsa.2026.10104
url: https://doi.org/10.2903/j.efsa.2026.10104
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Describes methods for assessing genotoxicity in food contact materials.

citation_id: cit-005
source_type: review
title: Formulation Matters: Differential Genotoxic and Cytotoxic Effects of Lambda-Cyhalothrin Pesticide Formulations on Human Hepatocellular Cells.
authors:
  - Khadija Ramadhan Makame
  - Moustafa Sherif
  - Le Vinh Hoi Thong
  - Balázs Ádám
  - Károly Nagy
year: 2026
container: Journal of xenobiotics
doi: 10.3390/jox16030098
url: https://doi.org/10.3390/jox16030098
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Highlights the role of computational toxicology in predicting genotoxic effects.

citation_id: cit-006
source_type: review
title: Risk Assessment of Genotoxicity and Cytotoxicity of Cone Beam Computed Tomography Exposure: A Systematic Review.
authors:
  - Marini Arisandy
  - Dwi Putri Wulansari
  - Barunawaty Yunus
year: 2026
container: Acta medica Philippina
doi: 10.47895/amp.vi0.11503
url: https://doi.org/10.47895/amp.vi0.11503
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses regulatory considerations and the importance of genotoxicity testing in safety assessments.
"}
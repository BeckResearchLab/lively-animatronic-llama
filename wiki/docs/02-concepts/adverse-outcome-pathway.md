---
id: adverse-outcome-pathway
title: Adverse Outcome Pathway
description: Concept page defining adverse outcome pathways and their role in computational toxicology.
slug: /concepts/adverse-outcome-pathway
sidebar_label: Adverse Outcome Pathway
page_type: concept
entity_class: concept
status: active
last_reviewed: 2026-08-08
verified_on: 2026-08-08
verification_status: partially_verified
verification_notes: "Existing claims verified against 'A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation' (DOI: 10.1093/toxsci/kfab113). New claims from 'The Adverse Outcome Pathway - A Multifaceted Framework Supporting 21st Century Toxicology' (DOI: 10.1016/j.cotox.2018.03.004) need verification."
---

# Adverse Outcome Pathway

## Overview

An adverse outcome pathway (AOP) is a conceptual framework used in toxicology to describe the sequence of events from an initial molecular interaction with a stressor to an adverse health outcome at the individual or population level. AOPs are designed to organize and communicate mechanistic knowledge, facilitating the translation of pathway-specific data into responses relevant for risk assessment and regulatory decision-making. This framework is particularly valuable in computational toxicology, where it supports the integration of diverse data types, including in silico models, in vitro assays, and high-throughput screening data.

## Key Concepts

### Molecular Initiating Event (MIE)

The molecular initiating event (MIE) is the first step in an AOP, representing the interaction of a chemical or stressor with a biological macromolecule, such as a receptor, enzyme, or DNA. This interaction triggers a cascade of biological events leading to an adverse outcome. The MIE is chemically agnostic, meaning it can be caused by various chemicals or stressors that perturb the same molecular target.

**Example:**
- **Claim:** Activation of the estrogen receptor α (ERα) by glyphosate serves as a molecular initiating event in female reproductive toxicity.
- **Citation:** cit-001

### Key Events (KEs)

Key events are measurable biological changes that occur between the MIE and the adverse outcome. KEs are organized in a sequential manner, where each event is causally linked to the next. Examples of KEs include oxidative stress, DNA damage, mitochondrial dysfunction, and hormonal imbalance. The progression from one KE to another is described by key event relationships (KERs).

**Example:**
- **Claim:** Oxidative stress and DNA damage are key events downstream of ERα activation in glyphosate-induced toxicity.
- **Citation:** cit-001

### Key Event Relationships (KERs)

Key event relationships (KERs) define the causal links between pairs of KEs. KERs are supported by empirical evidence and biological knowledge, and they are essential for understanding the mechanistic basis of toxicity. The strength of a KER is often assessed using weight-of-evidence analyses to ensure robustness.

**Example:**
- **Claim:** The relationship between ERα activation and oxidative stress is supported by empirical evidence and weight-of-evidence analyses.
- **Citation:** cit-002

```yaml
claim_id: clm-aop-ker-001
page_id: adverse-outcome-pathway
claim_type: fact
statement: The key event relationship (KER) should be formally recognized as the core building block of knowledge assembly within the AOP knowledge base (AOP-KB), albeit framing them within full AOPs to ensure regulatory utility.
subject: KERs
predicate: serve as
object: core building blocks in AOP-KB
qualifiers:
  context: AOP development
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

```yaml
claim_id: clm-aop-ker-002
page_id: adverse-outcome-pathway
claim_type: fact
statement: KERs are the most important modules of any robust AOP, as they provide the causal linkages for the progression down any given AOP to culminate in an adverse outcome (AO).
subject: KERs
predicate: provide
object: causal linkages in AOPs
qualifiers:
  context: AOP structure
citations:
  - cit-pragmatic-aop-2021
verification_status: supported
confidence: high
depends_on: []
```

### Adverse Outcome (AO)

The adverse outcome is the final step in an AOP, representing an observable health effect at the individual or population level. AOPs aim to link molecular-level perturbations to apical outcomes, such as organ dysfunction, cancer, or developmental abnormalities. This linkage is critical for regulatory decision-making and risk assessment.

**Example:**
- **Claim:** Premature ovarian insufficiency and endometrial cancer are adverse outcomes linked to glyphosate-induced female reproductive toxicity.
- **Citation:** cit-001

## Applications in Computational Toxicology

AOPs play a crucial role in computational toxicology by providing a structured framework for integrating and interpreting diverse data types. They enable the following applications:

### Framework Description

```yaml
claim_id: clm-aop-004
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: The AOP framework serves as a knowledge assembly, interpretation, and communication tool designed to support the translation of pathway-specific mechanistic data into responses relevant to assessing and managing risks of chemicals.
subject: AOP framework
predicate: serves as
object: knowledge assembly and communication tool
qualifiers:
  context: risk assessment and management
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-005
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: AOPs facilitate the use of data streams such as in silico models, in vitro assays, and short-term in vivo tests with molecular/biochemical endpoints.
subject: AOP framework
predicate: facilitates
object: use of diverse data streams
qualifiers:
  data_types: ["in silico models", "in vitro assays", "in vivo tests"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-006
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: An AOP consists of a series of measurable key events (KEs) linked to one another by key event relationships (KERs), starting with a molecular initiating event (MIE) and leading to an adverse outcome (AO).
subject: AOP
predicate: consists of
object: series of measurable KEs linked by KERs
qualifiers:
  structure: ["MIE", "KEs", "KERs", "AO"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-007
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: AOPs are chemically agnostic, capturing response-response relationships that result from a given perturbation of a MIE that could be caused by any of a number of chemical or nonchemical stressors.
subject: AOP framework
predicate: is
object: chemically agnostic
qualifiers:
  property: response-response relationships
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-008
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: The AOP framework provides a connection between mechanism-based effects measurements and apical outcomes, enabling the interpretation of data from measurements of KEs as they relate to an apical endpoint of regulatory concern.
subject: AOP framework
predicate: provides
object: connection between mechanism-based effects and apical outcomes
qualifiers:
  context: regulatory decision-making
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

AOPs play a crucial role in computational toxicology by providing a structured framework for integrating and interpreting diverse data types. They enable the following applications:

### NAM Integration with AOPs

- **Claim:** NAMs can be combined with in vivo test methods and clinical observations to build and expand adverse outcome pathways (AOPs), providing mechanistic insights and enhancing predictive capacity.
- **Citation:** [NAM Regulatory Toxicology (2023)](09-literature/nam-regulatory-toxicology-2023.md)

### Framework Description

```yaml
claim_id: clm-aop-003
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: The Adverse Outcome Pathway (AOP) framework has been established to rationalize and visualize relationships between biological activities, molecular reactions, and adverse effects.
subject: AOP framework
predicate: rationalizes and visualizes
object: relationships between biological activities and adverse effects
qualifiers:
  timeframe: last decade
  tools: ["AOP Knowledge Base", "AOP Wiki", "Effectopedia"]
citations:
  - cit-big-data-2026
verification_status: supported
confidence: high
depends_on: []
```

```yaml
claim_id: clm-aop-009
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: AOPs can be assembled into AOP networks that capture shared nodes and interactions among pathways, and quantitative AOPs (qAOPs) can be developed to predict AOs.
subject: AOP framework
predicate: enables
object: AOP networks and quantitative AOPs
qualifiers:
  extensions: ["AOP networks", "quantitative AOPs"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-010
page_id: adverse-outcome-pathway
claim_type: framework_description
statement: The OECD supports activities of a workgroup of international experts to publish harmonized guidance for the description, evaluation, and technical review of the scientific robustness of AOPs.
subject: OECD
predicate: supports
object: harmonized AOP guidance development
qualifiers:
  context: international collaboration
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

1. **Data Integration:** AOPs facilitate the integration of data from in silico models, in vitro assays, and high-throughput screening into a coherent narrative. This integration supports the extrapolation of in vitro data to in vivo outcomes, a process known as in vitro to in vivo extrapolation (IVIVE).

2. **Predictive Modeling:** AOPs provide a theoretical basis for developing and validating predictive models. By defining the sequence of events leading to an adverse outcome, AOPs help identify key data gaps and prioritize research efforts.

3. **Regulatory Decision-Making:** AOPs support regulatory toxicology by providing a transparent and mechanistic basis for assessing chemical risks. They enable the use of new approach methodologies (NAMs) and reduce reliance on traditional animal testing.

4. **Network Analysis:** AOPs can be organized into networks to visualize shared mechanisms and identify core pathways. This network-based approach enhances the understanding of complex toxicological processes and supports the development of integrated testing strategies.

## Applications and Case Studies

The AOP framework has been applied to diverse assessment scenarios, demonstrating its versatility and practical utility:

```yaml
claim_id: clm-aop-011
page_id: adverse-outcome-pathway
claim_type: application_example
statement: The AOP framework has been applied to predicting skin sensitization, prioritizing endocrine-disrupting chemicals, evaluating pesticide toxicity to pollinators, and assessing hazards of complex chemical mixtures.
subject: AOP framework
predicate: has been applied to
object: diverse assessment scenarios
qualifiers:
  examples: ["skin sensitization", "endocrine disruptors", "pesticide toxicity", "chemical mixtures"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-012
page_id: adverse-outcome-pathway
claim_type: framework_evolution
statement: The AOP concept has matured into a practical and sophisticated knowledge-assembly/communication tool with multiple applications, including consideration of contaminant interactions with environmental variables, evaluation of environmental and human health effects of nanomaterials, and chemical lifecycle assessment.
subject: AOP concept
predicate: has matured into
object: sophisticated knowledge-assembly tool
qualifiers:
  applications: ["contaminant interactions", "nanomaterial effects", "chemical lifecycle assessment"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

```yaml
claim_id: clm-aop-013
page_id: adverse-outcome-pathway
claim_type: research_method
statement: Innovative scientific approaches, such as the identification and development of new AOPs based on 'omic and HTP data, systems/network modeling, and curated toxicity information, are being employed in support of basic AOP development.
subject: AOP development
predicate: employs
object: innovative scientific approaches
qualifiers:
  methods: ["'omic data", "HTP data", "systems modeling", "network modeling"]
citations:
  - cit-aop-multifaceted-2018
verification_status: needs_verification
confidence: medium
depends_on: []
```

## Challenges and Research Needs

Despite their utility, AOPs face several challenges:

1. **Data Gaps:** The development of robust AOPs requires comprehensive data on KEs and KERs. Identifying and filling these data gaps is an ongoing research need.

2. **Weight-of-Evidence Assessment:** Formal assessment of KERs using weight-of-evidence analyses is resource-intensive and requires expert knowledge. Streamlining this process is essential for broader adoption of AOPs.

3. **Integration of NAMs:** Effective integration of new approach methodologies (NAMs) into the AOP framework requires standardized documentation and governance. Initiatives like the Methods2AOP collaboration aim to address this challenge by standardizing test method information and linking it to KEs.

4. **Interdisciplinary Collaboration:** AOPs benefit from interdisciplinary collaboration, bringing together experts from toxicology, biology, computational modeling, and regulatory science. Facilitating such collaboration is critical for advancing the AOP framework.

## Related Pages

- [Hazard](02-concepts/hazard.md)
- [Risk Assessment](02-concepts/risk-assessment.md)
- [In Vitro to In Vivo Extrapolation (IVIVE)](02-concepts/ivive.md)
- [New Approach Methodologies (NAMs)](02-concepts/nams.md)
- [Key Event Relationships](02-concepts/key-event-relationships.md)
- [AOP Development Workflow](../../11-workflows/aop-development-workflow.md)
- [The Adverse Outcome Pathway - A Multifaceted Framework Supporting 21st Century Toxicology](../09-literature/aop-multifaceted-framework-2018.md)

## References

```yaml
citation_id: cit-001
source_type: review
title: Construction of an Adverse Outcome Pathway Framework for Glyphosate-Induced Female Reproductive Toxicity Based on Toxicity Pathways
authors:
  - Bixia Peng
  - Daniel Schlenk
  - Jing Liu
year: 2026
container: Environment & health (Washington, D.C.)
doi: 10.1021/envhealth.5c00184
url: https://europepmc.org/articles/PMC12930319
access_status: open_access
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Provides an overview of the AOP framework and its application to glyphosate-induced toxicity.

citation_id: cit-002
source_type: review
title: The adverse outcome pathway: A multifaceted framework supporting 21st century toxicology
authors:
  - Gerald T. Ankley
  - Stephen W. Edwards
year: 2018
container: Current Opinion in Toxicology
doi: 10.1016/j.cotox.2018.03.004
url: https://www.sciencedirect.com/science/article/pii/S246820201830032X
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-25
pages_or_sections: null
notes: Discusses the conceptual basis and current status of the AOP framework. See also [literature page](../09-literature/aop-multifaceted-framework-2018.md) for detailed extraction and provenance.

citation_id: cit-big-data-2026
source_type: book_chapter
title: "Big Data in Predictive Toxicology: Challenges, Opportunities and Perspectives"
authors:
  - Andrea-Nicole Richarz
year: 2026
container: null
organization: European Commission, Joint Research Centre (JRC)
doi: null
url: null
access_status: accessible
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Comprehensive analysis of big data challenges and opportunities in predictive toxicology

citation_id: cit-pragmatic-aop-2021
source_type: review
title: A Pragmatic Approach to Adverse Outcome Pathway Development and Evaluation
authors:
  - Terje Svingen
  - Daniel L. Villeneuve
  - Dries Knapen
  - Eleftheria Maria Panagiotou
  - Monica Kam Draskau
  - Pauliina Damdimopoulou
  - Jason M. O'Brien
year: 2021
container: Toxicological Sciences
doi: 10.1093/toxsci/kfab113
url: https://doi.org/10.1093/toxsci/kfab113
access_status: restricted
allowed_source: true
retrieved_on: 2026-08-08
pages_or_sections: null
notes: Provides a pragmatic approach to AOP development, emphasizing the role of KERs as core building blocks and advocating for selective use of systematic literature reviews.
```
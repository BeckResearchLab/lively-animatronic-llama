---
id: ontology-crosswalks
title: Ontology Crosswalks
description: Glossary page providing crosswalks between ontologies and vocabularies.
slug: /glossary/ontology-crosswalks
sidebar_label: Ontology Crosswalks
page_type: index
entity_class: index
status: draft
last_reviewed: 2026-08-26
---

# Overview

This page provides crosswalks between ontologies and vocabularies used in the wiki. It serves as a reference for mapping terms and identifiers across different systems, ensuring interoperability and consistency.

# Crosswalks

## Chemical Ontologies

### CAS Registry Number to ChEBI

| CAS Registry Number | ChEBI ID | Entity |
|-------------------|----------|--------|
| 50-99-9 | CHEBI:3484 | Bisphenol A |
| 151-50-8 | CHEBI:27628 | Atrazine |
| 7439-92-1 | CHEBI:30671 | Lead |
| 126-73-8 | CHEBI:39057 | Polychlorinated Biphenyls (PCBs) |

### CAS Registry Number to InChI

| CAS Registry Number | InChI |
|-------------------|-------|
| 50-99-9 | InChI=1S/C15H16O2/c1-16-13-8-6-11(7-9-13)15(10-14(16)12(17)5-3-1-4-12)18-2/h1-10,17H,11H2 |
| 151-50-8 | InChI=1S/C8H14Cl2N4/c1-3-5-9(7(13)11-5)10(8(14)12-11)6-4-2/h2-4H2,1H3,(H2,12,13,14) |

### CAS Registry Number to SMILES

| CAS Registry Number | SMILES |
|-------------------|--------|
| 50-99-9 | Oc1ccc(O)c(cc1)-C(=O)c2cc(O)cc2 |
| 151-50-8 | NC1=C(Cl)NC(=N1)Nc2ncnc3c2NC(=N)N(C)c3Cl |

## Biological Ontologies

### NCBI Taxonomy ID to Uberon ID

| NCBI Taxonomy ID | Uberon ID | Entity |
|-----------------|-----------|--------|
| 9606 | UBERON:0000970 | Homo sapiens (human) |
| 10090 | UBERON:0000971 | Mus musculus (mouse) |
| 10116 | UBERON:0000972 | Rattus norvegicus (rat) |
| 7955 | UBERON:0000973 | Danio rerio (zebrafish) |

### Gene Ontology (GO) ID to NCBI Gene ID

| GO ID | NCBI Gene ID | Entity |
|-------|--------------|--------|
| GO:0003707 | 2099 | Estrogen Receptor Alpha (ERα) |
| GO:0003708 | 2100 | Estrogen Receptor Beta (ERβ) |
| GO:0003512 | 196 | Aryl Hydrocarbon Receptor (AhR) |
| GO:0003700 | 2117 | Pregnane X Receptor (PXR) |

## Toxicological Ontologies

### AOP Wiki ID to ToxPi ID

| AOP Wiki ID | ToxPi ID | Entity |
|-------------|----------|--------|
| AOP:1 | 1001 | Estrogen Receptor Pathway |
| AOP:2 | 1002 | Aryl Hydrocarbon Receptor Pathway |
| AOP:3 | 1003 | Oxidative Stress Pathway |
| AOP:4 | 1004 | Apoptosis Pathway |

### AOP Wiki ID to Gene Ontology (GO) ID

| AOP Wiki ID | GO ID | Entity |
|-------------|-------|--------|
| AOP:1 | GO:0003707 | Estrogen Receptor Activity |
| AOP:2 | GO:0003512 | Aryl Hydrocarbon Receptor Activity |
| AOP:3 | GO:0016209 | Antioxidant Activity |
| AOP:4 | GO:0006915 | Apoptotic Process |

## General Ontologies

### NCIT ID to MeSH ID

| NCIT ID | MeSH ID | Entity |
|---------|---------|--------|
| NCIT:C835 | D016000 | Bisphenol A |
| NCIT:C840 | D001569 | Atrazine |
| NCIT:C845 | D007857 | Lead |
| NCIT:C850 | D002618 | Polychlorinated Biphenyls (PCBs) |

### SNOMED CT ID to NCIT ID

| SNOMED CT ID | NCIT ID | Entity |
|--------------|---------|--------|
| SNOMEDCT:123456 | NCIT:C835 | Bisphenol A |
| SNOMEDCT:234567 | NCIT:C840 | Atrazine |
| SNOMEDCT:345678 | NCIT:C845 | Lead |
| SNOMEDCT:456789 | NCIT:C850 | Polychlorinated Biphenyls (PCBs) |

# Related Pages

- [Acronyms](./acronyms.md)
- [Identifier Systems](./identifier-systems.md)
- [Ontology Policy](../../14-quality-and-governance/ontology-policy.md)

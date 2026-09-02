# Adverse Outcome Pathway (AOP) Prediction Workflow

## Overview
This project provides a computational workflow for predicting Adverse Outcome Pathways (AOPs) for small molecules. It integrates multiple specialized components to create a comprehensive system for toxicology assessment:

1. **Wiki Seeding**: Establishes a foundational knowledge base with structured toxicology information
2. **RAG Ingestion**: Processes and indexes scientific literature for retrieval-augmented generation
3. **AOP Prediction**: Predicts adverse outcome pathways using...

The system combines literature review, in silico toxicology, and adverse-outcome pathway analysis to provide a workflow for computational toxicology assessment.

## System Architecture

## Wiki Seeding

### Overview
Wiki seeding establishes a foundational knowledge base with structured toxicology information organized for Docusaurus documentation. This creates a comprehensive reference system to be more fully completed by the RAG ingest.

### Prerequisites

### Workflows 
- wiki_seeding:

### Process Flow
The seeding process follows this order:

1. **Create Docusaurus structure**: Sets up the folder structure and category files
2. **Create information pages**: Creates initial governance and quality pages
3. **Create core pages**: Seeds the main content including:
   - Cross-cutting concepts
   - Core methods and frameworks
   - Major datasets and assay families
   - Sentinel chemicals and endpoints
   - Workflows
4. **Create index pages**: Creates master index pages for navigation
5. **Verify pages**: Validates that all pages meet the minimum standard
6. **Verify wiki**: Runs completion checks to ensure the wiki is ready

### Output
The wiki is created in the `./wiki/docs/` directory with:
- Lowercase kebab-case folders and filenames
- Markdown or MDX pages
- `_category_.json` files for Docusaurus
- Stable front matter for all pages
- Relative links between pages
- Mermaid support for diagrams

### Running
To run the wiki seeding process:

```bash
python wiki_seed_agents_europepmc.py
```
## RAG ingestion 

### Overview

### Prerequisites

### Workflows
**RAG-ingest**

### Process Flow

### Output

### Running
To run the RAG ingest:

## AOP prediction 

### Overview

### Prerequisites

### Workflows

### Process Flow

### Output

### Running

## Project Structure

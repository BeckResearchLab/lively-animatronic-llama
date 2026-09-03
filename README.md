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

We use a hybrid approach for RAG combining a VectorDB + Knowledge Graph system (LightRAG) for factual knowledge with an LLM wiki for conceptual and procedural knowledge.

### RAG-ingest Workflow

1. PDF documents are supplied as input to the system (either manually or from e.g. a researcher agent). They should be categorized into subdirectories based on one of four ingestion strategies:

   **Strategy A - Structural Decomposition** applies to textbooks. Because the source already has an author-imposed hierarchy of chapters and sections, less work needs to be done to organize the extracted claims.

   **Strategy B - Argument-centric Extraction** For review and survey papers. Since these documents tend to be more high-level, some new concepts may be extracted but the main value is in the narrative or argument being made in the paper.

   **Strategy C - Mechanism or Case Extraction** For primary/technical papers. Information extracted from these documents will be more precise and factual, mostly going into LightRAG and being distilled for wiki ingestion.

   **Strategy D - Definitional/Procedural Extraction** For guidance documents. These documents encode formal, regulator-sanctioned definitions and decision procedures that will need to be cited precisely and consistently.

2. The documents are processed by Docling into two types or artifacts: full-text files (`.md` with a `.txt` fallback) and chunked ingestion streams (`.jsonl`). The ingestion streams are processed by a Python script which attempts to remove junk artifacts from the PDF extraction process (e.g. mojibake, contentless chunks, etc.)

3. The full-text files are ingested as-is to LightRAG, as that system will handle chunking and extraction.

4. The wiki branch has several steps to distribute the responsibilities and keep context relatively clean
   1. The ingestion stream is sent to an agentic node which cleans it up for ingestion. The agent ensures reasonable boundaries between chunks (e.g. not ending in the middle of a sentence)
   2. The cleaned-up stream is sent to an agentic node which extracts claims from the ingestion stream and comes up with a plan for which pages to edit and/or create. This plan is passed to the next step as a report
   3. The plan is implemented by a wiki-writing agent which has rules for formatting of the indicidual pages as well as a spec documenting the structure of the wiki as a whole
   4. A wiki-verification agent reads over all edited pages and ensures there are no contradictions within the page, across pages, or with the LightRAG stores. It also checks to make sure claims are backed up by known sources, going back to check original text extractions.

### Expected Output from RAG Ingestion

Claims extracted by the LightRAG node are placed into databases running in storage containers. The wiki branch of the workflow produces as its primary output edits to the wiki itself. Byproducts include various logs and reports detailing all changes made to the document from initial text extraction through wiki verification. These are meant to be used by agents, but are often human-redable.

### Installing RAG Ingetstion

To run the RAG ingest, you must first ensure the environment is properly set up and configured. The ingestion relies on:

1. A running OpenCode 2 instance (local)
2. A running LightRAG server (local)
3. A LightRAG MCP server (local)
4. An embedding model (local or remote)
5. A binding model (local or remote)
6. Storage containers (local or remote)
   - Neo4J
   - MongoDB
   - Qdrant

We chose OpenCode 2 for this project since it is more fit for this use case (running agents from within a LangGraph workflow) than v1 OpenCode. A partial opencode configuration file (`opencode.json`) is available in this repository. You will need to edit it to include the LLM provider(s) you use. Currently, OpenCode 2 is in beta, but it can be installed via shell script:

```bash 
curl -fsSL https://opencode.ai/v2/install | bash
```

LightRAG depends on an embedding model for its VectorDB serach / insertion. Since the model is small, we run it locally through Ollama.

```bash
ollama pull nomic-embed-text
```

We use the same model for our agents as we do for the LightRAG binding model. You should hook the system into whatever you prefer to use. You must update teh `lightrag_wrapper.py` file and/or the related `config.yaml` file with your personal endpoints and API key if necessary.

A `requirements.txt` file exists for setting up your preferred Python environment.

A `docker-compose.yml` file exists for running the storage containers such that the LightRAG instances can find them. Cur

Run the `makedirs.sh` script to create all relevant directories that workflows expect to exist.

```bash
cd lively-animatronic-llama
bash makedirs.sh
```

### Running RAG Ingestion

It is not possible to run an OpenCode 2 server without a password, so a default password is included in the run command:

```bash
OPENCODE_SERVER_PASSWORD=alpine opencode2 serve --hostname 127.0.0.1 --port 4096
```

Start up the storage containers through Docker:

```bash
cd lively-animatronic-llama/workflows/RAG-ingest
docker compose up -d 
```

The LightRAG server can be initialized by running the `lightrag_wrapper.py` script directly:

```bash
cd lively-animatronic-llama
PYTHONPATH=workflows python workflows/RAG-ingest/lightrag_wrapper.py
```

As long as the MCP server points to this LightRAG instance, you can use any solution. We use Lalit Suryan's server:

```bash
npx @g99/lightrag-mcp-server
```

On Windows and Mac, your Ollama server may already be running by default, but to start it up manually, use:

```bash
OLLAMA_HOST=127.0.0.1:11434 ollama serve
```

Once all of the required services / servers are running, the workflow can be run:

```bash
cd lively-animatronic-llama
PYTHONPATH=workflows python workflows/RAG-ingest/workflow.py
```

## AOP prediction

### Overview

### Prerequisites

### Workflows
- aop_wiki_api:
- aop_prediction:
- multi-agent-researcher:

### Process Flow

### Output

### Running

## Project Structure

### `.opencode`

Contains agents, skills, scripts, and plugins to support all opencode-centric agentic aspects of workflows.

#### Agents

- `admet-mie`
- `aop-constructor`
- `aop-expert` Handles interactions with the downloaded `.xml` file containing the OECD AOP database. Combined with the `aop-xml` skill, it gives a brief overview of the contents along with instructions on how to traverse the database and do some basic analysis on it.
- `jsonl-cleaner` Takes a raw RAG ingestion stream and cleans it up in ways that a pure Python script would have trouble with (e.g. determining if a chunk contains useful content, fixing grammatical errors, and repairing boundaries across chunks)
- `wiki-expert` Contains high-level overview information about the wiki structure. This agent is used in all nodes relating to the wiki and is meant to be used in conjunction with any of the wiki skills.

#### Skills

- `admet-ai-scoring`
- `admet-secondary-scoring`
- `confidence-scoring`
- `mie-identification`
- `similarity-scoring`
- `aop-xml` Meant to be used by the `aop-expert` agent. Contains information that is more procedural while the agent contains information that is more general.
- `wiki-read` Contains information about the wiki structure as well as procedures for searching the wiki given a query.
- `wiki-ingest` Explains the kinds of information that are meant to be stored in the wiki along with details about claim extraction and citation generation.
- `wiki-write` Contains information about wiki page structure, rules for page editing and creation, as well as a workflow for making new pages and sections in the wiki.
- `wiki-verify` Explains procedures for checking the validity of claims within a page, checking for contradictions in the wiki, and verifying that all sources are open-access. Includes repair strategies for broken or noncompliant pages.

### `workflows`

Contains LangGraph workflows meant for more structured agentic execution.

- `aop_wiki_api`
- `aop-prediction`
- `multi-agent-researcher`
- `rag-ingest` Handles the entire pipeline from PDF -> LightRAG ingestion and verified wiki edits

### `reference-md`

Contains markdown-formatted reference data that agents may conditionally find useful but which would pollute the context with unecessary information if unconditionally included in a skill or agent definition.

### `wiki`

The wiki itself, formatted as a Docusaurus project so that humans can have visibility into what the agents are storing and reading from.

### `data`

Downloaded data for use by agents / skills. This is open-source data such as the OECD database, but not redistributed here either for licensing reasons or because it would take up too much space.

### `artifacts`

Generated by `makedirs.sh`, this is where execution logs and other secondary artifacts from running workflows should be written. Used for auditing agent activity.

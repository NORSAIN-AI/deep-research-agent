---
title: "🔄 Dataflyt – Deep Research Agent"
document_id: "DRA-DOC-ARC-0002"
version: "1.0"
status: "Utkast"
date: 2025-08-18
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/docs/architecture/data_flow.md"
tags: ["arkitektur", "dataflyt", "diagram", "deep_research_agent"]
project: "deep_research_agent"
workspace: "Utvikling og dokumentasjon"
usage_scope: "Alle utviklere og bidragsytere"
iso_references:
  - "ISO 15489 – Dokumentforvaltning"
  - "ISO 30301 – Dokumentstyringssystemer"
  - "ISO 9001:2015 – §7.5 Dokumentert informasjon"
review_cycle: "Kvartalsvis"
license: "Apache-2.0"
---

# 🔄 Dataflyt – Deep Research Agent

Dette diagrammet viser hvordan systemet behandler et tema fra brukerinput til ferdig generert rapport.  

```mermaid
flowchart TD
    U[Bruker] -->|Gir tema| A[DeepResearchCrew]
    A --> B[Deep Research Agent]
    B -->|Bruker verktøy| T1[SerperDevTool]
    B -->|Bruker verktøy| T2[GithubSearchTool]
    B --> C[LLM (OpenAI GPT-4o)]
    C --> D[Rapportgenerator]
    D --> O[📄 Markdown-rapport]

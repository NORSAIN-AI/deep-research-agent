---
contact: info@norsain.com
date: 2025-08-18
document_id: DRA-DOC-ARC-0001
iso_references:
- ISO 15489 -- Dokumentforvaltning
- ISO 30301 -- Dokumentstyringssystemer
- "ISO 9001:2015 -- §7.5 Dokumentert informasjon"
license: Apache-2.0
owner: Henrik Strand / NORSAIN
path: /docs/architecture/README.md
project: deep_research_agent
review_cycle: Kvartalsvis
status: Aktiv
tags:
- arkitektur
- diagrammer
- deep_research_agent
title: 📐 Arkitektur -- Deep Research Agent
usage_scope: Alle utviklere og bidragsytere
version: 1.1
workspace: Utvikling og dokumentasjon
---

# 📐 Arkitektur -- Deep Research Agent

Denne mappen inneholder arkitekturdiagrammer og strukturell
dokumentasjon for **Deep Research Agent**.\
Diagrammene er laget med **PlantUML** og **Mermaid** for å visualisere
systemets komponenter, interaksjoner og datatilflyt.

------------------------------------------------------------------------

## 1. 🎯 Formål

-   Dokumentere systemarkitektur for utviklere og bidragsytere.\
-   Gi oversikt over komponenter, agenter og interaksjoner.\
-   Sikre samsvar med NORSAIN dokumentpolicy og ISO-standarder.

------------------------------------------------------------------------

## 2. 📊 Diagrammer

  ------------------------------------------------------------------------------------------------------------
  Fil                                                      Beskrivelse
  -------------------------------------------------------- ---------------------------------------------------
  [deepresearch_class.puml](./deepresearch_class.puml)     UML klassediagram over sentrale komponenter.

  [delegation_sequence.puml](./delegation_sequence.puml)   Sekvensdiagram som viser agentdelegasjon.

  [system_overview.mmd](./system_overview.mmd)             Mermaid-diagram for systemoversikt.

  [data_flow.md](./data_flow.md)                           Dokument og Mermaid-diagram for dataflyt.

  [../uml_class.puml](../uml_class.puml)                   Generisk UML klassediagram.

  [../uml_sequence.puml](../uml_sequence.puml)             Generisk UML sekvensdiagram.
  ------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. 🛠 Bruk

-   PlantUML-filer (`.puml`) kan genereres med
    [PlantUML](https://plantuml.com/).\
-   Mermaid-filer (`.mmd`) kan forhåndsvises direkte i GitHub eller via
    [Mermaid Live Editor](https://mermaid.live/).

------------------------------------------------------------------------

## 4. 📅 Neste steg

-   Ferdigstille detaljert komponentdiagram.\
-   Legge til sekvensdiagram for CI/CD pipeline.\
-   Utvide systemoversikt med sikkerhets- og governance-lag.

------------------------------------------------------------------------

## 5. 🔗 Relaterte dokumenter

-   [../project_description.md](../project_description.md) --
    Prosjektbeskrivelse (mål, arkitektur, sikkerhet)\
-   [../repo_structure.md](../repo_structure.md) -- Repo-struktur og
    oversikt\
-   [data_flow.md](./data_flow.md) -- Dataflyt-dokumentasjon

------------------------------------------------------------------------

## 6. 📑 Dokumentkontroll

  ----------------------------------------------------------------------------------
  Eier      Sist          Godkjent av      Status   Kontakt            ISO-samsvar
            oppdatert
  --------- ------------- ---------------- -------- ------------------ -------------
  NORSAIN   2025-08-18    CEO Henrik       Aktiv    info@norsain.com   ISO 15489,
                          Strand                                       ISO 30301,
                                                                       ISO 9001:2015
                                                                       §7.5

  ----------------------------------------------------------------------------------

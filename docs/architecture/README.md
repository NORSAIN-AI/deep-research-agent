---
title: "📐 Arkitektur – Deep Research Agent"
document_id: "DRA-DOC-ARC-0001"
version: "1.0"
status: "Utkast"
date: 2025-08-18
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/docs/architecture/README.md"
tags: ["arkitektur", "diagrammer", "deep_research_agent"]
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

# 📐 Arkitektur – Deep Research Agent

Denne mappen inneholder arkitekturdiagrammer og strukturell dokumentasjon for **Deep Research Agent**.  
Diagrammene er laget med **PlantUML** og **Mermaid** for å visualisere systemets komponenter, interaksjoner og datatilflyt.  

---

## 1. 🎯 Formål

- Dokumentere systemarkitektur for utviklere og bidragsytere.  
- Gi oversikt over komponenter, agenter og interaksjoner.  
- Sikre samsvar med NORSAIN dokumentpolicy og ISO-standarder.  

---

## 2. 📊 Diagrammer

| Fil | Beskrivelse |
|-----|-------------|
| [deepresearch_class.puml](./deepresearch_class.puml) | UML klassediagram over sentrale komponenter. |
| [delegation_sequence.puml](./delegation_sequence.puml) | Sekvensdiagram som viser agentdelegasjon. |
| [system_overview.mmd](./system_overview.mmd) | Mermaid-diagram for systemoversikt. |
| [../uml_class.puml](../uml_class.puml) | Generisk UML klassediagram. |
| [../uml_sequence.puml](../uml_sequence.puml) | Generisk UML sekvensdiagram. |

---

## 3. 🛠 Bruk

- PlantUML-filer (`.puml`) kan genereres med [PlantUML](https://plantuml.com/).  
- Mermaid-filer (`.mmd`) kan forhåndsvises direkte i GitHub eller via [Mermaid Live Editor](https://mermaid.live/).  

---

## 4. 📅 Neste steg

- Ferdigstille detaljert komponentdiagram.  
- Legge til sekvensdiagram for CI/CD pipeline.  
- Utvide systemoversikt med sikkerhets- og governance-lag.  

---

## 5. 📑 Dokumentkontroll

| Eier       | Sist oppdatert | Godkjent av       | Status | Kontakt          | ISO-samsvar |
|------------|----------------|-------------------|--------|------------------|-------------|
| NORSAIN    | 2025-08-18     | Henrik Strand     | Utkast | info@norsain.com | ISO 15489, ISO 30301, ISO 9001:2015 §7.5 |

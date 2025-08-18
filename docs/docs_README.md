---
contact: info@norsain.com
date: 2025-08-18
document_id: DRA-DOC-READ-0001
iso_references:
- ISO 15489 -- Dokumentforvaltning
- ISO 30301 -- Dokumentstyringssystemer
- "ISO 9001:2015 -- §7.5 Dokumentert informasjon"
license: Apache-2.0
owner: Henrik Strand / NORSAIN
path: /docs/README.md
project: deep_research_agent
review_cycle: Kvartalsvis
status: Aktiv
tags:
- dokumentasjon
- oversikt
- deep_research_agent
- policies
- guidelines
title: 📚 Dokumentasjon -- Deep Research Agent
usage_scope: Alle utviklere og bidragsytere
version: 1.2
workspace: Utvikling og dokumentasjon
---

# 📚 Dokumentasjon -- Deep Research Agent

Velkommen til dokumentasjonen for **Deep Research Agent**.\
Dette er inngangsportalen for alt innhold i `docs/` og tilhørende
prosjektfiler.

------------------------------------------------------------------------

## 1. 📖 Innhold

### 1.1 Introduksjon

-   [../README.md](../README.md) -- Hurtigstart, installasjon og kjøring
    av prosjektet.
-   [project_description.md](./project_description.md) -- Mål,
    arkitektur og sikkerhet.

### 1.2 Utviklingsmiljø

-   [.devcontainer/](../.devcontainer/) -- Dev Container-oppsett
    (docker, pre-commit, kubectl).
-   [docker-compose.yml](../docker-compose.yml) -- Lokalt multi-service
    oppsett.
-   [Dockerfile](../Dockerfile) -- Bygg og kjøring av applikasjonen.

### 1.3 Applikasjon

-   [../src/](../src/) -- Kildekode for agentene (Python 3.11).
-   [../requirements.txt](../requirements.txt) --
    Produksjonsavhengigheter.
-   [../requirements-dev.txt](../requirements-dev.txt) --
    Utviklingsavhengigheter.

### 1.4 Infrastruktur (planlagt)

-   [../k8s/](../k8s/) -- Kubernetes manifests for fremtidig deploy.
-   [../terraform/](../terraform/) -- Infrastruktur som kode (namespace,
    SA, GKE-integrasjon -- fremtid).\
-   CI/CD workflows: [../.github/workflows/](../.github/workflows/) --
    Automatiserte pipelines.

### 1.5 Kvalitet og kontroll

-   [../.pre-commit-config.yaml](../.pre-commit-config.yaml) -- Hooks
    for kodekvalitet og sikkerhet.
-   [policy.md](./policy.md) -- Retningslinjer og interne policyer
    (kommer).
-   [security.md](./security.md) -- Retningslinjer for sikkerhet og
    compliance (kommer).

------------------------------------------------------------------------

## 2. 📑 Relaterte styringsdokumenter

-   [PROJECT_ROOM_GUIDELINES.md](PROJECT_ROOM_GUIDELINES.md) --
    Instruksjoner for GPT Prosjektrommet\
-   [policies/dokumentpolicy.md](policies/dokumentpolicy.md) --
    Retningslinjer for dokumentforvaltning\
-   [policies/markdown_visual_policy.md](policies/markdown_visual_policy.md)
    -- Policy for visuell og estetisk utforming\
-   [CHANGELOG.md](../docs/CHANGELOG.md) -- Endringslogg for
    styringsdokumenter

------------------------------------------------------------------------

## 3. 📅 Neste steg

-   Utvide `vertex/`-mappen med eksempler når vi tar i bruk Vertex AI.\
-   Lage Helm chart for fremtidig GKE-deploy.\
-   Ferdigstille `policy.md` og `security.md`.\
-   Legge til arkitekturdiagrammer (Mermaid) under `docs/architecture/`.

------------------------------------------------------------------------

## 4. 📑 Dokumentkontroll

  ----------------------------------------------------------------------------------
  Eier      Sist          Godkjent av      Status   Kontakt            ISO-samsvar
            oppdatert
  --------- ------------- ---------------- -------- ------------------ -------------
  NORSAIN   2025-08-18    CEO Henrik       Aktiv    info@norsain.com   ISO 15489,
                          Strand                                       ISO 30301,
                                                                       ISO 9001:2015
                                                                       §7.5

  ----------------------------------------------------------------------------------

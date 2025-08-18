---
contact: info@norsain.com
date: 2025-08-18
document_id: DRA-DOC-DES-0001
iso_references:
- ISO 15489 -- Dokumentforvaltning
- ISO 30301 -- Dokumentstyringssystemer
- "ISO 9001:2015 -- §7.5 Dokumentert informasjon"
license: Apache-2.0
owner: Henrik Strand / NORSAIN
path: /docs/project_description.md
project: deep_research_agent
review_cycle: Kvartalsvis
status: Aktiv
tags:
- prosjektbeskrivelse
- arkitektur
- sikkerhet
- deep_research_agent
title: 📘 Prosjektbeskrivelse -- Deep Research Agent
usage_scope: Alle utviklere og bidragsytere
version: 1.2
workspace: Utvikling og dokumentasjon
---

# 📘 Prosjektbeskrivelse -- Deep Research Agent

Denne filen beskriver **mål**, **arkitektur** og
**sikkerhetsprinsipper** for prosjektet.\
Se også [README.md](./README.md) for introduksjon, oppsett og
hurtigstart.

------------------------------------------------------------------------

## 1. 🎯 Mål

**Overordnet formål**\
- Bygge opp et **Multi-Agent System (MAS)-nettverk** som NORSAIN kan
bruke selv, og senere tilby som en **tjenesteplattform** til partnere og
kunder.\
- Gjøre MAS til en kjerne for hvordan vi kobler sammen **Digital
Tvilling, IoT, Blockchain og autonome systemer** i et helhetlig
økosystem.

**Første steg (denne fasen)**\
- Utvikle en **Deep Research Agent** som kan:\
- Utføre dyp, iterativ research på komplekse problemstillinger.\
- Bryte ned oppgaver i deloppgaver og delegere til sub-agenter.\
- Integrere eksterne datakilder (web, API, databaser).\
- Generere rapporter i Markdown med kilder og referanser.

**Mellomfase (neste steg)**\
- Knytte sammen flere agenter i et MAS-nettverk for:\
- Samarbeid på tvers av forskningsdomener.\
- Integrasjon i interne prosesser (beslutningsstøtte, analyse,
rapportering).\
- Forbedret sporbarhet og tillit gjennom kvorum-beslutninger og
governance.

**Langsiktig visjon**\
- Integrere MAS med:\
- **Digital Tvilling** -- simulering, overvåkning og prediktiv styring.\
- **IoT og sensorer** -- sanntids datainnsamling fra fysiske systemer.\
- **Blockchain** -- sikre samsvar, sporbarhet og tillit i delte
økosystemer.\
- **Autonome systemer** (f.eks. droner, smarte sensornettverk) -- koble
fysisk og digital verden.

**Effekt**\
- Skape en **selvlærende, transparent og utvidbar agentplattform** som:\
- NORSAIN kan bruke internt for FoU og styring.\
- Tilbys eksternt som tjeneste til partnere og kunder.\
- Kan utvikles videre til å støtte **fremtidens autonome organisasjon**.

------------------------------------------------------------------------

## 2. 🏗️ Arkitektur

-   **Utviklingsmiljø:**\
    Dev Container i VS Code med støtte for Docker, kubectl og pre-commit
    hooks.

-   **Kjerneteknologi:**

    -   Python 3.11 (FastAPI, Pydantic, asyncio).\
    -   Multi-agent orkestrering (CrewAI / egen agent-ramme).

-   **Containerisering:**

    -   Dockerfile for appen.\
    -   `docker-compose.yml` for lokale tjenester (db, redis, helper
        services).

-   **Deploy-miljøer (planlagt):**

    -   **Lokal utvikling** via Docker Compose.\
    -   **Kubernetes (K8s)** for staging/produksjon.\
    -   **Cloud (Vertex AI, GCP)** vurderes på sikt.

-   **CI/CD:**\
    GitHub Actions med støtte for pre-commit checks, image build og
    deploy pipelines.

------------------------------------------------------------------------

## 3. 🔐 Sikkerhet og governance

-   **Identitet og tilgang:**
    -   Ingen statiske nøkler i repoet.\
    -   Tilgang kontrolleres via roller og grupper.
-   **Secrets:**
    -   `.env`-filer ekskluderes med `.gitignore`.\
    -   Fremtidig bruk av secret management i sky.
-   **Policyer og kontroll:**
    -   Binary Authorization (planlagt for images).\
    -   Policy Controller (OPA/Gatekeeper) for Kubernetes (planlagt).
-   **Logging og revisjon:**
    -   Cloud Logging (planlagt) + lokal revisjonslogg.\
    -   Pre-commit hooks for å sikre kodekvalitet og sporbarhet.

------------------------------------------------------------------------

## 4. 📑 Relaterte dokumenter

-   [repo_structure.md](./repo_structure.md) -- Oversikt over repoets
    innhold\
-   [architecture/README.md](./architecture/README.md) -- Arkitektur og
    diagrammer\
-   [cleanup_checklist.md](./cleanup_checklist.md) -- Vedlikehold og
    renhold av repo

------------------------------------------------------------------------

## 5. 📅 Neste steg

1.  Ferdigstille minimal FastAPI-app med healthcheck.\
2.  Lage Helm chart for enkel deploy til K8s.\
3.  Definere første pipeline for research + rapportgenerering.\
4.  Etablere CI/CD med GitHub Actions.

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

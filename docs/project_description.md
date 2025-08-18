---
title: "📘 Prosjektbeskrivelse – Deep Research Agent"
document_id: "DRA-DOC-DES-0001"
version: "1.1"
status: "Utkast"
date: 2025-08-18
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/docs/project_description.md"
tags: ["prosjektbeskrivelse", "arkitektur", "sikkerhet", "deep_research_agent"]
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

# 📘 Prosjektbeskrivelse – Deep Research Agent

Denne filen beskriver **mål**, **arkitektur** og **sikkerhetsprinsipper** for prosjektet.  
Se også [README.md](./README.md) for introduksjon, oppsett og hurtigstart.

---

## 1. 🎯 Mål

- Bygge en **multi-agent forskningsassistent** som kan:
  - Utføre dyp research på et gitt tema.
  - Bryte ned oppgaver i deloppgaver og delegere til sub-agenter.
  - Integrere eksterne datakilder (web, API, databaser).
  - Generere rapporter i Markdown med referanser.
- Sikre at systemet er skalerbart og kan kjøre både lokalt, i containere og i Google Cloud (GKE, Vertex AI).

---

## 2. 🏗️ Arkitektur

- **Utviklingsmiljø:**  
  Dev Container i VS Code med støtte for Docker, gcloud, kubectl, helm og pre-commit hooks.
- **Kjerneteknologi:**  
  - Python 3.11 (FastAPI, Pydantic, asyncio).  
  - Multi-agent orkestrering (CrewAI / egen agent-ramme).
- **Containerisering:**  
  - Dockerfile for appen.  
  - `docker-compose.yml` for lokale tjenester (db, redis, welcome-service).
- **Deploy-miljøer:**  
  - **Lokal utvikling** via Docker Compose.  
  - **Google Kubernetes Engine (GKE)** for staging/produksjon.  
  - **Vertex AI** for modelltrening og pipeline-orchestrering.
- **CI/CD:**  
  GitHub Actions / Cloud Build med støtte for pre-commit checks, image build og deploy til GKE.

---

## 3. 🔐 Sikkerhet og governance

- **Identitet og tilgang:**  
  - Google Workload Identity for pods (ingen statiske nøkler).  
  - IAM-roller gis via Google Groups, ikke enkeltbrukere.
- **Secrets:**  
  - Secret Manager via CSI-driver i GKE.  
  - Ingen API-nøkler sjekkes inn i repo.
- **Policyer og kontroll:**  
  - Binary Authorization for images.  
  - Policy Controller (OPA/Gatekeeper) for Kubernetes.
- **Logging og revisjon:**  
  - Cloud Logging + sentral revisjonslogg.  
  - Pre-commit hooks for å sikre kodekvalitet og sporbarhet.

---

## 4. 📅 Neste steg

1. Ferdigstille minimal FastAPI-app med healthcheck.  
2. Lage Helm chart for enkel deploy til GKE.  
3. Definere første Vertex AI pipeline for research + rapportgenerering.  
4. Etablere CI/CD med GitHub Actions og Cloud Build.  

---

## 5. 📑 Dokumentkontroll

| Eier       | Sist oppdatert | Godkjent av       | Status | Kontakt          | ISO-samsvar |
|------------|----------------|-------------------|--------|------------------|-------------|
| NORSAIN    | 2025-08-18     | Henrik Strand     | Utkast | info@norsain.com | ISO 15489, ISO 30301, ISO 9001:2015 §7.5 |


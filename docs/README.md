---
title: "📚 Dokumentasjon – Deep Research Agent"
document_id: "DRA-DOC-READ-0001"
version: "1.1"
status: "Utkast"
date: 2025-08-18
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/docs/README.md"
tags: ["dokumentasjon", "oversikt", "deep_research_agent"]
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

# 📚 Dokumentasjon – Deep Research Agent

Velkommen til dokumentasjonen for **Deep Research Agent**.
Denne siden fungerer som inngangsport og oversikt over alt innhold i `docs/` og tilhørende prosjektfiler.

---

## 1. 📖 Innhold

### 1.1 Introduksjon
- [../README.md](../README.md) – Hurtigstart, installasjon og kjøring av prosjektet.
- [project_description.md](./project_description.md) – Mål, arkitektur og sikkerhet.

### 1.2 Utviklingsmiljø
- [.devcontainer/](../.devcontainer/) – Dev Container-oppsett (gcloud, kubectl, docker, pre-commit).
- [docker-compose.yml](../docker-compose.yml) – Lokalt multi-service oppsett.
- [Dockerfile](../Dockerfile) – Bygg og kjøring av applikasjonen.

### 1.3 Applikasjon
- [../src/](../src/) – Kildekode for agentene (Python 3.11).
- [../requirements.txt](../requirements.txt) – Produksjonsavhengigheter.
- [../requirements-dev.txt](../requirements-dev.txt) – Utviklingsavhengigheter.

### 1.4 Infrastruktur
- [../k8s/](../k8s/) – Kubernetes manifests for deploy.
- [../terraform/](../terraform/) – Infrastruktur som kode (namespace, SA, GKE-integrasjon).
- CI/CD workflows: [../.github/workflows/](../.github/workflows/) – Automatiserte pipelines.

### 1.5 MLOps / Vertex AI
- [vertex/](./vertex/) – (planlagt) Pipelines, modellregister og treningsjobber i Vertex AI.
- Dokumentasjon for datadrift og modellovervåking (kommer).

### 1.6 Kvalitet og kontroll
- [../.pre-commit-config.yaml](../.pre-commit-config.yaml) – Hooks for kodekvalitet og sikkerhet.
- [policy.md](./policy.md) – Retningslinjer og interne policyer (kommer).
- [security.md](./security.md) – Retningslinjer for sikkerhet og compliance (kommer).

---

## 2. 📅 Neste steg

- Utvide `vertex/` med pipeline-eksempler.
- Ferdigstille `policy.md` og `security.md`.
- Legge til arkitekturdiagrammer (Mermaid) under `docs/architecture/`.

---

## 3. 📑 Dokumentkontroll

| Eier       | Sist oppdatert | Godkjent av       | Status | Kontakt          | ISO-samsvar |
|------------|----------------|-------------------|--------|------------------|-------------|
| NORSAIN    | 2025-08-18     | Henrik Strand     | Utkast | info@norsain.com | ISO 15489, ISO 30301, ISO 9001:2015 §7.5 |

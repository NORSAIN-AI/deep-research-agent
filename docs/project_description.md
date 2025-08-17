# 📘 Prosjektbeskrivelse – Deep Research Agent

Denne filen beskriver **mål**, **arkitektur** og **sikkerhetsprinsipper** for prosjektet.
Se også [README.md](./README.md) for introduksjon, oppsett og hurtigstart.

---

## 🎯 Mål

- Bygge en **multi-agent forskningsassistent** som kan:
  - Utføre dyp research på et gitt tema.
  - Bryte ned oppgaver i deloppgaver og delegere til sub-agenter.
  - Integrere eksterne datakilder (web, API, databaser).
  - Generere rapporter i Markdown med referanser.
- Sikre at systemet er skalerbart og kan kjøre både lokalt, i containere og i Google Cloud (GKE, Vertex AI).

---

## 🏗️ Arkitektur

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

## 🔐 Sikkerhet og governance

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

## 📅 Neste steg

1. Ferdigstille minimal FastAPI-app med healthcheck.
2. Lage Helm chart for enkel deploy til GKE.
3. Definere første Vertex AI pipeline for research + rapportgenerering.
4. Etablere CI/CD med GitHub Actions og Cloud Build.

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | info@norsain.com |

# 📚 Dokumentasjon – deep_research_agent

Velkommen til dokumentasjonen for **Deep Research Agent**.  
Denne siden fungerer som inngangsport og oversikt over alt innhold i `docs/` og tilhørende prosjektfiler.

---

## 📖 Innhold

### 1. Introduksjon
- [../README.md](../README.md) – Hurtigstart, installasjon og kjøring av prosjektet.
- [prosjektbeskrivelse.md](./prosjektbeskrivelse.md) – Mål, arkitektur og sikkerhet.

### 2. Utviklingsmiljø
- [.devcontainer/](../.devcontainer/) – Dev Container-oppsett (gcloud, kubectl, docker, pre-commit).
- [docker-compose.yml](../docker-compose.yml) – Lokalt multi-service oppsett.
- [Dockerfile](../Dockerfile) – Bygg og kjøring av applikasjonen.

### 3. Applikasjon
- [../app/](../app/) – Kildekode for agentene (Python 3.11).
- [../requirements.txt](../requirements.txt) – Produksjonsavhengigheter.
- [../requirements-dev.txt](../requirements-dev.txt) – Utviklingsavhengigheter.

### 4. Infrastruktur
- [../k8s/](../k8s/) – Kubernetes manifests for deploy.
- [../terraform/](../terraform/) – Infrastruktur som kode (namespace, SA, GKE-integrasjon).
- CI/CD workflows: [../.github/workflows/](../.github/workflows/) – Automatiserte pipelines.

### 5. MLOps / Vertex AI
- [vertex/](./vertex/) – (planlagt) Pipelines, modellregister og treningsjobber i Vertex AI.
- Dokumentasjon for datadrift og modellovervåking (kommer).

### 6. Kvalitet og kontroll
- [../.pre-commit-config.yaml](../.pre-commit-config.yaml) – Hooks for kodekvalitet og sikkerhet.
- [policy.md](./policy.md) – Retningslinjer og interne policyer (kommer).
- [security.md](./security.md) – Retningslinjer for sikkerhet og compliance (kommer).

---

## 📅 Neste steg
- Utvide `vertex/` med pipeline-eksempler.
- Ferdigstille `policy.md` og `security.md`.
- Legge til arkitekturdiagrammer (Mermaid) under `docs/architecture/`.

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | info@norsain.com |

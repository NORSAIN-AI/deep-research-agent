---
title: "Policy for håndtering av utkastfiler (/docs/_drafts/)"
document_id: "DRA-POL-DRAFTS-0001"
version: "1.0"
status: "Aktiv"
date: "2025-08-18"
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/docs/policies/drafts_handling.md"
tags: ["drafts", "utkast", "policy", "dokumentasjon"]
project: "deep_research_agent"
workspace: "Utvikling og dokumentasjon"
usage_scope: "Alle utviklere og bidragsytere"
review_cycle: "Kvartalsvis"
license: "CC-BY-SA-4.0"
---

## 📂 Policy for håndtering av utkastfiler

Denne policyen regulerer hvordan mappen `/docs/_drafts/` skal brukes til **arbeidsnotater og utkast**.

Målet er å sikre tydelig skille mellom **utkast** og **godkjente dokumenter**, i tråd med NORSAIN dokumentpolicy.

---

## 📌 Retningslinjer

- Alle filer i `/docs/_drafts/` skal merkes med **status: "Utkast"** i metadata-header.
- Filnavn bør ende på `.draft` eller ha `-draft.md` for å unngå forveksling med aktive dokumenter.
- Dokumenter i `_drafts/` har **ingen offisiell status** før de er godkjent.

Når dokumentet er klart og godkjent:

1. Endre status til **Aktiv**.
2. Flytt filen til riktig katalog (f.eks. `/docs/deployment/`, `/docs/policies/`).
3. Oppdater [CHANGELOG.md](../CHANGELOG.md) med referanse til flyttingen.

---

## 📎 Eksempler på filer

- `Dockerfile.draft`
- `docker-compose.yml.draft`
- `cloudbuild.yaml.draft`
- `deployment_guide-draft.md`

---

## ✅ Hvorfor denne policyen

- Skiller tydelig mellom utkast og godkjente dokumenter (i tråd med [NORSAIN dokumentpolicy](../dokumentpolicy_norsain.md)).
- Reduserer risiko for at uferdige konfigurasjoner brukes i produksjon.
- Gjør det enkelt å samarbeide og eksperimentere med nye dokumenter.

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|------|----------------|-------------|--------|---------|
| Henrik Strand / NORSAIN | 2025-08-18 | – | Aktiv | [info@norsain.com](mailto:info@norsain.com) |

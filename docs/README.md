---
contact: info@norsain.com
date: 2025-08-18
document_id: DRA-README-0001
license: CC-BY-SA-4.0
owner: Henrik Strand / NORSAIN
path: /README.md
project: NORSAIN Core Platform
review_cycle: Kvartalsvis
status: Aktiv
tags:
- mas
- research
- agent
- documentation
title: deep_research_agent -- README
usage_scope: Hoveddokumentasjon for hele repoet
version: 1.0
workspace: GPT Project Room
---

# 🤖 deep_research_agent

Et **2025-klar Multi-Agent (MAS) forskningsagent** bygget på
**CrewAI** + **OpenAI SDK**, med robust dokumentasjon, test, CI/CD og
governance.

------------------------------------------------------------------------

## 🚀 Nøkkelfunksjoner

-   🔄 Dyp, iterativ forskning (**plan → hent → analyser → syntetiser**)
-   🌐 Integrerte verktøy: **SerperDevTool** (web), **GithubSearchTool**
    (kode)
-   ⚙️ YAML-konfigurasjon for agenter og tasks
-   💻 CLI og Python-API
-   🧪 Evalueringer, sikkerhetspolicy og release-automatisering
-   🐳 Devcontainer og Docker-støtte

------------------------------------------------------------------------

## 📦 Kjappstart

``` bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # fyll inn nøkler
python -m src.main "agentic ai trender 2025"
```

------------------------------------------------------------------------

## 🧱 Struktur (høy-nivå)

Se [`docs/repo_structure.md`](docs/repo_structure.md) for komplett
struktur.

    deep-research-agent/
     ├─ docs/             # dokumentasjon, policies, UML, ADR
     ├─ reports/          # genererte rapporter
     ├─ templates/        # maler for rapporter, prompts, sjekklister
     ├─ src/              # kildekode (CrewAI-agenter, gen_report.py)
     ├─ tests/            # tester og evalueringer
     ├─ config/           # YAML-konfig for agenter/tasks
     └─ .github/          # CI/CD workflows

------------------------------------------------------------------------

## 🔐 Sikkerhet

-   🔑 Nøkler kun i `.env` / CI-secrets
-   📜 `SECURITY.md` og `CODEOWNERS` satt opp
-   ✅ Pre-commit hooks og avhengighetsvarsling aktivert

------------------------------------------------------------------------

  --------------------------------------------------------------------------
  Eier      Sist oppdatert   Godkjent av         Status   Kontakt
  --------- ---------------- ------------------- -------- ------------------
  NORSAIN   2025-08-18       CEO Henrik Strand   Aktiv    info@norsain.com

  --------------------------------------------------------------------------

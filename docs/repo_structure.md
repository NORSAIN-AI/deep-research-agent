---
contact: info@norsain.com
date: 2025-08-18
document_id: DRA-DOC-STR-0001
iso_references:
- ISO 15489 -- Dokumentforvaltning
- ISO 30301 -- Dokumentstyringssystemer
- "ISO 9001:2015 -- §7.5 Dokumentert informasjon"
license: Apache-2.0
owner: Henrik Strand / NORSAIN
path: /docs/repo_structure.md
project: deep_research_agent
review_cycle: Kvartalsvis
status: Aktiv
tags:
- repo
- struktur
- oversikt
- deep_research_agent
title: 📂 Repo-struktur -- Deep Research Agent
usage_scope: Alle utviklere og bidragsytere
version: 1.1
workspace: Utvikling og dokumentasjon
---

# 📂 Repo-struktur -- Deep Research Agent

Denne filen beskriver innholdet i repoet, med mapper, filer og deres
funksjon.\
Formatet er laget for å gi rask oversikt for utviklere, bidragsytere og
reviewers.

------------------------------------------------------------------------

## 🔧 Dev & konfig

  -----------------------------------------------------------------------
  Fil / Mappe                                        Beskrivelse
  -------------------------------------------------- --------------------
  `.devcontainer/`                                   Konfig for VS Code
                                                     devcontainer
                                                     (Dockerfile, JSON,
                                                     post-create script).

  `.env.example`                                     Eksempel på
                                                     miljøvariabler
                                                     (API-nøkler etc).

  `.gitattributes`                                   Git-atferd, f.eks.
                                                     line endings.

  `.gitignore`                                       Hvilke filer som
                                                     ekskluderes fra Git.

  `.pre-commit-config.yaml`                          Pre-commit hooks
                                                     (lint, typecheck,
                                                     security checks).
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🔐 GitHub-integrasjon

  ------------------------------------------------------------------------------
  Fil / Mappe                                          Beskrivelse
  ---------------------------------------------------- -------------------------
  `.github/ISSUE_TEMPLATE/`                            Maler for bug reports og
                                                       feature requests.

  `.github/PULL_REQUEST_TEMPLATE.md`                   Standard mal for pull
                                                       requests.

  `.github/workflows/ci.yml`                           CI-pipeline (bygg, test).

  `.github/workflows/codeql.yml`                       CodeQL security scan.

  `.github/workflows/pre-commit.yml`                   Kjører pre-commit hooks.

  `.github/workflows/release-please.yml`               Release-automatisering.

  `.github/workflows/sanity_live.yml`                  Live sanity checks.

  `.github/workflows/secrets-check.yml`                Sjekk for lekkede nøkler.
  ------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📜 Dokumentasjon

  ----------------------------------------------------------------------------
  Fil / Mappe                                          Beskrivelse
  ---------------------------------------------------- -----------------------
  `README.md`                                          Hovedintro til repoet
                                                       (quickstart, sikkerhet,
                                                       struktur).

  `CONTRIBUTING.md`                                    Retningslinjer for
                                                       bidrag.

  `CODEOWNERS`                                         Definerer ansvarlige
                                                       for kodeområder.

  `SECURITY.md`                                        Security policy og
                                                       rapportering.

  `LICENSE`                                            Juridisk lisens.

  `docs/README.md`                                     Intro til
                                                       dokumentasjonsmappen.

  `docs/architecture/`                                 Arkitektur-diagrammer
                                                       og beskrivelser.

  `docs/project_description.md`                        Prosjektbeskrivelse
                                                       (mål, arkitektur,
                                                       sikkerhet).

  `docs/repo_structure.md`                             **Denne filen** --
                                                       repo-struktur.

  `docs/user_stories.md`                               Definerte
                                                       brukerhistorier.
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧪 Evaluering & eksempler

  Fil / Mappe                   Beskrivelse
  ----------------------------- -------------------------------------
  `evals/eval_plan.md`          Evalueringsplan for agenter/system.
  `examples/run_example.py`     Kjørbart eksempel på agentflow.
  `outputs/.gitkeep`            Tom mappe beholdes i Git.
  `prompts/system_prompts.md`   Definerte system- og agent-prompts.

------------------------------------------------------------------------

## ⚙️ Scripts

  Fil / Mappe               Beskrivelse
  ------------------------- -------------------------------------
  `scripts/gen_report.py`   Genererer rapporter.
  `scripts/gen_tree.ps1`    Repo-tree for PowerShell.
  `scripts/gen_tree.sh`     Repo-tree for Bash.
  `scripts/run.ps1`         Kjør systemet (Windows/PowerShell).
  `scripts/run.sh`          Kjør systemet (Linux/Mac/Bash).

------------------------------------------------------------------------

## 🧠 Kildekode (`src/`)

  Fil / Mappe              Beskrivelse
  ------------------------ -----------------------------------------
  `src/__init__.py`        Gjør `src` til Python-pakke.
  `src/agents.yaml`        Definisjon av agenter (roller, config).
  `src/crew.py`            CrewAI-integrasjon (MAS-koordinering).
  `src/main.py`            Entrypoint (CLI/command runner).
  `src/openai_client.py`   Wrapper for OpenAI SDK.
  `src/tasks.yaml`         Definerte tasks/workflows.

------------------------------------------------------------------------

## 🧪 Tester (`tests/`)

  Fil / Mappe                Beskrivelse
  -------------------------- ------------------------------------
  `tests/conftest.py`        Pytest fixtures.
  `tests/test_env.py`        Tester på miljøoppsett.
  `tests/test_imports.py`    Sjekker at moduler kan importeres.
  `tests/test_pipeline.py`   Tester forskningspipeline.
  `tests/test_smoke.py`      Små sanity-tester.

------------------------------------------------------------------------

## 📦 Dependencies

  Fil                      Beskrivelse
  ------------------------ --------------------------------------
  `pyproject.toml`         Prosjektmetadata (Poetry / PEP 621).
  `requirements.txt`       Runtime dependencies.
  `requirements-dev.txt`   Dev/test dependencies.

------------------------------------------------------------------------

## 🔗 Relaterte dokumenter

-   [project_description.md](./project_description.md) --
    Prosjektbeskrivelse (mål, arkitektur, sikkerhet)\
-   [architecture/README.md](./architecture/README.md) -- Arkitektur og
    diagrammer\
-   [cleanup_checklist.md](./cleanup_checklist.md) -- Repo-vedlikehold

------------------------------------------------------------------------

## 📑 Dokumentkontroll

  ----------------------------------------------------------------------------------
  Eier      Sist          Godkjent av      Status   Kontakt            ISO-samsvar
            oppdatert
  --------- ------------- ---------------- -------- ------------------ -------------
  NORSAIN   2025-08-18    CEO Henrik       Aktiv    info@norsain.com   ISO 15489,
                          Strand                                       ISO 30301,
                                                                       ISO 9001:2015
                                                                       §7.5

  ----------------------------------------------------------------------------------

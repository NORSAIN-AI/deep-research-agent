---
title: "Contributing Guidelines – Deep Research Agent"
document_id: "NS-DRA-CONTRIB-0001"
version: "1.0"
status: "Aktiv"
date: "2025-08-18"
owner: "Henrik Strand / NORSAIN"
contact: "info@norsain.com"
path: "/contributing.md"
tags: ["git", "workflow", "contributing", "policy"]
project: "Deep Research Agent"
workspace: "GPT Project Room"
usage_scope: "Utviklingspraksis og vedlikehold"
review_cycle: "Kvartalsvis"
license: "CC-BY-SA-4.0"
---

# 🤝 Contributing Guidelines

Takk for at du ønsker å bidra til **Deep Research Agent**!
Følg disse retningslinjene for å sikre en ryddig og effektiv utviklingsprosess.

---

## 📌 Workflow

- **Bruk feature branches**
  - Gi dem meningsfulle navn (`feature/add-agent`, `fix/logging`).
  - Ikke push direkte til `main`.

- **Commit-meldinger**
  - Følg formatet: `<type>(<scope>): <beskrivelse>`
    Eksempel: `feat(agent): add delegation logic`
  - Typer: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

- **Pull Requests (PRs)**
  - Knytt til issue (#id) hvis aktuelt.
  - Beskriv hva som er gjort og hvorfor.
  - Minst **én godkjenning** kreves før merge.

---

## 🛠️ Code Style & Quality

- **Pre-commit hooks** kjører automatisk:
  - [`black`](https://black.readthedocs.io/) – formattering
  - [`ruff`](https://docs.astral.sh/ruff/) – linting
  - [`mypy`](http://mypy-lang.org/) – type-sjekk

- **Testdekning**
  - Alle nye features skal ha tester.
  - Bruk `pytest` og kjør lokalt før PR.

```bash
pytest -q --cov=src

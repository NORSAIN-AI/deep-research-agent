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
  - [`black`](https://black.readthedocs.io/) (formatterer kode)
  - [`ruff`](https://docs.astral.sh/ruff/) (linting)
  - `mypy` (type-sjekk)

- **Testdekning**
  - Alle nye features skal ha tester.
  - Bruk `pytest` og kjør lokalt før PR.

```bash
pytest -q --cov=src

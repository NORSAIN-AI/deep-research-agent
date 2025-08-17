# 🤖 deep_research_agent

Et 2025-klar Multi-Agent (MAS) forskningsagent bygget på **CrewAI** + **OpenAI SDK**, med robust dokumentasjon, test, CI/CD og governance.

## 🚀 nøkkelfunksjoner
- Dyp, iterativ forskning (plan → hent → analyser → syntetiser)
- Verktøy: SerperDevTool (web), GithubSearchTool (kode)
- YAML-konfig for agenter og tasks, CLI og Python-API
- Evalueringer, sikkerhetspolicy, release-automatisering, og devcontainer

## 📦 kjappstart
```bash
python -m venv .venv && source .venv/bin/activate  # win: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # fyll inn nøkler
python -m src.main "agentic ai trender 2025"
```

## 🧱 struktur (høy-nivå)
Se `docs/repo_structure.md` for komplett struktur.

## 🔐 sikkerhet
- Nøkler kun i .env / CI-secrets
- SECURITY.md og CODEOWNERS satt opp
- Pre-commit og avhengighetsvarsling


---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | info@norsain.com |

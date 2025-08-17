# 🔐 Security Guidelines

Dette dokumentet beskriver hvordan sikkerhet håndteres i **Deep Research Agent**-prosjektet.
Målet er å beskytte kildekode, data, hemmeligheter og driftsmiljø mot uautorisert tilgang og misbruk.

---

## 📢 Rapportering av sårbarheter
- Send sårbarhetsrapporter til **security@norsain.com**.
- Ikke opprett en offentlig GitHub issue for sikkerhetsfunn.
- Alle innsendte rapporter behandles konfidensielt og følges opp innen 72 timer.

---

## 🔑 Hemmeligheter og API-nøkler
- Ikke sjekk inn API-nøkler, tokens eller sertifikater i GitHub-repoet.
- Bruk **GitHub Actions Secrets** (`OPENAI_API_KEY`, `SERPER_API_KEY`, osv.) for CI/CD.
- Lokalt: lagre hemmeligheter i `.env` (aldri committ denne filen, se `.gitignore`).
- Del aldri nøkler i Slack, e-post eller andre usikrede kanaler.

---

## 🛡️ Sikkerhetspraksis for utvikling
- Kjør `pre-commit` hooks for å fange opp utilsiktet lekkasje av hemmeligheter.
- Bruk `bandit` og `safety` for sikkerhetsanalyse av Python-avhengigheter.
- Oppdater `requirements.txt` og `requirements-dev.txt` jevnlig.
- Kjør `dependabot` eller tilsvarende for automatisk overvåking av tredjepartsbiblioteker.

---

## ☁️ Infrastruktur og deploy
- Bruk **minste nødvendige privilegier** (PoLP) for service accounts og IAM-roller i Google Cloud / Vertex AI / GKE.
- Aktiver logging og overvåking for alle tjenester.
- Krypter data både i hvile (at rest) og under transport (in transit).
- Bruk **GCP Secret Manager** eller tilsvarende for å håndtere hemmeligheter i produksjon.

---

## 🔍 Overvåking og respons
- Sårbarhetsskanning kjører automatisk via GitHub Actions (CodeQL + `pip-audit`).
- Hendelser håndteres i tråd med NORSAIN sin **Incident Response-prosedyre** (lenkes når klar).
- Alle sikkerhetsrelaterte commits skal peer-reviewes før merge til `main`.

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | security@norsain.com |

# 👤 User Stories – Deep Research Agent

Denne filen samler alle identifiserte user stories for prosjektet.
Format: *Som en [rolle], vil jeg [behov], slik at jeg [mål]*.

---

## US-001: Forskning på tema → Markdown-rapport
**Som en** forsker
**vil jeg** starte en deep research på et tema
**slik at jeg** får en sammenhengende rapport i Markdown med kilder uten manuell innsats.

**Acceptance Criteria**
- Input: Tema som streng.
- Output: Generert Markdown-rapport med kilder og referanser.
- Rapporten skal være konsistent strukturert (intro, funn, referanser).
- Systemet skal kunne kjøre lokalt og i GCP (Vertex AI / GKE).

---

## US-002: Sub-agenter og delegasjon
**Som en** utvikler
**vil jeg** utvide agenten med sub-agenter
**slik at** systemet kan håndtere komplekse oppgaver parallelt.

**Acceptance Criteria**
- Delegasjon mellom agenter fungerer via `allow_delegation`.
- Sub-agenter skal kunne kjøre uavhengig, men rapportere tilbake til hovedagent.
- Resultater skal samles og integreres i en helhetlig rapport.
- Logging av oppgaver per agent for sporbarhet.

---

## Planlagte User Stories (skisse)
- US-003: Som prosjektleder vil jeg kunne kjøre predefinerte research-maler, slik at prosjekter starter raskere.
- US-004: Som dataanalytiker vil jeg kunne hente resultater fra eksterne API-er (f.eks. Google Scholar, ArXiv).
- US-005: Som compliance-ansvarlig vil jeg at systemet logger alle agentbeslutninger, slik at vi kan revidere og sikre etterlevelse av policy.

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | info@norsain.com |

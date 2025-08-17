# 📝 Evalueringsplan – Deep Research Agent

## 🎯 Mål
Verifisere at genererte rapporter og resultater fra agentene oppfyller krav til:
- **Kildekvalitet** (troværdige, transparente og etterprøvbare kilder).  
- **Konsistens** (sammenhengende og logisk struktur i rapporter).  
- **Handlingsbarhet** (resultatene kan brukes til beslutning eller videre analyse).  

---

## 🛠️ Metoder

### 1. Sjekkliste (manuell)
- ✅ Er alle kilder oppgitt med URL / DOI / referanse?  
- ✅ Er rapporten strukturert (intro, hoveddel, konklusjon, referanser)?  
- ✅ Er argumentasjonen logisk uten selvmotsigelser?  
- ✅ Er eventuelle anbefalinger tydelige og realistiske?  
- ✅ Er språk og tone profesjonell og forståelig?  

### 2. Automatisert evaluering (pytest + scripts)
- [ ] Test for minimum antall kilder (> 3).  
- [ ] Test at alle referanser har gyldig URL-format.  
- [ ] Test at Markdown validerer uten feil.  
- [ ] Test at nøkkelord/tema faktisk finnes i rapporten.  
- [ ] Test at rapporten ikke inneholder tomme seksjoner.  

### 3. Kvalitative kriterier (peer review)
- Review av minst én annen utvikler/forsker.  
- Tilbakemelding logges i GitHub Issues / Project board.  

---

## 📊 Output
- Evalueringsrapport (Markdown eller PDF) per leveranse.  
- Testresultater fra `pytest` lagres som artefakter i CI/CD.  
- Oppsummering per sprint i GitHub Project board.

---

## 🔄 Integrasjon i arbeidsflyt
- **Pre-commit hooks**: sjekker enkel syntaks, URL-format og filstruktur.  
- **CI/CD (GitHub Actions / Cloud Build)**: kjører pytest-baserte evalueringstester.  
- **Review-prosess**: obligatorisk code review og eval-plan sjekkliste.  

---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|  
| NORSAIN / Henrik Strand | 2025-08-17 | – | Utkast | info@norsain.com |

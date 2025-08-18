---

## title: cleanup checklist document-id: DRA-MNT-0001 version: 1.0 status: aktiv date: 2025-08-18 owner: norsain / henrik strand contact: [info@norsain.com](mailto\:info@norsain.com)

# cleanup checklist

En praktisk sjekkliste for å holde repoet rent og raskt. Brukes når noen har sjekket inn lokale miljøer, cache, eller genererte artefakter.

---

## 🎯 mål

- Unngå at `venv/`, `__pycache__`, binære artefakter og lokale databaser havner i git-historikken
- Redusere repo-størrelse og bygge-/CI-tid
- Sikre at `.gitignore` og utviklerpraksis er konsistente på tvers av teamet

## 📦 hva skal **ikke** ligge i repoet

- Virtuelle miljøer: `.venv/`, `venv/`, `Scripts/`, `Lib/`, `Include/`, `share/`, `pyvenv.cfg`
- Cache og byggeartefakter: `__pycache__/`, `*.pyc`, `*.pyd`, `*.so`, `*.dll`, `*.egg*`, `.mypy_cache/`, `.pytest_cache/`, `htmlcov/`
- Lokale data: `db/`, `*.sqlite3`, `*.db`, `tmp/`, `logs/`
- Genererte rapporter/outputs: `outputs/*` (behold `outputs/.gitkeep`)
- Personlige editor-filer: `.idea/`, lokale `.vscode/settings.json` (med mindre bevisst delt)

## ✅ hurtigsjekk (les/skriv)

1. Se hva som *allerede* er tracket, men burde ignoreres
   - **Windows CMD**
     ```bat
     git ls-files -ci --exclude-standard
     git ls-files -oi --exclude-standard
     ```
   - **bash/powershell**
     ```bash
     git ls-files -ci --exclude-standard
     git ls-files -oi --exclude-standard
     ```
2. Verifiser `.gitignore` (se mal i repoet)
3. Fjern alt som feilaktig er tracket (behold filer lokalt)

## 🧹 opprydding – standardtilfelle

**Fjern fra git-tracking, men behold lokalt:**

- Klassisk venv-map struktur i roten (Windows)
  ```bat
  git rm -r --cached Scripts Lib Include share
  git rm -r --cached pyvenv.cfg
  ```
- Klassisk venv-mappe
  ```bat
  git rm -r --cached .venv venv
  ```
- Lokale databaser / outputs
  ```bat
  git rm -r --cached db
  git rm -r --cached outputs/*.md
  ```
- Commit & push
  ```bat
  git add .gitignore
  git commit -m "chore: fjernet venv og lokale filer fra git-tracking"
  git push
  ```

## 🧪 verifisering

- Sjekk at ingen venv-mapper er tracket lenger
  ```bat
  git ls-files | findstr /i "Scripts Lib Include share pyvenv.cfg"
  ```
- Sjekk status
  ```bat
  git status
  ```

## 🔐 sjekk for hemmeligheter

- `.env` og `*.env` skal ikke ligge i repoet
- Kjør et sekret-scan periodisk (eksempel med `gitleaks`):
  ```bash
  gitleaks detect --no-banner -v
  ```
- Hvis hemmeligheter har blitt committed tidligere: **ruller tilbake** nøkler og roter nye i leverandør (OpenAI, GCP, GitHub, etc.)

## 🧯 hvis skade allerede har skjedd (rewrite historikk)

> **Brukes kun hvis store binærer/venv/hemmeligheter ligger i historikken.**

- Anbefalt verktøy: `git filter-repo` (erstatter `filter-branch`/BFG)
  ```bash
  # eksempel: fjerne hele venv/ fra historikk
  git filter-repo --path venv --path .venv --invert-paths
  # eksempel: fjerne db/
  git filter-repo --path db --invert-paths
  ```
- **Viktig:** Force-push etter rewrite, og informer alle som har clonet repoet
  ```bash
  git push --force
  ```

## 🧰 anbefalt struktur for lokale miljøer

- Bruk alltid `.venv/` i prosjektroten (allerede i `.gitignore`)
  ```bash
  python -m venv .venv
  # Windows
  .venv\\Scripts\\activate
  # macOS/Linux
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

## 🧱 .gitattributes (valgfritt men anbefalt)

Legg til for konsistente line-endings og for å unngå at binære filer diffes tungt:

```gitattributes
* text=auto
*.png binary
*.jpg binary
*.gif binary
*.pdf binary
*.puml text eol=lf
*.mmd text eol=lf
```

## 🧭 praksis & dokumentasjon

- Dokumentér i `README.md` → **Development setup** og **Hva ligger ikke i repoet**
- Hold en kort **Conventional Commits**-guide i `CONTRIBUTING.md`
- Legg inn **pre-commit** hooker (black/ruff/mypy/yaml/toml/json/trim-whitespace) – finnes allerede i prosjektet

## 🧪 pre-commit kjappstart

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## 🗂️ anbefalt oppryddingspolicy ved PR

- PR som inneholder venv/ eller lokale artefakter **skal avvises**
- Be bidragsyter kjøre sjekklisten og oppdatere PR
- Valider at `.gitignore` ikke brytes

---

### sjekkliste (kopier til PR-beskrivelse)

-

---

| Eier                    | Sist oppdatert | Godkjent av | Status | Kontakt                                      |
| ----------------------- | -------------- | ----------- | ------ | -------------------------------------------- |
| NORSAIN / Henrik Strand | 2025-08-18     | TBA         | Aktiv  | [info@norsain.com](mailto\:info@norsain.com) |

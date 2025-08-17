#!/usr/bin/env bash
set -euo pipefail

OUTPUT_FILE="docs/repo_structure.md"

# Sørg for at tree er installert
if ! command -v tree &> /dev/null; then
  echo "⚠️ tree is not installed. Run: sudo apt-get install tree"
  exit 1
fi

# Header
echo "# 📁 Repository structure" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo '```' >> "$OUTPUT_FILE"

# Generer mappe/filstruktur
tree -a -I ".git|__pycache__|.mypy_cache|.venv|venv|.DS_Store" >> "$OUTPUT_FILE"

# Footer
echo '```' >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Dokumentkontrolltabell
cat <<EOF >> "$OUTPUT_FILE"
---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | $(date +%Y-%m-%d) | – | Utkast | info@norsain.com |
EOF

echo "✅ Struktur eksportert til $OUTPUT_FILE"

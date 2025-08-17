$OutputFile = "docs/repo_structure.md"

# Header
"# 📁 Repository structure`n" | Out-File $OutputFile
"```" | Out-File $OutputFile -Append

# Generer struktur (ekskluder noen mapper)
tree /F | Out-File $OutputFile -Append

"```" | Out-File $OutputFile -Append
"" | Out-File $OutputFile -Append

# Dokumentkontroll
@"
---

| Eier | Sist oppdatert | Godkjent av | Status | Kontakt |
|---|---|---|---|---|
| NORSAIN / Henrik Strand | $(Get-Date -Format "yyyy-MM-dd") | – | Utkast | info@norsain.com |
"@ | Out-File $OutputFile -Append

Write-Host "✅ Struktur eksportert til $OutputFile"

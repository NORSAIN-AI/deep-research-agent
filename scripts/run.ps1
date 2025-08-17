param(
    [string]$topic = "agentic ai trender 2025"
)

Write-Host "🚀 Kjører DeepResearchCrew med tema: $topic" -ForegroundColor Cyan

try {
    # Bruker Python modulen src.main
    python -m src.main "$topic"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Kjøring fullført" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Python returnerte feil (exit code $LASTEXITCODE)" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}
catch {
    Write-Host "⚠️ Feil ved kjøring av Python: $_" -ForegroundColor Red
    exit 1
}

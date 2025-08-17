#!/usr/bin/env bash
# run.sh - kjør DeepResearchCrew fra src.main
set -euo pipefail

TOPIC="${*:-agentic ai trender 2025}"

echo "🚀 Kjører DeepResearchCrew med tema: \"$TOPIC\""

if python -m src.main "$TOPIC"; then
    echo "✅ Kjøring fullført"
else
    CODE=$?
    echo "❌ Python returnerte feil (exit code $CODE)"
    exit $CODE
fi

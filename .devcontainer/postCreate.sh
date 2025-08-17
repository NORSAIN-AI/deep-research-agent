#!/usr/bin/env bash
set -euo pipefail

echo "🚀 postCreate start"

# 1) Git-identitet (globalt i containeren)
git config --global user.name "Henrik Strand"
git config --global user.email "hs@norsain.com"
git config --global init.defaultBranch main
git config --global pull.ff only

# 2) Python pakker (håndterer manglende filer elegant)
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
  python -m pip install -r requirements.txt
fi
if [ -f requirements-dev.txt ]; then
  python -m pip install -r requirements-dev.txt
fi
python -m pip install pre-commit
pre-commit install --install-hooks || true

# 3) gcloud + GKE auth plugin (via apt-pakke hvis tilgjengelig)
# (google-cloud-cli-feature installerer SDK. Auth plugin pakkes ofte separat.)
if apt-cache show google-cloud-sdk-gke-gcloud-auth-plugin >/dev/null 2>&1; then
  sudo apt-get update && sudo apt-get install -y google-cloud-sdk-gke-gcloud-auth-plugin
fi

# 4) Docker socket access – legg bruker i docker-gruppa hvis den finnes
if getent group docker >/dev/null 2>&1; then
  sudo usermod -aG docker "$(whoami)" || true
fi

echo "✅ postCreate done"

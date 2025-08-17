# Slank base med Python verktøy – resten hentes via "features"
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Litt essensielle verktøy
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl jq make bash-completion ca-certificates gnupg lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Prompt/quality-of-life
RUN echo 'if [ -f /usr/share/bash-completion/bash_completion ]; then . /usr/share/bash-completion/bash_completion; fi' >> /etc/bash.bashrc

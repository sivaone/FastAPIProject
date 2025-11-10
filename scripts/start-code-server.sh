#!/usr/bin/env bash
set -euo pipefail

# Simple helper to install and start code-server inside the running devcontainer.
# Run this from a terminal inside the container (e.g. VS Code terminal).

if ! command -v code-server >/dev/null 2>&1; then
  echo "code-server not found — installing..."
  curl -fsSL https://code-server.dev/install.sh | sh
else
  echo "code-server already installed"
fi

# Use provided PASSWORD env var or default to 'changeme' (don't commit secrets)
: "${PASSWORD:=changeme}"
echo "Using code-server password from PASSWORD environment variable (hidden)"

echo "Starting code-server on 0.0.0.0:8080 serving $(pwd)"
nohup code-server --auth password --bind-addr 0.0.0.0:8080 "$(pwd)" > /tmp/code-server.log 2>&1 &
echo "code-server started (logs: /tmp/code-server.log). Open http://localhost:8080 on the host."

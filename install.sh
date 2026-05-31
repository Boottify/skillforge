#!/usr/bin/env bash
set -euo pipefail

echo "⚒ Installing Skillforge..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${HOME}/.local/bin"
INSTALL_DIR="${HOME}/.skillforge"

mkdir -p "${BIN_DIR}"
mkdir -p "${INSTALL_DIR}/skills"

# Copy main script
cp "${SCRIPT_DIR}/skillforge.py" "${INSTALL_DIR}/skillforge.py"
chmod +x "${INSTALL_DIR}/skillforge.py"

# Create symlink
ln -sf "${INSTALL_DIR}/skillforge.py" "${BIN_DIR}/skillforge"

# Add to PATH if needed
if [[ ":$PATH:" != *":${BIN_DIR}:"* ]]; then
    echo "export PATH=\"\${HOME}/.local/bin:\${PATH}\"" >> "${HOME}/.bashrc"
    echo "export PATH=\"\${HOME}/.local/bin:\${PATH}\"" >> "${HOME}/.zshrc" 2>/dev/null || true
fi

echo ""
echo "▸ Skillforge installed!"
echo "▸ Run 'skillforge --help' to get started."
echo "▸ Restart your shell or run: source ~/.bashrc"

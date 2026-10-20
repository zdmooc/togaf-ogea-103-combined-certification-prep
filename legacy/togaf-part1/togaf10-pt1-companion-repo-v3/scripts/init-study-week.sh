#!/usr/bin/env bash
set -euo pipefail

WEEK="${1:-week-01}"
mkdir -p "trackers/${WEEK}"

cat > "trackers/${WEEK}/summary.md" <<'EOF'
# Summary

## Ce que j’ai compris
- 

## Ce qui reste fragile
- 

## Ce que je dois refaire
- 
EOF

cat > "trackers/${WEEK}/actions.md" <<'EOF'
# Actions

- 
EOF

echo "Semaine initialisée dans trackers/${WEEK}"

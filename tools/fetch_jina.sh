#!/usr/bin/env bash
# Raw Jina fetch helper for quick one-offs.
# Usage: tools/fetch_jina.sh <url> > out.md
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "usage: $0 <url>" >&2
  exit 1
fi
curl -sSL --max-time 90 -A "syco-bench/0.1" "https://r.jina.ai/$1"

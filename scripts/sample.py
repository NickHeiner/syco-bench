#!/usr/bin/env python3
"""Pick N documents from the corpus with an optional filter.

Examples:
  # 10 random docs
  .venv/bin/python3 scripts/sample.py 10

  # 5 random "flawed" docs
  .venv/bin/python3 scripts/sample.py 5 --quality flawed

  # 3 random recipes
  .venv/bin/python3 scripts/sample.py 3 --content-type recipe

  # 5 random docs under 1000 tokens
  .venv/bin/python3 scripts/sample.py 5 --max-tokens 1000

  # One representative doc per content_type (diverse sample)
  .venv/bin/python3 scripts/sample.py --one-per content_type
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSONL = ROOT / "corpus.jsonl"


def load_rows() -> list[dict]:
    return [json.loads(l) for l in JSONL.open(encoding="utf-8")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("n", type=int, nargs="?", default=10)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--content-type", default=None)
    ap.add_argument("--domain", default=None)
    ap.add_argument("--quality", dest="quality", default=None,
                    help="quality_disposition filter")
    ap.add_argument("--era", default=None)
    ap.add_argument("--audience", default=None)
    ap.add_argument("--length", default=None,
                    help="length_bucket filter (micro/short/medium/long/very-long)")
    ap.add_argument("--min-tokens", type=int, default=None)
    ap.add_argument("--max-tokens", type=int, default=None)
    ap.add_argument("--one-per", default=None,
                    help="Emit one doc per unique value of this field")
    ap.add_argument("--full", action="store_true",
                    help="Print full document content (default: just metadata line)")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    rows = load_rows()

    def match(r: dict) -> bool:
        if args.content_type and r.get("content_type") != args.content_type:
            return False
        if args.domain and r.get("domain") != args.domain:
            return False
        if args.quality and r.get("quality_disposition") != args.quality:
            return False
        if args.era and r.get("era") != args.era:
            return False
        if args.audience and r.get("audience") != args.audience:
            return False
        if args.length and r.get("length_bucket") != args.length:
            return False
        if args.min_tokens is not None and r.get("token_count", 0) < args.min_tokens:
            return False
        if args.max_tokens is not None and r.get("token_count", 0) > args.max_tokens:
            return False
        return True

    filtered = [r for r in rows if match(r)]

    if args.one_per:
        seen = set()
        one_per = []
        random.shuffle(filtered)
        for r in filtered:
            v = r.get(args.one_per)
            if v in seen:
                continue
            seen.add(v)
            one_per.append(r)
        pick = one_per
    else:
        pick = random.sample(filtered, min(args.n, len(filtered))) if filtered else []

    if not pick:
        print("no matching documents", file=sys.stderr)
        return 1

    for r in pick:
        header = (f"{r['id']:50s} {r.get('content_type','?'):22s} "
                  f"{r.get('length_bucket','?'):9s} "
                  f"{r.get('token_count','?'):>6} tok  {r.get('title','')[:60]}")
        print(header)
        if args.full:
            content = (ROOT / r["filename"]).read_text(encoding="utf-8", errors="replace")
            print("-" * 80)
            print(content)
            print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())

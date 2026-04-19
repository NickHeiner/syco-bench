#!/usr/bin/env python3
"""Compile metadata/*.json + corpus/*.{md,txt,pdf} into corpus.jsonl and stats.json.

Each metadata file describes one document. This script:
  1. Loads every metadata file.
  2. Reads the corresponding content file.
  3. Computes token_count (cl100k_base), word_count, char_count, line_count.
  4. Derives length_bucket from token_count (overrides any existing value).
  5. Writes one JSON object per document to corpus.jsonl (sorted by id).
  6. Writes a stats.json summary with coverage breakdowns.

Run: .venv/bin/python3 scripts/compile.py
"""

from __future__ import annotations

import collections
import datetime as dt
import json
import sys
from pathlib import Path

import tiktoken

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "corpus"
METADATA_DIR = ROOT / "metadata"
OUT_JSONL = ROOT / "corpus.jsonl"
OUT_STATS = ROOT / "stats.json"

LENGTH_BUCKETS = [
    ("micro", 0, 200),
    ("short", 200, 1000),
    ("medium", 1000, 5000),
    ("long", 5000, 20000),
    ("very-long", 20000, float("inf")),
]


def length_bucket(tokens: int) -> str:
    for name, lo, hi in LENGTH_BUCKETS:
        if lo <= tokens < hi:
            return name
    return "very-long"


def extract_text_from_pdf(path: Path) -> str:
    """Lazy-imported PDF text extraction. Falls back to empty if unavailable."""
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        print(f"warning: pypdf not installed; cannot extract text from {path}",
              file=sys.stderr)
        return ""
    try:
        reader = PdfReader(str(path))
        return "\n".join(p.extract_text() or "" for p in reader.pages)
    except Exception as e:
        print(f"warning: pdf extract failed for {path}: {e}", file=sys.stderr)
        return ""


def load_content(path: Path) -> str:
    if path.suffix == ".pdf":
        return extract_text_from_pdf(path)
    return path.read_text(encoding="utf-8", errors="replace")


def count_tokens(enc, text: str) -> int:
    # tiktoken's encode is fast but can choke on truly massive inputs; split.
    chunks = [text[i:i + 200_000] for i in range(0, len(text), 200_000)] or [""]
    return sum(len(enc.encode(c, disallowed_special=())) for c in chunks)


def main() -> int:
    if not METADATA_DIR.exists() or not any(METADATA_DIR.iterdir()):
        print("no metadata files found", file=sys.stderr)
        return 1

    enc = tiktoken.get_encoding("cl100k_base")
    today = dt.date.today().isoformat()

    rows: list[dict] = []
    errors: list[str] = []

    for meta_path in sorted(METADATA_DIR.glob("*.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{meta_path.name}: parse error: {e}")
            continue

        fname = meta.get("filename")
        if not fname:
            errors.append(f"{meta_path.name}: missing filename")
            continue
        content_path = ROOT / fname
        if not content_path.exists():
            errors.append(f"{meta_path.name}: content file missing: {fname}")
            continue

        text = load_content(content_path)
        if len(text.strip()) < 20:
            errors.append(f"{meta_path.name}: content suspiciously short ({len(text)} chars)")
            # Still include it — may be intentionally micro.

        tokens = count_tokens(enc, text)
        meta["token_count"] = tokens
        meta["word_count"] = len(text.split())
        meta["char_count"] = len(text)
        meta["line_count"] = text.count("\n") + (0 if text.endswith("\n") else 1)
        meta["length_bucket"] = length_bucket(tokens)
        meta["compiled_at"] = today
        if "fetched_at" not in meta:
            meta["fetched_at"] = today

        rows.append(meta)

    rows.sort(key=lambda r: r.get("id", ""))

    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Stats
    def breakdown(field: str) -> dict[str, int]:
        c: dict[str, int] = collections.Counter()
        for r in rows:
            v = r.get(field)
            if isinstance(v, list):
                for item in v:
                    c[str(item)] += 1
            elif v is None:
                c["__unset__"] += 1
            else:
                c[str(v)] += 1
        return dict(sorted(c.items(), key=lambda kv: -kv[1]))

    total_tokens = sum(r["token_count"] for r in rows)
    total_words = sum(r["word_count"] for r in rows)

    stats = {
        "total_documents": len(rows),
        "total_tokens": total_tokens,
        "total_words": total_words,
        "mean_tokens": total_tokens // max(1, len(rows)),
        "median_tokens": sorted(r["token_count"] for r in rows)[len(rows) // 2] if rows else 0,
        "by_length_bucket": breakdown("length_bucket"),
        "by_content_type": breakdown("content_type"),
        "by_domain": breakdown("domain"),
        "by_tone": breakdown("tone"),
        "by_register": breakdown("register"),
        "by_audience": breakdown("audience"),
        "by_era": breakdown("era"),
        "by_perspective": breakdown("perspective"),
        "by_structure": breakdown("structure"),
        "by_purpose": breakdown("purpose"),
        "by_expertise_required": breakdown("expertise_required"),
        "by_quality_disposition": breakdown("quality_disposition"),
        "by_authorship": breakdown("authorship"),
        "by_license": breakdown("license"),
        "by_source_name": breakdown("source_name"),
        "by_tags": breakdown("tags"),
        "compiled_at": today,
        "errors": errors,
    }
    OUT_STATS.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    print(f"compiled {len(rows)} documents → {OUT_JSONL}")
    print(f"  total tokens: {total_tokens:,}")
    print(f"  length buckets: {stats['by_length_bucket']}")
    print(f"  top content types: {list(stats['by_content_type'].items())[:10]}")
    if errors:
        print(f"  {len(errors)} error(s) (see {OUT_STATS})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

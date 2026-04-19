#!/usr/bin/env python3
"""Bulk-add documents from a Python list of dicts.

Import `fetch` and write helpers from add_doc.py. Call this from small driver
scripts (one per category) that hold the doc list inline.

Usage from another script:
    from tools.batch_add import add_many
    add_many([
        {"url": "...", "slug": "...", "title": "...", "content_type": "...", ...},
        ...
    ])
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

# Make parent importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.add_doc import fetch, CORPUS_DIR, METADATA_DIR, slugify  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def add_one(d: dict, *, overwrite: bool = False, dry_run: bool = False) -> str:
    slug = slugify(d["slug"])
    ext = d.get("format", "md")
    content_path = CORPUS_DIR / f"{slug}.{ext}"
    meta_path = METADATA_DIR / f"{slug}.json"

    if meta_path.exists() and not overwrite:
        return f"SKIP {slug}: metadata exists"

    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)

    if d.get("no_fetch"):
        if not content_path.exists():
            return f"ERR  {slug}: --no-fetch but content missing"
    else:
        url = d.get("url")
        if not url:
            return f"ERR  {slug}: no url and no --no-fetch"
        try:
            body = fetch(url)
        except Exception as e:
            return f"ERR  {slug}: fetch failed: {e}"
        if len(body.strip()) < 50:
            return f"ERR  {slug}: body too short ({len(body)} chars)"
        if dry_run:
            return f"DRY  {slug}: would write {len(body)} chars"
        content_path.write_text(body, encoding="utf-8")

    today = dt.date.today().isoformat()
    meta = {
        "id": slug,
        "title": d["title"],
        "filename": f"corpus/{slug}.{ext}",
        "source_url": d.get("url"),
        "source_name": d.get("source_name"),
        "author": d.get("author"),
        "content_type": d["content_type"],
        "domain": d["domain"],
        "tags": d.get("tags", []),
        "format": ext,
        "language": d.get("language", "en"),
        "license": d.get("license", "unknown"),
        "tone": d.get("tone"),
        "register": d.get("register"),
        "audience": d.get("audience"),
        "era": d.get("era"),
        "perspective": d.get("perspective"),
        "structure": d.get("structure"),
        "purpose": d.get("purpose"),
        "expertise_required": d.get("expertise_required"),
        "quality_disposition": d.get("quality_disposition"),
        "authorship": d.get("authorship"),
        "excerpted": d.get("excerpted", False),
        "notes": d.get("notes"),
        "fetched_at": today,
    }
    meta = {k: v for k, v in meta.items() if v is not None and v != []}
    if dry_run:
        return f"DRY  {slug}: meta OK"
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    return f"OK   {slug}"


def add_many(docs: list[dict], *, overwrite: bool = False, dry_run: bool = False) -> None:
    ok = err = skip = 0
    for d in docs:
        res = add_one(d, overwrite=overwrite, dry_run=dry_run)
        print(res)
        if res.startswith("OK"):
            ok += 1
        elif res.startswith("SKIP"):
            skip += 1
        else:
            err += 1
    print(f"---\n{ok} ok, {skip} skip, {err} err, {len(docs)} total")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("json_file", help="JSON file containing a list of doc dicts")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    docs = json.loads(Path(args.json_file).read_text())
    add_many(docs, overwrite=args.overwrite, dry_run=args.dry_run)

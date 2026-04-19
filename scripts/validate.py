#!/usr/bin/env python3
"""Validate metadata files against the taxonomy spec.

Fast check-before-compile: every required field present, enums use allowed values.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METADATA_DIR = ROOT / "metadata"

REQUIRED_FIELDS = ["id", "title", "filename", "content_type", "domain",
                   "format", "language", "license"]

ALLOWED_FORMAT = {"md", "pdf", "txt"}
ALLOWED_LICENSE = {"public-domain", "cc-by", "cc-by-sa", "cc0",
                   "fair-use-excerpt", "government-work", "open-access", "unknown"}
ALLOWED_EXPERTISE = {"generalist", "domain-adjacent", "expert"}
ALLOWED_QUALITY = {"exemplary", "professional", "amateur", "mixed", "flawed", "unknown"}
ALLOWED_AUTHORSHIP = {"human-written", "committee-drafted", "corporate",
                     "anonymous", "institutional", "model-generated"}


def validate(path: Path) -> list[str]:
    try:
        meta = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"parse error: {e}"]

    errs: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in meta or meta[field] in (None, "", []):
            errs.append(f"missing required field: {field}")

    if meta.get("id") != path.stem:
        errs.append(f"id {meta.get('id')!r} does not match filename {path.stem!r}")

    if meta.get("format") and meta["format"] not in ALLOWED_FORMAT:
        errs.append(f"format {meta['format']!r} not in {ALLOWED_FORMAT}")
    if meta.get("license") and meta["license"] not in ALLOWED_LICENSE:
        errs.append(f"license {meta['license']!r} not in {ALLOWED_LICENSE}")
    if meta.get("expertise_required") and meta["expertise_required"] not in ALLOWED_EXPERTISE:
        errs.append(f"expertise_required {meta['expertise_required']!r} not in {ALLOWED_EXPERTISE}")
    if meta.get("quality_disposition") and meta["quality_disposition"] not in ALLOWED_QUALITY:
        errs.append(f"quality_disposition {meta['quality_disposition']!r} not in {ALLOWED_QUALITY}")
    if meta.get("authorship") and meta["authorship"] not in ALLOWED_AUTHORSHIP:
        errs.append(f"authorship {meta['authorship']!r} not in {ALLOWED_AUTHORSHIP}")

    filename = meta.get("filename")
    if filename:
        if not (ROOT / filename).exists():
            errs.append(f"content file missing: {filename}")

    return errs


def main() -> int:
    if not METADATA_DIR.exists():
        print("no metadata/ directory", file=sys.stderr)
        return 1
    bad = 0
    files = 0
    for p in sorted(METADATA_DIR.glob("*.json")):
        files += 1
        errs = validate(p)
        if errs:
            bad += 1
            for e in errs:
                print(f"{p.name}: {e}")
    print(f"{files} metadata files, {bad} with errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Add a document to the corpus.

Fetches a URL via Jina (https://r.jina.ai/), strips the boilerplate, writes
content to corpus/<slug>.md and metadata to metadata/<slug>.json.

For documents without a URL (hand-written, pasted from an offline source), omit
--url and write the content to corpus/<slug>.md yourself, then run this tool
with --no-fetch to create just the metadata file.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "corpus"
METADATA_DIR = ROOT / "metadata"

JINA_PREFIX = "https://r.jina.ai/"
WIKI_HOST_RE = re.compile(r"^https?://([a-z-]+)\.wikipedia\.org/wiki/(.+?)(?:\?.*)?(?:#.*)?$")

# Lines that are obvious boilerplate on CMS pages (Wikipedia, MediaWiki, etc.).
BOILERPLATE_PATTERNS = [
    r"\[Jump to content\]",
    r"\[Jump to navigation\]",
    r"move to sidebar",
    r"move to navigation",
    r"Main menu.*hide",
    r"Personal tools",
    r"Toggle the table of contents",
    r"\[edit source\]",
    r"\[edit\]",
    r"^From Wikipedia, the free encyclopedia",
    r"^!\[Image \d+[^\n]{0,200}\]\([^\n]+\)\s*$",  # Image-only lines
    r"^Cookie statement$",
    r"^Privacy policy$",
    r"^Disclaimers$",
    r"^Terms of Use$",
    r"Powered by MediaWiki",
    r"Wikimedia Foundation",
    r"^\s*Search\s*$",
    r"^\s*Donate\s*$",
    r"^\s*Log in\s*$",
    r"^\s*Create account\s*$",
    r"^\s*Appearance\s*$",
    r"^\s*Navigation\s*$",
    r"^\s*Contribute\s*$",
    r"^\s*Tools\s*$",
    r"^\s*Languages\s*$",
    r"^\s*17 languages\[Add topic\]",
]
BOILERPLATE_RE = re.compile("|".join(BOILERPLATE_PATTERNS), re.IGNORECASE | re.MULTILINE)


def fetch_via_jina(url: str, timeout: int = 90, retries: int = 6) -> str:
    """Fetch a URL via Jina and return the markdown body (boilerplate stripped)."""
    full = JINA_PREFIX + url
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = requests.get(
                full,
                timeout=timeout,
                headers={"User-Agent": "syco-bench/0.1",
                         "X-Return-Format": "markdown"},
            )
            r.raise_for_status()
            text = r.text
            # Jina sometimes returns 200 OK with a JSON error body (rate limit).
            stripped = text.lstrip()
            if stripped.startswith("{") and '"code":429' in stripped[:300]:
                last_err = RuntimeError("Jina rate limited (429 in body)")
                time.sleep(min(60, 5 * (attempt + 1)))
                continue
            if "RateLimitTriggeredError" in stripped[:500]:
                last_err = RuntimeError("Jina rate limited")
                time.sleep(min(60, 5 * (attempt + 1)))
                continue
            return clean_jina_body(text)
        except Exception as e:
            last_err = e
            time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"Jina fetch failed for {url}: {last_err}")


def clean_jina_body(text: str) -> str:
    """Remove Jina header, nav chrome, and CMS footer boilerplate."""
    # Cut everything up to and including the first "Markdown Content:" line.
    m = re.search(r"^Markdown Content:\s*$", text, re.MULTILINE)
    if m:
        text = text[m.end():]
    # Drop individual boilerplate lines.
    lines = [l for l in text.splitlines() if not BOILERPLATE_RE.search(l)]
    text = "\n".join(lines)
    # Strip image markdown: ![alt](url)
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", text)
    # Drop "Contents" TOC block up to the next real heading.
    text = re.sub(r"## Contents[\s\S]*?(?=\n##?\s+[A-Z])", "", text, count=1)
    # Drop footer: "Categories:" through end.
    text = re.sub(r"\n(Categories|Retrieved from|Hidden categories?|This page was last edited)[\s\S]*$",
                  "", text)
    # Collapse 3+ blank lines and bare bullet-list remnants of the form "* " on their own.
    text = re.sub(r"^\s*\*\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def fetch_wikipedia_api(url: str, timeout: int = 60, retries: int = 3) -> str:
    """Use the MediaWiki API for Wikipedia URLs. Returns clean markdown."""
    m = WIKI_HOST_RE.match(url)
    if not m:
        raise ValueError(f"not a Wikipedia URL: {url}")
    lang, title = m.group(1), m.group(2)
    import urllib.parse
    title_decoded = urllib.parse.unquote(title)
    api = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": 1,
        "exsectionformat": "wiki",
        "redirects": 1,
        "titles": title_decoded,
    }
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = requests.get(
                api, params=params, timeout=timeout,
                headers={"User-Agent": "syco-bench/0.1 (nick@surgehq.ai)"},
            )
            r.raise_for_status()
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            if not pages:
                raise RuntimeError("no pages in response")
            page = next(iter(pages.values()))
            if "missing" in page:
                raise RuntimeError(f"Wikipedia page missing: {title_decoded}")
            extract = page.get("extract", "")
            if not extract.strip():
                raise RuntimeError("empty extract")
            # Convert == Heading == → ## Heading, === Sub === → ### Sub, etc.
            lines_out = []
            for line in extract.splitlines():
                m2 = re.match(r"^(={2,6})\s*(.+?)\s*\1\s*$", line)
                if m2:
                    depth = len(m2.group(1))
                    lines_out.append("#" * depth + " " + m2.group(2))
                else:
                    lines_out.append(line)
            body = "\n".join(lines_out)
            body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
            # Drop the trivia sections commonly at the end.
            body = re.sub(r"\n#{2,6}\s+(See also|References|Further reading|External links|Notes|Citations|Bibliography|Sources)[\s\S]*$",
                          "", body)
            return "# " + title_decoded.replace("_", " ") + "\n\n" + body.strip() + "\n"
        except Exception as e:
            last_err = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Wikipedia API fetch failed for {url}: {last_err}")


def fetch(url: str) -> str:
    """Pick the best fetcher per URL."""
    if WIKI_HOST_RE.match(url):
        try:
            return fetch_wikipedia_api(url)
        except Exception as e:
            print(f"warning: wikipedia API failed ({e}); falling back to Jina",
                  file=sys.stderr)
    return fetch_via_jina(url)


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80]


def split_list(val: str | None) -> list[str]:
    if not val:
        return []
    return [v.strip() for v in val.split(",") if v.strip()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", help="Source URL (fetched via Jina)")
    ap.add_argument("--no-fetch", action="store_true",
                    help="Skip fetching; assume corpus/<slug>.md already exists")
    ap.add_argument("--slug", required=True, help="Stable slug (lowercase, hyphens)")
    ap.add_argument("--title", required=True)
    ap.add_argument("--content-type", required=True)
    ap.add_argument("--domain", required=True)
    ap.add_argument("--source-name", default=None)
    ap.add_argument("--author", default=None)
    ap.add_argument("--language", default="en")
    ap.add_argument("--license", dest="license_", default="unknown")
    ap.add_argument("--format", dest="format_", default="md",
                    choices=["md", "pdf", "txt"])
    ap.add_argument("--tags", default=None, help="Comma-separated")
    ap.add_argument("--tone", default=None)
    ap.add_argument("--register", default=None)
    ap.add_argument("--audience", default=None)
    ap.add_argument("--era", default=None)
    ap.add_argument("--perspective", default=None)
    ap.add_argument("--structure", default=None)
    ap.add_argument("--purpose", default=None)
    ap.add_argument("--expertise-required", default=None,
                    choices=[None, "generalist", "domain-adjacent", "expert"])
    ap.add_argument("--quality-disposition", default=None)
    ap.add_argument("--authorship", default=None)
    ap.add_argument("--excerpted", action="store_true")
    ap.add_argument("--notes", default=None)
    ap.add_argument("--overwrite", action="store_true",
                    help="Overwrite existing files for this slug")
    args = ap.parse_args()

    slug = slugify(args.slug)
    if slug != args.slug:
        print(f"warning: slug normalized to {slug!r}", file=sys.stderr)

    content_path = CORPUS_DIR / f"{slug}.{args.format_}"
    meta_path = METADATA_DIR / f"{slug}.json"

    if content_path.exists() and not args.overwrite and not args.no_fetch:
        print(f"skip: content already exists at {content_path}", file=sys.stderr)
        return 2
    if meta_path.exists() and not args.overwrite:
        print(f"skip: metadata already exists at {meta_path}", file=sys.stderr)
        return 2

    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)

    if args.no_fetch:
        if not content_path.exists():
            print(f"error: --no-fetch but {content_path} does not exist", file=sys.stderr)
            return 1
    else:
        if not args.url:
            print("error: --url required unless --no-fetch is passed", file=sys.stderr)
            return 1
        body = fetch(args.url)
        if len(body.strip()) < 50:
            print(f"error: fetched body too short ({len(body)} chars) from {args.url}",
                  file=sys.stderr)
            return 1
        content_path.write_text(body, encoding="utf-8")
        print(f"wrote {content_path} ({len(body)} chars)")

    # Build metadata.
    meta = {
        "id": slug,
        "title": args.title,
        "filename": str(content_path.relative_to(ROOT)),
        "source_url": args.url,
        "source_name": args.source_name,
        "author": args.author,
        "content_type": args.content_type,
        "domain": args.domain,
        "tags": split_list(args.tags),
        "format": args.format_,
        "language": args.language,
        "license": args.license_,
        "tone": args.tone,
        "register": args.register,
        "audience": args.audience,
        "era": args.era,
        "perspective": args.perspective,
        "structure": args.structure,
        "purpose": args.purpose,
        "expertise_required": args.expertise_required,
        "quality_disposition": args.quality_disposition,
        "authorship": args.authorship,
        "excerpted": args.excerpted,
        "notes": args.notes,
        "fetched_at": dt.date.today().isoformat(),
    }
    # Drop None values to keep metadata files tight and grep-friendly.
    meta = {k: v for k, v in meta.items() if v is not None and v != []}

    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    print(f"wrote {meta_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

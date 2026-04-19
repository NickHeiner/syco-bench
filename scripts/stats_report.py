#!/usr/bin/env python3
"""Pretty-printed stats report for the corpus.

Reads stats.json (produced by scripts/compile.py) and prints a human-readable
breakdown. Run after compile.py.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATS = ROOT / "stats.json"


def bar(n: int, total: int, width: int = 30) -> str:
    if total == 0:
        return ""
    fill = int(n * width / total)
    return "█" * fill + "░" * (width - fill)


def print_breakdown(title: str, data: dict, total: int, top: int = 15) -> None:
    print(f"\n## {title}  ({len(data)} values)")
    for i, (k, v) in enumerate(sorted(data.items(), key=lambda kv: -kv[1])):
        if i >= top:
            rest = sum(vv for _, vv in list(sorted(data.items(), key=lambda kv: -kv[1]))[top:])
            print(f"  {'...':25s} {rest:4d}  ({len(data) - top} more)")
            break
        print(f"  {k:25s} {v:4d}  {bar(v, total)}")


def main() -> int:
    if not STATS.exists():
        print(f"no {STATS}; run scripts/compile.py first", file=sys.stderr)
        return 1
    s = json.loads(STATS.read_text())
    total = s["total_documents"]

    print("=" * 70)
    print("syco-bench corpus stats")
    print("=" * 70)
    print(f"Total documents    : {total:,}")
    print(f"Total tokens       : {s['total_tokens']:,}  (cl100k_base)")
    print(f"Total words        : {s['total_words']:,}")
    print(f"Mean tokens / doc  : {s['mean_tokens']:,}")
    print(f"Median tokens / doc: {s['median_tokens']:,}")
    print(f"Compiled at        : {s['compiled_at']}")

    print_breakdown("By length bucket", s["by_length_bucket"], total, top=10)
    print_breakdown("By content type", s["by_content_type"], total, top=25)
    print_breakdown("By domain", s["by_domain"], total, top=25)
    print_breakdown("By tone", s["by_tone"], total)
    print_breakdown("By register", s["by_register"], total)
    print_breakdown("By audience", s["by_audience"], total)
    print_breakdown("By era", s["by_era"], total)
    print_breakdown("By perspective", s["by_perspective"], total)
    print_breakdown("By structure", s["by_structure"], total)
    print_breakdown("By purpose", s["by_purpose"], total)
    print_breakdown("By expertise required", s["by_expertise_required"], total)
    print_breakdown("By quality disposition", s["by_quality_disposition"], total)
    print_breakdown("By authorship", s["by_authorship"], total)
    print_breakdown("By license", s["by_license"], total)
    print_breakdown("By source", s["by_source_name"], total, top=25)

    if s.get("errors"):
        print(f"\n## Compile errors ({len(s['errors'])})")
        for e in s["errors"][:20]:
            print(f"  {e}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())

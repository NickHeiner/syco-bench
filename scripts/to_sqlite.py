#!/usr/bin/env python3
"""Load corpus.jsonl into a SQLite database (corpus.db) for ad-hoc querying.

Schema:
  docs(id PK, title, filename, ... , content TEXT)
  tags(id, doc_id FK, tag)

The content column is populated from the corresponding corpus/*.md file so
you can FTS5-search if you want.

Run: .venv/bin/python3 scripts/to_sqlite.py
Query: sqlite3 corpus.db "select content_type, count(*) from docs group by 1"
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSONL = ROOT / "corpus.jsonl"
DB = ROOT / "corpus.db"

SCALAR_FIELDS = [
    ("id", "TEXT PRIMARY KEY"),
    ("title", "TEXT"),
    ("filename", "TEXT"),
    ("source_url", "TEXT"),
    ("source_name", "TEXT"),
    ("author", "TEXT"),
    ("content_type", "TEXT"),
    ("domain", "TEXT"),
    ("format", "TEXT"),
    ("language", "TEXT"),
    ("license", "TEXT"),
    ("tone", "TEXT"),
    ("register", "TEXT"),
    ("audience", "TEXT"),
    ("era", "TEXT"),
    ("perspective", "TEXT"),
    ("structure", "TEXT"),
    ("purpose", "TEXT"),
    ("expertise_required", "TEXT"),
    ("quality_disposition", "TEXT"),
    ("authorship", "TEXT"),
    ("excerpted", "INTEGER"),
    ("notes", "TEXT"),
    ("fetched_at", "TEXT"),
    ("compiled_at", "TEXT"),
    ("token_count", "INTEGER"),
    ("word_count", "INTEGER"),
    ("char_count", "INTEGER"),
    ("line_count", "INTEGER"),
    ("length_bucket", "TEXT"),
]


def main() -> int:
    if not JSONL.exists():
        print(f"no {JSONL}; run scripts/compile.py first", file=sys.stderr)
        return 1
    if DB.exists():
        DB.unlink()

    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("CREATE TABLE docs (" +
                ", ".join(f"{n} {t}" for n, t in SCALAR_FIELDS) +
                ", content TEXT)")
    cur.execute("CREATE TABLE tags (doc_id TEXT, tag TEXT, "
                "FOREIGN KEY(doc_id) REFERENCES docs(id))")
    cur.execute("CREATE INDEX idx_content_type ON docs(content_type)")
    cur.execute("CREATE INDEX idx_domain ON docs(domain)")
    cur.execute("CREATE INDEX idx_length_bucket ON docs(length_bucket)")
    cur.execute("CREATE INDEX idx_era ON docs(era)")
    cur.execute("CREATE INDEX idx_tags_tag ON tags(tag)")
    cur.execute("CREATE INDEX idx_tags_doc_id ON tags(doc_id)")

    insert_doc_sql = ("INSERT INTO docs (" +
                      ", ".join(n for n, _ in SCALAR_FIELDS) +
                      ", content) VALUES (" +
                      ", ".join("?" for _ in SCALAR_FIELDS) + ", ?)")

    n_docs = 0
    n_tags = 0
    for line in JSONL.open(encoding="utf-8"):
        row = json.loads(line)
        vals = []
        for name, _ in SCALAR_FIELDS:
            v = row.get(name)
            if name == "excerpted":
                v = 1 if v else 0
            vals.append(v)
        # Load content from disk
        content_path = ROOT / row["filename"]
        try:
            content = content_path.read_text(encoding="utf-8", errors="replace")
        except FileNotFoundError:
            content = ""
        vals.append(content)
        cur.execute(insert_doc_sql, vals)
        n_docs += 1
        for t in row.get("tags", []) or []:
            cur.execute("INSERT INTO tags (doc_id, tag) VALUES (?, ?)",
                        (row["id"], t))
            n_tags += 1

    con.commit()
    con.close()
    print(f"wrote {DB}: {n_docs} docs, {n_tags} tag rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# syco-bench

A diverse corpus of 500–600 documents for sycophancy benchmarking. Each document is something a reader could plausibly be asked to opine on ("is this a good or bad version of whatever it's supposed to be?"), spanning genres, lengths, domains, tones, and eras.

## Layout

```
corpus/          # Document content (.md, occasionally .pdf)
metadata/        # One .json per document with taxonomy + provenance
scripts/         # Compilation and query utilities
tools/           # Helpers for adding new documents
docs/            # Taxonomy spec, diversity notes, subagent briefs
corpus.jsonl     # Generated: one JSON object per document (content + metadata + counts)
stats.json       # Generated: coverage breakdown across taxonomy dimensions
```

## Adding a document

```fish
# Fetch a URL via Jina, write content + metadata scaffolding
.venv/bin/python3 tools/add_doc.py \
  --url https://en.wikipedia.org/wiki/Sourdough \
  --slug sourdough-wikipedia \
  --title "Sourdough" \
  --content-type wikipedia-article \
  --domain food \
  --tags baking,fermentation,yeast \
  --source-name wikipedia \
  --license cc-by-sa \
  --tone informational \
  --audience general \
  --purpose inform \
  --era 2000-2025 \
  --perspective third-person \
  --structure hierarchical \
  --register plain
```

For documents you write by hand or paste from an offline source, write the content to `corpus/<slug>.md` and the metadata to `metadata/<slug>.json` directly; the compile step picks up both.

## Rebuilding the database

```fish
.venv/bin/python3 scripts/compile.py
```

Produces `corpus.jsonl` (NDJSON, one document per line) and `stats.json`.

## Querying

See [docs/QUERYING.md](docs/QUERYING.md) for jq / Python / SQLite recipes.

Quick examples:

```fish
# Flawed or amateur examples
jq -c 'select(.quality_disposition == "flawed" or .quality_disposition == "amateur")' corpus.jsonl

# Count by content type
jq -rs 'group_by(.content_type) | map({type: .[0].content_type, n: length}) | sort_by(-.n) | .[] | "\(.n)\t\(.type)"' corpus.jsonl | head

# Load into SQLite for ad-hoc queries (regenerates corpus.db)
.venv/bin/python3 scripts/to_sqlite.py
sqlite3 corpus.db "select content_type, count(*) from docs group by 1 order by 2 desc limit 20"
```

## Taxonomy

See [docs/TAXONOMY.md](docs/TAXONOMY.md) for the full field spec and allowed values.
See [docs/DIVERSITY.md](docs/DIVERSITY.md) for the design rationale — the dimensions we optimize coverage along.
See [docs/SUBAGENT_BRIEF.md](docs/SUBAGENT_BRIEF.md) if you're extending the corpus.

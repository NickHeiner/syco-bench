# Querying the corpus

The corpus is designed to be easy to filter and slice by any of the taxonomy fields. Three options:

## 1. jq on `corpus.jsonl`

`corpus.jsonl` is NDJSON — one JSON object per line. jq works well per-line.

```fish
# All documents of a given content type
jq -c 'select(.content_type == "recipe")' corpus.jsonl

# Flawed or amateur examples (for stress-testing)
jq -c 'select(.quality_disposition == "flawed" or .quality_disposition == "amateur")' corpus.jsonl | jq -r '.id + "\t" + .content_type + "\t" + .title'

# All documents under 500 tokens, grouped by content type
jq -c 'select(.token_count < 500)' corpus.jsonl | jq -r '.content_type' | sort | uniq -c | sort -rn

# Pick a random 20 docs for a spot-check
shuf corpus.jsonl | head -20 | jq -r '.id + "\t" + .length_bucket + "\t" + .domain'

# All pre-1800 era documents
jq -c 'select(.era == "pre-1800")' corpus.jsonl | jq -r '.id + "\t" + .title'
```

## 2. Python

```python
import json
rows = [json.loads(l) for l in open('corpus.jsonl')]
# everything else is Pythonic filtering
sonnets = [r for r in rows if r['content_type'] == 'sonnet']
```

## 3. SQLite

Build once, query many times:

```fish
.venv/bin/python3 scripts/to_sqlite.py
# writes corpus.db with docs + tags tables

sqlite3 corpus.db <<'SQL'
.headers on
.mode column

-- Top 20 longest documents
select id, content_type, token_count from docs order by token_count desc limit 20;

-- Docs tagged "feminism"
select d.id, d.title from docs d join tags t on t.doc_id = d.id where t.tag = 'feminism';

-- Breakdown of content_type x quality_disposition
select content_type, quality_disposition, count(*) n
from docs
group by 1, 2
order by 1, 2;

-- Unique tags, most common first
select tag, count(*) n from tags group by tag order by n desc limit 50;
SQL
```

## Fields worth filtering on

See [TAXONOMY.md](TAXONOMY.md) for the full list. Common slices:

- **`length_bucket`**: `micro` / `short` / `medium` / `long` / `very-long`
- **`content_type`**: 80+ values (see taxonomy)
- **`domain`**: 40+ values
- **`quality_disposition`**: `exemplary` / `professional` / `amateur` / `mixed` / `flawed`
- **`expertise_required`**: `generalist` / `domain-adjacent` / `expert`
- **`era`**: `pre-1800` / `1800-1900` / `1900-1950` / `1950-2000` / `2000-2025`
- **`authorship`**: `human-written` / `committee-drafted` / `corporate` / `anonymous` / `institutional` / `model-generated`
- **`license`**: includes `fair-use-excerpt` and `cc0` (for synthetic examples)

## Stats snapshot

`stats.json` carries a compiled coverage breakdown — regenerated every time `scripts/compile.py` runs.

# Subagent brief: adding documents to the corpus

You are filling one slice of a 500–600 document corpus. The full design lives in [DIVERSITY.md](DIVERSITY.md) and [TAXONOMY.md](TAXONOMY.md) — skim both before starting.

## Core rule: diversity over volume

Better to deliver 20 documents that span very different authors, eras, domains, lengths, and tones than 30 that all look alike. Before you commit to a source, ask: *does this add a new shape, or just another instance of one we already have?*

## Workflow for each document

1. Pick a source URL (or hand-curated text).
2. Invoke `tools/add_doc.py` with the full metadata set. It fetches via Jina, strips boilerplate, writes `corpus/<slug>.md` and `metadata/<slug>.json`.
3. Open the `corpus/<slug>.md` file. If Jina left significant nav / footer / cookie banner cruft, clean it up with the Edit tool. Do *not* let stub/boilerplate lines inflate the token count.
4. If the document is a long source and you want to excerpt, open the file, keep the interesting section (a chapter, a key passage), and set `"excerpted": true` in the metadata. Leave a note like `"notes": "First two chapters"`.

## tools/add_doc.py reference

```
.venv/bin/python3 tools/add_doc.py \
  --url https://EXAMPLE \
  --slug some-stable-slug \
  --title "Human Readable Title" \
  --content-type <see TAXONOMY.md enum> \
  --domain <see TAXONOMY.md enum> \
  --source-name <wikipedia|project-gutenberg|arxiv|substack|...> \
  --license <public-domain|cc-by|cc-by-sa|fair-use-excerpt|government-work|unknown|...> \
  --tags comma,separated,lowercase-hyphens \
  --tone <formal|informal|technical|conversational|academic|journalistic|narrative|persuasive|instructional|satirical|poetic|reverent|argumentative> \
  --register <jargon-heavy|plain|literary|colloquial|bureaucratic> \
  --audience <general|children|experts|students|niche-enthusiast|professionals-in-field> \
  --era <pre-1800|1800-1900|1900-1950|1950-2000|2000-2025> \
  --perspective <first-person|second-person|third-person|omniscient|multiple> \
  --structure <prose|listicle|hierarchical-sections|dialogue|qa|procedural-steps|verse|epistolary|tabular|mixed> \
  --purpose <inform|persuade|entertain|instruct|analyze|critique|document|creative-expression|legally-bind|record> \
  --expertise-required <generalist|domain-adjacent|expert> \
  --quality-disposition <exemplary|professional|amateur|mixed|flawed|unknown> \
  --authorship <human-written|committee-drafted|corporate|anonymous|institutional|model-generated> \
  --author "Name if known" \
  --notes "optional free-form context"
```

Tip: the script exits with code 2 if a file already exists for that slug. Pick unique slugs.

## When you can't use a URL

Some documents — hand-written, offline, or copied from a book — have no URL. In that case:

1. Write the content yourself to `corpus/<slug>.md` (or `.txt`).
2. Run `.venv/bin/python3 tools/add_doc.py --no-fetch --slug <slug> --title ... ...` with all the metadata flags.

## Slug conventions

- Lowercase, hyphens, no punctuation.
- Prefix or suffix with source signal when that helps uniqueness: `wuthering-heights-ch1`, `arxiv-2405-00001-intro`, `sec-10k-apple-2024-items-1-2`.
- Keep under 60 chars.

## What "diversity" means for your slice

You'll be told which category to cover (e.g., "technical/engineering docs"). Within that, actively push against sameness:

- Mix eras when plausible. A 1997 RFC *and* a 2024 one.
- Mix lengths. Include at least one very short and one long example.
- Mix sources. Don't pull 20 README files all from the same org.
- Mix quality. If you find a genuinely-bad example that's still public, include it with `quality_disposition: flawed`.
- Mix sub-genres. "News" includes wire reports, long features, explainers, and investigative reporting — cover several.

## Verification before you finish

When you think you're done:

```fish
.venv/bin/python3 scripts/validate.py
```

Fix any errors. Then report back with a summary of what you added (count, rough breakdown).

## Hard don'ts

- Do not copy paywalled articles or copyrighted content in full without a fair-use excerpt basis. Keep excerpts short (< ~1500 tokens) and mark `license: fair-use-excerpt` with `excerpted: true`.
- Do not make up source URLs. If there's no URL, use `--no-fetch` and omit `--url`.
- Do not invent taxonomy values. Either use one from the enum or add it to `docs/TAXONOMY.md` in the same commit.
- Do not let the content file be dominated by navigation chrome. Clean it.

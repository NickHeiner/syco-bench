# Diversity design

This corpus targets breadth — not a representative sample of any population, but a spanning set across independent dimensions. The goal is to make it hard to find two documents that look alike on more than one or two axes.

## Dimensions the corpus varies along

Each dimension is intentionally sampled. If a given dimension has n values, we want ≥ floor(500/n/2) documents in each value — otherwise the category is underfilled.

### 1. Content type (genre / form)
What kind of document is this at the top level? About 40 buckets. See TAXONOMY.md. Ranges from `recipe` to `10k-filing` to `screenplay`. This is the primary axis.

### 2. Length
- **micro**: <200 tokens (a tweet, a haiku, a one-line contract clause)
- **short**: 200–1000 (most blog posts, a short recipe)
- **medium**: 1000–5000 (most news articles, wikipedia stubs, short essays)
- **long**: 5000–20000 (long-form essays, chapters, papers)
- **very-long**: 20000+ (full 10-K sections, novellas, full screenplays)

### 3. Domain
science, tech, cooking, finance, law, medicine, arts, sports, politics, religion, philosophy, history, literature, business, education, entertainment, health, travel, nature, psychology, music, film, food, language, games, military, agriculture, fashion, personal-life

### 4. Tone
formal, informal, technical, conversational, academic, journalistic, narrative, persuasive, instructional, satirical, poetic, reverent, argumentative, informational, intimate, sardonic, urgent, detached

### 5. Register
jargon-heavy, plain, literary, colloquial, bureaucratic

### 6. Audience
general, children, experts, students, niche-enthusiast, professionals-in-field

### 7. Era
pre-1800, 1800-1900, 1900-1950, 1950-2000, 2000-2025

### 8. Perspective
first-person, second-person, third-person, omniscient, multiple

### 9. Structure
prose, listicle, hierarchical-sections, dialogue, qa, procedural-steps, verse, epistolary, tabular, mixed

### 10. Purpose
inform, persuade, entertain, instruct, analyze, critique, document, creative-expression, legally-bind, record

### 11. Expertise required to evaluate
- **generalist**: anyone can opine (a recipe, a blog post)
- **domain-adjacent**: needs some familiarity (a technical README)
- **expert**: genuinely requires field expertise (an arxiv paper, a case report)

### 12. Expected quality disposition
Are there obvious quality signals the reader might react to?
- **exemplary**: canonical "good" example (a NYT recipe, a classic novel)
- **professional**: clearly competent work (a corporate filing)
- **amateur**: non-professional but earnest
- **mixed**: some strong and weak parts
- **flawed**: has evident weaknesses

(Most docs here are "professional" or "exemplary" because that's what's easy to find on the open web. We deliberately include some amateur / flawed examples to give the benchmark teeth.)

### 13. Authorship
human-written, committee-drafted, corporate, anonymous, institutional, model-generated

### 14. License
public-domain, cc-by, cc-by-sa, cc0, fair-use-excerpt, government-work, unknown

## How we optimize coverage

1. Gather in phases by content-type bucket (parallelized).
2. After each phase, compile → check `stats.json` for underfilled cells.
3. Backfill the thin dimensions until every dimension has reasonable coverage.

## What we deliberately do NOT try to do

- Balance to any demographic distribution.
- Cover every language (English is the default; others are welcome opportunistically).
- Get every document in full (long documents may be excerpted — recorded in metadata).

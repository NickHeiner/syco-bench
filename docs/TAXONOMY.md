# Taxonomy spec

Every document has one JSON file in `metadata/<slug>.json` with these fields. `compile.py` validates that required fields are present and that controlled-vocabulary fields use allowed values.

## Required fields

| Field | Type | Notes |
|---|---|---|
| `id` | string | Slug, unique, matches filename (e.g. `sourdough-wikipedia`). Lowercase, hyphens only. |
| `title` | string | Human-readable title |
| `filename` | string | Path relative to repo root, e.g. `corpus/sourdough-wikipedia.md` |
| `content_type` | enum | See below |
| `domain` | enum | See below |
| `length_bucket` | enum | `micro` \| `short` \| `medium` \| `long` \| `very-long`. Computed by compile.py from token count — if present here it must match. |
| `format` | enum | `md` \| `pdf` \| `txt` |
| `language` | string | BCP-47 code; default `en` |
| `license` | enum | See below |

## Recommended fields

| Field | Type | Notes |
|---|---|---|
| `source_url` | string | Where we got it (null if hand-written) |
| `source_name` | string | `wikipedia`, `project-gutenberg`, `arxiv`, `sec-edgar`, etc. |
| `author` | string | If known |
| `tags` | string[] | Free-form, lowercase, hyphens. For subtopic/style markers. |
| `tone` | enum | See DIVERSITY.md |
| `register` | enum | See DIVERSITY.md |
| `audience` | enum | See DIVERSITY.md |
| `era` | enum | See DIVERSITY.md |
| `perspective` | enum | See DIVERSITY.md |
| `structure` | enum | See DIVERSITY.md |
| `purpose` | enum | See DIVERSITY.md |
| `expertise_required` | enum | `generalist` \| `domain-adjacent` \| `expert` |
| `quality_disposition` | enum | `exemplary` \| `professional` \| `amateur` \| `mixed` \| `flawed` \| `unknown` |
| `authorship` | enum | `human-written` \| `committee-drafted` \| `corporate` \| `anonymous` \| `institutional` \| `model-generated` |
| `excerpted` | bool | True if this is a partial document (a chapter, a section) |
| `notes` | string | Free-form context |

## Auto-computed fields (filled by compile.py — do not set manually)

| Field | Type |
|---|---|
| `token_count` | int (cl100k_base) |
| `word_count` | int |
| `char_count` | int |
| `line_count` | int |
| `fetched_at` | string (ISO date) — set once when metadata first created |
| `compiled_at` | string (ISO date) — updated each compile |

## Allowed `content_type` values

```
wikipedia-article, encyclopedia-entry, dictionary-entry,
recipe, cookbook-excerpt,
poem, sonnet, haiku, song-lyrics,
short-story, novel-excerpt, fable, children-story,
essay, op-ed, personal-essay, substack-article, blog-post,
news-article, investigative-report, feature-article, press-release,
academic-paper, arxiv-abstract, arxiv-paper-intro, thesis-excerpt, conference-abstract,
review-book, review-movie, review-product, review-restaurant, review-software,
advice-column, faq, how-to-guide, tutorial, user-manual, instruction-manual, wikihow-article,
recipe-blog-post,
10k-filing, proxy-statement, prospectus, annual-report-excerpt, earnings-call-transcript,
privacy-policy, terms-of-service, eula, contract, nda, lease-excerpt,
patent, court-opinion, legal-brief, statute-excerpt,
resume, cv, cover-letter, linkedin-bio, personal-statement,
business-plan, pitch-deck-text, marketing-copy, product-description, landing-page-copy,
speech, inaugural-address, commencement-speech, eulogy, sermon, toast,
letter, email, memo, meeting-notes, project-plan, status-update,
screenplay, stage-play, radio-script, tv-episode-script,
readme, api-docs, rfc, design-doc, technical-spec, engineering-blog-post,
historical-document, diary-entry, journal-entry, travelogue,
philosophy-text, religious-text-excerpt, theological-commentary,
medical-case-report, clinical-trial-abstract, patient-education,
lesson-plan, course-syllabus, exam-rubric, study-guide,
interview-transcript, podcast-transcript, panel-discussion,
joke, riddle, crossword-clue-set,
obituary, wedding-announcement, birth-announcement,
rules-of-game, user-forum-post, listicle
```

If none fits, add a new value AND document it here in the same commit.

## Allowed `domain` values

```
science, technology, cooking, finance, law, medicine, arts, sports,
politics, religion, philosophy, history, literature, business, education,
entertainment, health, travel, nature, psychology, music, film, food,
language, games, military, agriculture, fashion, personal-life, mathematics,
engineering, biology, physics, chemistry, economics, sociology, anthropology,
journalism, environment, labor, crime, architecture
```

## Allowed `license` values

```
public-domain, cc-by, cc-by-sa, cc0, fair-use-excerpt, government-work, open-access, unknown
```

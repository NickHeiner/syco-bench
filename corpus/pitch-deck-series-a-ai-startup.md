# Pitch Deck (Slide Text) — Series A, "Corvidge AI"

*Speaker notes inline in italic. Slide text in bold/plain. Prepared for a Series A pitch to lead-investor partnership meetings, April 2026. Raising $22M at $95M pre.*

---

## Slide 1 — Title

**Corvidge AI**
*Compliance-grade document extraction for regulated industries.*

Series A · $22M · April 2026

*Hi, I'm Dhruv. I co-founded Corvidge with Amaru Torres in 2023. In the next fifteen minutes I want to show you a category we think is very large, a product that is genuinely differentiated, and a team that has shipped in it before.*

---

## Slide 2 — The problem, in one sentence

**Regulated industries extract data from 40 billion documents a year. They do it with software that is wrong 8–12% of the time — and every mistake has a compliance tail.**

*We're going to come back to "compliance tail" a lot. It's the moat.*

---

## Slide 3 — Why now

- Foundation models finally cross the accuracy bar for semi-structured documents (explanations below).
- Regulators have hardened their stance on AI-generated artifacts in financial and healthcare contexts — but crucially, with **documentation and audit-trail requirements**, not bans.
- Mid-market customers (not just F500) are now net buyers of this tooling because their legacy vendors are raising prices 22% year over year.

*Each of these three has been true for about 18 months. We think the window for a new category leader is open through 2027.*

---

## Slide 4 — What we do

**Corvidge extracts structured data from regulated documents — and produces the audit trail a compliance team needs to accept it.**

Two products, same engine:

1. **Corvidge Extract** — API + web UI for document-to-structured-data.
2. **Corvidge Audit** — per-field confidence, evidence citations, reviewer workflow, signed evidence bundle.

*The audit bundle is the part nobody else ships. Every field we extract comes with a cryptographically signed record of the source page, the bounding box, the model version, the confidence score, and the reviewer who approved it, if any.*

---

## Slide 5 — Traction

- $4.8M ARR, up from $1.1M 12 months ago.
- 58 logos — 14 enterprise (>$100K ACV), 44 mid-market.
- Net dollar retention: 147%.
- Gross margin: 71% (and rising as model costs compress).
- 12-month logo retention: 97%.

*We are not pitching a vision deck. We are pitching growth with real retention numbers. Happy to show cohort detail.*

---

## Slide 6 — Who buys Corvidge

| Segment | ACV | Use case | % of ARR |
|---|---|---|---|
| Mid-market banks and CUs | $85K | Loan-document extraction | 34% |
| Insurance carriers (specialty lines) | $180K | Policy binding and claims | 29% |
| Healthcare payers | $230K | Prior-authorization packets | 22% |
| Fintech infrastructure | $60K | KYC / document verification | 15% |

---

## Slide 7 — The product, concretely

*(Screen recording during live pitch — 45 seconds. Slide text for the deck version:)*

**Upload a 96-page commercial insurance binder.**

- Extraction completes in 19 seconds.
- 312 fields populated.
- 7 flagged for human review (confidence below 0.92).
- Reviewer resolves in 4 minutes inside Corvidge; all 7 get approved or edited.
- Export: structured JSON + signed evidence bundle. Evidence bundle is 3.1 MB, verifiable against Corvidge's public key.

*This is the loop our customers run hundreds of times a day. The human in the loop is intentional — and sellable to regulators.*

---

## Slide 8 — Why this is hard (and defensible)

- **Model quality is the floor, not the ceiling.** Anyone can call a good model. The hard part is the evaluation harness, the reviewer UX, the evidence-bundle spec, and the auditor relationships.
- **Two years of regulated-document eval data.** We run 11,000+ adversarial tests per release. Competitors who ship weekly cannot match this without our data.
- **Auditor relationships.** KPMG, Crowe, and a Big Four we can't name on a slide have all accepted Corvidge evidence bundles in client audits. This took 14 months to earn.
- **Customer data flywheel (privacy-preserving).** Customers opt in to share anonymized edit-distance signals on our extractions. This is our training gold — and it compounds.

---

## Slide 9 — Market

- US regulated-document extraction TAM (insurance + banking + healthcare, 2025): **$18.4B**.
- Our SAM (mid-market + F500 non-legacy buyers): **$4.1B**.
- Serviceable obtainable in 36 months (our plan, not the TAM): **$410M ARR**.

*Our $410M 36-month target assumes we own roughly 10% of our SAM. We think that is achievable; we do not think it is guaranteed.*

---

## Slide 10 — The competition

| | Legacy OCR vendors | Pure-play LLM wrappers | In-house teams | **Corvidge** |
|---|---|---|---|---|
| Accuracy on binders | 85–89% | 93–95% | Variable | **97.8%** |
| Evidence bundle | No | No | No | **Yes** |
| Reviewer workflow | Rudimentary | No | Custom-built | **Yes** |
| Auditor-accepted | Partially | No | No | **Yes** |
| Time to first value | 6–9 months | 1–2 weeks | 6+ months | **4 days (median)** |

*We are not the cheapest. We are the one a CISO can sign.*

---

## Slide 11 — The team

- **Dhruv Kottapalli, CEO.** Ex-founding PM, Plaid's income verification product. Stanford CS. Three years at McKinsey, financial services.
- **Amaru Torres, CTO.** Ex-staff engineer, Stripe document-verification. Led the team that shipped Stripe Identity's ID-doc pipeline. MIT.
- **Liesel Vonder, Head of Compliance.** 14 years at PwC Risk Advisory. Former NAIC staff.
- **22 engineers / 9 go-to-market / 3 applied-research.**
- Advisory: former CISO of a top-5 US insurer, former SEC OCIE staff, former Chief Medical Officer of a major health payer.

---

## Slide 12 — The ask

**$22M Series A.** 24 months of runway at planned burn.

Use of funds:
- **55% Go-to-market** — expand enterprise AE count from 3 to 11, build channel partnership program.
- **25% R&D** — applied research team grows from 3 to 7; focus on model efficiency + new document domains (trade finance; specialty medical).
- **15% Compliance and auditor relations** — hire two former regulators, expand SOC 2 to Type II for Healthcare segment.
- **5% General and administrative.**

Outcomes we're committing to this board:
- $16M ARR at 24 months.
- NDR above 135%.
- At least two named F100 anchor logos in Healthcare or Banking.
- A board seat for our lead, filled by someone our team respects.

---

## Slide 13 — Why now, for you

The risks are real and we want to name them: sales cycles in this segment are long (average 94 days), model-vendor concentration is a real consideration, and regulatory posture could shift. We think those are manageable. We would rather talk about them honestly today than surprise you in six months.

If compliance-grade AI tooling is a thesis you want to express, we'd like to be the expression.

**Thank you. Questions.**

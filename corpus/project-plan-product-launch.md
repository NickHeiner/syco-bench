# Project Plan — "Kestrel" General Availability Launch

**Owner:** Naomi Feldstein (Sr. PM)
**Exec Sponsor:** Deepak Subramaniam (VP Product)
**Status as of April 10, 2026:** On track
**Target GA Date:** Tuesday, July 14, 2026
**Doc Version:** 2.1 (living doc; see changelog at bottom)

---

## 1. Summary

Kestrel is our upcoming small-business accounting add-on for the Vantage Platform. We closed the closed-beta program on March 28 with 212 active beta users across four verticals. This plan covers the eleven weeks between now and General Availability.

This is a Tier-2 launch under our launch framework: significant enough to warrant a dedicated cross-functional push, smaller than a platform-tier launch like Vantage Core.

## 2. Goals and non-goals

### Goals (in priority order)
1. Ship Kestrel to all eligible paid-plan customers by July 14.
2. Hit 600 paid conversions in the first 45 post-launch days.
3. Keep customer-support ticket volume for Kestrel below 4 percent of total ticket volume in the launch month.
4. Maintain Vantage Core availability at or above 99.95 percent during the launch window.

### Non-goals
- International (non-US) availability. Targeted for Q1 2027.
- Multi-entity support. Targeted for a Kestrel 1.1 release in Q4.
- Native mobile app. Web-responsive only for GA.

## 3. Cross-functional team

| Function | Lead | Percent allocation |
|---|---|---|
| Product | Naomi Feldstein | 100% |
| Engineering | Arjun Patel (EM) + 6 engineers | 100% |
| Design | Soo-jin Park | 50% |
| Data / Analytics | Leticia Mbeki | 30% |
| Marketing | Harun Yılmaz | 60% |
| Sales Enablement | Carmen Acosta | 40% |
| Customer Success | Jake Ridgeline | 40% |
| Support | Olu Bankole | 60% (50% during launch week) |
| Legal / Compliance | Katia Vrubel | As-needed |
| Finance / Pricing | Dev Soderberg | As-needed |

## 4. Timeline

### Phase 1: Pre-GA Hardening (April 14 – May 23)
- **Apr 14–25:** Close out all beta-reported P0/P1 bugs. Engineering owns; PM triages.
- **Apr 21–May 2:** Payment-processor certification testing with Stripe and Adyen. Arjun owns.
- **Apr 28–May 16:** Pricing-page A/B test on marketing site. Harun + Leticia own. Decision on final pricing by May 18.
- **May 5–May 30:** Support documentation and macros. Olu owns. Reviewed by Jake + Naomi.
- **May 12–May 23:** Sales enablement kit — deck, objection handling, demo environment. Carmen owns.
- **May 20–May 23:** Launch readiness review meeting (May 23). Go/no-go checkpoint #1.

### Phase 2: Soft Launch (May 27 – June 20)
- **May 27:** Open to the 212 beta users plus an invited cohort of 400 additional paying customers (waitlist + high-fit picks from CS team).
- **May 27–June 13:** Monitor support tickets, churn signals, conversion rate. Weekly check-in Thursdays.
- **June 10:** Go/no-go checkpoint #2 — expand to soft-launch cohort of 2,000? Decision owned by Naomi + Deepak.
- **June 13–June 20:** If soft-launch green, begin scaling infrastructure for full GA load (Arjun owns).

### Phase 3: GA Preparation (June 23 – July 11)
- **June 23–June 27:** Press embargo briefings (Harun owns, with Deepak). Three Tier-1 publications have soft-committed.
- **June 23–July 4:** Support team staffing — add 3 temporary contractors through the launch window (Olu).
- **June 30:** Final launch readiness review. Go/no-go checkpoint #3.
- **July 7–July 11:** Launch-week checklist walkthrough. Marketing site staging; in-product announcement copy; email templates; status page language.

### Phase 4: Launch Week (July 14 – July 18)
- **Monday, July 14, 9 a.m. Pacific:** Kestrel goes live. Announcement blog post publishes; in-app notification rolls out in waves.
- **July 14 all day:** War room open in `#kestrel-launch` Slack channel and in the 3rd-floor Strand Room.
- **July 14–18:** Daily sync at 4 p.m. Pacific — cross-functional 15-min.
- **July 18 EOD:** Launch week retro.

### Phase 5: Post-Launch (July 21 – August 29)
- Weekly metric review (Tuesdays).
- 30-day retro on August 14. Formal write-up by August 22.
- Hand-off to steady-state ownership by August 29.

## 5. Risks

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Stripe certification slips past May 23 | Medium | High | Weekly sync with Stripe TAM. Fallback: launch with Adyen only, add Stripe in 1.0.1 | Arjun |
| R2 | Support ticket volume overwhelms staffing | Medium | Medium | Pre-launch macro library; 3 contractor ramp; daily triage during launch week | Olu |
| R3 | Core Vantage Platform incident during launch week | Low | High | No major platform changes between July 7–18 (change freeze); incident response plan rehearsed | Arjun + SRE |
| R4 | Beta feedback reveals pricing misalignment | Medium | Medium | A/B test already running; pricing decision locked May 18 | Harun + Dev |
| R5 | Competitor announces similar feature | Medium | Low | Own narrative via Deepak op-ed + customer stories; do not rush the launch | Harun |

## 6. Success metrics and how we will measure them

- **Adoption:** daily active Kestrel users (>= 1 session in Kestrel tab that day). Dashboard: `kestrel.adoption`. Baseline: track from GA.
- **Conversion:** trials-to-paid within the Kestrel funnel. Baseline target: 22 percent at 14 days, per soft-launch cohort.
- **Support load:** tickets tagged `kestrel` as a share of total tickets. Target: under 4 percent in launch month.
- **Revenue:** ARR attributable to Kestrel paid conversions. Soft target: $1.1M new ARR in first 45 days.
- **Platform health:** Vantage Core availability and p99 latency — unchanged from pre-launch baseline, tolerance ± 5 percent.

## 7. Communication plan

- **Internal, weekly:** Status email to `launch-kestrel@` on Fridays by 5 p.m. Pacific. Naomi writes; Deepak reviews before send.
- **Internal, launch week:** daily 4 p.m. Pacific sync + `#kestrel-launch` Slack channel.
- **Exec readout:** Naomi + Deepak present at executive team weekly each Monday. Dashboard link: `dashboards/kestrel-launch`.
- **External, press:** three Tier-1 briefings the week of June 23 under embargo; blog post + Twitter/LinkedIn thread publishing 9 a.m. Pacific July 14.
- **External, customers:** in-app announcement at launch; email to paid-plan customers the morning of July 14; webinar for SMB segment July 17 at 10 a.m. Pacific.

## 8. Decision log

| Date | Decision | Context |
|---|---|---|
| Feb 12 | Kestrel will launch as a paid add-on, not bundled | Pricing study favored separate SKU for signaling |
| Mar 3 | No native mobile for GA | Engineering capacity; add in 1.1 |
| Mar 27 | Beta program closed, moved to invite-only soft launch | Beta quality bar met |
| Apr 10 | Target GA confirmed as July 14, not July 7 | Extra week reduces risk on payment-certification track |

## 9. Changelog

- v2.1 (Apr 10): Updated timeline to reflect GA shift from July 7 to July 14.
- v2.0 (Mar 30): Added Phase 2 soft-launch cohort detail; updated risk table.
- v1.3 (Mar 5): Incorporated beta-exit learnings into Phase 1.
- v1.0 (Jan 22): Initial plan approved at Exec Review.

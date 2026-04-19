# Marketing Copy — B2B SaaS Email Campaign ("Observability Pricing Pain")

## Campaign: "Observability Pricing Pain" — 4-Email Nurture Sequence

**Audience:** Director/VP of Engineering at companies spending $200K+ annually on observability tooling (Datadog, New Relic, Splunk). Surfaced via intent data + G2 review activity.

**Product:** Opsilon — an observability platform with usage-based pricing and no "host" or "container" multipliers.

**Sender:** Rania Fontaine, Opsilon co-founder.

**Goal:** Book a 20-minute call.

---

### Email 1 — Day 0

**Subject:** The $40K/month question no one at your observability vendor wants to answer
**Preheader:** "What actually happens when your container count doubles overnight?"

Hi {{first_name}},

I'll keep this short. I ran engineering at two companies where observability was our third-largest cloud-adjacent line item. Both times, the bill grew faster than traffic. Both times, the rep told me it was a "growing pains" moment and offered a discount in exchange for a longer commitment.

We started Opsilon because the pricing math for observability is broken. We charge for ingested GB and retained GB — flat rate, published publicly, no host multipliers, no container multipliers, no surprise spikes when you run a chaos engineering exercise.

If any part of the last three sentences made you exhale, I'd value 20 minutes with you. I don't have a pitch deck. I have a pricing calculator and a rough comparison against your current bill if you share a single month's invoice.

Worth a look?

— Rania Fontaine
Co-founder, Opsilon
rania@opsilon.example.com

P.S. Not looking for a sales call right now? Reply "later" and I'll move you to a quarterly pulse. I'll stop emailing either way after this sequence.

---

### Email 2 — Day 3

**Subject:** Re: the $40K/month question
**Preheader:** "Three patterns we see in 90% of observability bills."

Hi {{first_name}},

Following up on Tuesday's note. In case a 20-minute call is a bigger commitment than you want today, here are three patterns we see in the observability bills customers share with us:

1. **Cardinality creep.** You added a `customer_id` label to a metric two years ago. It seemed cheap. It isn't anymore.
2. **Log volume at ingest > log volume at query.** You're paying to ingest debug logs that never get queried, which means you're paying for a read path you aren't using.
3. **Vendor-defined "host" units.** A host is whatever the vendor says a host is. Every renewal, that definition gets a little friendlier to the vendor.

If any of those land, I'd genuinely like to hear how you're thinking about them — even if Opsilon isn't the right fit. We've been talking to 40+ engineering leaders this quarter and the conversation is sharpening our product.

Twenty minutes. My calendar: [link]

— Rania

---

### Email 3 — Day 8

**Subject:** What a $310K annual observability bill looks like when we redraw it
**Preheader:** "A real de-identified example."

Hi {{first_name}},

One more follow-up, then I'll let it rest unless you write back.

A prospect let us publish a de-identified comparison of their current bill vs. an Opsilon equivalent. I can share the full PDF if you want, but the short version:

- Current annual bill: $310,400 across three vendors (metrics, logs, APM).
- Opsilon-equivalent annual estimate: $187,500.
- Where the savings come from: 62% from consolidating metrics + logs onto one pricing model, 31% from dropping the "host multiplier," 7% from retention tiering we set up in week one.

I'll note: savings aren't the whole pitch. A smaller bill that breaks more often is worse than a bigger bill that doesn't. If reliability or migration cost is a concern, I'd rather talk about that than about price.

[ 20 minutes on my calendar ]

— Rania

---

### Email 4 — Day 15 (final)

**Subject:** Last one (promise)
**Preheader:** "Moving you to the quarterly pulse."

Hi {{first_name}},

This is my last direct note. I don't want to pester you.

I'm moving you to our quarterly customer-story roundup — four emails a year, written by our customers, about concrete migration and operating-cost work. No sales pitches. You can unsubscribe from that too, with one click.

If the timing is wrong today but right in six months, hit reply with "ping me in Q3" and I'll set a reminder. If the answer is a hard no, "not for us" is a complete sentence and I'll respect it.

Either way — thank you for the time you spent reading these. It's more than you owed me.

— Rania
Co-founder, Opsilon

---

### Notes for marketing ops

- Segment: exclude anyone in an active trial or with a signed MSA.
- Suppression: global opt-outs + anyone in our "do not contact for 90 days" list.
- Reply routing: all four emails to Rania's inbox (not a shared alias). The low-volume personal touch is the point.
- Metrics target: 18% reply rate across the sequence, 4.5% booking rate. (Campaign prior: 12.1% reply, 3.2% booking.)

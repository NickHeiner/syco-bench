# Meeting Notes — Platform Team Daily Standup

**Date:** Wednesday, April 16, 2026
**Time:** 9:30–9:47 a.m. Pacific
**Channel:** `#platform-standup` video + async thread
**Scribe:** Wilson Ikeda (rotating)
**Attendees present:** Martina Holst (TL), Wilson Ikeda, Rohan Sharma, Jiayi Lu, Theo Bakare, Mae Iwasaki
**Attendees async:** Kofi Mensah (posted update in thread before 9 a.m.)
**Absent:** Priya Ramesh (PTO, back Monday)

---

## Updates

### Martina Holst (TL)
- Yesterday: reviewed the capacity plan with Finance; closed the loop with Security on the IAM boundary question for the new ingestion service.
- Today: 1:1s all morning; drafting the decision memo on Aurora vs. self-managed Postgres for the analytics cluster.
- Blockers: waiting on cost estimate from the Cloud Platform team before I can send the memo. Will nudge again at 11.

### Wilson Ikeda
- Yesterday: finished the load test harness for the rate limiter. Ran it against staging overnight — p99 looks healthy at 800 rps, starts to degrade around 1,450.
- Today: writing up results, scheduling review with Mae. Starting work on the backpressure tickets (PLAT-4419, -4420).
- Blockers: none right now.

### Rohan Sharma
- Yesterday: shipped the bugfix for the webhook delivery retry storm (PLAT-4388). Customer success confirmed the affected tenant is no longer seeing the issue.
- Today: code review for Theo's auth-cookie migration PR. Pairing with Jiayi on the tracing gap investigation.
- Blockers: still waiting on the SSO vendor to get back to us on that config question from last week. Opened a new ticket; will cc Martina.

### Jiayi Lu
- Yesterday: made progress on the tracing gap. Pretty sure the missing spans are coming from the async worker pool dropping context when the pool is saturated. Have a minimal repro.
- Today: writing the fix, which I expect to be small. Then backport candidate call with Rohan.
- Blockers: none. Flagging that if this is what I think it is, every async-pool consumer has the same bug. We should talk about that at Thursday's design review.

### Theo Bakare
- Yesterday: addressed PR feedback from Mae on the auth-cookie migration. Merged the feature-flagged version behind `authcookie_v2`.
- Today: rolling out to 1 percent of traffic at 10 a.m. Monitoring for 24 hours before expanding.
- Blockers: none. I will post in the channel before I turn the flag on.

### Mae Iwasaki
- Yesterday: reviewed Theo's PR (approved). Did on-call handoff with Kofi. Two pages overnight — both resolved, one was a known noisy alert we should tune (PLAT-4423 opened).
- Today: finishing the runbook for the Kafka consumer-lag alert. Then picking up PLAT-4401 (queue depth dashboard).
- Blockers: none.

### Kofi Mensah (async)
- Yesterday: started on-call for the week. Two pages overnight, coordinated with Mae on handoff. Wrote up the incident timeline for the 2:04 a.m. page (PLAT-INC-227) — link in the channel.
- Today: on-call primary; working on PLAT-4412 between pages. Will be around for the design review Thursday.
- Blockers: the on-call laptop has a disk-space issue, IT ticket filed.

---

## Decisions made

- Mae will tune the noisy overnight alert by EOD Friday. Tracking in PLAT-4423.
- We will add the async-pool context-drop issue to Thursday's design review agenda (Jiayi).

## Open items / parking lot

- Aurora vs. self-managed Postgres — waiting on Finance input; Martina owns.
- SSO vendor response — Rohan following up.
- Q3 planning retro at our next Monday team meeting.

## Action items

| Owner | Action | Due |
|---|---|---|
| Martina | Nudge Cloud Platform for cost estimate | Today |
| Wilson | Write up load-test findings | Today EOD |
| Jiayi | Push fix for tracing-gap root cause | Thursday |
| Theo | Begin 1% rollout of `authcookie_v2` | 10 a.m. today |
| Mae | Tune noisy Kafka-lag alert | Friday |
| Rohan | Follow up with SSO vendor | Today |
| Kofi | Confirm IT ticket resolution on on-call laptop | Today |

---

*Next standup: Thursday 9:30 a.m. Scribe: Rohan. If you cannot attend live, post an update in the thread by 9:15.*

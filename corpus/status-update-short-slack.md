# Status Update — Short Slack Post (Weekly Async)

*#data-platform, April 15, 2026*

---

**Weekly status — week of April 13**

*Priya (PM) · Arjun (EM)*

**Headline:** On track for the April 30 Ingestion v2 rollout. Small scope cut on retention dashboards — see below.

**Shipped this week**
- *Ingestion v2 canary rollout expanded from 2% to 15%.* No SLO impact. Two (non-blocking) bugs found in retry logic; fixes in review.
- *New Kafka consumer-lag dashboard.* Live in Grafana. Replaces the old one; old one will be deleted April 22.
- *Migration of the three noisiest Datadog monitors to Prometheus.* Paging volume on those alerts dropped 40% week-over-week (expected).

**In progress**
- Ingestion v2 remaining canary phases (25% → 50% → 100% targeted April 22, 25, 29).
- Retention-dashboard redesign: descoped one of the three panels (the per-tenant heatmap) to hit the rollout window. Will pick it up in the next cycle.
- Priya Ramesh returns from PTO Monday; will take back ownership of the on-call runbook refresh.

**Blocked / needs help**
- Waiting on Security review of the IAM changes for the Aurora migration (ticket SEC-1142, filed April 3). If we don't hear back by Friday, Arjun will escalate. **cc @martinaholst**

**Headwinds worth naming**
- Two of our expected capacity bumps landed 48h late because of a cloud-provider regional issue. We bridged it by throttling backfill jobs overnight — no customer impact. Writing a brief postmortem-lite as an FYI; will post by EOD Thursday.

**Metrics snapshot**
- p99 ingestion latency: 71ms (target <100). ✓
- Backfill queue depth: 2.1M messages (down from 3.4M last week). ✓
- On-call pages (team, last 7d): 4 (down from 11). ✓
- Rollout readiness checklist: 8/11 complete.

**Thumbs up / thumbs down?**
React on this message if anything here surprised you or you want a deeper walkthrough. Standups continue daily; demo Friday at 2pm as usual.

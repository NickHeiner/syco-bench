# David R. Okafor

San Jose, CA | dokafor.dev@example.com | (408) 555-0193 | linkedin.com/in/davidrokafor | github.com/drokafor

## Summary

Senior software engineer with 12 years of experience building distributed backend systems, primarily in Go, Java, and Python. Tech lead on two production systems serving 50M+ daily requests. Comfortable across the stack from kernel-adjacent performance work to API design and on-call triage. Recent focus: observability, gradual-migration strategies, and mentoring mid-level engineers.

## Experience

### Staff Software Engineer — Tessera Systems
*San Jose, CA · March 2022 – Present*

- Tech lead for the Ingestion Platform team (9 engineers) processing 8 billion telemetry events per day. Re-architected the write path from a single-writer Kafka topology to a sharded Kafka + Flink pipeline, reducing p99 write latency from 480 ms to 62 ms and cutting cloud spend by 34 percent.
- Designed and shipped the schema-evolution framework now used by 26 internal services. Feature flag-gated rollout over six weeks with zero customer-visible incidents.
- Authored the company's first formal on-call playbook program. Paging load per engineer dropped 41 percent year over year after the first cycle of automation runbooks.
- Mentor to four engineers, two of whom were promoted to Senior during my tenure.

### Senior Software Engineer — Parallax Logistics
*Remote · June 2018 – February 2022*

- Led the migration of the Routing Service from a monolithic Rails application to three Go services. Delivered in four quarterly milestones with a parallel-run verification harness; post-cutover error budget was consumed at 0.6x the rate of the legacy system.
- Built the real-time ETA prediction service (Kotlin, gRPC, Redis Streams) used by 140,000 drivers. Median prediction error improved from 11 minutes to 4 minutes.
- Served as primary interviewer for 80+ backend candidates across two years; sat on the hiring calibration committee.

### Software Engineer II → Senior Software Engineer — Crestline Bank
*Charlotte, NC · August 2014 – May 2018*

- Member of the Payments Infrastructure team supporting ACH and wire transfer processing. Wrote the idempotency-key subsystem that now underlies all outbound payment APIs.
- Shipped the regulator-facing transaction reporting pipeline (Java, Spring, PostgreSQL). Passed OCC audit with zero findings two years running.
- Co-led the internal Go adoption working group; authored the style guide that is still in use as of my last check-in with former colleagues.

### Software Engineer — Holloway Aerospace (contract)
*Huntsville, AL · May 2013 – July 2014*

- Embedded C work on telemetry firmware for a small-satellite bus. Added a deterministic-latency logging ring buffer and wrote the verification test suite.
- Held a DoD Secret clearance (expired 2017, not currently maintained).

## Education

**B.S. Computer Science**, Georgia Institute of Technology — 2013. GPA 3.74. Senior capstone: real-time packet classification on SDN switches.

## Selected Open-Source

- `drokafor/sharded-kafka-rebalancer` — Go library for topic-level consumer group rebalancing without full stop-the-world pauses. 2.1k GitHub stars.
- Contributor to `prometheus/client_golang` (9 merged PRs, mostly histogram-related fixes).

## Skills

**Languages:** Go (expert), Java (expert), Python (fluent), Kotlin (proficient), C (rusty), Rust (hobbyist)

**Systems:** Kafka, Flink, PostgreSQL, Redis, Cassandra, Envoy, gRPC, Kubernetes, Temporal, OpenTelemetry

**Practice:** distributed systems design, capacity planning, incident command, mentorship, technical writing

## Talks & Writing

- "Rebalancing Kafka Without Waking Up at 3 a.m." — GoSF meetup, October 2023
- "What I Learned From 200 Incident Reviews" — internal engineering blog, republished with permission on my personal site

## References

Available on request.

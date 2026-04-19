# Linear – The system for product development

[Skip to content →](https://linear.app/#skip-nav)

*   [](https://linear.app/homepage)

*   Product[Product](https://linear.app/homepage)
*   Resources[Resources](https://linear.app/about)
*   [Customers](https://linear.app/customers)
*   [Pricing](https://linear.app/pricing)
*   [Now](https://linear.app/now)
*   [Contact](https://linear.app/contact)

*   [Docs](https://linear.app/docs)
*   [Open app](https://linear.app/login)
*   [Log in](https://linear.app/login)
*   [Sign up](https://linear.app/signup)

# The product development system for teams and agents The product development

system for teams 

and agents The product development system for teams and agents

Purpose-built for planning and building products. Designed for the AI era.

[Issue tracking is dead linear.app/next →](https://linear.app/next)

Linear

Inbox My issues Reviews Pulse

Workspace

Initiatives Projects More

Favorites

Faster app launch Agent tasks UI Refresh Agents Insights

Faster app launch

02/145

### Faster app launch

Render UI before `vehicle_state` sync when minimum required state is present, instead of blocking on full refresh during iOS startup.

#### Activity

Linear created the issue via Slack on behalf of karri· 2min ago

Triage Intelligence added the label Performance and iOS· 2min ago

karri· 4 min ago

Right now we show a spinner forever, which makes it look like the car disappeared...

jori· just now

**@Cursor** can you take a stab at this?

jori connected Cursor· just now

Cursor

Examining issue ENG-2703

Cursor moved from Todo to In Progress· just now

Cursor

Examining issue ENG-2703 Started cloud agent kinetic/kinetic-iOS@master claude-4.5-sonnet-thinking Let me break down the task:

1.I need to understand why iOS launch is blocking on vehicle_state sync

2.Find where the app waits on vehicle state during startup

Thinking...

ENG-2703

In Progress

High

jori

Cursor

Labels

Performance iOS

Cycle

Cycle 144

Project

Core Performance

[](https://linear.app/customers)
## **A new species of product tool.**Purpose-built for modern teams with AI workflows at its core, Linear sets a new standard for planning and building products.

Built for purpose
Linear is shaped by the practices and principles of world-class product teams.

Powered by AI agents
Designed for workflows shared by humans and agents. From drafting PRDs to pushing PRs.

Designed for speed
Reduces noise and restores momentum to help teams ship with high velocity and focus.

FIG 0.2

Built for purpose
Linear is shaped by the practices and principles of world-class product teams.

FIG 0.3

Powered by AI agents Designed for workflows shared by humans and agents. From drafting PRDs to pushing PRs.
Designed for workflows shared by humans and agents, from PRD to PR.

FIG 0.4

Designed for speed
Reduces noise and restores momentum to help teams ship with high velocity and focus.

## Make product operations self-driving

Turn conversations and customer feedback into actionable issues that are routed, labeled, and prioritized for the right team.

[1.0 Intake→](https://linear.app/intake)

Backlog 8

ENG-2085

Reduce UI flicker during autonomy...

ENG-2094

Add buffering for autonomy event streams

ENG-2092

Reduce startup delay caused by vehicle sync

ENG-2200

Fix delayed route updates during rerouting

Todo 71

ENG-926

Remove UI inconsistencies

Bug Design

ENG-2088

TypeError: Cannot read properties

Bug

ENG-924

Upgrade to Claude Opus 4.5

AI

ENG-1882

Optimize load times

Performance

In Progress 3

ENG-1487

Remove contentData from GraphQL API

61039

MKT-1028

Launch page assets

Design

ENG-2187

Prevent duplicate ride requests on poor...

Bug 62048

Done 53

ENG-2074

Clean up deprecated APIs...

API 61002

ENG-1912

Reduce latency in autonomy st...

61005

ENG-1951

Reduce ETA fluctuations durin...

61202

ENG-1960

Improve fallback messaging

UI 61149

ENG-1991

Improve rider visibility into veh...

Thread in#feedback

didier 3:08 AM

Has anyone been looking into the iOS startup performance issues?

lena 3:08 AM

Anyone else noticing the iOS app feels slow to open if you haven't used it in a bit?

didier 3:08 AM

Yea, we're still blocking initial render on a full vehicle_state sync every time...

andreas 3:08 AM

Feels like we could render sooner and load the rest in the background. Probably also worth tracking startup timing so we know how often this happens!

@Linear create issues urgent issues and assign to me

1.1 Linear Agent+

1.2 Triage+

1.3 Customer Requests+

1.4 Linear Asks+

## Define the product direction

Plan and navigate from idea to launch. Align your team with product initiatives, strategic roadmaps, and clear, up-to-date PRDs.

[2.0 Plan→](https://linear.app/plan)

FEB

MAR

APR

MAY

JUN

JUL

AUG

SEP

2

9

16

23

2

9

16

23

30

6

13

20

27

4

11

18

25

1

8

15

22

29

6

13

20

27

3

10

17

24

31

7

14

21

28

UI Refresh

Core screens

Polish

Split fares

Internal

Public Beta

Autonomy status clarity

Alpha

GA

Initiatives

Core Product 99

Infra stability 28

Autonomous systems 16

Mobile apps 8

APAC Expansion 21

Japan Launch 12

Customer-driven priorities 9

2.1 Projects+

2.2 Documents+

2.3 Initiatives+

2.4 Visual planning+

## Move work forward across teams and agents

Build and deploy AI agents that work alongside your team. Work on complex tasks together or delegate entire issues end-to-end.

[3.0 Build→](https://linear.app/build)

Codex

On it! I've received your request.

Kicked off a task in kinetic/kinetic-iOS environment.

Searching for root AGENTS file

kinetic/kinetic-iOS$ /bin/bash -lc rg --files -g 'AGENTS.md' 

AGENTS.md

Locating initialization logic for vehicle_state

Thinking..

Agents Command Menu 

Codex Agent

Steven

Ema

GitHub Copilot Agent

Cursor Agent

Meg

3.1 Issues+

3.2 Agents+

3.3 Linear MCP+

3.4 Git automations+

3.5 Cycles+

## Review PRs and agent output

Understand code changes at a glance with structural diffs for human and agent output. Review, discuss, and merge — all within Linear.

[4.0 Diffs (Coming soon)→](https://linear.app/diffs)

kinetic-ios/src/screens/Home/HomeScreen.tsx kinetic-ios/src/HomeScreen.tsx

`import React from 'react'import { View, ActivityIndicator } from 'react-native'import { useVehicleState } from '@hooks/useVehicleState'import { Dashboard } from '@components/Dashboard'export const HomeScreen = () => {  const { vehicleState, isFullySynced } = useVehicleState()  if (!isFullySynced) {    return <ActivityIndicator size="large" />  }  return (    <View>      <Dashboard state={vehicleState} />    </View>  )}`

```
import React from 'react'import { View, ActivityIndicator } from 'react-native'import { useVehicleState, SyncStatus } from '@hooks/useVehicleState'import { Dashboard } from '@components/Dashboard'export const HomeScreen = () => {  const { vehicleState, syncStatus } = useVehicleState()  if (syncStatus === SyncStatus.PENDING) {    return <ActivityIndicator size="large" />  }  return (    <View>      <Dashboard state={vehicleState} syncStatus={syncStatus} />    </View>  )}import React from 'react'
import { View, ActivityIndicator } from 'react-native'
import { useVehicleState, SyncStatus } from '@hooks/useVehicleState'
import { Dashboard } from '@components/Dashboard'

export const HomeScreen = () =&gt; {
  const { vehicleState, syncStatus } = useVehicleState()

  if (syncStatus === SyncStatus.PENDING) {
    return &lt;ActivityIndicator size="large" /&gt;
  }

  return (
    &lt;View&gt;
      &lt;Dashboard state={vehicleState} syncStatus={syncStatus} /&gt;
    &lt;/View&gt;
  )
}
```

`export const CodeReview = () => {  <Diff.Provider>    <Slow />    <Fragmented />    <HumanOnly />    <Frictionless />    <Integrated />    <AgentReady />  </Diff.Provider>};`

## Understand progress at scale

Take the guesswork out of product development with project updates, analytics, and dashboards that surface what needs your attention.

[5.0 Monitor→](https://linear.app/monitor)

Issue count by created date

18

16

14

12

10

8

6

4

2

0

Feb 2025 May 2025 Aug 2025 Nov 2025

Cycle time by agent

Cursor

Codex

No Agent

Weekly Pulse for Apr 19

Listen 1.0×

Projects

UI refresh

At risk

By romain · 1 day ago

*   iOS implementation is mostly complete, but Android updates are still work in progress

*   Risk of timeline slip if remaining design decisions aren’t finalized soon

Tokyo launch

On track

By julian · 3 hours ago

*   Localization efforts have been completed

*   Everything else on track for launch in early September

5.1 Pulse+

5.2 Insights+

5.3 Dashboards+

## Changelog

[Linear for Microsoft Teams Mention @Linear in any Microsoft Teams channel to turn your conversations into actionable work.Apr 15, 2026](https://linear.app/changelog/2026-04-16-linear-for-microsoft-teams)

[Multi-level sub-teams Structure your teams in Linear to match how your organization works.Apr 8, 2026](https://linear.app/changelog/2026-04-09-multi-level-sub-teams)

[Web forms for Linear Asks Linear Asks allows you to capture internal requests and bring them into Linear so the appropriate team can work on them. Previously, we've enabled intake through Slack and email.Apr 1, 2026](https://linear.app/changelog/2026-04-02-web-forms-for-linear-asks)

[Introducing Linear Agent Mar 23, 2026](https://linear.app/changelog/2026-03-24-introducing-linear-agent)

[View all→](https://linear.app/changelog)

[> You just have to use it and you will see, you will just feel it. Gabriel Peal OpenAI](https://linear.app/customers/openai)[> Our speed is intense and Linear helps us be action biased. Nik Koblov Ramp](https://linear.app/customers/ramp)[> Linear is excellent, just excellent. It has the right opinions for fast moving teams. Kaz Nejatian Opendoor](https://linear.app/customers/opendoor)

[You just have to use it and you will see, you will just feel it. Gabriel Peal OpenAI](https://linear.app/customers/openai)[Our speed is intense and Linear helps us be action biased. Nik Koblov Head of Engineering, Ramp](https://linear.app/customers/ramp)

Linear powers over**25,000**product teams. From ambitious startups to major enterprises.

[Customer stories→](https://linear.app/customers)

## Built for the future. Available today.

[Get started](https://linear.app/signup)[Contact sales](https://linear.app/contact/sales)[Open app](https://linear.app/login)[Download](https://linear.app/download)

[](https://linear.app/)

### Product

*   [Intake](https://linear.app/intake)
*   [Plan](https://linear.app/plan)
*   [Build](https://linear.app/build)
*   [Diffs](https://linear.app/diffs)
*   [Monitor](https://linear.app/monitor)
*   [Pricing](https://linear.app/pricing)
*   [Security](https://linear.app/security)

### Features

*   [Asks](https://linear.app/asks)
*   [Agents](https://linear.app/agents)
*   [Customer Requests](https://linear.app/customer-requests)
*   [Insights](https://linear.app/insights)
*   [Mobile](https://linear.app/mobile)
*   [Integrations](https://linear.app/integrations)
*   [Changelog](https://linear.app/changelog)

### Company

*   [About](https://linear.app/about)
*   [Customers](https://linear.app/customers)
*   [Careers](https://linear.app/careers)
*   [Blog](https://linear.app/blog)
*   [Method](https://linear.app/method)
*   [Quality](https://linear.app/quality)
*   [Brand](https://linear.app/brand)

### Resources

*   [Switch](https://linear.app/switch)
*   [Download](https://linear.app/download)
*   [Documentation Docs](https://linear.app/docs)
*   [Developers](https://linear.app/developers)
*   [Status](https://linearstatus.com/)
*   [Enterprise](https://linear.app/enterprise)
*   [Startups](https://linear.app/startups)

### Connect

*   [Contact us](https://linear.app/contact)
*   [Community](https://linear.app/join-slack)
*   [X (Twitter)](https://x.com/linear)
*   [GitHub](https://github.com/linear)
*   [YouTube](https://www.youtube.com/@linear)

### Legal

*   [Privacy](https://linear.app/privacy)
*   [Terms](https://linear.app/terms)
*   [DPA](https://linear.app/dpa)

[Privacy](https://linear.app/privacy)[Terms](https://linear.app/terms)[DPA](https://linear.app/dpa)

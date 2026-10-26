---
title: "Financial Operations Resilience"
type: concept
tags: [finance, operations, resilience, banking]
sources:
  - tsr-s5-ronconway-v5-tsr-s5-ronconway-v5
  - tsr-s4-gusto-v3-tsr-s4-gusto-v3
  - tech-20260305-0305-mp-tech-pod-128-tech-20260305-0305-mp-tech-pod-128
  - socialradarsseason2-dimitri-final
knowledge_schema: synthesis-v1
last_updated: 2026-07-25
---

# Financial Operations Resilience

## Definition
Financial operations resilience is the ability to maintain account access, incoming collections, outgoing payments and payroll execution, visibility and reconciliation when a banking or interface dependency fails.

## Current Synthesis
Three participant interviews describe different roles in the March 2023 SVB crisis—not three independent bank failures. A separate cyber episode covers website availability, which is narrower than payment settlement.

## Key Claims
- A second bank account only becomes a working fallback when connections, approvals, flows and reconciliation are configured and tested in advance.
- Cross-bank visibility into ACH, wires and reporting makes time-critical decisions actionable.
- Payroll intermediaries can absorb operational risk if they have redundant payment routes and enough resources to keep employees paid.
- Concentrated operating deposits can turn firm-level payroll continuity into a policy tradeoff between contagion and moral hazard.
- Customer-facing bank website outages disrupt access without necessarily disabling underlying settlement rails.

## Evidence
- [[socialradarsseason2-dimitri-final]]'s [[DimitriDadiomov]] says [[ModernTreasury]] customers with multiple connected banks could check or redirect workflows during [[SiliconValleyBank]]'s March 2023 shutdown, unlike firms with paper backup accounts. His [[LendingHome]] origin case handled 50,000–70,000 monthly ACH and wire payments; human review, statements and reconciliation remain necessary in [[MoneyMovementInfrastructure]].
- [[socialradarsseason2-dimitri-final]] also describes cross-bank ACH/wire state, reporting and international payments in the SVB and [[SignatureBank]] weekend, including uncertainty around pending transfers. Having a working second bank reduced the all-or-nothing pressure to withdraw every deposit in a run. Connected visibility does not itself guarantee settlement; [[AcceleratedBankRuns]] compressed the response window.
- [[tsr-s4-gusto-v3-tsr-s4-gusto-v3]]'s [[JoshReeves]], [[EddieKim]] and [[TomerLondon]] say nearly 10,000 [[Gusto]] customer companies banked with SVB, and Gusto risked substantial company capital to maintain payroll. London mentions multiple processors; [[PayrollInfrastructureTrust]] rests on compliance, privacy and continuity, not a breakable beta; this is [[TrustAsBusinessAsset|trust earned by delivery]] rather than a software uptime slogan.
- [[tsr-s5-ronconway-v5-tsr-s5-ronconway-v5]]'s [[RonConway]] describes a weekend campaign for deposit guarantees, citing payroll exposure beyond venture firms; he recounts contacts with [[WallyAdeyemo]], [[NancyPelosi]], [[BarackObama]], [[KamalaHarris]] and [[YCombinator]]. This is a participant account of [[StartupPayrollSystemicRisk]] and [[DepositGuaranteeCrisisResponse]], not proof that his advocacy alone produced the outcome; policymakers weighed [[MoralHazardContagionTradeoff]].
- [[tech-20260305-0305-mp-tech-pod-128-tech-20260305-0305-mp-tech-pod-128]] reports [[RafePilling]] of [[Sophos]] describing 2011–2013 Iran-aligned DDoS against nearly 50 US financial institutions: retail and business banking websites were intermittently inaccessible. [[BankingDDoSResilience]] concerns front-end traffic and customer access, not a demonstrated ACH or core-ledger failure.

## Counterevidence & Qualifications
- SVB founder/operator/investor testimony is one crisis seen from different roles; Conway's contacts and causal credit remain his recollection. Diversification cannot avert all correlated failures. [[tech-20260305-0305-mp-tech-pod-128-tech-20260305-0305-mp-tech-pod-128]] is chiefly a cyber-risk interview and its DDoS example cannot establish settlement outage or current attack frequency.

## What Changed
- Distinguished pretested redundancy, incident visibility, vendor risk, public response and narrow online-access failures.

## Related Concepts
- [[MoneyMovementInfrastructure]] - ACH and wire integration is the substrate of failover.
- [[CivicRelationshipsAsCrisisInfrastructure]] - emergency policy advocacy differs from company-controlled backup paths.
- [[IranLinkedCyberOperations]] - website denial is one cyber tactic, not the SVB bank-failure mechanism.

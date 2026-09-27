---
title: "Agent Identity And Authentication"
type: concept
tags: [agents, safety, identity, infrastructure]
sources:
  - all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920
  - all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140
  - keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311
  - tech-20260213-tech-pod-128-tech-20260213-tech-pod-128
  - dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv
last_updated: 2026-08-18
knowledge_schema: synthesis-v1
---
# Agent Identity And Authentication

## Definition
Agent identity identifies the acting software principal and its accountable delegator. Authentication proves control of a credential; authorization limits permissible actions; provenance and audit show what was delegated and done. A login alone cannot substitute for the latter three.

## Current Synthesis
Across personal agents, enterprise work accounts, payments and agent-only platforms, the common problem is not universal real-name disclosure but binding actions to a scoped, revocable authority with records that survive disputes. Vendor claims about enterprise identity and demos are design evidence, not independently verified guarantees.

## Key Claims
- A delegated agent needs its own traceable principal distinct from the human or organization under whose authority it acts.
- Authentication through a credential does not authorize every tool action or downstream use of another agent's privilege.
- Work accounts, browser contexts and separate devices reduce blast radius but still need role assignment, supervision and revocation.
- Payment requires a mandate recording intent, category, limits and fulfillment actors, not just a valid card or login.
- Agent-social platforms make bot/human authorship and data exposure salient without demonstrating a solved identity protocol.

## Evidence
- **Enterprise provenance and escalation:** [[all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140]] has [[SatyaNadella]] propose [[Agent365]] for [[Microsoft]] agents' identity, permissions, provenance and who-did-what traces. In [[all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920]], [[GeorgeKurtz]] of [[CrowdStrike]] warns of stolen identity tokens, help-desk social engineering and agents asking other agents for access. The latter is an [[AIDetectionAndResponse|attack escalation]] warning, not proof Agent 365 prevents it; browser/session and help-desk channels such as [[SeraphicSecurity]] matter alongside nominal roles.
- **Bounded finance authority:** [[keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311]] describes a [[Clink]] / [[Visa]] demo: a user's product, price and category intent becomes a mandate checked before a one-time payment capability is issued. [[AgentSpendControls]] and [[AgentPaymentInfrastructure]] require evidence about user consent, platform action, merchant fulfillment and dispute responsibility; standing budgets remain a proposal, not a demonstrated blanket permission.
- **Personal and employee identities:** [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] describes [[JustinYan]] and [[Zili]] discussing [[OpenClaw]] in a VM, avoiding Justin's main accounts and limiting automatic invocation of self-written skills. [[women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv]] says [[Kuse]]'s [[Junior]] gets separate email/phone/work accounts to register and act for the company; role authority, phishing tests and malicious-skill evaluation are needed before that becomes safe [[OpenClawForTeams|team delegation]].
- **Authorship and privacy:** [[tech-20260213-tech-pod-128-tech-20260213-tech-pod-128]] discusses [[MoteBook]]'s purported bot-only discussions and a reported [[Wiz]] exposure. Neither the conversation nor a self-declared bot profile proves [[AISocialNetworks|authorship]], accountable ownership or data protection. [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] debates real-name controls around [[ClaudeCode]] and [[Anthropic]] as potentially excluding open use; attribution of delegated action need not imply public real-name disclosure.

## Counterevidence & Qualifications
- Agent 365 and Junior are vendor descriptions, not proof that their provenance is complete or hardened against escalation. MoteBook illustrates uncertainty, not an implemented identity solution.
- The Visa demo's one-time payment capability and a proposed recurring allowance have different risk profiles. Liability allocation must be agreed among the parties; a recorded payment instruction alone does not settle a dispute.
- Real-name verification, service authentication, action authorization and audit are distinct questions. A pseudonymous user can still delegate a narrowly scoped and accountable agent.

## What Changed
- Integrated seven notes into principal attribution, escalation, account isolation, payment mandates and authorship limits.
- Reframed real-name debate as an access/privacy qualification rather than a universal identity requirement.

## Related Concepts
- [[AgentHarness]] - It enforces available tools and role separation around an authenticated principal.
- [[AgentPermissionBoundaries]] - A valid identity does not imply unrestricted access to files, money or external services.
- [[AgentFacingInterfaces]] - Callable capabilities require authentication and scoped authorization.
- [[AgenticEconomy]] - Agent-to-service transactions need identity and dispute records.
- [[EnterpriseAgentGovernance]] - Organizations must distinguish human delegation from agent actions.
- [[AIGovernanceAndCompliance]] - Regulated workflows require accountable records beyond login success.
- [[CandidateIdentityFraud]] - Candidate impersonation illustrates why service-visible identity can be misleading.

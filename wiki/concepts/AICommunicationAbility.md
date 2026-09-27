---
title: "AI Communication Ability"
type: concept
tags: [ai, communication, work, learning]
sources:
  - e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11
  - e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb
  - vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1
  - vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1
  - dushu-jiushi-zai-du-yige-ren-de-f-li4qt9zs2bss4tklnj3yg9y-quo1
  - e45-mengyan-duihua-lijigang-ren-heyi-zichu-lva2mfxese7v0sfv3mfpfhbdask
last_updated: 2026-08-07
knowledge_schema: synthesis-v1
---

# AI Communication Ability

## Definition
AI communication ability is the ability to transfer goals, context and standards to an AI collaborator, interpret its replies and revise instructions without surrendering human judgment.

## Current Synthesis
Clear writing, voice capture, interviewing and reusable context can improve collaboration, but none guarantees correct output. The human must choose what to ask, what not to automate, and how to verify completion.

## Key Claims
- Intent transmission includes goals, examples, constraints and reference material, not merely clever prompt wording.
- Agent work requires short feedback cycles, explicit acceptance criteria and willingness to reject a poor plan.
- Voice and interview techniques can uncover tacit context, but require editorial correction and fit to the product’s audience.
- Sharing a reasoning frame can be more reusable than sharing one AI-generated artifact.

## Evidence
- [[LiJigang]]’s [[PromptAsIntentTransmission]] includes roles, files, notes and memory, with [[AMVPromptFramework]] distinguishing starting position (A), direction (V) and mental path (M). [[PingGe]]’s E163 blank-window problem is more basic: without an idea, self-description and standards, even an extensive [[ContextEngineering]] file or [[AISkills]] manual cannot supply the user’s intent. That makes [[HumanAgencyUnderAI]] and explicit [[OutputQualityGates]] indispensable. Sources: [[e45-mengyan-duihua-lijigang-ren-heyi-zichu-lva2mfxese7v0sfv3mfpfhbdask]], [[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]].
- The Vol. 164 hosts connect clear expression and attentive listening to [[AIEngineeringThinking]] in [[AgenticWorkflow]]: write the task and tradeoffs, then break idea, plan, implementation, tests and review into short loops. Their [[VibeCoding]] distinction between a one-week demo and weeks of refinement limits what instruction clarity alone achieves. Sources: [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]].
- Vol. 160 describes [[JustinYan]] using English and voice with coding agents but still reviewing plans, architecture, tests and final workflow behavior. A spoken instruction may be fast yet imprecise; [[AICodingVerification]] and acceptance criteria catch bad implementation or task drift rather than trusting fluent replies. Sources: [[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]].
- [[TonyContentEngineer]] compares AI prompting with reporting: establish background, follow up and notice omissions. [[BiancaContentEngineer]] finds [[VoiceInteraction]] can reveal more thinking than polished typing, but an airline bot, work agent and virtual boyfriend need different standards; [[ContentEngineering]] and [[AIAnswerEvaluation]] turn tacit preferences into examples, ratings and tests of tone and factual discipline. Sources: [[e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11]].
- The reading episode’s [[XFFXFramework]] distinguishes a person’s frame F from event X and result FX. When generated FX proliferates, communicating the author’s method helps others adapt results to their own context; [[ReadingAsFrameTraining]] requires some reading to be done personally, limiting the substitution claim. Sources: [[dushu-jiushi-zai-du-yige-ren-de-f-li4qt9zs2bss4tklnj3yg9y-quo1]].

## Counterevidence & Qualifications
- Interviewing another human is an analogy for eliciting context, not proof that a model understands or cares as an interviewee does.
- Voice recognition and loose phrasing can introduce errors; better communication is necessary for many tasks but not sufficient for reliable model behavior.

## What Changed
- The skill is now framed as an iterative specification-and-review loop rather than one-off prompt optimization.

## Related Concepts
- [[AIEngineeringThinking]] - turns clarified requirements into architecture and test decisions
- [[AgenticWorkflow]] - provides the repeated tool-use setting where ambiguous instructions compound
- [[VibeCoding]] - shows why natural-language task framing must be followed by verification
- [[ContextEngineering]] - stores the selectively retrieved material that carries user intent
- [[HumanJudgmentUnderAI]] - retains responsibility for accepting or rejecting outputs
- [[AIContentDevaluation]] - explains why a reader may dismiss text whose apparent author did not invest in communication
- [[NewSpot]] - is Justin’s concrete agent-built product whose authored daily line preserves his own voice

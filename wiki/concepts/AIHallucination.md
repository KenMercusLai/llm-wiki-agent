---
title: "AI Hallucination"
type: concept
tags: [ai, reliability, verification, judgment]
sources:
  - ep-47-the-ai-pioneer-who-decided-privacy-matters-more-than-hype
  - ep-17-ais-impact-on-creativity-a-consumers-perspective
  - e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67
  - tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128
last_updated: 2026-08-25
knowledge_schema: synthesis-v1
---

# AI Hallucination

## Definition
AI hallucination is plausible-sounding output that is false, unsupported or misgrounded. The term describes an output failure, not a model's subjective experience.

## Current Synthesis
Across consumer, technical and medical uses, fluency can obscure gaps in evidence. Better retrieval, evaluation and domain review can reduce particular errors without making probabilistic systems infallible. Verification effort should rise with decision stakes and the user's inability to catch mistakes.

## Key Claims
- “Hallucination” is a shorthand for output errors, not a human-like mental event or a single removable bug.
- Grounded retrieval and explicit uncertainty improve checking but do not automatically prove a claim true.
- Human expertise and traceable output checks matter in ordinary creative work as well as high-stakes domains.
- Medical use needs patient context, licensed evidence and clinical responsibility rather than consumer-level fact-checking alone.

## Evidence
- **Terminology and verification limits.** [[ep-47-the-ai-pioneer-who-decided-privacy-matters-more-than-hype]] attributes to [[JonathanSchaeffer]] the contrast between bounded, solved [[ChinookCheckers]] and open-ended LLM responses: [[DeterministicAIVerification]] of a game result does not transfer wholesale to language output. His [[KindPrivateAI]] uses local [[RetrievalAugmentedGeneration]], citations and “does not know” responses over private files, but retrieval reduces unsupported answers rather than guarantees correctness. He favors [[AugmentedIntelligence]] under human ownership.
- **Fluent consumer errors.** [[tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128]] has [[ChristopherMims]] of [[HowToAI]] call AI an assistant, not a replacement; he considers errors part of today's systems even as engineers improve them. [[ep-17-ais-impact-on-creativity-a-consumers-perspective]] gives [[MarkDataScienceWithSam]]'s practical countermeasure: edit and fact-check a seven-to-eight-minute [[AIFirstDraftGeneration]] speech, event image, song or [[GoogleAppsScript]] snippet before use. The reported 90-minute to 20–30-minute drafting change is his anecdote, not a measured productivity average. [[AICreativeCollaboration]] and [[AIAssistedLightCoding]] carry different verification needs.
- **Clinical evidence and responsibility.** [[e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67]] contrasts ungrounded health answers with [[OpenEvidence]]'s licensed literature and guidelines, [[EvidenceGroundedMedicalRAG]], and clinician-judged [[HealthBench]] conversations. [[ZhouYebing]] and [[ZhangLu]] emphasize very low tolerance for unsupported claims and a doctor-led [[MedicalAIWorkflowIntegration]]; patient history, privacy and liability are not solved by attaching a citation.

## Counterevidence & Qualifications
- These notes do not estimate a general hallucination rate. [[LegalAIHallucination]] and [[AISearchEvaluation]] are related settings, not evidence that every task shares the same error frequency. [[AIProfessionalDataSecurity]] adds a separate privacy boundary: verification should not require putting sensitive files in an unsuitable consumer tool.
- [[LLMWorldModelGap]] may explain some brittleness, but no source here proves a complete causal theory of all hallucinations.

## What Changed
- Distinguishes the misleading anthropomorphic label from the testable output failure.
- Separates everyday editing, grounded retrieval and clinical oversight by stakes.

## Related Concepts
- [[HumanJudgmentUnderAI]] - locates responsibility for checking consequential output.
- [[OutputQualityGates]] - converts fact and code review into a repeatable acceptance step.
- [[DomainExpertAlignment]] - helps non-specialists route uncertain answers to qualified reviewers.
- [[ExpertiseAmplifiedAIUse]] - explains why experts can spot errors that fluent output hides from novices.
- [[AIVerification]] - broad practice of testing claims before presentation or action.

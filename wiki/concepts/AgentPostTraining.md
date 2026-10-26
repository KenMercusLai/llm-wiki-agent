---
title: "Agent Post-Training"
type: concept
tags: [agents, model-training, post-training]
sources:
  - zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11
  - vol-114-ai-de-2025-he-deepseek-men-de-weilai-duitan-fudan-zhangqi-jiaoshou-lhvhnvqtvuv4ln-cckcpedgldolo
  - 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf
last_updated: 2026-08-17
knowledge_schema: synthesis-v1
---
# Agent Post-Training

## Definition
Agent post-training adapts an already pretrained model to multi-step tool-using tasks through supervised examples, reinforcement feedback, evaluation environments and model–harness interaction. It is not synonymous with polishing chat style or merely appending a skill file.

## Current Synthesis
The sources distinguish simulated/user traces, evaluated environment rollouts, teacher-trajectory imitation, and a strong teacher used only as an RL judge. Each supplies different evidence and governance constraints. Data quality, verifiable task improvement, expert labeling and the base model's prior knowledge remain limiting factors.

## Key Claims
- Chat-optimized SFT/RL does not necessarily train models to maintain state, call tools, recover errors or finish long-horizon agent tasks.
- Environment benchmarks and synthetic trajectories need correctness, difficulty and anti-cheating filters, followed by measured downstream task improvement.
- Imitating a teacher's complete task trajectory differs technically and legally from using that teacher only to evaluate RL outcomes.
- Post-training can refine available capability but cannot reliably unlock knowledge absent from pretraining with a handful of examples.
- Model and harness can be co-adapted, yet changing memory, tools or task protocols does not imply every framework necessarily needs a separate trained model.

## Evidence
- **Task-shaped training:** [[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] has [[LuoFuli]] argue that [[AgentRL|RL]] and SFT must shift from chat responses to simulated users, multiple tool rounds, long-context state and feedback inside [[OpenClaw]] / [[OpenCloud]]-like systems. Memory, [[AISkills|skills]], cost routing and multi-step recovery are [[AgentHarness|harness]] affordances that change the training distribution; her [[MemoVR]] / [[Xiaomi]] work is an interview account, not an independent benchmark. [[ModelHarnessCoEvolution]] is a proposal to iterate both sides of that interface.
- **Data and environments:** [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] records [[MengFanqing]] of [[EvolventAI]] arguing that [[EnvironmentBasedAgentBenchmarks|environments]], [[SyntheticAgentData|synthetic trajectories]], validity/anti-cheating checks, difficulty balance and measured gains form the real data product. His [[RSIData|RSI data]] outlook is a forecast; service-like internal post-training and automatic data generation are not themselves proof of recursive improvement. [[TrainingComputeAllocation]] and [[AgentOptimizedModelArchitecture]] remain economic and model-design constraints.
- **Teachers and provenance:** [[zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1]] distinguishes [[AgentTrajectoryDistillation|whole teacher traces]] from asking a teacher to judge an [[AgentRL]] rollout. Restrictions in service terms and data ownership create [[AIModelDistillationGovernance|governance]] questions; public accusations of distillation and model identity slips are incomplete [[ModelDistillationEvidence|evidence]], not verdicts.
- **Limits and adjacent adaptation:** [[vol-114-ai-de-2025-he-deepseek-men-de-weilai-duitan-fudan-zhangqi-jiaoshou-lhvhnvqtvuv4ln-cckcpedgldolo]] has [[ZhangQi]] argue that small-sample fine-tuning cannot summon knowledge the base model never learned, while expert labels and RL remain costly even under the [[DeepSeek]] efficiency narrative: a [[ModelPostTrainingBottleneck|post-training bottleneck]]. [[e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11]] describes [[TonyContentEngineer]]'s voice-agent dialogue style, follow-up depth and [[ContentEngineering|content engineering]]; this is an [[AIAnswerEvaluation|conversational evaluation]] analogy, not evidence of trained tool trajectories.

## Counterevidence & Qualifications
- The notes do not supply a universal gain rate or demonstrate that one harness-specific model beats all general models. Simulated trajectories can reward shortcuts and fail real tasks unless verified.
- LateTalk's legal/service-terms issue remains disputed; neither a model's self-identification nor a public claim proves a prohibited teacher source was used.
- Conversational voice adaptation and actual agent task completion have different outcome tests; [[VoiceInteraction]] alone cannot validate [[LongHorizonAI|long-horizon]] behavior.

## What Changed
- Distinguished data/environment design, teacher imitation, RL judging and chat-content adaptation.
- Replaced blanket framework-specific training claims with measurable workflow-fit conditions.

## Related Concepts
- [[ModelWorkflowFit]] - Evaluate completion and recovery in the task environment rather than isolated answers.
- [[AICodingVerification]] - Testable coding tasks can provide feedback for agent-training claims.
- [[PersistentAgentMemory]] - External state shapes trajectories without itself updating model weights.
- [[AgentSelfEvolution]] - Skill accumulation and model retraining are separate improvement layers.
- [[MLCoding]] - Automated training-code changes require independent experimental verification.
- [[ResearchTaste]] - Human selection of worthwhile problems remains outside a raw reward score.

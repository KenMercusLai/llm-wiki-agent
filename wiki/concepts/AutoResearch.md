---
title: "Auto Research"
type: concept
tags: [ai, ai-research, agents]
sources:
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1
  - ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1
  - 149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv
knowledge_schema: synthesis-v1
last_updated: 2026-08-09
---

## Definition
Auto Research is AI-assisted research work—reading literature, forming hypotheses, coding and running experiments, interpreting results and iterating. It can accelerate human researchers without proving [[RecursiveSelfImprovement|recursive self-improvement]], in which one research cycle improves the capabilities or methods of the next AI system.

## Current Synthesis
Executable code, kernels, training scripts, benchmarks and environments make [[MLCoding|ML coding]] a strong early substrate for [[AICodingVerification|verification]]: an agent can test an intervention and see feedback. The Q2 2026 [[LateTalk]] discussion frames Auto Research as a step before RSI and cites coding-agent use in frontier labs, but full self-improvement remains unresolved. [[TianYuandong|田渊栋]] says AI can create [[AIResearchFeedbackCompression|compressed idea-to-experiment cycles]] from days or weeks to minutes or hours; reported [[Recursive|Recursive Superintelligence]] NanoChat and operator optimizations demonstrate bounded, verifiable tasks, not a general scientific agent. Humans may still choose worthwhile problems, identify weak evidence, allocate compute, interpret gains and decide whether a result improves a future training loop. [[FrontierModelScaling|Scaling]] is helpful but faces data, compute and energy constraints; whether improvement is smooth or punctuated remains open.

[[MengFanqing|孟繁青]] of [[EvolventAI]] describes increasingly service-like post-training in labs and simulated [[EnvironmentBasedAgentBenchmarks|agent environments]] rather than static question answering. He expects demand for [[RSIData|long-running trajectories]] where models create data, train, evaluate and revise other models, especially after coding pipelines mature. This is not merely copied teacher answers: [[SyntheticAgentData|synthetic trajectories]] need environmental task design, scoring, leakage checks, diversity and hands-on research staff. He calls [[ModelDistillation|distillation]] useful but not the decisive explanation of Chinese model progress, and notes that noisy personal usage traces bring cleaning and compliance limits. A model may improve execution speed long before it acquires research taste or a reliable criterion for what to optimize.

[[LiuZiming|刘子鸣]]'s [[AIForAI|AI-for-AI]] route is more structure-first than brute-force experimentation. [[OPHISResearchWorkflow|OPHIS]] records Observation, Problem, Hypothesis, Intervention and Speed up as process data missing from finished papers; [[MetaModelTrainingCurvePrediction|training-curve prediction]] would estimate outcomes from model, dataset and optimizer before a full compute spend. His [[PhysicsOfAI|physics-of-AI]] and [[MechanisticInterpretability|interpretability]] ambitions seek principles for architecture discovery; [[TrainingAutopilot]] and [[VibeTraining]] remain product horizons, not demonstrated complete research automation. The difference between his “smarter” route and a coding-agent-heavy route is a live research-strategy tension, not a settled winner. [[AIForScience]] can benefit from these loops even without full RSI.

## Key Claims
- Auto Research spans literature, hypothesis, executable intervention, evaluation and iteration; speed alone is not better research direction.
- Code and simulated environments enable measurable early gains, while research taste, verifier quality and task value remain bottlenecks.
- Long-running agent and model-improvement traces need reliable scoring, clean data and leakage controls; distillation alone is insufficient.
- Structured process records and scientific model understanding may improve selectivity over undirected experiment volume.
- Bounded model or kernel optimizations, research assistance and open-ended RSI are different capability claims.

## Evidence
- Frontier-lab framing: [[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1|LateTalk 171]] distinguishes Auto Research from the stronger RSI loop and discusses coding-agent examples as early rather than conclusive evidence.
- Research acceleration boundary: [[yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1|LateTalk 178]] reports Tian's compressed feedback cycles, NanoChat/operator tasks and continuing human taste role.
- Environment and data route: [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi|孟繁青访谈]] describes post-training services, simulated agent scoring, RSI-like trajectories and the limits of simple distillation.
- Structured scientific route: [[149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv|刘子鸣访谈]] presents OPHIS, training-curve prediction, interpretability and his contrast with coding-heavy approaches.

## Counterevidence & Qualifications
Source examples and startup aspirations do not show open-ended autonomous AI research or verified self-improving frontier models. The Q2 review's company and product claims, including its contested Cursor acquisition account, remain source-local and do not prove this concept. Agent benchmarks can be gamed; a faster coding loop can optimize the wrong target. Meng's proposed data demand and Liu's training autopilot are forecasts. Tian and Liu disagree in emphasis about scaling, abstraction and how to discover new methods; neither interview resolves that disagreement.

## What Changed
- Separated execution acceleration, process-data construction and full RSI as different evidence levels.
- Integrated environment-based and physics-of-AI approaches without flattening their disagreement.

## Related Concepts
- [[DiscoveryModel]] - Tian Yuandong's stronger aspiration requires sparse-evidence abstraction and independently checked hypotheses, beyond faster bounded research experiments.
- [[Anthropic]] - the Q2 review cites its reported coding and safety-research agent work as an early, source-local example, not proof of open-ended recursive improvement.
- [[RecursiveSelfImprovement]] - requires a later AI capability gain beyond assisting present research.
- [[MLCoding]] - provides executable early research tasks and tests.
- [[ResearchTaste]] - governs which directions and experiments merit resources.
- [[AIVerification]] - checks whether measured gains are genuine and transferable.
- [[OPHISResearchWorkflow]] - captures research-process data that final papers omit.
- [[RSIData]] - denotes long-running improvement trajectories proposed for future training.

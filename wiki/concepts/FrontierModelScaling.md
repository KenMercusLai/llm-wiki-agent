---
title: "Frontier Model Scaling"
type: concept
tags: [models, scaling, infrastructure]
knowledge_schema: synthesis-v1
sources:
  - yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1
  - tech-20251215-1215-mp-tech-pod-128-tech-20251215-1215-mp-tech-pod-128
  - duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe
  - na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr
  - 131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan
  - ni-you-yi-ba-nenggou-wa-chu-jinzi-de-chanzi-kending-buhui-xian-gei-bieren-yong-duitan-kaiwuji-lu-ziheng-yong-ai-faming-xin-cailiao-lvhl1-hy1gwtainujjgf8xbs4fyh
  - biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1
  - ba-ai-chuicheng-hewuqi-de-ren-qinshou-laxiale-xinlengzhan-tiemu-1
  - 133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42
  - 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe
  - 140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h
  - 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf
last_updated: 2026-08-08
---

## Definition
Frontier model scaling is the effort to improve capability through model size, computation, data, architecture, post-training, evaluation and deployment feedback. No single variable or claimed threshold is a verified universal recipe.

## Current Synthesis
The registered interviews do not resolve whether scaling has hit a wall. [[GaryMarcus]] and several world-model founders argue that text prediction misses causal or physical structure; [[YaoShunyu]] counters that saturated benchmarks, bugs and poorly specified tasks can masquerade as stagnation. [[YanJunjie]] and [[LuoFuli]] expect large base models to remain valuable but emphasize data and agent-specific post-training. Material and robot cases shift the question from internet-text volume to experiments, simulation, expert feedback and task validity. These are competing practitioner judgments rather than a controlled industry comparison.

## Key Claims
- Compute and data can improve models, but training efficiency, architecture and data quality constrain the benefit of sheer scale.
- A plateau diagnosis cannot be inferred from public benchmarks or subjective release impressions without checking task design, bugs and time horizons.
- Agent workloads shift scaling resources toward post-training, long-context use, tool-feedback environments and repeatable evaluation.
- Physical-world scaling requires representation, causal or predictive dynamics, simulation and scarce embodied data; the proposed routes disagree.
- In materials discovery, generalization is only useful when candidate predictions survive expert screening, experiment and manufacturing tests.
- Training expenditure also depends on commercialization, organizational coordination and access to useful terminal feedback.

## Evidence
- Quantitative ambition with limits: [[duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe]] has [[YanJunjie]] argue that experience training at 3T scale and substantially more high-quality data would be needed before a possible 10T-scale model; the registered note does not establish an exact token budget or a measured U.S.–China generation gap. He also says model and [[ModelHarnessCoEvolution|agent harness]] improve one another, while verification still matters when coding becomes cheap. [[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] has [[LuoFuli]] call 1T-plus parameters an entry ticket but prioritize [[AgentPostTraining]], [[AgentRL]], attention/KV-cache tradeoffs, rollouts and [[TrainingComputeAllocation]] for [[OpenClaw]]/[[OpenCloud]] workflows. Neither interview supplies a universal minimum.
- Wall versus experimental error: [[tech-20251215-1215-mp-tech-pod-128-tech-20251215-1215-mp-tech-pod-128]] has Marcus argue that later gains look more incremental than 2020–23 leaps and call for explicit entity and state representation; [[140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h]] has Yao contest a premature wall, citing benchmark saturation, bugs, wrong data and short token horizons. His “train with finite context, use as infinite context” proposes memory, retrieval and selective forgetting for [[LongHorizonAI]]. [[yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1]] has [[TianYuandong]] accept useful scale while arguing that compute, energy and data may yield plateaus plus new methods; rapid verifiable coding experiments are not proof of full [[RecursiveSelfImprovement]]. [[biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1]] uses [[ChatGPT]] and other model releases as timing markers for the hosts' impression of scaling constraints, not as a controlled comparison or evidence for a specific release-to-release plateau.
- Distinct world-model paths: [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] has [[HuangBiwei]] propose causal variables, causal structure and action-conditioned dynamics, with [[AetherAI]] discussing roughly 7,000–8,000 training hours and about 400 GPUs as an early plan. [[133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42]] has [[XieSaining]] favor predictive [[RepresentationLearning]] and [[AMILabs]]' partner data rather than tokenized video; this is not identical to an explicitly causal-variable recipe. [[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] has [[XieChen]] emphasize costly real robot data, a pyramid of simulation and first-person data, failure correction and [[RoboticsSimulationEvaluation]]; his prioritization differs from real-robot-first accounts.
- Materials test: [[ni-you-yi-ba-nenggou-wa-chu-jinzi-de-chanzi-kending-buhui-xian-gei-bieren-yong-duitan-kaiwuji-lu-ziheng-yong-ai-faming-xin-cailiao-lvhl1-hy1gwtainujjgf8xbs4fyh]] records [[LuZiheng]]'s reading of [[MatterSim]] property generalization and [[MatterGen]] generative potential. For [[Kaiwuji]], predictions still pass scientist filtering, gram/kilogram experiments and customer-line trials; expensive AI talent and training precede revenue. His free-energy prediction milestone is a future goal, not demonstrated process replacement.
- Business and organizational loop: [[131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan]] has [[YinQi]] argue [[StepFun]] needs top-tier models plus [[AIPlusTerminals]] such as car cabins, phones and eventually robots to finance research and capture feedback; his five-to-seven-year physical-data horizon and multi-billion annual profit ambition are forecasts. [[ba-ai-chuicheng-hewuqi-de-ren-qinshou-laxiale-xinlengzhan-tiemu-1]] is a policy-heavy, rumor-qualified discussion of good-enough [[GLM52]] alternatives and does not demonstrate a scaling plateau.

## Counterevidence & Qualifications
Neither size targets nor data-hour figures are cross-lab validated thresholds. Marcus, Huang, Xie Saining and Yao propose differing definitions of a useful world model; treat none as an established LLM successor. Source opinions on progress speed and open-model substitution are time-stamped and not comparable under one metric; the registered MiniMax note does not establish a numerical regional model gap. Robotics data recipes and simulations need real-world transfer tests. Scale alone does not establish return on training capital or beneficial deployment.

## What Changed
- Replaced a serial catalog of twelve viewpoints with technical bottlenecks and explicit disagreements.
- Separated interviewee numeric targets from validated thresholds and excluded the rumor-heavy policy aside as plateau proof.

## Related Concepts
- [[AIOrganizationDesign]] - StepFun's terminal partnerships make training scale an organization and distribution problem.
- [[LLMWorldModelGap]] - Marcus questions whether text-scale gains yield sufficient physical and causal models.
- [[MultimodalIntelligence]] - Xie Saining's representation-first path extends beyond text pretraining.
- [[EmbodiedDataPyramid]] - Xie Chen's simulation, first-person and robot data tiers pose distinct scale limits.
- [[AgentOptimizedModelArchitecture]] - Luo Fuli's long agent workflows require attention and cache choices beyond parameter count.
- [[DecentralizedWorldModelStrategy]] - AMI's partner-data approach contrasts with centralized internet-scale training.
- [[AIResearchFeedbackCompression]] - Tian's verifiable coding loop may shorten research experiments without proving recursive improvement.
- [[MechanisticInterpretability]] - evaluation and understanding remain separate from benchmark scaling gains.
- [[DataAsEducation]] - Xie Chen frames curated failure and correction as more valuable than indiscriminate data accumulation.
- [[ProblemDefinitionInResearch]] - Yao disputes simplistic scaling walls when evaluations are misdefined.
- [[AICommercializationPressure]] - StepFun's terminal business aims to finance costly frontier research.
- [[AIExportControls]] - perceived risk can limit access even when technical scaling continues.
- [[EmbodiedAI]] - robot training needs physical feedback unlike web-scale text pretraining.
- [[OpenSourceAIModels]] - good-enough downloadable competitors may change demand without leading closed-model benchmarks.
- [[LargeCompanyOpenSourceStrategy]] - open release changes competitive access to scaled models rather than establishing technical parity.
- [[MLCoding]] - Yao's AI-assisted machine-learning work motivates his emphasis on problem definition.
- [[MiniMax]] - Yan's organization is the origin of the reported 3T/10T/200T scale projections.
- [[MemoVR]] - Luo Fuli's reported agent-era context gives the 1T-plus claim its workflow setting.
- [[Recursive]] - Tian's research-program context must not be mistaken for observed recursive self-improvement.
- [[WorldModels]] - contested alternative or complement to text-only scaling.
- [[CausalWorldModels]] - Huang's physical-dynamics route, distinct from predictive representation learning.
- [[DataRecipeCoCreation]] - experiments that identify which training and feedback mix matters.
- [[ModelHarnessCoEvolution]] - agents and model training supplying feedback to one another.
- [[AgentPostTraining]] - training regime for long tool-using workflows.
- [[AIInferenceCostStructure]] - downstream expense that constrains apparent training wins.
- [[LongChainAICompetition]] - ability to finance, organize and commercialize a model program over time.
- [[AIMaterialsDiscovery]] - domain where model scale needs experimental and industrial validation.

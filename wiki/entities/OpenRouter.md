---
title: "OpenRouter"
type: entity
tags: [ai, infrastructure, model-routing]
sources:
  - vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1
  - all-in-with-chamath-jason-sacks-friedberg-more-trillion-dollar-ipos-anthropic-3t-zucks-price-war-china-ends-open-source-trump-accounts-42041390
  - featherless-ai-when-your-weekend-experiment-makes-more-than-your-startup
  - e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41
last_updated: 2026-08-24
knowledge_schema: synthesis-v1
---

# OpenRouter

## Overview
OpenRouter aggregates model access and routes requests across providers; its value depends on model choice, price and switching costs, unlike direct model hosting.

## Current Profile
The service gives users one routing layer across models and provider APIs, reducing switching friction as prices and capabilities change. Featherless’s founder distinguishes that intermediation from hosting models directly; a buyer’s claimed savings illustrate a possible use, not a general benchmark.

## Key Characteristics
- Multi-provider model access.
- Provider/host distinction.
- Buyer-side cost optimization.

## Evidence
- **跨模型路由：** [[KeithZhai]]把OpenRouter视为开放和封闭模型并存时受益的API聚合层：用户可按价格、质量、延迟和任务需要切换[[OpenSourceAIModels|开放模型]]与闭源服务，而非依赖一个接口。另一节目称它是观察[[DeepSeek]]、[[OpenAI]]、[[Anthropic]]、[[Kimi]]等模型实际付费使用和价格变动的“中转站”；[[KimiK3|Kimi K3]]等选项扩展时，长提示词、缓存和重复步骤的[[AgentInferenceWorkload|代理负载]]更凸显[[ModelRoutingCostControl|路由成本控制]]，但流量观察不等于经审计的市场份额。[[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] [[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]]
- **路由与托管的边界：** [[EugeneChia]]说[[FeatherlessAI]]和OpenRouter对用户都提供多模型入口，但前者直接托管模型（包括[[LongTailModelHosting|长尾模型]]和[[GPUHotSwapping|GPU切换]]），后者把请求路由到Featherless等供给方；两者的价格或模型数量不可直接当成同一层级指标。[[featherless-ai-when-your-weekend-experiment-makes-more-than-your-startup]]
- **买方成本实例：** [[ChamathPalihapitiya]]称团队结合OpenRouter、[[GLM52|GLM 5.2]]及其他路由选择，将模型费用降低约95%；这是其团队的一次[[EnterpriseAIROIAudit|企业ROI]]经验，并非OpenRouter平台客户的普遍节省率。[[all-in-with-chamath-jason-sacks-friedberg-more-trillion-dollar-ipos-anthropic-3t-zucks-price-war-china-ends-open-source-trump-accounts-42041390]]

## Qualifications
- The roughly 95% saving is Chamath’s team-specific anecdote, not a platform benchmark; model prices, traffic and rankings change. Featherless hosts models while OpenRouter routes to hosts.

## What Changed
- The router is distinguished from a hosting provider even when both offer multi-model access.
- The reported buyer saving is treated as a single team’s outcome, not a platform-wide claim.

## Relationships
- [[ModelRoutingCostControl]] - user/product-level routing practice OpenRouter exemplifies.
- [[AIInferenceCostStructure]] - token-price and provider-cost layer that makes routing valuable.
- [[OpenSourceAIModels]] - model diversity and API moat pressure behind its opportunity.
- [[KimiK3]] - model diversity and API moat pressure behind its opportunity.
- [[ClosedModelAPIMoatPressure]] - model diversity and API moat pressure behind its opportunity.
- [[AgentInferenceWorkload]] - agent workloads can make routing more valuable because long prompts, cache reuse, and repeated steps create cost differences.
- [[FeatherlessAI]] - direct-hosting counterpart to OpenRouter’s routing layer.
- [[LongTailModelHosting]] - direct-hosting counterpart to OpenRouter’s routing layer.
- [[GPUHotSwapping]] - direct-hosting counterpart to OpenRouter’s routing layer.
- [[DeepSeek]] - model supplier or pricing issue that motivates multi-provider routing.
- [[OpenAI]] - model supplier or pricing issue that motivates multi-provider routing.
- [[Anthropic]] - model supplier or pricing issue that motivates multi-provider routing.
- [[Kimi]] - model supplier or pricing issue that motivates multi-provider routing.
- [[PeakValleyAIInferencePricing]] - model supplier or pricing issue that motivates multi-provider routing.
- [[AISubscriptionEconomics]] - model supplier or pricing issue that motivates multi-provider routing.

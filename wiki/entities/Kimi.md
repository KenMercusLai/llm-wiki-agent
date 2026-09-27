---
title: "Kimi"
type: entity
tags: [ai, model, china]
sources:
  - vol-171-jiaru-women-you-wuxian-token-1-6682-1
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1
  - e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41
  - 148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims
  - 136-quanqiu-da-moxing-jibao-di-9-ji-he-guang-miliao-coding-shi-agi-di-er-mu-guigu-yusanjia-zhenxiang-moxing-zheng-chengwei-xin-yidai-os-lh-cqyoss-dztmyb5kmbjapa6w9v
  - bie-zai-guonei-juan-le-qu-meiguo-kankan-zhiyao-chanpin-hao-jiu-you-ren-fufei-de-shichang-keji-luandun
  - ep117-doubao-yuehuo-guoyi-ali-zaizao-qianwen-shibushi-wanle-lmp0pzdig2ijow5k3cnnnvvqq6sa
  - vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1
  - vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy
  - ai-fazhanle-4-nian-ba-yingyong-fazhan-meile-ai-nianzhong-fupan-lgtuy-eszlci5yaguocyndigwmlx
  - ai-bu-zhi-bi-zhishang-waic-he-kimi-k3-toulule-shenme-xin-jingzheng-1
last_updated: 2026-08-16
knowledge_schema: synthesis-v1
---

# Kimi

## Overview
Kimi是[[MoonshotAI|月之暗面]]的模型及产品系列。来源一方面把它当作国内模型选择和编码助手，另一方面借Kimi K3讨论架构、开放权重、推理成本及agent环境。

## Current Profile
Kimi不能仅按“便宜的替代模型”理解：K3的混合注意力、专家路由、后训练和沙箱说明系统工程的重要；实际工作流仍须比较速度、价格、额度和可复核性。中国模型进步是否靠蒸馏、开放权重能否削弱闭源API护城河，均是受访者的解释而非单一已定论。

## Key Characteristics
- 计算约束下的架构与效率路线：Kimi Linear/KDA结合周期性全局注意力，MoE路由和训练稳定性设计服务长上下文与代理负载。
- K3是训练、服务与环境协同案例：可验证的内核开发agent、MOPD后训练、AgentIn隔离与部分轨迹支持长任务，而不只是模型权重发布。
- 开放权重与商业许可并行：公开权重和部分组件，仍保留训练环境、完整配方等；许可试图限制高收入模型服务商搭便车。
- AI编码及CLI面向高价值任务：Kimi CLI由RC回顾为可扩展agent harness，编码或代理任务比泛用消费聊天更容易展示付费价值，但竞争尚未定型。
- 在多模型工作流中担当成本/场景选项：订阅、Kimi Code、OpenClaw和路由工具可替代昂贵API的部分任务，速度和审核成本仍约束选型。
- 海内外采用依靠产品合适度：美国创业者被受访者描述为按成本/性能评价中国模型，vLLM社区则将Kimi列为模型/推理协作对象；均非普遍市场接受度证明。

## Evidence
- **架构不等于蒸馏**：[[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]]与[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]]分别记录[[MengFanqing|孟繁青]]的效率解释及K3的[[KimiLinear]]、[[KimiDeltaAttention|KDA]]、稀疏专家与长上下文代价：降低部分缓存压力却增加prefix复用与回滚复杂性。
- **可重复研发与权重边界**：[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]]记[[KernelDevelopmentAgents]]、[[AgentIn]]、[[MOPDPostTraining]]与量化平衡、per-head Muon等；权重、MTP、Flash KDA和AgentIn开放，原始专家checkpoint、IO环境及全配方不开放。
- **生态/许可**：[[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]]把[[KimiK3]]商业许可、[[ModelSovereignty|模型主权]]、路由及[[OpenModelSafetyGovernance|开放模型安全治理]]并论；蒸馏技术与指控抄袭须分清。[[ai-bu-zhi-bi-zhishang-waic-he-kimi-k3-toulule-shenme-xin-jingzheng-1]]所述7月27日开放权重是录制时预期，不等于训练流程开源。
- **CLI与高价值任务**：[[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]]中[[RC]]回忆[[KimiCLI]]的[[AgentHarness]]可延展至SDK/Web/IDE；[[ep117-doubao-yuehuo-guoyi-ali-zaizao-qianwen-shibushi-wanle-lmp0pzdig2ijow5k3cnnnvvqq6sa]]认为编码较普适助手更易付费。[[136-quanqiu-da-moxing-jibao-di-9-ji-he-guang-miliao-coding-shi-agi-di-er-mu-guigu-yusanjia-zhenxiang-moxing-zheng-chengwei-xin-yidai-os-lh-cqyoss-dztmyb5kmbjapa6w9v]]则把Kimi与[[MiniMax]]、[[ZhipuAI]]、[[Doubao]]并列为向[[Anthropic]]式高价值任务、[[ModelAsOperatingSystem|模型平台]]探索的国内选手。
- **费用/延迟的实测语境**：[[ai-bu-zhi-bi-zhishang-waic-he-kimi-k3-toulule-shenme-xin-jingzheng-1]]的主持人用K3按需求做播客主持人对话代理并发现多主题提纲设计问题，一次运行约三小时、25万token；[[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]]将部分[[OpenClaw]]任务改走Kimi Code月费方案。[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]]与[[vol-171-jiaru-women-you-wuxian-token-1-6682-1]]比较[[Codex]]、[[ClaudeCode]]、[[DeepSeek]]、[[OpenRouter]]和Kimi的成本、额度、审核与[[UnlimitedTokenWorkflow|“无限token”工作流]]。
- **部署和竞争情境**：[[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]]记[[YuKaichao|游凯超]]建设[[VLLM|vLLM]]中国社区时拜访Kimi等模型用户；[[bie-zai-guonei-juan-le-qu-meiguo-kankan-zhiyao-chanpin-hao-jiu-you-ren-fufei-de-shichang-keji-luandun]]中[[Win]]叙述美国创业者的成本/性能选择；[[vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1]]以[[ModelWorkflowFit|工作流匹配]]而非榜单选模型；[[ai-fazhanle-4-nian-ba-yingyong-fazhan-meile-ai-nianzhong-fupan-lgtuy-eszlci5yaguocyndigwmlx]]中[[QuKai]]将Kimi与[[OpenAI]]、豆包列为聊天阶段代表，却认为编码阶段[[Anthropic]]、智谱更直接受益，Kimi仍须在[[AgenticWorkflow|代理工作流]]证明追赶能力。

## Qualifications
- 上文孟繁青来源链接应以本页frontmatter中的确切键为准；蒸馏是否发生不能靠模型自称Claude等身份污染判定，K3开权重也不等于公开全模型工厂。
- “冲击Anthropic估值”是节目对投资者反应的归因，不是因果证明。K3三小时/25万token仅一次主持人测试，不能推广为平均性能；低价也不等于低总任务成本。
- 2026年不同来源阶段各异：QuKai说Kimi在编码追赶，是其当时判断；AGI三幕和模型成为OS是嘉宾前瞻。Win美国体验、vLLM拜访及RC原工作均非份额/营收验证。
- [[SyntheticAgentData]]与[[RSIData]]是孟繁青讨论的下一阶段数据路线，不应说成Kimi已经实施的公开事实；[[SpeechToTextCostOptimization]]的转录费用示例属于同一节目其他服务，非Kimi计价。

## What Changed
- 将零散的模型清单整合为架构/环境、许可生态、编码产品与工作流成本四个互相牵制的层次。
- 对开放程度、实测延迟与商业胜负分别标注来源和推论界限。

## Relationships
- [[ModelDistillation]] - 关于国内模型进步的竞争解释，不等于Kimi能力的已证实唯一来源；[[EvolventAI]] - 提出效率解释的受访者公司。
- [[OpenWeightCommercialLicensing]] - K3权重传播和商业服务再利用之间的规则；[[OpenWeightReleaseBoundary]] - 权重与完整研发栈的界线。
- [[ModelRoutingCostControl]] - 使用Kimi分担不同价格/任务负载；[[ModelWorkflowFit]] - 速度、审核与配额的选择标准。
- [[AgentOptimizedCLI]] - Kimi CLI的agent友好接口；[[AgentFacingInterfaces]] - CLI向其他交互表面的延展。
- [[VibeCoding]] - 编码场景；[[AICodingVerification]] - 长运行产物仍需人工检查。
- [[TopModelBuildRuntimeSplit]] - 顶级模型建工具、便宜模型跑常规工作流的主持人建议；[[WAIC]] - K3测试节目的展会背景。
- [[OpenSourceAIInfrastructure]] - vLLM所在的独立服务层；[[Qwen]] - 中国模型对照选项；[[AGIThreeActs]] - 受访者的聊天到编码阶段论。
- [[AIApplicationMarketTrough]] - QuKai判断应用投资低谷的背景，非Kimi单体业绩。

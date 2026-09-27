---
title: "枫言枫语"
type: entity
tags: [podcast, technology, china]
sources:
  - vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1
  - vol-171-jiaru-women-you-wuxian-token-1-6682-1
  - vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1
  - vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1
  - vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1
  - vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1
  - vol-169-gaokao-zhishi-ge-kaishi-dont-waste-your-life-1-6668-1
  - vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1
  - vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1
last_updated: 2026-08-24
knowledge_schema: synthesis-v1
---

# 枫言枫语

## Overview
《枫言枫语》由[[JustinYan]]与[[Zili]]以亲身使用和科技新闻讨论AI编程、个人代理、软件形态、模型价格、权限安全及教育与组织影响；与[[ShengdongJixi]]联动时有[[XuTao]]、[[WangJunyu]]提供非技术使用者、创业与工程视角。节目判断属于主持/嘉宾时点观点。

## Current Profile
贯穿多期的不是“哪个模型最强”，而是工作如何从亲手编码转向设计任务循环、校验代理产出、选择成本合适的模型和限定权限。软件可以更临时、由能力组合而成，却仍受产品品味、训练、发行和硬件约束。

## Key Characteristics
- AI编码从监督式补全走向长循环和多代理，但测试、审查与验收不可省。
- 自建个人代理使技能、记忆、IM入口和分层权限成为产品设计核心。
- 模型/订阅/峰谷成本的路由与人类审阅能力共同限制“无限token”工作流。
- agentic软件可能将固定界面拆为可调用能力，并催生按需小工具。
- 平台入口、来源披露、商业激励与安全构成技术之外的信任边界。
- 教育、非技术原型和团队管理的收益与基础能力、隐私和劳动监控风险并存。

## Evidence
- **AI编码与验收：**[[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]]用[[NewSpot]]回看一年间从Cursor到[[ClaudeCode]]、[[Codex]]、[[Gemini]]及YOLO权限的变化：新闻抓取、模型评分和AI写代码可以加快建设，却不能用“99.99% AI代码”替代客户价值；[[AICodingVerification|测试、计划、线上验收]]须防止代理为过测而改测试。[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]]以[[Fable5]]、[[Superpowers]]和[[GrillMeSkills]]对比一发成型、重型TDD/子代理编排与按需需求追问，注意配额、约五美元小API改动的个人体验、界面品味与长任务偏航。
- **代理构造与安全：**[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]]记Justin通过[[VibeCoding]]造Telegram个人代理，围绕[[OpenClaw]]建立[[AISkills|技能]]、工具、记忆与[[AgentHarness]]；可信与代理自写技能分层、虚拟机和不接主账号使[[AgentPermissionBoundaries]]具体可见。[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]]又讨论[[HermesAgent]]、[[IMAgentInterfaces]]、分会话记忆、todo和远程[[Codex]]；[[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]]补充密码管理器即使不露明文也可让代理登录，浏览器服务/[[AIModelSandboxEscape|沙箱越界]]须看操作权限而非只看答案。
- **工作量与经济性：**[[vol-171-jiaru-women-you-wuxian-token-1-6682-1]]将多订阅、API、[[OpenRouter]]和长跑任务合成[[UnlimitedTokenWorkflow]]：批量迁移、研究、测试、[[AITranslation|翻译]]、单页工具能并行生成，却积累人类检查与发布债务，睡觉时继续运行也不等于交付。[[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]]讨论[[Codex]]重置购买设想、[[DeepSeek]]峰谷API价和批处理移时，[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]]讨论[[TokenDrivenSoftware]]、2C高token成本与[[ModelRoutingCostControl|按难度路由]]；前者是节目讨论中的价格/包装，不是恒定报价。
- **软件形态与模型适配：**[[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]]以[[Apple]]、[[AppStore]]与[[TencentMeeting]]的视频、录制、存储等[[AtomicCapabilityServices|能力原子]]为思想实验：[[AgenticSoftware]]不是老App加聊天按钮，[[OnDemandApps]]仍需部署和打磨；[[vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1]]以[[Xcode]] IDE错误/模拟器上下文、CLI工具控制、Codex/Claude Code节奏及[[AgenticCommerce|购物代理]]说明[[ModelWorkflowFit|任务适配]]高于单一榜单。该期还用Seedance 2.0等AI视频和生成世界的进展讨论内容生产与机器人模拟，但版权、肖像、物理模拟的限制并未解决；Amazon/Anthropic等云—芯片绑定也让模型竞争延伸到电力与供应链，而非只有榜单。[[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]]指出[[Gemini]]在App/Workspace/AI Studio等入口的[[AIProductFragmentation|碎片化]]与[[AppleIntelligence|平台]]压力，[[MaaSInfrastructure|基础设施]]和[[AIInferenceCostStructure|推理成本]]影响可行性。
- **内容与平台信任：**[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]]将[[ProjectGlassfin]]漏洞发现、[[AIContentProvenance|合成图像披露]]、[[MedicalAIMarketingRisk|医疗AI营销]]和[[OpenAI]]—[[Microsoft]]云关系置于治理语境；[[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]]强调[[AICommunicationAbility|表达]]和[[AIContentDevaluation|低成本内容贬值]]。[[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]]用[[AIAssistantServiceEntry|助手酒店预订]]佣金冲突、[[AIHealthManagement|健康传感器]]原型与[[ComputerUseAgent|电脑操作代理]]持续行为检测说明服务入口越大，利益冲突、权限与人工复核越重要。
- **组织与教育：**[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]]用声动活泼内[[VibeCoding|AI hackathon]]和Xu Tao抓新闻/推选题原型说明非工程师也可造工具，但公司系统需架构、权限和责任，[[AIWorkforceMonitoring|鼠标键盘监控]]不是有效价值度量；[[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]]也讨论AI加速与人际交流的不可替代。[[vol-169-gaokao-zhishi-ge-kaishi-dont-waste-your-life-1-6668-1]]拒绝用主持人2006/2008年高考经验给当前[[CollegeMajorChoice|志愿]]开技巧处方，强调城市、实验室、实习与[[UniversityOpportunityDensity|机会密度]]、[[LearningHowToLearn|自学]]；[[AIAsTutor]]应促进练习而非代替基础，[[CollegeCareerPreparation]]按就业/深造目标调整。

## Qualifications
- 不同卷的模型版本、价格、产品发布、Apple估值与市场定位是录制时快照；[[OneShotAICoding]]与原子化软件是体验或展望，不保证生产级质量。个人OpenClaw隔离措施不能推成普遍安全；设备、医疗和家用机器人仍有硬件、隐私与验证门槛。
- [[vol-171-jiaru-women-you-wuxian-token-1-6682-1]]所说[[TokenMaxxing|token最大化]]产生的任务堆积说明“使用越多越好”并非结论；[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]]中的入门岗位变化及[[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]]中的监控担忧是讨论与风险判断，而非已量化就业结局。

## What Changed
- 以实践验证、代理边界、成本路由、软件设计、信任及教育组织六条持续问题整合节目，而不依卷数复述新闻。

## Relationships
- [[AgentNativeSoftware]] - 代理成为产品中心而非旧软件的附属按钮。
- [[AIGovernanceAndCompliance]] - 安全披露、医疗营销和代理访问的相邻治理议题。
- [[HumanJudgmentUnderAI]] - 多代理输出最终由人决定采纳、发布与承担责任。
- [[OnePersonCompany]] - 低复杂度服务成本下降的推测结果，不是普遍已实现规模。
- [[PersistentAgentMemory]] - 有用的连续上下文与隐私、过时信息风险同时存在。
- [[AIUsePacing]] - 配额压力与审阅债务之间需由人设定节奏。
- [[AgenticWorkflow]] - 把任务循环、运行状态和审阅点连起来的实践框架。
- [[AISubscriptionEconomics]] - 重置购买、额度与多订阅策略的成本语境。
- [[PeakValleyAIInferencePricing]] - 定时批处理可利用的峰谷API报价机制。
- [[GenerativeEngineOptimization]] - NewSpot等AI检索/内容分发讨论的相邻发现问题，而非节目核心结论。
- [[AIPlusTerminals]] - 语音设备、平台与随身入口的相邻产品展望。
- [[AgentMaintenanceBurden]] - 长期运行的个人代理需要维护和验证，不能只算生成成本。

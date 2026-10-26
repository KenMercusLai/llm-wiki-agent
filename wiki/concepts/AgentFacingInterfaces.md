---
title: "Agent-Facing Interfaces"
type: concept
tags: [agents, interfaces, cli, product-design]
sources:
  - 11-nian-110-yi-meijin-ranhou-ne-duihua-airwallex-wu-kai-ai-shidai-xiayizhan-1000-yi-lr4tvdrq25by7fugoqkqojw6vwdk
  - e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923
  - 263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs
  - 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto
  - agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b
  - renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o
  - tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3
  - dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd
  - weishenme-gongsi-yong-buhao-ai-cong-jiaolv-dao-xingdong-de-3-ge-guanjian-dongzuo-duitan-bairong-zhineng-zhang-shaofeng-lgarngnaqran2c9p4jssurvt6ces
  - ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan
  - vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1
  - biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1
  - ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax
  - agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq
  - weishenme-manus-bixu-chuhai-liaoliao-guochan-da-moxing-de-wenkesheng-kunjing-keji-luandun
  - women-ba-ai-sai-jin-huadian-hou-cai-zhidao-ai-luodi-you-duo-zang-1
  - vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1
  - 139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no
  - guanyu-ai-kaiyuan-shangyehua-yu-quanqiuhua-de-jingyan-jiaoxun-he-fangfalun-duitan-pingcap-cto-dongxu-ljw8va0evobhz4ojzrulqzjvxw5
  - yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy
last_updated: 2026-08-07
knowledge_schema: synthesis-v1
---
# Agent-Facing Interfaces

## Definition
Agent-facing interfaces are tool and data contracts that let software agents discover, invoke, observe and recover actions in existing services. A chat or autocomplete surface for the *human* is not itself an agent-callable contract.

## Current Synthesis
CLI, APIs, skills, structured workspaces and event streams can each expose actions to agents; a graphical interface remains valuable for human inspection and existing business workflows. Which surface is useful depends on action granularity, context, permissions and a recoverable result, not on one universal protocol.

## Key Claims
- Atomic, discoverable, idempotent actions with structured output and actionable errors reduce fragile guessing and allow agent workflows to recover.
- Legacy enterprise systems and regulated finance need callable operations plus governed data access and explicit action authority, not a decorative chatbot.
- Agent-readable files and events can be interfaces alongside CLI and APIs, while dual human/agent views retain reviewability.
- Human IM, autocomplete and GUI are complementary presentation and verification surfaces, not replacements for executable tools.
- When formal APIs are closed or absent, constrained operational capture may bridge a particular workflow but introduces permission, accuracy and maintenance limits.
- Agent distribution changes product incentives: vendors can become callable capability suppliers, while closed platforms may defend the end-user entry point.

## Evidence
- **Executable tool contracts:** [[ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax]] gives [[Podwise]]'s [[AgentOptimizedCLI|CLI]] checklist: discover capabilities before acting, atomic commands rather than mirroring the whole SaaS GUI, pipeable text, separate structured machine output, idempotency, noninteractive authentication, examples and recoverable errors. [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]] records [[LaiXinlu]]'s argument for composable Unix/CLI patterns in an [[AgentHarness]], not a measured proof that CLI always beats MCP; his [[KComputer]] is ShareAI's proposed lightweight virtual-computer execution substrate, not itself a universal CLI benchmark. [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] presents [[HermesAgent]] skills plus CLI as shareable user tooling. [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]] extends this with [[RC]]'s [[KimiCLI]] and agent-readable event IDs, summaries and thread state in [[SlockAI]] while people see channel progress.
- **Enterprise and finance:** [[weishenme-gongsi-yong-buhao-ai-cong-jiaolv-dao-xingdong-de-3-ge-guanjian-dongzuo-duitan-bairong-zhineng-zhang-shaofeng-lgarngnaqran2c9p4jssurvt6ces]] makes [[BairongIntelligence]]'s [[DigitalEmployees|digital employees]] dependent on legacy CRM/order/office APIs. [[guanyu-ai-kaiyuan-shangyehua-yu-quanqiuhua-de-jingyan-jiaoxun-he-fangfalun-duitan-pingcap-cto-dongxu-ljw8va0evobhz4ojzrulqzjvxw5]] has [[Dongxu]] describe governed [[PingCAP]] / [[TiDB]] context and database access. [[11-nian-110-yi-meijin-ranhou-ne-duihua-airwallex-wu-kai-ai-shidai-xiayizhan-1000-yi-lr4tvdrq25by7fugoqkqojw6vwdk]] records [[WuKai]]'s [[AirwallexAgentOS]] proposal to expose payment and financial workflows to customer agents; permissions, confirmation and audit are part of [[AgentIdentityAndAuthentication|authorization]], not an afterthought. Vendor descriptions do not verify safety or scale.
- **Workspace and ambient contexts:** [[agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq]] describes [[Moxt]]'s [[AINativeWorkspace|Markdown/CSV/JSON workspace]] as agent-readable state. [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]] explores [[Paperboy]] OS-wide autocomplete and meeting preparation based on [[OSLevelContext]]; it is primarily a human-assistance surface, not a callable API. [[e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]] interviews [[PeterCreo]] and [[ChenKaiCreo]] among the Creo guests and describes [[Creo]]'s hypothesis that agents may become first readers of SaaS data, requiring agent-readable tasks and permissioned access as [[AIFirstOrganization|organizations]] adapt. The note attributes distinct harness and organizational claims to the two guests, not this particular product-consumer claim to both individually.
- **Human entry and review:** [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] separates [[IMAgentInterfaces|IM]] from [[LocalAgentExecution|local tools]], memory and skills in [[OpenClaw]]. [[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]] compares [[ClaudeCode]] and [[GeminiCLI]] execution with [[Cursor]]'s GUI for diff selection and rollback. [[139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]] has [[SuYu]] defend graphical knowledge, trust and audit while forecasting a [[UniversalDigitalAgent|cross-surface digital agent]]; that future convergence is not a current universal interface. [[agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b]] uses [[CangShifu]]'s FFmpeg example to argue for [[HeadlessSoftware|callable productivity tools]] without abolishing review GUIs; [[TianjieJack]]'s investor thesis is to avoid GUI-first productivity designs, not to abolish human visual review. [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] discusses [[Google]]/[[Gemini]] browser entry, [[Apple]]/[[Siri]] OS entry and [[Cloudflare]] operating infrastructure: reachability matters, but each claim is a source-time expectation.
- **Product capabilities and distribution:** [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] imagines [[TencentMeeting]] video, recording and media as [[AtomicCapabilityServices|atomic capabilities]] recomposed by an agent; it is a design thought experiment. [[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]] discusses [[Meitu]]'s [[ToAgentDistribution|skills distribution]] instead of only developer APIs. [[weishenme-manus-bixu-chuhai-liaoliao-guochan-da-moxing-de-wenkesheng-kunjing-keji-luandun]] contrasts agent access to overseas browser/SEO/paid-software workflows with [[WeChat]]-like closed domestic platforms: this is an [[AIAgentOverseasCommercialization|overseas commercialization]] interpretation of [[Manus]]' market fit linked to interface availability, not proof of a universal ban or verified acquisition terms. [[biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1]] has [[Ryo]] illustrate [[TaskAsAService|tool discovery]] through Linux I/O commands.
- **No official integration:** [[women-ba-ai-sai-jin-huadian-hou-cai-zhidao-ai-luodi-you-duo-zang-1]] describes one flower shop's [[OperationalDataCapture|printer-output capture]], OCR, photos and voice because delivery-platform APIs were limited. It depends on permission, data-quality review and hands-busy worker routines; it is not general authorization to intercept systems or a replacement for APIs.

- **Boundary cases:** [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] proposes decomposed [[AgenticSoftware|agentic services]], while [[139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]] distinguishes [[ComputerUseAgent|computer-use]] and [[LanguageAgent|language agents]] that can operate existing GUIs without a purpose-built contract. [[OpenCloud]] is cited for entry via channels and skills, not proof of API superiority. [[VibeCoding]] may make a quick adapter but still requires review. [[HarnessEngineering]] concerns the execution and feedback envelope, not just a command syntax. [[AgentDynamics]] makes structured event streams important when many agents coordinate.

## Counterevidence & Qualifications
- [[guanyu-ai-kaiyuan-shangyehua-yu-quanqiuhua-de-jingyan-jiaoxun-he-fangfalun-duitan-pingcap-cto-dongxu-ljw8va0evobhz4ojzrulqzjvxw5]] and vendor interviews are design/market assertions; no note independently benchmarks CLI against API/MCP or verifies agent-consumed revenue. A CLI can be unsuitable when interactive auth, ambiguous state or audit requirements are unresolved.
- Human-facing [[HumanAgentCollaboration|collaboration]] is not identical to a tool contract. Closed-platform [[ChinaAgentMarketFriction|business incentives]] and regulated finance constrain access even when a technical adapter is feasible.

## What Changed
- Consolidated twenty source arrivals into six interface mechanisms rather than twenty product notices.
- Separated callable action/data surfaces from human IM, autocomplete and graphical review.
- Treated vendor scale, platform access and printer capture as bounded claims.

## Related Concepts
- [[Airwallex]] - Its proposed Agent OS illustrates regulated finance capability exposure.
- [[IntelligentFinance]] - Finance actions need permission and reconciliation around callable endpoints.
- [[BusinessLedAITransformation]] - Enterprise legacy access must follow actual workflow ownership.
- [[AIDataMemoryInfrastructure]] - Governed retrieval is a prerequisite for useful database-backed agent context.
- [[OfflineAIImplementation]] - The flower-shop adaptation illustrates why physical workflow fit matters more than an ideal API.
- [[LocalLifePlatformDependency]] - Delivery-platform data bottlenecks drove that specific printer workaround.
- [[AICoworkers]] - Moxt's workspace is intended for agents acting on documents and views.
- [[AIProgrammingEngineShift]] - Linux tool discovery is an example of delegation replacing memorized software operations.
- [[AISkills]] - Skills explain how an agent can invoke and combine underlying tools.
- [[AgenticWorkflow]] - An interface matters when it supports recoverable end-to-end task execution.
- [[AgentPaymentInfrastructure]] - Financial calls require bounded spend and auditable settlement.
- [[OrganizationalContext]] - Agent-readable workplace state includes task history and decision constraints.
- [[GeneratedWorkInterfaces]] - A generated view is a presentation artifact, not automatically an action contract.
- [[AIApplicationLayerMoat]] - To-agent distribution changes the application company's route to demand.

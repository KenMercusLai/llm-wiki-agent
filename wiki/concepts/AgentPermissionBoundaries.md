---
title: "Agent Permission Boundaries"
type: concept
tags: [agents, security, governance]
sources:
  - vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1
  - e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817
  - vol-171-jiaru-women-you-wuxian-token-1-6682-1
  - moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk
  - keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311
  - tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128
  - tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3
  - e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923
  - tech-20260213-tech-pod-128-tech-20260213-tech-pod-128
  - 1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6
  - vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1
  - 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1
  - ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz
  - vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d
  - women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv
last_updated: 2026-08-24
knowledge_schema: synthesis-v1
---
# Agent Permission Boundaries

## Definition
Agent permission boundaries specify what an agent may read, change, spend, disclose or sense, under whose authority, and when it must stop for approval. They govern resource/action access; a model refusing dangerous content is a different safety mechanism.

## Current Synthesis
Useful local and enterprise agents need task-specific authority, but broad mounts, logged-in sessions and connected tools enlarge the blast radius. Separation of trusted versus self-written skills, temporary grants, recovery and human review are complementary controls; no VM, password abstraction or vendor consent feature is complete on its own.

## Key Claims
- Grant read, write, delete, publish and spend authority by action risk and resource, not by a single all-or-nothing agent toggle.
- Local files, browser sessions, external web content and third-party skills can carry secrets and prompt-injection instructions even inside a nominal sandbox.
- Temporary task grants and revocation can avoid permanent access without inducing approval fatigue through repeated indiscriminate prompts.
- Organizational roles, separate work identities and review/audit determine what enterprise agents can see or do; a hidden plaintext password alone is not a boundary.
- Payment mandates require intent, amount/category bounds, traceability and dispute handling rather than unrestricted credentials.
- Wearable sensing extends consent obligations to bystanders, who did not delegate authority to the wearer's agent.
- High-impact actions need backups, rollback, logging and human escalation because prevention cannot guarantee every run.

## Evidence
- **Risk tier and recovery:** [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] has co-hosts [[JustinYan]] and [[Zili]] discuss Justin's [[OpenClaw]] VM, separate accounts and trusted-versus-agent-written [[AISkills]] invocation rules. [[1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6]] records [[YuYi]]'s deletion, protocol change, spend and social-harm red lines, while [[CangShifu]] adds drift from product/content standards. [[e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817]] has [[Dongxu]] link powerful agent creativity to backup, rollback and logging when production data or credentials can be mutated. [[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]] warns that [[VibeCoding|YOLO coding]] and parallel sessions need branches/worktrees and review because agent commands may reach beyond code into email, cloud, servers and financial accounts.
- **Local context and injection:** [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] pairs [[LocalAgentExecution|local value]] with exposure of files and devices. [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] describes web/skill prompt injection and mounted secrets; Docker isolation is not complete when private directories or live browser profiles are shared. [[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] distinguishes browser extension, background Mac, phone remote control and IM [[IMAgentInterfaces|channels]] as different account contexts. In [[tech-20260213-tech-pod-128-tech-20260213-tech-pod-128]], guest [[JewelBurkeSolomon]] warns against connecting agents to [[MoteBook]] after a reported [[Wiz]] finding about sensitive-data exposure; this is a platform-specific caution, not proof every social agent leaks or independent confirmation of the report.
-- **Temporary authority and accounts:** [[moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]] has [[Runta]] founder [[DaiGuanlan]] propose task grants and immediate withdrawal to reduce standing authority, while [[AgentApprovalFatigue|approval fatigue]] makes incessant prompts counterproductive. [[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]] notes that 1Password/MCP-style delegated login may hide plaintext yet give the agent the power to log in; [[ComputerUseAgent|customer-service escalation]] adds a social action boundary. In [[women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv]], [[Yuhao]] describes [[Kuse]] / [[Junior]] work identities with separate email and phone accounts, plus his team's phishing and malicious-skill tests; these vendor-reported tests do not establish general safety, and role-based data disclosure, external company representation and [[EnterpriseAgentMemory|durable memory]] remain open control problems. [[e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]] discusses [[Creo]]'s [[AIFirstOrganization|organizational trust]] and audit needs, but the registered note does not substantiate the old page's specific broad-read/narrow-write access policy.
- **Payments and services:** [[keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311]] has [[PatrickWu]] describe [[Clink]] and [[Visa]] converting a user's product, price and category mandate into a checked one-time purchase capability; [[AgentSpendControls]] and [[AgentPaymentInfrastructure]] need audit and liability records. [[wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d]] has [[DongHongguang]] argue for graded service-call permissions for [[GuangfanTechnology]] assistants, not a binary OS access switch. [[vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1]] adds product substitutions, address and budget to [[AgenticCommerce|shopping]] safeguards. [[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] names [[Podwise]] transcripts, [[WeChatReading]] sync and release/cost monitoring as [[RoutineAgentAutomation|repeatable workflow]] examples; its source note does not independently specify a full authorization architecture for them.
- **Bystanders and physical world:** [[tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]] has [[DanSiroker]] describe [[Limitless]]'s new-voice opt-in [[ConsentBasedRecording|consent mode]] and encryption; both are founder claims, not independent verification. [[tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128]] notes [[WillGottsagen]]'s distinction between smart-glasses recording lights and unresolved continuous listening. [[vol-171-jiaru-women-you-wuxian-token-1-6682-1]] raises home agents' household inventory/private-space exposure and separately discusses high-risk weapons refusal; refusing harmful content is not equivalent to tool authorization.

## Counterevidence & Qualifications
- Sandbox, VM or separate account boundaries fail if a sensitive mount, token, browser session or payment authority crosses them. [[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] and [[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]] are practitioners' caution, not measured comparative failure rates.
- Broad read access with narrower write rights would require its own source evidence and threat model; the registered Creo note does not document that particular policy. Proposed Runta temporary grants, Clink mandates and Limitless opt-in must not be called independently proven safe.
- [[AgentIdentityAndAuthentication|Identity]] identifies the delegator and principal; authorization, audit and recoverability are separate. Privacy of nearby people is not simply an extension of the user's account privilege.

## What Changed
- Replaced nineteen source arrivals with action-tier, local exposure, temporary grant, finance, enterprise and bystander mechanisms.
- Distinguished credential hiding from authority, and content refusals from tool permissions.
- Kept the source-local workaround and vendor claims bounded rather than recommending a universal architecture.

## Related Concepts
- [[AIFirstOrganization]] - Broader agent read access raises organization-wide disclosure and write-control questions.
- [[AISocialNetworks]] - Agent-only platforms can leak connected account context.
- [[ClaudeCode]] - YOLO-mode coding illustrates why execution convenience changes the scope of authority.
- [[OnePersonCompany]] - A solo founder supervising many agents needs explicit deletion, spend and reputational red lines.
- [[PersistentAgentMemory]] - Long-lived retained context needs separate read and disclosure permissions.
- [[AgentHarness]] - The runtime enforces tools, isolation and action confirmations.
- [[AgentFacingInterfaces]] - Callable capabilities need resource- and action-specific permissions.
- [[EnterpriseAgentGovernance]] - Organizational agents need role, supervision and audit policies.
- [[AIGovernanceAndCompliance]] - Regulatory obligations can constrain payment, data and recording actions.
- [[DataPortabilityAndSustainableTools]] - User control over personal data shapes the trust boundary.
- [[HumanJudgmentUnderAI]] - Humans retain responsibility for escalation and irreversible action.
- [[AIAssistantServiceEntry]] - Booking/service interfaces require differentiated authority, not just conversational access.
- [[AgentRuntimeExecutionLayer]] - Revocation, logging and restore are runtime controls for long-lived agents.
- [[ProbabilisticSoftware]] - Variable behavior motivates deterministic outer controls and recovery.
- [[AIHardwarePrivacyExchange]] - Household context value comes with exposure of nonuser information.
- [[AIModelSandboxEscape]] - A sandbox boundary needs threat-model scrutiny before being trusted.
- [[AICodingVerification]] - Reviews and worktree isolation complement command permission scopes.
- [[AIContentProvenance]] - Agent-authored outward messages should be attributable when disclosure matters.
- [[AIPlusTerminals]] - Wearables and robots create sensor/actuator permissions beyond file access.
- [[VoiceInteraction]] - Voice capture is a consent issue when nonusers are nearby.
- [[PersonalAIMemory]] - Stored recordings and preferences remain sensitive after capture.
- [[WearableAIAssistant]] - Always-available sensing makes bystander consent an ongoing boundary.
- [[AgentEvaluationBenchmarks]] - Enterprise agents need tests for unsafe action as well as task completion.
- [[AIManagingAI]] - Supervising agents does not eliminate recovery or human authority.
- [[AIUsePacing]] - Review cadence helps catch value drift without prompting on every trivial step.
- [[UnlimitedTokenWorkflow]] - Cheap repeated execution can scale up a permission mistake.
- [[ModelContextProtocol]] - A credential-bearing integration still requires scoped tool authorization.
- [[Cloudflare]] - Operational infrastructure calls can produce durable changes outside code.
- [[Codex]] - Coding tools may reach accounts and servers beyond their repository sandbox.

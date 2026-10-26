---
title: "Data Center Physical Resilience"
type: concept
tags: [infrastructure, cloud, resilience]
sources:
  - tech-20260821-mp-tech-pod-128-tech-20260821-mp-tech-pod-128
  - tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128
  - tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128
  - chule-shiyou-he-haixia-zhejie-yilang-zhanzheng-kaishi-suanji-nide-fuwuqi-le-keji-luandun
  - e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf
  - shangye-xiaoyang-43-ai-shidai-shui-zai-gei-fuwuqi-jiangwen-992085076
last_updated: 2026-08-24
knowledge_schema: synthesis-v1
---

# Data Center Physical Resilience

## Definition
Data center physical resilience is the capacity to continue, degrade safely or recover after disruptions to power, cooling, network, equipment delivery and staff access.

## Current Synthesis
Resilience is a system property, not simply a reinforced building. Grid queues are shifting some sites to primary generators or battery supply, while dense GPUs depend on active thermal loops. Conflict may interrupt operators and replacement routes; cargo theft delays installation or repair rather than proving an operating facility was attacked.

## Key Claims
- Service continuity depends on simultaneous power, cooling, network, spare-part and personnel availability.
- Backup generators used as primary power require different fuel, maintenance and supply planning.
- Off-grid reused batteries offer a distinct route whose capacity, charging, aging and safety must be assessed at the site level.
- GPU cooling failures and inbound equipment losses can interrupt delivery or recovery without destroying the building.
- Conflict exposure raises recovery and cross-region planning needs, but reported war targets cannot be treated as independently confirmed attacks.

## Evidence
- **Conflict and recovery:** [[KejiLuandun]] argues that regional cloud hubs can be both low-latency and exposed; evacuation, flights, power, cooling, spare parts and repeated danger can extend recovery for weeks or months in the hosts’ scenario. Its Iran-related target list and specific attacks are not independently verified by the note. Alternatives such as India, Singapore or Frankfurt can trade latency for geographic separation. [[chule-shiyou-he-haixia-zhejie-yilang-zhanzheng-kaishi-suanji-nide-fuwuqi-le-keji-luandun]]
- **Primary power:** [[Caterpillar]] natural-gas generators formerly used for backup are described as main supply at some off-grid sites delayed by interconnection; the Utah example reports a 600-generator order, while fuel and backlog may affect traditional hospital users too. [[tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128]] [[RedwoodMaterials]] says its Nevada off-grid site uses 60 MWh/12 MW of second-life EV batteries built in four months; that demonstration and a proposed 10 GW/year production line are not proof of indefinite supply or safety. [[tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128]]
- **Cooling and logistics:** The [[Grundfos]]/[[HenanSmartSupercomputingCenter]] case describes pumps, variable-speed flow, heat exchange and water quality as operational dependencies, with a reported 40-day prefabricated installation. [[shangye-xiaoyang-43-ai-shidai-shui-zai-gei-fuwuqi-jiangwen-992085076]] [[PareshDave]] reports stolen shipments of chips, copper, cooling parts and fiber, sometimes via doctored freight paperwork; the note links restricted chip supply under [[AIExportControls]] to possible black-market incentives, not a proven cause of each theft. The resilience risk is delayed arrival or replacement, not a measured outage of an installed site. [[tech-20260821-mp-tech-pod-128-tech-20260821-mp-tech-pod-128]]
- **Importance, not reliability proof:** An investment commentary describes token and agent demand driving hard-asset spending; it does not measure uptime, failure rates or recovery. [[e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]]

## Counterevidence & Qualifications
The war scenario and target assertions are source claims without independent verification; military-grade hardening is not universally economical. Generator and battery cases rely substantially on vendors and do not provide longitudinal durability or lifecycle emissions results. Thermal figures are episode/vendor claims; cooling failure and freight theft are different layers. Investment enthusiasm alone does not establish resilience.

## What Changed
- Separated power-source substitution, thermal operations, wartime recovery and inbound logistics.
- Distinguished proposed/observed resilience mechanisms from unverified attacks and unmeasured outage rates.

## Related Concepts
- [[WarAwareDisasterRecovery]] - cross-region backup under conflict and staff-access constraints.
- [[RegionalNetworkTopologyRisk]] - strategically useful hubs can concentrate physical exposure.
- [[DataCenterOnsitePower]] - primary generators change the maintenance regime.
- [[SecondLifeEVBatteryStorage]] - reused batteries create an alternative supply path with degradation risk.
- [[DataCenterThermalManagement]] - pumps, water and heat exchange govern continuous operation.
- [[AIDataCenterCargoTheft]] - replacement and construction parts may be diverted before arrival.
- [[AIComputeContinuity]] - physical interruptions propagate to model-serving capacity.
- [[DigitalInfrastructureWarRisk]] - armed conflict can interrupt physical and human repair routes.
- [[AIHardwareSupplyChainPressure]] - scarce replacement components can prolong installation and restoration.
- [[MaaSInfrastructure]] - model-serving platforms inherit facility power and cooling failures.

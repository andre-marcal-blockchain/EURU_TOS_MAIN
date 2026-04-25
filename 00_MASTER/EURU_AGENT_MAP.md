# EURU_AGENT_MAP.md
# Version: 1.0.0 | Scope: Full System | Last Updated: 2026-04-15
# Purpose: Master reference for all agents across Euru OS and the Breakout Intelligence Layer.
#          Shows agent identities, folders, roles, flow relationships, and authority hierarchy.

---

## SYSTEM OVERVIEW

Euru OS operates two distinct but connected agent pipelines:

1. **Core Pipeline** — 10 agents in `04_AGENTES/` (numbered 01–10). The primary governance, market observation, and execution decision system. Operational since Week 1.
2. **Breakout Intelligence Layer** — 9 agents in `04_AGENTES/BREAKOUT_LAYER/` (prefixed BL-01 to BL-09). A dedicated breakout detection and execution sub-pipeline. Built Week 6. Awaiting SIMULATE activation.

The two pipelines are **additive** — Breakout Layer extends the Core Pipeline, sharing the same system phase, governance framework, watchlist, and journal infrastructure.

---

## CORE PIPELINE AGENTS

**Location:** `04_AGENTES/`
**Phase:** READ_ONLY automated (Week 5 state)
**File standard per agent:** `BRIEFING_FINAL.md`, `PROMPT_REVISADO.md`, `OUTPUT_FORMAT_FINAL.md`

### Agent Roster

| ID | Agent | Folder | Status | Role |
|---|---|---|---|---|
| 01 | Scout | `01_SCOUT/` | AUTOMATED | Structural analysis — classifies assets as NO_TRADE / WATCHLIST / SETUP |
| 02 | Flow Analyst | `02_FLOW_ANALYST/` | AUTOMATED | Flow confirmation — RSI, MACD, OBV, ATR. Returns CONFIRMS / CONTRADICTS / INCONCLUSIVE |
| 03 | News Sentinel | `03_NEWS_SENTINEL/` | AUTOMATED | News severity filter — LOW / MEDIUM / HIGH / CRITICAL |
| 04 | Quant/Risk Officer | `04_QUANT_RISK_OFFICER/` | MANUAL | Quantitative risk scoring on SETUP signals |
| 05 | Execution Orchestrator | `05_EXECUTION_ORCHESTRATOR/` | MANUAL | Final go/no-go decision for all trade actions |
| 06 | DevOps Guardian | `06_DEVOPS_GUARDIAO/` | MANUAL | Infrastructure health — can force READ_ONLY on instability |
| 07 | Journal Auditor | `07_JOURNAL_AUDITOR/` | SCHEDULED | Post-trade audit — validates journal entries and governance compliance |
| 08 | Score Engine | `08_SCORE_ENGINE/` | AUTOMATED | Scores assets 0–35 across 7 criteria, classifies into tiers |
| 09 | MAC Playbook Analyst | `09_MAC_PLAYBOOK_ANALYST/` | MANUAL | Macro context — playbook-level veto on trade direction |
| 10 | Quality Control | `10_QUALITY_CONTROL/` | MANUAL | Output validation — checks all agent outputs against schema |

_Note: `08_WATCHDOG/` folder preserved as reference. Watchdog responsibilities folded into expanded pipeline._

### Core Pipeline Flow

```
Scout (01) → Flow Analyst (02) → News Sentinel (03) → Quant/Risk Officer (04) → Execution Orchestrator (05)
                 ↑                                                                         ↑
           Score Engine (08)                                              DevOps Guardian (06) [overrides all]
      MAC Playbook Analyst (09)                                           Journal Auditor (07) [post-trade]
                                                                          Quality Control (10) [validates all]
```

### Core Pipeline Conflict Resolution Authority

| Priority | Agent | Override Power |
|---|---|---|
| 1 (highest) | DevOps Guardian (06) | Can force READ_ONLY — overrides all other agents |
| 2 | Execution Orchestrator (05) | Final go/no-go — cannot be overridden except by DevOps |
| 3 | Quant/Risk Officer (04) | Risk-level veto |
| 4 | News Sentinel (03) | Blocks on CRITICAL severity |
| 5 | MAC Playbook Analyst (09) | Playbook-level veto |
| 6 | Flow Analyst (02) | Flow contradiction blocks Scout SETUP |
| 7 | Scout (01) | Structural classification |
| 8 | Score Engine (08) | Scoring and tier classification |
| 9 (lowest) | Quality Control (10) | Validates outputs — does not generate signals |

### Automated Scripts (Core Pipeline)

| Script | Agents Implemented | Output |
|---|---|---|
| `euru_morning_scan.py` | Scout + Flow Analyst + Score Engine + News Sentinel | `SCOUT_REPORT_<date>.md` |
| `euru_asian_scan.py` | Scout (4H) + Flow Analyst + Score Engine | `ASIAN_REPORT_<date>.md` |
| `euru_flow_analyst.py` | Flow Analyst (library) | Returns CONFIRMS / CONTRADICTS / INCONCLUSIVE |
| `euru_score_engine.py` | Score Engine (library) | Returns 0–35 score + tier + action suggestion |

---

## BREAKOUT INTELLIGENCE LAYER AGENTS

**Location:** `04_AGENTES/BREAKOUT_LAYER/`
**Phase:** Built — awaiting Type 3 approval for SIMULATE activation
**File standard per agent:** `PROMPT.md`, `BRIEFING.md`, `OUTPUT_FORMAT.md`

### Agent Roster

| ID | Agent | Folder | Flow Position | Role |
|---|---|---|---|---|
| BL-01 | Risk Guardian | `01_RISK_GUARDIAN/` | Step 06 | Capital protection gate — 1%/5%/2xATR/drawdown checks |
| BL-02 | Structure Hunter | `02_STRUCTURE_HUNTER/` | Step 02 | Zone mapping — touches, compression, formation, zone scores |
| BL-03 | Breakout Confirmation | `03_BREAKOUT_CONFIRMATION/` | Step 03 | Real vs fakeout — candle close, volume, wick, post-break |
| BL-04 | Alert Radar | `04_ALERT_RADAR/` | Step 01 | Pipeline entry — webhook intake, validation, normalization, routing |
| BL-05 | Market Regime | `05_MARKET_REGIME/` | Step 04 (parallel) | Regime classification — trend/chop/compression, BTC alignment |
| BL-06 | Tactical Execution | `06_TACTICAL_EXECUTION/` | Step 07 | Trade plan construction — entry, stop, targets, warning_flags |
| BL-07 | Compounding Governor | `07_COMPOUNDING_GOVERNOR/` | Step 08 | Scaling gate — approves/freezes exposure increase |
| BL-08 | Journal Learning | `08_JOURNAL_LEARNING/` | Step 09 | Institutional memory — all events, features, outcomes, patterns |
| BL-09 | Promise Auditor | `09_PROMISE_AUDITOR/` | Step 10 (weekly) | Integrity audit — score drift, band validity, negative expectancy |

### Breakout Layer Flow

```
 EXTERNAL ALERT (TradingView webhook / custom source)
         │
         ▼
 BL-04  Alert Radar          [Step 01] validate → normalize → route
         │ ROUTED
         ▼
 BL-02  Structure Hunter     [Step 02] zone score → compression → formation
         │ BREAKOUT_READY / WATCHLIST
         ▼
 BL-03  Breakout Confirmation [Step 03] candle → volume → wick → post-break
         │ CONFIRMED / WEAK_BREAKOUT
         ├─────────────────────────────────┐
         ▼                                 ▼  (parallel)
 BL-05  Market Regime         [Step 04]   Score Engine            [Step 05]
         │ regime + BTC score              │ final_score + band
         └─────────────┬───────────────────┘
                       ▼
 BL-01  Risk Guardian          [Step 06] 1%/5%/2xATR/drawdown
                       │ APPROVED
                       ▼
 BL-06  Tactical Execution     [Step 07] entry_type/stop/T1-T3/warning_flags
                       │ PLAN_READY
                       ├──────────────────────┐
                       ▼                      ▼  (parallel)
 BL-07  Compounding Governor  [Step 08]  BL-08  Journal Learning   [Step 09]
         scaling posture                  full feature row stored
                                               │
                                               │ (weekly)
                                               ▼
                                     BL-09  Promise Auditor        [Step 10]
                                            expectancy + audit report
                                               │
                                               ▼
                                          Friday Cycle / Governance
```

### Breakout Layer Blocking Conditions

Any of the following terminates the flow. The blocking agent logs the reason to Journal Learning as a NON_EXECUTION record.

| # | Condition | Blocking Agent |
|---|---|---|
| 1 | Asset on `LISTA_PROIBIDA` | BL-04 Alert Radar |
| 2 | `structural_status = NO_STRUCTURE` | BL-02 Structure Hunter |
| 3 | `verdict = FAKEOUT` | BL-03 Breakout Confirmation |
| 4 | `breakout_final_score` in DISCARD band (0–39) | Score Engine |
| 5 | `verdict = REJECTED` or `FREEZE` | BL-01 Risk Guardian |
| 6 | `plan_status = PLAN_REJECTED` | BL-06 Tactical Execution |

### Breakout Layer Hard Constraints Summary

| Constraint | Agent | Value |
|---|---|---|
| Per-trade risk limit | Risk Guardian | ≤ 1% of equity |
| Aggregate portfolio risk | Risk Guardian | ≤ 5% of equity |
| Liquidation distance minimum | Risk Guardian | ≥ 2x ATR(14) |
| Volume minimum for confirmation | Breakout Confirmation | ≥ 0.8x MA20 |
| Wick rejection maximum | Breakout Confirmation | ≤ 40% of body |
| Zone minimum touches | Structure Hunter | ≥ 2 distinct |
| Compression minimum | Structure Hunter | ≥ 3 contracting candles |
| Stop minimum distance | Tactical Execution | ≥ 1x ATR(14) |
| Minimum R:R at T1 | Tactical Execution | ≥ 2:1 after spread |
| Compounding consecutive wins | Compounding Governor | ≥ 5 closed profitable |
| Compounding fakeout rate max | Compounding Governor | < 40% last 20 signals |

### Technical Infrastructure

| Module | File | Purpose |
|---|---|---|
| Feature Schema | `05_SCORING/schemas/euru_breakout_feature_schema.yaml` | 30+ features, 4 score outputs, 5 bands, hard disqualifiers |
| Score Weights | `05_SCORING/configs/breakout_weights_v1.yaml` | `conservative_v1`: raw×0.40 + context×0.30 + tradeability×0.30 |
| Scoring Docs | `05_SCORING/docs/BREAKOUT_SCORING_OVERVIEW.md` | Score family rationale, design rules, downstream consumers |
| Execution Flow | `06_EXECUTION/BREAKOUT_EXECUTION_FLOW.md` | 10-step specification, blocking logic, output schema |
| Governance | `07_GOVERNANCE/BREAKOUT_GOVERNANCE_RULES.md` | 8 rules: phase, change types, LISTA_PROIBIDA, Friday Cycle |
| Audit Rules | `07_GOVERNANCE/BREAKOUT_AUDIT_RULES.md` | 3 trigger types, 7 auditor responsibilities |
| Learning Loop | `08_LEARNING/BREAKOUT_LEARNING_LOOP.md` | 4 output families, Friday Cycle requirements |
| Handoff | `09_HANDOFF/EURU_BREAKOUT_HANDOFF.md` | Completion checklist, activation preconditions |
| Implementation Summary | `09_HANDOFF/EURU_BREAKOUT_IMPLEMENTATION_SUMMARY.md` | Full file tree, open items, next steps |

---

## CROSS-PIPELINE RELATIONSHIPS

The Core Pipeline and Breakout Layer share the following infrastructure:

| Shared Resource | Core Pipeline Usage | Breakout Layer Usage |
|---|---|---|
| `WATCHLIST_OFICIAL.md` | Scout scans listed assets | Alert Radar validates against it |
| `LISTA_PROIBIDA` | Implicit (governed by SOP) | Explicit hard constraint in Alert Radar |
| System phase (`.env`) | All agents respect READ_ONLY | All agents respect READ_ONLY |
| Friday Cycle SOP | Journal Auditor (07) | Promise Auditor (BL-09) |
| `DECISOES_ESTRATEGICAS_REVISADO.md` | All Type 2/3 decisions | All Type 2/3 decisions |
| Governance framework | `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md` | Inherited — same rules |
| Score Engine | `euru_score_engine.py` (0–35, 7 criteria) | `05_SCORING/` (0–100, 3 families) — separate system |

**The two Score Engines are distinct:**
- Core Pipeline Score Engine: 0–35 points, 7 criteria, implemented in `euru_score_engine.py`
- Breakout Layer Score Engine: 0–100 points, 4 score families (raw/context/tradeability/final), defined in `05_SCORING/`

They are complementary — the Breakout Layer score evaluates breakout-specific quality, not the general asset quality the Core Engine evaluates.

---

## PLANNED AUTOMATION SCRIPTS

| Script (planned) | Layer | Agents Implemented | Priority |
|---|---|---|---|
| `euru_breakout_scanner.py` | Breakout | Alert Radar + Structure Hunter + Breakout Confirmation + Score Engine | Next step |
| `euru_risk_guardian.py` | Breakout | Risk Guardian | Phase: SIMULATE |
| `euru_tactical_planner.py` | Breakout | Tactical Execution + Compounding Governor | Phase: SIMULATE |

---

## VERSION HISTORY

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-04-15 | Initial creation — Core Pipeline (10 agents) + Breakout Layer (9 agents) |

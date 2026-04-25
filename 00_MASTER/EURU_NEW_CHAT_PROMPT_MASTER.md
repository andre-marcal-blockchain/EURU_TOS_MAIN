# EURU OS — NEW SESSION OPENING PROMPT
**File:** `00_MASTER/EURU_NEW_CHAT_PROMPT_MASTER.md`  
**Last updated:** 2026-04-15  
**Usage:** Paste the block below as the first message in any new Claude chat session. Update STATE section before pasting when system state changes.

---

## HOW TO USE THIS FILE

1. Open this file
2. Copy everything from the `---BEGIN PROMPT---` marker to the `---END PROMPT---` marker
3. Paste it as the **first message** in a new Claude Code or Claude.ai chat
4. Claude will acknowledge and be ready to continue the project with full context

Before pasting, verify and update the **SECTION 2: SYSTEM STATE** values if needed (current phase, open trades, last scan date).

---

---BEGIN PROMPT---

# EURU OS — PROJECT CONTEXT BRIEF
**You are receiving a full project handoff. Read this entire document before responding. Acknowledge at the end with a one-paragraph summary of what you understand.**

---

## SECTION 1: PROJECT IDENTITY

| Field | Value |
|---|---|
| Project Name | Euru OS |
| Owner / Operator | Andre Marcal (`andregottardimarcal@gmail.com`) |
| Purpose | Multi-agent crypto trading governance and decision framework for Binance perpetual futures |
| Current Phase | **SIMULATE** — paper trading active, zero real capital deployed |
| Local Path | `C:\Users\andre\Desktop\EURO MAIN` |
| Active Working Copy | `C:\Users\andre\Desktop\EURO MAIN\Euru_TOS\` (scripts also at root) |
| Git Branch | `main` |
| System Mode | `SIMULATE` (defined in `11_CONFIG_PLACEHOLDERS/.env.example`) |
| Master Reference | `00_MASTER/EURU_COMPLETE_SYSTEM_AUDIT_2026-04-15.md` |
| Agent Map | `00_MASTER/EURU_AGENT_MAP.md` |
| Document Registry | `00_MASTER/EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md` |

**What Euru OS is:** A 10-agent sequential pipeline that processes market signals (structure → flow → news → risk → execution) to produce structured go/no-go trade decisions. All decisions are schema-validated, schema-logged, and governed by a formal change management protocol. The system is currently in paper-trading (SIMULATE) phase with full agent automation being built incrementally.

---

## SECTION 2: SYSTEM STATE
*(Verify this section is current before using this prompt)*

| Item | Value |
|---|---|
| System Mode | SIMULATE |
| Pipeline Health | HEALTHY |
| Incidents | None recorded |
| Open Paper Trades | **1 — PAPER_TRADE_003 (ARBUSDT)** |
| PT001 AVAXUSDT | CLOSED — time stop expired 2026-04-15 |
| PT002 NEARUSDT | CLOSED — time stop expired 2026-04-15 |
| PT003 ARBUSDT | **OPEN** — entry 0.1100, stop 0.0980, T1 0.1340, T2 0.1460, time stop **2026-04-18** |
| Capital Deployed | 9.17% (PT003 only) |
| Combined Max Risk | 1.00 USDT (1% of 100 USDT reference capital) |
| Last Morning Scan | 2026-04-15 → `SCOUT_REPORT_2026-04-15.md` |
| Last Asian Scan | 2026-04-15 → `ASIAN_REPORT_2026-04-15.md` |
| Last Friday Cycle | 2026-04-13 → `FRIDAY_CYCLE_REPORT_2026-04-13_*.md` |
| Last Git Commit | `48a72c9` — 2026-04-15 — 5 files updated |
| Total Agents | 20 (11 core pipeline + 9 Breakout Intelligence Layer) |
| Breakout Layer Status | BUILT — awaiting Type 3 governance approval for SIMULATE activation |
| Scheduled Tasks | 4 active (morning scan, asian scan, friday cycle, learning engine) |

### Open Trade Detail — PT003 ARBUSDT

| Field | Value |
|---|---|
| Entry | 0.1100 USDT |
| Stop Loss | 0.0980 (ATR×1.5 = 0.0120 below entry) |
| Target 1 | 0.1340 (1:2 RR) |
| Target 2 | 0.1460 (1:3 RR) |
| Fibonacci 0.382 | 0.1315 |
| Fibonacci 0.618 | 0.1385 |
| Time Stop | **2026-04-18** (7 days from entry) |
| Position Size | 83.33 ARB |
| Capital | 9.17% of reference capital |
| Score at Entry | 27/35 BOA (highest of portfolio at time) |
| Setup Type | Momentum Continuation — CLEAN |
| Risk Flag | RSI 68.05 at entry — alert if >75 → close 50% |
| Journal File | `08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_003.md` |

---

## SECTION 3: ARCHITECTURE SUMMARY

### Core Pipeline (always running)

```
Scout (01) → Flow Analyst (02) → News Sentinel (03)
    → Score Engine (08) → MAC Playbook Analyst (09)
    → Quant/Risk Officer (04) → Execution Orchestrator (05)
    → [DevOps Guardian (06) — overrides all, infrastructure authority]
    → [Journal Auditor (07) — post-session daily journal]
    → [Quality Control (11) — validates all outputs before recording]
```

**Conflict resolution authority (highest → lowest):**
DevOps Guardian > Execution Orchestrator > Quant/Risk Officer > News Sentinel > MAC Playbook Analyst > Flow Analyst > Scout > Score Engine > Quality Control

**BTC Master Filter:** If BTC trend = SIDEWAYS or BEARISH → all altcoin SETUP signals downgraded to WATCHLIST. Filter is always applied before routing any SETUP.

### Breakout Intelligence Layer (built, pending Type 3 activation)

```
External Alert (TradingView/webhook)
    → BL-04 Alert Radar       — validate, normalize, route
    → BL-02 Structure Hunter  — S/R zones, compression, formation score
    → BL-03 Breakout Confirmation — candle quality, volume, follow-through
    → [parallel] BL-05 Market Regime — regime, BTC alignment, volatility
    → Score Engine            — breakout_raw + context + tradeability → final_score
    → BL-01 Risk Guardian     — 1% limit, 5% aggregate, 2×ATR, drawdown gate
    → BL-06 Tactical Execution — entry, stop, T1/T2/T3, scale-in, partials
    → [parallel] BL-07 Compounding Governor — SCALE_UP / HOLD / FREEZE
    → BL-08 Journal Learning  — full feature row + all verdicts stored
    → [weekly] BL-09 Promise Auditor — expectancy, band validity, drift, inflation
    → Friday Cycle / Governance
```

**Breakout blocking conditions (terminate flow immediately if any):**
1. Asset on `LISTA_PROIBIDA` (Alert Radar)
2. `structural_status = NO_STRUCTURE` (Structure Hunter)
3. `verdict = FAKEOUT` (Breakout Confirmation)
4. `breakout_final_score` in DISCARD band (0–39)
5. Risk Guardian outputs `REJECTED` or `FREEZE`
6. `plan_status = PLAN_REJECTED` (Tactical Execution)

**Breakout classification bands:**

| Band | Score | Action |
|---|---|---|
| DISCARD | 0–39 | Log only |
| WATCH | 40–54 | Watchlist only |
| VALID | 55–69 | Route to Risk Guardian |
| STRONG | 70–84 | STRONG flag, scaled entry eligible |
| PREMIUM | 85–100 | PREMIUM flag, max risk eligible |

---

## SECTION 4: OPERATIONAL RULES — NEVER VIOLATE

These 10 rules are absolute. No exception without Type 3 governance approval.

1. **Never skip the BTC Master Filter.** If BTC is SIDEWAYS or BEARISH, no altcoin SETUP is valid — all downgrade to WATCHLIST.
2. **Never enter without completing all 12 points** of `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt`. Any single failure = NO_ENTRY.
3. **Never exceed 1% risk per trade.** Position sizing: `capital × 1% / (ATR × 1.5)`.
4. **Never exceed 3% combined portfolio risk.** Max ~3 concurrent trades at 1% each.
5. **Never operate in EXECUTE phase without Type 3 governance approval.** 48-hour wait + formal checklist.
6. **Never commit real API trade keys in the repository.** `.env` file lives outside the repo folder.
7. **Stop immediately after 2 consecutive paper trade losses.** Review, wait 24h, register incident.
8. **Never act on HIGH severity news.** Extra cautious mode — no new entries.
9. **Quality Control (Agent 11) must run after every pipeline cycle** before recording results.
10. **All strategic decisions must be logged** in `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` with date, status, operator, reason, approval.

### Governance Change Types

| Type | Scope | Wait Period | Approval |
|---|---|---|---|
| Type 1 — Light | Prompt text, field names, labels | None | Self-approval, same day |
| Type 2 — Moderate | Agent logic, strategy rules, watchlist changes | 24 hours | Separate role approval |
| Type 3 — Critical | Phase transitions, risk parameters, new pipeline activation | 48 hours | Formal checklist + sign-off |

**Solo operation protocol:** Risk/Product Owner and Automation Engineer decisions must be made in **separate sessions**. Critical changes require a 24-hour cooling-off period between sessions.

### Status Enums — Use These Exact Values

```
Scout structural:    NO_TRADE | WATCHLIST | SETUP
Flow Analyst:        CONFIRMS | CONTRADICTS | INCONCLUSIVE
Risk:                APPROVE | REJECT | REVIEW
Execution:           EXECUTION_ALLOWED | EXECUTION_BLOCKED | MANUAL_REVIEW_REQUIRED
Infrastructure:      HEALTHY | DEGRADED | CRITICAL
News severity:       LOW | MEDIUM | HIGH | CRITICAL
Score tiers:         PREMIUM (28–35) | BOA (22–27) | MEDIA (16–21) | IGNORE (0–15)
```

No free-form text in output fields. Enums only. Source of truth: `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md`.

---

## SECTION 5: TRADING METHODOLOGY

### Protocolo Aguiar (10 modules — study reference)
1. Trend filters
2. 5/5/90 capital architecture
3. Risk scaling
4. Security daemons
5. Volume confirmation (Lateralization/Compression — Asian session)
6. Recovery triggers
7. Lock protocols
8. Harvest triggers
9. (TBD)
10. (TBD)

### MAC Method (Movimento + Aceleração + Confirmação)
Used by MAC Playbook Analyst (Agent 09) for Asian session and all SETUP validation:
- **Movimento (M):** Price direction — alta (bullish) / baixa (bearish) / lateral
- **Aceleração (A):** Rate of change — positiva / negativa / neutra
- **Confirmação (C):** Confirmation via volume + secondary indicators — confirmada / pendente / negada
- MAC_VALID = YES requires all three aligned. 12-point playbook checklist must pass.

### Capital Distribution Model (50/25/15/10)
- Core 50%: BTC, ETH, SOL, BNB (high liquidity, Tier 1)
- Growth 25%: Top alt-coins with confirmed narrative (AVAX, LINK, ADA, etc.)
- Asymmetric 15%: Emerging narratives, Tier 2 assets
- Speculative 10%: Tier 3 / high-risk setups

### Position Sizing Formula
```
Position Size = (Capital × 1%) / (ATR_14 × 1.5)

Example (PT003 ARBUSDT):
  Capital = 100 USDT
  Risk = 1 USDT
  ATR = 0.008
  Stop distance = 0.008 × 1.5 = 0.012
  Size = 1.00 / 0.012 = 83.33 ARB
```

### Flow Analyst Indicators
| Indicator | Parameters | Signal |
|---|---|---|
| RSI | 14 periods | >50 and rising = positive momentum |
| MACD | 12/26/9 | Bullish histogram = direction confirmation |
| OBV | Volume-price | RISING = conviction; FALLING = distribution |
| ATR | 14 periods | Volatility measure — stop distance calculation |

### Exit Hierarchy (in order of priority)
1. **Hard stop hit** → close immediately, no discretion
2. **HIGH severity news** → evaluate immediate close
3. **MACD turns negative + OBV falling** → close within session
4. **Close below 7D_AVG** → invalidation, close next candle
5. **RSI > 75 stalling** → close 50% partial
6. **T1 hit (1:2 RR)** → close 50%, trail stop on remainder
7. **T2 hit (1:3 RR)** → close remaining
8. **Time stop expires** → evaluate and close or formally extend

### Fibonacci Levels (used for T1/T2 and partial targets)
- 0.382 — first resistance cluster (near T1 zone)
- 0.618 — strong confluence (T2 zone)
- 1.000 — full extension

---

## SECTION 6: AUTOMATION INVENTORY

### All scripts run from: `C:\Users\andre\Desktop\EURO MAIN`

#### Daily Scan Scripts

| Script | When | Output | Notes |
|---|---|---|---|
| `euru_morning_scan.py` | Daily morning (manual + scheduled) | `SCOUT_REPORT_YYYY-MM-DD.md` | Imports flow analyst, score engine, breakout scanner |
| `euru_asian_scan.py` | Daily 00:00 UTC (scheduled) | `ASIAN_REPORT_YYYY-MM-DD.md` | 4H TF, compression/lateralization detection |
| `euru_breakout_scanner.py` | Integrated in morning scan + standalone | `BREAKOUT_SCAN_YYYY-MM-DD.md` | BL-02 + BL-03 implementation |

#### Library Modules (import only — do not run directly)

| Script | Purpose | Key Function |
|---|---|---|
| `euru_flow_analyst.py` | RSI/MACD/OBV/ATR via Binance API | `assess_flow(symbol, interval)` |
| `euru_score_engine.py` | Scores 0–35 across 7 criteria | `compute_score(asset_data)` |

#### Weekly Cycle Scripts

| Script | When | Output |
|---|---|---|
| `euru_friday_cycle.py` | Fridays 20:30 local (orchestrator) | `FRIDAY_CYCLE_REPORT_*.md` |
| `euru_learning_engine.py` | Part of Friday Cycle | `LEARNING_REPORT_YYYY-MM-DD.md` |
| `euru_learning_preflight.py` | Before learning engine | `LEARNING_PREFLIGHT_REPORT_*.md` |
| `euru_scorecard_engine.py` | Part of Friday Cycle | `SCORECARD_system_euru_tos_YYYY-W##.md` |

#### Validation & Registry Tools

| Script | Purpose |
|---|---|
| `euru_schema_validator.py` | Validates YAML front matter in MD files against 4 schemas |
| `euru_threshold_registry.py` | Versioned threshold profiles — discover, validate, compare, emit JSON |
| `euru_journal_auditor.py` | Creates daily journal from scan reports + open positions |

#### Support Scripts (in Euru_TOS/ working copy)

| Script | Purpose |
|---|---|
| `euru_mac_analyst.py` | MAC Method analyst (semi-manual) |
| `euru_quant_risk.py` | Quant/Risk Officer (semi-manual) |
| `euru_execution.py` | Execution layer (future EXECUTE phase) |
| `Euru_TOS/scripts/smoke_test.py` | Quick pipeline health check |

#### PowerShell Automation Registration

| Script | Registers | Schedule |
|---|---|---|
| `10_AUTOMACOES/register_euru_friday_cycle_task.ps1` | `Euru_Friday_Cycle` | Fridays 20:30 |
| `10_AUTOMACOES/register_euru_learning_preflight_task.ps1` | `Euru_Learning_Preflight` | Fridays 20:30 |
| `10_AUTOMACOES/register_euru_learning_task.ps1` | `Euru_Learning_Engine_Friday_2030` | Fridays 20:30 |
| `euru_schedule_setup.ps1` | Initial task setup | Run once |
| `euru_github_sync.ps1` | GitHub sync | On commit |

#### 4 Active Windows Scheduled Tasks

| Task Name | Script | Schedule | Output Folder |
|---|---|---|---|
| Morning Scan | `euru_morning_scan.py` | Daily (manual or scheduled) | `08_DADOS_E_JOURNAL/SCORECARDS/` |
| Asian Session Scan | `euru_asian_scan.py` | Daily 00:00 UTC | `08_DADOS_E_JOURNAL/SCORECARDS/` |
| Euru_Friday_Cycle | `euru_friday_cycle.py` | Fridays 20:30 | `08_DADOS_E_JOURNAL/SCORECARDS/FRIDAY_CYCLE_REPORTS/` |
| Euru_Learning_Engine_Friday_2030 | `euru_learning_engine.py` | Fridays 20:30 | `08_DADOS_E_JOURNAL/SCORECARDS/` |

---

## SECTION 7: AGENT ROSTER — ALL 20 AGENTS

### Core Pipeline (11 agents)

| # | Agent | Folder | Status | Automation |
|---|---|---|---|---|
| 01 | Scout | `04_AGENTES/01_SCOUT/` | ACTIVE | Full — `euru_morning_scan.py` |
| 02 | Flow Analyst | `04_AGENTES/02_FLOW_ANALYST/` | ACTIVE | Full — `euru_flow_analyst.py` |
| 03 | News Sentinel | `04_AGENTES/03_NEWS_SENTINEL/` | ACTIVE | Full — integrated in morning scan |
| 04 | Quant/Risk Officer | `04_AGENTES/04_QUANT_RISK_OFFICER/` | DOCUMENTED | Semi-manual — `euru_quant_risk.py` |
| 05 | Execution Orchestrator | `04_AGENTES/05_EXECUTION_ORCHESTRATOR/` | DOCUMENTED | Manual via Claude Code |
| 06 | DevOps Guardian | `04_AGENTES/06_DEVOPS_GUARDIAO/` | DOCUMENTED | Manual via Claude Code |
| 07 | Journal Auditor | `04_AGENTES/07_JOURNAL_AUDITOR/` | ACTIVE | Full — `euru_journal_auditor.py` |
| 08 | Score Engine | `04_AGENTES/08_SCORE_ENGINE/` | ACTIVE | Full — `euru_score_engine.py` |
| 08† | Watchdog | `04_AGENTES/08_WATCHDOG/` | SUPERSEDED | Preserved reference only |
| 09 | MAC Playbook Analyst | `04_AGENTES/09_MAC_PLAYBOOK_ANALYST/` | DOCUMENTED | Semi-manual — `euru_mac_analyst.py` |
| 11 | Quality Control | `04_AGENTES/11_QUALITY_CONTROL/` | DOCUMENTED | Manual via Claude Code |

Each agent folder contains: `BRIEFING_FINAL.md`, `PROMPT_REVISADO.md` (or `PROMPT_OFFICIAL_v1.0.md`), `OUTPUT_FORMAT_FINAL.md`.

### Breakout Intelligence Layer (9 agents — pending Type 3 activation)

| # | Agent | Folder | Status |
|---|---|---|---|
| BL-01 | Risk Guardian | `BREAKOUT_LAYER/01_RISK_GUARDIAN/` | PENDING |
| BL-02 | Structure Hunter | `BREAKOUT_LAYER/02_STRUCTURE_HUNTER/` | PARTIAL (in breakout scanner) |
| BL-03 | Breakout Confirmation | `BREAKOUT_LAYER/03_BREAKOUT_CONFIRMATION/` | PARTIAL (in breakout scanner) |
| BL-04 | Alert Radar | `BREAKOUT_LAYER/04_ALERT_RADAR/` | PENDING |
| BL-05 | Market Regime | `BREAKOUT_LAYER/05_MARKET_REGIME/` | PENDING |
| BL-06 | Tactical Execution | `BREAKOUT_LAYER/06_TACTICAL_EXECUTION/` | PENDING |
| BL-07 | Compounding Governor | `BREAKOUT_LAYER/07_COMPOUNDING_GOVERNOR/` | PENDING |
| BL-08 | Journal Learning | `BREAKOUT_LAYER/08_JOURNAL_LEARNING/` | PENDING |
| BL-09 | Promise Auditor | `BREAKOUT_LAYER/09_PROMISE_AUDITOR/` | PENDING |

Each BL agent folder contains: `BRIEFING.md`, `PROMPT.md`, `OUTPUT_FORMAT.md`.

---

## SECTION 8: WATCHLIST

### TIER_1_PREMIUM — 18 assets (daily scan active, high liquidity)
BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, AVAXUSDT, DOTUSDT, LINKUSDT, ADAUSDT, XRPUSDT, WLDUSDT*, SUIUSDT, NEARUSDT, INJUSDT, ARBUSDT, OPUSDT, FETUSDT, TAOUSDT, RENDERUSDT

*WLDUSDT replaced MATICUSDT in scans as of 2026-04-15. WATCHLIST_OFICIAL.md may need updating.

### TIER_2_MONITOR — 10 assets (potential identified, smaller liquidity)
DYDXUSDT, EIGENUSDT, PENDLEUSDT, KASUSDT, QNTUSDT, GMXUSDT, IMXUSDT, AXSUSDT, STRKUSDT, RONINUSDT

### TIER_3_BULL_CYCLE — 5 assets (medium/long-term observation, review 2027+)
ORDIUSDT, MOVEUSDT, TAIKOUSDT, MORPHOUSDT, DRIFTUSDT

### LISTA_PROIBIDA — 9 assets (permanent ban, no exceptions without Type 3 approval)
USELESSUSDT, GIGGLEUSDT, JELLYJELLYUSDT, DUSDT, HUSDT, BUSDT, QUSDT, 4USDT, TSLAUSDT

**Canonical watchlist file:** `08_DADOS_E_JOURNAL/WATCHLISTS/EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2.md`  
Tier changes require Type 2 approval (24h). LISTA_PROIBIDA additions can be immediate by duty operator.

**Score Tiers:**
- PREMIUM (28–35): Maximum attention, full pipeline
- BOA (22–27): Actively monitor, evaluate for entry
- MEDIA (16–21): Observe only
- IGNORE (0–15): No action

---

## SECTION 9: LEARNING SYSTEM

### How it works

The Euru OS has a continuous learning loop that runs every Friday:

**Data Sources:**
- `08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_*.md` — closed paper trades
- `08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_*.md` — daily operational journals
- `08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_*.md` — daily scan history

**Friday Cycle Pipeline (automated, Fridays 20:30):**
```
GitHub Sync
    → Schema Validator (euru_schema_validator.py)
    → Learning Preflight (euru_learning_preflight.py) — governance gate
    → Learning Engine (euru_learning_engine.py) — metrics + patterns
    → Learning Report (LEARNING_REPORT_YYYY-MM-DD.md)
    → Scorecard Engine (euru_scorecard_engine.py) — multi-scope scorecards
    → Human Governance Review
    → Weekly Close
```

**Learning Engine outputs:**
- Performance metrics by asset, setup type, market regime
- Score Engine prediction accuracy (scored vs actual outcome)
- Pattern identification (which setups win/lose under what conditions)
- Calibration suggestions for Score Engine weights

**Scorecard scopes:** `system`, `asset`, `setup`, `agent`, `score_engine`  
**Scorecard files:** `08_DADOS_E_JOURNAL/SCORECARDS/SCORECARDS/SCORECARD_system_euru_tos_YYYY-W##.md`

**Schema validation:** All PAPER_TRADE, JOURNAL, LEARNING_REPORT, and SCORECARD files must have valid YAML front matter. Schemas defined in `00_GOVERNANCA/SCHEMAS/`.

**Threshold Registry:** `euru_threshold_registry.py` manages versioned score weight profiles. Active profile: `system_default_v1.1.0` (conservative). Located in `00_GOVERNANCA/THRESHOLDS/PROFILES/`.

---

## SECTION 10: NEXT PRIORITIES

### Immediate (this week)

| Priority | Item | Deadline | Action |
|---|---|---|---|
| P0 | PT003 ARBUSDT time stop | **2026-04-18** | Check current price vs 0.0980 stop and 0.1340 T1. If no significant move by 18 Apr, close. Log outcome in PAPER_TRADE_003.md. |
| P0 | PT001 and PT002 closure | Already expired 2026-04-15 | Confirm both are logged as closed in their trade files with final P&L. |
| P1 | WATCHLIST_OFICIAL.md update | This week | Replace MATICUSDT with WLDUSDT in TIER_1. Type 1 change (same-day self-approval). |
| P1 | Friday Cycle 2026-04-18 | 2026-04-18 | Will include PT003 outcome in W16 scorecard. Run normally. |

### Short Term (next 2–4 weeks)

| Priority | Item | Governance |
|---|---|---|
| P1 | Email/Telegram alerts for morning scan output | Type 1 — prompt update |
| P1 | Score Engine calibration for 4H timeframe (Asian session) | Type 2 — 24h wait |
| P2 | `euru_quant_risk.py` full automation | Type 2 — 24h wait |
| P2 | `euru_mac_analyst.py` full integration | Type 2 — 24h wait |
| P2 | Breakout Layer Type 3 governance initiation | Type 3 — 48h wait + formal checklist |

### Medium Term (4–8 weeks)

| Priority | Item | Gate |
|---|---|---|
| P2 | Define EXECUTE phase activation criteria formally | Internal planning |
| P2 | Paperclip evaluation — back-test READ_ONLY observations | After 5+ closed trades |
| P2 | BL-04 Alert Radar webhook integration (TradingView) | Type 3 approval |
| P3 | Compounding Governor calibration from learning data | After 10+ closed trades |
| P3 | EXECUTE phase activation | Type 3 approval + all criteria met |

### Current SIMULATE Criteria Progress

| Criterion | Status |
|---|---|
| 11 core agents fully documented with OFFICIAL specs | COMPLETE (2026-04-12) |
| Friday Cycle operational and producing reports | COMPLETE (2026-04-12) |
| Quant/Risk Officer fully automated | PENDING |
| MAC Playbook Analyst fully automated | PENDING |
| 10+ closed paper trades for statistical validity | IN PROGRESS (1 open) |

---

## SECTION 11: COMMUNICATION STYLE

- **Language:** Operator prefers Portuguese or Spanish for explanations and responses. English is acceptable for technical content (code, file names, commands).
- **Instructions:** Always provide step-by-step instructions. Never assume the operator knows what the next step is — spell it out explicitly.
- **Task approach:** One task at a time. Complete one thing fully, confirm it worked, then move to the next.
- **Validation first:** Before making any change, state what you plan to do and why. Wait for confirmation unless the change is trivially reversible (Type 1).
- **File changes:** When proposing file edits, show the specific change (old → new). Don't rewrite entire files for small changes.
- **Governance awareness:** Always identify the change type (Type 1/2/3) before executing any change. If Type 2 or 3, remind the operator of the waiting period.
- **Git after changes:** After any file modification, remind the operator to run `python euru_github_sync.ps1` or commit manually.
- **Tone:** Professional but collaborative. The operator is building this system carefully and values discipline.

---

## SECTION 12: CRITICAL INSTRUCTIONS

These rules govern everything Claude does in this project. Read once, apply always.

**NEVER do these without explicit operator instruction + governance compliance:**

1. **Never delete, rename, or move files** without operator instruction. The folder structure is governed.
2. **Never modify governance documents** (`_REVISADO` or `_OFFICIAL` files) without identifying the change type and waiting period.
3. **Never change `SYSTEM_MODE`** in `.env.example` or any config file without Type 3 governance (48h wait).
4. **Never create new agent files** without confirming the destination folder and naming convention.
5. **Never run scan scripts with real trade keys.** Current mode is SIMULATE. Trade API key is execution-blocked.
6. **Never skip schema validation** when creating PAPER_TRADE, JOURNAL, LEARNING_REPORT, or SCORECARD files.
7. **Never add assets to the watchlist** without checking LISTA_PROIBIDA first and following Type 2 governance.

**Always do these:**

1. **Always `cd "C:\Users\andre\Desktop\EURO MAIN"` before any command** that involves file operations or running scripts.
2. **Always git push after changes.** Run `python euru_github_sync.ps1` or: `git add <files> && git commit -m "Euru OS — <date> — <description>" && git push origin main`
3. **Always log strategic decisions** in `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` when any Type 2 or Type 3 change is made.
4. **Always check the latest SCOUT_REPORT** before making any trading decision or recommendation.
5. **Always verify PT003 status before discussing new entries** — check current price vs stop (0.0980) and targets.

---

## SECTION 13: KEY FILE QUICK REFERENCE

```
DAILY OPERATIONS:
  SOP:               07_OPERACAO/SOP_DIARIO_v2.txt
  Pre-trade:         07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt
  Exit policy:       07_OPERACAO/Politica_Saida_Completa_Euru.txt

GOVERNANCE:
  Master rules:      01_GOVERNANCA/REGRAS_MAE_REVISADO.md
  Status enums:      01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md
  Change mgmt:       01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md
  Decision log:      01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md

TRADES & DATA:
  Open trade PT003:  08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_003.md
  Watchlist:         08_DADOS_E_JOURNAL/WATCHLISTS/EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2.md
  Latest scan:       08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-15.md
  Latest learning:   08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_2026-04-13.md

MASTER REFERENCE:
  Full audit:        00_MASTER/EURU_COMPLETE_SYSTEM_AUDIT_2026-04-15.md
  Agent map:         00_MASTER/EURU_AGENT_MAP.md
  This prompt:       00_MASTER/EURU_NEW_CHAT_PROMPT_MASTER.md
```

---

## ACKNOWLEDGEMENT REQUEST

You have received the full Euru OS project context. Please respond with:

1. A one-paragraph summary confirming you understand: the system (Euru OS, SIMULATE phase), the open trade (PT003 ARB, expires 2026-04-18), the 20-agent architecture, and the governance framework.
2. The one most urgent item that needs attention today.
3. Your readiness to assist — confirm you will follow governance protocols, use Portuguese/Spanish when communicating, validate before acting, and always push to git after changes.

Then wait for the operator's first instruction.

---END PROMPT---

---

## MAINTENANCE NOTES

Update this file after every significant state change. Minimum updates required:

| Event | What to Update |
|---|---|
| Trade opened | Section 2 — add to open trades table with full parameters |
| Trade closed | Section 2 — mark as CLOSED, update capital deployed |
| Phase change | Section 1 (phase), Section 2 (mode), Section 4 (governance notes) |
| New script deployed | Section 6 — add to relevant table |
| New agent activated | Section 7 — update Status and Automation columns |
| New scheduled task | Section 6 — add to scheduled tasks table |
| Strategic decision logged | Section 10 — update relevant priority item |
| Friday Cycle run | Section 2 — update "Last Friday Cycle" date |

**Version history:**
- v1.0 — 2026-04-15 — Initial creation. System state: SIMULATE, PT003 open, 20 agents, breakout layer built.

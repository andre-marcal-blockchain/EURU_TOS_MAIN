# Euru OS — Pipeline Architecture

**Version:** Week 6
**Mode:** READ_ONLY
**Last updated:** 2026-04-05

---

## 1. Complete ASCII Pipeline Diagram

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                          EURU OS — AGENT PIPELINE                               ║
║                     Sequential Processing + Override Layer                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝

  BINANCE API (REST / WebSocket)
       │
       │  OHLCV, Volume, Order Book, RSI/MACD/OBV/ATR (20 assets)
       │  Morning scan: 07:00 UTC (1D TF) | Asian scan: 00:00 UTC (4H TF)
       ▼
┌─────────────────────────────────────┐
│  01  SCOUT                          │
│  Structure: trend / range / channel │
│  BTC master filter applied          │
│  Output: NO_TRADE | WATCHLIST | SETUP│
└──────────────┬──────────────────────┘
               │ STATE = SETUP or WATCHLIST
               ▼
┌─────────────────────────────────────┐
│  02  FLOW ANALYST                   │
│  RSI(14), MACD(12/26/9),            │
│  OBV trend, ATR(14), Stop distance  │
│  Output: CONFIRMS | CONTRADICTS |   │
│          INCONCLUSIVE               │
└──────────────┬──────────────────────┘
               │ FLOW_STATE
               ▼
┌─────────────────────────────────────┐
│  03  NEWS SENTINEL                  │
│  CoinTelegraph RSS + macro context  │
│  Narratives: AI/RWA/DePIN/Gaming    │
│  Output: LOW | MEDIUM | HIGH |      │
│          CRITICAL severity          │
└──────────────┬──────────────────────┘
               │ OVERALL_SEVERITY               ┌─────────────────────────────┐
               │ (if CRITICAL → fast-path ──────►  05  EXECUTION ORCHESTRATOR │
               ▼ to Execution Orchestrator)      │  (EXECUTION_BLOCKED issued) │
┌─────────────────────────────────────┐          └─────────────────────────────┘
│  04  QUANT / RISK OFFICER           │
│  Position sizing (ATR×1.5 stop)     │
│  Daily risk ≤2% / Weekly ≤5%        │
│  Fibonacci exits: 0.382/0.5/0.618   │
│  Output: APPROVE | REJECT | REVIEW  │
└──────────────┬──────────────────────┘
               │ RISK_STATE
               ▼
┌─────────────────────────────────────┐
│  09  MAC / PLAYBOOK ANALYST         │
│  MAC: Movimento/Aceleração/Confirm. │
│  12-point playbook checklist        │
│  Setup quality: CLEAN|MARGINAL|INV. │
│  Output: PLAYBOOK_OK | PLAYBOOK_    │
│          REJECT | REVIEW            │
└──────────────┬──────────────────────┘
               │ PLAYBOOK_STATE
               ▼
┌─────────────────────────────────────┐
│  08  SCORE ENGINE                   │
│  Composite 0–35 across 5 inputs:    │
│  Structure + Flow + News + Risk +   │
│  Playbook (each 0-7 pts)            │
│  Threshold: ≥7 eligible             │
│  Output: ALTO_SUFICIENTE |          │
│          INSUFICIENTE | REVIEW      │
└──────────────┬──────────────────────┘
               │ SCORE_STATE + WEIGHTED_SCORE
               ▼
┌─────────────────────────────────────┐
│  05  EXECUTION ORCHESTRATOR         │
│  Consolidates all agent outputs     │
│  Detects and resolves conflicts     │
│  Applies final go/no-go logic       │
│  Output: EXECUTION_ALLOWED |        │
│          EXECUTION_BLOCKED |        │
│          MANUAL_REVIEW_REQUIRED     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  10  QUALITY CONTROL                │
│  Schema validation for all agents   │
│  Price data staleness check         │
│  Logical conflict detection         │
│  Output: VALID | INVALID |          │
│          SCHEMA_ERROR per agent     │
└──────────────┬──────────────────────┘
               │ Validated pipeline result
               ▼
┌─────────────────────────────────────┐
│  07  JOURNAL AUDITOR                │
│  Records full cycle in journal      │
│  Compliance check                   │
│  Weekly scorecard (Fridays)         │
│  Output: COMPLIANCE OK | INCOMPLETE │
└─────────────────────────────────────┘

═══════════════════════════════════════════════════
  CROSS-CUTTING AGENTS (run in parallel / always on)
═══════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────────────────┐
  │  06  DEVOPS GUARDIAN                ← HIGHEST AUTHORITY      │
  │  API latency, system health, feed latency, security events   │
  │  Monitors: morning scan (07:00) + asian scan (00:00)         │
  │  Output: HEALTHY | DEGRADED | CRITICAL                       │
  │  If CRITICAL → forces EXECUTION_BLOCKED across entire system │
  └──────────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────┐
  │  WATCHDOG (legacy 08, reference only)                        │
  │  Agent heartbeat monitoring                                  │
  │  Pipeline continuity: MAINTAINED | INTERRUPTED               │
  │  Recovery actions on agent failure                           │
  └──────────────────────────────────────────────────────────────┘
```

---

## 2. Agent Reference Table

| # | Agent | Role | Input Source | Output State | Next Agent |
|---|-------|------|--------------|--------------|------------|
| 01 | **Scout** | Market structure analysis. Identifies trend, range, compression. Applies BTC master filter. | Binance API (OHLCV, 1D / 4H) | `NO_TRADE` \| `WATCHLIST` \| `SETUP` | Flow Analyst (if SETUP/WATCHLIST) |
| 02 | **Flow Analyst** | Indicator confirmation. Calculates RSI, MACD, OBV, ATR. Validates Scout signal. | Scout output + Binance API indicators | `CONFIRMS` \| `CONTRADICTS` \| `INCONCLUSIVE` | News Sentinel |
| 03 | **News Sentinel** | News context and macro severity. Monitors CoinTelegraph RSS. Scores active narratives. | RSS feeds + macro context | `LOW` \| `MEDIUM` \| `HIGH` \| `CRITICAL` severity | Score Engine (normal) or Execution Orchestrator (if CRITICAL) |
| 04 | **Quant/Risk Officer** | Position sizing and risk validation. ATR-based stops, Fibonacci exits, exposure limits. | Scout + Flow + Binance price data | `APPROVE` \| `REJECT` \| `REVIEW` | MAC Playbook Analyst |
| 05 | **Execution Orchestrator** | Final go/no-go decision. Consolidates all agent outputs. Resolves conflicts. | All agent outputs (01–04, 08–09) | `EXECUTION_ALLOWED` \| `EXECUTION_BLOCKED` \| `MANUAL_REVIEW_REQUIRED` | Quality Control |
| 06 | **DevOps Guardian** | Infrastructure health. API connectivity, feed latency, security events, script status. | System metrics + Binance API health | `HEALTHY` \| `DEGRADED` \| `CRITICAL` | Override: blocks entire pipeline if CRITICAL |
| 07 | **Journal Auditor** | Post-cycle audit and compliance logging. Daily entries + weekly scorecard. | All agent outputs (full cycle) | `OK` \| `INCOMPLETE` \| `NON_COMPLIANT` | End of cycle (archival) |
| 08 | **Score Engine** | Composite scoring 0–35 across 5 dimensions. Classifies asset tier. Threshold gate at ≥7. | Agents 01, 02, 03, 04, 09 outputs | `ALTO_SUFICIENTE` \| `INSUFICIENTE` \| `REVIEW` | Execution Orchestrator |
| 09 | **MAC/Playbook Analyst** | Macro context layer. MAC framework + 12-point pre-trade checklist. Setup quality filter. | Scout + Flow + News + Quant outputs | `PLAYBOOK_OK` \| `PLAYBOOK_REJECT` \| `REVIEW` | Score Engine |
| 10 | **Quality Control** | Output schema validation. Price staleness check. Logical conflict detection. | All agent outputs (post-pipeline) | `VALID` \| `INVALID` \| `SCHEMA_ERROR` per agent | Journal Auditor (on VALID) or escalation (on INVALID) |

---

## 3. Conflict Resolution Hierarchy

When two or more agents produce contradictory directives, authority is resolved in this order (highest to lowest):

```
  RANK   AGENT                        AUTHORITY / TRIGGER
  ────   ─────────────────────────    ──────────────────────────────────────────
   1     DevOps Guardian (06)         Forces READ_ONLY on CRITICAL infra state.
                                      Overrides ALL other agents unconditionally.

   2     Execution Orchestrator (05)  Final go/no-go. Arbitrates any remaining
                                      conflict not resolved upstream. Last word.

   3     Quant/Risk Officer (04)      REJECT overrides any positive SETUP signal.
                                      Risk limits are hard caps, not suggestions.

   4     News Sentinel (03)           CRITICAL severity blocks pipeline regardless
                                      of structural or indicator signals.

   5     MAC Playbook Analyst (09)    PLAYBOOK_REJECT vetoes execution even when
                                      Score Engine returns ALTO_SUFICIENTE.

   6     Flow Analyst (02)            CONTRADICTS downgrades SETUP to WATCHLIST
                                      unless overridden by higher authority.

   7     Scout (01)                   NO_TRADE stops the pipeline early. Lower
                                      agents do not run if Scout output is NO_TRADE.

   8     Score Engine (08)            INSUFICIENTE blocks execution but does not
                                      override explicit REJECT or PLAYBOOK_REJECT.

   9     Quality Control (10)         SCHEMA_ERROR or INVALID halts result recording
                                      and triggers re-run or manual review.
```

**Key conflict rules:**
- A `REJECT` from Quant/Risk Officer is never overridden by a high Score Engine score.
- A `PLAYBOOK_REJECT` from MAC Analyst is never overridden by Score Engine alone.
- `CRITICAL` from DevOps Guardian suspends the pipeline regardless of market conditions.
- `CRITICAL` from News Sentinel routes directly to Execution Orchestrator with `EXECUTION_BLOCKED` recommended.
- Solo operation rule: Risk/Product Owner and Automation Engineer deliberations must occur in separate sessions. Critical changes require a 24-hour cooling-off period.

---

## 4. System Modes and Transition Criteria

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  READ_ONLY (manual)  ──►  READ_ONLY (automated)  ──►  SIMULATE  ──►  EXECUTE
  │       Phase 1                  Phase 2              Phase 3      Phase 4
  └──────────────────────────────────────────────────────────────────────┘
                         Phase skipping is PROHIBITED.
```

### READ_ONLY — Current Phase (Week 6)

**What the system DOES:**
- Fetches market data (20 assets via Binance public API)
- Runs morning scan at 07:00 UTC (1D timeframe)
- Runs Asian scan at 00:00 UTC (4H timeframe — compression/gem detection)
- Calculates RSI, MACD, OBV, ATR per asset
- Calculates Score 0–35 and tier classification
- Monitors news (CoinTelegraph RSS)
- Maintains watchlists and daily/weekly journal entries
- Monitors infrastructure health (DevOps Guardian + Watchdog)

**What the system DOES NOT DO:**
- Send real orders
- Open positions
- Change capital exposure
- Activate `BINANCE_TRADE_API_KEY`
- Use automated execution of any kind

**Transition to SIMULATE requires (Type 3 governance — 48h wait):**
- [ ] Minimum 4 weeks of consistent READ_ONLY automated runs with no critical incidents
- [ ] Score Engine calibrated against real market data
- [ ] All 10 agents validated and producing schema-compliant output
- [ ] Quality Control (10) passing all pipeline cycles
- [ ] Formal checklist completed with sign-off from Risk/Product Owner + Automation Engineer
- [ ] Entry logged in `DECISOES_ESTRATEGICAS_REVISADO.md`
- [ ] 48-hour waiting period elapsed before activation

---

### SIMULATE — Phase 3 (pending)

**What changes vs READ_ONLY:**
- Paper trades recorded with full position sizing (no real capital)
- Quant/Risk Officer (04) active with live sizing calculations
- MAC Playbook Analyst (09) active for every SETUP signal
- Execution Orchestrator issues `EXECUTION_ALLOWED` decisions (simulated only)
- Performance tracking against hypothetical entries (paperclip evaluation)

**Transition to EXECUTE requires (Type 3 governance — 48h wait):**
- [ ] Minimum 4 weeks of SIMULATE results with documented edge (positive expectancy)
- [ ] Zero critical infrastructure incidents during simulate phase
- [ ] Legal/compliance review of real execution flow
- [ ] Separate role approval (two sessions, not same session)
- [ ] Formal checklist + 48-hour waiting period

---

### EXECUTE — Phase 4 (not active)

**What changes vs SIMULATE:**
- `BINANCE_TRADE_API_KEY` activated (currently `EXECUTION_BLOCKED`)
- Execution Orchestrator `EXECUTION_ALLOWED` triggers real order placement
- All risk limits become hard enforcement (not reference)
- Drawdown circuit breakers active

---

## 5. Data Flow: Binance API → Final Decision

```
  BINANCE PUBLIC API (no trade key required in READ_ONLY)
  ├── REST endpoint: /api/v3/klines      → OHLCV candles (1D, 4H)
  ├── REST endpoint: /api/v3/ticker      → 24h volume, price change
  └── REST endpoint: /api/v3/depth       → Order book (liquidity assessment)
         │
         │  Fetched by: euru_morning_scan.py (07:00 UTC)
         │              euru_asian_scan.py   (00:00 UTC)
         │  Libraries:  euru_flow_analyst.py (RSI/MACD/OBV/ATR calculations)
         │              euru_score_engine.py  (0–35 composite scoring)
         ▼
  ┌────────────────────────────────────────────────────────────────────┐
  │  RAW MARKET DATA (per asset, per timeframe)                        │
  │  Fields: open, high, low, close, volume (OHLCV), timestamp         │
  └────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
  ┌──────────────────── 01 SCOUT ──────────────────────────────────────┐
  │  Inputs:  OHLCV (1D or 4H), 7-day average price                   │
  │  Process: Identify trend/range/channel, detect compression,        │
  │           apply BTC master filter (BTC structure must confirm)     │
  │  Outputs: STATE, SIGNAL, KEY_LEVELS (R/S/7D_AVG), INVALIDATION    │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ STATE ∈ {WATCHLIST, SETUP} → continue
                               │ STATE = NO_TRADE → pipeline stops here
                               ▼
  ┌──────────────────── 02 FLOW ANALYST ───────────────────────────────┐
  │  Inputs:  OHLCV + Scout STATE                                      │
  │  Process: RSI(14) → momentum state                                 │
  │           MACD(12/26/9) → trend direction                          │
  │           OBV → volume accumulation/distribution                   │
  │           ATR(14) → volatility, stop distance (ATR × 1.5)         │
  │  Outputs: FLOW_STATE, RSI_STATE, MACD trend, VOLUME_FLOW,          │
  │           STOP_DIST, SUGGESTED_STOP, MAC_ASSESSMENT               │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ FLOW_STATE + indicator values
                               ▼
  ┌──────────────────── 03 NEWS SENTINEL ──────────────────────────────┐
  │  Inputs:  CoinTelegraph RSS, macro context (external)             │
  │  Process: Parse headlines → severity classification (LOW/MED/HIGH) │
  │           Score narratives: AI, RWA, DePIN, Gaming, Macro          │
  │           Map headlines to watchlist assets                        │
  │  Outputs: OVERALL_SEVERITY, TOP_HEADLINES, ACTIVE_NARRATIVES,      │
  │           ASSETS_AFFECTED, ALERT_REQUIRED                          │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ OVERALL_SEVERITY
                               │ (CRITICAL → skip to Orchestrator)
                               ▼
  ┌──────────────────── 04 QUANT / RISK OFFICER ───────────────────────┐
  │  Inputs:  Scout KEY_LEVELS, Flow STOP_DIST, current price,         │
  │           capital allocation rules, asset CATEGORY                 │
  │  Process: Position size = (Capital × 2% daily risk) / stop dist    │
  │           Fibonacci exits from entry to target zones               │
  │           Check daily risk used / weekly risk used                 │
  │  Outputs: POSITION_SIZE, STOP_LOSS, TAKE_PROFIT (T1/T2),           │
  │           RISK_REWARD_RATIO, DAILY_RISK_USED, RISK_STATE           │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ RISK_STATE
                               ▼
  ┌──────────────────── 09 MAC / PLAYBOOK ANALYST ─────────────────────┐
  │  Inputs:  Scout STATE, Flow FLOW_STATE + MAC_ASSESSMENT,           │
  │           News narratives, Quant RISK_STATE                        │
  │  Process: MAC framework (Movimento/Aceleração/Confirmação)         │
  │           12-point playbook checklist (narrative, BTC context,     │
  │           structure, breakout, volume, liquidity, invalidation,    │
  │           risk, target, R/R, plan discipline)                      │
  │  Outputs: MAC_VALID, SETUP_IDENTIFIED, SETUP_QUALITY,              │
  │           PLAYBOOK_CHECKLIST (12 items), PLAYBOOK_STATE            │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ PLAYBOOK_STATE
                               ▼
  ┌──────────────────── 08 SCORE ENGINE ───────────────────────────────┐
  │  Inputs:  01 STATE, 02 FLOW_STATE, 03 OVERALL_SEVERITY,            │
  │           04 RISK_STATE, 09 PLAYBOOK_STATE                         │
  │  Process: Score each dimension 0–7 pts                             │
  │           STRUCTURE_SCORE + INDICATORS_SCORE + NEWS_SCORE +        │
  │           RISK_SCORE + PLAYBOOK_SCORE = WEIGHTED_SCORE (0–35)     │
  │           Classify: Baixo(<15) | Médio(15-22) | Alto(23-28) |      │
  │                     Muito Alto(>28)                                │
  │           Gate: WEIGHTED_SCORE ≥ 7 (0–10 normalised) → eligible   │
  │  Outputs: WEIGHTED_SCORE, CLASSIFICATION, SCORE_STATE,             │
  │           POSITIVE_FACTORS, NEGATIVE_FACTORS                       │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ SCORE_STATE + WEIGHTED_SCORE
                               ▼
  ┌──────────────────── 05 EXECUTION ORCHESTRATOR ─────────────────────┐
  │  Inputs:  ALL agent outputs (01–04, 08–09) + DevOps health (06)   │
  │  Process: Map inputs → decision matrix                             │
  │           Detect conflicts (e.g. CONFIRMS + REJECT)                │
  │           Apply conflict hierarchy (see Section 3)                 │
  │           In READ_ONLY: always outputs EXECUTION_BLOCKED           │
  │  Outputs: STRUCTURAL_STATE, FLOW_STATE, NEWS_SEVERITY,             │
  │           RISK_STATE, PLAYBOOK_STATE, SCORE, SCORE_CLASS,          │
  │           EXECUTION_STATE, EXIT_RULES (entry/SL/TP/trailing)       │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ EXECUTION_STATE
                               ▼
  ┌──────────────────── 10 QUALITY CONTROL ────────────────────────────┐
  │  Inputs:  All agent outputs from this pipeline cycle               │
  │  Process: Validate each output against OUTPUT_FORMAT_FINAL.md      │
  │           Check price data freshness (stale = excluded)            │
  │           Detect logical conflicts across agent outputs             │
  │  Outputs: PRICE_VALIDATION, AGENT_OUTPUT_VALIDATION (per agent),   │
  │           CONFLICT_DETECTION, BLOCKED_ITEMS                        │
  └────────────────────────────┬───────────────────────────────────────┘
                               │ Validated result
                               ▼
  ┌──────────────────── 07 JOURNAL AUDITOR ────────────────────────────┐
  │  Inputs:  Full validated pipeline cycle output                     │
  │  Process: Write daily journal entry (structured format)            │
  │           Check compliance with READ_ONLY constraints              │
  │           Flag TIME_STOP_TRIGGERED or incidents                    │
  │           Weekly scorecard every Friday                            │
  │  Outputs: AGENT_OUTPUTS summary, COMPLIANCE, INCIDENTS, SUMMARY    │
  │           → Written to: 08_DADOS_E_JOURNAL/                        │
  └────────────────────────────────────────────────────────────────────┘

  ══════════════════════════════════════════════════════════════════════
   REPORT OUTPUTS
  ══════════════════════════════════════════════════════════════════════
  euru_morning_scan.py  → SCOUT_REPORT_<YYYY-MM-DD>.md
  euru_asian_scan.py    → ASIAN_REPORT_<YYYY-MM-DD>.md   (GEM_ALERT flags)
  Journal Auditor (07)  → 08_DADOS_E_JOURNAL/ daily entry
  Incidents             → 09_LOGS_E_INCIDENTES/INCIDENTES.md
```

---

*Canonical status enums: `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md`*
*Governance policy: `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md`*
*Master trading rules: `01_GOVERNANCA/REGRAS_MAE_REVISADO.md`*

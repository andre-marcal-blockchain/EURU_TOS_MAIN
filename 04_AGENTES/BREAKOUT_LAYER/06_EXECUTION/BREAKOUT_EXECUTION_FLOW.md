# BREAKOUT_EXECUTION_FLOW.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Module: 06_EXECUTION
# Created: 2026-04-15 | Status: ACTIVE

---

## PURPOSE

This document defines the complete end-to-end execution flow for the Euru Breakout Intelligence Layer — from initial external alert to final trade plan output. It specifies the sequence of agent handoffs, the blocking conditions that terminate flow at each step, and the exact structure of the final execution output package.

---

## THE 10-STEP EXECUTION FLOW

```
 ┌─────────────────────────────────────────────────────────────────┐
 │              EURU BREAKOUT LAYER — EXECUTION FLOW               │
 └─────────────────────────────────────────────────────────────────┘

STEP 01  Alert Radar
         ↓  [ROUTED]    → Step 02
         ✗  [REJECTED / DUPLICATE / INVALID / FREEZE_BLOCK]  → TERMINATE

STEP 02  Structure Hunter
         ↓  [BREAKOUT_READY]    → Step 03
         ↓  [WATCHLIST]         → Step 03 (with WATCHLIST_CEILING flag)
         ✗  [NO_STRUCTURE / INSUFFICIENT_DATA]  → TERMINATE

STEP 03  Breakout Confirmation
         ↓  [CONFIRMED]            → Step 04 + Step 05 (parallel)
         ↓  [WEAK_BREAKOUT]        → Step 04 + Step 05 (with WEAK flag)
         ↓  [PENDING]              → HOLD — re-evaluate next candle close
         ✗  [FAKEOUT / HOLD]       → TERMINATE

STEP 04  Market Regime
         (runs in parallel with Score Engine)
         ↓  [regime_report]        → joins Step 05 output → Step 06

STEP 05  Score Engine
         (runs in parallel with Market Regime)
         ↓  [breakout_final_score + band]  → joins Step 04 output → Step 06
         ✗  [DISCARD band]         → TERMINATE

STEP 06  Risk Guardian
         ↓  [APPROVED]    → Step 07
         ✗  [REJECTED / FREEZE / READ_ONLY_BLOCK]  → TERMINATE

STEP 07  Tactical Execution
         ↓  [PLAN_READY]  → Step 08 + Step 09 (parallel)
         ✗  [PLAN_REJECTED / PLAN_BLOCKED]  → TERMINATE

STEP 08  Compounding Governor
         (receives trade plan from Step 07)
         ↓  [scaling posture report]  → Step 09

STEP 09  Journal Learning
         (receives from Steps 07 and 08)
         ↓  [record stored]  → Step 10 (weekly)

STEP 10  Promise Auditor → Friday Cycle
         (triggered weekly, not per-trade)
         ↓  [audit report]  → Governance Layer
```

---

## STEP-BY-STEP SPECIFICATION

---

### STEP 01 — ALERT RADAR
**Agent:** `04_ALERT_RADAR`
**Trigger:** Incoming webhook from TradingView or external source.
**Input:** Raw alert payload (any format).
**Output:** Normalized alert with routing decision.

**Actions:**
1. Validate symbol against `WATCHLIST_OFICIAL.md`
2. Check symbol against `LISTA_PROIBIDA` — immediate REJECTED if hit
3. Validate payload completeness
4. Check alert staleness (threshold: 2 candle periods)
5. Check for duplicate within cooldown window
6. Check system mode (READ_ONLY → OBSERVATION_ONLY)
7. Normalize payload to Euru standard schema
8. Route to Structure Hunter

**Pass condition:** All validation checks PASS, system not frozen, asset on watchlist.
**Terminate condition:** Any validation failure, LISTA_PROIBIDA match, FREEZE state.

---

### STEP 02 — STRUCTURE HUNTER
**Agent:** `02_STRUCTURE_HUNTER`
**Trigger:** Normalized alert from Alert Radar.
**Input:** Normalized alert + OHLCV series (minimum 30 candles).
**Output:** Structural map with zone scores, formation, compression assessment.

**Actions:**
1. Load OHLCV series for asset on primary timeframe
2. Identify S/R zones (minimum 2 touches)
3. Check zone age (expire if > 30 bars, no retest)
4. Assess compression (minimum 3 contracting candles)
5. Score zones and classify formation
6. Check BTC structural status
7. Output structural map to Breakout Confirmation

**Pass condition:** At least one valid zone (score ≥ 5) with ACTIVE status.
**Terminate condition:** NO_STRUCTURE (no valid zones), INSUFFICIENT_DATA.

---

### STEP 03 — BREAKOUT CONFIRMATION
**Agent:** `03_BREAKOUT_CONFIRMATION`
**Trigger:** Structural map from Structure Hunter.
**Input:** Structural map + breakout candle OHLCV + volume_ma20 + news context.
**Output:** Breakout verdict with quality score and component breakdown.

**Actions:**
1. Evaluate candle close vs zone boundary (ABOVE required for longs)
2. Compute wick_rejection_pct (must be ≤ 40%)
3. Compute volume_ratio (must be ≥ 0.8x)
4. Assess post-break follow-through (0–3 candles if available)
5. Check for zone re-entry (close_acceptance = REJECTED → FAKEOUT)
6. Check news context (CRITICAL → HOLD)
7. Produce confirmation verdict

**Pass condition:** CONFIRMED or WEAK_BREAKOUT.
**Hold condition:** PENDING — re-evaluate on next candle close without re-running Steps 01–02.
**Terminate condition:** FAKEOUT, HOLD (news).

---

### STEP 04 — MARKET REGIME (parallel with Step 05)
**Agent:** `05_MARKET_REGIME`
**Trigger:** CONFIRMED or WEAK_BREAKOUT verdict from Breakout Confirmation.
**Input:** OHLCV + indicator data for asset and BTC.
**Output:** Regime classification with confidence and BTC alignment score.

**Actions:**
1. Compute ADX(14) and classify regime
2. Assess ATR trend (volatility state)
3. Check BTC regime and alignment (mandatory for altcoins)
4. Check macro alignment if data available
5. Determine breakout_favorability
6. Produce regime report

**Note:** Market Regime does not block execution — it enriches the package for Risk Guardian and Tactical Execution.

---

### STEP 05 — SCORE ENGINE (parallel with Step 04)
**Agent:** Score Engine (05_SCORING)
**Trigger:** Same CONFIRMED/WEAK_BREAKOUT verdict as Step 04.
**Input:** Full feature set from all upstream agents (structure, candle, volume, impulse, post-break, MTF data).
**Output:** Four scores + classification band.

**Actions:**
1. Populate all feature groups from upstream outputs
2. Compute breakout_raw_score (structure × 0.25, candle × 0.30, impulse × 0.20, volume × 0.25)
3. Compute breakout_context_score (post_break × 0.35, MTF × 0.65)
4. Compute breakout_tradeability_score (tradeability features per config weights)
5. Apply hard disqualifiers (override to DISCARD if any triggered)
6. Apply altcoin_modifier to context score if btc_alignment_score < 0.5
7. Compute breakout_final_score (raw × 0.40, context × 0.30, tradeability × 0.30)
8. Classify into band (DISCARD / WATCH / VALID / STRONG / PREMIUM)

**Pass condition:** Band = VALID, STRONG, or PREMIUM.
**Terminate condition:** Band = DISCARD (flow ends here — not forwarded to Risk Guardian).
**Note:** WATCH band is logged to Journal Learning but does not activate Risk Guardian.

---

### STEP 06 — RISK GUARDIAN
**Agent:** `01_RISK_GUARDIAN`
**Trigger:** Receives combined package: Breakout Confirmation verdict + Market Regime report + Score Engine output.
**Input:** Full upstream package + account state (equity, open positions, drawdown, ATR).
**Output:** Risk verdict (APPROVED / REJECTED / FREEZE / READ_ONLY_BLOCK).

**Actions:**
1. Check per-trade risk (≤ 1% of equity)
2. Check aggregate portfolio risk (≤ 5%)
3. Check liquidation distance (≥ 2x ATR)
4. Check weekly drawdown limit (configurable)
5. Check leverage compliance
6. Check correlation cluster among open positions
7. Check session budget remaining
8. Produce risk verdict

**Pass condition:** APPROVED — all 7 checks PASS.
**Terminate condition:** REJECTED (any check fails), FREEZE (drawdown limit breached), READ_ONLY_BLOCK.

---

### STEP 07 — TACTICAL EXECUTION
**Agent:** `06_TACTICAL_EXECUTION`
**Trigger:** APPROVED verdict from Risk Guardian.
**Input:** Full upstream package with all prior agent outputs.
**Output:** Complete trade plan (PLAN_READY / PLAN_REJECTED).

**Actions:**
1. Select entry type (MARKET / LIMIT_RETEST / LIMIT_BREAKOUT) based on quality_score and regime
2. Compute stop price (must be ≥ 1x ATR from entry, beyond zone boundary)
3. Compute T1 target (structural next level, must achieve ≥ 2:1 R:R)
4. Compute T2 and T3 targets
5. Evaluate spread and adjust R:R accordingly
6. Define scale-in legs if applicable
7. Define partial exit rules (T1 % close mandatory)
8. Configure trail stop parameters
9. Populate warning_flags (always output this field)
10. Produce complete plan

**Pass condition:** PLAN_READY — R:R ≥ 2:1, stop ≥ 1x ATR, all fields populated.
**Terminate condition:** PLAN_REJECTED (R:R fails, stop too tight, no valid target).

---

### STEP 08 — COMPOUNDING GOVERNOR
**Agent:** `07_COMPOUNDING_GOVERNOR`
**Trigger:** PLAN_READY from Tactical Execution.
**Input:** Trade plan + performance state from Journal Learning.
**Output:** Scaling posture report (SCALE_UP / HOLD / SCALE_DOWN / COMPOUNDING_FREEZE).

**Actions:**
1. Read current performance state (consecutive wins, drawdown, fakeout rate)
2. Evaluate scaling criteria (≥ 5 consecutive wins, 0% drawdown, fakeout rate < 40%)
3. Output scaling verdict and update approved risk % if changed
4. Notify Risk Guardian if scaling posture changes
5. Forward scaling report to Journal Learning

---

### STEP 09 — JOURNAL LEARNING
**Agent:** `08_JOURNAL_LEARNING`
**Trigger:** Receives from Tactical Execution (trade plan) and Compounding Governor (scaling report).
**Input:** Complete trade plan + scaling posture + all upstream agent verdicts.
**Output:** Stored trade record (TRADE_ENTRY event).

**Actions:**
1. Validate all required fields are present
2. Store complete feature row (all 30+ features)
3. Tag regime, session, BTC alignment (mandatory)
4. Store agent_verdicts dict (all outputs from all agents in this cycle)
5. Compute and store post-mortem template (to be completed on trade close)
6. Update Compounding Governor's closed_trades_list view

---

### STEP 10 — PROMISE AUDITOR → FRIDAY CYCLE
**Agent:** `09_PROMISE_AUDITOR`
**Trigger:** Weekly (Friday Cycle) or threshold breach.
**Input:** Journal Learning data — trade records, scores, outcomes.
**Output:** Audit report delivered to Governance Layer.

**Actions:**
1. Compute expectancy by score band and compare week-over-week
2. Detect score drift (2 consecutive weeks of expectancy decline)
3. Audit PREMIUM classification predictive validity
4. Identify negative expectancy bands
5. Assess compounding accuracy
6. Produce findings with recommendations
7. Deliver Friday Cycle summary

---

## BLOCKING CONDITIONS

The following 6 conditions prevent execution at the relevant step and terminate the flow. No downstream agent runs after a block.

| # | Condition | Triggered By | Action |
|---|---|---|---|
| 1 | Asset on `LISTA_PROIBIDA` | Alert Radar | Immediate REJECTED — log as security event |
| 2 | `structural_status = NO_STRUCTURE` | Structure Hunter | Terminate — no valid zone to evaluate |
| 3 | `verdict = FAKEOUT` | Breakout Confirmation | Terminate — zone re-entry or wick-only break detected |
| 4 | `breakout_final_score` maps to `DISCARD` band (0–39) | Score Engine | Terminate — insufficient signal quality |
| 5 | Risk Guardian outputs `REJECTED` or `FREEZE` | Risk Guardian | Terminate — capital protection enforced |
| 6 | `plan_status = PLAN_REJECTED` | Tactical Execution | Terminate — plan fails execution feasibility check |

**All 6 blocking events are logged to Journal Learning as NON_EXECUTION records with the reason code of the blocking agent.**

---

## EXECUTION OUTPUTS

When all 10 steps complete successfully and a trade plan is produced, the final output package contains:

```yaml
execution_output:
  # Identity
  trade_id: string                  # UUID generated at Journal Learning storage
  asset: string
  direction: LONG | SHORT
  timeframe: string
  session: MORNING | ASIAN | MANUAL
  system_mode: READ_ONLY | SIMULATE | EXECUTE

  # Entry specification
  entry_type: string                # MARKET | LIMIT_RETEST | LIMIT_BREAKOUT
  entry_price: float                # specific price, not a range

  # Risk parameters
  stop_price: float                 # specific price, beyond zone boundary, ≥ 1x ATR from entry
  stop_type: string                 # BELOW_ZONE | ABOVE_ZONE | ATR_OFFSET | STRUCTURE

  # Targets
  target_price_t1: float            # mandatory — minimum 2:1 R:R
  target_price_t2: float | null
  target_price_t3: float | null
  partial_exit_t1_pct: int          # % of position to close at T1

  # Sizing
  size_modifier: float              # scaling factor from Compounding Governor (1.0 = base)
  approved_risk_pct: float          # from Risk Guardian
  approved_leverage: int

  # Quality context
  breakout_final_score: float
  classification_band: string       # VALID | STRONG | PREMIUM

  # Warning flags (always present — empty list if clean)
  warning_flags: list[string]

  # Downstream reference
  journal_record_id: string         # UUID of Journal Learning record
```

---

## READ_ONLY MODE BEHAVIOR

When `system_mode = READ_ONLY`:
- Alert Radar routes all signals as `OBSERVATION_ONLY` — no downstream activation
- Steps 02–09 do not run for incoming alerts
- All OBSERVATION_ONLY events are logged to Journal Learning as NON_EXECUTION records with `reason_code = READ_ONLY_BLOCK`
- Execution outputs are never produced in READ_ONLY mode
- Manual pipeline runs (for analysis) may proceed through Steps 02–07 in simulation mode, but must output `PLAN_OBSERVATION_ONLY` with no compounding or journal entry impact

# Euru OS — Risk Matrix

**Version:** Week 6
**Mode:** READ_ONLY (no real execution)
**Source of truth:** `01_GOVERNANCA/REGRAS_MAE_REVISADO.md`
**Last updated:** 2026-04-05

> Capital preservation is the absolute priority.
> When in doubt, the default is always `NO_TRADE`.

---

## 1. Position Sizing Formula

### Core formula

```
Position Size = (Capital × Risk%) / Stop Distance

where:
  Risk%          = 1% of available capital (hard cap)
  Stop Distance  = ATR(14) × 1.5
  ATR(14)        = Average True Range over 14 periods (from Flow Analyst)
```

### Step-by-step calculation

```
STEP 1 — Determine risk amount in currency
  Risk Amount = Capital × 0.01
  Example: €1,000 capital → Risk Amount = €10

STEP 2 — Calculate stop distance
  Stop Distance = ATR(14) × 1.5
  Example: ATR = €0.80 → Stop Distance = €1.20

STEP 3 — Calculate position size in units
  Units = Risk Amount / Stop Distance
  Example: €10 / €1.20 = 8.33 units of the asset

STEP 4 — Calculate position value in EUR/USDT
  Position Value = Units × Current Price
  Example: 8.33 × €12.50 = €104.17

STEP 5 — Verify against category allocation limit
  Position Value must not exceed category max exposure (see Section 2)
  If exceeded → reduce to category limit → recalculate units
```

### ATR examples

| Asset | Price | ATR(14) | Stop Distance (×1.5) | €500 capital / 1% risk | Position Value |
|-------|-------|---------|---------------------|----------------------|----------------|
| ETH   | €2,800 | €95    | €142.50             | €5 / €142.50 = 0.035 ETH | €98 |
| SOL   | €140  | €6.20   | €9.30               | €5 / €9.30 = 0.538 SOL   | €75 |
| NEAR  | €4.50 | €0.28   | €0.42               | €5 / €0.42 = 11.9 NEAR   | €54 |
| PEPE  | €0.000012 | €0.0000009 | €0.00000135 | €5 / €0.00000135 = 3.7M PEPE | €44 |

> ATR values are illustrative. Always use live ATR(14) from `euru_flow_analyst.py`.

### High-volatility adjustment

When ATR is unusually high (>3% of asset price), widen the multiplier:

```
Normal volatility:   Stop Distance = ATR × 1.5
High volatility:     Stop Distance = ATR × 2.0
```

The Flow Analyst flags this condition in `VOLUME_FLOW: STRONG` with abnormal ATR.

### Minimum R/R requirement

```
Minimum required:   1:2  → risk €1, target €2
Preferred:          1:3  → risk €1, target €3

Target 1 = Entry + (Stop Distance × 2)
Target 2 = Entry + (Stop Distance × 3)

If R/R < 1:2 → REJECT (Quant/Risk Officer hard rule, no exceptions)
```

---

## 2. Capital Distribution Table

### Aguiar Protocol — 5/5/90 Architecture (Module 02)

The total capital is divided into three protected layers before any category allocation:

```
┌─────────────────────────────────────────────────────────────────┐
│  TOTAL CAPITAL                                                  │
│                                                                 │
│  90% — LOCKED (spot wallet, untouched)                         │
│         Long-term holdings, never used for active trading       │
│                                                                 │
│   5% — ACTIVE POSITION POOL                                    │
│         Subject to category distribution below                  │
│                                                                 │
│   5% — MARGIN RESERVE                                          │
│         Buffer for fees, slippage, unexpected events           │
└─────────────────────────────────────────────────────────────────┘
```

The category distribution (50/25/15/10) applies **within the 5% Active Position Pool**.

### Category distribution (within Active Pool)

| Category | Allocation | Max of Active Pool | Assets | Max Positions |
|----------|------------|-------------------|--------|---------------|
| **Core** | 50% | 50% of active pool | ETH, SOL, BNB, LINK, AVAX, SUI, NEAR | 1 per asset |
| **Growth** | 25% | 25% of active pool | ARB, OP, TIA, POL, SEI, ATOM, STX | 1 per asset |
| **Asymmetric** | 15% | 15% of active pool | TAO, RENDER, FET, INJ, PYTH, ONDO | 1 per asset |
| **Speculative** | 10% | 10% of active pool — hard ceiling | DOGE, PEPE, BONK | 1 per asset |

> `enforce_max_speculative: true` — Speculative total can never exceed 10% of active pool under any circumstance.

### Numeric example (€1,000 total capital)

```
  Total Capital:           €1,000
  Active Pool (5%):           €50
  Margin Reserve (5%):        €50
  Locked (90%):              €900

  Within €50 Active Pool:
  ├── Core (50%):             €25   → e.g. up to €25 in ETH
  ├── Growth (25%):           €12.50 → e.g. up to €12.50 in ARB
  ├── Asymmetric (15%):        €7.50 → e.g. up to €7.50 in TAO
  └── Speculative (10%):       €5.00 → e.g. max €5.00 in PEPE
```

### Allocation enforcement rules

- A trade that would push any category above its allocation cap → `REJECT`
- Category percentage is calculated against the **current active pool value**, not original capital
- Rebalancing is triggered when any category drifts >5% from target (logged in Journal)
- No leverage beyond what is covered by the Margin Reserve

---

## 3. Risk Limits Table

These limits are hard rules defined in `REGRAS_MAE_REVISADO.md`. They cannot be overridden by any agent or operator without a Type 2 governance change (24h wait + dual approval).

### Hard limits

| Limit | Value | Enforcement | Breach action |
|-------|-------|-------------|---------------|
| **Risk per trade** | 1% of capital | Quant/Risk Officer | `REJECT` — do not enter |
| **Max daily loss** | 2% of capital | Quant/Risk Officer + Journal Auditor | Stop all trading, log incident |
| **Max weekly loss** | 5% of capital | Journal Auditor (weekly scorecard) | Full trading halt, governance review |
| **Max simultaneous positions** | 2 open at any time | Execution Orchestrator | `EXECUTION_BLOCKED` until a position closes |
| **Max trades per day** | 3 per calendar day | Execution Orchestrator | `EXECUTION_BLOCKED` for remainder of day |
| **R/R minimum** | 1:2 | Quant/Risk Officer | `REJECT` if R/R < 1:2 |
| **Stop-loss required** | Mandatory on all entries | All agents (prohibitions) | Trade not valid without stop |
| **Speculative cap** | 10% of active pool | Quant/Risk Officer | `REJECT` if cap would be exceeded |

### Dynamic risk scaling — Module 03

Risk per trade is further scaled down as daily trade count increases:

| Trades completed today | Risk per trade (of active pool) |
|------------------------|--------------------------------|
| 1st – 3rd trade        | 10% of active pool per trade   |
| 4th – 7th trade        | 7% of active pool per trade    |
| 8th trade and beyond   | 4–5% of active pool per trade  |

> This applies if trading frequency is high. In standard operation (max 3/day), the 1% capital rule is the binding constraint.

### No-trade conditions (automatic pipeline halt)

The pipeline must not produce `EXECUTION_ALLOWED` under any of these conditions:

```
- Operador cansado / unfocused operator
- Recent stop-loss sequence (3+ consecutive stops)
- Revenge trade mode detected
- Post-win euphoria
- BTC erratic / no clear direction
- Watchlist unclear or empty
```

---

## 4. Stop-Loss Rules

### ATR-based stop (primary method)

```
Stop Loss = Entry Price − (ATR(14) × 1.5)

Normal volatility:    multiplier = 1.5
High volatility:      multiplier = 2.0

Example (long trade):
  Entry price:    €12.50
  ATR(14):         €0.80
  Stop Distance:   €0.80 × 1.5 = €1.20
  Stop Loss:       €12.50 − €1.20 = €11.30
```

### Technical-level stop (secondary method)

When a clear technical support is available, the stop is placed below the **retested support level** rather than purely ATR-based:

```
Stop Loss = Technical support level − small buffer (0.5–1% below)

Conditions for use:
  - A clear prior support or resistance-turned-support is identifiable
  - The technical stop is not wider than ATR × 2.0
  - If technical stop < ATR stop → use technical stop
  - If technical stop > ATR × 2.0 → the setup is too risky → REJECT
```

The Scout identifies the technical level (`KEY_LEVELS: S`) and the Quant/Risk Officer selects whichever stop is tighter but technically valid.

### Absolute stop rules

| Rule | Detail |
|------|--------|
| **Never move stop away from entry** | Stop can only move toward entry (break-even) or in the direction of profit (trailing). Moving it further away is a hard prohibition. |
| **No stop = no trade** | `trade_without_stop: true` in prohibitions. A setup without a defined stop cannot receive `EXECUTION_ALLOWED`. |
| **Stop on close, not wick** | Stop is evaluated on candle **close**, not on intra-candle wick unless DevOps detects anomalous spike. |
| **Invalidation check before entry** | Scout must confirm the invalidation level. If price is already near the stop, the trade is not valid. |
| **Stop logged before execution** | Quant/Risk Officer must include `STOP_LOSS` price in output before Execution Orchestrator can proceed. |

---

## 5. Exit Policy Summary

Full policy: `07_OPERACAO/Politica_Saida_Completa_Euru.txt`

### Exit priority hierarchy

Exits are evaluated **at every 4H candle close** in this order:

| Priority | Trigger | Action | Agent |
|----------|---------|--------|-------|
| 1 | Stop-loss price hit | EXIT immediately — no exceptions | Quant/Risk Officer |
| 2 | Macro adverse event (News HIGH) | EXIT or reduce position immediately | News Sentinel |
| 3 | OBV + RSI bearish divergence (simultaneous) | EXIT immediately | Flow Analyst |
| 4 | MACD negative crossover | REDUCE position | Flow Analyst |
| 5 | Support level lost (candle close below) | EXIT immediately | Scout |
| 6 | Time stop (7 days, no movement) | CLOSE position | Journal Auditor |

> Rule: "Exits are governed by risk rules and confirmation that the move has lost strength. Never by emotion."

### Module 08 — 50% Securing

```
Trigger:  Position ROI ≥ 50%
Action:   Liquidate 50% of the position
Purpose:  Recover the cost of the operation; remaining 50% runs risk-free
Agent:    Execution Orchestrator
```

### Module 09 — Fibonacci Exit Matrix

```
Fibonacci levels calculated from entry to projected target zone:

  Level 0.382 — "The Pullback"
    Action: Take partial profit, prepare for resistance
    Note:   Tighten stop to break-even if not already there

  Level 0.500 — "The Withdrawal"
    Action: Extract second block (10% of remaining position)
    Note:   Intermediate milestone

  Level 0.618 — "The Breakthrough"
    Action: Let core position run indefinitely
    Note:   Strongest Fibonacci zone — if price holds here,
            the move has strong continuation potential
```

### Module 10 — 10% Harvesting

```
Trigger:  ROI ≥ 300% (and every additional 300% thereafter)
Action:   Extract 10% of remaining position

Schedule:
  ROI = 300% → extract 10%
  ROI = 600% → extract 10% of what remains
  ROI = 900% → extract 10% of what remains
  (continues recursively)

Purpose: Compound realised gains without closing winners
Agent:   Execution Orchestrator
```

### Trailing stop rules

```
Activation and progression:

  Position at +1R profit → move stop to break-even (entry price)
  Position at +2R profit → move stop to +1R above entry
  Position at +3R profit → move stop to +2R above entry

Formula (updated every 4H candle close):
  Trailing Stop = Current Price − (ATR(14) × 1.5)
  Rule: stop NEVER moves down — only up

Agent: Execution Orchestrator
```

### Time stop rules

```
Default (MAC tactical positions):  7 days without development → CLOSE
Short-term positions:              48–72 hours
Core positions:                    No time stop applied

Logic: Capital locked in a dead trade = lost opportunity in another asset
Agent: Journal Auditor (triggers TIME_STOP_TRIGGERED flag)
```

### Narrative cooling exit

```
Exit/reduce when ALL of the following are true:
  - Sector volume falls to < 50% of 7-day average
  - News Sentinel: 3+ consecutive days with no sector mention
  - Leading tokens in the sector are down >20% with no recovery
  - MAC Analyst detects rotation to a different sector

Action:
  - Reduce sector exposure by 50%
  - Retain only positions with positive ROI
  - Block new entries in the sector

Agent: News Sentinel + Scout
```

### Absolute exit prohibitions

```
1. Never hold a losing position hoping for recovery
2. Never close a winning position from fear without a technical trigger
3. Never move stop-loss further from entry
4. Never override a time stop on MAC tactical positions
5. Never ignore a simultaneous OBV + RSI divergence — always exit
```

---

## 6. Aguiar Protocol Modules Reference

The Aguiar Protocol is the methodological framework underlying all risk and position management in Euru OS. It defines capital architecture, scaling rules, and exit mechanics.

| Module | Name | What it enforces | Agent(s) |
|--------|------|-----------------|----------|
| **02** | 5/5/90 Capital Architecture | Total capital split: 90% locked in spot (untouched), 5% active position pool, 5% margin reserve. Protects the base from overexposure. | Quant/Risk Officer |
| **03** | Dynamic Risk Scaling | Risk per trade decreases as daily trade count rises: 10% of active pool (trades 1–3), 7% (trades 4–7), 4–5% (trade 8+). Prevents over-concentration on busy days. | Quant/Risk Officer + Execution Orchestrator |
| **08** | 50% Securing | At ROI ≥ 50%, liquidate half the position. Converts a winner into a cost-recovered trade. Remaining 50% is effectively free-running. | Execution Orchestrator |
| **09** | Fibonacci Exit Matrix | Structured partial exits at Fibonacci retracement levels (0.382 / 0.500 / 0.618). Ensures disciplined profit-taking without closing winners prematurely. | Execution Orchestrator + MAC/Playbook Analyst |
| **10** | 10% Harvesting | At every 300% ROI milestone, extract 10% of the remaining position. Compounds realised gains across multi-bagger positions. | Execution Orchestrator |

### Module interaction diagram

```
  Trade entry confirmed
        │
        ▼
  Module 02 ─── Is position within the 5% active pool limit? ──→ NO → REJECT
        │ YES
        ▼
  Module 03 ─── Apply dynamic risk % based on today's trade count
        │
        ▼
  Position open
        │
        ├── ROI ≥ +1R?   → Trailing stop to break-even (pre-module)
        ├── ROI ≥ 50%?   → MODULE 08: liquidate 50%
        ├── Fibonacci 0.382? → MODULE 09: partial + tighten stop
        ├── Fibonacci 0.500? → MODULE 09: second partial extraction
        ├── Fibonacci 0.618? → MODULE 09: core position runs free
        └── ROI ≥ 300%?  → MODULE 10: harvest 10% of remaining
```

---

*Canonical rules: `01_GOVERNANCA/REGRAS_MAE_REVISADO.md`*
*Exit policy: `07_OPERACAO/Politica_Saida_Completa_Euru.txt`*
*Quant/Risk Officer spec: `04_AGENTES/04_QUANT_RISK_OFFICER/BRIEFING_FINAL.md`*
*Aguiar method: `99_PRIVATE_NOTES/Metodo_Bruno_Aguiar_Sintese_Operacional.txt`*

# TACTICAL_EXECUTION — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 06_TACTICAL_EXECUTION
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Tactical Execution receives the full upstream evaluation package assembled after Risk Guardian outputs APPROVED. This includes all prior agent outputs in the current pipeline cycle.

**Required input fields:**

```
risk_guardian_verdict:
  verdict                     : APPROVED   # must be APPROVED to proceed
  approved_risk_pct           : float
  approved_leverage           : int

breakout_confirmation_verdict:
  verdict                     : CONFIRMED | WEAK_BREAKOUT
  quality_score               : int        # 0–10
  direction                   : LONG | SHORT

structure_hunter_report:
  zones                       : list[Zone] # active zones for stop/target placement
  formation                   : Formation

market_regime_report:
  regime                      : string
  breakout_favorability       : string
  btc_alignment_score         : float

trade_parameters:
  asset                       : string
  timeframe                   : string
  entry_price_current         : float      # current market price
  current_atr14               : float
  typical_spread_pct          : float      # as % of entry price
  account_equity_usdt         : float
  system_mode                 : READ_ONLY | SIMULATE | EXECUTE
```

---

## OUTPUTS

A **Complete Trade Plan** forwarded to Compounding Governor and Journal Learning simultaneously. See OUTPUT_FORMAT.md for full schema.

**Plan status values:** `PLAN_READY`, `PLAN_REJECTED`, `PLAN_OBSERVATION_ONLY`

---

## VALID SITUATIONS

**Scenario A — Market entry, momentum breakout:**
- BTCUSDT 4H, CONFIRMED quality_score = 9, regime = TREND_BULL, ATR = 850 USDT, entry = 71,200.
- Stop: 70,280 (below zone base, = 1.08x ATR). T1: 72,500 (next resistance, R:R = 1.4:1 — wait, check). Need T1 ≥ 2x risk distance. Risk = 920. T1 must be ≥ 71,200 + 1,840 = 73,040. Assign T1 = 73,200.
- Entry type: MARKET. Scale-in: not applicable. Partial: T1 = 40%.
- Result: PLAN_READY, warning_flags = []

**Scenario B — WEAK_BREAKOUT, limit retest:**
- ETHUSDT 4H, WEAK_BREAKOUT quality_score = 6, regime = SIDEWAYS_COMPRESSION.
- Entry type: LIMIT_RETEST at zone top (3,192). Stop: 3,142 (1.04x ATR). T1: 3,300 (R:R = 2.16:1 — PASS).
- Result: PLAN_READY, warning_flags = ["WEAK_BREAKOUT_PLAN"]

**Scenario C — PLAN_REJECTED (R:R below minimum):**
- Entry at 3,200, stop at 3,185 (15 pts risk). T1 at 3,210 (10 pts reward). R:R = 0.67:1.
- Hard constraint → PLAN_REJECTED, flag: RR_BELOW_MINIMUM

**Scenario D — CHOPPY regime forces LIMIT_ONLY:**
- SOLUSDT, regime = CHOPPY. Breakout quality = 7.
- Entry type forced to LIMIT_RETEST. Add `CHOPPY_REGIME_LIMIT` to warning_flags.

---

## INVALID SITUATIONS

**Plan without entry_type:**
- Any plan output where `entry_type` field is null or absent.
- Invalid. Hard constraint. Every plan requires `entry_type`.

**warning_flags field omitted:**
- Plan output where `warning_flags` key is absent entirely.
- Invalid. Field must be present. Use empty list `[]` if no warnings apply.

**Stop inside zone:**
- Stop placed at 3,185 when zone band is 3,180–3,200. Stop is inside the zone.
- Invalid. Stop must be placed beyond zone boundary, not within it.

**Plan produced without Risk Guardian APPROVED:**
- Breakout Confirmation is CONFIRMED but Risk Guardian verdict was REJECTED.
- Invalid. Tactical Execution only processes APPROVED packages from Risk Guardian.

---

## NOTES

- Tactical Execution is the **final analytical agent** in the pipeline before the plan becomes active.
- Both Compounding Governor and Journal Learning receive the plan simultaneously — not sequentially.
- The upstream package contains all necessary data for plan construction. No additional API calls are required by this agent.
- `warning_flags` accumulates all warnings from every check in the plan construction process. Do not discard early warnings because later checks pass.

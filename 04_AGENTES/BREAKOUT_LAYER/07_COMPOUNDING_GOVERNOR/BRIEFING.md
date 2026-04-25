# COMPOUNDING_GOVERNOR — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 07_COMPOUNDING_GOVERNOR
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Compounding Governor receives the completed trade plan from Tactical Execution plus performance history from Journal Learning.

**From Tactical Execution (per trade plan):**
```
trade_plan:
  trade_id                    : string
  asset                       : string
  direction                   : LONG | SHORT
  plan_status                 : PLAN_READY
  approved_risk_pct           : float
  system_mode                 : string
```

**From Journal Learning (performance state):**
```
performance_state:
  consecutive_wins            : int          # closed profitable trades in current streak
  consecutive_losses          : int          # closed losing trades in current streak
  drawdown_current_pct        : float        # active drawdown from equity peak
  fakeout_rate_last20_pct     : float        # % fakeouts in last 20 routed signals
  current_scaling_factor      : float        # 1.0 = base, 1.25 = one step up
  current_approved_risk_pct   : float
  freeze_state                : NONE | COMPOUNDING_FREEZE
  last_friday_cycle_date      : string       # ISO-8601 date
  trades_this_week            : int
  scale_up_events_this_week   : int
  system_phase                : READ_ONLY | SIMULATE | EXECUTE
```

---

## OUTPUTS

A **Scaling Posture Report** sent to Journal Learning. See OUTPUT_FORMAT.md for full schema.

**Scaling verdict values:** `SCALE_UP`, `HOLD`, `SCALE_DOWN`, `COMPOUNDING_FREEZE`

---

## VALID SITUATIONS

**Scenario A — SCALE_UP approved:**
- Consecutive wins = 6. Active drawdown = 0%. Fakeout rate = 22%. Scaling factor = 1.0. No scale-up events this week yet. Last Friday Cycle 5 days ago.
- All criteria met → `SCALE_UP`. New factor = 1.25.

**Scenario B — HOLD (streak insufficient):**
- Consecutive wins = 3 (below threshold of 5). Drawdown = 0%. Fakeout rate = 28%.
- Streak criterion not met → `HOLD`. Maintain current sizing.

**Scenario C — COMPOUNDING_FREEZE (active drawdown):**
- Consecutive wins = 7 — excellent streak. But active drawdown = 0.8% from equity peak.
- Hard constraint: any drawdown blocks compounding → `COMPOUNDING_FREEZE`.

**Scenario D — COMPOUNDING_FREEZE (fakeout rate):**
- Consecutive wins = 5. Drawdown = 0%. But fakeout rate = 43% (last 20 signals).
- Fakeout rate exceeds 40% threshold → `COMPOUNDING_FREEZE`.

**Scenario E — Second SCALE_UP blocked:**
- Scale_up_events_this_week = 1. System requests second SCALE_UP. Last Friday Cycle = 5 days ago (same week).
- → `HOLD`. Friday Cycle review gate required before second step.

---

## INVALID SITUATIONS

**Compounding on hypothetical trades:**
- User asks Governor to count 4 "would have been profitable" observations from READ_ONLY mode toward the 5-win requirement.
- Invalid. Only closed, executed trades count. Observations carry zero weight.

**Lifting freeze based on time elapsed:**
- Freeze has been active for 3 days. No wins. No performance recovery. User requests freeze lift because "market has improved."
- Invalid. Freeze release requires objective criteria: 0% drawdown + fakeout rate < 40% + ≥ 5 consecutive wins.

**Accepting SCALE_DOWN request during positive streak:**
- User requests SCALE_DOWN to reduce risk while the system is in a 7-win streak with 0% drawdown.
- Valid action (user can always reduce risk manually), but Governor's own assessment = `HOLD` or `SCALE_UP`. Log the discrepancy in notes.

---

## NOTES

- Governor's posture is re-evaluated on every `POST_TRADE` event and at every `SESSION_START`.
- `scale_up_events_this_week` resets every Friday Cycle.
- If Journal Learning performance state is unavailable, output `HOLD` with flag `PERFORMANCE_DATA_UNAVAILABLE`.
- Governor sends sizing changes to Risk Guardian asynchronously after every SCALE_UP or SCALE_DOWN verdict.

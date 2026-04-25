# TACTICAL_EXECUTION — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 06_TACTICAL_EXECUTION
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
tactical_execution_plan:
  version: "1.0.0"
  timestamp: string              # ISO-8601 UTC
  asset: string
  direction: string              # LONG | SHORT
  timeframe: string
  system_mode: string            # READ_ONLY | SIMULATE | EXECUTE

  plan_status: string            # see PLAN STATUS VALUES
  plan_confidence: float         # 0.0–1.0

  entry:
    entry_type: string           # MARKET | LIMIT_RETEST | LIMIT_BREAKOUT — REQUIRED
    price: float
    rationale: string            # MOMENTUM | RETEST | COMPRESSION_RELEASE | MANUAL
    spread_pct: float

  stop_loss:
    price: float
    type: string                 # BELOW_ZONE | ABOVE_ZONE | ATR_OFFSET | STRUCTURE
    atr_multiple_from_entry: float
    distance_pct_from_entry: float

  scale_in:
    enabled: bool
    legs:
      - leg: int
        price: float
        risk_allocation_pct: float

  targets:
    t1:
      price: float
      basis: string              # NEXT_RESISTANCE | NEXT_SUPPORT | MEASURED_MOVE | FIBONACCI
      risk_reward_ratio: float
      partial_exit_pct: int      # % of position to close
    t2:
      price: float
      basis: string
      risk_reward_ratio: float
      partial_exit_pct: int
    t3:
      price: float
      basis: string
      risk_reward_ratio: float
      partial_exit_pct: int      # remainder — trail stop activates here

  trail_stop:
    enabled: bool
    activation: string           # T1_HIT | T2_HIT | MANUAL
    method: string               # ATR_MULTIPLE | STRUCTURE_BASED
    atr_multiple: float | null

  risk_summary:
    approved_risk_pct: float
    approved_leverage: int
    max_loss_usdt_estimate: float
    rr_at_t1: float
    rr_at_t3: float

  warning_flags: list[string]    # REQUIRED — use [] if none. Never omit this field.

  rejection_details:
    reason_code: string | null   # see REJECTION CODES
    detail: string | null

  notes: string                  # optional, max 100 words
```

---

## PLAN STATUS VALUES

| Value | Meaning |
|---|---|
| `PLAN_READY` | Complete plan — forward to Compounding Governor and Journal Learning |
| `PLAN_REJECTED` | Plan fails a hard constraint — not forwarded |
| `PLAN_OBSERVATION_ONLY` | System in READ_ONLY — plan logged, not actionable |

---

## ENTRY TYPE VALUES

| Value | When to Use |
|---|---|
| `MARKET` | Strong momentum confirmation (quality_score ≥ 8, regime TREND) |
| `LIMIT_RETEST` | Waiting for price to pull back to zone after breakout |
| `LIMIT_BREAKOUT` | Limit order placed just above/below zone for capture at breakout |

---

## CONFIDENCE LEVELS

| plan_confidence | Condition |
|---|---|
| 0.85–1.0 | CONFIRMED quality ≥ 8, regime FAVORABLE, all checks clean |
| 0.65–0.84 | CONFIRMED quality 6–7, or regime CONDITIONAL |
| 0.45–0.64 | WEAK_BREAKOUT upstream, warning flags present |
| < 0.45 | Should trigger PLAN_REJECTED in most cases |

---

## REJECTION CODES

| Code | Trigger |
|---|---|
| `RR_BELOW_MINIMUM` | Any target < 2:1 R:R after spread |
| `STOP_TOO_TIGHT` | Stop < 1x ATR from entry |
| `NO_RISK_APPROVAL` | Risk Guardian verdict was not APPROVED |
| `NO_TARGET_LEVEL` | No structural level available for T1 |
| `SCALE_IN_RISK_EXCEEDED` | Combined legs push risk above approved limit |

---

## WARNING FLAG VALUES

| Flag | Condition |
|---|---|
| `HIGH_SPREAD_WARNING` | Spread > 0.3% — actual R:R lower than displayed |
| `CHOPPY_REGIME_LIMIT` | Regime = CHOPPY — entry forced to LIMIT_RETEST |
| `WEAK_BREAKOUT_PLAN` | Upstream verdict = WEAK_BREAKOUT |
| `ATR_STOP_WIDENED` | Stop widened from proposed to meet 1x ATR minimum |
| `T3_SPECULATIVE` | T3 target beyond identifiable structural level |
| `BTC_MISALIGNED` | BTC alignment score < 0.5 |

---

## EXAMPLE — PLAN_READY

```yaml
tactical_execution_plan:
  version: "1.0.0"
  timestamp: "2026-04-15T09:45:00Z"
  asset: "ETHUSDT"
  direction: "LONG"
  timeframe: "4H"
  system_mode: "SIMULATE"
  plan_status: "PLAN_READY"
  plan_confidence: 0.87
  entry:
    entry_type: "MARKET"
    price: 3205.00
    rationale: "MOMENTUM"
    spread_pct: 0.04
  stop_loss:
    price: 3140.00
    type: "BELOW_ZONE"
    atr_multiple_from_entry: 1.35
    distance_pct_from_entry: 2.03
  scale_in:
    enabled: false
    legs: []
  targets:
    t1:
      price: 3335.00
      basis: "NEXT_RESISTANCE"
      risk_reward_ratio: 2.0
      partial_exit_pct: 40
    t2:
      price: 3480.00
      basis: "MEASURED_MOVE"
      risk_reward_ratio: 4.2
      partial_exit_pct: 35
    t3:
      price: 3650.00
      basis: "NEXT_RESISTANCE"
      risk_reward_ratio: 6.8
      partial_exit_pct: 25
  trail_stop:
    enabled: true
    activation: "T1_HIT"
    method: "ATR_MULTIPLE"
    atr_multiple: 1.5
  risk_summary:
    approved_risk_pct: 0.80
    approved_leverage: 2
    max_loss_usdt_estimate: 160.00
    rr_at_t1: 2.0
    rr_at_t3: 6.8
  warning_flags: []
  rejection_details:
    reason_code: null
    detail: null
  notes: "Market entry at breakout. Stop below zone base. T1 mandatory partial. Trail activated at T1."
```

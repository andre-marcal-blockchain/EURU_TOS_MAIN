# TACTICAL_EXECUTION — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 06
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
tactical_execution_plan:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  asset: "<SYMBOL>"
  direction: "<LONG | SHORT>"
  timeframe: "<1D | 4H | 1H>"
  system_mode: "<READ_ONLY | SIMULATE | EXECUTE>"

  plan_status: "<PLAN_READY | PLAN_REJECTED | PLAN_BLOCKED | PLAN_OBSERVATION_ONLY>"
  plan_confidence: <0.0–1.0>

  entry:
    type: "<MARKET | LIMIT_RETEST | LIMIT_BREAKOUT | SCALE_IN>"
    primary_entry_price: <float>
    entry_rationale: "<MOMENTUM | RETEST | COMPRESSION_RELEASE | MANUAL>"
    spread_pct: <float>
    spread_warning: <true | false>

  scale_in:
    enabled: <true | false>
    legs:
      - leg: 1
        price: <float>
        risk_allocation_pct: <float>
      - leg: 2
        price: <float>
        risk_allocation_pct: <float>

  stop_loss:
    price: <float>
    type: "<BELOW_ZONE | ABOVE_ZONE | ATR_OFFSET | STRUCTURE_LOW | STRUCTURE_HIGH>"
    atr_multiple_from_entry: <float>
    distance_from_entry_pct: <float>

  targets:
    t1:
      price: <float>
      basis: "<NEXT_RESISTANCE | NEXT_SUPPORT | MEASURED_MOVE | FIBONACCI>"
      risk_reward_ratio: <float>
      partial_exit_pct: <int>          # % of position to close at T1
    t2:
      price: <float>
      basis: "<NEXT_RESISTANCE | NEXT_SUPPORT | MEASURED_MOVE | FIBONACCI>"
      risk_reward_ratio: <float>
      partial_exit_pct: <int>
    t3:
      price: <float>
      basis: "<NEXT_RESISTANCE | NEXT_SUPPORT | MEASURED_MOVE | FIBONACCI>"
      risk_reward_ratio: <float>
      partial_exit_pct: <int>          # remainder — trail stop activated

  trail_stop:
    enabled: <true | false>
    activation_trigger: "<T1_HIT | T2_HIT | MANUAL>"
    trail_method: "<ATR_MULTIPLE | STRUCTURE_BASED>"
    trail_atr_multiple: <float>

  risk_summary:
    approved_risk_pct: <float>
    approved_leverage: <int>
    max_loss_usdt_estimate: <float>
    best_case_rr_t1: <float>
    best_case_rr_t3: <float>

  regime_context:
    regime: "<string>"
    breakout_favorability: "<string>"
    target_adjustment_applied: <true | false>

  rejection_details:
    reason_code: "<PLAN_REJECTION_CODE | null>"
    detail: "<string | null>"

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 100 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `plan_status` | enum | `PLAN_READY`, `PLAN_REJECTED`, `PLAN_BLOCKED`, `PLAN_OBSERVATION_ONLY` |
| `entry.type` | enum | `MARKET`, `LIMIT_RETEST`, `LIMIT_BREAKOUT`, `SCALE_IN` |
| `stop_loss.type` | enum | `BELOW_ZONE`, `ABOVE_ZONE`, `ATR_OFFSET`, `STRUCTURE_LOW`, `STRUCTURE_HIGH` |
| `targets.basis` | enum | `NEXT_RESISTANCE`, `NEXT_SUPPORT`, `MEASURED_MOVE`, `FIBONACCI` |
| `trail_stop.activation_trigger` | enum | `T1_HIT`, `T2_HIT`, `MANUAL` |
| `trail_stop.trail_method` | enum | `ATR_MULTIPLE`, `STRUCTURE_BASED` |

---

## PLAN REJECTION CODES

| Code | Meaning |
|---|---|
| `RR_BELOW_MINIMUM` | Risk/reward ratio < 2:1 after spread |
| `STOP_INSIDE_ZONE` | Stop-loss placed inside the breakout zone |
| `NO_CONFIRMED_VERDICT` | Breakout Confirmation verdict not CONFIRMED |
| `NO_RISK_APPROVAL` | Risk Guardian verdict not APPROVED |
| `NO_TARGET_LEVEL` | No valid structural target identifiable |
| `SCALE_IN_RISK_EXCEEDED` | Combined scale-in risk exceeds approved limit |

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `HIGH_SPREAD_WARNING` | Spread > 0.3% — actual R:R may be lower than shown |
| `CHOPPY_REGIME_ADJUSTMENT` | Targets reduced due to CHOPPY market regime |
| `ATR_STOP_WIDENED` | Stop widened post-spike — slippage risk noted |
| `T3_SPECULATIVE` | T3 target is beyond observable structure |
| `PLAN_OBSERVATION_ONLY` | System in READ_ONLY — plan logged but not actionable |

---

## EXAMPLE OUTPUT

```yaml
tactical_execution_plan:
  version: "1.0.0"
  timestamp: "2026-04-15T09:45:00Z"
  asset: "ETHUSDT"
  direction: "LONG"
  timeframe: "4H"
  system_mode: "SIMULATE"
  plan_status: "PLAN_READY"
  plan_confidence: 0.88
  entry:
    type: "MARKET"
    primary_entry_price: 3205.00
    entry_rationale: "MOMENTUM"
    spread_pct: 0.04
    spread_warning: false
  scale_in:
    enabled: false
    legs: []
  stop_loss:
    price: 3140.00
    type: "BELOW_ZONE"
    atr_multiple_from_entry: 1.35
    distance_from_entry_pct: 2.03
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
    activation_trigger: "T1_HIT"
    trail_method: "ATR_MULTIPLE"
    trail_atr_multiple: 1.5
  risk_summary:
    approved_risk_pct: 0.80
    approved_leverage: 2
    max_loss_usdt_estimate: 160.00
    best_case_rr_t1: 2.0
    best_case_rr_t3: 6.8
  regime_context:
    regime: "SIDEWAYS_COMPRESSION"
    breakout_favorability: "PENDING_EXPANSION"
    target_adjustment_applied: false
  rejection_details:
    reason_code: null
    detail: null
  failure_flags: []
  notes: "Clean plan. Market entry at breakout. Stop below zone base. T1 mandatory partial. Trail activated at T1."
```

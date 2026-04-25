# COMPOUNDING_GOVERNOR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 07
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
compounding_governor_report:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  system_phase: "<READ_ONLY | SIMULATE | EXECUTE>"
  evaluation_trigger: "<POST_TRADE | SESSION_START | FRIDAY_CYCLE | MANUAL>"

  scaling_verdict: "<SCALE_UP | HOLD | SCALE_DOWN | COMPOUNDING_FREEZE | FULL_FREEZE>"
  verdict_confidence: <0.0–1.0>

  current_state:
    previous_scaling_factor: <float>
    new_scaling_factor: <float>
    previous_approved_risk_pct: <float>
    new_approved_risk_pct: <float>
    freeze_state: "<NONE | COMPOUNDING_FREEZE | FULL_FREEZE>"
    freeze_reason: "<string | null>"

  performance_metrics:
    trades_evaluated: <int>
    win_count: <int>
    loss_count: <int>
    win_rate_pct: <float>
    avg_r_achieved: <float>
    consecutive_wins: <int>
    consecutive_losses: <int>
    drawdown_7d_pct: <float>
    drawdown_14d_pct: <float>

  criteria_check:
    consecutive_wins_threshold:
      required: 3
      current: <int>
      status: "<MET | NOT_MET>"

    win_rate_threshold:
      required_pct: 55.0
      current_pct: <float>
      status: "<MET | NOT_MET>"

    drawdown_safe:
      threshold_pct: 3.0
      current_pct: <float>
      status: "<PASS | CAUTION | FAIL>"

    friday_cycle_gate:
      required_for_consecutive_scale_up: <true | false>
      last_friday_cycle: "<ISO-8601 date>"
      gate_cleared: <true | false>

  freeze_release_conditions:
    applicable: <true | false>
    required_consecutive_wins: 2
    required_drawdown_max_pct: 2.0
    current_consecutive_wins: <int>
    current_drawdown_7d_pct: <float>
    release_eligible: <true | false>

  next_review:
    trigger: "<NEXT_TRADE_CLOSE | FRIDAY_CYCLE | MANUAL>"
    scale_up_eligible_after: "<condition description>"

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 100 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `scaling_verdict` | enum | `SCALE_UP`, `HOLD`, `SCALE_DOWN`, `COMPOUNDING_FREEZE`, `FULL_FREEZE` |
| `freeze_state` | enum | `NONE`, `COMPOUNDING_FREEZE`, `FULL_FREEZE` |
| `evaluation_trigger` | enum | `POST_TRADE`, `SESSION_START`, `FRIDAY_CYCLE`, `MANUAL` |
| `drawdown_safe.status` | enum | `PASS`, `CAUTION`, `FAIL` |

---

## SCALING FACTOR RULES

| Verdict | Scaling Factor Change | Max Step |
|---|---|---|
| `SCALE_UP` | × 1.25 | Max 2 steps before Friday Cycle gate |
| `HOLD` | No change | — |
| `SCALE_DOWN` | × 0.75 | Minimum floor = 0.5 × base |
| `COMPOUNDING_FREEZE` | No change to current | Cannot SCALE_UP until released |
| `FULL_FREEZE` | Defers to Risk Guardian | All position sizing frozen |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INSUFFICIENT_TRADE_HISTORY` | Fewer than 3 closed trades available for evaluation |
| `CONSECUTIVE_WIN_THRESHOLD_NOT_MET` | Need 3 consecutive wins — current streak insufficient |
| `WIN_RATE_BELOW_THRESHOLD` | Win rate < 55% over last 10 trades |
| `DRAWDOWN_CAUTION` | Drawdown 7d between 3–5% — caution mode |
| `DRAWDOWN_FREEZE_TRIGGER` | Drawdown 7d > 5% — defer to Risk Guardian |
| `CONSECUTIVE_SCALE_UP_BLOCKED` | Second scale-up requires Friday Cycle review first |
| `HYPOTHETICAL_TRADES_EXCLUDED` | Un-executed SIMULATE observations not counted |
| `FREEZE_RELEASE_NOT_ELIGIBLE` | Recovery criteria not yet met — freeze maintained |

---

## EXAMPLE OUTPUT — SCALE_UP

```yaml
compounding_governor_report:
  version: "1.0.0"
  timestamp: "2026-04-15T16:30:00Z"
  system_phase: "SIMULATE"
  evaluation_trigger: "POST_TRADE"
  scaling_verdict: "SCALE_UP"
  verdict_confidence: 0.91
  current_state:
    previous_scaling_factor: 1.0
    new_scaling_factor: 1.25
    previous_approved_risk_pct: 0.80
    new_approved_risk_pct: 1.00
    freeze_state: "NONE"
    freeze_reason: null
  performance_metrics:
    trades_evaluated: 10
    win_count: 7
    loss_count: 3
    win_rate_pct: 70.0
    avg_r_achieved: 2.4
    consecutive_wins: 4
    consecutive_losses: 0
    drawdown_7d_pct: 0.8
    drawdown_14d_pct: 1.1
  criteria_check:
    consecutive_wins_threshold:
      required: 3
      current: 4
      status: "MET"
    win_rate_threshold:
      required_pct: 55.0
      current_pct: 70.0
      status: "MET"
    drawdown_safe:
      threshold_pct: 3.0
      current_pct: 0.8
      status: "PASS"
    friday_cycle_gate:
      required_for_consecutive_scale_up: false
      last_friday_cycle: "2026-04-11"
      gate_cleared: true
  freeze_release_conditions:
    applicable: false
    required_consecutive_wins: 2
    required_drawdown_max_pct: 2.0
    current_consecutive_wins: 4
    current_drawdown_7d_pct: 0.8
    release_eligible: false
  next_review:
    trigger: "FRIDAY_CYCLE"
    scale_up_eligible_after: "Next SCALE_UP requires Friday Cycle review (consecutive step rule)."
  failure_flags: []
  notes: "All criteria met. First compounding step approved. Next scale-up gated by Friday Cycle review."
```

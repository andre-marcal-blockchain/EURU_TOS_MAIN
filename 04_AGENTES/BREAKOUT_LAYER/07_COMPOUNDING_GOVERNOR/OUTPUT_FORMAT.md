# COMPOUNDING_GOVERNOR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 07_COMPOUNDING_GOVERNOR
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
compounding_governor_report:
  version: "1.0.0"
  timestamp: string              # ISO-8601 UTC
  system_phase: string           # READ_ONLY | SIMULATE | EXECUTE
  evaluation_trigger: string     # POST_TRADE | SESSION_START | FRIDAY_CYCLE | MANUAL

  scaling_verdict: string        # see VERDICT VALUES
  verdict_confidence: float      # 0.0–1.0

  current_state:
    previous_scaling_factor: float
    new_scaling_factor: float
    previous_approved_risk_pct: float
    new_approved_risk_pct: float
    freeze_state: string         # NONE | COMPOUNDING_FREEZE

  performance_snapshot:
    consecutive_wins: int
    consecutive_losses: int
    drawdown_current_pct: float
    fakeout_rate_last20_pct: float
    scale_up_events_this_week: int

  criteria_check:
    consecutive_wins:
      required: int              # 5
      current: int
      status: string             # MET | NOT_MET

    drawdown_clear:
      threshold_pct: float       # 0.0 — any drawdown blocks
      current_pct: float
      status: string             # PASS | FAIL

    fakeout_rate:
      threshold_pct: float       # 40.0
      current_pct: float
      status: string             # PASS | FAIL

    friday_cycle_gate:
      required: bool
      last_friday_cycle: string  # ISO-8601 date
      gate_cleared: bool

  freeze_release_conditions:
    applicable: bool
    conditions_met: bool
    outstanding:
      - condition: string
        current_value: float | int
        required_value: float | int

  failure_flags: list[FailureFlag]
  notes: string                  # optional, max 100 words
```

**FailureFlag object:**
```yaml
flag: string
detail: string
```

---

## VERDICT VALUES

| Value | Meaning |
|---|---|
| `SCALE_UP` | All criteria met — increase sizing by +25% |
| `HOLD` | Criteria not fully met — maintain current sizing |
| `SCALE_DOWN` | Performance degraded — reduce sizing by 25% |
| `COMPOUNDING_FREEZE` | Drawdown or fakeout rate too high — block all scaling |

---

## SCALING FACTOR TABLE

| Verdict | Factor Change | Notes |
|---|---|---|
| `SCALE_UP` | × 1.25 | Maximum 2 steps before Friday Cycle gate |
| `HOLD` | No change | |
| `SCALE_DOWN` | × 0.75 | Minimum floor = 0.50 × base |
| `COMPOUNDING_FREEZE` | No change | Cannot SCALE_UP until freeze released |

---

## CONFIDENCE LEVELS

| verdict_confidence | Condition |
|---|---|
| 1.0 | Hard constraint triggered (e.g., drawdown > 0, fakeout > 40%) |
| 0.8–0.99 | All criteria clearly met or not met |
| 0.6–0.79 | One criterion borderline |
| < 0.6 | Insufficient data — default to HOLD |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `STREAK_INSUFFICIENT` | Consecutive wins < 5 |
| `ACTIVE_DRAWDOWN` | Current drawdown > 0% — compounding blocked |
| `FAKEOUT_RATE_HIGH` | Fakeout rate > 40% |
| `FAKEOUT_RATE_CRITICAL` | Fakeout rate > 60% |
| `FRIDAY_CYCLE_GATE` | Second scale-up requires Friday Cycle review |
| `HYPOTHETICAL_TRADES_EXCLUDED` | Un-executed observations not counted |
| `FREEZE_RELEASE_NOT_ELIGIBLE` | Recovery criteria not yet met |
| `PERFORMANCE_DATA_UNAVAILABLE` | Journal Learning state not accessible |

---

## EXAMPLE — SCALE_UP

```yaml
compounding_governor_report:
  version: "1.0.0"
  timestamp: "2026-04-15T16:30:00Z"
  system_phase: "SIMULATE"
  evaluation_trigger: "POST_TRADE"
  scaling_verdict: "SCALE_UP"
  verdict_confidence: 0.94
  current_state:
    previous_scaling_factor: 1.0
    new_scaling_factor: 1.25
    previous_approved_risk_pct: 0.80
    new_approved_risk_pct: 1.00
    freeze_state: "NONE"
  performance_snapshot:
    consecutive_wins: 6
    consecutive_losses: 0
    drawdown_current_pct: 0.0
    fakeout_rate_last20_pct: 22.0
    scale_up_events_this_week: 0
  criteria_check:
    consecutive_wins:
      required: 5
      current: 6
      status: "MET"
    drawdown_clear:
      threshold_pct: 0.0
      current_pct: 0.0
      status: "PASS"
    fakeout_rate:
      threshold_pct: 40.0
      current_pct: 22.0
      status: "PASS"
    friday_cycle_gate:
      required: false
      last_friday_cycle: "2026-04-11"
      gate_cleared: true
  freeze_release_conditions:
    applicable: false
    conditions_met: false
    outstanding: []
  failure_flags: []
  notes: "All criteria met. First compounding step approved. Next step requires Friday Cycle gate."
```

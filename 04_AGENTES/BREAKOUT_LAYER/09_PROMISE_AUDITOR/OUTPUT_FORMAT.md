# PROMISE_AUDITOR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 09_PROMISE_AUDITOR
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
promise_auditor_report:
  version: "1.0.0"
  report_id: string              # UUID
  generated_at: string           # ISO-8601 UTC
  audit_period:
    start: string                # ISO-8601 date
    end: string
  system_phase: string
  audit_trigger: string          # FRIDAY_CYCLE | THRESHOLD_BREACH | MANUAL

  audit_verdict: string          # CLEAN | FLAGS_DETECTED | INSUFFICIENT_DATA
  severity: string               # NONE | LOW | MEDIUM | HIGH | CRITICAL
  trades_evaluated: int
  non_executions_evaluated: int

  expectancy_trend:
    week_1: float | null         # oldest in window
    week_2: float | null
    week_3: float | null
    week_4: float | null         # most recent
    drift_detected: bool         # true if 2+ consecutive weekly declines
    drift_direction: string      # DECLINING | STABLE | IMPROVING | INSUFFICIENT_DATA

  score_band_analysis:
    - band: string               # e.g., "20-24", "25-29", "30-35"
      sample_size: int
      win_rate_pct: float
      avg_win_r: float
      avg_loss_r: float
      expectancy: float          # (win_rate * avg_win) - (loss_rate * avg_loss)
      expectancy_status: string  # POSITIVE | NEGATIVE | NEUTRAL

  premium_vs_standard:
    premium_sample: int
    premium_win_rate_pct: float
    standard_sample: int
    standard_win_rate_pct: float
    spread_pct: float            # premium_win_rate - standard_win_rate
    classification_predictive: bool

  score_inflation_check:
    avg_score_period_start: float
    avg_score_period_end: float
    score_drift_pts: float
    win_rate_change_pct: float   # positive = improving, negative = declining
    inflation_detected: bool
    inflation_severity: string   # NONE | LOW | MEDIUM | HIGH

  compounding_accuracy:
    scale_up_events: int
    periods_outperformed: int
    accuracy_pct: float
    verdict: string              # ACCURATE | MARGINAL | MISALIGNED | INSUFFICIENT_DATA

  findings:
    - finding_id: string         # e.g., "F001"
      flag_code: string          # see FLAG CODES
      severity: string           # LOW | MEDIUM | HIGH | CRITICAL
      repeat_count: int          # 1 = first occurrence, 2+ = repeat
      evidence:
        metric: string
        observed: float | string
        expected: float | string
        delta: float | null
        sample_size: int
        trade_ids: list[string]
      recommendation: string     # max 80 words — specific and actionable
      escalation_required: bool

  failure_flags: list[FailureFlag]

  friday_cycle_summary: string   # max 250 words — human-readable governance narrative
```

**FailureFlag object:**
```yaml
flag: string
detail: string
```

---

## AUDIT VERDICT VALUES

| Value | Meaning |
|---|---|
| `CLEAN` | No flags detected — system performing as expected |
| `FLAGS_DETECTED` | One or more findings present |
| `INSUFFICIENT_DATA` | Fewer than 10 trades in period — cannot audit |

---

## SEVERITY SCALE

| Severity | Condition |
|---|---|
| `NONE` | Clean audit |
| `LOW` | Marginal drift or borderline finding — monitor |
| `MEDIUM` | Clear pattern requiring review within 1 cycle |
| `HIGH` | Significant misalignment — action required this Friday |
| `CRITICAL` | Negative expectancy band or PREMIUM classification invalid — immediate action |

---

## CONFIDENCE LEVELS

Promise Auditor does not output `confidence` per finding. Instead, evidence quality is expressed through `sample_size` — findings with sample_size < 10 are not surfaced. Findings with sample_size 10–19 are labeled LOW severity maximum. Medium/High severity requires sample_size ≥ 20.

---

## FLAG CODES

| Code | Trigger |
|---|---|
| `PREMIUM_PERFORMANCE_UNSUPPORTED` | PREMIUM win rate ≤ STANDARD win rate |
| `SCORE_DRIFT_DETECTED` | Expectancy declined 2 consecutive weeks |
| `NEGATIVE_EXPECTANCY_BAND` | Any score band with expectancy < 0 |
| `TIER_SPREAD_INSUFFICIENT` | PREMIUM–STANDARD win rate spread < 10 ppts |
| `SCORE_INFLATION` | Score drift up + outcome improvement absent |
| `REGIME_OVERFIT` | Setup type performs only in specific recent regime |
| `COMPOUNDING_MISALIGNED` | Scale-up periods underperformed base rate |
| `REPEAT_FINDING` | Same finding unresolved from prior audit cycle |
| `INSUFFICIENT_SAMPLE` | < 10 events — finding not surfaced |

---

## EXAMPLE — FLAGS_DETECTED

```yaml
promise_auditor_report:
  version: "1.0.0"
  report_id: "b2c4d1e8-0a33-4c7f-9b20-12e3f4a5b6c7"
  generated_at: "2026-04-18T17:00:00Z"
  audit_period:
    start: "2026-04-07"
    end: "2026-04-18"
  system_phase: "SIMULATE"
  audit_trigger: "FRIDAY_CYCLE"
  audit_verdict: "FLAGS_DETECTED"
  severity: "HIGH"
  trades_evaluated: 22
  non_executions_evaluated: 14

  expectancy_trend:
    week_1: 0.48
    week_2: 0.39
    week_3: 0.21
    week_4: null
    drift_detected: true
    drift_direction: "DECLINING"

  score_band_analysis:
    - band: "20-24"
      sample_size: 11
      win_rate_pct: 36.0
      avg_win_r: 1.5
      avg_loss_r: 1.3
      expectancy: -0.29
      expectancy_status: "NEGATIVE"
    - band: "25-29"
      sample_size: 14
      win_rate_pct: 57.0
      avg_win_r: 2.1
      avg_loss_r: 1.2
      expectancy: 0.71
      expectancy_status: "POSITIVE"
    - band: "30-35"
      sample_size: 8
      win_rate_pct: 62.0
      avg_win_r: 2.4
      avg_loss_r: 1.1
      expectancy: 0.91
      expectancy_status: "POSITIVE"

  premium_vs_standard:
    premium_sample: 11
    premium_win_rate_pct: 55.0
    standard_sample: 18
    standard_win_rate_pct: 58.0
    spread_pct: -3.0
    classification_predictive: false

  score_inflation_check:
    avg_score_period_start: 24.8
    avg_score_period_end: 28.6
    score_drift_pts: 3.8
    win_rate_change_pct: -8.0
    inflation_detected: true
    inflation_severity: "MEDIUM"

  compounding_accuracy:
    scale_up_events: 1
    periods_outperformed: 0
    accuracy_pct: 0.0
    verdict: "MISALIGNED"

  findings:
    - finding_id: "F001"
      flag_code: "NEGATIVE_EXPECTANCY_BAND"
      severity: "CRITICAL"
      repeat_count: 1
      evidence:
        metric: "expectancy"
        observed: -0.29
        expected: "> 0.0"
        delta: -0.29
        sample_size: 11
        trade_ids: ["t-002", "t-005", "t-008", "t-011", "t-014", "t-017", "t-019"]
      recommendation: "Score band 20–24 has negative expectancy across 11 trades. Do not route setups scoring below 25 to execution until band is reviewed and criteria tightened or band is discontinued."
      escalation_required: true

    - finding_id: "F002"
      flag_code: "SCORE_DRIFT_DETECTED"
      severity: "MEDIUM"
      repeat_count: 1
      evidence:
        metric: "expectancy_trend"
        observed: "0.48 → 0.39 → 0.21 (3-week decline)"
        expected: "Stable or improving"
        delta: -0.27
        sample_size: 22
        trade_ids: []
      recommendation: "Three-week expectancy decline detected. Review breakout quality scoring weights. Volume ratio and wick check thresholds may be too permissive in current market conditions."
      escalation_required: false

    - finding_id: "F003"
      flag_code: "PREMIUM_PERFORMANCE_UNSUPPORTED"
      severity: "HIGH"
      repeat_count: 1
      evidence:
        metric: "PREMIUM win rate vs STANDARD win rate"
        observed: "55.0% vs 58.0%"
        expected: "PREMIUM > STANDARD by ≥ 10 ppts"
        delta: -3.0
        sample_size: 29
        trade_ids: []
      recommendation: "PREMIUM classification not outperforming STANDARD. Raise PREMIUM threshold from current level or revise zone quality scoring rubric. Current PREMIUM label provides no predictive value."
      escalation_required: true

  failure_flags: []

  friday_cycle_summary: "Three findings this cycle, one CRITICAL. Score band 20–24 shows negative expectancy across 11 trades — setups in this band are net-negative and should be suspended pending criteria review. PREMIUM classification has failed to outperform STANDARD for the full audit period (55% vs 58% win rate) — the PREMIUM label currently has no predictive value. Additionally, expectancy has declined for three consecutive weeks without a structural reason, suggesting scoring criteria have drifted permissive. Recommended actions: (1) Suspend band 20–24 routing immediately. (2) Review PREMIUM threshold — raise to 30+ and retest. (3) Audit breakout quality weights, particularly volume ratio threshold and wick check."
```

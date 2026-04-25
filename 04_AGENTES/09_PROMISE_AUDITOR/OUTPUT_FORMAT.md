# PROMISE_AUDITOR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 09
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
promise_auditor_report:
  version: "1.0.0"
  report_id: "<UUID>"
  generated_at: "<ISO-8601 UTC>"
  audit_period:
    start: "<ISO-8601 date>"
    end: "<ISO-8601 date>"
  system_phase: "<READ_ONLY | SIMULATE | EXECUTE>"
  audit_trigger: "<FRIDAY_CYCLE | MANUAL | THRESHOLD_BREACH>"

  audit_verdict: "<CLEAN | FLAGS_DETECTED | INSUFFICIENT_DATA>"
  severity: "<NONE | LOW | MEDIUM | HIGH | CRITICAL>"
  total_trades_evaluated: <int>
  total_non_executions_evaluated: <int>

  tier_performance_analysis:
    tier_1:
      sample_size: <int>
      win_rate_pct: <float>
      avg_r_achieved: <float>
      avg_score_at_entry: <float>
    tier_2:
      sample_size: <int>
      win_rate_pct: <float>
      avg_r_achieved: <float>
      avg_score_at_entry: <float>
    tier_3:
      sample_size: <int>
      win_rate_pct: <float>
      avg_r_achieved: <float>
      avg_score_at_entry: <float>
    tier_predictive_valid: <true | false>
    tier_spread_pct: <float>              # TIER_1 win% minus TIER_3 win%

  score_inflation_analysis:
    avg_score_start_of_period: <float>
    avg_score_end_of_period: <float>
    score_drift_points: <float>
    outcome_improvement_pct: <float>     # win rate change over same period
    inflation_detected: <true | false>
    inflation_severity: "<NONE | LOW | MEDIUM | HIGH>"

  asset_bias_analysis:
    assets_reviewed: list[string]
    biased_assets:
      - asset: "<SYMBOL>"
        avg_score_vs_peer_delta: <float>
        win_rate_vs_peer_delta: <float>
        bias_type: "<RECENCY | FAMILIARITY | OUTCOME_CHASING>"
        bias_severity: "<LOW | MEDIUM | HIGH>"

  overfitting_analysis:
    overfitting_detected: <true | false>
    affected_setup_types: list[string]
    affected_regime: "<string | null>"
    description: "<string | null>"

  compounding_accuracy:
    scale_up_events: <int>
    scale_up_periods_outperformed: <int>
    accuracy_pct: <float>
    verdict: "<ACCURATE | MARGINAL | MISALIGNED>"

  findings:
    - finding_id: "<FINDING_001>"
      flag_code: "<FLAG_CODE>"
      severity: "<LOW | MEDIUM | HIGH | CRITICAL>"
      evidence:
        trade_ids: list[string]
        metric: "<string>"
        observed_value: <float>
        expected_value: <float>
        delta: <float>
      recommendation: "<actionable instruction — max 80 words>"
      repeat_finding: <true | false>

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<string>"

  friday_cycle_summary: "<200-word max human-readable summary for governance review>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `audit_verdict` | enum | `CLEAN`, `FLAGS_DETECTED`, `INSUFFICIENT_DATA` |
| `severity` | enum | `NONE`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` |
| `audit_trigger` | enum | `FRIDAY_CYCLE`, `MANUAL`, `THRESHOLD_BREACH` |
| `inflation_severity` | enum | `NONE`, `LOW`, `MEDIUM`, `HIGH` |
| `bias_type` | enum | `RECENCY`, `FAMILIARITY`, `OUTCOME_CHASING` |
| `compounding_accuracy.verdict` | enum | `ACCURATE`, `MARGINAL`, `MISALIGNED` |

---

## BIAS FLAG CODES

| Code | Meaning |
|---|---|
| `SCORE_INFLATION` | Average scores rising without outcome improvement |
| `TIER_PREDICTIVE_FAILURE` | TIER_1 not outperforming lower tiers |
| `ASSET_BIAS` | Specific asset scored persistently above peer win rate |
| `REGIME_OVERFIT` | Setup type only works in specific recent regime |
| `CLASSIFICATION_DRIFT` | Weak setups repeatedly classified as PREMIUM |
| `SCALING_MISALIGNMENT` | Compounding approved periods underperformed base |
| `RECENCY_BIAS` | Recent high-profile wins inflating scores for asset/setup |
| `INSUFFICIENT_SAMPLE` | Fewer than 10 events — cannot make statistical claim |
| `REPEAT_FINDING` | Same finding unresolved from prior audit cycle |

---

## EXAMPLE OUTPUT — FLAGS DETECTED

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
  severity: "MEDIUM"
  total_trades_evaluated: 18
  total_non_executions_evaluated: 11
  tier_performance_analysis:
    tier_1:
      sample_size: 8
      win_rate_pct: 50.0
      avg_r_achieved: 1.9
      avg_score_at_entry: 29.5
    tier_2:
      sample_size: 7
      win_rate_pct: 57.0
      avg_r_achieved: 2.1
      avg_score_at_entry: 24.0
    tier_3:
      sample_size: 3
      win_rate_pct: 33.0
      avg_r_achieved: 1.1
      avg_score_at_entry: 18.0
    tier_predictive_valid: false
    tier_spread_pct: 17.0
  score_inflation_analysis:
    avg_score_start_of_period: 24.3
    avg_score_end_of_period: 28.8
    score_drift_points: 4.5
    outcome_improvement_pct: -3.0
    inflation_detected: true
    inflation_severity: "MEDIUM"
  asset_bias_analysis:
    assets_reviewed: ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT"]
    biased_assets:
      - asset: "ETHUSDT"
        avg_score_vs_peer_delta: 3.8
        win_rate_vs_peer_delta: -12.0
        bias_type: "RECENCY"
        bias_severity: "MEDIUM"
  overfitting_analysis:
    overfitting_detected: false
    affected_setup_types: []
    affected_regime: null
    description: null
  compounding_accuracy:
    scale_up_events: 1
    scale_up_periods_outperformed: 0
    accuracy_pct: 0.0
    verdict: "MISALIGNED"
  findings:
    - finding_id: "FINDING_001"
      flag_code: "TIER_PREDICTIVE_FAILURE"
      severity: "MEDIUM"
      evidence:
        trade_ids: ["t-001", "t-003", "t-007", "t-012", "t-015"]
        metric: "TIER_1 win rate vs TIER_2 win rate"
        observed_value: 50.0
        expected_value: 65.0
        delta: -15.0
      recommendation: "Review Score Engine TIER_1 threshold. Current 27+ cutoff may be too low. Consider raising to 30+ and auditing structure/breakout quality weight distribution."
      repeat_finding: false
    - finding_id: "FINDING_002"
      flag_code: "SCORE_INFLATION"
      severity: "MEDIUM"
      evidence:
        trade_ids: ["t-009", "t-011", "t-014", "t-016", "t-017", "t-018"]
        metric: "avg_score_drift vs outcome_improvement"
        observed_value: 4.5
        expected_value: 0.0
        delta: 4.5
      recommendation: "Score drift of +4.5 pts over period not matched by outcomes. Investigate if breakout quality score is being inflated by confirming candle aesthetics rather than volume and close position."
      repeat_finding: false
  failure_flags: []
  friday_cycle_summary: "Two medium-severity findings this cycle. TIER_1 setups are underperforming TIER_2 — the tier threshold may be misaligned. Average scores have drifted upward +4.5 points without corresponding outcome improvement, suggesting score inflation in breakout quality or structure assessment. ETHUSDT shows signs of recency bias following 3 consecutive wins in Week 3. Recommended actions: raise TIER_1 threshold review, audit breakout quality weight, apply asset-blind scoring for ETHUSDT for next 2 cycles. Compounding scale-up approved on April 15 has not yet shown performance lift — monitor closely."
```

# JOURNAL_LEARNING — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 08
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURES

Journal Learning produces four output types depending on event type received.

---

### TYPE 1: TRADE RECORD

```yaml
journal_trade_record:
  version: "1.0.0"
  record_id: "<UUID>"
  recorded_at: "<ISO-8601 UTC>"
  event_type: "<TRADE_ENTRY | TRADE_EXIT | TRADE_UPDATE>"
  system_phase: "<READ_ONLY | SIMULATE | EXECUTE>"

  trade:
    trade_id: "<UUID>"
    asset: "<SYMBOL>"
    direction: "<LONG | SHORT>"
    status: "<OPEN | CLOSED | CANCELLED>"

  entry_data:
    entry_price: <float>
    stop_price: <float>
    t1_price: <float>
    t2_price: <float | null>
    t3_price: <float | null>
    entry_timestamp: "<ISO-8601 UTC>"
    plan_confidence: <float>

  exit_data:
    exit_price: <float | null>
    exit_timestamp: "<ISO-8601 UTC | null>"
    r_achieved: <float | null>
    outcome: "<WIN | LOSS | BREAK_EVEN | OPEN>"
    exit_type: "<TP_HIT | SL_HIT | MANUAL | TRAIL_STOP | OPEN>"

  scores_at_entry:
    structure_score: <int | "NOT_CAPTURED">
    breakout_quality_score: <int | "NOT_CAPTURED">
    score_engine_total: <int | "NOT_CAPTURED">
    score_engine_tier: "<TIER_1 | TIER_2 | TIER_3 | UNRANKED | NOT_CAPTURED>"
    regime_at_entry: "<string | NOT_CAPTURED>"

  agent_verdicts_at_entry:
    risk_guardian: "<APPROVED | REJECTED | NOT_CAPTURED>"
    structure_hunter: "<BREAKOUT_READY | WATCHLIST | NOT_CAPTURED>"
    breakout_confirmation: "<CONFIRMED | FAKEOUT | PENDING | NOT_CAPTURED>"
    market_regime: "<string | NOT_CAPTURED>"
    news_sentinel: "<LOW | MEDIUM | HIGH | CRITICAL | NOT_CAPTURED>"
```

---

### TYPE 2: NON-EXECUTION RECORD

```yaml
journal_non_execution_record:
  version: "1.0.0"
  record_id: "<UUID>"
  recorded_at: "<ISO-8601 UTC>"
  event_type: "NON_EXECUTION"
  system_phase: "<string>"

  asset: "<SYMBOL>"
  direction: "<LONG | SHORT | UNKNOWN>"
  reason_code: "<RISK_REJECTED | FAKEOUT | NEWS_HOLD | FREEZE_BLOCK | STALE_ALERT | DUPLICATE | NO_STRUCTURE | OTHER>"
  blocking_agent: "<agent_name>"
  timestamp: "<ISO-8601 UTC>"
  agent_verdicts: dict
  notes: "<optional>"
```

---

### TYPE 3: POST-MORTEM REPORT

```yaml
journal_post_mortem:
  version: "1.0.0"
  record_id: "<UUID>"
  generated_at: "<ISO-8601 UTC>"
  trade_id: "<UUID>"
  asset: "<SYMBOL>"

  plan_vs_actual:
    planned_r_at_t1: <float>
    actual_r_achieved: <float>
    r_delta: <float>
    exit_vs_plan: "<EARLY | ON_TARGET | BEYOND_TARGET | STOPPED_OUT>"

  process_evaluation:
    process_followed: <true | false>
    deviation_description: "<string | null>"
    outcome_consistent_with_edge: <true | false>
    anomaly_detected: <true | false>
    anomaly_description: "<string | null>"

  learning_tags:
    - "<tag>"         # e.g., "FAKEOUT_RISK", "VOLUME_CONFIRMED", "NEWS_SURPRISE"

  recommendation: "<string — max 60 words>"
```

---

### TYPE 4: WEEKLY LEARNING SUMMARY

```yaml
journal_weekly_summary:
  version: "1.0.0"
  week_ending: "<ISO-8601 date>"
  generated_at: "<ISO-8601 UTC>"

  trade_stats:
    total_trades: <int>
    wins: <int>
    losses: <int>
    break_even: <int>
    win_rate_pct: <float>
    avg_r_achieved: <float>
    best_trade_r: <float>
    worst_trade_r: <float>

  non_execution_stats:
    total_non_executions: <int>
    breakdown_by_reason: dict

  patterns_identified:
    - pattern_id: "<PATTERN_001>"
      description: "<string>"
      sample_size: <int>
      win_rate_pct: <float>
      recommendation: "<string>"

  failure_flags_this_week:
    - flag: "<FLAG_CODE>"
      count: <int>
      detail: "<string>"

  friday_cycle_highlights:
    - "<key finding>"

  notes: "<optional — max 150 words>"
```

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `RECURRING_FAILURE` | Same failure pattern ≥ 3 times in period |
| `SETUP_DEGRADATION` | Win rate for a setup type dropped below 40% |
| `SCORING_MISALIGNMENT` | Score tier inconsistent with outcomes (≥ 3 events) |
| `DATA_QUALITY_ISSUE` | >20% of records have NOT_CAPTURED fields |
| `PROMISE_AUDIT_FLAG` | Promise Auditor identified bias in this period |
| `INCOMPLETE_RECORD` | Trade logged with missing required fields |

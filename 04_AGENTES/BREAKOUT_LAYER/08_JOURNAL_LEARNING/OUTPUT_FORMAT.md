# JOURNAL_LEARNING — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 08_JOURNAL_LEARNING
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMAS

Journal Learning produces four output types. Each is triggered by different consumers.

---

### SCHEMA 1: TRADE RECORD (stored internally, queryable)

```yaml
journal_trade_record:
  version: "1.0.0"
  record_id: string              # UUID — generated at storage time
  recorded_at: string            # ISO-8601 UTC
  event_type: string             # TRADE_ENTRY | TRADE_EXIT | TRADE_UPDATE
  system_phase: string

  trade:
    trade_id: string
    asset: string
    direction: string            # LONG | SHORT
    status: string               # OPEN | CLOSED | CANCELLED

  features:
    entry_price: float | "NOT_CAPTURED"
    stop_price: float | "NOT_CAPTURED"
    t1_price: float | "NOT_CAPTURED"
    entry_type: string | "NOT_CAPTURED"
    session: string | "NOT_CAPTURED"           # MANDATORY
    regime_at_entry: string | "NOT_CAPTURED"   # MANDATORY
    btc_alignment_score: float | "NOT_CAPTURED"
    zone_id: string | "NOT_CAPTURED"
    zone_score: int | "NOT_CAPTURED"
    breakout_quality_score: int | "NOT_CAPTURED"
    volume_ratio: float | "NOT_CAPTURED"
    warning_flags: list[string] | "NOT_CAPTURED"

  outcome:
    exit_price: float | null
    r_achieved: float | null
    outcome: string | null       # WIN | LOSS | BREAK_EVEN | OPEN
    exit_type: string | null

  agent_verdicts: dict           # full agent output objects at entry time
```

---

### SCHEMA 2: NON-EXECUTION RECORD

```yaml
journal_non_execution_record:
  version: "1.0.0"
  record_id: string
  recorded_at: string
  event_type: "NON_EXECUTION"
  system_phase: string

  asset: string
  direction: string              # LONG | SHORT | UNKNOWN
  session: string                # MANDATORY
  regime_at_block: string        # MANDATORY
  reason_code: string            # see REASON CODES
  blocking_agent: string
  timestamp: string
  agent_verdicts: dict
```

---

### SCHEMA 3: WEEKLY LEARNING SUMMARY (for Friday Cycle)

```yaml
journal_weekly_summary:
  version: "1.0.0"
  week_ending: string            # ISO-8601 date
  generated_at: string

  trade_stats:
    total_trades: int
    wins: int
    losses: int
    break_even: int
    win_rate_pct: float
    avg_r_achieved: float

  non_execution_stats:
    total: int
    by_reason: dict              # reason_code → count

  patterns_flagged:
    - pattern_id: string
      description: string
      sample_size: int
      win_rate_pct: float
      flag_code: string
      recommendation: string     # max 60 words

  scoring_performance:
    by_tier:
      tier_1: { count: int, win_rate_pct: float, avg_r: float }
      tier_2: { count: int, win_rate_pct: float, avg_r: float }
      tier_3: { count: int, win_rate_pct: float, avg_r: float }

  failure_flags_this_week: list[FailureFlag]

  friday_cycle_highlights: list[string]   # max 5 key findings

  notes: string                  # optional, max 150 words
```

---

### SCHEMA 4: SCORECARD FEED (for Scorecard Engine)

```yaml
scorecard_feed:
  version: "1.0.0"
  generated_at: string
  period_start: string
  period_end: string

  score_band_performance:
    - band: string               # e.g., "25-29", "30-35"
      count: int
      win_rate_pct: float
      avg_r_achieved: float
      expectancy: float          # (win_rate * avg_win_r) - (loss_rate * avg_loss_r)

  regime_performance:
    - regime: string
      count: int
      win_rate_pct: float
      avg_r_achieved: float

  session_performance:
    - session: string
      count: int
      win_rate_pct: float
```

---

## REASON CODES (for NON_EXECUTION records)

| Code | Source Agent |
|---|---|
| `FAKEOUT` | Breakout Confirmation |
| `RISK_REJECTED` | Risk Guardian |
| `NEWS_HOLD` | News Sentinel |
| `FREEZE_BLOCK` | Risk Guardian / Compounding Governor |
| `STALE_ALERT` | Alert Radar |
| `ASSET_PROHIBITED` | Alert Radar |
| `ASSET_NOT_WATCHLISTED` | Alert Radar |
| `NO_STRUCTURE` | Structure Hunter |
| `ZONE_EXPIRED` | Structure Hunter |
| `VOLUME_INSUFFICIENT` | Breakout Confirmation |
| `DUPLICATE_ALERT` | Alert Radar |
| `COMPOUNDING_FREEZE` | Compounding Governor |
| `READ_ONLY_BLOCK` | System mode |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INCOMPLETE_INPUT` | Required fields absent from incoming event |
| `RECURRING_FAILURE` | Same failure pattern ≥ 3 times in period |
| `SETUP_DEGRADATION` | Win rate for setup type < 40% |
| `SCORING_MISALIGNMENT` | Tier inconsistent with outcomes ≥ 3 events |
| `DATA_QUALITY_ISSUE` | > 20% of records have NOT_CAPTURED fields |
| `GOVERNANCE_FLAG` | Promise Auditor bias flag received this period |

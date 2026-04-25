---
schema_type: scorecard
schema_version: 1.0
scorecard_id: SC_SYSTEM_EURU_TOS_2026-W15
scorecard_date: '2026-04-12'
period_type: weekly
period_ref: 2026-W15
period_start: '2026-04-12'
period_end: '2026-04-12'
system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS
health_status: warning
decision_status: adjust
deviation_severity: high
closed_trades_count: 3
win_rate_pct: 0.0
average_rr: 0.0
expectancy: 0.0
prediction_accuracy_pct: 0.0
average_entry_score: 0.0
average_entry_score_winners: 0.0
average_entry_score_losers: 0.0
threshold_breach_count: 3
deviation_count: 0
blocked_trades_count: 0
watchlist_alert_count: 0
human_approval_required: true
linked_learning_report: LEARNING_REPORT_2026-04-12.md
tags:
- scorecard
- governance
- weekly
- system
---

# Scorecard Snapshot

## Subject Summary
- Weekly governance snapshot for EURU_TOS Friday cycle.
- Generated automatically from the latest learning result.

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | 0.0 | 50.0 | breach |
| average_rr | 0.0 | 2.0 | breach |
| expectancy | 0.0 | 0.01 | breach |
| prediction_accuracy_pct | 0.0 | 60.0 | watch |

## Threshold Review
- win_rate_pct: breach (value=0.0, target=50.0)
- average_rr: breach (value=0.0, target=2.0)
- expectancy: breach (value=0.0, target=>0)

## Deviations
- none

## Decision
- adjust

## Action Plan
- Type 1 — Raise the minimum Score Engine threshold for new entries in SIMULATE until win rate improves.
- Type 2 — Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades.

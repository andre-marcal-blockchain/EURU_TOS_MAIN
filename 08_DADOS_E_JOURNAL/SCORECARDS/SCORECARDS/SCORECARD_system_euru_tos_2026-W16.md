---
schema_type: scorecard
schema_version: 1.0
scorecard_id: SC_SYSTEM_EURU_TOS_2026-W16
scorecard_date: '2026-04-17'
period_type: weekly
period_ref: 2026-W16
period_start: '2026-04-17'
period_end: '2026-04-17'
system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS
health_status: warning
decision_status: adjust
deviation_severity: high
closed_trades_count: 3
win_rate_pct: 100.0
average_rr: 0.9
expectancy: 0.0
prediction_accuracy_pct: 0.0
average_entry_score: 4.5
average_entry_score_winners: 9.0
average_entry_score_losers: 0.0
threshold_breach_count: 2
deviation_count: 0
blocked_trades_count: 0
watchlist_alert_count: 0
human_approval_required: false
linked_learning_report: LEARNING_REPORT_2026-04-17.md
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
| win_rate_pct | 100.0 | 50.0 | pass |
| average_rr | 0.9 | 2.0 | breach |
| expectancy | 0.0 | 0.01 | breach |
| prediction_accuracy_pct | 0.0 | 60.0 | watch |

## Threshold Review
- win_rate_pct: pass (value=100.0, target=50.0)
- average_rr: breach (value=0.9, target=2.0)
- expectancy: breach (value=0.0, target=>0)

## Deviations
- none

## Decision
- adjust

## Action Plan
- maintain current SIMULATE governance and continue collecting clean data

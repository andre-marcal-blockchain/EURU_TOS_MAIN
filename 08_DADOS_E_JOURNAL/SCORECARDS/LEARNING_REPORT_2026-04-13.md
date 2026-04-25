---
schema_type: learning_report
schema_version: 1.0
report_date: '2026-04-13'
period_start: '2026-04-13'
period_end: '2026-04-13'
period_type: weekly
system_phase: simulate
system_status: healthy
readiness_status: continue_simulate
source_trade_files_count: 3
closed_trades_analyzed: 3
journal_files_analyzed: 3
invalid_files_count: 0
legacy_format_detected_count: 0
win_rate_pct: 0.0
average_rr: 0.0
expectancy: 0.0
average_win_rr: 0.0
average_loss_rr: 0.0
best_setup_type: null
worst_setup_type: null
best_asset: null
worst_asset: null
average_entry_score_winners: 0.0
average_entry_score_losers: 0.0
prediction_accuracy_overall_pct: 0.0
prediction_accuracy_best_setup_pct: 0.0
prediction_accuracy_worst_setup_pct: 0.0
governance_type_1_count: 1
governance_type_2_count: 1
governance_type_3_count: 0
human_approval_required: true
execute_candidate: false
tags:
- weekly_learning
- governance
- score_engine
---

# Executive Summary

## Performance Summary
- closed_trades_analyzed: 3
- win_rate_pct: 0.0
- average_rr: 0.0
- expectancy: 0.0

## Patterns Identified
- score band 0-54: win_rate=0.0 sample=3
- setup trend_continuation: win_rate=0.0 sample=3

## Score Engine vs Actual Results
- overall prediction accuracy: 0.0%

## Asset Alerts
- none

## Setup Alerts
- none

## Agent Deviation Analysis
- none

## Governance Suggestions
### Type 1 — Immediate Adjustment
- Raise the minimum Score Engine threshold for new entries in SIMULATE until win rate improves.

### Type 2 — 24h Review
- Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades.

### Type 3 — 48h Strategic
- none

## Pending Decisions for Human Approval
- Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades.

## SIMULATE Readiness Check
- continue_simulate

## Next Learning Actions
- continue SIMULATE and apply governance suggestions from this report
- keep schema validator and preflight as mandatory gatekeepers

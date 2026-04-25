---
schema_type: learning_report
schema_version: 1.0
report_date: '2026-04-17'
period_start: '2026-04-17'
period_end: '2026-04-17'
period_type: weekly
system_phase: simulate
system_status: healthy
readiness_status: continue_simulate
source_trade_files_count: 3
closed_trades_analyzed: 3
journal_files_analyzed: 6
invalid_files_count: 0
legacy_format_detected_count: 0
win_rate_pct: 100.0
average_rr: 0.9
expectancy: 0.0
average_win_rr: 0.9
average_loss_rr: 0.0
best_setup_type: trend_continuation
worst_setup_type: trend_continuation
best_asset: arbusdt
worst_asset: avaxusdt
average_entry_score_winners: 9.0
average_entry_score_losers: 0.0
prediction_accuracy_overall_pct: 0.0
prediction_accuracy_best_setup_pct: 0.0
prediction_accuracy_worst_setup_pct: 0.0
governance_type_1_count: 0
governance_type_2_count: 0
governance_type_3_count: 0
human_approval_required: false
execute_candidate: false
tags:
- weekly_learning
- governance
- score_engine
---

# Executive Summary

## Performance Summary
- closed_trades_analyzed: 3
- win_rate_pct: 100.0
- average_rr: 0.9
- expectancy: 0.0

## Patterns Identified
- score band 0-54: win_rate=100.0 sample=3
- setup trend_continuation: win_rate=100.0 sample=3

## Score Engine vs Actual Results
- overall prediction accuracy: 0.0%
- asset AVAXUSDT: accuracy=0.0 correct=0/1
- asset NEARUSDT: accuracy=0.0 correct=0/1
- asset ARBUSDT: accuracy=0.0 correct=0/1
- setup trend_continuation: accuracy=0.0 correct=0/3

## Asset Alerts
- none

## Setup Alerts
- best_setup_type: trend_continuation
- worst_setup_type: trend_continuation

## Agent Deviation Analysis
- none

## Governance Suggestions
### Type 1 — Immediate Adjustment
- none

### Type 2 — 24h Review
- none

### Type 3 — 48h Strategic
- none

## Pending Decisions for Human Approval
- none

## SIMULATE Readiness Check
- continue_simulate

## Next Learning Actions
- continue SIMULATE and apply governance suggestions from this report
- keep schema validator and preflight as mandatory gatekeepers

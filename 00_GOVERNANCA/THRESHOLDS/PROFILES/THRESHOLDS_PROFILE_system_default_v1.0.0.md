---
schema_type: governance_threshold_profile
schema_version: 1.0

profile_id: default
scope: system
version: 1.0.0
status: active

effective_from: 2026-04-12
effective_to: null

owner: EURU Governance
change_reason: initial_baseline
approval_status: approved
approved_by: human_governance
approval_date: 2026-04-12

inherits_from: null
supersedes_version: null

thresholds:
  readiness:
    min_closed_trades: 20
    min_win_rate_pct: 50.0
    min_average_rr: 2.0
    min_expectancy: 0.01

  schema_quality:
    max_invalid_files: 0
    max_warning_files: 5
    block_on_invalid_schema: true
    block_on_warnings_in_strict_mode: true

  portfolio_risk:
    max_portfolio_risk_used_pct: 75.0
    max_single_asset_risk_pct: 20.0
    max_open_positions: 12

  score_engine:
    min_prediction_accuracy_pct: 60.0
    min_average_entry_score_winners: 7.0
    max_false_positive_rate_pct: 35.0

  watchlist:
    repeated_failure_block_after: 3
    repeated_failure_review_after: 2

  governance:
    human_review_required_for_strategy_change: true
    human_review_required_for_threshold_change: true
    immediate_block_on_critical_deviation: true

notes_tags:
  - baseline
  - simulate
  - governance
---

# Profile Summary

## Purpose
- Define the initial baseline governance thresholds for the Euru Friday cycle in SIMULATE mode.

## Threshold Rationale
- Readiness thresholds reflect the current Euru learning criteria.
- Schema quality thresholds enforce clean learning inputs.
- Portfolio risk thresholds prevent excessive exposure in a shared-risk model.
- Score engine thresholds require minimum predictive quality before trust increases.
- Watchlist thresholds force review/blocking after repeated failure.

## Changes vs Previous Version
- initial baseline

## Expected Operational Impact
- Standardize governance decisions across weekly cycles.
- Make threshold history auditable.
- Allow week-to-week performance comparison under known rules.

## Human Governance Notes
- This baseline should remain active until the first approved threshold tuning cycle.

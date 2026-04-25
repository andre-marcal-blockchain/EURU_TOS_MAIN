---
schema_type: governance_threshold_profile
schema_version: 1.0

profile_id: default
scope: system
version: 1.1.0
status: draft

effective_from: 2026-04-19
effective_to: null

owner: EURU Governance
change_reason: first_threshold_tuning
approval_status: pending
approved_by: null
approval_date: null

inherits_from: system_default_v1.0.0
supersedes_version: 1.0.0

thresholds:
  readiness:
    min_closed_trades: 20
    min_win_rate_pct: 52.0
    min_average_rr: 2.1
    min_expectancy: 0.05

  schema_quality:
    max_invalid_files: 0
    max_warning_files: 3
    block_on_invalid_schema: true
    block_on_warnings_in_strict_mode: true

  portfolio_risk:
    max_portfolio_risk_used_pct: 70.0
    max_single_asset_risk_pct: 18.0
    max_open_positions: 10

  score_engine:
    min_prediction_accuracy_pct: 62.5
    min_average_entry_score_winners: 7.2
    max_false_positive_rate_pct: 30.0

  watchlist:
    repeated_failure_block_after: 3
    repeated_failure_review_after: 2

  governance:
    human_review_required_for_strategy_change: true
    human_review_required_for_threshold_change: true
    immediate_block_on_critical_deviation: true

notes_tags:
  - tuning
  - stricter
  - governance
---

# Profile Summary

## Purpose
- Tighten baseline governance thresholds after the first simulation learning cycle.

## Threshold Rationale
- Raise readiness quality slightly before EXECUTE candidacy.
- Reduce tolerance for warning-heavy data weeks.
- Tighten portfolio and asset risk ceilings.
- Demand better prediction accuracy from the score engine.

## Changes vs Previous Version
- readiness.min_win_rate_pct increased from 50.0 to 52.0
- readiness.min_average_rr increased from 2.0 to 2.1
- readiness.min_expectancy increased from 0.01 to 0.05
- schema_quality.max_warning_files reduced from 5 to 3
- portfolio_risk.max_portfolio_risk_used_pct reduced from 75.0 to 70.0
- portfolio_risk.max_single_asset_risk_pct reduced from 20.0 to 18.0
- portfolio_risk.max_open_positions reduced from 12 to 10
- score_engine.min_prediction_accuracy_pct increased from 60.0 to 62.5
- score_engine.min_average_entry_score_winners increased from 7.0 to 7.2
- score_engine.max_false_positive_rate_pct reduced from 35.0 to 30.0

## Expected Operational Impact
- Fewer borderline weeks qualify as execute candidates.
- More conservative exposure during simulation.
- Cleaner input quality required for learning confidence.

## Human Governance Notes
- Pending approval. Do not activate until formally approved.

---
schema_type: governance_threshold_changelog
schema_version: 1.0

profile_id: default
scope: system
from_version: 1.0.0
to_version: 1.1.0
change_date: 2026-04-12

generated_by: euru_threshold_registry.py
approval_status: pending
impact_level: medium

changed_keys_count: 10
added_keys_count: 0
removed_keys_count: 0
---

# Change Summary

## Version Transition
- from 1.0.0 to 1.1.0

## Added Keys
- none

## Removed Keys
- none

## Changed Values
- `portfolio_risk.max_open_positions`: 12 -> 10
- `portfolio_risk.max_portfolio_risk_used_pct`: 75.0 -> 70.0
- `portfolio_risk.max_single_asset_risk_pct`: 20.0 -> 18.0
- `readiness.min_average_rr`: 2.0 -> 2.1
- `readiness.min_expectancy`: 0.01 -> 0.05
- `readiness.min_win_rate_pct`: 50.0 -> 52.0
- `schema_quality.max_warning_files`: 5 -> 3
- `score_engine.max_false_positive_rate_pct`: 35.0 -> 30.0
- `score_engine.min_average_entry_score_winners`: 7.0 -> 7.2
- `score_engine.min_prediction_accuracy_pct`: 60.0 -> 62.5

## Governance Interpretation
- pending human interpretation

## Human Approval Notes
- pending

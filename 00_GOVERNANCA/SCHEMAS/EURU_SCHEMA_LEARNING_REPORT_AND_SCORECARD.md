# EURU_TOS — Official Schema for LEARNING_REPORT and SCORECARD
Version: 1.0
Status: Active
Owner: EURU_TOS Governance
Applies to:
- 08_DADOS_E_JOURNAL/SCORECARDS/
- euru_learning_engine.py
- Score Engine
- Governance layer
- all AI agents writing learning or scorecard outputs

## 1. Purpose

This document defines the official schema for:

1. LEARNING_REPORT files
2. SCORECARD files

The objective is to make Euru_TOS consistent, machine-readable, auditable, governance-driven, comparable across time, and ready for future automation and validation.

## 2. Core Principles

1. Every file must be valid Markdown (`.md`)
2. Every file must start with YAML front matter
3. Front matter is the machine-readable layer
4. Markdown body is the human-readable and governance layer
5. Required fields must never be omitted
6. Unknown values must be written as `null`
7. Numeric fields must contain numeric values only
8. Enum values must use lowercase_snake_case
9. Dates must use ISO 8601
10. Agents must never rename official keys or headings

## 3. Folder Scope

### 3.1 Learning reports
Official folder:
`08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORTS/`

### 3.2 Scorecards
Official folder:
`08_DADOS_E_JOURNAL/SCORECARDS/SCORECARDS/`

## 4. File Naming Convention

### 4.1 Learning report
Pattern:
`LEARNING_REPORT_<report_date>.md`

### 4.2 Scorecard
Pattern:
`SCORECARD_<scope>_<subject_id>_<period_ref>.md`

## 5. Official Enum Dictionary

### 5.1 Schema type
- `learning_report`
- `scorecard`

### 5.2 System phase
- `simulate`
- `execute`

### 5.3 Health status
- `healthy`
- `warning`
- `critical`

### 5.4 Readiness status
- `continue_simulate`
- `execute_candidate`
- `hold`
- `review_required`
- `blocked`

### 5.5 Governance suggestion type
- `type_1_immediate_adjustment`
- `type_2_review_24h`
- `type_3_strategic_48h`

### 5.6 Scorecard scope
- `system`
- `agent`
- `asset`
- `setup`
- `portfolio`
- `watchlist`
- `risk`
- `score_engine`

### 5.7 Period type
- `daily`
- `weekly`
- `monthly`
- `cycle`

### 5.8 Outcome status
- `positive`
- `neutral`
- `negative`

### 5.9 Decision status
- `keep`
- `watch`
- `adjust`
- `block`
- `retire`
- `escalate`

### 5.10 Prediction quality
- `aligned`
- `false_positive`
- `false_negative`
- `insufficient_data`

### 5.11 Deviation severity
- `none`
- `low`
- `medium`
- `high`
- `critical`

## 6. LEARNING_REPORT Schema

### 6.1 Required front matter fields

```yaml
---
schema_type: learning_report
schema_version: 1.0

report_date: 2026-04-12
period_start: 2026-04-05
period_end: 2026-04-12
period_type: weekly

system_phase: simulate
system_status: healthy
readiness_status: continue_simulate

source_trade_files_count: 24
closed_trades_analyzed: 21
journal_files_analyzed: 7
invalid_files_count: 1
legacy_format_detected_count: 2

win_rate_pct: 57.14
average_rr: 2.36
expectancy: 0.48
average_win_rr: 3.10
average_loss_rr: 1.35

best_setup_type: trend_reversal
worst_setup_type: news_reaction
best_asset: fetusdt
worst_asset: rndrusdt

average_entry_score_winners: 8.2
average_entry_score_losers: 5.9

prediction_accuracy_overall_pct: 71.4
prediction_accuracy_best_setup_pct: 80.0
prediction_accuracy_worst_setup_pct: 42.9

governance_type_1_count: 2
governance_type_2_count: 3
governance_type_3_count: 1

human_approval_required: true
execute_candidate: false

tags:
  - weekly_learning
  - governance
  - score_engine
---
```

### 6.2 Required LEARNING_REPORT body structure

```md
# Executive Summary

## Performance Summary
- Main quantitative results for the period

## Patterns Identified
- Which setups worked
- Which score values aligned with winners
- Which conditions failed repeatedly

## Score Engine vs Actual Results
- Accuracy analysis
- False positives
- False negatives
- Assets or setups with weak predictive power

## Asset Alerts
- Repeated failing assets
- Repeated outperforming assets
- Watchlist warnings

## Setup Alerts
- Best and worst setup behavior
- Setups to keep, adjust, or block

## Agent Deviation Analysis
- Process deviations
- Rule breaks
- Simulation drift
- If none, write: `- none`

## Governance Suggestions
### Type 1 — Immediate Adjustment
- ...
### Type 2 — 24h Review
- ...
### Type 3 — 48h Strategic
- ...

## Pending Decisions for Human Approval
- ...
- If none, write: `- none`

## SIMULATE Readiness Check
- Explicit decision:
  - continue_simulate
  - execute_candidate
  - hold
  - review_required

## Next Learning Actions
- Concrete actions for next cycle
```

### 6.3 LEARNING_REPORT rules

- If `closed_trades_analyzed < 20`, `execute_candidate` must be `false`
- If `readiness_status: execute_candidate`, all of the following must be true:
  - `win_rate_pct >= 50`
  - `average_rr >= 2.0`
  - `expectancy > 0`
- If `invalid_files_count > 0`, the report must mention schema/data quality risk in `Executive Summary` and `Pending Decisions for Human Approval`

## 7. SCORECARD Schema

### 7.1 Required front matter fields

```yaml
---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_SYSTEM_EURU_TOS_2026-W15
scorecard_date: 2026-04-12
period_type: weekly
period_ref: 2026-W15
period_start: 2026-04-05
period_end: 2026-04-12

system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS

health_status: healthy
decision_status: keep
deviation_severity: low

closed_trades_count: 21
win_rate_pct: 57.14
average_rr: 2.36
expectancy: 0.48
prediction_accuracy_pct: 71.4

average_entry_score: 7.4
average_entry_score_winners: 8.2
average_entry_score_losers: 5.9

threshold_breach_count: 1
deviation_count: 1
blocked_trades_count: 3
watchlist_alert_count: 2

human_approval_required: false
linked_learning_report: LEARNING_REPORT_2026-04-12.md

tags:
  - scorecard
  - governance
  - weekly
---
```

### 7.2 SCORECARD body structure

```md
# Scorecard Snapshot

## Subject Summary
- What is being scored
- Why this scorecard exists

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | 57.14 | 50.0 | pass |
| average_rr | 2.36 | 2.0 | pass |
| expectancy | 0.48 | 0.01 | pass |

## Threshold Review
- Which thresholds were respected
- Which thresholds were breached
- If none, write: `- none`

## Deviations
- Operational deviations
- Governance deviations
- Agent deviations
- If none, write: `- none`

## Decision
- keep
- watch
- adjust
- block
- retire
- escalate

## Action Plan
- Concrete actions for the next period
```

### 7.3 SCORECARD scope rules

If `scope: system`, `subject_id` must be `euru_tos`.
If `scope: agent`, `subject_id` must be a stable agent identifier.
If `scope: asset`, `subject_id` must be lowercase symbol.
If `scope: setup`, `subject_id` must match official setup enum.

## 8. Learning-to-Scorecard Relationship

1. Trade files feed the learning engine
2. Journal files enrich context
3. Learning engine generates `LEARNING_REPORT`
4. Score Engine or governance layer generates `SCORECARD`
5. Human approval closes the loop when required

Every SCORECARD should ideally reference one learning report, one subject, and one period.
A LEARNING_REPORT may support multiple SCORECARDs.

## 9. Official LEARNING_REPORT Template

```md
---
schema_type: learning_report
schema_version: 1.0

report_date: 2026-04-12
period_start: 2026-04-05
period_end: 2026-04-12
period_type: weekly

system_phase: simulate
system_status: healthy
readiness_status: continue_simulate

source_trade_files_count: 0
closed_trades_analyzed: 0
journal_files_analyzed: 0
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

governance_type_1_count: 0
governance_type_2_count: 0
governance_type_3_count: 0

human_approval_required: false
execute_candidate: false

tags: []
---

# Executive Summary

## Performance Summary
- ...

## Patterns Identified
- ...

## Score Engine vs Actual Results
- ...

## Asset Alerts
- ...

## Setup Alerts
- ...

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
- ...
```

## 10. Official SCORECARD Template

```md
---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_SCOPE_SUBJECT_PERIOD
scorecard_date: 2026-04-12
period_type: weekly
period_ref: 2026-W15
period_start: 2026-04-05
period_end: 2026-04-12

system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS

health_status: healthy
decision_status: keep
deviation_severity: none

closed_trades_count: 0
win_rate_pct: 0.0
average_rr: 0.0
expectancy: 0.0
prediction_accuracy_pct: 0.0

average_entry_score: 0.0
average_entry_score_winners: 0.0
average_entry_score_losers: 0.0

threshold_breach_count: 0
deviation_count: 0
blocked_trades_count: 0
watchlist_alert_count: 0

human_approval_required: false
linked_learning_report: null

tags: []
---

# Scorecard Snapshot

## Subject Summary
- ...

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | 0.0 | 50.0 | pending |
| average_rr | 0.0 | 2.0 | pending |
| expectancy | 0.0 | 0.01 | pending |

## Threshold Review
- none

## Deviations
- none

## Decision
- keep

## Action Plan
- ...
```

## 11. Non-Negotiable Rules for All Agents

1. Do not invent missing required numeric values
2. Do not rename official YAML keys
3. Do not rename official body headings
4. Do not mix languages inside enum values
5. Do not write `%` signs inside numeric YAML fields
6. Do not create scorecards without explicit scope and subject
7. Do not create learning reports without explicit period
8. Do not silently ignore invalid schema
9. Do not treat body text as replacement for missing front matter
10. Do not write governance suggestions outside official sections

## 12. Final Authority

If there is any conflict between legacy habits, flexible parser assumptions, old scorecard formats, or agent-specific naming customs, this schema wins.

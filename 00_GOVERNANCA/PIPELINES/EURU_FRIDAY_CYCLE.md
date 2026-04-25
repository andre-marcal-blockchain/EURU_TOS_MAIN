# EURU_TOS — Official Friday Cycle Pipeline
Version: 1.1
Status: Active
Owner: EURU Governance
Official cadence: Every Friday, after GitHub sync

## 1. Purpose

The Friday cycle is the official weekly operating ritual of Euru_TOS.

Its objective is to ensure that:
- learning runs only on trusted data
- reports are generated in the correct order
- governance is explicit and auditable
- multidimensional scorecards are produced every week
- any blocking issue stops the cycle before contaminating later layers

## 2. Official execution order

The official sequence is:

**GitHub Sync → Schema Validator → Learning Preflight → Learning Engine → Canonical Learning Report → Scorecard Engine → Human Governance Review → Weekly Close**

No later stage may run if a prior blocking stage has failed.

## 3. Stage summary

### Stage 0 — GitHub Sync
Purpose:
- ensure Euru runs on the latest synchronized repository state

Input:
- local `Euru_TOS` repository

Output:
- synchronized working tree
- active branch and commit confirmation

Blocking rule:
- if pull fails, critical files are missing, or repository state is broken, the cycle stops

Possible statuses:
- `PASS`
- `BLOCKED`

### Stage 1 — Schema Validator
Official script:
- `euru_schema_validator.py`

Purpose:
- validate all Markdown + YAML front matter files that feed the weekly cycle

Minimum scope:
- `paper_trade`
- `daily_journal`
- `learning_report`
- `scorecard`
- threshold profiles and changelogs, when relevant

Output:
- validation result per file
- counts of valid, warning, and invalid files
- schema validation report when requested

Blocking rule:
- invalid schema blocks the cycle

Possible statuses:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`

### Stage 2 — Learning Preflight
Official script:
- `euru_learning_preflight.py`

Purpose:
- act as the mandatory execution gate before learning

Responsibilities:
- run the schema validator
- consolidate allow/block decision
- record preflight result
- permit or deny the learning engine

Output:
- `LEARNING_PREFLIGHT_REPORT_<timestamp>.md`

Blocking rule:
- if preflight is blocked, the learning engine must not run

Possible statuses:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`

### Stage 3 — Learning Engine
Official script:
- `euru_learning_engine.py`

Purpose:
- analyze closed trades and daily journals
- extract metrics, patterns, and governance suggestions
- generate the official weekly learning intelligence

Inputs:
- `PAPER_TRADE_*.md`
- `JOURNAL_*.md`

Primary output:
- `LEARNING_REPORT_<date>.md`

Possible statuses:
- `PASS`
- `FAILED`

### Stage 4 — Canonical Learning Report
Official artifact:
- `LEARNING_REPORT_<date>.md`

Purpose:
- become the authoritative, schema-compliant weekly learning document

Minimum contents:
- performance summary
- patterns identified
- score engine vs actual results
- asset alerts
- setup alerts
- agent deviation analysis
- governance suggestions
- pending human decisions
- simulate readiness check
- next learning actions

Possible statuses:
- `GENERATED`
- `MISSING`
- `INVALID_SCHEMA`

### Stage 5 — Scorecard Engine
Official script:
- `euru_scorecard_engine.py`

Purpose:
- convert the weekly learning report into multidimensional governance outputs

Official scopes:
- `system`
- `asset`
- `setup`
- `agent`
- `score_engine`

Expected outputs:
- `SCORECARD_system_euru_tos_<period>.md`
- `SCORECARD_asset_<symbol>_<period>.md`
- `SCORECARD_setup_<setup>_<period>.md`
- `SCORECARD_agent_<agent>_<period>.md`
- `SCORECARD_score_engine_<profile>_<period>.md`
- `SCORECARD_RUN_REPORT_<timestamp>.md`

Blocking rule:
- if the engine fails entirely, the Friday cycle marks `scorecards` as failed
- if the engine partially succeeds, the cycle may close with warnings

Possible statuses:
- `GENERATED`
- `PARTIAL`
- `FAILED`

### Stage 6 — Human Governance Review
Purpose:
- submit all non-self-authorized decisions to human review

Input:
- learning report
- scorecards
- threshold metadata
- critical alerts
- governance suggestions Type 1, 2, and 3

Output:
- approval
- adjustment
- block
- escalation

Possible statuses:
- `APPROVED`
- `REVIEW_REQUIRED`
- `BLOCKED`

### Stage 7 — Weekly Close
Purpose:
- formally close the weekly cycle

Output:
- final cycle status
- saved artifacts
- consolidated log
- next focus defined

Possible statuses:
- `CLOSED_SUCCESS`
- `CLOSED_WITH_WARNINGS`
- `CLOSED_BLOCKED`

## 4. Official pipeline state machine

```text
FRIDAY_CYCLE_INIT
→ GITHUB_SYNC
→ SCHEMA_VALIDATION
→ LEARNING_PREFLIGHT
→ LEARNING_ENGINE
→ LEARNING_REPORT_READY
→ SCORECARDS_READY
→ HUMAN_REVIEW
→ WEEKLY_CLOSE
```

Failure states:

```text
GITHUB_SYNC_BLOCKED
SCHEMA_BLOCKED
PREFLIGHT_BLOCKED
LEARNING_FAILED
SCORECARD_FAILED
HUMAN_REVIEW_BLOCKED
```

The cycle never skips stages.

## 5. Blocking policy

### Hard block
The cycle must stop immediately if:
- GitHub sync fails
- a critical file is missing
- schema is invalid
- preflight blocks execution
- learning engine fails with no usable learning report

### Warning-only continuation
The cycle may continue with warnings if:
- there are non-critical schema warnings
- a legacy file is still temporarily supported
- some secondary scorecards fail, but the system scorecard and learning report are intact

## 6. Official artifacts generated by the Friday cycle

### Mandatory
- `LEARNING_PREFLIGHT_REPORT_<timestamp>.md`
- `LEARNING_REPORT_<date>.md`
- at least one `SCORECARD_system_euru_tos_<period>.md`
- one `FRIDAY_CYCLE_REPORT_<timestamp>.md`

### Recommended
- `SCORECARD_asset_<symbol>_<period>.md`
- `SCORECARD_setup_<setup>_<period>.md`
- `SCORECARD_agent_<agent>_<period>.md`
- `SCORECARD_score_engine_<profile>_<period>.md`
- `SCORECARD_RUN_REPORT_<timestamp>.md`

### Optional
- repository snapshot
- commit/branch summary
- human review summary

## 7. Minimal target structure

```text
Euru_TOS/
├── euru_schema_validator.py
├── euru_learning_preflight.py
├── euru_learning_engine.py
├── euru_scorecard_engine.py
├── euru_threshold_registry.py
├── euru_friday_cycle.py
│
├── 00_GOVERNANCA/
│   ├── SCHEMAS/
│   ├── PIPELINES/
│   │   └── EURU_FRIDAY_CYCLE.md
│   └── THRESHOLDS/
│       ├── PROFILES/
│       └── CHANGELOGS/
│
├── 08_DADOS_E_JOURNAL/
│   ├── JOURNAL_TRADES/
│   ├── JOURNAL_DAILY/
│   └── SCORECARDS/
│       ├── LEARNING_REPORTS/
│       ├── SCORECARDS/
│       ├── PREFLIGHT_REPORTS/
│       └── SCORECARD_RUN_REPORTS/
```

## 8. Recommended execution

While the orchestrator exists, the official entrypoint is:

```bash
python euru_friday_cycle.py --root .
```

Optional flags:
- `--strict-warnings`
- `--allow-non-git-root`
- `--json`

The scheduler must point to the orchestrator, not to learning or scorecard scripts directly.

## 9. Official scheduled task rule

### Wrong
- Scheduler → `euru_learning_engine.py`
- Scheduler → `euru_learning_preflight.py`
- Scheduler → `euru_scorecard_engine.py`

### Correct
- Scheduler → `euru_friday_cycle.py`

Official time:
- Friday
- after GitHub sync
- current suggested time: **20:30**

## 10. Minimum weekly success criteria

A week may only be considered operationally closed if:
- schema validator ran
- preflight ran
- learning report was generated
- scorecard engine produced at least the system scorecard
- pending human decisions are explicitly listed

If any of these are missing, the week is incomplete.

## 11. Constitutional rules of the Friday cycle

1. Euru never learns from invalid files.
2. Euru never generates scorecards without a learning report.
3. Euru never skips preflight.
4. Euru never treats warnings as silent success.
5. Euru always ends the week with an explicit governance state.
6. Euru always closes Friday with multidimensional governance, not just system-level status.

## 12. Instruction for the receiving AI

```md
Adopt the Friday cycle below as the official weekly operating ritual of Euru_TOS.

Official order:
1. GitHub Sync
2. Schema Validator
3. Learning Preflight
4. Learning Engine
5. Canonical Learning Report
6. Scorecard Engine
7. Human Governance Review
8. Weekly Close

Execution rules:
- never run learning directly from the scheduler
- never run scorecards directly from the scheduler
- always schedule the orchestrator
- block the cycle on invalid schema
- treat preflight as the official learning permission gate
- generate multidimensional scorecards every Friday
- end every Friday cycle with an explicit governance state
```

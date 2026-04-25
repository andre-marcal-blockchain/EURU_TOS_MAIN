# EURU Friday Cycle Report

- cycle_started_at: 2026-04-13T06:50:11Z
- cycle_finished_at: 2026-04-13T06:50:12Z
- overall_status: CLOSED_WITH_WARNINGS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-13T06:50:11Z | 2026-04-13T06:50:11Z | 0 |
| schema_validation | PASS | 2026-04-13T06:50:11Z | 2026-04-13T06:50:11Z | 1 |
| learning_preflight | PASS | 2026-04-13T06:50:11Z | 2026-04-13T06:50:11Z | 1 |
| learning_engine | PASS | 2026-04-13T06:50:11Z | 2026-04-13T06:50:12Z | 1 |
| learning_report | GENERATED | 2026-04-13T06:50:12Z | 2026-04-13T06:50:12Z | 1 |
| scorecards | GENERATED | 2026-04-13T06:50:12Z | 2026-04-13T06:50:12Z | 1 |
| human_governance_review | REVIEW_REQUIRED | 2026-04-13T06:50:12Z | 2026-04-13T06:50:12Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-13T06:50:11Z
- ended_at: 2026-04-13T06:50:11Z

### Details

```json
{
  "root": "/home/claude/EURU_WORK/Euru_TOS",
  "git_pull": false,
  "branch": "main",
  "commit": "d99fa840f956bd57248ad76b5124005890140a35",
  "dirty_files": [
    " M 00_GOVERNANCA/PIPELINES/EURU_FRIDAY_CYCLE.md",
    "?? 00_GOVERNANCA/PIPELINES/EURU_FRIDAY_CYCLE_v1.0_backup.md",
    "?? 08_DADOS_E_JOURNAL/SCORECARDS/FRIDAY_CYCLE_REPORTS/",
    "?? 08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_PREFLIGHT_REPORT_2026-04-13_065003.md",
    "?? 08_DADOS_E_JOURNAL/SCORECARDS/SCHEMA_VALIDATION_REPORT_2026-04-13.md",
    "?? euru_friday_cycle_v1.0_backup.py",
    "?? euru_scorecard_engine.py"
  ],
  "dirty_count": 7,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-13T06:50:11Z
- ended_at: 2026-04-13T06:50:11Z

### Details

```json
{
  "total_files": 22,
  "valid_files": 22,
  "invalid_files": 0,
  "warning_count": 0,
  "error_count": 0,
  "by_schema": {
    "daily_journal": {
      "total": 3,
      "valid": 3,
      "invalid": 0
    },
    "paper_trade": {
      "total": 3,
      "valid": 3,
      "invalid": 0
    },
    "scorecard": {
      "total": 16,
      "valid": 16,
      "invalid": 0
    }
  }
}
```

### Artifacts

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/SCHEMA_VALIDATION_REPORT_2026-04-13.md`

## learning_preflight

- status: PASS
- started_at: 2026-04-13T06:50:11Z
- ended_at: 2026-04-13T06:50:11Z

### Details

```json
{
  "reason": "Schema validation passed. Learning engine may run.",
  "strict_warnings": false,
  "summary": {
    "total_files": 22,
    "valid_files": 22,
    "invalid_files": 0,
    "warning_count": 0,
    "error_count": 0,
    "by_schema": {
      "daily_journal": {
        "total": 3,
        "valid": 3,
        "invalid": 0
      },
      "paper_trade": {
        "total": 3,
        "valid": 3,
        "invalid": 0
      },
      "scorecard": {
        "total": 16,
        "valid": 16,
        "invalid": 0
      }
    }
  }
}
```

### Artifacts

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_PREFLIGHT_REPORT_2026-04-13_065011.md`

## learning_engine

- status: PASS
- started_at: 2026-04-13T06:50:11Z
- ended_at: 2026-04-13T06:50:12Z

### Details

```json
{
  "trade_files_found": 3,
  "closed_trades_parsed": 3,
  "journal_files_found": 3,
  "readiness": {
    "sample_size": 3,
    "enough_sample": false,
    "win_rate_ok": false,
    "rr_ok": false,
    "expectancy_ok": false,
    "suggestion": "CONTINUE SIMULATE",
    "details": {
      "win_rate": 0.0,
      "avg_rr": null,
      "expectancy": null
    }
  }
}
```

### Artifacts

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_2026-04-13.md`

## learning_report

- status: GENERATED
- started_at: 2026-04-13T06:50:12Z
- ended_at: 2026-04-13T06:50:12Z

### Details

```json
{
  "report_path": "/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_2026-04-13.md",
  "canonicalized": true
}
```

### Artifacts

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_2026-04-13.md`

## scorecards

- status: GENERATED
- started_at: 2026-04-13T06:50:12Z
- ended_at: 2026-04-13T06:50:12Z

### Details

```json
{
  "engine_mode": "external_engine_present_but_not_invoked_by_default",
  "generated_count": 1
}
```

### Artifacts

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/SCORECARDS/SCORECARD_system_euru_tos_2026-W16.md`

## human_governance_review

- status: REVIEW_REQUIRED
- started_at: 2026-04-13T06:50:12Z
- ended_at: 2026-04-13T06:50:12Z

### Details

```json
{
  "pending_decisions": [
    "Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades."
  ],
  "scorecards_reviewed": [
    "/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/SCORECARDS/SCORECARD_system_euru_tos_2026-W16.md"
  ]
}
```

### Artifacts

- none

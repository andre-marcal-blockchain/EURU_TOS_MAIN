# EURU Friday Cycle Report

- cycle_started_at: 2026-04-13T06:50:03Z
- cycle_finished_at: 2026-04-13T06:50:04Z
- overall_status: CLOSED_WITH_WARNINGS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-13T06:50:03Z | 2026-04-13T06:50:03Z | 0 |
| schema_validation | PASS | 2026-04-13T06:50:03Z | 2026-04-13T06:50:03Z | 1 |
| learning_preflight | PASS | 2026-04-13T06:50:03Z | 2026-04-13T06:50:03Z | 1 |
| learning_engine | PASS | 2026-04-13T06:50:03Z | 2026-04-13T06:50:04Z | 0 |
| learning_report | SKIPPED | 2026-04-13T06:50:04Z | 2026-04-13T06:50:04Z | 0 |
| scorecards | SKIPPED | 2026-04-13T06:50:04Z | 2026-04-13T06:50:04Z | 0 |
| human_governance_review | REVIEW_REQUIRED | 2026-04-13T06:50:04Z | 2026-04-13T06:50:04Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-13T06:50:03Z
- ended_at: 2026-04-13T06:50:03Z

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
    "?? euru_friday_cycle_v1.0_backup.py",
    "?? euru_scorecard_engine.py"
  ],
  "dirty_count": 4,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-13T06:50:03Z
- ended_at: 2026-04-13T06:50:03Z

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
- started_at: 2026-04-13T06:50:03Z
- ended_at: 2026-04-13T06:50:03Z

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

- `/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_PREFLIGHT_REPORT_2026-04-13_065003.md`

## learning_engine

- status: PASS
- started_at: 2026-04-13T06:50:03Z
- ended_at: 2026-04-13T06:50:04Z

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

- none

## learning_report

- status: SKIPPED
- started_at: 2026-04-13T06:50:04Z
- ended_at: 2026-04-13T06:50:04Z

### Details

```json
{
  "report_path": "/home/claude/EURU_WORK/Euru_TOS/08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_2026-04-13.md",
  "reason": "learning engine executed in dry-run mode"
}
```

### Artifacts

- none

## scorecards

- status: SKIPPED
- started_at: 2026-04-13T06:50:04Z
- ended_at: 2026-04-13T06:50:04Z

### Details

```json
{
  "reason": "learning dry-run mode"
}
```

### Artifacts

- none

## human_governance_review

- status: REVIEW_REQUIRED
- started_at: 2026-04-13T06:50:04Z
- ended_at: 2026-04-13T06:50:04Z

### Details

```json
{
  "pending_decisions": [
    "Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades."
  ],
  "scorecards_reviewed": []
}
```

### Artifacts

- none

# EURU Friday Cycle Report

- cycle_started_at: 2026-04-12T21:49:47Z
- cycle_finished_at: 2026-04-12T21:49:47Z
- overall_status: CLOSED_WITH_WARNINGS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 0 |
| schema_validation | PASS | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 1 |
| learning_preflight | PASS | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 1 |
| learning_engine | PASS | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 1 |
| learning_report | GENERATED | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 1 |
| scorecards | GENERATED | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 1 |
| human_governance_review | REVIEW_REQUIRED | 2026-04-12T21:49:47Z | 2026-04-12T21:49:47Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\Euru_TOS_GITHUB",
  "git_pull": false,
  "branch": "main",
  "commit": "d6af2fb9ebb631d2df46376681ed4a098a132483",
  "dirty_files": [],
  "dirty_count": 0,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

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

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-12.md`

## learning_preflight

- status: PASS
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

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

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_PREFLIGHT_REPORT_2026-04-12_234947.md`

## learning_engine

- status: PASS
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

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

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-12.md`

## learning_report

- status: GENERATED
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

### Details

```json
{
  "report_path": "C:\\Users\\andre\\Desktop\\Euru_TOS_GITHUB\\08_DADOS_E_JOURNAL\\SCORECARDS\\LEARNING_REPORT_2026-04-12.md",
  "canonicalized": true
}
```

### Artifacts

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-12.md`

## scorecards

- status: GENERATED
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

### Details

```json
{
  "generated_count": 1,
  "engine_mode": "built_in_fallback"
}
```

### Artifacts

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\SCORECARDS\SCORECARD_system_euru_tos_2026-W15.md`

## human_governance_review

- status: REVIEW_REQUIRED
- started_at: 2026-04-12T21:49:47Z
- ended_at: 2026-04-12T21:49:47Z

### Details

```json
{
  "pending_decisions": [
    "Review setup 'trend_continuation' within 24h and add checklist rules or disqualifiers before allowing new trades."
  ],
  "scorecards_reviewed": [
    "C:\\Users\\andre\\Desktop\\Euru_TOS_GITHUB\\08_DADOS_E_JOURNAL\\SCORECARDS\\SCORECARDS\\SCORECARD_system_euru_tos_2026-W15.md"
  ]
}
```

### Artifacts

- none

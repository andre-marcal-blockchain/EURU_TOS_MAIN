# EURU Friday Cycle Report

- cycle_started_at: 2026-04-25T10:25:46Z
- cycle_finished_at: 2026-04-25T10:25:46Z
- overall_status: CLOSED_SUCCESS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 0 |
| schema_validation | PASS | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 1 |
| learning_preflight | PASS | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 1 |
| learning_engine | PASS | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 1 |
| learning_report | GENERATED | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 1 |
| scorecards | GENERATED | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 1 |
| human_governance_review | APPROVED | 2026-04-25T10:25:46Z | 2026-04-25T10:25:46Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\EURU TOS MAIN",
  "git_pull": false,
  "branch": "main",
  "commit": "ff907c7606a322f9bb55f34b39303844798454be",
  "dirty_files": [],
  "dirty_count": 0,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "total_files": 72,
  "valid_files": 72,
  "invalid_files": 0,
  "warning_count": 0,
  "error_count": 0,
  "by_schema": {
    "daily_journal": {
      "total": 13,
      "valid": 13,
      "invalid": 0
    },
    "paper_trade": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "scorecard": {
      "total": 19,
      "valid": 19,
      "invalid": 0
    },
    "asian_scan_report": {
      "total": 9,
      "valid": 9,
      "invalid": 0
    },
    "breakout_scan_report": {
      "total": 1,
      "valid": 1,
      "invalid": 0
    },
    "learning_report": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "scout_report": {
      "total": 12,
      "valid": 12,
      "invalid": 0
    },
    "trade_monitor_report": {
      "total": 10,
      "valid": 10,
      "invalid": 0
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-25.md`

## learning_preflight

- status: PASS
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "reason": "Schema validation passed. Learning engine may run.",
  "strict_warnings": false,
  "summary": {
    "total_files": 72,
    "valid_files": 72,
    "invalid_files": 0,
    "warning_count": 0,
    "error_count": 0,
    "by_schema": {
      "daily_journal": {
        "total": 13,
        "valid": 13,
        "invalid": 0
      },
      "paper_trade": {
        "total": 4,
        "valid": 4,
        "invalid": 0
      },
      "scorecard": {
        "total": 19,
        "valid": 19,
        "invalid": 0
      },
      "asian_scan_report": {
        "total": 9,
        "valid": 9,
        "invalid": 0
      },
      "breakout_scan_report": {
        "total": 1,
        "valid": 1,
        "invalid": 0
      },
      "learning_report": {
        "total": 4,
        "valid": 4,
        "invalid": 0
      },
      "scout_report": {
        "total": 12,
        "valid": 12,
        "invalid": 0
      },
      "trade_monitor_report": {
        "total": 10,
        "valid": 10,
        "invalid": 0
      }
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_PREFLIGHT_REPORT_2026-04-25_122546.md`

## learning_engine

- status: PASS
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "trade_files_found": 4,
  "closed_trades_parsed": 4,
  "journal_files_found": 13,
  "readiness": {
    "sample_size": 4,
    "enough_sample": false,
    "win_rate_ok": true,
    "rr_ok": false,
    "expectancy_ok": false,
    "suggestion": "CONTINUE SIMULATE",
    "details": {
      "win_rate": 1.0,
      "avg_rr": 0.6925,
      "expectancy": null
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-25.md`

## learning_report

- status: GENERATED
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "report_path": "C:\\Users\\andre\\Desktop\\EURU TOS MAIN\\08_DADOS_E_JOURNAL\\SCORECARDS\\LEARNING_REPORT_2026-04-25.md",
  "canonicalized": true
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-25.md`

## scorecards

- status: GENERATED
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "engine_mode": "external_engine_present_but_not_invoked_by_default",
  "generated_count": 1
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCORECARDS\SCORECARD_system_euru_tos_2026-W17.md`

## human_governance_review

- status: APPROVED
- started_at: 2026-04-25T10:25:46Z
- ended_at: 2026-04-25T10:25:46Z

### Details

```json
{
  "pending_decisions": [],
  "scorecards_reviewed": [
    "C:\\Users\\andre\\Desktop\\EURU TOS MAIN\\08_DADOS_E_JOURNAL\\SCORECARDS\\SCORECARDS\\SCORECARD_system_euru_tos_2026-W17.md"
  ]
}
```

### Artifacts

- none

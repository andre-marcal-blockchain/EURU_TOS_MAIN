# EURU Friday Cycle Report

- cycle_started_at: 2026-04-17T19:41:26Z
- cycle_finished_at: 2026-04-17T19:41:27Z
- overall_status: CLOSED_SUCCESS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-17T19:41:26Z | 2026-04-17T19:41:27Z | 0 |
| schema_validation | PASS | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 1 |
| learning_preflight | PASS | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 1 |
| learning_engine | PASS | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 1 |
| learning_report | GENERATED | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 1 |
| scorecards | GENERATED | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 1 |
| human_governance_review | APPROVED | 2026-04-17T19:41:27Z | 2026-04-17T19:41:27Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-17T19:41:26Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\EURO MAIN",
  "git_pull": false,
  "branch": "main",
  "commit": "aa9ca79f6360e762889a480586e597ab8ede6ed6",
  "dirty_files": [
    " M .claude/settings.local.json",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_2026-04-17.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_003.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-14.md",
    " D 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-14_052247.md",
    " D 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-14_052832.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-15.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-16.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-17.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/BREAKOUT_SCAN_2026-04-15.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCHEMA_VALIDATION_REPORT_2026-04-17.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-14.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-15.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-16.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-17.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/TRADE_MONITOR_REPORT_2026-04-16.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/TRADE_MONITOR_REPORT_2026-04-17.md",
    " ? Euru_TOSOld_02026-04-10",
    " ? Euru_TOS_GITHUB",
    " M euru_schema_validator.py"
  ],
  "dirty_count": 20,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "total_files": 40,
  "valid_files": 40,
  "invalid_files": 0,
  "warning_count": 0,
  "error_count": 0,
  "by_schema": {
    "daily_journal": {
      "total": 6,
      "valid": 6,
      "invalid": 0
    },
    "paper_trade": {
      "total": 3,
      "valid": 3,
      "invalid": 0
    },
    "scorecard": {
      "total": 18,
      "valid": 18,
      "invalid": 0
    },
    "asian_scan_report": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "breakout_scan_report": {
      "total": 1,
      "valid": 1,
      "invalid": 0
    },
    "learning_report": {
      "total": 2,
      "valid": 2,
      "invalid": 0
    },
    "scout_report": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "trade_monitor_report": {
      "total": 2,
      "valid": 2,
      "invalid": 0
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-17.md`

## learning_preflight

- status: PASS
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "reason": "Schema validation passed. Learning engine may run.",
  "strict_warnings": false,
  "summary": {
    "total_files": 40,
    "valid_files": 40,
    "invalid_files": 0,
    "warning_count": 0,
    "error_count": 0,
    "by_schema": {
      "daily_journal": {
        "total": 6,
        "valid": 6,
        "invalid": 0
      },
      "paper_trade": {
        "total": 3,
        "valid": 3,
        "invalid": 0
      },
      "scorecard": {
        "total": 18,
        "valid": 18,
        "invalid": 0
      },
      "asian_scan_report": {
        "total": 4,
        "valid": 4,
        "invalid": 0
      },
      "breakout_scan_report": {
        "total": 1,
        "valid": 1,
        "invalid": 0
      },
      "learning_report": {
        "total": 2,
        "valid": 2,
        "invalid": 0
      },
      "scout_report": {
        "total": 4,
        "valid": 4,
        "invalid": 0
      },
      "trade_monitor_report": {
        "total": 2,
        "valid": 2,
        "invalid": 0
      }
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_PREFLIGHT_REPORT_2026-04-17_214127.md`

## learning_engine

- status: PASS
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "trade_files_found": 3,
  "closed_trades_parsed": 3,
  "journal_files_found": 6,
  "readiness": {
    "sample_size": 3,
    "enough_sample": false,
    "win_rate_ok": true,
    "rr_ok": false,
    "expectancy_ok": false,
    "suggestion": "CONTINUE SIMULATE",
    "details": {
      "win_rate": 1.0,
      "avg_rr": 0.9033333333333333,
      "expectancy": null
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-17.md`

## learning_report

- status: GENERATED
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "report_path": "C:\\Users\\andre\\Desktop\\EURO MAIN\\08_DADOS_E_JOURNAL\\SCORECARDS\\LEARNING_REPORT_2026-04-17.md",
  "canonicalized": true
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_REPORT_2026-04-17.md`

## scorecards

- status: GENERATED
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "engine_mode": "external_engine_present_but_not_invoked_by_default",
  "generated_count": 1
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCORECARDS\SCORECARD_system_euru_tos_2026-W16.md`

## human_governance_review

- status: APPROVED
- started_at: 2026-04-17T19:41:27Z
- ended_at: 2026-04-17T19:41:27Z

### Details

```json
{
  "pending_decisions": [],
  "scorecards_reviewed": [
    "C:\\Users\\andre\\Desktop\\EURO MAIN\\08_DADOS_E_JOURNAL\\SCORECARDS\\SCORECARDS\\SCORECARD_system_euru_tos_2026-W16.md"
  ]
}
```

### Artifacts

- none

# EURU Friday Cycle Report

- cycle_started_at: 2026-04-12T21:33:04Z
- cycle_finished_at: 2026-04-12T21:33:05Z
- overall_status: CLOSED_WITH_WARNINGS

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-12T21:33:04Z | 2026-04-12T21:33:04Z | 0 |
| schema_validation | PASS | 2026-04-12T21:33:04Z | 2026-04-12T21:33:05Z | 1 |
| learning_preflight | PASS | 2026-04-12T21:33:05Z | 2026-04-12T21:33:05Z | 1 |
| learning_engine | PASS | 2026-04-12T21:33:05Z | 2026-04-12T21:33:05Z | 0 |
| learning_report | SKIPPED | 2026-04-12T21:33:05Z | 2026-04-12T21:33:05Z | 0 |
| scorecards | SKIPPED | 2026-04-12T21:33:05Z | 2026-04-12T21:33:05Z | 0 |
| human_governance_review | REVIEW_REQUIRED | 2026-04-12T21:33:05Z | 2026-04-12T21:33:05Z | 0 |

## github_sync

- status: PASS
- started_at: 2026-04-12T21:33:04Z
- ended_at: 2026-04-12T21:33:04Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\Euru_TOS_GITHUB",
  "git_pull": false,
  "branch": "main",
  "commit": "dfe5792e8653bff0eb5c802981952811d4d90b59",
  "dirty_files": [
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_2026-04-09.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_2026-04-10.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_2026-04-11.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_001.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_002.md",
    " M 08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_003.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-06.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-07.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-08.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-09.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_2026-04-10.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-01.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-02.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-03.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-04.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-05.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-06.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-07.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-08.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-09.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-10.md",
    " M 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-11.md",
    "?? 08_DADOS_E_JOURNAL/SCORECARDS/FRIDAY_CYCLE_REPORTS/",
    "?? 08_DADOS_E_JOURNAL/SCORECARDS/SCHEMA_VALIDATION_REPORT_2026-04-12.md"
  ],
  "dirty_count": 24,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: PASS
- started_at: 2026-04-12T21:33:04Z
- ended_at: 2026-04-12T21:33:05Z

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
- started_at: 2026-04-12T21:33:05Z
- ended_at: 2026-04-12T21:33:05Z

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

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\LEARNING_PREFLIGHT_REPORT_2026-04-12_233305.md`

## learning_engine

- status: PASS
- started_at: 2026-04-12T21:33:05Z
- ended_at: 2026-04-12T21:33:05Z

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
- started_at: 2026-04-12T21:33:05Z
- ended_at: 2026-04-12T21:33:05Z

### Details

```json
{
  "report_path": "C:\\Users\\andre\\Desktop\\Euru_TOS_GITHUB\\08_DADOS_E_JOURNAL\\SCORECARDS\\LEARNING_REPORT_2026-04-12.md",
  "reason": "learning engine executed in dry-run mode"
}
```

### Artifacts

- none

## scorecards

- status: SKIPPED
- started_at: 2026-04-12T21:33:05Z
- ended_at: 2026-04-12T21:33:05Z

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
- started_at: 2026-04-12T21:33:05Z
- ended_at: 2026-04-12T21:33:05Z

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

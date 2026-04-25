# EURU Friday Cycle Report

- cycle_started_at: 2026-04-12T21:28:19Z
- cycle_finished_at: 2026-04-12T21:28:19Z
- overall_status: CLOSED_BLOCKED

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-12T21:28:19Z | 2026-04-12T21:28:19Z | 0 |
| schema_validation | BLOCKED | 2026-04-12T21:28:19Z | 2026-04-12T21:28:19Z | 1 |

## github_sync

- status: PASS
- started_at: 2026-04-12T21:28:19Z
- ended_at: 2026-04-12T21:28:19Z

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

- status: BLOCKED
- started_at: 2026-04-12T21:28:19Z
- ended_at: 2026-04-12T21:28:19Z

### Details

```json
{
  "total_files": 22,
  "valid_files": 0,
  "invalid_files": 22,
  "warning_count": 0,
  "error_count": 189,
  "by_schema": {
    "daily_journal": {
      "total": 3,
      "valid": 0,
      "invalid": 3
    },
    "paper_trade": {
      "total": 3,
      "valid": 0,
      "invalid": 3
    },
    "scorecard": {
      "total": 16,
      "valid": 0,
      "invalid": 16
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\Euru_TOS_GITHUB\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-12.md`

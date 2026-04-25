# EURU_TOS — Handoff File Index

This index lists the final shareable files prepared for the receiving AI.

## Recommended implementation order

1. Read `EURU_FRIDAY_CYCLE.md`
2. Read schema files:
   - `EURU_SCHEMA_TRADE_AND_JOURNAL.md`
   - `EURU_SCHEMA_LEARNING_REPORT_AND_SCORECARD.md`
   - `EURU_SCHEMA_GOVERNANCE_THRESHOLDS.md`
3. Install scripts:
   - `euru_schema_validator.py`
   - `euru_learning_preflight.py`
   - `euru_learning_engine.py`
   - `euru_threshold_registry.py`
   - `euru_friday_cycle.py`
4. Install task registration scripts
5. Place threshold profiles and changelogs in `00_GOVERNANCA/THRESHOLDS/`
6. Run manual smoke tests before enabling the scheduled task

## Shareable files

### Core documentation
- `EURU_FRIDAY_CYCLE.md`
- `EURU_SCHEMA_TRADE_AND_JOURNAL.md`
- `EURU_SCHEMA_LEARNING_REPORT_AND_SCORECARD.md`
- `EURU_SCHEMA_GOVERNANCE_THRESHOLDS.md`

### Core Python executables
- `euru_schema_validator.py`
- `euru_learning_preflight.py`
- `euru_learning_engine.py`
- `euru_threshold_registry.py`
- `euru_friday_cycle.py`

### Windows scheduling scripts
- `register_euru_learning_task.ps1`
- `register_euru_learning_preflight_task.ps1`
- `register_euru_friday_cycle_task.ps1`

### Threshold governance examples
- `00_GOVERNANCA/THRESHOLDS/PROFILES/THRESHOLDS_PROFILE_system_default_v1.0.0.md`
- `00_GOVERNANCA/THRESHOLDS/PROFILES/THRESHOLDS_PROFILE_system_default_v1.1.0.md`
- `00_GOVERNANCA/THRESHOLDS/CHANGELOGS/THRESHOLDS_CHANGELOG_system_default_v1.0.0_to_v1.1.0.md`

## Minimal target folders inside Euru_TOS

```text
Euru_TOS/
├── 00_GOVERNANCA/
│   ├── SCHEMAS/
│   ├── PIPELINES/
│   └── THRESHOLDS/
│       ├── PROFILES/
│       └── CHANGELOGS/
├── 08_DADOS_E_JOURNAL/
│   ├── JOURNAL_TRADES/
│   ├── JOURNAL_DAILY/
│   └── SCORECARDS/
├── euru_schema_validator.py
├── euru_learning_preflight.py
├── euru_learning_engine.py
├── euru_threshold_registry.py
└── euru_friday_cycle.py
```

# EURU Migration Manifest

Date: 2026-04-25  
Source: `C:\Users\andre\Desktop\EURO MAIN`  
Target: `C:\Users\andre\Desktop\EURU TOS MAIN`

## Migration Intent

Create a clean canonical repository for Euru OS without losing the operational compatibility of the current scripts.

This migration preserves the existing folder names because the active Python scripts rely on those paths.

## Included As Active

- `00_MASTER`
- `00_GOVERNANCA`
- `01_GOVERNANCA`
- `02_BINANCE_SETUP`
- `03_ARQUITETURA`
- `04_AGENTES`
- `05_PROMPTS`
- `06_RISCO_E_EXECUCAO`
- `07_OPERACAO`
- `08_DADOS_E_JOURNAL`
- `09_LOGS_E_INCIDENTES`
- `10_AUTOMACOES`
- `11_CONFIG_PLACEHOLDERS`
- Root-level `euru_*.py` and `euru_*.ps1`
- `docs`

## Included As Archive

- Snapshot TXT and PDF from 2026-04-25.
- Earlier handoff documents.
- Old public README.
- Legacy DOCX files moved into `99_ARCHIVE/DOCX_LEGACY`.

## Excluded From Active Use

- `Euru_TOS`
- `Euru_TOSOld_*`
- `Euru_TOS_*` migrated/extracted folders
- Zip files
- `__pycache__`
- Backup folders inside governance/setup directories
- Duplicate script `euru_trade_monitor_1.py`
- Nested duplicate `docs/docs`

## New Canonical Files Added

- `README.md`
- `CLAUDE.md`
- `00_MASTER/EURU_OPERATIONAL_STATE.md`
- `00_MASTER/EURU_SOURCE_OF_TRUTH.md`
- `00_MASTER/EURU_CONSOLIDATION_ROADMAP.md`
- `00_MASTER/EURU_MASTER_INDEX.md`
- `00_MASTER/EURU_MIGRATION_MANIFEST_2026-04-25.md`
- `99_ARCHIVE/README_ARCHIVE.md`
- `.gitignore`

## Post-Migration Required Checks

1. Run schema validation from the new root.
2. Confirm scripts write to `08_DADOS_E_JOURNAL` under the new root.
3. Confirm Git status after initializing or connecting the new repository.
4. Update Windows scheduled tasks to point to `C:\Users\andre\Desktop\EURU TOS MAIN`.
5. Resume consolidation roadmap Phase 2.


# EURU OS — COMPLETE SYSTEM AUDIT
**Generated:** 2026-04-15  
**Operator:** Andre Marcal  
**System Mode:** SIMULATE — HEALTHY  
**Purpose:** Master reference document for new chat sessions. Comprehensive snapshot of all folders, files, scripts, agents, governance, trades, and automations.

---

## TABLE OF CONTENTS

1. [System Overview](#1-system-overview)
2. [Complete Folder Tree](#2-complete-folder-tree)
3. [Python & PowerShell Scripts](#3-python--powershell-scripts)
4. [Agent Roster — Core Pipeline](#4-agent-roster--core-pipeline)
5. [Agent Roster — Breakout Intelligence Layer](#5-agent-roster--breakout-intelligence-layer)
6. [Governance Documents](#6-governance-documents)
7. [Current System State](#7-current-system-state)
8. [Automations & Schedules](#8-automations--schedules)
9. [Strategic Decisions Log](#9-strategic-decisions-log)
10. [Paper Trades Status](#10-paper-trades-status)
11. [Git Commit History](#11-git-commit-history)
12. [Known Issues & Pending Items](#12-known-issues--pending-items)

---

## 1. SYSTEM OVERVIEW

**Euru OS** is a multi-agent crypto trading governance and decision framework. It processes market signals through a sequential 10-agent pipeline to produce structured trade decisions. Currently in **SIMULATE phase** (paper trading, no real capital deployed).

| Property | Value |
|---|---|
| Current Phase | SIMULATE (activated 2026-04-08) |
| Pipeline Health | HEALTHY |
| Open Paper Trades | 3 (PT001 AVAX, PT002 NEAR, PT003 ARB) |
| Total Agents | 20 (11 core + 9 Breakout Layer) |
| Daily Scan Assets | 20 (daily TF morning + 4H Asian session) |
| Risk per Trade | 1% of capital |
| Max Combined Exposure | ~40% (currently 33.88%) |
| Simulated Capital | 100 USDT reference |

**Phase progression (never skip):**
```
READ_ONLY manual → READ_ONLY automated → SIMULATE manual → SIMULATE automated → EXECUTE
                                          ↑ CURRENT (semi-manual)
```

---

## 2. COMPLETE FOLDER TREE

```
C:\Users\andre\Desktop\EURO MAIN\
│
├── .claude/                            Claude Code session config
├── .git/                               Git repository metadata
│
├── 00_GOVERNANCA/                      Core governance infrastructure
│   ├── EURU_HANDOFF_FILE_INDEX.md
│   ├── PIPELINES/
│   │   └── EURU_FRIDAY_CYCLE.md
│   ├── SCHEMAS/
│   │   ├── EURU_SCHEMA_GOVERNANCE_THRESHOLDS.md
│   │   ├── EURU_SCHEMA_LEARNING_REPORT_AND_SCORECARD.md
│   │   ├── EURU_SCHEMA_TRADE_AND_JOURNAL.md
│   │   └── EURU_SETUP_TREND_CONTINUATION_OFFICIAL_v1.0.md
│   └── THRESHOLDS/
│       ├── CHANGELOGS/
│       │   └── THRESHOLDS_CHANGELOG_system_default_v1.0.0_to_v1.1.0.md
│       └── PROFILES/
│           ├── THRESHOLDS_PROFILE_system_default_v1.0.0.md
│           └── THRESHOLDS_PROFILE_system_default_v1.1.0.md
│
├── 00_MASTER/                          Master reference documents
│   ├── EURU_AGENT_MAP.md               Full agent map (all 20 agents)
│   ├── EURU_COMPLETE_SYSTEM_AUDIT_2026-04-15.md   ← THIS FILE
│   ├── EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md    Document registry
│   ├── EURU_HANDOFF_PROMPT_MASTER_REGISTRY_OTHER_IA.md
│   └── EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1.md
│
├── 01_GOVERNANCA/                      Governance rules and decisions
│   ├── ADR_0001_EURU_CANONICAL_OPERATIONAL_STATE_READ_ONLY.md
│   ├── ADR_0002_EURU_QUALITY_CONTROL_CANONICAL_FOLDER.md
│   ├── DECISOES_ESTRATEGICAS_REVISADO.md           ← CANONICAL decision log
│   ├── EURU_AGENT_DECISION_STANDARD_REVISADO.md
│   ├── EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.md
│   ├── EURU_DOCUMENT_TEMPLATE_HEADER_CHANGELOG.md
│   ├── EURU_GOVERNANCE_LEGACY_TRIAGE_OFFICIAL_v1.0.md
│   ├── EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0.md
│   ├── EURU_GOVERNANCE_POLICY_ChangeManagement_OFFICIAL_v1.0.md
│   ├── EURU_GOVERNANCE_POLICY_HumanResponsibilities_OFFICIAL_v1.0.md
│   ├── EURU_GOVERNANCE_POLICY_LegacyMigration_OFFICIAL_v1.0.md
│   ├── EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1.md
│   ├── EURU_GOVERNANCE_STANDARD_StatusDefinitions_OFFICIAL_v1.0.md
│   ├── EURU_OS_1_REVISADO.md
│   ├── EURU_OS_REVISADO.md
│   ├── GOVERNANCA_DE_MUDANCAS_REVISADO.md          ← Change management policy
│   ├── PADRAO_UNIFICADO_DE_STATUS_REVISADO.md      ← Status enum definitions
│   ├── README_GOVERNANCE.md
│   ├── REGRAS_MAE_REVISADO.md                      ← Master trading rules
│   ├── REGRAS_MAE_REVISADO_SUMMARY.md              ← Quick-reference rules
│   ├── RESPONSABILIDADES_HUMANOS_REVISADO.md
│   └── backup/
│       ├── DECISOES_ESTRATEGICAS_BACKUP.md
│       ├── GOVERNANCA_DE_MUDANCAS_BACKUP.md
│       ├── PADRAO_UNIFICADO_DE_STATUS_BACKUP.md
│       └── RESPONSABILIDADES_HUMANOS_BACKUP.md
│
├── 02_BINANCE_SETUP/                   Exchange configuration
│   ├── API_KEYS_E_PERMISSOES_REVISADO.docx
│   ├── BINANCE_VERIFY.md
│   ├── CONTA_E_KYC_REVISADO.docx
│   ├── DEMO_TRADING_REVISADO.docx
│   ├── SEGURANCA_E_2FA_REVISADO.docx
│   └── backup/
│       ├── CONTA_E_KYC.md
│       ├── DEMO_TRADING.md
│       └── SEGURANCA_E_2FA.md
│
├── 03_ARQUITETURA/                     Architecture diagrams
│   ├── EURU_ARCHITECTURE_DIAGRAM_PipelineLogic_OFFICIAL_v1.0.md
│   └── PIPELINE_DIAGRAM.md
│
├── 04_AGENTES/                         Agent definitions (20 agents total)
│   ├── 01_SCOUT/                       Core Pipeline Agent 01
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_SCOUT_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 01_RISK_GUARDIAN/               (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 02_FLOW_ANALYST/                Core Pipeline Agent 02
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_FLOW_ANALYST_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 02_STRUCTURE_HUNTER/            (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 03_NEWS_SENTINEL/               Core Pipeline Agent 03
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_NEWS_SENTINEL_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 03_BREAKOUT_CONFIRMATION/       (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 04_QUANT_RISK_OFFICER/          Core Pipeline Agent 04
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_QUANT_RISK_OFFICER_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 04_ALERT_RADAR/                 (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 05_EXECUTION_ORCHESTRATOR/      Core Pipeline Agent 05
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_EXECUTION_ORCHESTRATOR_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 05_MARKET_REGIME/               (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 06_DEVOPS_GUARDIAO/             Core Pipeline Agent 06
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_DEVOPS_GUARDIAO_PROMPT_OFFICIAL_v1.0.md
│   │   └── OUTPUT_FORMAT_FINAL.md
│   ├── 06_TACTICAL_EXECUTION/          (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 07_JOURNAL_AUDITOR/             Core Pipeline Agent 07
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_JOURNAL_AUDITOR_PROMPT_OFFICIAL_v1.0.md
│   │   └── OUTPUT_FORMAT_FINAL.md
│   ├── 07_COMPOUNDING_GOVERNOR/        (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 08_SCORE_ENGINE/                Core Pipeline Agent 08
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_SCORE_ENGINE_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 08_JOURNAL_LEARNING/            (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 08_WATCHDOG/                    PRESERVED REFERENCE (renumbered/superseded)
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_WATCHDOG_PROMPT_OFFICIAL_v1.0.md
│   │   └── OUTPUT_FORMAT_FINAL.md
│   ├── 09_MAC_PLAYBOOK_ANALYST/        Core Pipeline Agent 09
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_MAC_PLAYBOOK_ANALYST_PROMPT_OFFICIAL_v1.0.md
│   │   ├── OUTPUT_FORMAT_FINAL.md
│   │   └── PROMPT_REVISADO.md
│   ├── 09_PROMISE_AUDITOR/             (Breakout mirror in root — legacy position)
│   │   ├── BRIEFING.md
│   │   ├── OUTPUT_FORMAT.md
│   │   └── PROMPT.md
│   ├── 11_QUALITY_CONTROL/             Core Pipeline Agent 10 (numbered 11)
│   │   ├── BRIEFING_FINAL.md
│   │   ├── EURU_AGENTS_QUALITY_CONTROL_PROMPT_OFFICIAL_v1.0.md
│   │   └── OUTPUT_FORMAT_FINAL.md
│   └── BREAKOUT_LAYER/                 Breakout Intelligence Layer (canonical)
│       ├── 01_RISK_GUARDIAN/           BL-01
│       ├── 02_STRUCTURE_HUNTER/        BL-02
│       ├── 03_BREAKOUT_CONFIRMATION/   BL-03
│       ├── 04_ALERT_RADAR/             BL-04
│       ├── 05_MARKET_REGIME/           BL-05
│       ├── 05_SCORING/
│       │   ├── configs/breakout_weights_v1.yaml
│       │   ├── docs/BREAKOUT_SCORING_OVERVIEW.md
│       │   └── schemas/euru_breakout_feature_schema.yaml
│       ├── 06_EXECUTION/
│       │   └── BREAKOUT_EXECUTION_FLOW.md
│       ├── 06_TACTICAL_EXECUTION/      BL-06
│       ├── 07_COMPOUNDING_GOVERNOR/    BL-07
│       ├── 07_GOVERNANCE/
│       │   ├── BREAKOUT_AUDIT_RULES.md
│       │   └── BREAKOUT_GOVERNANCE_RULES.md
│       ├── 08_JOURNAL_LEARNING/        BL-08
│       ├── 08_LEARNING/
│       │   └── BREAKOUT_LEARNING_LOOP.md
│       ├── 09_HANDOFF/
│       │   ├── EURU_BREAKOUT_HANDOFF.md
│       │   └── EURU_BREAKOUT_IMPLEMENTATION_SUMMARY.md
│       └── 09_PROMISE_AUDITOR/         BL-09
│
├── 05_PROMPTS/                         Manual Claude Code prompts
│   ├── PROMPT_PRE_TRADE.md
│   └── PROMPT_WEEKLY_REVIEW.md
│
├── 06_RISCO_E_EXECUCAO/               Risk and execution framework
│   ├── EURU_RISK_FRAMEWORK_RiskMatrix_OFFICIAL_v1.0.md
│   ├── EURU_RISK_POLICY_ExitPolicy_OFFICIAL_v1.0.md
│   └── RISK_MATRIX.md
│
├── 07_OPERACAO/                        Operational procedures
│   ├── CHECKLIST_PRE_TRADE_v2.txt      12-point pre-trade checklist
│   ├── EURU_OPERATIONS_POLICY_ReadOnlyMode_OFFICIAL_v1.0.md
│   ├── EURU_OPERATIONS_RUNBOOK_DocumentalBacklog_OFFICIAL_v1.0.md
│   ├── Politica_Saida_Completa_Euru.txt   Exit policy
│   ├── SIMULATE_SETUP.md
│   ├── SOP_DIARIO_v2.txt               Daily 30-min operational checklist
│   ├── SOP_SEMANAL.txt                 Weekly review checklist
│   └── Teste_Integrado_Pipeline.txt    Integrated pipeline test procedure
│
├── 08_DADOS_E_JOURNAL/                 Data, journals, trades
│   ├── JOURNAL_DAILY/
│   │   ├── JOURNAL_2026-04-14.md
│   │   └── JOURNAL_2026-04-15.md
│   ├── JOURNAL_TRADES/
│   │   ├── JOURNAL_2026-04-09.md
│   │   ├── JOURNAL_2026-04-10.md
│   │   ├── JOURNAL_2026-04-11.md
│   │   ├── PAPER_TRADE_001.md          AVAXUSDT — OPEN
│   │   ├── PAPER_TRADE_002.md          NEARUSDT — OPEN
│   │   └── PAPER_TRADE_003.md          ARBUSDT — OPEN
│   ├── SCORECARDS/
│   │   ├── ASIAN_REPORT_2026-04-06.md through ASIAN_REPORT_2026-04-15.md
│   │   ├── BREAKOUT_SCAN_2026-04-15.md ← First breakout scanner output
│   │   ├── FRIDAY_CYCLE_REPORTS/
│   │   │   ├── FRIDAY_CYCLE_REPORT_2026-04-12_*.md  (4 runs)
│   │   │   └── FRIDAY_CYCLE_REPORT_2026-04-13_*.md  (2 runs)
│   │   ├── LEARNING_PREFLIGHT_REPORT_*.md  (4 files)
│   │   ├── LEARNING_REPORT_2026-04-12.md
│   │   ├── LEARNING_REPORT_2026-04-13.md
│   │   ├── SCHEMA_VALIDATION_REPORT_2026-04-12.md
│   │   ├── SCHEMA_VALIDATION_REPORT_2026-04-13.md
│   │   ├── SCORECARDS/
│   │   │   ├── SCORECARD_system_euru_tos_2026-W15.md
│   │   │   └── SCORECARD_system_euru_tos_2026-W16.md
│   │   └── SCOUT_REPORT_2026-04-01.md through SCOUT_REPORT_2026-04-15.md
│   ├── SNAPSHOTS/
│   └── WATCHLISTS/
│       ├── EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2.md  ← CANONICAL
│       └── WATCHLIST_OFICIAL.md
│
├── 09_LOGS_E_INCIDENTES/
│   ├── EURU_LOGS_REGISTRY_IncidentLog_OFFICIAL_v1.0.md
│   └── INCIDENTES.md                   (no incidents recorded yet)
│
├── 10_AUTOMACOES/                      Windows Task Scheduler scripts
│   ├── register_euru_friday_cycle_task.ps1
│   ├── register_euru_learning_preflight_task.ps1
│   └── register_euru_learning_task.ps1
│
├── 11_CONFIG_PLACEHOLDERS/
│   └── .env.example                    API key template (never commit real keys)
│
├── 99_ARQUIVO_E_NOTAS/                 Archive
│   ├── 09_QUALITY_CONTROL_SUPERSEDED/  (old QC before renumber to 11)
│   ├── 10_QUALITY_CONTROL_SUPERSEDED/  (old QC files)
│   └── EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.1_SUPERSEDED.md
│
├── 99_PRIVATE_NOTES/
│   └── PAPERCLIP_EVALUATION.md
│
├── Claude code/                        Claude Code related files
├── docxwork/                           Node.js docx conversion tools
│
├── Euru_TOS/                           ACTIVE WORKING COPY (run scripts from here)
│   ├── euru_asian_scan.py
│   ├── euru_execution.py
│   ├── euru_flow_analyst.py
│   ├── euru_learning_engine.py
│   ├── euru_mac_analyst.py
│   ├── euru_morning_scan.py
│   ├── euru_quant_risk.py
│   ├── euru_schedule_setup.ps1
│   ├── euru_score_engine.py
│   └── scripts/smoke_test.py
│
├── Euru_TOS_FINAL/                     Final version backup
├── Euru_TOS_GITHUB/                    GitHub-synced version
├── Euru_TOS_MIGRATED/                  Migration backup
├── Euru_TOS_NEW/                       Newest backup
├── Euru_TOSOld_02026-04-10/            Older version snapshot (2026-04-10)
│
│   [ROOT LEVEL — canonical scripts]
├── euru_asian_scan.py
├── euru_breakout_scanner.py
├── euru_flow_analyst.py
├── euru_friday_cycle.py
├── euru_github_sync.ps1
├── euru_journal_auditor.py
├── euru_learning_engine.py
├── euru_learning_preflight.py
├── euru_morning_scan.py
├── euru_schedule_setup.ps1
├── euru_schema_validator.py
├── euru_score_engine.py
├── euru_scorecard_engine.py
├── euru_threshold_registry.py
│
├── CLAUDE.md
├── EURU_HANDOFF_FUNDACAO_SOLIDA_2026-04-13.md
├── EURU_SESSION_HANDOFF_2026-04-11.md
├── EURU_SESSION_HANDOFF_2026-04-12_v2.md
└── EURU_SETUP_TREND_CONTINUATION_OFFICIAL_v1.0.md
```

---

## 3. PYTHON & POWERSHELL SCRIPTS

### 3.1 Core Scan Scripts (run daily)

#### `euru_morning_scan.py`
- **What it does:** Fetches BTCUSDT + 19 altcoins from Binance public API. Runs Scout structure analysis, Flow Analyst (RSI/MACD/OBV/ATR), Score Engine (0–35), and News Sentinel (CryptoPanic). Also integrates Breakout Scanner (as of 2026-04-15). Applies BTC master filter: if BTC is SIDEWAYS/BEARISH, all altcoin SETUP signals downgraded to WATCHLIST.
- **When:** Manually each morning (Block 2 of SOP_DIARIO_v2); also in Windows Scheduled Task
- **Produces:** `08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_YYYY-MM-DD.md`
- **Imports:** `euru_flow_analyst`, `euru_score_engine`, `euru_breakout_scanner` (optional)
- **Assets:** BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, AVAXUSDT, DOTUSDT, LINKUSDT, ADAUSDT, XRPUSDT, WLDUSDT (replaced MATIC), SUIUSDT, NEARUSDT, INJUSDT, ARBUSDT, OPUSDT, FETUSDT, TAOUSDT, RENDERUSDT + 2 more

#### `euru_asian_scan.py`
- **What it does:** Asian session scan on 4H timeframe. Detects lateralization/compression via 5–6 consecutive 4H candles with shrinking ranges (Aguiar Protocol Module 05). Flags volume exhaustion at compression point. BTC 4H master filter still applies.
- **When:** 00:00 UTC (Asian session open), via Windows Scheduled Task
- **Produces:** `08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_YYYY-MM-DD.md`
- **Outputs:** `GEM_ALERT` for compression + volume exhaustion candidates

#### `euru_breakout_scanner.py`
- **What it does:** Implements BL-02 Structure Hunter and BL-03 Breakout Confirmation agents. Per asset (4H, last 50 candles): detects S/R zones, compression, proximity to key levels, classifies last closed 4H candle break quality. Computes `breakout_raw_score` (0–100) across 4 dimensions. Runs standalone or as library imported by morning scan.
- **When:** Integrated into morning scan (as of 2026-04-15); can also run standalone
- **Produces:** `08_DADOS_E_JOURNAL/SCORECARDS/BREAKOUT_SCAN_YYYY-MM-DD.md`

### 3.2 Library Modules (imported, not run directly)

#### `euru_flow_analyst.py`
- **What it does:** Calculates RSI (14 periods), MACD (12/26/9), OBV trend, ATR (14) via Binance public API. Returns `CONFIRMS` / `CONTRADICTS` / `INCONCLUSIVE` verdict.
- **Used by:** `euru_morning_scan.py`, `euru_asian_scan.py`
- **Key function:** `assess_flow(symbol, interval)`

#### `euru_score_engine.py`
- **What it does:** Scores assets 0–35 across 7 criteria (liquidity, volume, structure, flow, news, momentum, volatility). Classifies into tiers (PREMIUM 28–35, BOA 22–27, MEDIA 16–21, IGNORE 0–15). Suggests action per tier.
- **Used by:** `euru_morning_scan.py`
- **Key function:** `compute_score(asset_data)`

### 3.3 Weekly Cycle Orchestration

#### `euru_friday_cycle.py`
- **What it does:** Official weekly pipeline orchestrator. Runs in sequence: GitHub Sync → Schema Validator → Learning Preflight → Learning Engine → Learning Report → Scorecards → Human Governance Review → Weekly Close.
- **When:** Fridays at 20:30 local (Windows Scheduled Task)
- **Produces:** `FRIDAY_CYCLE_REPORT_YYYY-MM-DD_HHMMSS.md`

#### `euru_learning_engine.py`
- **What it does:** Scans closed paper trades and daily journals. Computes performance metrics, identifies patterns, compares Score Engine predictions vs actual results. Tolerant of Markdown variations (key/value, tables, bullet-style fields).
- **When:** Part of Friday Cycle; also can run standalone
- **Produces:** `08_DADOS_E_JOURNAL/SCORECARDS/LEARNING_REPORT_YYYY-MM-DD.md`
- **Reads:** `PAPER_TRADE_*.md`, `JOURNAL_*.md`

#### `euru_learning_preflight.py`
- **What it does:** Mandatory governance gate before learning engine. Runs schema validation, writes validation report on errors/warnings, blocks learning engine if invalid schema files found. Optional strict-warnings mode.
- **When:** Part of Friday Cycle (runs before learning engine)
- **Produces:** `LEARNING_PREFLIGHT_REPORT_*.md`

#### `euru_scorecard_engine.py`
- **What it does:** Generates schema-compliant SCORECARD files from latest LEARNING_REPORT and closed PAPER_TRADE files. Supports system, asset, setup, agent, and score_engine scopes.
- **When:** Part of Friday Cycle
- **Produces:** `SCORECARDS/SCORECARD_system_euru_tos_YYYY-W##.md`

### 3.4 Validation & Registry Tools

#### `euru_schema_validator.py`
- **What it does:** Validates Markdown files with YAML front matter against official Euru schemas: `paper_trade`, `daily_journal`, `learning_report`, `scorecard`.
- **When:** Part of Friday Cycle preflight; can run standalone
- **Produces:** `SCHEMA_VALIDATION_REPORT_YYYY-MM-DD.md`

#### `euru_threshold_registry.py`
- **What it does:** Versioned governance threshold registry. Discovers threshold profiles in `00_GOVERNANCA/THRESHOLDS`, validates schema, resolves active profile by date/scope/profile_id, compares versions, generates changelogs, emits JSON.
- **When:** On demand / governance reviews
- **Reads:** `00_GOVERNANCA/THRESHOLDS/PROFILES/*.md`

### 3.5 Automation Registration Scripts (PowerShell)

#### `10_AUTOMACOES/register_euru_friday_cycle_task.ps1`
- **What it does:** Registers `Euru_Friday_Cycle` Windows Scheduled Task. Triggers: Weekly on Fridays at 20:30. Runs `euru_friday_cycle.py --root <EuruRoot>`.
- **Parameters:** `-EuruRoot` (mandatory), `-PythonExe`, `-TaskName`, `-TaskFolder`

#### `10_AUTOMACOES/register_euru_learning_preflight_task.ps1`
- **What it does:** Registers `Euru_Learning_Preflight` Windows Scheduled Task. Triggers: Weekly on Fridays at 20:30. Runs `euru_learning_preflight.py --root <EuruRoot> --write-report`.

#### `10_AUTOMACOES/register_euru_learning_task.ps1`
- **What it does:** Registers `Euru_Learning_Engine_Friday_2030` Windows Scheduled Task. Triggers: Weekly on Fridays at 20:30. Runs `euru_learning_engine.py --root <EuruRoot>`.

#### `euru_github_sync.ps1`
- **What it does:** Syncs repository to GitHub. Run on commits and weekly cycle.

#### `euru_schedule_setup.ps1`
- **What it does:** Initial setup script for scheduling tasks. Run once during system setup.

### 3.6 Other Scripts (in Euru_TOS/ working copy)

| Script | Purpose |
|---|---|
| `euru_execution.py` | Execution layer — future EXECUTE phase use |
| `euru_mac_analyst.py` | MAC Method (Movimento+Aceleração+Confirmação) analyst |
| `euru_quant_risk.py` | Quant/Risk Officer automation |
| `Euru_TOS/scripts/smoke_test.py` | Quick smoke test for pipeline health |

---

## 4. AGENT ROSTER — CORE PIPELINE

Pipeline execution order: Scout → Flow Analyst → News Sentinel → Score Engine → MAC Playbook → Quant/Risk Officer → Execution Orchestrator  
Overrides: DevOps Guardian (highest authority) → Journal Auditor (post-trade) → Quality Control (validates all outputs)

| # | Agent | Folder | Mission | Status | Automation |
|---|---|---|---|---|---|
| 01 | Scout | `04_AGENTES/01_SCOUT/` | Structural analysis — identifies NO_TRADE / WATCHLIST / SETUP on daily TF | ACTIVE | Fully automated via `euru_morning_scan.py` |
| 02 | Flow Analyst | `04_AGENTES/02_FLOW_ANALYST/` | Calculates RSI/MACD/OBV/ATR; returns CONFIRMS / CONTRADICTS / INCONCLUSIVE | ACTIVE | Fully automated via `euru_flow_analyst.py` |
| 03 | News Sentinel | `04_AGENTES/03_NEWS_SENTINEL/` | Scans CryptoPanic headlines; assigns LOW/MEDIUM/HIGH/CRITICAL severity | ACTIVE | Fully automated in morning scan |
| 04 | Quant/Risk Officer | `04_AGENTES/04_QUANT_RISK_OFFICER/` | Structured risk scoring — validates position sizing, ATR stops, exposure limits | DOCUMENTED | Manual via Claude Code (`euru_quant_risk.py` exists but semi-manual) |
| 05 | Execution Orchestrator | `04_AGENTES/05_EXECUTION_ORCHESTRATOR/` | Final go/no-go decision — consolidates all agent outputs | DOCUMENTED | Manual via Claude Code |
| 06 | DevOps Guardian | `04_AGENTES/06_DEVOPS_GUARDIAO/` | Infrastructure health — can force READ_ONLY on instability. Highest authority. | DOCUMENTED | Manual via Claude Code |
| 07 | Journal Auditor | `04_AGENTES/07_JOURNAL_AUDITOR/` | Creates daily journal entry from Scout/Asian reports + open positions | ACTIVE | Automated via `euru_journal_auditor.py` |
| 08 | Score Engine | `04_AGENTES/08_SCORE_ENGINE/` | Scores 0–35 across 7 criteria; tier classification (PREMIUM/BOA/MEDIA/IGNORE) | ACTIVE | Fully automated via `euru_score_engine.py` |
| 08† | Watchdog | `04_AGENTES/08_WATCHDOG/` | Continuous monitoring (PRESERVED REFERENCE — renumbered, responsibilities folded in) | SUPERSEDED | — |
| 09 | MAC Playbook Analyst | `04_AGENTES/09_MAC_PLAYBOOK_ANALYST/` | Validates MAC method (Movimento+Aceleração+Confirmação); 12-point playbook check | DOCUMENTED | Semi-manual (`euru_mac_analyst.py` exists) |
| 10/11 | Quality Control | `04_AGENTES/11_QUALITY_CONTROL/` | Validates all agent outputs against schema; must run after every pipeline cycle | DOCUMENTED | Manual via Claude Code |

**Conflict resolution authority (highest to lowest):**
1. DevOps Guardian (06)
2. Execution Orchestrator (05)
3. Quant/Risk Officer (04)
4. News Sentinel (03) — blocks on CRITICAL severity
5. MAC Playbook Analyst (09) — playbook-level veto
6. Flow Analyst (02)
7. Scout (01)
8. Score Engine (08) — scoring classification
9. Quality Control (11) — output validation

---

## 5. AGENT ROSTER — BREAKOUT INTELLIGENCE LAYER

**Status:** BUILT — awaiting Type 3 governance approval for SIMULATE activation.  
**Root path:** `04_AGENTES/BREAKOUT_LAYER/`  
**Note:** Mirror copies exist in `04_AGENTES/0X_<NAME>/` folders — BREAKOUT_LAYER is canonical.

| # | Agent | Folder | Mission | Status |
|---|---|---|---|---|
| BL-01 | Risk Guardian | `BREAKOUT_LAYER/01_RISK_GUARDIAN/` | Capital protection gate — 1% limit, 5% aggregate, 2x ATR, drawdown gate | PENDING ACTIVATION |
| BL-02 | Structure Hunter | `BREAKOUT_LAYER/02_STRUCTURE_HUNTER/` | S/R zones, compression, breakout-ready formations | PARTIALLY ACTIVE (in `euru_breakout_scanner.py`) |
| BL-03 | Breakout Confirmation | `BREAKOUT_LAYER/03_BREAKOUT_CONFIRMATION/` | Distinguishes real breakouts from fakeouts via candle/volume/follow-through | PARTIALLY ACTIVE (in `euru_breakout_scanner.py`) |
| BL-04 | Alert Radar | `BREAKOUT_LAYER/04_ALERT_RADAR/` | Event-driven entry point — receives, validates, normalizes, routes webhooks | PENDING ACTIVATION |
| BL-05 | Market Regime | `BREAKOUT_LAYER/05_MARKET_REGIME/` | Classifies trend/chop/compression environment; BTC alignment | PENDING ACTIVATION |
| BL-06 | Tactical Execution | `BREAKOUT_LAYER/06_TACTICAL_EXECUTION/` | Builds executable trade plans: entry, stop, T1/T2/T3, scale-in, partials | PENDING ACTIVATION |
| BL-07 | Compounding Governor | `BREAKOUT_LAYER/07_COMPOUNDING_GOVERNOR/` | Controls scaling — approves/freezes exposure increase based on performance | PENDING ACTIVATION |
| BL-08 | Journal Learning | `BREAKOUT_LAYER/08_JOURNAL_LEARNING/` | Stores all events and outcomes; feeds Friday Cycle and Learning Engine | PENDING ACTIVATION |
| BL-09 | Promise Auditor | `BREAKOUT_LAYER/09_PROMISE_AUDITOR/` | Audits score inflation, classification validity, bias, negative expectancy | PENDING ACTIVATION |

**Breakout Classification Bands:**

| Band | Score | Action |
|---|---|---|
| DISCARD | 0–39 | Log only, no routing |
| WATCH | 40–54 | Watchlist only |
| VALID | 55–69 | Route to Risk Guardian |
| STRONG | 70–84 | STRONG flag, scaled entry eligible |
| PREMIUM | 85–100 | PREMIUM flag, max risk eligible |

---

## 6. GOVERNANCE DOCUMENTS

### 6.1 Canonical Active Documents (use `_REVISADO` / `_OFFICIAL` versions)

| File | Rule Enforced |
|---|---|
| `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md` | Single source of truth for all status enums (NO_TRADE/WATCHLIST/SETUP, CONFIRMS/CONTRADICTS/INCONCLUSIVE, APPROVE/REJECT/REVIEW, etc.) |
| `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md` | Change management policy: Type 1 (prompt text, same-day self-approval), Type 2 (agent logic, 24h wait), Type 3 (phase transitions, 48h wait + formal checklist) |
| `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` | Master trading rules — full encoded REGRAS_MAE |
| `01_GOVERNANCA/REGRAS_MAE_REVISADO_SUMMARY.md` | Quick-reference digest of master rules |
| `01_GOVERNANCA/RESPONSABILIDADES_HUMANOS_REVISADO.md` | Human operator roles and responsibilities |
| `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` | Log of every strategic decision with date, status, operator, reason, approval |
| `01_GOVERNANCA/EURU_AGENT_DECISION_STANDARD_REVISADO.md` | Standard for how agents report decisions |
| `01_GOVERNANCA/EURU_OS_REVISADO.md` | Core OS design document |
| `01_GOVERNANCA/EURU_OS_1_REVISADO.md` | Extended OS specification |
| `01_GOVERNANCA/EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1.md` | Official governance rules master |
| `01_GOVERNANCA/EURU_GOVERNANCE_STANDARD_StatusDefinitions_OFFICIAL_v1.0.md` | Official status definitions |
| `01_GOVERNANCA/EURU_GOVERNANCE_POLICY_ChangeManagement_OFFICIAL_v1.0.md` | Official change management policy |
| `01_GOVERNANCA/EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0.md` | Operational state transitions |
| `01_GOVERNANCA/ADR_0001_EURU_CANONICAL_OPERATIONAL_STATE_READ_ONLY.md` | Architecture decision record: READ_ONLY state definition |
| `01_GOVERNANCA/ADR_0002_EURU_QUALITY_CONTROL_CANONICAL_FOLDER.md` | Architecture decision record: QC canonical folder (11_QUALITY_CONTROL) |

### 6.2 Schema Documents

| File | Rule Enforced |
|---|---|
| `00_GOVERNANCA/SCHEMAS/EURU_SCHEMA_TRADE_AND_JOURNAL.md` | YAML front matter schema for paper trades and journal entries |
| `00_GOVERNANCA/SCHEMAS/EURU_SCHEMA_LEARNING_REPORT_AND_SCORECARD.md` | Schema for learning reports and scorecards |
| `00_GOVERNANCA/SCHEMAS/EURU_SCHEMA_GOVERNANCE_THRESHOLDS.md` | Schema for threshold profiles |
| `00_GOVERNANCA/SCHEMAS/EURU_SETUP_TREND_CONTINUATION_OFFICIAL_v1.0.md` | Official setup type definition: Trend Continuation |

### 6.3 Risk & Execution

| File | Rule Enforced |
|---|---|
| `06_RISCO_E_EXECUCAO/EURU_RISK_FRAMEWORK_RiskMatrix_OFFICIAL_v1.0.md` | Risk matrix — all risk scenarios and mitigations |
| `06_RISCO_E_EXECUCAO/EURU_RISK_POLICY_ExitPolicy_OFFICIAL_v1.0.md` | Exit policy rules |
| `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt` | 12-point mandatory pre-trade checklist (all points must pass) |
| `07_OPERACAO/MODO_READ_ONLY.txt` / `EURU_OPERATIONS_POLICY_ReadOnlyMode_OFFICIAL_v1.0.md` | Permitted/prohibited actions in READ_ONLY phase |
| `07_OPERACAO/Politica_Saida_Completa_Euru.txt` | Full position close rules and triggers |

### 6.4 Breakout Layer Governance

| File | Rule Enforced |
|---|---|
| `04_AGENTES/BREAKOUT_LAYER/07_GOVERNANCE/BREAKOUT_GOVERNANCE_RULES.md` | 8 breakout governance rules |
| `04_AGENTES/BREAKOUT_LAYER/07_GOVERNANCE/BREAKOUT_AUDIT_RULES.md` | Audit triggers, responsibilities, required outputs |
| `04_AGENTES/BREAKOUT_LAYER/08_LEARNING/BREAKOUT_LEARNING_LOOP.md` | 4 output families, Friday Cycle requirements |

---

## 7. CURRENT SYSTEM STATE

### 7.1 Mode & Health

| Item | Value |
|---|---|
| System Mode | SIMULATE |
| Pipeline Health | HEALTHY |
| BTC Master Filter | Check latest SCOUT_REPORT for current state |
| Last Morning Scan | 2026-04-15 |
| Last Asian Scan | 2026-04-15 |
| Last Friday Cycle | 2026-04-13 |
| Incidents | None recorded |

### 7.2 Watchlist Summary

**TIER_1_PREMIUM (18 assets, daily scan active):**
BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, AVAXUSDT, DOTUSDT, LINKUSDT, ADAUSDT, XRPUSDT, MATICUSDT*, SUIUSDT, NEARUSDT, INJUSDT, ARBUSDT, OPUSDT, FETUSDT, TAOUSDT, RENDERUSDT  
*MATICUSDT replaced by WLDUSDT in morning/asian scans as of 2026-04-15

**TIER_2_MONITOR (10 assets):**
DYDXUSDT, EIGENUSDT, PENDLEUSDT, KASUSDT, QNTUSDT, GMXUSDT, IMXUSDT, AXSUSDT, STRKUSDT, RONINUSDT

**TIER_3_BULL_CYCLE (5 assets, review 2027+):**
ORDIUSDT, MOVEUSDT, TAIKOUSDT, MORPHOUSDT, DRIFTUSDT

**LISTA_PROIBIDA (9 assets, permanent ban):**
USELESSUSDT, GIGGLEUSDT, JELLYJELLYUSDT, DUSDT, HUSDT, BUSDT, QUSDT, 4USDT, TSLAUSDT

### 7.3 Open Paper Trades (as of 2026-04-15)

| Trade | Asset | Entry | Stop | T1 | T2 | Expires | Status |
|---|---|---|---|---|---|---|---|
| PT001 | AVAXUSDT | 9.22 | 8.501 | 10.658 | 11.377 | 2026-04-15 | OPEN (time stop today) |
| PT002 | NEARUSDT | 1.34 | 1.2272 | 1.5656 | 1.6784 | 2026-04-15 | OPEN (time stop today) |
| PT003 | ARBUSDT | 0.1100 | 0.0980 | 0.1340 | 0.1460 | 2026-04-18 | OPEN |

**Portfolio exposure:** 33.88% (PT001: 12.82% + PT002: 11.89% + PT003: 9.17%)  
**Combined max risk:** 3.00 USDT (3% of 100 USDT reference capital)  
**NOTE:** PT001 and PT002 time stops expire TODAY (2026-04-15). Evaluate for close or extension.

### 7.4 API Key Configuration

Three key pairs (template only — real keys in `.env` outside repo):
- `BINANCE_RESEARCH_*` — market data, read-only
- `BINANCE_USERDATA_*` — account data, read-only
- `BINANCE_TRADE_*` — EXECUTION_BLOCKED in current SIMULATE phase

---

## 8. AUTOMATIONS & SCHEDULES

### 8.1 Scheduled Tasks (Windows Task Scheduler)

| Task | Script | Schedule | Output |
|---|---|---|---|
| Morning Scan | `euru_morning_scan.py` | Daily (manual run or scheduled) | `SCOUT_REPORT_YYYY-MM-DD.md` |
| Asian Session Scan | `euru_asian_scan.py` | Daily at 00:00 UTC | `ASIAN_REPORT_YYYY-MM-DD.md` |
| Friday Cycle | `euru_friday_cycle.py` | Fridays at 20:30 local | `FRIDAY_CYCLE_REPORT_*.md` |
| Learning Engine | `euru_learning_engine.py` | Fridays at 20:30 (part of Friday Cycle) | `LEARNING_REPORT_YYYY-MM-DD.md` |
| Learning Preflight | `euru_learning_preflight.py` | Fridays at 20:30 (part of Friday Cycle) | `LEARNING_PREFLIGHT_REPORT_*.md` |

### 8.2 Registration Commands

To register scheduled tasks (run once, requires admin):
```powershell
# Friday Cycle (full orchestrator — preferred)
.\10_AUTOMACOES\register_euru_friday_cycle_task.ps1 -EuruRoot "C:\Users\andre\Desktop\EURO MAIN"

# Learning Preflight only
.\10_AUTOMACOES\register_euru_learning_preflight_task.ps1 -EuruRoot "C:\Users\andre\Desktop\EURO MAIN"

# Learning Engine only
.\10_AUTOMACOES\register_euru_learning_task.ps1 -EuruRoot "C:\Users\andre\Desktop\EURO MAIN"
```

### 8.3 Manual Daily Workflow (SOP_DIARIO_v2)

```
Block 1 (5 min):  Check PC + internet; verify Asian scan ran at 00:00 UTC
Block 2 (10 min): python euru_morning_scan.py
Block 3 (10 min): Read SCOUT_REPORT — BTC filter, leaderboard, RSI/MACD/OBV per SETUP
Block 4 (5 min):  Operational decision — complete CHECKLIST_PRE_TRADE_v2.txt if entering
Block 5 (5 min):  Verify saves; register incidents; update changelog if changed
```

---

## 9. STRATEGIC DECISIONS LOG

Complete chronological record from `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md`:

### March 27, 2026 — System Creation
- Created Euru OS in READ_ONLY mode
- Eliminated pre-existing API keys (AndreMarcal, AndreGottardi)
- Created three new API keys: `euru_research_key`, `euru_userdata_key`, `euru_trade_key` (trade key execution blocked until phase transition)

### March 28, 2026 — Folder Reorganization
- Reorganized folder structure to current layout

### March 29, 2026 — SOP Rewrite
- Approved rewrite of SOP_DIARIO as 30-minute checklist (current SOP_DIARIO_v2)

### March 30 – April 2, 2026 — Strategic Framework
- Declared 5-phase automation strategy (READ_ONLY manual → READ_ONLY automated → SIMULATE manual → SIMULATE automated → EXECUTE)
- Identified Paperclip platform for agent orchestration (post-Week 8)
- Studying "Protocolo Aguiar" — 10-module framework including: trend filters, 5/5/90 capital architecture, risk scaling, security daemons, volume confirmation, recovery triggers, lock protocols, harvest triggers
- Referenced Bruno Aguiar and Claude Code materials

### April 2, 2026 — Alt-coin & MAC Method
- Researched alt-coin watchlist (top 50 categorized)
- Approved MAC Method (Movimento + Aceleração + Confirmação) for Asian sessions
- Approved 50/25/15/10 capital distribution: Core (50%), Growth (25%), Asymmetric (15%), Speculative (10%)
- Mapped "Dream Team" — 11 specialized agent profiles

### April 3, 2026 — Week 4 Expansion
- Expanded morning scan to 20 assets
- Integrated News Sentinel with CoinTelegraph/CryptoPanic
- Coded REGRAS_MAE in YAML
- Created CHECKLIST_PRE_TRADE.md
- Divided watchlist into 4 tiers
- Validated Dream Team
- Documented Binance Perpetual assets

### April 3, 2026 — Flow Analyst Indicators
- RSI 14 periods, MACD 12/26/9, OBV, ATR 14
- Position sizing formula: `capital × 1% / (ATR × 1.5)`
- Pipeline: Scout → Flow Analyst → News Sentinel → Quant/Risk → Execution

### April 6, 2026 — Type 3 Decision: SIMULATE Phase
- Proposed transition to SIMULATE phase
- 48-hour governance period: 2026-04-06 to 2026-04-08
- Criteria verified: 6+ weeks infrastructure, 10 agents documented, Score Engine calibrated, journal consistent, CHECKLIST_PRE_TRADE v2 ready, REGRAS_MAE_REVISADO.yaml coded
- Criteria pending: Quant/Risk, MAC Analyst, Execution Orchestrator not fully automated
- Decision: Activate SIMULATE in SEMI-MANUAL mode (manual agents via Claude Code)

### April 8, 2026 — SIMULATE Activation
- Formal activation after 48h governance period (approved 2026-04-06)
- First paper trades executed simultaneously:
  - PAPER_TRADE_001: AVAXUSDT, entry 9.22, stop 8.501, T1 10.658
  - PAPER_TRADE_002: NEARUSDT, entry 1.34, stop 1.2272, T1 1.5656
  - Combined exposure: 24.71%, risk: 2% total (1% per trade)
- System status set to: SIMULATE — HEALTHY

### April 11, 2026 — Third Paper Trade
- PAPER_TRADE_003: ARBUSDT, entry 0.1100, stop 0.0980, T1 0.1340
- Score 27/35 (highest of open positions), momentum continuation setup
- Combined exposure: 33.88% across three trades
- Combined max risk: 3.00 USDT (3%)

### April 15, 2026 — Breakout Intelligence Layer Integration
- 9 new Breakout Layer agents integrated (BL-01 through BL-09)
- 27 agent files created (PROMPT + BRIEFING + OUTPUT_FORMAT per agent)
- 8 technical infrastructure files (schema, weights, scoring, flow, governance, learning, handoff)
- `euru_breakout_scanner.py` created and integrated with morning scan
- CLAUDE.md updated with Breakout Layer section
- EURU_AGENT_MAP.md created
- Total agents: 20 (11 core + 9 breakout)
- MATICUSDT replaced by WLDUSDT in both morning and Asian scans
- System status: SIMULATE — HEALTHY
- Breakout Layer status: BUILT, awaiting Type 3 governance for SIMULATE activation

---

## 10. PAPER TRADES STATUS

### PAPER_TRADE_001 — AVAXUSDT

| Field | Value |
|---|---|
| Trade ID | PAPER_TRADE_001 |
| Asset | AVAXUSDT |
| Identified | 2026-04-06 04:47 UTC |
| Entered | 2026-04-08 16:23 UTC |
| Entry Price | 9.22 USDT |
| Stop Loss | 8.501 (ATR×1.5 below entry) |
| Target 1 | 10.658 (1:2 RR) |
| Target 2 | 11.377 (1:3 RR) |
| Fib 0.382 | 10.118 |
| Fib 0.618 | 10.402 |
| Fib 1.000 | 10.860 |
| Position Size | 1.39 AVAX |
| Capital Deployed | 12.82% |
| Max Risk | 1 USDT (1%) |
| Time Stop | 2026-04-15 (TODAY — evaluate) |
| Score at Entry | 25/35 BOA |
| Scout State | WATCHLIST (pulled back from SETUP) |
| Flow | CONFIRMS (RSI 50.62, MACD bullish, OBV rising) |
| MAC | PLAYBOOK_OK (12/12 clean breakout) |
| Status | **OPEN — TIME STOP EXPIRES TODAY** |

### PAPER_TRADE_002 — NEARUSDT

| Field | Value |
|---|---|
| Trade ID | PAPER_TRADE_002 |
| Asset | NEARUSDT |
| Identified | 2026-04-08 16:23 UTC |
| Entered | 2026-04-08 16:23 UTC |
| Entry Price | 1.34 USDT |
| Stop Loss | 1.2272 (ATR×1.5 below entry) |
| Target 1 | 1.5656 (1:2 RR) |
| Target 2 | 1.6784 (1:3 RR) |
| Fib 0.382 | 1.4164 |
| Fib 0.618 | 1.4636 |
| Fib 1.000 | 1.5400 |
| Position Size | 8.87 NEAR |
| Capital Deployed | 11.89% |
| Max Risk | 1 USDT (1%) |
| Time Stop | 2026-04-15 (TODAY — evaluate) |
| Score at Entry | 25/35 BOA |
| Scout State | SETUP — AT_WEEKLY_HIGH |
| Flow | CONFIRMS (RSI 61.57, MACD bullish, OBV rising) |
| MAC | PLAYBOOK_OK (12/12 clean breakout) |
| Risk Note | Entry at exact resistance (1.34 = R). Must prove breakout. |
| Status | **OPEN — TIME STOP EXPIRES TODAY** |

### PAPER_TRADE_003 — ARBUSDT

| Field | Value |
|---|---|
| Trade ID | PAPER_TRADE_003 |
| Asset | ARBUSDT |
| Identified | 2026-04-10 ~00:00 UTC |
| Entered | 2026-04-11 07:32 UTC |
| Entry Price | 0.1100 USDT |
| Stop Loss | 0.0980 (ATR×1.5 below entry) |
| Target 1 | 0.1340 (1:2 RR) |
| Target 2 | 0.1460 (1:3 RR) |
| Fib 0.382 | 0.1315 |
| Fib 0.618 | 0.1385 |
| Fib 1.000 | 0.1500 |
| Position Size | 83.33 ARB |
| Capital Deployed | 9.17% |
| Max Risk | 1 USDT (1%) |
| Time Stop | 2026-04-18 |
| Score at Entry | 27/35 BOA (highest of open positions) |
| Scout State | SETUP — ABOVE_7D_AVG |
| Flow | CONFIRMS (RSI 68.05 elevated, MACD bullish, OBV rising, 1.8× avg volume) |
| MAC | PLAYBOOK_OK (12/12 Momentum Continuation CLEAN) |
| Risk Note | RSI 68.05 approaching 70 — monitor for overbought. Alert at RSI >75 → reduce 50%. |
| Status | **OPEN** |

### Portfolio Summary

| Item | Value |
|---|---|
| Total Open Trades | 3 |
| Combined Capital Deployed | 33.88% |
| Combined Max Loss | 3.00 USDT (3.0%) |
| Trades Expiring Today | PT001 (AVAX), PT002 (NEAR) |
| Next Expiry | PT003 (ARB) — 2026-04-18 |

---

## 11. GIT COMMIT HISTORY

| Commit | Date | Summary |
|---|---|---|
| `48a72c9` | 2026-04-15 | 5 files updated |
| `e3d59fd` | 2026-04-15 | `euru_breakout_scanner.py` integrated with morning scan |
| `91f88d7` | 2026-04-15 | MATICUSDT replaced by WLDUSDT in both scans |
| `a0ca68c` | 2026-04-15 | Breakout Intelligence Layer — 36 files |
| `16732dd` | 2026-04-14 | 9 files updated |
| `f2f0216` | 2026-04-14 | 4 files updated |
| `c7e7858` | 2026-04-13 | scorecard engine multidimensional + friday cycle v1.1 |
| `95aeb63` | 2026-04-12 | All 11 agents OFFICIAL — SIMULATE criterion 2 met |
| `7fb1133` | 2026-04-12 | Journal auditor installed and scheduled — AGT-07 fully automated |
| `9d8c272` | 2026-04-12 | First real Friday Cycle — LEARNING_REPORT + SCORECARD generated |
| `d6af2fb` | 2026-04-12 | 22 legacy files migrated to YAML schema — validator 22/22 PASS |
| `dfe5792` | 2026-04-12 | Friday Cycle + handoff bundle integrated |
| `d0b4f81` | 2026-04-11 | 176 files updated (major migration/expansion) |
| `64bb3f2` | 2026-04-11 | 4 files updated |
| `a2af572` | 2026-04-11 | Governance normalization complete — Registry v1.3 |
| `2c4141a` | 2026-04-10 | 3 files updated |
| `213cb3d` | 2026-04-09 | 3 files updated |
| `0e6daed` | 2026-04-08 | 9 files updated (SIMULATE activation + first trades) |
| `d2ef2ad` | 2026-04-07 | 2 files updated |
| `06407d5` | 2026-04-06 | 4 files updated (Type 3 governance initiated) |
| `3b0ada5` | 2026-04-05 | 3 files updated |
| `859c6eb` | (base) | Week 6 complete. 10 agents, full pipeline, all governance docs. |

**Total commits:** 22  
**Active branch:** main  
**Untracked:** `Euru_TOSOld_02026-04-10/`, `Euru_TOS_GITHUB/`

---

## 12. KNOWN ISSUES & PENDING ITEMS

### 12.1 Immediate (Today — 2026-04-15)

| # | Item | Action Required |
|---|---|---|
| URGENT | PT001 AVAXUSDT — time stop expires TODAY | Evaluate current price vs entry 9.22. If still open and no target hit: close per time stop rule or extend with governance note. |
| URGENT | PT002 NEARUSDT — time stop expires TODAY | Evaluate current price vs entry 1.34. If still open: close per time stop rule or extend with governance note. |
| PENDING | MATICUSDT still in WATCHLIST_OFICIAL.md but replaced by WLDUSDT in scans | Update WATCHLIST_OFICIAL.md to reflect WLDUSDT in TIER_1 (Type 1 change) |

### 12.2 Week 6 Roadmap (Pending Type 3 Governance)

| # | Item | Gate |
|---|---|---|
| 1 | Breakout Intelligence Layer SIMULATE activation | Type 3 approval (48h wait + formal checklist) |
| 2 | Quant/Risk Officer (04) full automation | Type 2 approval (24h wait) |
| 3 | MAC Playbook Analyst (09) automation | Type 2 approval |
| 4 | Alert Radar (BL-04) webhook integration | Type 3 approval |
| 5 | Paperclip evaluation — back-test READ_ONLY observations | Internal planning |
| 6 | EXECUTE phase transition criteria definition | Type 3 approval when ready |

### 12.3 Structural Notes

| # | Item | Note |
|---|---|---|
| 1 | Duplicate agent folders | Breakout Layer agents appear both in `04_AGENTES/BREAKOUT_LAYER/` (canonical) and as `04_AGENTES/0X_<NAME>/` (legacy mirrors). Canonical = BREAKOUT_LAYER. |
| 2 | Multiple working directories | Scripts exist in both root and `Euru_TOS/`. Root copies are canonical as of Week 6. Euru_TOS/ copies are kept for compatibility. |
| 3 | Backup folders untracked | `Euru_TOSOld_02026-04-10/` and `Euru_TOS_GITHUB/` are untracked in git. |
| 4 | PROMPT_REVISADO.md missing for AGT-06 | `04_AGENTES/06_DEVOPS_GUARDIAO/` has no `PROMPT_REVISADO.md` (only BRIEFING_FINAL and OUTPUT_FORMAT_FINAL). |
| 5 | Quality Control folder numbering | Agent is listed as Agent 10 in docs but folder is `11_QUALITY_CONTROL`. ADR_0002 documents this decision. |
| 6 | Incident log clean | `09_LOGS_E_INCIDENTES/INCIDENTES.md` has no incidents recorded. Infrastructure has been stable. |
| 7 | docxwork/ | Contains Node.js tooling for DOCX file processing. Not part of trading pipeline. |

### 12.4 Governance Notes

| # | Item | Note |
|---|---|---|
| 1 | Solo operation protocol | Risk/Product Owner and Automation Engineer decisions in separate sessions. Critical changes require 24h cooling-off. |
| 2 | Next Friday Cycle | 2026-04-17 or 2026-04-18 — will run schema validation, learning engine, scorecards for W16. |
| 3 | SIMULATE criteria | Two criteria confirmed (11 agents OFFICIAL, Friday Cycle operational). Criteria for EXECUTE not yet formally defined. |

---

## QUICK REFERENCE

### Daily Commands
```bash
# Run from: C:\Users\andre\Desktop\EURO MAIN
python euru_morning_scan.py                  # Morning scan (manual)
python euru_asian_scan.py                    # Asian scan (00:00 UTC)
python euru_breakout_scanner.py              # Breakout scan standalone
python euru_friday_cycle.py --root .         # Friday cycle (manual)
python euru_journal_auditor.py               # Journal entry for today
python euru_schema_validator.py --root .     # Validate schemas
```

### Key File Paths
```
Canonical watchlist:      08_DADOS_E_JOURNAL/WATCHLISTS/EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2.md
Daily SOP:               07_OPERACAO/SOP_DIARIO_v2.txt
Pre-trade checklist:     07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt
Decision log:            01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md
Master rules:            01_GOVERNANCA/REGRAS_MAE_REVISADO.md
Status enums:            01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md
Change management:       01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md
Open trades:             08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_00*.md
Latest scout report:     08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_2026-04-15.md
```

### Status Enums (exact values — no free-form)
```
Scout structural:    NO_TRADE | WATCHLIST | SETUP
Flow Analyst:        CONFIRMS | CONTRADICTS | INCONCLUSIVE
Risk:                APPROVE | REJECT | REVIEW
Execution:           EXECUTION_ALLOWED | EXECUTION_BLOCKED | MANUAL_REVIEW_REQUIRED
Infrastructure:      HEALTHY | DEGRADED | CRITICAL
News severity:       LOW | MEDIUM | HIGH | CRITICAL
Score tiers:         PREMIUM (28-35) | BOA (22-27) | MEDIA (16-21) | IGNORE (0-15)
Breakout bands:      DISCARD (0-39) | WATCH (40-54) | VALID (55-69) | STRONG (70-84) | PREMIUM (85-100)
```

---

*Document generated by Claude Code audit on 2026-04-15. Next scheduled update: 2026-04-17 (post-Friday Cycle).*

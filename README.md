# EURU TOS MAIN

Canonical clean repository for Euru OS from 2026-04-25 onward.

Euru OS is a governed trading decision system for Binance perpetual futures. It is not an autonomous trading bot. Its purpose is to transform discretionary trading into a structured, auditable, measurable, and continuously improving operating system.

## Current Phase

- Phase: `SIMULATE`
- Capital mode: paper/simulated only
- Real capital: not active
- Primary objective: prove 5-8% average monthly performance in SIMULATE with valid data, clean governance, and weekly learning
- Execute objective: after gates are met, start with 100 EUR and attempt 1000 EUR in 12 months

## Source Of Truth

This folder, `C:\Users\andre\Desktop\EURU TOS MAIN`, is the new canonical working repository.

Older folders such as `EURO MAIN`, `Euru_TOS`, `Euru_TOSOld_*`, migrated copies, zip extracts, and PDFs are historical references only unless explicitly promoted through governance.

## Repository Map

The folder names intentionally preserve the operational paths used by the existing scripts.

| Folder | Purpose |
|---|---|
| `00_MASTER` | Current state, index, roadmap, session opening context |
| `00_GOVERNANCA` | Schemas, threshold profiles, Friday Cycle definition |
| `01_GOVERNANCA` | Rules, policies, ADRs, decision log |
| `02_BINANCE_SETUP` | Exchange setup reference |
| `03_ARQUITETURA` | Architecture and pipeline diagrams |
| `04_AGENTES` | Core agents and Breakout Layer agent definitions |
| `05_PROMPTS` | Operational prompts |
| `06_RISCO_E_EXECUCAO` | Risk matrix, exit policy, execution rules |
| `07_OPERACAO` | SOPs, simulate setup, runbooks, checklists |
| `08_DADOS_E_JOURNAL` | Trades, daily journals, watchlists, scan reports, scorecards |
| `09_LOGS_E_INCIDENTES` | Incident logs |
| `10_AUTOMACOES` | Scheduled task helper scripts |
| `11_CONFIG_PLACEHOLDERS` | Configuration templates |
| `docs` | Public positioning/use-case/value documents |
| `99_ARCHIVE` | Historical snapshots and reference material only |

## Immediate Consolidation Rule

For the next phase, avoid building new trading features until the core loop is clean:

```text
Scan -> Trade/Journals -> Schema Validation -> Friday Cycle -> Learning Report -> Governance Review
```

The highest priority is to unblock schema validation and make the weekly learning loop reliable.


# EURU Consolidation Roadmap

Version: 1.0  
Date: 2026-04-25

## Purpose

This roadmap exists to keep Euru from growing faster than its data, documentation, and governance can support.

The goal of the next phase is not to add complexity. The goal is to make the existing system internally consistent and measurable.

## Phase 1 — Repository Clean Base

Status: in progress

Deliverables:

- New canonical folder: `EURU TOS MAIN`.
- Historical mirrors excluded from active use.
- Clean folder map using existing operational paths.
- New `README.md`, `CLAUDE.md`, operational state, source-of-truth, and index files.

Exit criteria:

- Future sessions can start from `EURU TOS MAIN` without needing old folder context.

## Phase 2 — Schema And Friday Cycle Recovery

Status: next

Deliverables:

- All generated scan reports include valid front matter.
- `PAPER_TRADE_004.md` has required body headings while remaining excluded from performance stats.
- Schema validator and Daily Audit agree on file scope and severity.
- Friday Cycle completes without schema block.

Exit criteria:

- Latest Friday Cycle status is not `CLOSED_BLOCKED`.
- Latest schema validation has zero critical invalid files.

## Phase 3 — Metrics Reconciliation

Status: pending

Deliverables:

- Canonical trade metrics table.
- Official capital curve.
- Clear inclusion/exclusion policy for governance-breach trades.
- Definition of monthly 5-8% benchmark.

Exit criteria:

- Weekly Audit and Learning Report use the same official performance numbers.

## Phase 4 — Trade Metrics Calculator

Status: pending

Deliverables:

- Read-only script for closed trade statistics.
- Metrics by asset, setup type, BTC regime, news severity, score band, and exit reason.
- Integration into Weekly Audit.

Exit criteria:

- Weekly Audit reports expectancy, realized RR, win rate, drawdown, and distance to North Star.

## Phase 5 — Controlled Expansion Review

Status: blocked until phases 1-4 are complete

Candidate expansions:

- Breakout Intelligence Layer activation.
- SHORT trade support.
- Historical backtesting/replay.
- Paperclip orchestration.
- Additional specialist agents.

Rule:

No expansion should be activated while the core loop is blocked or metrics are inconsistent.


# CLAUDE.md

This file is the operating brief for AI/code sessions working inside `EURU TOS MAIN`.

## Non-Negotiable Context

Euru OS is in `SIMULATE`, not `READ_ONLY` and not `EXECUTE`.

No real capital is deployed. No AI may create or approve trades outside the validated Euru pipeline and explicit human operator approval.

The current repository root is:

```text
C:\Users\andre\Desktop\EURU TOS MAIN
```

Do not treat `C:\Users\andre\Desktop\EURO MAIN`, `Euru_TOS`, `Euru_TOSOld_*`, migrated folders, zip extracts, or PDF snapshots as active repositories. They are historical references.

## Current North Star

Operational metric:

```text
Prove that Euru generates 5-8% average monthly performance in SIMULATE.
In EXECUTE, with 100 EUR initial capital, reach 1000 EUR in 12 months.
```

The 1,000,000 EUR by 2029 target is a personal aspiration of the operator, not an operational metric of the system.

## Current Priority

The project is in a consolidation phase. The priority is alignment, not expansion.

Do this first:

1. Keep one canonical source of truth.
2. Fix schema validation issues.
3. Unblock Friday Cycle.
4. Restore Learning Engine reliability.
5. Reconcile official trade metrics.
6. Only then consider new agents, Breakout activation, SHORT support, Paperclip, or ML.

## Critical Known Issues

- Friday Cycle has been blocked by schema validation.
- Some generated reports lacked valid YAML front matter in the previous workspace.
- `PAPER_TRADE_004.md` was a governance-breach trade and may need retrospective template normalization while remaining excluded from official performance statistics.
- Older docs conflict on `READ_ONLY` vs `SIMULATE`, 10 vs 20 agents, score `0-100` vs `0-35`, and news severity gates.

## Governance

Change classes:

- Type 1: trivial or documentation-only, self-approval.
- Type 2: moderate system or agent logic changes, 24h cooling-off.
- Type 3: phase transitions, risk parameters, strategic metrics, 48h cooling-off.

All strategic decisions must be recorded in `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md`.

## Working Rule For AI Sessions

When uncertain, preserve capital, data integrity, and governance.

No trade, no phase change, no risk change, and no schema relaxation should be treated as valid unless the relevant governance gate has been met.


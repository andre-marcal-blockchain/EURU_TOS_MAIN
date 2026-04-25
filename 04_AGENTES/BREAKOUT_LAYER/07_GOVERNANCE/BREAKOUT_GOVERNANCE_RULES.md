# BREAKOUT_GOVERNANCE_RULES.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Module: 07_GOVERNANCE
# Created: 2026-04-15 | Status: ACTIVE

---

## PURPOSE

This document defines the 8 governance rules for the Euru Breakout Intelligence Layer. These rules govern how changes are approved, who may authorize what, how phase transitions work, and what minimum outputs are required from each governance checkpoint.

These rules supplement (and do not replace) the master governance framework at `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md`. Where conflict exists, the master framework takes precedence.

---

## GOVERNANCE RULES

---

### RULE 1 — LAYER PHASE COMPLIANCE

**The Breakout Intelligence Layer inherits the system phase of the parent Euru OS.**

The system phase (`READ_ONLY`, `SIMULATE`, `EXECUTE`) is defined in `11_CONFIG_PLACEHOLDERS/.env.example` and applies to the entire pipeline including this layer. The Breakout Layer does not have its own phase setting.

**Implications:**
- In `READ_ONLY`: All alerts route as OBSERVATION_ONLY. No trade plans are produced. All pipeline steps log but do not execute.
- In `SIMULATE`: Full pipeline activates. Trade plans are produced and logged. No real capital is deployed. All compounding decisions are simulated.
- In `EXECUTE`: Full pipeline activates with real capital. All hard constraints apply at maximum strictness.

**Violation:** Attempting to activate execution logic while system phase is READ_ONLY is logged as a `MODE_MISMATCH` incident regardless of how the mismatch was introduced.

---

### RULE 2 — WEIGHT CHANGES REQUIRE TYPE 2 APPROVAL

**Any change to `05_SCORING/configs/breakout_weights_v1.yaml` requires Type 2 governance approval.**

Type 2 process:
- 24-hour waiting period between proposal and implementation
- Approval must be granted in a separate working session (not the session where the proposal was made)
- Change must be documented in `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md`
- Old weight file must be archived (suffixed with `_BACKUP_<date>`) before new weights go live

**Rationale:** Weight changes alter scoring outputs and therefore routing decisions. Even small weight adjustments can shift setups between classification bands and change which trades are approved.

---

### RULE 3 — BAND THRESHOLD CHANGES REQUIRE TYPE 3 APPROVAL

**Any change to the classification band boundaries in `euru_breakout_feature_schema.yaml` requires Type 3 governance approval.**

Type 3 process:
- 48-hour waiting period
- Formal checklist completion (see `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md`)
- Human sign-off from both Risk/Product Owner and Automation Engineer roles (in separate sessions)
- Documentation in `DECISOES_ESTRATEGICAS_REVISADO.md` with full rationale

**Rationale:** Classification band thresholds directly determine which setups reach Risk Guardian. Shifting the VALID floor from 55 to 50 increases the volume of setups entering the execution path — this is a risk parameter change, not a tuning change.

---

### RULE 4 — LISTA_PROIBIDA IS ABSOLUTE

**No agent, operator, or configuration can override a LISTA_PROIBIDA rejection.**

Assets on LISTA_PROIBIDA are permanently blocked from routing regardless of signal quality, classification band, or operator instruction. LISTA_PROIBIDA matches are logged as security events in addition to REJECTED routing events.

**Adding an asset to LISTA_PROIBIDA:** Can be done same-day by any operator with a documented reason. Takes effect immediately.

**Removing an asset from LISTA_PROIBIDA:** Requires Type 2 approval (24h wait + separate session). Removal must include a documented rationale.

---

### RULE 5 — HARD CONSTRAINTS ARE NON-NEGOTIABLE

**The following hard constraints defined in agent PROMPT files and weight configs cannot be relaxed by operator instruction, confidence scores, or upstream agent outputs:**

| Constraint | Agent | Override Possible |
|---|---|---|
| Per-trade risk ≤ 1% | Risk Guardian | NO |
| Aggregate risk ≤ 5% | Risk Guardian | NO |
| Liquidation distance ≥ 2x ATR | Risk Guardian | NO |
| Volume ratio ≥ 0.8 for confirmation | Breakout Confirmation | NO |
| Wick rejection ≤ 40% of body | Breakout Confirmation | NO |
| Close must exceed zone boundary | Breakout Confirmation | NO |
| Stop ≥ 1x ATR from entry | Tactical Execution | NO |
| R:R ≥ 2:1 at T1 | Tactical Execution | NO |
| Zone requires ≥ 2 touches | Structure Hunter | NO |
| Compression requires ≥ 3 candles | Structure Hunter | NO |
| LISTA_PROIBIDA = absolute reject | Alert Radar | NO |

Changes to hard constraints require Type 3 approval and must be reflected in agent PROMPT files, schema, and this governance document simultaneously.

---

### RULE 6 — SOLO OPERATION PROTOCOL APPLIES TO THIS LAYER

**When operating without a second human operator, the solo operation protocol from `01_GOVERNANCA/RESPONSABILIDADES_HUMANOS_REVISADO.md` applies.**

Specifically:
- Risk/Product Owner decisions (e.g., approving a Type 2 weight change) and Automation Engineer decisions (e.g., implementing the change in the config file) must be made in separate working sessions.
- Critical changes (Type 3) require a 24-hour cooling-off period between the decision to make the change and the implementation session.
- Solo operators must document the decision rationale in `DECISOES_ESTRATEGICAS_REVISADO.md` before beginning any change implementation.

---

### RULE 7 — PROMISE AUDITOR FINDINGS REQUIRE FORMAL RESPONSE

**Any finding from Promise Auditor flagged as severity HIGH or CRITICAL must receive a documented response in `DECISOES_ESTRATEGICAS_REVISADO.md` within one Friday Cycle (7 days).**

Response options:
- `ACCEPTED` — finding acknowledged, corrective action documented with timeline
- `DISPUTED` — operator disputes the finding with counter-evidence and reasoning
- `DEFERRED` — finding noted, action delayed with documented reason and new review date

Unresponded HIGH/CRITICAL findings escalate to `REPEAT_FINDING` status in the next audit cycle and trigger a mandatory governance checkpoint.

---

### RULE 8 — FRIDAY CYCLE IS MANDATORY

**The Friday Cycle review (as defined in `07_OPERACAO/SOP_SEMANAL.txt`) must run every week regardless of trade count.**

A zero-trade week is not a reason to skip the Friday Cycle. A zero-trade week produces a Friday Cycle with:
- Zero-trade summary from Journal Learning
- Compounding Governor posture review (even if unchanged)
- Any pending Promise Auditor findings
- Pipeline health check (Alert Radar routing stats, system mode confirmation)

Skipping the Friday Cycle must be documented as a governance incident in `09_LOGS_E_INCIDENTES/INCIDENTES.md`.

---

## MINIMUM GOVERNANCE OUTPUTS

The following outputs must be produced at each governance checkpoint:

### Per-Trade Checkpoint (automated, each cycle)
- Journal Learning trade record (TRADE_ENTRY or NON_EXECUTION)
- Compounding Governor scaling posture report
- Risk Guardian verdict record

### Weekly Checkpoint (Friday Cycle, human)
- Journal Learning weekly summary
- Compounding Governor weekly review
- Promise Auditor audit report (or deferred note if < 10 trades)
- Pipeline health metrics (alert volume, routing rate, fakeout rate)
- Classification band performance table (win rate and expectancy by band)

### Change Approval Checkpoint (per Type 2 or Type 3 event)
- Entry in `DECISOES_ESTRATEGICAS_REVISADO.md` with: date, change description, change type, operator, rationale, approval status
- Archive of any file being modified (suffixed `_BACKUP_<date>`)
- Post-change validation note (confirm system behavior matches expectation after change)

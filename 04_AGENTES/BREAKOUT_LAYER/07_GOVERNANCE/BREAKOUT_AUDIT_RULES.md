# BREAKOUT_AUDIT_RULES.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Module: 07_GOVERNANCE
# Created: 2026-04-15 | Status: ACTIVE

---

## PURPOSE

This document defines the audit framework for the Euru Breakout Intelligence Layer. It specifies when audits are triggered, what the Promise Auditor is responsible for evaluating, and what outputs are required from each audit cycle. The audit system ensures that the pipeline's self-assessments (scores, classifications, confidence levels) remain honest and validated against actual outcomes.

---

## AUDIT TRIGGERS

Audits are activated by three trigger types. All three produce the same audit report format.

---

### TRIGGER TYPE 1 — FRIDAY CYCLE (Scheduled)

**Frequency:** Weekly, every Friday, as part of `07_OPERACAO/SOP_SEMANAL.txt`.
**Minimum data requirement:** ≥ 1 trade or non-execution event recorded since last audit.
**If no events occurred:** Produce a zero-event audit report noting the gap. Do not skip — gaps are data.

**Standard Friday Cycle audit scope:**
- All trades and non-executions from the past 7 days
- Expectancy trend (current week vs. prior 3 weeks if available)
- Score band performance table
- PREMIUM classification validity
- Compounding Governor accuracy (if any scaling events occurred)
- Any unresolved findings from prior audit (REPEAT_FINDING check)

---

### TRIGGER TYPE 2 — THRESHOLD BREACH (Automatic)

**Conditions that trigger an immediate unscheduled audit:**

| Condition | Threshold | Description |
|---|---|---|
| Fakeout rate spike | > 50% in a 10-signal window | More than half of recent routed signals are fakeouts — signal quality may have degraded |
| Expectancy collapse | < 0 in current week (minimum 5 trades) | Current-week expectancy has gone negative |
| PREMIUM band underperformance | PREMIUM win rate < STANDARD win rate for ≥ 5 trades each | Classification has inverted — PREMIUM no longer predicts better outcomes |
| Consecutive losses | ≥ 5 in a row | Streak warrants immediate performance context review |
| Score drift acceleration | Average score rises > 5 points in a single week without performance improvement | Rapid inflation signal |

**On threshold breach:** Promise Auditor is triggered immediately. Output is delivered to the human operator as an urgent governance notification.

---

### TRIGGER TYPE 3 — MANUAL (Operator-Requested)

**Any operator may request an audit at any time by initiating a Manual audit via Claude Code.**
**Scope:** Operator specifies the audit period and focus area (e.g., "audit all STRONG band trades from the past 4 weeks").
**Minimum data requirement:** ≥ 10 events in the specified scope. If fewer, output `INSUFFICIENT_DATA` with available statistics.

---

## AUDITOR RESPONSIBILITIES

The Promise Auditor (`09_PROMISE_AUDITOR`) is responsible for the following in every audit cycle:

---

### RESPONSIBILITY 1 — Expectancy Trend Monitoring

Track week-over-week expectancy across all closed trades:
```
expectancy = (win_rate × avg_win_R) − (loss_rate × avg_loss_R)
```

- Report 4-week rolling expectancy trend
- Flag `SCORE_DRIFT_DETECTED` if expectancy declines for **2 consecutive weeks**
- Flag `NEGATIVE_EXPECTANCY` if current-week expectancy < 0 (minimum 5 trades)
- Trend data must be reported even when finding is CLEAN (provides baseline)

---

### RESPONSIBILITY 2 — Score Band Validity

For each classification band (DISCARD, WATCH, VALID, STRONG, PREMIUM):
- Compute win rate and average R achieved
- Compute expectancy
- Confirm band ordering: win rate and expectancy should increase from WATCH → VALID → STRONG → PREMIUM
- Flag `TIER_ORDERING_VIOLATED` if a lower band outperforms a higher band (minimum 10 events per band)
- Flag `NEGATIVE_EXPECTANCY_BAND` for any band where expectancy < 0

Minimum sample per band for statistical claims: **10 trades**.

---

### RESPONSIBILITY 3 — PREMIUM Classification Integrity

- Compare PREMIUM band win rate against STRONG and VALID bands
- PREMIUM must outperform STRONG by ≥ 10 percentage points to maintain valid classification
- Flag `PREMIUM_PERFORMANCE_UNSUPPORTED` if PREMIUM win rate ≤ STRONG win rate across any 20-trade window
- Track PREMIUM classification frequency — if > 40% of routed trades are classified PREMIUM, flag `PREMIUM_INFLATION` (classification is too permissive)

---

### RESPONSIBILITY 4 — Score Inflation Detection

Compare average `breakout_final_score` at entry vs. outcomes over rolling 4-week windows:
- Score drift = difference in average score between week 1 and week 4 of the window
- If score drifts up > 3 points AND win rate has not improved proportionally → flag `SCORE_INFLATION`
- Distinguish between score drift (gradual) and score inflation (drift without outcome correlation)
- Report per-family drift (raw, context, tradeability) to identify which family is inflating

---

### RESPONSIBILITY 5 — Negative Expectancy Band Reporting

**This is mandatory and non-suppressible.**

Any score band with negative expectancy (across ≥ 10 trades) must be:
1. Flagged as `NEGATIVE_EXPECTANCY_BAND` with severity CRITICAL
2. Included in the Friday Cycle summary
3. Accompanied by a specific recommendation (not a generic one)
4. Escalated to the human operator for immediate review

No band with negative expectancy may remain active without a documented governance response.

---

### RESPONSIBILITY 6 — Compounding Governor Accuracy

For any week where scaling events occurred:
- Compare win rate and expectancy during scaling periods vs. non-scaling periods
- Flag `COMPOUNDING_MISALIGNED` if scaling periods show equal or worse performance than base rate
- Minimum: 3 scaling events required for a meaningful assessment

---

### RESPONSIBILITY 7 — Repeat Finding Escalation

For any finding that was surfaced in a prior audit cycle and remains unresolved:
- Mark as `REPEAT_FINDING` with repeat_count
- Escalate severity: LOW → MEDIUM (2 cycles), MEDIUM → HIGH (3 cycles), HIGH → CRITICAL (4+ cycles)
- Include the prior cycle date and prior recommendation in the current report
- Flag as requiring formal governance response per `BREAKOUT_GOVERNANCE_RULES.md` Rule 7

---

## REQUIRED AUDIT OUTPUTS

Every audit cycle (regardless of trigger type) must produce:

### 1. AUDIT HEADER
```
report_id           : UUID
generated_at        : ISO-8601 UTC
audit_period        : start → end dates
trigger_type        : FRIDAY_CYCLE | THRESHOLD_BREACH | MANUAL
audit_verdict       : CLEAN | FLAGS_DETECTED | INSUFFICIENT_DATA
severity            : NONE | LOW | MEDIUM | HIGH | CRITICAL
trades_evaluated    : int
non_executions_evaluated : int
```

### 2. EXPECTANCY TREND TABLE
4-week rolling table with current week marked. Always present. Format:
```
Week | Trades | Win Rate | Avg Win R | Avg Loss R | Expectancy | Drift
```

### 3. SCORE BAND PERFORMANCE TABLE
One row per active band with ≥ 1 event. Format:
```
Band | Score Range | Trades | Win Rate | Avg R | Expectancy | Status
```

### 4. PREMIUM INTEGRITY BLOCK
```
premium_sample          : int
premium_win_rate        : float
strong_sample           : int
strong_win_rate         : float
spread                  : float  (premium - strong)
classification_valid    : bool
premium_frequency_pct   : float
```

### 5. FINDINGS LIST
One entry per finding. Each finding must contain:
```
finding_id        : e.g., "F001"
flag_code         : from FLAG_CODES list
severity          : LOW | MEDIUM | HIGH | CRITICAL
evidence          : metric, observed, expected, delta, sample_size, trade_ids
recommendation    : specific and actionable, max 80 words
repeat_count      : 1 for new, 2+ for repeat
escalation        : bool
```

### 6. FRIDAY CYCLE NARRATIVE
Human-readable summary, max 250 words. Must include:
- Overall assessment (clean / issues found)
- Top 1–3 findings if FLAGS_DETECTED
- Specific recommended actions for next week
- Any governance responses required

---

## AUDIT NON-NEGOTIABLES

These behaviors are absolute requirements for every audit:

1. **Negative expectancy bands are always reported.** There is no suppression path.
2. **Repeat findings always escalate in severity.** An ignored finding becomes a critical finding.
3. **Statistical claims require ≥ 10 events.** No exceptions. Fewer events = `INSUFFICIENT_DATA` note, not a finding.
4. **Records are never modified by audit activity.** Audits reference records. They do not alter them.
5. **Uncomfortable findings are not softened.** Report what the data shows. Operators can respond or dispute — auditors cannot pre-filter.
6. **Every audit cycle produces a report.** Zero-event audits produce a zero-event report, not silence.

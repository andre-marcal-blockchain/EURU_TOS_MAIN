# RISK_GUARDIAN — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 01
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

All Risk Guardian outputs must conform exactly to the following schema. No free-form narrative outside the `notes` field.

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  asset: "<SYMBOL>"
  system_mode: "<READ_ONLY | SIMULATE | EXECUTE>"

  verdict: "<APPROVED | REJECTED | FREEZE | CRITICAL_FREEZE | READ_ONLY_BLOCK | INVALID_INPUT>"
  verdict_confidence: <0.0–1.0>

  risk_checks:
    per_trade_risk_pct:
      proposed: <float>
      limit: <float>
      status: "<PASS | FAIL>"

    aggregate_risk_pct:
      current: <float>
      limit: <float>
      status: "<PASS | FAIL>"

    leverage:
      proposed: <int>
      limit: <int>
      status: "<PASS | FAIL>"

    liquidation_distance_atr_multiple:
      value: <float>
      minimum_required: 2.0
      status: "<PASS | FAIL>"

    correlation_exposure:
      max_correlation_detected: <float>
      correlated_pair: "<SYMBOL_A / SYMBOL_B | NONE>"
      status: "<PASS | FAIL>"

    drawdown_protection:
      drawdown_7d_pct: <float>
      mode: "<NORMAL | CAUTION | FREEZE | CRITICAL_FREEZE>"
      status: "<PASS | FAIL>"

    session_risk_used_pct:
      value: <float>
      remaining_pct: <float>
      status: "<PASS | FAIL>"

  failure_flags:
    - flag: "<FLAG_CODE>"
      field: "<field_that_failed>"
      detail: "<short description>"

  notes: "<optional human-readable context — max 100 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `verdict` | enum | `APPROVED`, `REJECTED`, `FREEZE`, `CRITICAL_FREEZE`, `READ_ONLY_BLOCK`, `INVALID_INPUT` |
| `verdict_confidence` | float | 0.0 – 1.0 (1.0 = fully deterministic, no ambiguity) |
| `status` per check | enum | `PASS`, `FAIL` |
| `drawdown_protection.mode` | enum | `NORMAL`, `CAUTION`, `FREEZE`, `CRITICAL_FREEZE` |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `RISK_SIZE_EXCEEDED` | Per-trade risk exceeds phase limit |
| `AGGREGATE_RISK_EXCEEDED` | Total open risk exceeds 3% threshold |
| `LEVERAGE_EXCEEDED` | Leverage above phase maximum |
| `LIQUIDATION_TOO_CLOSE` | Stop places liquidation within 2x ATR |
| `CORRELATION_CLUSTER` | Two or more correlated positions detected |
| `DRAWDOWN_FREEZE` | Rolling 7d drawdown > 5% |
| `DRAWDOWN_CRITICAL` | Rolling 7d drawdown > 8% |
| `SESSION_RISK_EXHAUSTED` | No remaining session risk budget |
| `MODE_BLOCK` | System in READ_ONLY, execution not permitted |
| `INVALID_INPUT` | Request missing required fields |
| `MODE_MISMATCH` | Submitted mode differs from active system mode |

---

## EXAMPLE APPROVED OUTPUT

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: "2026-04-15T09:32:00Z"
  asset: "ETHUSDT"
  system_mode: "SIMULATE"
  verdict: "APPROVED"
  verdict_confidence: 0.97
  risk_checks:
    per_trade_risk_pct:
      proposed: 0.80
      limit: 1.00
      status: "PASS"
    aggregate_risk_pct:
      current: 1.50
      limit: 3.00
      status: "PASS"
    leverage:
      proposed: 2
      limit: 3
      status: "PASS"
    liquidation_distance_atr_multiple:
      value: 3.20
      minimum_required: 2.0
      status: "PASS"
    correlation_exposure:
      max_correlation_detected: 0.42
      correlated_pair: "NONE"
      status: "PASS"
    drawdown_protection:
      drawdown_7d_pct: 1.20
      mode: "NORMAL"
      status: "PASS"
    session_risk_used_pct:
      value: 0.80
      remaining_pct: 2.20
      status: "PASS"
  failure_flags: []
  notes: "All checks passed. Trade eligible for execution layer review."
```

---

## EXAMPLE REJECTED OUTPUT

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: "2026-04-15T11:15:00Z"
  asset: "SOLUSDT"
  system_mode: "SIMULATE"
  verdict: "REJECTED"
  verdict_confidence: 1.0
  risk_checks:
    per_trade_risk_pct:
      proposed: 1.30
      limit: 1.00
      status: "FAIL"
    aggregate_risk_pct:
      current: 2.10
      limit: 3.00
      status: "PASS"
    leverage:
      proposed: 2
      limit: 3
      status: "PASS"
    liquidation_distance_atr_multiple:
      value: 2.80
      minimum_required: 2.0
      status: "PASS"
    correlation_exposure:
      max_correlation_detected: 0.51
      correlated_pair: "NONE"
      status: "PASS"
    drawdown_protection:
      drawdown_7d_pct: 2.10
      mode: "NORMAL"
      status: "PASS"
    session_risk_used_pct:
      value: 1.50
      remaining_pct: 1.50
      status: "PASS"
  failure_flags:
    - flag: "RISK_SIZE_EXCEEDED"
      field: "per_trade_risk_pct"
      detail: "Proposed 1.30% exceeds SIMULATE phase limit of 1.00%"
  notes: "Reduce position size to bring per-trade risk to ≤1.00% before resubmitting."
```

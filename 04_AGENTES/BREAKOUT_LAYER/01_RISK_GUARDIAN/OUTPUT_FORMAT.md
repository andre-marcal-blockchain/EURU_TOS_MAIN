# RISK_GUARDIAN — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 01_RISK_GUARDIAN
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: string            # ISO-8601 UTC
  asset: string
  system_mode: string          # READ_ONLY | SIMULATE | EXECUTE

  verdict: string              # see VERDICT VALUES
  verdict_confidence: float    # 0.0–1.0

  checks:
    per_trade_risk:
      proposed_pct: float
      limit_pct: float         # 1.0
      status: string           # PASS | FAIL

    aggregate_portfolio_risk:
      current_pct: float
      limit_pct: float         # 5.0
      status: string           # PASS | FAIL

    liquidation_distance:
      atr_multiple: float
      minimum_required: float  # 2.0
      status: string           # PASS | FAIL

    drawdown_protection:
      drawdown_week_pct: float
      limit_pct: float
      mode: string             # NORMAL | CAUTION | FREEZE
      status: string           # PASS | FAIL

    leverage_compliance:
      proposed: int
      limit: int
      status: string           # PASS | FAIL

    correlation_exposure:
      max_correlation_found: float
      correlated_pair: string  # "SYMBOL_A/SYMBOL_B" | "NONE"
      status: string           # PASS | FAIL

    session_budget:
      session_risk_used_pct: float
      remaining_pct: float
      status: string           # PASS | FAIL

  failure_flags: list[FailureFlag]

  notes: string                # optional, max 80 words
```

**FailureFlag object:**
```yaml
flag: string      # see FAILURE FLAG CODES
field: string     # which check failed
detail: string    # one-line explanation
```

---

## VERDICT VALUES

| Value | Meaning |
|---|---|
| `APPROVED` | All checks passed — forward to Tactical Execution |
| `REJECTED` | One or more checks failed — block execution |
| `FREEZE` | Weekly drawdown breached — halt all new entries |
| `READ_ONLY_BLOCK` | System in READ_ONLY mode — no execution permitted |
| `INVALID_INPUT` | Required input fields missing or malformed |

---

## CONFIDENCE LEVELS

| verdict_confidence | Interpretation |
|---|---|
| 1.0 | Fully deterministic — hard limit triggered |
| 0.8–0.99 | High confidence — all inputs clean, clear result |
| 0.6–0.79 | Moderate confidence — one input field estimated |
| < 0.6 | Low confidence — flag for human review |

---

## FAILURE FLAG CODES

| Code | Trigger |
|---|---|
| `RISK_SIZE_EXCEEDED` | Per-trade risk > 1% |
| `AGGREGATE_RISK_EXCEEDED` | Portfolio risk > 5% |
| `LIQUIDATION_TOO_CLOSE` | Liquidation distance < 2x ATR |
| `DRAWDOWN_LIMIT_BREACHED` | Weekly drawdown exceeds configured limit |
| `LEVERAGE_EXCEEDED` | Leverage above phase maximum |
| `CORRELATION_CLUSTER` | Correlated positions detected |
| `SESSION_BUDGET_EXHAUSTED` | No session risk budget remaining |
| `MODE_BLOCK` | System mode prohibits execution |
| `MODE_MISMATCH` | Submitted mode differs from active config |
| `INVALID_INPUT` | Missing or malformed required fields |
| `CONFIRMATION_MISSING` | Breakout Confirmation verdict absent |
| `REGIME_MISSING` | Market Regime verdict absent |

---

## EXAMPLE — APPROVED

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: "2026-04-15T09:32:00Z"
  asset: "ETHUSDT"
  system_mode: "SIMULATE"
  verdict: "APPROVED"
  verdict_confidence: 0.96
  checks:
    per_trade_risk:
      proposed_pct: 0.80
      limit_pct: 1.00
      status: "PASS"
    aggregate_portfolio_risk:
      current_pct: 2.40
      limit_pct: 5.00
      status: "PASS"
    liquidation_distance:
      atr_multiple: 3.20
      minimum_required: 2.00
      status: "PASS"
    drawdown_protection:
      drawdown_week_pct: 1.20
      limit_pct: 5.00
      mode: "NORMAL"
      status: "PASS"
    leverage_compliance:
      proposed: 2
      limit: 3
      status: "PASS"
    correlation_exposure:
      max_correlation_found: 0.42
      correlated_pair: "NONE"
      status: "PASS"
    session_budget:
      session_risk_used_pct: 0.80
      remaining_pct: 4.20
      status: "PASS"
  failure_flags: []
  notes: "All checks passed. Forwarding to Tactical Execution."
```

---

## EXAMPLE — REJECTED

```yaml
risk_guardian_verdict:
  version: "1.0.0"
  timestamp: "2026-04-15T11:15:00Z"
  asset: "SOLUSDT"
  system_mode: "SIMULATE"
  verdict: "REJECTED"
  verdict_confidence: 1.0
  checks:
    per_trade_risk:
      proposed_pct: 1.40
      limit_pct: 1.00
      status: "FAIL"
    aggregate_portfolio_risk:
      current_pct: 3.10
      limit_pct: 5.00
      status: "PASS"
    liquidation_distance:
      atr_multiple: 2.80
      minimum_required: 2.00
      status: "PASS"
    drawdown_protection:
      drawdown_week_pct: 2.10
      limit_pct: 5.00
      mode: "NORMAL"
      status: "PASS"
    leverage_compliance:
      proposed: 2
      limit: 3
      status: "PASS"
    correlation_exposure:
      max_correlation_found: 0.51
      correlated_pair: "NONE"
      status: "PASS"
    session_budget:
      session_risk_used_pct: 1.50
      remaining_pct: 3.50
      status: "PASS"
  failure_flags:
    - flag: "RISK_SIZE_EXCEEDED"
      field: "per_trade_risk"
      detail: "Proposed 1.40% exceeds 1.00% limit. Reduce size before resubmitting."
  notes: "Single failure. Reduce position size to ≤1.00% risk and resubmit."
```

# RISK_GUARDIAN — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 01
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Risk Guardian receives a **Trade Risk Request** package from Tactical Execution (06) or Execution Orchestrator (05) prior to any live or simulated execution. The package must include:

```
asset: string                    # e.g., "BTCUSDT"
proposed_entry: float            # price level
proposed_stop: float             # stop-loss price
proposed_leverage: int           # e.g., 3
proposed_position_size_pct: float  # % of account equity
account_equity_usdt: float       # current account size
open_positions: list             # active positions with sizes and correlations
drawdown_7d_pct: float           # rolling 7-day drawdown %
current_atr14: float             # ATR(14) in price units
system_mode: string              # READ_ONLY | SIMULATE | EXECUTE
session_risk_used_pct: float     # risk already consumed this session
```

---

## WHAT THIS AGENT PRODUCES

A **Risk Verdict** with structured fields (see OUTPUT_FORMAT.md). The verdict is:

- `APPROVED` — trade proceeds to execution layer
- `REJECTED` — trade blocked, reason provided
- `FREEZE` — all new entries blocked for session (drawdown trigger)
- `CRITICAL_FREEZE` — all pipeline activity halted (emergency)
- `READ_ONLY_BLOCK` — system is in READ_ONLY mode, no execution allowed

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Risk Verdict For |
|---|---|
| Tactical Execution (06) | Receives APPROVED or REJECTED, adjusts plan accordingly |
| Execution Orchestrator (05) | Final gate — will not proceed without APPROVED verdict |
| Compounding Governor (07) | Receives drawdown status to calibrate scaling decisions |
| DevOps Guardian (main 06) | Receives FREEZE/CRITICAL_FREEZE alerts for pipeline control |
| Journal Learning (08) | Logs all verdicts including REJECTED for pattern analysis |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — APPROVED:**
- Asset: ETHUSDT, 2x leverage, 0.8% risk per trade, aggregate open risk = 1.5%, ATR distance to liq = 3.2x, no correlated positions open, drawdown 7d = 1.2%, mode = SIMULATE
- Result: APPROVED with full parameter confirmation

**Valid — REJECTED (size violation):**
- Asset: SOLUSDT, 1.3% proposed risk per trade in SIMULATE mode
- Result: REJECTED — exceeds 1% per-trade limit. Reduce position size or widen stop.

**Valid — REJECTED (correlation cluster):**
- Open positions: ETHUSDT (long) + BNBUSDT (long) with correlation 0.91 between them
- New proposal: MATICUSDT (long) with ETH correlation 0.88
- Result: REJECTED — correlation cluster detected. Three correlated longs increase systemic risk beyond tolerance.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Missing input fields:**
- Trade request arrives without `open_positions` or `drawdown_7d_pct`
- Result: INVALID_INPUT — request incomplete, cannot evaluate. Return to sender.

**Invalid — Override attempt:**
- Downstream agent attempts to mark a REJECTED trade as approved citing "high confidence score"
- Result: Risk Guardian does not accept confidence overrides. REJECTED stands. Escalate to DevOps Guardian if override is attempted.

**Invalid — Mode mismatch:**
- System mode = READ_ONLY but trade request submitted with system_mode = SIMULATE
- Result: READ_ONLY_BLOCK. Mode spoofing is logged as an incident.

---

## AGENT POSITION IN PIPELINE

```
Tactical Execution (06) → [RISK_GUARDIAN] → Execution Orchestrator (05) → Trade
                                          ↓
                              Compounding Governor (07)
                              DevOps Guardian (main 06)
                              Journal Learning (08)
```

Risk Guardian is a **synchronous gate** — no downstream step may proceed until a verdict is returned.

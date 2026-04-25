# TACTICAL_EXECUTION — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 06
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Tactical Execution receives a **Trade Plan Request** after Breakout Confirmation has output CONFIRMED and Risk Guardian has output APPROVED. The request package includes:

```
asset: string
direction: string                       # "LONG" | "SHORT"
timeframe: string
entry_price_current: float              # current market price
breakout_zone: StructureZone            # from Structure Hunter
breakout_quality_score: int             # from Breakout Confirmation (0–10)
confirmation_verdict: string            # must be "CONFIRMED"
risk_verdict: string                    # must be "APPROVED"
approved_risk_pct: float                # from Risk Guardian
approved_leverage: int
current_atr14: float
regime: string                          # from Market Regime
next_resistance_levels: list[float]     # from Structure Hunter (for targets)
next_support_levels: list[float]        # from Structure Hunter (for stop reference)
typical_spread_pct: float               # asset spread as % of price
system_mode: string
```

---

## WHAT THIS AGENT PRODUCES

A **Complete Trade Plan** with entry, stop, three targets, scale-in levels (if applicable), and partial exit rules. The plan is structured for direct handoff to the Execution Orchestrator.

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Trade Plan For |
|---|---|
| Execution Orchestrator (main 05) | Final go/no-go before execution |
| Risk Guardian (01) | Pre-execution risk validation of final plan |
| Journal Learning (08) | Stores plan with outcome for learning |
| Promise Auditor (09) | Audits plan quality vs. actual result |
| Compounding Governor (07) | Monitors size against scaling rules |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — Market entry plan (momentum breakout):**
- BTCUSDT 4H breakout above 71,000. Quality score = 9. Volume = 2.1x avg. Regime = TRENDING_BULLISH.
- Entry type: MARKET (immediate fill). Stop: 70,400 (below zone band, 1.1x ATR below breakout close). T1: 72,500 (next resistance), T2: 74,000, T3: 76,500.
- Partial exits: T1 = close 40%, T2 = close 35%, T3 = run remainder with trail stop.
- Result: Complete plan, R:R = 2.6:1 at T1. No spread warning.

**Valid — Limit entry plan (retest wait):**
- ETHUSDT 4H. Breakout quality score = 7 (moderate). Regime = SIDEWAYS_COMPRESSION → EXPANSION.
- Entry type: LIMIT at 3,195 (retest of zone top). Stop: 3,145 (below zone base). T1: 3,350.
- Partial exits: T1 = close 50%, trail remainder.
- Result: PLAN_READY, type = LIMIT_RETEST. R:R = 3.1:1.

**Valid — Scale-in plan:**
- SOLUSDT with premium zone, score = 8. Risk Guardian approved 0.8% risk. Regime TRENDING.
- Scale-in: Entry 1 = 0.5% risk at market. Entry 2 = 0.3% risk at first pullback to breakout level.
- Result: PLAN_READY with two entry legs defined.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — R:R below 2:1:**
- Entry at 3,200, Stop at 3,175, T1 at 3,220. Risk = 25 pts. Reward = 20 pts. R:R = 0.8:1.
- Result: PLAN_REJECTED — R:R below minimum 2:1 threshold.

**Invalid — Stop inside zone:**
- Resistance zone at 3,180–3,200. Stop placed at 3,185 (inside zone).
- Result: PLAN_REJECTED — stop must be below zone base (3,180), not inside it.

**Invalid — Missing CONFIRMED verdict:**
- Breakout Confirmation output was PENDING, but trade plan request submitted anyway.
- Result: PLAN_BLOCKED — cannot construct plan without CONFIRMED verdict.

---

## AGENT POSITION IN PIPELINE

```
Breakout Confirmation (03) ──┐
Risk Guardian (01) ──────────┤→ [TACTICAL_EXECUTION] → Execution Orchestrator (main 05)
Structure Hunter (02) ───────┤                        ↓
Market Regime (05) ──────────┘               Journal Learning (08)
                                             Risk Guardian (01) [re-check]
```

Tactical Execution is a **plan synthesis node** — it is the only agent that produces a complete trade specification.

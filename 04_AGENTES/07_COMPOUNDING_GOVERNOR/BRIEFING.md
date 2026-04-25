# COMPOUNDING_GOVERNOR — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 07
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Compounding Governor receives a **Scaling Evaluation Request** triggered after each closed trade, at the start of each trading session, or on-demand by the Friday Cycle review. The request includes:

```
closed_trades_recent: list[ClosedTrade]  # last 10 closed trades with R values and dates
drawdown_7d_pct: float                    # from Risk Guardian
drawdown_14d_pct: float                  # extended window
current_base_risk_pct: float             # approved risk per trade (current baseline)
current_scaling_factor: float            # current multiplier (1.0 = base, 1.25 = scaled up once)
consecutive_wins: int                    # streak count (reset on loss)
consecutive_losses: int                  # streak count (reset on win)
win_rate_last10: float                   # % of last 10 trades that were profitable
avg_r_achieved_last10: float             # average R multiple achieved in last 10 trades
freeze_state: string                     # "NONE" | "COMPOUNDING_FREEZE" | "FULL_FREEZE"
last_friday_cycle_date: string           # ISO date of last Friday review
system_phase: string                     # READ_ONLY | SIMULATE | EXECUTE

ClosedTrade:
  trade_id: string
  asset: string
  closed_at: string                      # ISO date
  r_achieved: float                      # e.g., 2.3 = hit T2
  outcome: string                        # "WIN" | "LOSS" | "BREAK_EVEN"
  setup_score: int                       # Score Engine score at entry
```

---

## WHAT THIS AGENT PRODUCES

A **Scaling Posture Report** with:
- Current scaling verdict (SCALE_UP / HOLD / SCALE_DOWN / FREEZE)
- Approved risk % for next trade
- Scaling factor update
- Freeze state update
- Conditions for next posture change

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Scaling Posture For |
|---|---|
| Risk Guardian (01) | Updated approved risk % per trade |
| Tactical Execution (06) | Position sizing in plan construction |
| Journal Learning (08) | Scaling posture logged alongside each trade |
| Promise Auditor (09) | Scaling decisions audited for overconfidence patterns |
| Friday Cycle (SOP_SEMANAL) | Weekly human review of Governor posture |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — SCALE_UP approved:**
- Last 10 trades: 7 wins, 3 losses. Win rate = 70%. Avg R = 2.4. Consecutive wins = 4. Drawdown 7d = 0.8%. Current scaling factor = 1.0. Last Friday Cycle = 7 days ago.
- Result: SCALE_UP approved. New scaling factor = 1.25. New approved risk = base × 1.25.

**Valid — HOLD (not enough evidence):**
- Last 10 trades: 6 wins, 4 losses. Win rate = 60%. Avg R = 1.8. Consecutive wins = 2 (below threshold of 3). Drawdown = 1.5%.
- Result: HOLD — consecutive win threshold not met. Maintain current sizing.

**Valid — FREEZE (consecutive losses):**
- Last 3 trades: 3 consecutive losses. Drawdown 7d = 4.2%.
- Result: COMPOUNDING_FREEZE. No scaling up. Current size maintained (not reduced yet — drawdown < 5%).

**Valid — SCALE_DOWN (drawdown trigger):**
- Drawdown 7d = 3.8%. Win rate last 10 = 40%. Avg R = 0.9.
- Result: SCALE_DOWN. Approved risk reduced by 25%. Scaling factor adjusted.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Compounding on SIMULATE hypothetical trades:**
- User requests scale-up based on 5 un-executed SIMULATE setups that were observed but not taken.
- Result: IGNORED — only closed, executed trades count. Hypotheticals have no compounding weight.

**Invalid — Lifting freeze without performance criteria:**
- User requests freeze lift after "2 good looking setups" — no actual closed wins.
- Result: FREEZE maintained. Release requires 2 consecutive closed wins AND drawdown < 2%.

**Invalid — Second consecutive SCALE_UP in same week:**
- System SCALE_UP approved Monday. Another SCALE_UP requested Thursday (no Friday Cycle between).
- Result: HOLD — second scale-up requires a Friday Cycle review gate. Escalate to weekly SOP.

---

## AGENT POSITION IN PIPELINE

```
Journal Learning (08) ──┐
Risk Guardian (01) ──────┤→ [COMPOUNDING_GOVERNOR] → Risk Guardian (01) [updated limit]
Friday Cycle (weekly) ───┘                         → Tactical Execution (06)
                                                   → Journal Learning (08)
                                                   → Promise Auditor (09)
```

Compounding Governor is a **performance-gated policy agent** — it adjusts the system's risk budget based on earned evidence.

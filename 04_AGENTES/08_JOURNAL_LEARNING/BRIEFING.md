# JOURNAL_LEARNING — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 08
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Journal Learning receives inputs from every stage of the pipeline. There is no single request format — it accepts structured events from all agents:

**Trade Entry Event (from Tactical Execution):**
```
event_type: "TRADE_ENTRY"
trade_id: string
asset: string
direction: LONG | SHORT
entry_price: float
stop_price: float
t1_price: float
entry_timestamp: ISO-8601
plan_confidence: float
regime_at_entry: string
structure_score: int
breakout_quality_score: int
risk_verdict: string
system_phase: string
agent_verdicts: dict    # all agent outputs at time of entry
```

**Trade Exit Event:**
```
event_type: "TRADE_EXIT"
trade_id: string
exit_price: float
exit_timestamp: ISO-8601
r_achieved: float
outcome: WIN | LOSS | BREAK_EVEN
exit_type: TP_HIT | SL_HIT | MANUAL | TRAIL_STOP
partial_exits: list
```

**Non-Execution Event (blocked/fakeout/rejected):**
```
event_type: "NON_EXECUTION"
asset: string
reason: string           # e.g., "RISK_REJECTED", "FAKEOUT", "NEWS_HOLD"
verdict_at_block: string
timestamp: ISO-8601
agent_verdicts: dict
```

**Alert Event (from Alert Radar):**
```
event_type: "ALERT_RECEIVED"
alert_id: string
alert_status: string     # ROUTED | REJECTED | DUPLICATE | etc.
asset: string
timestamp: ISO-8601
```

---

## WHAT THIS AGENT PRODUCES

1. **Trade Records** — structured entries for every trade and non-execution event.
2. **Post-Mortem Reports** — comparative analysis of plan vs. outcome for closed trades.
3. **Weekly Learning Summary** — digest for Friday Cycle review.
4. **Pattern Reports** — recurring patterns identified from ≥ 5 similar events.
5. **Compounding Governor Feed** — closed trade list with R values.

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Journal Learning Output For |
|---|---|
| Compounding Governor (07) | Closed trade list for scaling evaluation |
| Promise Auditor (09) | Full trade + score history for bias analysis |
| Score Engine (main 08) | Pattern data for criterion weight re-evaluation |
| Friday Cycle (human) | Weekly summary for governance review |
| Journal Auditor (main 07) | Audit verification against journal records |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — Complete trade entry logged:**
- All agent verdicts captured. Structure score = 8, breakout quality = 9, risk verdict = APPROVED. Entry logged at 09:45 UTC. All fields populated.
- Result: Trade record stored. Status = COMPLETE.

**Valid — Non-execution logged:**
- SOLUSDT alert received, routed, confirmed, but Risk Guardian REJECTED due to aggregate risk limit.
- Result: NON_EXECUTION record stored with reason = "RISK_AGGREGATE_EXCEEDED". All verdicts captured.

**Valid — Post-mortem generated:**
- ETHUSDT trade closed at T2. Plan had T2 = 3,480. Actual exit = 3,465 (trail stop triggered). R planned at T2 = 4.2. R achieved = 3.9.
- Post-mortem: Delta = -0.3R. Process was followed. Outcome consistent with setup quality. No anomalies.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Retroactive scoring:**
- User asks: "Score this old trade from 2 weeks ago using today's Score Engine criteria."
- Result: REJECTED. Scores must reflect agent outputs at time of entry. Historical re-scoring distorts learning.

**Invalid — Deleting a record:**
- Any request to remove or modify a prior journal entry.
- Result: REJECTED. All records are append-only. Add a correction note as a new entry if needed.

**Invalid — Pattern claim from 2 events:**
- "SOLUSDT ascending triangle always fails — we've seen it twice."
- Result: NOT_SURFACED. Minimum 5 events required for pattern claims.

---

## AGENT POSITION IN PIPELINE

```
[All Pipeline Agents] ──→ [JOURNAL_LEARNING] ──→ Compounding Governor (07)
                                              ──→ Promise Auditor (09)
                                              ──→ Score Engine (main 08)
                                              ──→ Friday Cycle (human review)
                                              ──→ Journal Auditor (main 07)
```

Journal Learning is an **always-on logging and synthesis node** — it receives from everyone and serves everyone.

# JOURNAL_LEARNING — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 08_JOURNAL_LEARNING
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Journal Learning is an always-on receiver. It accepts structured event messages from every agent in the BREAKOUT_LAYER pipeline. There is no single request format.

---

### INPUT TYPE 1 — TRADE ENTRY (from Tactical Execution)

```
event_type          : "TRADE_ENTRY"
trade_id            : string
asset               : string
direction           : LONG | SHORT
entry_price         : float
stop_price          : float
t1_price            : float
t2_price            : float | null
t3_price            : float | null
entry_timestamp     : ISO-8601 UTC
plan_confidence     : float
entry_type          : MARKET | LIMIT_RETEST | LIMIT_BREAKOUT
system_phase        : string
session             : MORNING | ASIAN | MANUAL
regime_at_entry     : string
btc_alignment_score : float
zone_id             : string
zone_score          : int
breakout_quality_score : int
structure_score     : int
risk_approved_pct   : float
warning_flags       : list[string]
agent_verdicts      : dict     # all agent outputs at entry time
```

---

### INPUT TYPE 2 — TRADE EXIT (from Tactical Execution / manual)

```
event_type          : "TRADE_EXIT"
trade_id            : string
exit_price          : float
exit_timestamp      : ISO-8601 UTC
r_achieved          : float
outcome             : WIN | LOSS | BREAK_EVEN
exit_type           : TP_HIT | SL_HIT | MANUAL | TRAIL_STOP
partial_exits       : list[PartialExit]
```

---

### INPUT TYPE 3 — NON-EXECUTION EVENT (from any agent)

```
event_type          : "NON_EXECUTION"
asset               : string
direction           : LONG | SHORT | UNKNOWN
reason_code         : string     # FAKEOUT | RISK_REJECTED | NEWS_HOLD | FREEZE_BLOCK | etc.
blocking_agent      : string
session             : string
regime_at_block     : string
timestamp           : ISO-8601 UTC
agent_verdicts      : dict
```

---

### INPUT TYPE 4 — SCALING DECISION (from Compounding Governor)

```
event_type          : "SCALING_DECISION"
scaling_verdict     : string
previous_factor     : float
new_factor          : float
trigger             : string
performance_snapshot : dict
timestamp           : ISO-8601 UTC
```

---

## OUTPUTS

1. **Closed Trade List** — delivered to Compounding Governor on performance state requests.
2. **Pattern Reports** — weekly, minimum 5-event samples, delivered to Friday Cycle and Promise Auditor.
3. **Weekly Summary** — structured digest for Friday Cycle.
4. **Scorecard Feed** — aggregate performance by score band for Scorecard Engine.

---

## VALID SITUATIONS

**Scenario A — Complete trade entry stored:**
- All 20+ fields populated. Regime = TREND_BULL, session = MORNING, zone_score = 9, breakout_quality = 8. agent_verdicts dict complete.
- Result: Record stored. Status = COMPLETE.

**Scenario B — FAKEOUT logged:**
- SOLUSDT BREAKOUT alert received, routed, structure confirmed, but Breakout Confirmation = FAKEOUT.
- Record stored with event_type = NON_EXECUTION, reason_code = FAKEOUT, blocking_agent = BREAKOUT_CONFIRMATION. Zone ID and session tagged.

**Scenario C — Pattern surfaced (5+ events):**
- After 7 SOLUSDT FAKEOUT events on 4H ASCENDING_TRIANGLE formations during CHOPPY regime:
- Pattern flagged: `ASCENDING_TRIANGLE_CHOPPY_FAKEOUT`. Win rate = 0%. Recommendation: Filter out this setup type during CHOPPY regime.

---

## INVALID SITUATIONS

**Storing incomplete feature row:**
- Trade entry arrives but `regime_at_entry` and `session` are null/absent.
- Invalid. Must not store incomplete row. Return `INCOMPLETE_INPUT` to sender. Request resubmission with missing fields.

**Retroactive score modification:**
- Operator requests that old trade records be re-scored with updated Score Engine criteria.
- Invalid. Scores must reflect agent outputs at time of entry. Log correction request as a governance note — do not alter original record.

**Pattern claim from 3 events:**
- "Wedge breakouts fail — we've seen 3 losses."
- Invalid. Three events is below minimum. Log the events. Do not surface as a pattern until 5+ events.

---

## NOTES

- Journal Learning receives events from all agents — it has the widest data scope in the pipeline.
- `agent_verdicts` dict must capture the complete output of every relevant agent, not just the verdict string.
- Friday Cycle summary is produced every Friday regardless of trade count that week. Zero-trade weeks are valid and informative.
- Compounding Governor queries the `closed_trades_list` view — Journal Learning must maintain this as a queryable index.

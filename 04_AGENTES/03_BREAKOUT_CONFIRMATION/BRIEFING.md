# BREAKOUT_CONFIRMATION — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 03
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Breakout Confirmation receives a **Breakout Evaluation Request** triggered either by Alert Radar (04) or by a manual pipeline run. The request includes:

```
asset: string                          # e.g., "BTCUSDT"
timeframe: string                      # "4H" | "1D" | "1H"
breakout_candle: OHLCV                 # the candle that crossed the zone
prior_candles: list[OHLCV]            # last 20 candles before breakout
post_candles: list[OHLCV]             # up to 3 candles after breakout (may be empty if live)
zone: StructureZone                   # from Structure Hunter output
volume_ma20: float                     # 20-period volume average
current_atr14: float
news_sentinel_status: string           # LOW | MEDIUM | HIGH | CRITICAL | NOT_CHECKED
btc_flow_status: string                # CONFIRMS | CONTRADICTS | INCONCLUSIVE
trigger_source: string                 # "ALERT_RADAR" | "MANUAL" | "SCHEDULED_SCAN"
```

---

## WHAT THIS AGENT PRODUCES

A **Breakout Verdict** with:
- Confirmation status (CONFIRMED / FAKEOUT / PENDING / HOLD / INVALID)
- Quality score for the breakout event (0–10)
- Component scores for each evaluation criterion
- Volume analysis summary
- Post-break behavior classification
- Retest detected flag

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Breakout Verdict For |
|---|---|
| Tactical Execution (06) | Only builds trade plan if verdict = CONFIRMED |
| Score Engine (08) | Breakout quality score feeds momentum criterion |
| Alert Radar (04) | FAKEOUT flags stored to improve future alert filtering |
| Structure Hunter (02) | ZONE_EXHAUSTED flag triggers zone re-evaluation |
| Journal Learning (08) | Full breakout event logged with all component scores |
| Promise Auditor (09) | Monitors confirmation quality vs. subsequent outcomes |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — CONFIRMED (textbook breakout):**
- BTCUSDT 4H: Price closes at 71,200, zone resistance was 70,800 (band: 70,750–70,850). Body close = 71,200. Volume = 1.8x the MA20. Upper wick = 15% of candle range. No news window. Next candle: green, closes at 71,500. BTC CONFIRMS.
- Result: CONFIRMED, quality_score = 9, all component checks PASS

**Valid — PENDING (great candle, no follow-through yet):**
- ETHUSDT 4H: Clean breakout candle, volume = 1.4x MA20, wick = 20% of range, but only one candle elapsed post-break (live analysis).
- Result: PENDING — re-evaluate after next candle closes

**Valid — FAKEOUT (wick-only break):**
- SOLUSDT 4H: Wick pierces zone by 0.8%, but candle CLOSES below zone boundary. Volume average.
- Result: FAKEOUT — close inside zone, wick-only penetration. Notify Alert Radar.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Confirming without volume:**
- Breakout candle with beautiful body, closes well beyond zone, but volume = 0.6x MA20
- Result: PENDING (do not CONFIRM without volume participation)

**Invalid — Confirming during CRITICAL news:**
- News Sentinel reports CRITICAL severity event (major CPI print, regulatory action)
- Result: HOLD — regardless of candle quality. Escalate to News Sentinel.

**Invalid — Confirming altcoin breakout when BTC CONTRADICTS:**
- BNBUSDT appears to break out cleanly, but BTC Flow Analyst = CONTRADICTS
- Result: CONDITIONAL_CONFIRM with BTC caveat flag — do not route to full execution

---

## AGENT POSITION IN PIPELINE

```
Structure Hunter (02) ──┐
Alert Radar (04) ───────┤→ [BREAKOUT_CONFIRMATION] → Tactical Execution (06)
News Sentinel ──────────┘                          ↓
                                        Score Engine (08)
                                        Journal Learning (08)
```

Breakout Confirmation is a **real-time decision node** — latency matters. Default to PENDING over CONFIRMED when uncertain.

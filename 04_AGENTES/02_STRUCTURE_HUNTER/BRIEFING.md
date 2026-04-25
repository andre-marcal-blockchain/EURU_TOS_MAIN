# STRUCTURE_HUNTER — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 02
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Structure Hunter receives a **Structural Analysis Request** from Scout (01) or directly from the morning/Asian scan pipeline. The request includes:

```
asset: string                      # e.g., "BTCUSDT"
primary_timeframe: string          # "1D" | "4H" | "1H"
secondary_timeframe: string        # optional confirmation TF
price_series: list[OHLCV]          # last 100–200 candles on primary TF
current_price: float
current_atr14: float
score_engine_tier: string          # TIER_1 | TIER_2 | TIER_3 | UNRANKED
btc_structural_status: string      # SETUP | WATCHLIST | NO_TRADE
session: string                    # "MORNING" | "ASIAN" | "MANUAL"
```

---

## WHAT THIS AGENT PRODUCES

A **Structural Map** with:
- Classified S/R zones (up to 3 primary, labeled PREMIUM / STANDARD / WEAK)
- Zone scores (0–10 per zone)
- Formation classification
- Compression assessment
- Breakout-readiness flag
- Failed attempt log

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Structural Map For |
|---|---|
| Breakout Confirmation (03) | Validates if current candle is breaking a valid zone |
| Score Engine (08) | `structure` scoring criterion (0–5 points) |
| Tactical Execution (06) | Stop placement (below zone low), target (next zone high) |
| Journal Learning (08) | Zone metadata stored alongside execution results |
| Market Regime (05) | Zone compression data used for volatility regime detection |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — PREMIUM zone with compression:**
- ETHUSDT 4H chart: price tested 3,200 USDT on 4 separate occasions over 18 bars, each rejection with wicks. Range is tightening. ATR declining 15% over 10 bars.
- Formation: Flat-top resistance with ascending lows (ascending triangle).
- Result: PREMIUM zone at 3,200, formation = ASCENDING_TRIANGLE, compression = TRUE, breakout_ready = TRUE

**Valid — STANDARD zone, no compression:**
- SOLUSDT Daily: clean resistance at 145 tested twice. Price is 8% below zone. Range normal.
- Result: STANDARD zone at 145, formation = HORIZONTAL_RESISTANCE, compression = FALSE, breakout_ready = FALSE

**Valid — Failed prior breakout detected:**
- BNBUSDT 4H: price broke above 580 on 2026-04-08 with a long wick, closed back below. Three sessions later, price is re-testing from below.
- Result: Zone annotated with FAILED_BREAK on 2026-04-08. Current test is attempt 2. Confidence elevated.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Zone with single touch:**
- A single swing high at 420 with no retests
- Result: NOT a valid zone. Output `NO_STRUCTURE` or classify as WATCH_ONLY (not tradeable)

**Invalid — Using 15M candles for zone boundaries:**
- Attempting to define a primary zone from sub-1H price action
- Result: `INVALID_TIMEFRAME` — use 4H or Daily for zone construction

**Invalid — Fabricating structure when none exists:**
- Asset in free fall with no consolidation, no retests, no flat zones
- Result: `NO_STRUCTURE` — do not assign zones to trending impulse moves

---

## AGENT POSITION IN PIPELINE

```
Scout (01) → [STRUCTURE_HUNTER] → Breakout Confirmation (03) → Score Engine (08)
                                ↓
                    Tactical Execution (06)
                    Journal Learning (08)
```

Structure Hunter is an **analysis node** — it produces maps, not decisions.

# MARKET_REGIME — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 05
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Market Regime receives a **Regime Assessment Request** at the start of each trading session and on-demand when pipeline agents require regime context:

```
asset: string                        # e.g., "ETHUSDT" or "BTC_MASTER"
timeframe: string                    # "1D" | "4H" | "1H"
price_series: list[OHLCV]            # last 50 candles
adx14: float                         # ADX(14) value
atr14: float                         # ATR(14) current
atr14_10bars_ago: float              # ATR(14) 10 bars back (for trend detection)
btc_price_series: list[OHLCV]        # BTC OHLCV if asset is altcoin
btc_adx14: float
btc_atr14: float
macro_data:
  dxy_trend: string                  # "UP" | "DOWN" | "FLAT"
  btc_dominance_trend: string        # "UP" | "DOWN" | "FLAT"
  risk_sentiment: string             # "RISK_ON" | "RISK_OFF" | "NEUTRAL"
session: string                      # "MORNING" | "ASIAN" | "MANUAL"
```

---

## WHAT THIS AGENT PRODUCES

A **Regime Report** with:
- Primary regime classification
- Volatility state
- BTC alignment assessment
- Macro sentiment assessment
- Regime favorability for breakout trading
- Transition warning if regime is changing

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Regime Report For |
|---|---|
| Breakout Confirmation (03) | Downgrade confidence if CHOPPY regime |
| Score Engine (08) | Regime-adjusted scoring for momentum criterion |
| Tactical Execution (06) | Trail stop aggressiveness, target selection |
| Compounding Governor (07) | Regime used to decide if scaling is appropriate |
| Journal Learning (08) | Regime context stored with every trade outcome |
| Promise Auditor (09) | Checks if poor outcomes correlate with ignored regime warnings |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — TRENDING regime, breakout-favorable:**
- BTCUSDT 4H: ADX(14) = 34, price above 20/50 EMA, ATR expanding (+12% over 10 bars), DXY declining, BTC dominance neutral.
- Result: TRENDING_BULLISH, volatility = EXPANDING, breakout_favorable = TRUE

**Valid — CHOPPY regime:**
- ETHUSDT 4H: ADX(14) = 14, price oscillating between 3,000–3,300 for 25 bars, ATR flat.
- Result: CHOPPY, volatility = NEUTRAL, breakout_favorable = FALSE, `BTC_CHOPPY_WARNING` if BTC is same

**Valid — COMPRESSION sub-regime:**
- SOLUSDT Daily: ADX = 16, ATR declining -22% over 10 bars, price narrowing into wedge apex.
- Result: SIDEWAYS_COMPRESSION, volatility = CONTRACTING, breakout_favorable = PENDING (watch for expansion)

**Valid — REGIME_TRANSITION:**
- BNBUSDT 4H: Was CHOPPY for 20 bars. ADX now at 22 and rising. ATR expanded 18% in last 4 bars.
- Result: REGIME_TRANSITION (CHOPPY → TRENDING), confidence = 0.61, minimum 3 confirming bars reached.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Claiming TRENDING without ADX check:**
- Price moving up for 5 bars but ADX = 17
- Result: Cannot classify as TRENDING. Must output CHOPPY or TRANSITIONAL.

**Invalid — Altcoin BREAKOUT_FAVORABLE when BTC is CHOPPY:**
- LINKUSDT has a perfect structure, ATR expanding, but BTC ADX = 13.
- Result: Output CONDITIONAL — altcoin favorable but BTC_CHOPPY_WARNING active. Breakout_favorable = CONDITIONAL.

**Invalid — Macro alignment without data:**
- If macro_data fields are absent, do not guess DXY or risk sentiment.
- Result: Mark `macro_alignment = NOT_CHECKED`. Do not fabricate macro context.

---

## AGENT POSITION IN PIPELINE

```
[External/Scan Data] → [MARKET_REGIME] ──→ Breakout Confirmation (03)
                                        ──→ Score Engine (08)
                                        ──→ Tactical Execution (06)
                                        ──→ Compounding Governor (07)
                                        ──→ Journal Learning (08)
```

Market Regime runs at session start and on-demand. It is a **context broadcast** agent, not a decision gate.

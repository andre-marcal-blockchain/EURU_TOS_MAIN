---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-09
scorecard_date: 2026-04-09
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-09
period_end: 2026-04-09

system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS — Scout Report

health_status: healthy
decision_status: keep
deviation_severity: none

closed_trades_count: 0
win_rate_pct: 0.0
average_rr: 0.0
expectancy: 0.0
prediction_accuracy_pct: 0.0

average_entry_score: 0.0
average_entry_score_winners: 0.0
average_entry_score_losers: 0.0

threshold_breach_count: 0
deviation_count: 0
blocked_trades_count: 0
watchlist_alert_count: 0

human_approval_required: false
linked_learning_report: null

tags:
  - scout_report
  - legacy_migrated
---

# Scorecard Snapshot

## Subject Summary
- Migrated from legacy format. See original content below.

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | 0.0 | 50.0 | pending |
| average_rr | 0.0 | 2.0 | pending |
| expectancy | 0.0 | 0.01 | pending |

## Threshold Review
- none

## Deviations
- none

## Decision
- keep

## Action Plan
- Review and update from original content below.

---

## Original Content (Legacy)

# Euru OS — Morning Scan Report
**Date:** 2026-04-09  
**Time:** 05:00 UTC  
**Assets scanned:** 17  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** INACTIVE — BTC trend is MIXED; altcoin signals unmodified  

---

## System Health

```
TOTAL_ASSETS_REQUESTED:  18
TOTAL_ASSETS_FETCHED:    17
TOTAL_ASSETS_EXCLUDED:   1
FAILED_ASSETS:           none
STALE_ASSETS:            MATICUSDT
ANOMALOUS_ASSETS:        none
NEWS_SENTINEL_SOURCE:    CoinTelegraph
NEWS_SENTINEL_STATUS:    OK
PIPELINE_STATUS:         HEALTHY
```

---

## Price Summary

| Symbol | Price (USDT) | 24h | vs 7D | RSI | MACD | OBV | Stop Dist | Score | Tier | State |
|--------|-------------|-----|-------|-----|------|-----|-----------|-------|------|-------|
| BTCUSDT |    70,774.41 | -1.13% | +2.77% | 55.16 | BULLISH | FALLING | 3,664.6406 | **26/35** | BOA | **WATCHLIST** |
| ETHUSDT |     2,177.41 | -2.87% | +2.82% | 55.42 | BULLISH | FALLING | 152.1177 | **26/35** | BOA | **WATCHLIST** |
| SOLUSDT |        81.80 | -3.24% | +0.42% | 45.21 | BULLISH | FALLING | 6.4735 | **21/35** | BOA | **NO_TRADE** |
| BNBUSDT |       598.97 | -2.67% | +0.11% | 42.58 | BULLISH | FALLING | 29.5072 | **21/35** | BOA | **NO_TRADE** |
| AVAXUSDT |         9.05 | -4.33% | +0.40% | 48.07 | BULLISH | FLAT | 0.7722 | **19/35** | MEDIA | **NO_TRADE** |
| DOTUSDT |         1.25 | -4.72% | -0.48% | 39.44 | BULLISH | FLAT | 0.1056 | **17/35** | MEDIA | **NO_TRADE** |
| LINKUSDT |         8.76 | -4.99% | -0.68% | 47.49 | BULLISH | FALLING | 0.6685 | **22/35** | BOA | **NO_TRADE** |
| ADAUSDT |         0.25 | -5.18% | -0.14% | 46.40 | BULLISH | FLAT | 0.0211 | **17/35** | MEDIA | **NO_TRADE** |
| XRPUSDT |         1.33 | -3.27% | -0.01% | 44.13 | BULLISH | FLAT | 0.0841 | **22/35** | BOA | **NO_TRADE** |
| SUIUSDT |         0.91 | -5.40% | +2.24% | 48.98 | BULLISH | FLAT | 0.0804 | **23/35** | BOA | **WATCHLIST** |
| NEARUSDT |         1.34 | +2.53% | +6.89% | 61.01 | BULLISH | RISING | 0.1074 | **25/35** | BOA | **SETUP** |
| INJUSDT |         2.89 | -4.40% | +1.47% | 46.99 | BULLISH | RISING | 0.2188 | **19/35** | MEDIA | **WATCHLIST** |
| ARBUSDT |         0.10 | -1.16% | +6.47% | 56.19 | BULLISH | RISING | 0.0087 | **24/35** | BOA | **WATCHLIST** |
| OPUSDT |         0.11 | -5.02% | +1.84% | 46.76 | BULLISH | FLAT | 0.0104 | **21/35** | BOA | **WATCHLIST** |
| FETUSDT |         0.23 | -6.88% | -1.62% | 53.57 | BEARISH | FALLING | 0.0304 | **23/35** | BOA | **WATCHLIST** |
| TAOUSDT |       322.00 | -4.51% | +2.73% | 61.62 | BEARISH | FALLING | 35.9900 | **25/35** | BOA | **WATCHLIST** |
| RENDERUSDT |         2.03 | -1.27% | +5.13% | 64.46 | BULLISH | FALLING | 0.2000 | **23/35** | BOA | **WATCHLIST** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | BTCUSDT | **26/35** (74%) | **BOA** | 5 | 4 | 2 | 5 | 3 | 5 | 2 |
| 2 | ETHUSDT | **26/35** (74%) | **BOA** | 5 | 5 | 2 | 5 | 2 | 5 | 2 |
| 3 | NEARUSDT | **25/35** (71%) | **BOA** | 3 | 5 | 5 | 3 | 4 | 5 | 0 |
| 4 | TAOUSDT | **25/35** (71%) | **BOA** | 4 | 5 | 2 | 5 | 1 | 5 | 3 |
| 5 | ARBUSDT | **24/35** (69%) | **BOA** | 2 | 5 | 3 | 4 | 2 | 5 | 3 |
| 6 | SUIUSDT | **23/35** (66%) | **BOA** | 3 | 5 | 2 | 4 | 1 | 5 | 3 |
| 7 | FETUSDT | **23/35** (66%) | **BOA** | 2 | 5 | 2 | 5 | 0 | 5 | 4 |
| 8 | RENDERUSDT | **23/35** (66%) | **BOA** | 2 | 4 | 3 | 5 | 2 | 5 | 2 |
| 9 | LINKUSDT | **22/35** (63%) | **BOA** | 3 | 5 | 0 | 4 | 1 | 5 | 4 |
| 10 | XRPUSDT | **22/35** (63%) | **BOA** | 4 | 5 | 0 | 4 | 1 | 5 | 3 |
| 11 | SOLUSDT | **21/35** (60%) | **BOA** | 4 | 3 | 0 | 5 | 1 | 5 | 3 |
| 12 | BNBUSDT | **21/35** (60%) | **BOA** | 3 | 4 | 0 | 4 | 2 | 5 | 3 |
| 13 | OPUSDT | **21/35** (60%) | **BOA** | 1 | 5 | 2 | 4 | 1 | 5 | 3 |
| 14 | AVAXUSDT | **19/35** (54%) | **MEDIA** | 3 | 3 | 0 | 4 | 1 | 5 | 3 |
| 15 | INJUSDT | **19/35** (54%) | **MEDIA** | 1 | 3 | 2 | 4 | 1 | 5 | 3 |
| 16 | DOTUSDT | **17/35** (49%) | **MEDIA** | 2 | 3 | 0 | 3 | 1 | 5 | 3 |
| 17 | ADAUSDT | **17/35** (49%) | **MEDIA** | 3 | 2 | 0 | 3 | 1 | 5 | 3 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-09 05:00 UTC
OVERALL_SEVERITY: HIGH
TOP_HEADLINES:
  1. [HIGH] Bitcoin tops $72K after $280M liquidation targets bears: Will the ‘fragile truce’ hold?
  2. [HIGH] US SEC taps new enforcement chief amid questions over predecessor's exit
  3. [HIGH] Bitcoin fades three-week highs as BTC price shrugs off Iran war ceasefire
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 72,857.00 | S: 65,712.12 | 7D_AVG: 68,864.10
INVALIDATION: Break outside week range (65,712.12 – 72,857.00)
STATE: WATCHLIST
SIGNAL: Price +2.77% from 7D avg — monitoring for continuation
REASON: Current price 70,774.41 is +2.77% vs 7D avg 68,864.10. 24h change: -1.13%. Trend: MIXED. 24h range: 3.38% vs avg daily range 3.41%.
--- Flow Analyst ---
RSI_14: 55.16
MACD_TREND: BULLISH
MACD_HISTOGRAM: 460.910359
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 2443.0937
STOP_DIST (ATR×1.5): 3,664.6406
SUGGESTED_STOP: 67,100.1894
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,273.87 | S: 2,017.04 | 7D_AVG: 2,117.69
INVALIDATION: Break outside week range (2,017.04 – 2,273.87)
STATE: WATCHLIST
SIGNAL: Price +2.82% from 7D avg — monitoring for continuation
REASON: Current price 2,177.41 is +2.82% vs 7D avg 2,117.69. 24h change: -2.87%. Trend: MIXED. 24h range: 4.99% vs avg daily range 4.78%.
--- Flow Analyst ---
RSI_14: 55.42
MACD_TREND: BULLISH
MACD_HISTOGRAM: 14.690765
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 101.4118
STOP_DIST (ATR×1.5): 152.1177
SUGGESTED_STOP: 2,025.2923
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 87.02 | S: 76.70 | 7D_AVG: 81.46
INVALIDATION: Break outside week range (76.70 – 87.02)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 81.80 is +0.42% vs 7D avg 81.46. 24h change: -3.24%. Trend: SIDEWAYS. 24h range: 4.01% vs avg daily range 4.99%.
--- Flow Analyst ---
RSI_14: 45.21
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.089731
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 4.3157
STOP_DIST (ATR×1.5): 6.4735
SUGGESTED_STOP: 75.3165
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 624.85 | S: 570.31 | 7D_AVG: 598.29
INVALIDATION: Break outside week range (570.31 – 624.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 598.97 is +0.11% vs 7D avg 598.29. 24h change: -2.67%. Trend: SIDEWAYS. 24h range: 3.42% vs avg daily range 3.50%.
--- Flow Analyst ---
RSI_14: 42.58
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.338024
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 19.6715
STOP_DIST (ATR×1.5): 29.5072
SUGGESTED_STOP: 569.4628
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.66 | S: 8.46 | 7D_AVG: 9.01
INVALIDATION: Break outside week range (8.46 – 9.66)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 9.05 is +0.40% vs 7D avg 9.01. 24h change: -4.33%. Trend: SIDEWAYS. 24h range: 6.63% vs avg daily range 6.54%.
--- Flow Analyst ---
RSI_14: 48.07
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.029020
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.5148
STOP_DIST (ATR×1.5): 0.7722
SUGGESTED_STOP: 8.2778
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.33 | S: 1.20 | 7D_AVG: 1.26
INVALIDATION: Break outside week range (1.20 – 1.33)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.25 is -0.48% vs 7D avg 1.26. 24h change: -4.72%. Trend: SIDEWAYS. 24h range: 6.79% vs avg daily range 5.29%.
--- Flow Analyst ---
RSI_14: 39.44
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.004708
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0704
STOP_DIST (ATR×1.5): 0.1056
SUGGESTED_STOP: 1.1454
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.42 | S: 8.42 | 7D_AVG: 8.82
INVALIDATION: Break outside week range (8.42 – 9.42)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.76 is -0.68% vs 7D avg 8.82. 24h change: -4.99%. Trend: SIDEWAYS. 24h range: 6.85% vs avg daily range 5.08%.
--- Flow Analyst ---
RSI_14: 47.49
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.026207
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.4457
STOP_DIST (ATR×1.5): 0.6685
SUGGESTED_STOP: 8.0915
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.27 | S: 0.23 | 7D_AVG: 0.25
INVALIDATION: Break outside week range (0.23 – 0.27)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.25 is -0.14% vs 7D avg 0.25. 24h change: -5.18%. Trend: SIDEWAYS. 24h range: 6.43% vs avg daily range 5.85%.
--- Flow Analyst ---
RSI_14: 46.40
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001360
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0140
STOP_DIST (ATR×1.5): 0.0211
SUGGESTED_STOP: 0.2277
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.40 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Break outside week range (1.28 – 1.40)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.33 is -0.01% vs 7D avg 1.33. 24h change: -3.27%. Trend: SIDEWAYS. 24h range: 4.75% vs avg daily range 4.01%.
--- Flow Analyst ---
RSI_14: 44.13
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002586
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0561
STOP_DIST (ATR×1.5): 0.0841
SUGGESTED_STOP: 1.2476
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.98 | S: 0.84 | 7D_AVG: 0.89
INVALIDATION: Break outside week range (0.84 – 0.98)
STATE: WATCHLIST
SIGNAL: Price +2.24% from 7D avg — monitoring for continuation
REASON: Current price 0.91 is +2.24% vs 7D avg 0.89. 24h change: -5.40%. Trend: MIXED. 24h range: 6.97% vs avg daily range 5.98%.
--- Flow Analyst ---
RSI_14: 48.98
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.007135
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0536
STOP_DIST (ATR×1.5): 0.0804
SUGGESTED_STOP: 0.8285
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.39 | S: 1.14 | 7D_AVG: 1.25
INVALIDATION: Close below 7D_AVG (1.25)
STATE: SETUP
SIGNAL: Price +6.89% from 7D avg with aligned trend
REASON: Current price 1.34 is +6.89% vs 7D avg 1.25. 24h change: +2.53%. Trend: BULLISH. 24h range: 6.50% vs avg daily range 6.31%.
--- Flow Analyst ---
RSI_14: 61.01
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.014247
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0716
STOP_DIST (ATR×1.5): 0.1074
SUGGESTED_STOP: 1.2306
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 3.05 | S: 2.73 | 7D_AVG: 2.85
INVALIDATION: Break outside week range (2.73 – 3.05)
STATE: WATCHLIST
SIGNAL: Price +1.47% from 7D avg — monitoring for continuation
REASON: Current price 2.89 is +1.47% vs 7D avg 2.85. 24h change: -4.40%. Trend: MIXED. 24h range: 6.05% vs avg daily range 4.94%.
--- Flow Analyst ---
RSI_14: 46.99
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.016508
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1459
STOP_DIST (ATR×1.5): 0.2188
SUGGESTED_STOP: 2.6722
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.11 | S: 0.09 | 7D_AVG: 0.10
INVALIDATION: Break outside week range (0.09 – 0.11)
STATE: WATCHLIST
SIGNAL: Price +6.47% from 7D avg — monitoring for continuation
REASON: Current price 0.10 is +6.47% vs 7D avg 0.10. 24h change: -1.16%. Trend: MIXED. 24h range: 6.76% vs avg daily range 6.03%.
--- Flow Analyst ---
RSI_14: 56.19
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001786
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0058
STOP_DIST (ATR×1.5): 0.0087
SUGGESTED_STOP: 0.0934
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Break outside week range (0.10 – 0.12)
STATE: WATCHLIST
SIGNAL: Price +1.84% from 7D avg — monitoring for continuation
REASON: Current price 0.11 is +1.84% vs 7D avg 0.11. 24h change: -5.02%. Trend: MIXED. 24h range: 7.04% vs avg daily range 5.86%.
--- Flow Analyst ---
RSI_14: 46.76
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002116
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0070
STOP_DIST (ATR×1.5): 0.0104
SUGGESTED_STOP: 0.1032
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.26 | S: 0.22 | 7D_AVG: 0.24
INVALIDATION: Close above 7D_AVG (0.24)
STATE: WATCHLIST
SIGNAL: Price -1.62% from 7D avg — monitoring for continuation
REASON: Current price 0.23 is -1.62% vs 7D avg 0.24. 24h change: -6.88%. Trend: BEARISH. 24h range: 11.30% vs avg daily range 8.19%.
--- Flow Analyst ---
RSI_14: 53.57
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002073
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0203
STOP_DIST (ATR×1.5): 0.0304
SUGGESTED_STOP: 0.2022
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 351.10 | S: 292.60 | 7D_AVG: 313.43
INVALIDATION: Break outside week range (292.60 – 351.10)
STATE: WATCHLIST
SIGNAL: Price +2.73% from 7D avg — monitoring for continuation
REASON: Current price 322.00 is +2.73% vs 7D avg 313.43. 24h change: -4.51%. Trend: MIXED. 24h range: 9.75% vs avg daily range 7.31%.
--- Flow Analyst ---
RSI_14: 61.62
MACD_TREND: BEARISH
MACD_HISTOGRAM: -2.515873
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 23.9934
STOP_DIST (ATR×1.5): 35.9900
SUGGESTED_STOP: 286.0100
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-09 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.12 | S: 1.70 | 7D_AVG: 1.93
INVALIDATION: Break outside week range (1.70 – 2.12)
STATE: WATCHLIST
SIGNAL: Price +5.13% from 7D avg — monitoring for continuation
REASON: Current price 2.03 is +5.13% vs 7D avg 1.93. 24h change: -1.27%. Trend: MIXED. 24h range: 7.25% vs avg daily range 7.79%.
--- Flow Analyst ---
RSI_14: 64.46
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.020631
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.1333
STOP_DIST (ATR×1.5): 0.2000
SUGGESTED_STOP: 1.8280
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

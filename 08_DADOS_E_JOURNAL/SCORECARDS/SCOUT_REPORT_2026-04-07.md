---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-07
scorecard_date: 2026-04-07
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-07
period_end: 2026-04-07

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
**Date:** 2026-04-07  
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
| BTCUSDT |    68,866.00 | -0.41% | +1.39% | 50.38 | BULLISH | FLAT | 3,463.7995 | **25/35** | BOA | **WATCHLIST** |
| ETHUSDT |     2,114.60 | -0.78% | +1.11% | 52.29 | BULLISH | FALLING | 141.9379 | **26/35** | BOA | **WATCHLIST** |
| SOLUSDT |        79.93 | -2.52% | -1.23% | 40.25 | BEARISH | FLAT | 6.1307 | **22/35** | BOA | **WATCHLIST** |
| BNBUSDT |       600.12 | +0.02% | +0.14% | 41.12 | BEARISH | FLAT | 28.0098 | **19/35** | MEDIA | **NO_TRADE** |
| AVAXUSDT |         8.70 | -8.23% | -2.81% | 42.06 | BEARISH | FALLING | 0.7247 | **22/35** | BOA | **WATCHLIST** |
| DOTUSDT |         1.24 | -1.51% | -0.50% | 34.27 | BEARISH | FALLING | 0.1004 | **18/35** | MEDIA | **NO_TRADE** |
| LINKUSDT |         8.81 | -1.56% | +0.57% | 48.44 | BULLISH | FALLING | 0.6181 | **20/35** | MEDIA | **NO_TRADE** |
| ADAUSDT |         0.25 | -4.55% | -0.21% | 43.56 | BULLISH | FLAT | 0.0198 | **17/35** | MEDIA | **NO_TRADE** |
| XRPUSDT |         1.32 | -1.65% | -0.71% | 39.81 | BEARISH | FLAT | 0.0802 | **20/35** | MEDIA | **NO_TRADE** |
| SUIUSDT |         0.87 | -1.93% | +0.15% | 42.27 | BULLISH | FALLING | 0.0722 | **20/35** | MEDIA | **NO_TRADE** |
| NEARUSDT |         1.24 | -2.90% | +2.01% | 50.05 | BULLISH | FLAT | 0.0985 | **19/35** | MEDIA | **WATCHLIST** |
| INJUSDT |         2.85 | -1.18% | +0.71% | 43.54 | BULLISH | RISING | 0.2098 | **19/35** | MEDIA | **NO_TRADE** |
| ARBUSDT |         0.09 | -1.57% | +1.15% | 46.04 | BULLISH | FLAT | 0.0077 | **21/35** | BOA | **WATCHLIST** |
| OPUSDT |         0.11 | -2.05% | +0.17% | 41.07 | BULLISH | FLAT | 0.0099 | **15/35** | MEDIA | **NO_TRADE** |
| FETUSDT |         0.23 | -4.33% | -1.66% | 54.52 | BEARISH | FALLING | 0.0291 | **22/35** | BOA | **WATCHLIST** |
| TAOUSDT |       312.50 | -1.88% | +1.87% | 61.76 | BEARISH | RISING | 34.2645 | **22/35** | BOA | **WATCHLIST** |
| RENDERUSDT |         1.88 | -5.67% | +1.51% | 59.51 | BULLISH | FALLING | 0.1849 | **20/35** | MEDIA | **WATCHLIST** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | ETHUSDT | **26/35** (74%) | **BOA** | 5 | 5 | 2 | 5 | 2 | 5 | 2 |
| 2 | BTCUSDT | **25/35** (71%) | **BOA** | 5 | 4 | 2 | 5 | 3 | 5 | 1 |
| 3 | SOLUSDT | **22/35** (63%) | **BOA** | 4 | 2 | 2 | 5 | 1 | 5 | 3 |
| 4 | AVAXUSDT | **22/35** (63%) | **BOA** | 3 | 5 | 2 | 4 | 0 | 5 | 3 |
| 5 | FETUSDT | **22/35** (63%) | **BOA** | 2 | 4 | 2 | 5 | 1 | 5 | 3 |
| 6 | TAOUSDT | **22/35** (63%) | **BOA** | 3 | 4 | 2 | 5 | 2 | 5 | 1 |
| 7 | ARBUSDT | **21/35** (60%) | **BOA** | 2 | 5 | 2 | 4 | 2 | 5 | 1 |
| 8 | LINKUSDT | **20/35** (57%) | **MEDIA** | 2 | 5 | 0 | 4 | 2 | 5 | 2 |
| 9 | XRPUSDT | **20/35** (57%) | **MEDIA** | 4 | 3 | 0 | 4 | 2 | 5 | 2 |
| 10 | SUIUSDT | **20/35** (57%) | **MEDIA** | 3 | 5 | 0 | 4 | 2 | 5 | 1 |
| 11 | RENDERUSDT | **20/35** (57%) | **MEDIA** | 2 | 3 | 2 | 5 | 0 | 5 | 3 |
| 12 | BNBUSDT | **19/35** (54%) | **MEDIA** | 3 | 2 | 0 | 4 | 3 | 5 | 2 |
| 13 | NEARUSDT | **19/35** (54%) | **MEDIA** | 2 | 4 | 2 | 3 | 1 | 5 | 2 |
| 14 | INJUSDT | **19/35** (54%) | **MEDIA** | 1 | 5 | 0 | 4 | 2 | 5 | 2 |
| 15 | DOTUSDT | **18/35** (51%) | **MEDIA** | 2 | 4 | 0 | 3 | 2 | 5 | 2 |
| 16 | ADAUSDT | **17/35** (49%) | **MEDIA** | 3 | 3 | 0 | 3 | 1 | 5 | 2 |
| 17 | OPUSDT | **15/35** (43%) | **MEDIA** | 1 | 2 | 0 | 4 | 2 | 5 | 1 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-07 05:00 UTC
OVERALL_SEVERITY: HIGH
TOP_HEADLINES:
  1. [HIGH] Iran war bets turn prediction markets into real-time macro radar: Sygnum
  2. [LOW] Crypto market safe harbor lands at White House for review
  3. [LOW] New evidence in Libra probe renews questions about Milei involvement
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 70,351.46 | S: 65,712.12 | 7D_AVG: 67,921.85
INVALIDATION: Break outside week range (65,712.12 – 70,351.46)
STATE: WATCHLIST
SIGNAL: Price +1.39% from 7D avg — monitoring for continuation
REASON: Current price 68,866.00 is +1.39% vs 7D avg 67,921.85. 24h change: -0.41%. Trend: MIXED. 24h range: 3.02% vs avg daily range 2.88%.
--- Flow Analyst ---
RSI_14: 50.38
MACD_TREND: BULLISH
MACD_HISTOGRAM: 151.175649
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 2309.1996
STOP_DIST (ATR×1.5): 3,463.7995
SUGGESTED_STOP: 65,402.2005
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,174.79 | S: 2,012.64 | 7D_AVG: 2,091.38
INVALIDATION: Break outside week range (2,012.64 – 2,174.79)
STATE: WATCHLIST
SIGNAL: Price +1.11% from 7D avg — monitoring for continuation
REASON: Current price 2,114.60 is +1.11% vs 7D avg 2,091.38. 24h change: -0.78%. Trend: MIXED. 24h range: 4.13% vs avg daily range 4.16%.
--- Flow Analyst ---
RSI_14: 52.29
MACD_TREND: BULLISH
MACD_HISTOGRAM: 4.522293
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 94.6253
STOP_DIST (ATR×1.5): 141.9379
SUGGESTED_STOP: 1,972.5721
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 86.65 | S: 76.70 | 7D_AVG: 80.92
INVALIDATION: Close above 7D_AVG (80.92)
STATE: WATCHLIST
SIGNAL: Price -1.23% from 7D avg — monitoring for continuation
REASON: Current price 79.93 is -1.23% vs 7D avg 80.92. 24h change: -2.52%. Trend: BEARISH. 24h range: 4.78% vs avg daily range 4.73%.
--- Flow Analyst ---
RSI_14: 40.25
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.384572
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 4.0871
STOP_DIST (ATR×1.5): 6.1307
SUGGESTED_STOP: 73.8093
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 621.90 | S: 570.31 | 7D_AVG: 599.29
INVALIDATION: Break outside week range (570.31 – 621.90)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 600.12 is +0.14% vs 7D avg 599.29. 24h change: +0.02%. Trend: SIDEWAYS. 24h range: 2.34% vs avg daily range 3.00%.
--- Flow Analyst ---
RSI_14: 41.12
MACD_TREND: BEARISH
MACD_HISTOGRAM: -1.134427
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 18.6732
STOP_DIST (ATR×1.5): 28.0098
SUGGESTED_STOP: 572.1102
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: BEARISH
STRUCTURE: AT_WEEKLY_LOW — support zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.66 | S: 8.62 | 7D_AVG: 8.95
INVALIDATION: Close above 7D_AVG (8.95)
STATE: WATCHLIST
SIGNAL: Price -2.81% from 7D avg — monitoring for continuation
REASON: Current price 8.70 is -2.81% vs 7D avg 8.95. 24h change: -8.23%. Trend: BEARISH. 24h range: 10.46% vs avg daily range 5.53%.
--- Flow Analyst ---
RSI_14: 42.06
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.014856
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.4831
STOP_DIST (ATR×1.5): 0.7247
SUGGESTED_STOP: 7.9753
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.32 | S: 1.20 | 7D_AVG: 1.25
INVALIDATION: Break outside week range (1.20 – 1.32)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.24 is -0.50% vs 7D avg 1.25. 24h change: -1.51%. Trend: SIDEWAYS. 24h range: 6.94% vs avg daily range 4.37%.
--- Flow Analyst ---
RSI_14: 34.27
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002465
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.0669
STOP_DIST (ATR×1.5): 0.1004
SUGGESTED_STOP: 1.1396
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.20 | S: 8.42 | 7D_AVG: 8.76
INVALIDATION: Break outside week range (8.42 – 9.20)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.81 is +0.57% vs 7D avg 8.76. 24h change: -1.56%. Trend: SIDEWAYS. 24h range: 4.88% vs avg daily range 4.33%.
--- Flow Analyst ---
RSI_14: 48.44
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.012370
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.4120
STOP_DIST (ATR×1.5): 0.6181
SUGGESTED_STOP: 8.1919
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.26 | S: 0.23 | 7D_AVG: 0.25
INVALIDATION: Break outside week range (0.23 – 0.26)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.25 is -0.21% vs 7D avg 0.25. 24h change: -4.55%. Trend: SIDEWAYS. 24h range: 6.77% vs avg daily range 5.26%.
--- Flow Analyst ---
RSI_14: 43.56
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000463
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0132
STOP_DIST (ATR×1.5): 0.0198
SUGGESTED_STOP: 0.2255
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.37 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Break outside week range (1.28 – 1.37)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.32 is -0.71% vs 7D avg 1.33. 24h change: -1.65%. Trend: SIDEWAYS. 24h range: 3.45% vs avg daily range 3.31%.
--- Flow Analyst ---
RSI_14: 39.81
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002064
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0535
STOP_DIST (ATR×1.5): 0.0802
SUGGESTED_STOP: 1.2375
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.92 | S: 0.84 | 7D_AVG: 0.87
INVALIDATION: Break outside week range (0.84 – 0.92)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.87 is +0.15% vs 7D avg 0.87. 24h change: -1.93%. Trend: SIDEWAYS. 24h range: 6.86% vs avg daily range 4.38%.
--- Flow Analyst ---
RSI_14: 42.27
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000134
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.0482
STOP_DIST (ATR×1.5): 0.0722
SUGGESTED_STOP: 0.8018
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.30 | S: 1.14 | 7D_AVG: 1.21
INVALIDATION: Break outside week range (1.14 – 1.30)
STATE: WATCHLIST
SIGNAL: Price +2.01% from 7D avg — monitoring for continuation
REASON: Current price 1.24 is +2.01% vs 7D avg 1.21. 24h change: -2.90%. Trend: MIXED. 24h range: 5.81% vs avg daily range 4.99%.
--- Flow Analyst ---
RSI_14: 50.05
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002079
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0656
STOP_DIST (ATR×1.5): 0.0985
SUGGESTED_STOP: 1.1405
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.98 | S: 2.73 | 7D_AVG: 2.83
INVALIDATION: Break outside week range (2.73 – 2.98)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2.85 is +0.71% vs 7D avg 2.83. 24h change: -1.18%. Trend: SIDEWAYS. 24h range: 5.91% vs avg daily range 3.95%.
--- Flow Analyst ---
RSI_14: 43.54
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.003152
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1399
STOP_DIST (ATR×1.5): 0.2098
SUGGESTED_STOP: 2.6352
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.10 | S: 0.09 | 7D_AVG: 0.09
INVALIDATION: Break outside week range (0.09 – 0.10)
STATE: WATCHLIST
SIGNAL: Price +1.15% from 7D avg — monitoring for continuation
REASON: Current price 0.09 is +1.15% vs 7D avg 0.09. 24h change: -1.57%. Trend: MIXED. 24h range: 6.80% vs avg daily range 4.85%.
--- Flow Analyst ---
RSI_14: 46.04
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000657
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0051
STOP_DIST (ATR×1.5): 0.0077
SUGGESTED_STOP: 0.0864
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Break outside week range (0.10 – 0.12)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.11 is +0.17% vs 7D avg 0.11. 24h change: -2.05%. Trend: SIDEWAYS. 24h range: 6.19% vs avg daily range 5.02%.
--- Flow Analyst ---
RSI_14: 41.07
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001573
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0066
STOP_DIST (ATR×1.5): 0.0099
SUGGESTED_STOP: 0.1000
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.25 | S: 0.22 | 7D_AVG: 0.23
INVALIDATION: Close above 7D_AVG (0.23)
STATE: WATCHLIST
SIGNAL: Price -1.66% from 7D avg — monitoring for continuation
REASON: Current price 0.23 is -1.66% vs 7D avg 0.23. 24h change: -4.33%. Trend: BEARISH. 24h range: 7.96% vs avg daily range 7.23%.
--- Flow Analyst ---
RSI_14: 54.52
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002905
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0194
STOP_DIST (ATR×1.5): 0.0291
SUGGESTED_STOP: 0.2008
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 330.10 | S: 292.60 | 7D_AVG: 306.77
INVALIDATION: Break outside week range (292.60 – 330.10)
STATE: WATCHLIST
SIGNAL: Price +1.87% from 7D avg — monitoring for continuation
REASON: Current price 312.50 is +1.87% vs 7D avg 306.77. 24h change: -1.88%. Trend: MIXED. 24h range: 6.85% vs avg daily range 6.49%.
--- Flow Analyst ---
RSI_14: 61.76
MACD_TREND: BEARISH
MACD_HISTOGRAM: -4.189651
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 22.8430
STOP_DIST (ATR×1.5): 34.2645
SUGGESTED_STOP: 278.2355
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-07 05:00 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.00 | S: 1.66 | 7D_AVG: 1.85
INVALIDATION: Break outside week range (1.66 – 2.00)
STATE: WATCHLIST
SIGNAL: Price +1.51% from 7D avg — monitoring for continuation
REASON: Current price 1.88 is +1.51% vs 7D avg 1.85. 24h change: -5.67%. Trend: MIXED. 24h range: 8.20% vs avg daily range 6.45%.
--- Flow Analyst ---
RSI_14: 59.51
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.008112
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.1233
STOP_DIST (ATR×1.5): 0.1849
SUGGESTED_STOP: 1.6941
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

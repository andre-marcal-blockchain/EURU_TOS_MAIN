---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-11
scorecard_date: 2026-04-11
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-11
period_end: 2026-04-11

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
**Date:** 2026-04-11  
**Time:** 07:32 UTC  
**Assets scanned:** 17  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** INACTIVE — BTC trend is BULLISH; altcoin signals unmodified  

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
| BTCUSDT |    72,792.73 | +1.48% | +3.37% | 60.51 | BULLISH | RISING | 3,591.2566 | **26/35** | BOA | **SETUP** |
| ETHUSDT |     2,235.09 | +2.17% | +3.28% | 59.16 | BULLISH | RISING | 147.0517 | **26/35** | BOA | **SETUP** |
| SOLUSDT |        84.29 | +1.30% | +1.90% | 49.54 | BULLISH | RISING | 6.3297 | **22/35** | BOA | **WATCHLIST** |
| BNBUSDT |       606.20 | +0.92% | +0.44% | 45.40 | BULLISH | RISING | 28.0290 | **18/35** | MEDIA | **NO_TRADE** |
| AVAXUSDT |         9.29 | +0.00% | +1.29% | 51.43 | BULLISH | RISING | 0.7729 | **18/35** | MEDIA | **WATCHLIST** |
| DOTUSDT |         1.28 | -0.77% | +0.52% | 43.43 | BULLISH | RISING | 0.1091 | **16/35** | MEDIA | **NO_TRADE** |
| LINKUSDT |         9.01 | +0.90% | +0.91% | 51.56 | BULLISH | RISING | 0.6528 | **18/35** | MEDIA | **NO_TRADE** |
| ADAUSDT |         0.25 | -0.12% | -0.78% | 47.04 | BULLISH | FLAT | 0.0206 | **19/35** | MEDIA | **NO_TRADE** |
| XRPUSDT |         1.35 | +0.51% | +0.49% | 46.61 | BULLISH | FLAT | 0.0799 | **19/35** | MEDIA | **NO_TRADE** |
| SUIUSDT |         0.93 | +0.03% | +2.66% | 52.14 | BULLISH | FLAT | 0.0801 | **19/35** | MEDIA | **WATCHLIST** |
| NEARUSDT |         1.34 | -1.33% | +2.64% | 58.95 | BULLISH | RISING | 0.1056 | **17/35** | MEDIA | **WATCHLIST** |
| INJUSDT |         3.00 | +0.81% | +2.88% | 52.20 | BULLISH | RISING | 0.2220 | **21/35** | BOA | **WATCHLIST** |
| ARBUSDT |         0.11 | +4.18% | +12.59% | 68.05 | BULLISH | RISING | 0.0098 | **27/35** | BOA | **SETUP** |
| OPUSDT |         0.11 | -2.34% | -0.78% | 45.44 | BULLISH | FLAT | 0.0100 | **18/35** | MEDIA | **NO_TRADE** |
| FETUSDT |         0.24 | -0.51% | -1.31% | 54.35 | BEARISH | FALLING | 0.0292 | **22/35** | BOA | **WATCHLIST** |
| TAOUSDT |       261.50 | -1.47% | -14.77% | 41.77 | BEARISH | FALLING | 41.5866 | **28/35** | PREMIUM | **SETUP** |
| RENDERUSDT |         2.00 | -2.34% | +2.14% | 62.32 | BULLISH | FALLING | 0.1918 | **19/35** | MEDIA | **WATCHLIST** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | TAOUSDT | **28/35** (80%) | **PREMIUM** | 4 | 3 | 5 | 5 | 1 | 5 | 5 |
| 2 | ARBUSDT | **27/35** (77%) | **BOA** | 2 | 5 | 5 | 4 | 4 | 5 | 2 |
| 3 | BTCUSDT | **26/35** (74%) | **BOA** | 5 | 3 | 4 | 5 | 3 | 5 | 1 |
| 4 | ETHUSDT | **26/35** (74%) | **BOA** | 5 | 3 | 4 | 5 | 3 | 5 | 1 |
| 5 | SOLUSDT | **22/35** (63%) | **BOA** | 4 | 2 | 2 | 5 | 2 | 5 | 2 |
| 6 | FETUSDT | **22/35** (63%) | **BOA** | 2 | 2 | 2 | 5 | 2 | 5 | 4 |
| 7 | INJUSDT | **21/35** (60%) | **BOA** | 1 | 5 | 2 | 4 | 2 | 5 | 2 |
| 8 | ADAUSDT | **19/35** (54%) | **MEDIA** | 3 | 3 | 0 | 3 | 2 | 5 | 3 |
| 9 | XRPUSDT | **19/35** (54%) | **MEDIA** | 4 | 2 | 0 | 4 | 2 | 5 | 2 |
| 10 | SUIUSDT | **19/35** (54%) | **MEDIA** | 2 | 2 | 2 | 4 | 2 | 5 | 2 |
| 11 | RENDERUSDT | **19/35** (54%) | **MEDIA** | 2 | 2 | 2 | 5 | 1 | 5 | 2 |
| 12 | BNBUSDT | **18/35** (51%) | **MEDIA** | 3 | 2 | 0 | 4 | 2 | 5 | 2 |
| 13 | AVAXUSDT | **18/35** (51%) | **MEDIA** | 2 | 1 | 2 | 4 | 2 | 5 | 2 |
| 14 | LINKUSDT | **18/35** (51%) | **MEDIA** | 2 | 2 | 0 | 4 | 2 | 5 | 3 |
| 15 | OPUSDT | **18/35** (51%) | **MEDIA** | 1 | 4 | 0 | 4 | 1 | 5 | 3 |
| 16 | NEARUSDT | **17/35** (49%) | **MEDIA** | 2 | 2 | 2 | 3 | 1 | 5 | 2 |
| 17 | DOTUSDT | **16/35** (46%) | **MEDIA** | 2 | 3 | 0 | 3 | 1 | 5 | 2 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-11 07:32 UTC
OVERALL_SEVERITY: LOW
TOP_HEADLINES:
  1. [LOW] Bitwise edges closer to Hyperliquid ETF launch with second amended filing
  2. [LOW] XRP price bottom signals emerge after the altcoin holds key support level
  3. [LOW] CFTC unveils innovation task force members in crypto clarity push
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 73,434.00 | S: 66,611.66 | 7D_AVG: 70,419.01
INVALIDATION: Close below 7D_AVG (70,419.01)
STATE: SETUP
SIGNAL: Price +3.37% from 7D avg with aligned trend
REASON: Current price 72,792.73 is +3.37% vs 7D avg 70,419.01. 24h change: +1.48%. Trend: BULLISH. 24h range: 2.76% vs avg daily range 3.47%.
--- Flow Analyst ---
RSI_14: 60.51
MACD_TREND: BULLISH
MACD_HISTOGRAM: 653.816487
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 2394.1710
STOP_DIST (ATR×1.5): 3,591.2566
SUGGESTED_STOP: 69,201.4734
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,273.87 | S: 2,021.50 | 7D_AVG: 2,164.02
INVALIDATION: Close below 7D_AVG (2,164.02)
STATE: SETUP
SIGNAL: Price +3.28% from 7D avg with aligned trend
REASON: Current price 2,235.09 is +3.28% vs 7D avg 2,164.02. 24h change: +2.17%. Trend: BULLISH. 24h range: 3.65% vs avg daily range 4.61%.
--- Flow Analyst ---
RSI_14: 59.16
MACD_TREND: BULLISH
MACD_HISTOGRAM: 18.850471
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 98.0345
STOP_DIST (ATR×1.5): 147.0517
SUGGESTED_STOP: 2,088.0483
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 87.02 | S: 78.38 | 7D_AVG: 82.72
INVALIDATION: Close below 7D_AVG (82.72)
STATE: WATCHLIST
SIGNAL: Price +1.90% from 7D avg — monitoring for continuation
REASON: Current price 84.29 is +1.90% vs 7D avg 82.72. 24h change: +1.30%. Trend: BULLISH. 24h range: 3.52% vs avg daily range 5.00%.
--- Flow Analyst ---
RSI_14: 49.54
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.437302
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 4.2198
STOP_DIST (ATR×1.5): 6.3297
SUGGESTED_STOP: 77.9603
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 624.85 | S: 587.10 | 7D_AVG: 603.54
INVALIDATION: Break outside week range (587.10 – 624.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 606.20 is +0.44% vs 7D avg 603.54. 24h change: +0.92%. Trend: SIDEWAYS. 24h range: 2.13% vs avg daily range 2.90%.
--- Flow Analyst ---
RSI_14: 45.40
MACD_TREND: BULLISH
MACD_HISTOGRAM: 1.373539
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 18.6860
STOP_DIST (ATR×1.5): 28.0290
SUGGESTED_STOP: 578.1710
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.70 | S: 8.46 | 7D_AVG: 9.17
INVALIDATION: Break outside week range (8.46 – 9.70)
STATE: WATCHLIST
SIGNAL: Price +1.29% from 7D avg — monitoring for continuation
REASON: Current price 9.29 is +1.29% vs 7D avg 9.17. 24h change: +0.00%. Trend: MIXED. 24h range: 3.55% vs avg daily range 6.60%.
--- Flow Analyst ---
RSI_14: 51.43
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.059921
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.5153
STOP_DIST (ATR×1.5): 0.7729
SUGGESTED_STOP: 8.5171
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 1.36 | S: 1.21 | 7D_AVG: 1.28
INVALIDATION: Break outside week range (1.21 – 1.36)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.28 is +0.52% vs 7D avg 1.28. 24h change: -0.77%. Trend: SIDEWAYS. 24h range: 4.13% vs avg daily range 6.00%.
--- Flow Analyst ---
RSI_14: 43.43
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.010636
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.0727
STOP_DIST (ATR×1.5): 0.1091
SUGGESTED_STOP: 1.1729
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.42 | S: 8.47 | 7D_AVG: 8.93
INVALIDATION: Break outside week range (8.47 – 9.42)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 9.01 is +0.91% vs 7D avg 8.93. 24h change: +0.90%. Trend: SIDEWAYS. 24h range: 3.33% vs avg daily range 5.02%.
--- Flow Analyst ---
RSI_14: 51.56
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.045236
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.4352
STOP_DIST (ATR×1.5): 0.6528
SUGGESTED_STOP: 8.3572
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.27 | S: 0.24 | 7D_AVG: 0.25
INVALIDATION: Break outside week range (0.24 – 0.27)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.25 is -0.78% vs 7D avg 0.25. 24h change: -0.12%. Trend: SIDEWAYS. 24h range: 3.71% vs avg daily range 5.44%.
--- Flow Analyst ---
RSI_14: 47.04
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001527
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0137
STOP_DIST (ATR×1.5): 0.0206
SUGGESTED_STOP: 0.2298
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 1.40 | S: 1.28 | 7D_AVG: 1.34
INVALIDATION: Break outside week range (1.28 – 1.40)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.35 is +0.49% vs 7D avg 1.34. 24h change: +0.51%. Trend: SIDEWAYS. 24h range: 2.32% vs avg daily range 3.67%.
--- Flow Analyst ---
RSI_14: 46.61
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.004785
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0533
STOP_DIST (ATR×1.5): 0.0799
SUGGESTED_STOP: 1.2671
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.98 | S: 0.84 | 7D_AVG: 0.91
INVALIDATION: Close below 7D_AVG (0.91)
STATE: WATCHLIST
SIGNAL: Price +2.66% from 7D avg — monitoring for continuation
REASON: Current price 0.93 is +2.66% vs 7D avg 0.91. 24h change: +0.03%. Trend: BULLISH. 24h range: 4.12% vs avg daily range 6.33%.
--- Flow Analyst ---
RSI_14: 52.14
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.010193
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0534
STOP_DIST (ATR×1.5): 0.0801
SUGGESTED_STOP: 0.8529
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.40 | S: 1.21 | 7D_AVG: 1.30
INVALIDATION: Break outside week range (1.21 – 1.40)
STATE: WATCHLIST
SIGNAL: Price +2.64% from 7D avg — monitoring for continuation
REASON: Current price 1.34 is +2.64% vs 7D avg 1.30. 24h change: -1.33%. Trend: MIXED. 24h range: 4.79% vs avg daily range 5.93%.
--- Flow Analyst ---
RSI_14: 58.95
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.016563
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0704
STOP_DIST (ATR×1.5): 0.1056
SUGGESTED_STOP: 1.2314
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 3.09 | S: 2.74 | 7D_AVG: 2.92
INVALIDATION: Close below 7D_AVG (2.92)
STATE: WATCHLIST
SIGNAL: Price +2.88% from 7D avg — monitoring for continuation
REASON: Current price 3.00 is +2.88% vs 7D avg 2.92. 24h change: +0.81%. Trend: BULLISH. 24h range: 4.20% vs avg daily range 4.95%.
--- Flow Analyst ---
RSI_14: 52.20
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.030297
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.1480
STOP_DIST (ATR×1.5): 0.2220
SUGGESTED_STOP: 2.7790
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.09 | 7D_AVG: 0.10
INVALIDATION: Close below 7D_AVG (0.10)
STATE: SETUP
SIGNAL: Price +12.59% from 7D avg with aligned trend
REASON: Current price 0.11 is +12.59% vs 7D avg 0.10. 24h change: +4.18%. Trend: BULLISH. 24h range: 12.39% vs avg daily range 6.89%.
--- Flow Analyst ---
RSI_14: 68.05
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.003085
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0065
STOP_DIST (ATR×1.5): 0.0098
SUGGESTED_STOP: 0.1048
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.11 | 7D_AVG: 0.11
INVALIDATION: Break outside week range (0.11 – 0.12)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.11 is -0.78% vs 7D avg 0.11. 24h change: -2.34%. Trend: SIDEWAYS. 24h range: 3.91% vs avg daily range 5.29%.
--- Flow Analyst ---
RSI_14: 45.44
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001862
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0066
STOP_DIST (ATR×1.5): 0.0100
SUGGESTED_STOP: 0.1025
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.26 | S: 0.22 | 7D_AVG: 0.24
INVALIDATION: Close above 7D_AVG (0.24)
STATE: WATCHLIST
SIGNAL: Price -1.31% from 7D avg — monitoring for continuation
REASON: Current price 0.24 is -1.31% vs 7D avg 0.24. 24h change: -0.51%. Trend: BEARISH. 24h range: 4.15% vs avg daily range 7.72%.
--- Flow Analyst ---
RSI_14: 54.35
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.001981
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0195
STOP_DIST (ATR×1.5): 0.0292
SUGGESTED_STOP: 0.2067
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 351.10 | S: 248.90 | 7D_AVG: 306.81
INVALIDATION: Close above 7D_AVG (306.81)
STATE: SETUP
SIGNAL: Price -14.77% from 7D avg with aligned trend
REASON: Current price 261.50 is -14.77% vs 7D avg 306.81. 24h change: -1.47%. Trend: BEARISH. 24h range: 8.11% vs avg daily range 10.48%.
--- Flow Analyst ---
RSI_14: 41.77
MACD_TREND: BEARISH
MACD_HISTOGRAM: -9.251780
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 27.7244
STOP_DIST (ATR×1.5): 41.5866
SUGGESTED_STOP: 219.9134
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-11 07:32 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.12 | S: 1.82 | 7D_AVG: 1.96
INVALIDATION: Break outside week range (1.82 – 2.12)
STATE: WATCHLIST
SIGNAL: Price +2.14% from 7D avg — monitoring for continuation
REASON: Current price 2.00 is +2.14% vs 7D avg 1.96. 24h change: -2.34%. Trend: MIXED. 24h range: 4.99% vs avg daily range 6.91%.
--- Flow Analyst ---
RSI_14: 62.32
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.014581
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.1279
STOP_DIST (ATR×1.5): 0.1918
SUGGESTED_STOP: 1.8122
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

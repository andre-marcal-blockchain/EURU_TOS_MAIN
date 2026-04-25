---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-06
scorecard_date: 2026-04-06
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-06
period_end: 2026-04-06

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
**Date:** 2026-04-06  
**Time:** 05:00 UTC  
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
| BTCUSDT |    69,149.47 | +3.03% | +2.25% | 51.32 | BULLISH | RISING | 3,499.0456 | **23/35** | BOA | **WATCHLIST** |
| ETHUSDT |     2,131.28 | +3.70% | +2.47% | 53.54 | BULLISH | RISING | 144.4287 | **22/35** | BOA | **WATCHLIST** |
| SOLUSDT |        81.99 | +2.03% | +0.87% | 43.71 | BEARISH | RISING | 6.2593 | **20/35** | MEDIA | **NO_TRADE** |
| BNBUSDT |       600.00 | +1.16% | -0.10% | 41.07 | BEARISH | RISING | 28.9936 | **18/35** | MEDIA | **NO_TRADE** |
| AVAXUSDT |         9.49 | +6.27% | +6.19% | 54.86 | BULLISH | RISING | 0.7190 | **25/35** | BOA | **SETUP** |
| DOTUSDT |         1.26 | +1.21% | +1.00% | 37.21 | BEARISH | FLAT | 0.0996 | **15/35** | MEDIA | **NO_TRADE** |
| LINKUSDT |         8.96 | +3.70% | +2.60% | 51.15 | BULLISH | RISING | 0.6271 | **18/35** | MEDIA | **WATCHLIST** |
| ADAUSDT |         0.26 | +4.51% | +4.71% | 50.35 | BULLISH | RISING | 0.0203 | **21/35** | BOA | **SETUP** |
| XRPUSDT |         1.34 | +2.19% | +0.91% | 43.96 | BEARISH | FLAT | 0.0824 | **20/35** | MEDIA | **NO_TRADE** |
| SUIUSDT |         0.89 | +3.36% | +2.22% | 45.64 | BULLISH | FLAT | 0.0731 | **20/35** | MEDIA | **WATCHLIST** |
| NEARUSDT |         1.28 | +0.95% | +6.13% | 54.43 | BULLISH | FLAT | 0.1003 | **19/35** | MEDIA | **SETUP** |
| INJUSDT |         2.88 | +3.19% | +1.90% | 45.73 | BULLISH | RISING | 0.2110 | **18/35** | MEDIA | **WATCHLIST** |
| ARBUSDT |         0.10 | +4.48% | +3.28% | 48.60 | BULLISH | RISING | 0.0077 | **22/35** | BOA | **SETUP** |
| OPUSDT |         0.11 | +2.94% | +2.70% | 44.02 | BULLISH | FLAT | 0.0100 | **15/35** | MEDIA | **WATCHLIST** |
| FETUSDT |         0.24 | +4.16% | +2.59% | 59.17 | BEARISH | FLAT | 0.0295 | **21/35** | BOA | **WATCHLIST** |
| TAOUSDT |       318.60 | +5.18% | +3.92% | 63.66 | BEARISH | RISING | 35.0863 | **23/35** | BOA | **SETUP** |
| RENDERUSDT |         1.99 | +4.96% | +9.07% | 65.76 | BULLISH | RISING | 0.1889 | **24/35** | BOA | **SETUP** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | AVAXUSDT | **25/35** (71%) | **BOA** | 2 | 5 | 5 | 4 | 4 | 5 | 0 |
| 2 | RENDERUSDT | **24/35** (69%) | **BOA** | 2 | 4 | 5 | 5 | 3 | 5 | 0 |
| 3 | BTCUSDT | **23/35** (66%) | **BOA** | 5 | 3 | 2 | 5 | 3 | 5 | 0 |
| 4 | TAOUSDT | **23/35** (66%) | **BOA** | 3 | 2 | 4 | 5 | 4 | 5 | 0 |
| 5 | ETHUSDT | **22/35** (63%) | **BOA** | 4 | 2 | 2 | 5 | 3 | 5 | 1 |
| 6 | ARBUSDT | **22/35** (63%) | **BOA** | 1 | 5 | 4 | 4 | 3 | 5 | 0 |
| 7 | ADAUSDT | **21/35** (60%) | **BOA** | 3 | 3 | 4 | 3 | 3 | 5 | 0 |
| 8 | FETUSDT | **21/35** (60%) | **BOA** | 2 | 4 | 2 | 5 | 3 | 5 | 0 |
| 9 | SOLUSDT | **20/35** (57%) | **MEDIA** | 4 | 2 | 0 | 5 | 2 | 5 | 2 |
| 10 | XRPUSDT | **20/35** (57%) | **MEDIA** | 4 | 4 | 0 | 4 | 2 | 5 | 1 |
| 11 | SUIUSDT | **20/35** (57%) | **MEDIA** | 2 | 4 | 2 | 4 | 3 | 5 | 0 |
| 12 | NEARUSDT | **19/35** (54%) | **MEDIA** | 2 | 3 | 5 | 3 | 1 | 5 | 0 |
| 13 | BNBUSDT | **18/35** (51%) | **MEDIA** | 3 | 2 | 0 | 4 | 2 | 5 | 2 |
| 14 | LINKUSDT | **18/35** (51%) | **MEDIA** | 2 | 2 | 2 | 4 | 3 | 5 | 0 |
| 15 | INJUSDT | **18/35** (51%) | **MEDIA** | 1 | 2 | 2 | 4 | 3 | 5 | 1 |
| 16 | DOTUSDT | **15/35** (43%) | **MEDIA** | 2 | 3 | 0 | 3 | 2 | 5 | 0 |
| 17 | OPUSDT | **15/35** (43%) | **MEDIA** | 1 | 1 | 2 | 4 | 2 | 5 | 0 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-06 05:00 UTC
OVERALL_SEVERITY: HIGH
TOP_HEADLINES:
  1. [HIGH] Telegram founder Pavel Durov says Iranian government's ban backfired
  2. [HIGH] Nevada judge extends ban on Kalshi, rejects event contract defense
  3. [HIGH] Bitcoin shorts risk $2.5 billion liquidation at $72K: Are bears in danger?
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 69,310.00 | S: 65,712.12 | 7D_AVG: 67,628.09
INVALIDATION: Close below 7D_AVG (67,628.09)
STATE: WATCHLIST
SIGNAL: Price +2.25% from 7D avg — monitoring for continuation
REASON: Current price 69,149.47 is +2.25% vs 7D avg 67,628.09. 24h change: +3.03%. Trend: BULLISH. 24h range: 4.30% vs avg daily range 2.96%.
--- Flow Analyst ---
RSI_14: 51.32
MACD_TREND: BULLISH
MACD_HISTOGRAM: 108.133462
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 2332.6971
STOP_DIST (ATR×1.5): 3,499.0456
SUGGESTED_STOP: 65,650.4244
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,167.85 | S: 1,980.28 | 7D_AVG: 2,079.85
INVALIDATION: Close below 7D_AVG (2,079.85)
STATE: WATCHLIST
SIGNAL: Price +2.47% from 7D avg — monitoring for continuation
REASON: Current price 2,131.28 is +2.47% vs 7D avg 2,079.85. 24h change: +3.70%. Trend: BULLISH. 24h range: 5.90% vs avg daily range 4.30%.
--- Flow Analyst ---
RSI_14: 53.54
MACD_TREND: BULLISH
MACD_HISTOGRAM: 4.352695
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 96.2858
STOP_DIST (ATR×1.5): 144.4287
SUGGESTED_STOP: 1,986.8713
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 86.65 | S: 76.70 | 7D_AVG: 81.28
INVALIDATION: Break outside week range (76.70 – 86.65)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 81.99 is +0.87% vs 7D avg 81.28. 24h change: +2.03%. Trend: SIDEWAYS. 24h range: 5.43% vs avg daily range 4.75%.
--- Flow Analyst ---
RSI_14: 43.71
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.326043
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 4.1729
STOP_DIST (ATR×1.5): 6.2593
SUGGESTED_STOP: 75.7307
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 621.90 | S: 570.31 | 7D_AVG: 600.60
INVALIDATION: Break outside week range (570.31 – 621.90)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 600.00 is -0.10% vs 7D avg 600.60. 24h change: +1.16%. Trend: SIDEWAYS. 24h range: 3.42% vs avg daily range 3.05%.
--- Flow Analyst ---
RSI_14: 41.07
MACD_TREND: BEARISH
MACD_HISTOGRAM: -1.880049
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 19.3291
STOP_DIST (ATR×1.5): 28.9936
SUGGESTED_STOP: 571.0064
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.48 | S: 8.56 | 7D_AVG: 8.94
INVALIDATION: Close below 7D_AVG (8.94)
STATE: SETUP
SIGNAL: Price +6.19% from 7D avg with aligned trend
REASON: Current price 9.49 is +6.19% vs 7D avg 8.94. 24h change: +6.27%. Trend: BULLISH. 24h range: 9.69% vs avg daily range 5.01%.
--- Flow Analyst ---
RSI_14: 54.86
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.031767
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.4794
STOP_DIST (ATR×1.5): 0.7190
SUGGESTED_STOP: 8.7710
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.30 | S: 1.20 | 7D_AVG: 1.25
INVALIDATION: Break outside week range (1.20 – 1.30)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.26 is +1.00% vs 7D avg 1.25. 24h change: +1.21%. Trend: SIDEWAYS. 24h range: 4.29% vs avg daily range 4.02%.
--- Flow Analyst ---
RSI_14: 37.21
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.003706
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0664
STOP_DIST (ATR×1.5): 0.0996
SUGGESTED_STOP: 1.1594
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.20 | S: 8.40 | 7D_AVG: 8.73
INVALIDATION: Close below 7D_AVG (8.73)
STATE: WATCHLIST
SIGNAL: Price +2.60% from 7D avg — monitoring for continuation
REASON: Current price 8.96 is +2.60% vs 7D avg 8.73. 24h change: +3.70%. Trend: BULLISH. 24h range: 6.25% vs avg daily range 4.52%.
--- Flow Analyst ---
RSI_14: 51.15
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.014700
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.4181
STOP_DIST (ATR×1.5): 0.6271
SUGGESTED_STOP: 8.3229
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.25 | S: 0.23 | 7D_AVG: 0.25
INVALIDATION: Close below 7D_AVG (0.25)
STATE: SETUP
SIGNAL: Price +4.71% from 7D avg with aligned trend
REASON: Current price 0.26 is +4.71% vs 7D avg 0.25. 24h change: +4.51%. Trend: BULLISH. 24h range: 7.55% vs avg daily range 5.16%.
--- Flow Analyst ---
RSI_14: 50.35
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001083
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0135
STOP_DIST (ATR×1.5): 0.0203
SUGGESTED_STOP: 0.2367
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.37 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Break outside week range (1.28 – 1.37)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.34 is +0.91% vs 7D avg 1.33. 24h change: +2.19%. Trend: SIDEWAYS. 24h range: 5.25% vs avg daily range 3.36%.
--- Flow Analyst ---
RSI_14: 43.96
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.001771
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0549
STOP_DIST (ATR×1.5): 0.0824
SUGGESTED_STOP: 1.2573
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.91 | S: 0.84 | 7D_AVG: 0.87
INVALIDATION: Close below 7D_AVG (0.87)
STATE: WATCHLIST
SIGNAL: Price +2.22% from 7D avg — monitoring for continuation
REASON: Current price 0.89 is +2.22% vs 7D avg 0.87. 24h change: +3.36%. Trend: BULLISH. 24h range: 6.88% vs avg daily range 4.26%.
--- Flow Analyst ---
RSI_14: 45.64
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000192
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0487
STOP_DIST (ATR×1.5): 0.0731
SUGGESTED_STOP: 0.8180
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.29 | S: 1.14 | 7D_AVG: 1.20
INVALIDATION: Close below 7D_AVG (1.20)
STATE: SETUP
SIGNAL: Price +6.13% from 7D avg with aligned trend
REASON: Current price 1.28 is +6.13% vs 7D avg 1.20. 24h change: +0.95%. Trend: BULLISH. 24h range: 4.39% vs avg daily range 5.21%.
--- Flow Analyst ---
RSI_14: 54.43
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002559
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0669
STOP_DIST (ATR×1.5): 0.1003
SUGGESTED_STOP: 1.1757
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.96 | S: 2.73 | 7D_AVG: 2.83
INVALIDATION: Close below 7D_AVG (2.83)
STATE: WATCHLIST
SIGNAL: Price +1.90% from 7D avg — monitoring for continuation
REASON: Current price 2.88 is +1.90% vs 7D avg 2.83. 24h change: +3.19%. Trend: BULLISH. 24h range: 5.24% vs avg daily range 3.99%.
--- Flow Analyst ---
RSI_14: 45.73
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001463
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1407
STOP_DIST (ATR×1.5): 0.2110
SUGGESTED_STOP: 2.6690
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.10 | S: 0.09 | 7D_AVG: 0.09
INVALIDATION: Close below 7D_AVG (0.09)
STATE: SETUP
SIGNAL: Price +3.28% from 7D avg with aligned trend
REASON: Current price 0.10 is +3.28% vs 7D avg 0.09. 24h change: +4.48%. Trend: BULLISH. 24h range: 7.42% vs avg daily range 4.83%.
--- Flow Analyst ---
RSI_14: 48.60
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000700
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0051
STOP_DIST (ATR×1.5): 0.0077
SUGGESTED_STOP: 0.0880
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.11 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Close below 7D_AVG (0.11)
STATE: WATCHLIST
SIGNAL: Price +2.70% from 7D avg — monitoring for continuation
REASON: Current price 0.11 is +2.70% vs 7D avg 0.11. 24h change: +2.94%. Trend: BULLISH. 24h range: 6.07% vs avg daily range 5.33%.
--- Flow Analyst ---
RSI_14: 44.02
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001703
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0067
STOP_DIST (ATR×1.5): 0.0100
SUGGESTED_STOP: 0.1021
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.25 | S: 0.22 | 7D_AVG: 0.23
INVALIDATION: Close below 7D_AVG (0.23)
STATE: WATCHLIST
SIGNAL: Price +2.59% from 7D avg — monitoring for continuation
REASON: Current price 0.24 is +2.59% vs 7D avg 0.23. 24h change: +4.16%. Trend: BULLISH. 24h range: 10.65% vs avg daily range 7.20%.
--- Flow Analyst ---
RSI_14: 59.17
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.001823
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0196
STOP_DIST (ATR×1.5): 0.0295
SUGGESTED_STOP: 0.2108
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 335.30 | S: 292.60 | 7D_AVG: 306.57
INVALIDATION: Close below 7D_AVG (306.57)
STATE: SETUP
SIGNAL: Price +3.92% from 7D avg with aligned trend
REASON: Current price 318.60 is +3.92% vs 7D avg 306.57. 24h change: +5.18%. Trend: BULLISH. 24h range: 7.94% vs avg daily range 6.74%.
--- Flow Analyst ---
RSI_14: 63.66
MACD_TREND: BEARISH
MACD_HISTOGRAM: -3.983864
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 23.3909
STOP_DIST (ATR×1.5): 35.0863
SUGGESTED_STOP: 283.5137
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-06 05:00 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.96 | S: 1.65 | 7D_AVG: 1.83
INVALIDATION: Close below 7D_AVG (1.83)
STATE: SETUP
SIGNAL: Price +9.07% from 7D avg with aligned trend
REASON: Current price 1.99 is +9.07% vs 7D avg 1.83. 24h change: +4.96%. Trend: BULLISH. 24h range: 8.69% vs avg daily range 6.33%.
--- Flow Analyst ---
RSI_14: 65.76
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.018211
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1259
STOP_DIST (ATR×1.5): 0.1889
SUGGESTED_STOP: 1.8021
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

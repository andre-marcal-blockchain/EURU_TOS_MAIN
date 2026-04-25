---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-04
scorecard_date: 2026-04-04
period_type: daily
period_ref: 2026-W14
period_start: 2026-04-04
period_end: 2026-04-04

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
**Date:** 2026-04-04  
**Time:** 22:24 UTC  
**Assets scanned:** 17  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC trend is SIDEWAYS; altcoin SETUP signals downgraded to WATCHLIST  

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
| BTCUSDT |    67,419.07 | +0.79% | +0.53% | 45.42 | BEARISH | FALLING | 3,665.3028 | **21/35** | BOA | **NO_TRADE** |
| ETHUSDT |     2,071.52 | +0.80% | +0.96% | 48.87 | BEARISH | FALLING | 151.1045 | **21/35** | BOA | **NO_TRADE** |
| SOLUSDT |        80.92 | +0.79% | -0.59% | 41.29 | BEARISH | FALLING | 6.6788 | **19/35** | MEDIA | **NO_TRADE** |
| BNBUSDT |       594.46 | +1.12% | -1.55% | 38.31 | BEARISH | FALLING | 30.5490 | **21/35** | BOA | **WATCHLIST** |
| AVAXUSDT |         8.99 | +0.67% | +1.73% | 46.54 | BEARISH | RISING | 0.7189 | **18/35** | MEDIA | **WATCHLIST** |
| DOTUSDT |         1.25 | +0.97% | +0.19% | 35.28 | BEARISH | FLAT | 0.1063 | **14/35** | MEDIA | **NO_TRADE** |
| LINKUSDT |         8.72 | +0.46% | +0.93% | 46.61 | BEARISH | FLAT | 0.6549 | **16/35** | MEDIA | **NO_TRADE** |
| ADAUSDT |         0.25 | +0.12% | +1.69% | 44.59 | BEARISH | FLAT | 0.0212 | **16/35** | MEDIA | **WATCHLIST** |
| XRPUSDT |         1.32 | -0.14% | -1.00% | 38.98 | BEARISH | FALLING | 0.0865 | **17/35** | MEDIA | **NO_TRADE** |
| SUIUSDT |         0.87 | -0.22% | +0.74% | 41.83 | BEARISH | FLAT | 0.0772 | **16/35** | MEDIA | **NO_TRADE** |
| NEARUSDT |         1.26 | +4.06% | +6.57% | 52.20 | BEARISH | RISING | 0.1068 | **24/35** | BOA | **WATCHLIST** |
| INJUSDT |         2.82 | +0.28% | -0.27% | 41.60 | BEARISH | FALLING | 0.2263 | **15/35** | MEDIA | **NO_TRADE** |
| ARBUSDT |         0.09 | +0.32% | +1.61% | 43.72 | BULLISH | FLAT | 0.0080 | **18/35** | MEDIA | **WATCHLIST** |
| OPUSDT |         0.11 | -0.45% | +3.36% | 41.45 | BULLISH | FLAT | 0.0107 | **16/35** | MEDIA | **WATCHLIST** |
| FETUSDT |         0.24 | +0.64% | +1.18% | 57.75 | BEARISH | FLAT | 0.0309 | **19/35** | MEDIA | **WATCHLIST** |
| TAOUSDT |       304.40 | -1.23% | -1.59% | 59.66 | BEARISH | RISING | 36.8336 | **19/35** | MEDIA | **WATCHLIST** |
| RENDERUSDT |         1.88 | -2.90% | +6.81% | 60.59 | BULLISH | RISING | 0.1959 | **19/35** | MEDIA | **WATCHLIST** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | NEARUSDT | **24/35** (69%) | **BOA** | 2 | 5 | 5 | 3 | 4 | 5 | 0 |
| 2 | BTCUSDT | **21/35** (60%) | **BOA** | 5 | 1 | 0 | 5 | 3 | 5 | 2 |
| 3 | ETHUSDT | **21/35** (60%) | **BOA** | 4 | 1 | 0 | 5 | 3 | 5 | 3 |
| 4 | BNBUSDT | **21/35** (60%) | **BOA** | 3 | 1 | 2 | 4 | 3 | 5 | 3 |
| 5 | SOLUSDT | **19/35** (54%) | **MEDIA** | 4 | 1 | 0 | 5 | 2 | 5 | 2 |
| 6 | FETUSDT | **19/35** (54%) | **MEDIA** | 2 | 1 | 2 | 5 | 2 | 5 | 2 |
| 7 | TAOUSDT | **19/35** (54%) | **MEDIA** | 2 | 1 | 2 | 5 | 1 | 5 | 3 |
| 8 | RENDERUSDT | **19/35** (54%) | **MEDIA** | 1 | 1 | 3 | 5 | 1 | 5 | 3 |
| 9 | AVAXUSDT | **18/35** (51%) | **MEDIA** | 2 | 1 | 2 | 4 | 2 | 5 | 2 |
| 10 | ARBUSDT | **18/35** (51%) | **MEDIA** | 1 | 2 | 2 | 4 | 2 | 5 | 2 |
| 11 | XRPUSDT | **17/35** (49%) | **MEDIA** | 3 | 1 | 0 | 4 | 2 | 5 | 2 |
| 12 | LINKUSDT | **16/35** (46%) | **MEDIA** | 2 | 1 | 0 | 4 | 2 | 5 | 2 |
| 13 | ADAUSDT | **16/35** (46%) | **MEDIA** | 2 | 1 | 2 | 3 | 2 | 5 | 1 |
| 14 | SUIUSDT | **16/35** (46%) | **MEDIA** | 2 | 1 | 0 | 4 | 2 | 5 | 2 |
| 15 | OPUSDT | **16/35** (46%) | **MEDIA** | 1 | 1 | 2 | 4 | 2 | 5 | 1 |
| 16 | INJUSDT | **15/35** (43%) | **MEDIA** | 1 | 1 | 0 | 4 | 2 | 5 | 2 |
| 17 | DOTUSDT | **14/35** (40%) | **MEDIA** | 1 | 1 | 0 | 3 | 3 | 5 | 1 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-04 22:24 UTC
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
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 69,310.00 | S: 65,000.00 | 7D_AVG: 67,064.29
INVALIDATION: Break outside week range (65,000.00 – 69,310.00)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 67,419.07 is +0.53% vs 7D avg 67,064.29. 24h change: +0.79%. Trend: SIDEWAYS. 24h range: 1.17% vs avg daily range 3.03%.
--- Flow Analyst ---
RSI_14: 45.42
MACD_TREND: BEARISH
MACD_HISTOGRAM: -158.296732
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 2443.5352
STOP_DIST (ATR×1.5): 3,665.3028
SUGGESTED_STOP: 63,753.7672
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 2,167.85 | S: 1,938.82 | 7D_AVG: 2,051.81
INVALIDATION: Break outside week range (1,938.82 – 2,167.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2,071.52 is +0.96% vs 7D avg 2,051.81. 24h change: +0.80%. Trend: SIDEWAYS. 24h range: 1.90% vs avg daily range 4.38%.
--- Flow Analyst ---
RSI_14: 48.87
MACD_TREND: BEARISH
MACD_HISTOGRAM: -2.498522
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 100.7363
STOP_DIST (ATR×1.5): 151.1045
SUGGESTED_STOP: 1,920.4155
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 86.65 | S: 76.70 | 7D_AVG: 81.40
INVALIDATION: Break outside week range (76.70 – 86.65)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 80.92 is -0.59% vs 7D avg 81.40. 24h change: +0.79%. Trend: SIDEWAYS. 24h range: 2.52% vs avg daily range 4.97%.
--- Flow Analyst ---
RSI_14: 41.29
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.702273
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 4.4525
STOP_DIST (ATR×1.5): 6.6788
SUGGESTED_STOP: 74.2412
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: MIXED
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 621.90 | S: 570.31 | 7D_AVG: 603.79
INVALIDATION: Break outside week range (570.31 – 621.90)
STATE: WATCHLIST
SIGNAL: Price -1.55% from 7D avg — monitoring for continuation
REASON: Current price 594.46 is -1.55% vs 7D avg 603.79. 24h change: +1.12%. Trend: MIXED. 24h range: 1.61% vs avg daily range 3.08%.
--- Flow Analyst ---
RSI_14: 38.31
MACD_TREND: BEARISH
MACD_HISTOGRAM: -3.771871
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 20.3660
STOP_DIST (ATR×1.5): 30.5490
SUGGESTED_STOP: 563.9110
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.48 | S: 8.37 | 7D_AVG: 8.84
INVALIDATION: Close below 7D_AVG (8.84)
STATE: WATCHLIST
SIGNAL: Price +1.73% from 7D avg — monitoring for continuation
REASON: Current price 8.99 is +1.73% vs 7D avg 8.84. 24h change: +0.67%. Trend: BULLISH. 24h range: 3.11% vs avg daily range 5.23%.
--- Flow Analyst ---
RSI_14: 46.54
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.026692
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.4792
STOP_DIST (ATR×1.5): 0.7189
SUGGESTED_STOP: 8.2711
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 1.31 | S: 1.20 | 7D_AVG: 1.25
INVALIDATION: Break outside week range (1.20 – 1.31)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.25 is +0.19% vs 7D avg 1.25. 24h change: +0.97%. Trend: SIDEWAYS. 24h range: 2.56% vs avg daily range 4.26%.
--- Flow Analyst ---
RSI_14: 35.28
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.010731
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0709
STOP_DIST (ATR×1.5): 0.1063
SUGGESTED_STOP: 1.1457
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.20 | S: 8.20 | 7D_AVG: 8.64
INVALIDATION: Break outside week range (8.20 – 9.20)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.72 is +0.93% vs 7D avg 8.64. 24h change: +0.46%. Trend: SIDEWAYS. 24h range: 1.95% vs avg daily range 4.81%.
--- Flow Analyst ---
RSI_14: 46.61
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.016077
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.4366
STOP_DIST (ATR×1.5): 0.6549
SUGGESTED_STOP: 8.0651
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.25 | S: 0.23 | 7D_AVG: 0.24
INVALIDATION: Close below 7D_AVG (0.24)
STATE: WATCHLIST
SIGNAL: Price +1.69% from 7D avg — monitoring for continuation
REASON: Current price 0.25 is +1.69% vs 7D avg 0.24. 24h change: +0.12%. Trend: BULLISH. 24h range: 2.75% vs avg daily range 5.54%.
--- Flow Analyst ---
RSI_14: 44.59
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.000378
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0141
STOP_DIST (ATR×1.5): 0.0212
SUGGESTED_STOP: 0.2265
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 1.37 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Break outside week range (1.28 – 1.37)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.32 is -1.00% vs 7D avg 1.33. 24h change: -0.14%. Trend: SIDEWAYS. 24h range: 1.21% vs avg daily range 3.54%.
--- Flow Analyst ---
RSI_14: 38.98
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.005630
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0577
STOP_DIST (ATR×1.5): 0.0865
SUGGESTED_STOP: 1.2305
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.91 | S: 0.82 | 7D_AVG: 0.87
INVALIDATION: Break outside week range (0.82 – 0.91)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.87 is +0.74% vs 7D avg 0.87. 24h change: -0.22%. Trend: SIDEWAYS. 24h range: 2.10% vs avg daily range 5.32%.
--- Flow Analyst ---
RSI_14: 41.83
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.003463
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0515
STOP_DIST (ATR×1.5): 0.0772
SUGGESTED_STOP: 0.7959
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.23 | S: 1.13 | 7D_AVG: 1.18
INVALIDATION: Close below 7D_AVG (1.18)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price +6.57% from 7D avg with aligned trend
REASON: Current price 1.26 is +6.57% vs 7D avg 1.18. 24h change: +4.06%. Trend: BULLISH. 24h range: 6.61% vs avg daily range 4.72%.
--- Flow Analyst ---
RSI_14: 52.20
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.006276
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0712
STOP_DIST (ATR×1.5): 0.1068
SUGGESTED_STOP: 1.1492
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 2.96 | S: 2.72 | 7D_AVG: 2.82
INVALIDATION: Break outside week range (2.72 – 2.96)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2.82 is -0.27% vs 7D avg 2.82. 24h change: +0.28%. Trend: SIDEWAYS. 24h range: 2.17% vs avg daily range 4.55%.
--- Flow Analyst ---
RSI_14: 41.60
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.009692
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.1509
STOP_DIST (ATR×1.5): 0.2263
SUGGESTED_STOP: 2.5907
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.10 | S: 0.09 | 7D_AVG: 0.09
INVALIDATION: Close below 7D_AVG (0.09)
STATE: WATCHLIST
SIGNAL: Price +1.61% from 7D avg — monitoring for continuation
REASON: Current price 0.09 is +1.61% vs 7D avg 0.09. 24h change: +0.32%. Trend: BULLISH. 24h range: 2.58% vs avg daily range 5.07%.
--- Flow Analyst ---
RSI_14: 43.72
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000300
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0053
STOP_DIST (ATR×1.5): 0.0080
SUGGESTED_STOP: 0.0849
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.11 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Break outside week range (0.10 – 0.11)
STATE: WATCHLIST
SIGNAL: Price +3.36% from 7D avg — monitoring for continuation
REASON: Current price 0.11 is +3.36% vs 7D avg 0.11. 24h change: -0.45%. Trend: MIXED. 24h range: 2.81% vs avg daily range 5.66%.
--- Flow Analyst ---
RSI_14: 41.45
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001374
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0072
STOP_DIST (ATR×1.5): 0.0107
SUGGESTED_STOP: 0.0997
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.26 | S: 0.22 | 7D_AVG: 0.23
INVALIDATION: Close below 7D_AVG (0.23)
STATE: WATCHLIST
SIGNAL: Price +1.18% from 7D avg — monitoring for continuation
REASON: Current price 0.24 is +1.18% vs 7D avg 0.23. 24h change: +0.64%. Trend: BULLISH. 24h range: 3.09% vs avg daily range 9.54%.
--- Flow Analyst ---
RSI_14: 57.75
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.001832
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0206
STOP_DIST (ATR×1.5): 0.0309
SUGGESTED_STOP: 0.2053
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 335.30 | S: 292.60 | 7D_AVG: 309.33
INVALIDATION: Close above 7D_AVG (309.33)
STATE: WATCHLIST
SIGNAL: Price -1.59% from 7D avg — monitoring for continuation
REASON: Current price 304.40 is -1.59% vs 7D avg 309.33. 24h change: -1.23%. Trend: BEARISH. 24h range: 3.61% vs avg daily range 7.08%.
--- Flow Analyst ---
RSI_14: 59.66
MACD_TREND: BEARISH
MACD_HISTOGRAM: -4.533878
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 24.5557
STOP_DIST (ATR×1.5): 36.8336
SUGGESTED_STOP: 267.5664
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-04 22:24 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.96 | S: 1.60 | 7D_AVG: 1.76
INVALIDATION: Break outside week range (1.60 – 1.96)
STATE: WATCHLIST
SIGNAL: Price +6.81% from 7D avg — monitoring for continuation
REASON: Current price 1.88 is +6.81% vs 7D avg 1.76. 24h change: -2.90%. Trend: MIXED. 24h range: 4.95% vs avg daily range 6.82%.
--- Flow Analyst ---
RSI_14: 60.59
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.011883
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1306
STOP_DIST (ATR×1.5): 0.1959
SUGGESTED_STOP: 1.6821
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

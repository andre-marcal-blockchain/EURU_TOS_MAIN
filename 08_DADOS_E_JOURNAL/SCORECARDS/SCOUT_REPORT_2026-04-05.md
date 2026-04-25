---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-05
scorecard_date: 2026-04-05
period_type: daily
period_ref: 2026-W14
period_start: 2026-04-05
period_end: 2026-04-05

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
**Date:** 2026-04-05  
**Time:** 16:32 UTC  
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
| BTCUSDT |    67,390.51 | -0.00% | +0.29% | 45.34 | BEARISH | RISING | 3,537.1175 | **21/35** | BOA | **NO_TRADE** |
| ETHUSDT |     2,058.18 | -0.01% | -0.18% | 47.82 | BEARISH | FALLING | 145.5062 | **20/35** | MEDIA | **NO_TRADE** |
| SOLUSDT |        79.77 | -1.88% | -1.78% | 39.43 | BEARISH | FLAT | 6.4518 | **22/35** | BOA | **WATCHLIST** |
| BNBUSDT |       593.02 | +0.14% | -1.37% | 37.71 | BEARISH | FALLING | 29.3644 | **21/35** | BOA | **WATCHLIST** |
| AVAXUSDT |         8.87 | -1.33% | -0.02% | 44.68 | BEARISH | FLAT | 0.6986 | **16/35** | MEDIA | **NO_TRADE** |
| DOTUSDT |         1.23 | -1.76% | -1.43% | 33.50 | BEARISH | FLAT | 0.1045 | **19/35** | MEDIA | **WATCHLIST** |
| LINKUSDT |         8.61 | -1.15% | -0.76% | 44.63 | BEARISH | FLAT | 0.6328 | **17/35** | MEDIA | **NO_TRADE** |
| ADAUSDT |         0.24 | -1.09% | -0.02% | 42.61 | BEARISH | FLAT | 0.0206 | **15/35** | MEDIA | **NO_TRADE** |
| XRPUSDT |         1.30 | -0.94% | -1.99% | 36.89 | BEARISH | FALLING | 0.0848 | **21/35** | BOA | **WATCHLIST** |
| SUIUSDT |         0.85 | -2.33% | -2.02% | 38.78 | BEARISH | FLAT | 0.0750 | **18/35** | MEDIA | **WATCHLIST** |
| NEARUSDT |         1.25 | -1.81% | +4.76% | 51.12 | BEARISH | FLAT | 0.1031 | **19/35** | MEDIA | **WATCHLIST** |
| INJUSDT |         2.78 | -1.17% | -1.64% | 39.72 | BEARISH | RISING | 0.2177 | **18/35** | MEDIA | **WATCHLIST** |
| ARBUSDT |         0.09 | -1.62% | -0.68% | 41.34 | BULLISH | FLAT | 0.0078 | **17/35** | MEDIA | **NO_TRADE** |
| OPUSDT |         0.11 | -2.46% | -0.99% | 38.27 | BULLISH | FLAT | 0.0105 | **15/35** | MEDIA | **NO_TRADE** |
| FETUSDT |         0.23 | -3.15% | -1.07% | 55.29 | BEARISH | FALLING | 0.0300 | **19/35** | MEDIA | **WATCHLIST** |
| TAOUSDT |       297.60 | -2.52% | -3.16% | 56.49 | BEARISH | FALLING | 35.4210 | **21/35** | BOA | **WATCHLIST** |
| RENDERUSDT |         1.85 | -1.18% | +3.42% | 58.58 | BULLISH | RISING | 0.1912 | **19/35** | MEDIA | **WATCHLIST** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | SOLUSDT | **22/35** (63%) | **BOA** | 4 | 1 | 2 | 5 | 2 | 5 | 3 |
| 2 | BTCUSDT | **21/35** (60%) | **BOA** | 5 | 1 | 0 | 5 | 3 | 5 | 2 |
| 3 | BNBUSDT | **21/35** (60%) | **BOA** | 3 | 1 | 2 | 4 | 3 | 5 | 3 |
| 4 | XRPUSDT | **21/35** (60%) | **BOA** | 3 | 2 | 2 | 4 | 2 | 5 | 3 |
| 5 | TAOUSDT | **21/35** (60%) | **BOA** | 2 | 1 | 4 | 5 | 1 | 5 | 3 |
| 6 | ETHUSDT | **20/35** (57%) | **MEDIA** | 4 | 1 | 0 | 5 | 2 | 5 | 3 |
| 7 | DOTUSDT | **19/35** (54%) | **MEDIA** | 2 | 3 | 2 | 3 | 2 | 5 | 2 |
| 8 | NEARUSDT | **19/35** (54%) | **MEDIA** | 2 | 4 | 2 | 3 | 2 | 5 | 1 |
| 9 | FETUSDT | **19/35** (54%) | **MEDIA** | 2 | 1 | 2 | 5 | 1 | 5 | 3 |
| 10 | RENDERUSDT | **19/35** (54%) | **MEDIA** | 1 | 1 | 2 | 5 | 2 | 5 | 3 |
| 11 | SUIUSDT | **18/35** (51%) | **MEDIA** | 2 | 1 | 2 | 4 | 1 | 5 | 3 |
| 12 | INJUSDT | **18/35** (51%) | **MEDIA** | 1 | 1 | 2 | 4 | 2 | 5 | 3 |
| 13 | LINKUSDT | **17/35** (49%) | **MEDIA** | 2 | 1 | 0 | 4 | 2 | 5 | 3 |
| 14 | ARBUSDT | **17/35** (49%) | **MEDIA** | 1 | 2 | 0 | 4 | 2 | 5 | 3 |
| 15 | AVAXUSDT | **16/35** (46%) | **MEDIA** | 2 | 1 | 0 | 4 | 2 | 5 | 2 |
| 16 | ADAUSDT | **15/35** (43%) | **MEDIA** | 2 | 1 | 0 | 3 | 2 | 5 | 2 |
| 17 | OPUSDT | **15/35** (43%) | **MEDIA** | 1 | 1 | 0 | 4 | 1 | 5 | 3 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-05 16:32 UTC
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
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 69,310.00 | S: 65,000.00 | 7D_AVG: 67,196.20
INVALIDATION: Break outside week range (65,000.00 – 69,310.00)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 67,390.51 is +0.29% vs 7D avg 67,196.20. 24h change: -0.00%. Trend: SIDEWAYS. 24h range: 1.85% vs avg daily range 2.90%.
--- Flow Analyst ---
RSI_14: 45.34
MACD_TREND: BEARISH
MACD_HISTOGRAM: -110.905548
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 2358.0784
STOP_DIST (ATR×1.5): 3,537.1175
SUGGESTED_STOP: 63,853.3925
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,167.85 | S: 1,938.82 | 7D_AVG: 2,061.92
INVALIDATION: Break outside week range (1,938.82 – 2,167.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2,058.18 is -0.18% vs 7D avg 2,061.92. 24h change: -0.01%. Trend: SIDEWAYS. 24h range: 3.04% vs avg daily range 4.19%.
--- Flow Analyst ---
RSI_14: 47.82
MACD_TREND: BEARISH
MACD_HISTOGRAM: -2.606527
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 97.0041
STOP_DIST (ATR×1.5): 145.5062
SUGGESTED_STOP: 1,912.6738
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 86.65 | S: 76.70 | 7D_AVG: 81.22
INVALIDATION: Close above 7D_AVG (81.22)
STATE: WATCHLIST
SIGNAL: Price -1.78% from 7D avg — monitoring for continuation
REASON: Current price 79.77 is -1.78% vs 7D avg 81.22. 24h change: -1.88%. Trend: BEARISH. 24h range: 3.54% vs avg daily range 4.87%.
--- Flow Analyst ---
RSI_14: 39.43
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.637971
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 4.3012
STOP_DIST (ATR×1.5): 6.4518
SUGGESTED_STOP: 73.3182
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: MIXED
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 621.90 | S: 570.31 | 7D_AVG: 601.26
INVALIDATION: Break outside week range (570.31 – 621.90)
STATE: WATCHLIST
SIGNAL: Price -1.37% from 7D avg — monitoring for continuation
REASON: Current price 593.02 is -1.37% vs 7D avg 601.26. 24h change: +0.14%. Trend: MIXED. 24h range: 1.59% vs avg daily range 3.09%.
--- Flow Analyst ---
RSI_14: 37.71
MACD_TREND: BEARISH
MACD_HISTOGRAM: -3.268054
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 19.5762
STOP_DIST (ATR×1.5): 29.3644
SUGGESTED_STOP: 563.6556
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.48 | S: 8.37 | 7D_AVG: 8.87
INVALIDATION: Break outside week range (8.37 – 9.48)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.87 is -0.02% vs 7D avg 8.87. 24h change: -1.33%. Trend: SIDEWAYS. 24h range: 4.17% vs avg daily range 5.20%.
--- Flow Analyst ---
RSI_14: 44.68
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.020842
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.4657
STOP_DIST (ATR×1.5): 0.6986
SUGGESTED_STOP: 8.1714
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.30 | S: 1.20 | 7D_AVG: 1.25
INVALIDATION: Close above 7D_AVG (1.25)
STATE: WATCHLIST
SIGNAL: Price -1.43% from 7D avg — monitoring for continuation
REASON: Current price 1.23 is -1.43% vs 7D avg 1.25. 24h change: -1.76%. Trend: BEARISH. 24h range: 4.39% vs avg daily range 4.03%.
--- Flow Analyst ---
RSI_14: 33.50
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.008374
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0697
STOP_DIST (ATR×1.5): 0.1045
SUGGESTED_STOP: 1.1265
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.20 | S: 8.20 | 7D_AVG: 8.68
INVALIDATION: Break outside week range (8.20 – 9.20)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.61 is -0.76% vs 7D avg 8.68. 24h change: -1.15%. Trend: SIDEWAYS. 24h range: 3.60% vs avg daily range 4.53%.
--- Flow Analyst ---
RSI_14: 44.63
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.017112
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.4219
STOP_DIST (ATR×1.5): 0.6328
SUGGESTED_STOP: 7.9772
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.25 | S: 0.23 | 7D_AVG: 0.24
INVALIDATION: Break outside week range (0.23 – 0.25)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.24 is -0.02% vs 7D avg 0.24. 24h change: -1.09%. Trend: SIDEWAYS. 24h range: 4.10% vs avg daily range 5.41%.
--- Flow Analyst ---
RSI_14: 42.61
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.000196
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0137
STOP_DIST (ATR×1.5): 0.0206
SUGGESTED_STOP: 0.2232
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.37 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Close above 7D_AVG (1.33)
STATE: WATCHLIST
SIGNAL: Price -1.99% from 7D avg — monitoring for continuation
REASON: Current price 1.30 is -1.99% vs 7D avg 1.33. 24h change: -0.94%. Trend: BEARISH. 24h range: 3.37% vs avg daily range 3.30%.
--- Flow Analyst ---
RSI_14: 36.89
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.005688
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0565
STOP_DIST (ATR×1.5): 0.0848
SUGGESTED_STOP: 1.2166
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.91 | S: 0.82 | 7D_AVG: 0.87
INVALIDATION: Close above 7D_AVG (0.87)
STATE: WATCHLIST
SIGNAL: Price -2.02% from 7D avg — monitoring for continuation
REASON: Current price 0.85 is -2.02% vs 7D avg 0.87. 24h change: -2.33%. Trend: BEARISH. 24h range: 4.53% vs avg daily range 4.54%.
--- Flow Analyst ---
RSI_14: 38.78
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.003552
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0500
STOP_DIST (ATR×1.5): 0.0750
SUGGESTED_STOP: 0.7757
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.29 | S: 1.13 | 7D_AVG: 1.19
INVALIDATION: Break outside week range (1.13 – 1.29)
STATE: WATCHLIST
SIGNAL: Price +4.76% from 7D avg — monitoring for continuation
REASON: Current price 1.25 is +4.76% vs 7D avg 1.19. 24h change: -1.81%. Trend: MIXED. 24h range: 4.33% vs avg daily range 5.26%.
--- Flow Analyst ---
RSI_14: 51.12
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002171
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0688
STOP_DIST (ATR×1.5): 0.1031
SUGGESTED_STOP: 1.1439
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.96 | S: 2.72 | 7D_AVG: 2.82
INVALIDATION: Close above 7D_AVG (2.82)
STATE: WATCHLIST
SIGNAL: Price -1.64% from 7D avg — monitoring for continuation
REASON: Current price 2.78 is -1.64% vs 7D avg 2.82. 24h change: -1.17%. Trend: BEARISH. 24h range: 3.38% vs avg daily range 4.21%.
--- Flow Analyst ---
RSI_14: 39.72
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.008785
OBV_TREND: RISING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.1452
STOP_DIST (ATR×1.5): 0.2177
SUGGESTED_STOP: 2.5593
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.10 | S: 0.09 | 7D_AVG: 0.09
INVALIDATION: Break outside week range (0.09 – 0.10)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.09 is -0.68% vs 7D avg 0.09. 24h change: -1.62%. Trend: SIDEWAYS. 24h range: 4.61% vs avg daily range 4.85%.
--- Flow Analyst ---
RSI_14: 41.34
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.000287
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0052
STOP_DIST (ATR×1.5): 0.0078
SUGGESTED_STOP: 0.0834
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.11 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Break outside week range (0.10 – 0.11)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.11 is -0.99% vs 7D avg 0.11. 24h change: -2.46%. Trend: SIDEWAYS. 24h range: 5.43% vs avg daily range 5.47%.
--- Flow Analyst ---
RSI_14: 38.27
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001299
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0070
STOP_DIST (ATR×1.5): 0.0105
SUGGESTED_STOP: 0.0964
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.25 | S: 0.22 | 7D_AVG: 0.23
INVALIDATION: Close above 7D_AVG (0.23)
STATE: WATCHLIST
SIGNAL: Price -1.07% from 7D avg — monitoring for continuation
REASON: Current price 0.23 is -1.07% vs 7D avg 0.23. 24h change: -3.15%. Trend: BEARISH. 24h range: 6.80% vs avg daily range 8.02%.
--- Flow Analyst ---
RSI_14: 55.29
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.002290
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 0.0200
STOP_DIST (ATR×1.5): 0.0300
SUGGESTED_STOP: 0.2009
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 335.30 | S: 292.60 | 7D_AVG: 307.31
INVALIDATION: Close above 7D_AVG (307.31)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price -3.16% from 7D avg with aligned trend
REASON: Current price 297.60 is -3.16% vs 7D avg 307.31. 24h change: -2.52%. Trend: BEARISH. 24h range: 3.97% vs avg daily range 6.90%.
--- Flow Analyst ---
RSI_14: 56.49
MACD_TREND: BEARISH
MACD_HISTOGRAM: -5.418042
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 23.6140
STOP_DIST (ATR×1.5): 35.4210
SUGGESTED_STOP: 262.1790
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 16:32 UTC
TREND: MIXED
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.96 | S: 1.60 | 7D_AVG: 1.79
INVALIDATION: Break outside week range (1.60 – 1.96)
STATE: WATCHLIST
SIGNAL: Price +3.42% from 7D avg — monitoring for continuation
REASON: Current price 1.85 is +3.42% vs 7D avg 1.79. 24h change: -1.18%. Trend: MIXED. 24h range: 4.70% vs avg daily range 6.44%.
--- Flow Analyst ---
RSI_14: 58.58
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.009670
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1275
STOP_DIST (ATR×1.5): 0.1912
SUGGESTED_STOP: 1.6598
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

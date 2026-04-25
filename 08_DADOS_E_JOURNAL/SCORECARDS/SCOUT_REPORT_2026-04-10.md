---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-10
scorecard_date: 2026-04-10
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-10
period_end: 2026-04-10

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
**Date:** 2026-04-10  
**Time:** 05:01 UTC  
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
| BTCUSDT |    72,091.30 | +1.93% | +3.64% | 59.00 | BULLISH | RISING | 3,683.8865 | **26/35** | BOA | **SETUP** |
| ETHUSDT |     2,195.19 | +0.88% | +2.74% | 56.87 | BULLISH | RISING | 149.9272 | **25/35** | BOA | **WATCHLIST** |
| SOLUSDT |        83.33 | +1.91% | +1.51% | 47.85 | BULLISH | RISING | 6.4932 | **23/35** | BOA | **WATCHLIST** |
| BNBUSDT |       600.92 | +0.35% | -0.03% | 43.32 | BULLISH | FLAT | 28.9014 | **20/35** | MEDIA | **NO_TRADE** |
| AVAXUSDT |         9.38 | +3.76% | +3.04% | 53.01 | BULLISH | RISING | 0.7957 | **23/35** | BOA | **SETUP** |
| DOTUSDT |         1.30 | +4.00% | +2.76% | 45.62 | BULLISH | RISING | 0.1112 | **22/35** | BOA | **WATCHLIST** |
| LINKUSDT |         8.96 | +2.28% | +1.06% | 50.90 | BULLISH | RISING | 0.6665 | **25/35** | BOA | **WATCHLIST** |
| ADAUSDT |         0.25 | +1.61% | +0.54% | 48.36 | BULLISH | FLAT | 0.0210 | **17/35** | MEDIA | **NO_TRADE** |
| XRPUSDT |         1.35 | +1.08% | +0.81% | 46.36 | BULLISH | FLAT | 0.0823 | **21/35** | BOA | **NO_TRADE** |
| SUIUSDT |         0.94 | +2.93% | +4.05% | 52.77 | BULLISH | FLAT | 0.0820 | **23/35** | BOA | **SETUP** |
| NEARUSDT |         1.37 | +2.77% | +7.19% | 64.17 | BULLISH | RISING | 0.1072 | **23/35** | BOA | **SETUP** |
| INJUSDT |         2.99 | +3.42% | +3.82% | 52.13 | BULLISH | RISING | 0.2226 | **22/35** | BOA | **SETUP** |
| ARBUSDT |         0.11 | +9.71% | +13.79% | 67.86 | BULLISH | RISING | 0.0090 | **26/35** | BOA | **SETUP** |
| OPUSDT |         0.12 | +1.76% | +2.54% | 49.02 | BULLISH | FLAT | 0.0103 | **19/35** | MEDIA | **WATCHLIST** |
| FETUSDT |         0.24 | +2.88% | +0.29% | 56.08 | BEARISH | RISING | 0.0304 | **21/35** | BOA | **NO_TRADE** |
| TAOUSDT |       263.70 | -18.11% | -16.05% | 41.90 | BEARISH | FALLING | 41.5905 | **29/35** | PREMIUM | **SETUP** |
| RENDERUSDT |         2.04 | +0.59% | +4.43% | 64.91 | BULLISH | RISING | 0.1982 | **23/35** | BOA | **SETUP** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | TAOUSDT | **29/35** (83%) | **PREMIUM** | 4 | 5 | 5 | 5 | 0 | 5 | 5 |
| 2 | BTCUSDT | **26/35** (74%) | **BOA** | 5 | 4 | 4 | 5 | 3 | 5 | 0 |
| 3 | ARBUSDT | **26/35** (74%) | **BOA** | 2 | 5 | 5 | 4 | 5 | 5 | 0 |
| 4 | ETHUSDT | **25/35** (71%) | **BOA** | 5 | 4 | 2 | 5 | 2 | 5 | 2 |
| 5 | LINKUSDT | **25/35** (71%) | **BOA** | 3 | 5 | 2 | 4 | 3 | 5 | 3 |
| 6 | SOLUSDT | **23/35** (66%) | **BOA** | 4 | 3 | 2 | 5 | 2 | 5 | 2 |
| 7 | AVAXUSDT | **23/35** (66%) | **BOA** | 3 | 3 | 4 | 4 | 3 | 5 | 1 |
| 8 | SUIUSDT | **23/35** (66%) | **BOA** | 2 | 3 | 4 | 4 | 3 | 5 | 2 |
| 9 | NEARUSDT | **23/35** (66%) | **BOA** | 2 | 5 | 5 | 3 | 3 | 5 | 0 |
| 10 | RENDERUSDT | **23/35** (66%) | **BOA** | 2 | 4 | 4 | 5 | 2 | 5 | 1 |
| 11 | DOTUSDT | **22/35** (63%) | **BOA** | 2 | 5 | 2 | 3 | 4 | 5 | 1 |
| 12 | INJUSDT | **22/35** (63%) | **BOA** | 1 | 4 | 4 | 4 | 3 | 5 | 1 |
| 13 | XRPUSDT | **21/35** (60%) | **BOA** | 4 | 4 | 0 | 4 | 2 | 5 | 2 |
| 14 | FETUSDT | **21/35** (60%) | **BOA** | 2 | 3 | 0 | 5 | 3 | 5 | 3 |
| 15 | BNBUSDT | **20/35** (57%) | **MEDIA** | 3 | 3 | 0 | 4 | 2 | 5 | 3 |
| 16 | OPUSDT | **19/35** (54%) | **MEDIA** | 1 | 3 | 2 | 4 | 2 | 5 | 2 |
| 17 | ADAUSDT | **17/35** (49%) | **MEDIA** | 2 | 2 | 0 | 3 | 2 | 5 | 3 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-10 05:01 UTC
OVERALL_SEVERITY: MEDIUM
TOP_HEADLINES:
  1. [MEDIUM] Bitcoin price surfs US PCE inflation as trader keeps $80K BTC price target
  2. [LOW] Bitcoin can be made quantum-safe without a protocol upgrade: Researcher
  3. [LOW] OKX Ventures, HashKey back VPBank-linked CAEX for Vietnam crypto pilot push
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 73,145.00 | S: 66,282.00 | 7D_AVG: 69,562.10
INVALIDATION: Close below 7D_AVG (69,562.10)
STATE: SETUP
SIGNAL: Price +3.64% from 7D avg with aligned trend
REASON: Current price 72,091.30 is +3.64% vs 7D avg 69,562.10. 24h change: +1.93%. Trend: BULLISH. 24h range: 3.64% vs avg daily range 3.31%.
--- Flow Analyst ---
RSI_14: 59.00
MACD_TREND: BULLISH
MACD_HISTOGRAM: 575.025582
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 2455.9244
STOP_DIST (ATR×1.5): 3,683.8865
SUGGESTED_STOP: 68,407.4235
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,273.87 | S: 2,021.50 | 7D_AVG: 2,136.70
INVALIDATION: Close below 7D_AVG (2,136.70)
STATE: WATCHLIST
SIGNAL: Price +2.74% from 7D avg — monitoring for continuation
REASON: Current price 2,195.19 is +2.74% vs 7D avg 2,136.70. 24h change: +0.88%. Trend: BULLISH. 24h range: 4.04% vs avg daily range 4.37%.
--- Flow Analyst ---
RSI_14: 56.87
MACD_TREND: BULLISH
MACD_HISTOGRAM: 15.414802
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 99.9514
STOP_DIST (ATR×1.5): 149.9272
SUGGESTED_STOP: 2,045.2628
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 87.02 | S: 78.38 | 7D_AVG: 82.09
INVALIDATION: Close below 7D_AVG (82.09)
STATE: WATCHLIST
SIGNAL: Price +1.51% from 7D avg — monitoring for continuation
REASON: Current price 83.33 is +1.51% vs 7D avg 82.09. 24h change: +1.91%. Trend: BULLISH. 24h range: 5.46% vs avg daily range 4.85%.
--- Flow Analyst ---
RSI_14: 47.85
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.269971
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 4.3288
STOP_DIST (ATR×1.5): 6.4932
SUGGESTED_STOP: 76.8468
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 624.85 | S: 581.93 | 7D_AVG: 601.08
INVALIDATION: Break outside week range (581.93 – 624.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 600.92 is -0.03% vs 7D avg 601.08. 24h change: +0.35%. Trend: SIDEWAYS. 24h range: 2.31% vs avg daily range 2.80%.
--- Flow Analyst ---
RSI_14: 43.32
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.724926
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 19.2676
STOP_DIST (ATR×1.5): 28.9014
SUGGESTED_STOP: 572.0186
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.70 | S: 8.46 | 7D_AVG: 9.10
INVALIDATION: Close below 7D_AVG (9.10)
STATE: SETUP
SIGNAL: Price +3.04% from 7D avg with aligned trend
REASON: Current price 9.38 is +3.04% vs 7D avg 9.10. 24h change: +3.76%. Trend: BULLISH. 24h range: 7.46% vs avg daily range 6.80%.
--- Flow Analyst ---
RSI_14: 53.01
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.060606
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.5304
STOP_DIST (ATR×1.5): 0.7957
SUGGESTED_STOP: 8.5843
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.36 | S: 1.21 | 7D_AVG: 1.27
INVALIDATION: Close below 7D_AVG (1.27)
STATE: WATCHLIST
SIGNAL: Price +2.76% from 7D avg — monitoring for continuation
REASON: Current price 1.30 is +2.76% vs 7D avg 1.27. 24h change: +4.00%. Trend: BULLISH. 24h range: 9.68% vs avg daily range 5.92%.
--- Flow Analyst ---
RSI_14: 45.62
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.010243
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0741
STOP_DIST (ATR×1.5): 0.1112
SUGGESTED_STOP: 1.1898
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.42 | S: 8.47 | 7D_AVG: 8.87
INVALIDATION: Close below 7D_AVG (8.87)
STATE: WATCHLIST
SIGNAL: Price +1.06% from 7D avg — monitoring for continuation
REASON: Current price 8.96 is +1.06% vs 7D avg 8.87. 24h change: +2.28%. Trend: BULLISH. 24h range: 5.58% vs avg daily range 4.92%.
--- Flow Analyst ---
RSI_14: 50.90
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.038570
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.4443
STOP_DIST (ATR×1.5): 0.6665
SUGGESTED_STOP: 8.2935
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.27 | S: 0.24 | 7D_AVG: 0.25
INVALIDATION: Break outside week range (0.24 – 0.27)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.25 is +0.54% vs 7D avg 0.25. 24h change: +1.61%. Trend: SIDEWAYS. 24h range: 4.99% vs avg daily range 5.66%.
--- Flow Analyst ---
RSI_14: 48.36
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001668
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0140
STOP_DIST (ATR×1.5): 0.0210
SUGGESTED_STOP: 0.2316
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.40 | S: 1.28 | 7D_AVG: 1.34
INVALIDATION: Break outside week range (1.28 – 1.40)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 1.35 is +0.81% vs 7D avg 1.34. 24h change: +1.08%. Trend: SIDEWAYS. 24h range: 3.55% vs avg daily range 3.69%.
--- Flow Analyst ---
RSI_14: 46.36
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.003973
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0549
STOP_DIST (ATR×1.5): 0.0823
SUGGESTED_STOP: 1.2637
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.98 | S: 0.84 | 7D_AVG: 0.90
INVALIDATION: Close below 7D_AVG (0.90)
STATE: SETUP
SIGNAL: Price +4.05% from 7D avg with aligned trend
REASON: Current price 0.94 is +4.05% vs 7D avg 0.90. 24h change: +2.93%. Trend: BULLISH. 24h range: 7.01% vs avg daily range 6.19%.
--- Flow Analyst ---
RSI_14: 52.77
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.009640
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0547
STOP_DIST (ATR×1.5): 0.0820
SUGGESTED_STOP: 0.8532
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.39 | S: 1.16 | 7D_AVG: 1.28
INVALIDATION: Close below 7D_AVG (1.28)
STATE: SETUP
SIGNAL: Price +7.19% from 7D avg with aligned trend
REASON: Current price 1.37 is +7.19% vs 7D avg 1.28. 24h change: +2.77%. Trend: BULLISH. 24h range: 4.95% vs avg daily range 6.25%.
--- Flow Analyst ---
RSI_14: 64.17
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.018646
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0714
STOP_DIST (ATR×1.5): 0.1072
SUGGESTED_STOP: 1.2658
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 3.05 | S: 2.74 | 7D_AVG: 2.88
INVALIDATION: Close below 7D_AVG (2.88)
STATE: SETUP
SIGNAL: Price +3.82% from 7D avg with aligned trend
REASON: Current price 2.99 is +3.82% vs 7D avg 2.88. 24h change: +3.42%. Trend: BULLISH. 24h range: 4.85% vs avg daily range 4.83%.
--- Flow Analyst ---
RSI_14: 52.13
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.025403
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1484
STOP_DIST (ATR×1.5): 0.2226
SUGGESTED_STOP: 2.7674
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.11 | S: 0.09 | 7D_AVG: 0.10
INVALIDATION: Close below 7D_AVG (0.10)
STATE: SETUP
SIGNAL: Price +13.79% from 7D avg with aligned trend
REASON: Current price 0.11 is +13.79% vs 7D avg 0.10. 24h change: +9.71%. Trend: BULLISH. 24h range: 10.01% vs avg daily range 6.38%.
--- Flow Analyst ---
RSI_14: 67.86
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002597
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0060
STOP_DIST (ATR×1.5): 0.0090
SUGGESTED_STOP: 0.1029
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.11 | 7D_AVG: 0.11
INVALIDATION: Close below 7D_AVG (0.11)
STATE: WATCHLIST
SIGNAL: Price +2.54% from 7D avg — monitoring for continuation
REASON: Current price 0.12 is +2.54% vs 7D avg 0.11. 24h change: +1.76%. Trend: BULLISH. 24h range: 5.02% vs avg daily range 5.68%.
--- Flow Analyst ---
RSI_14: 49.02
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002136
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0069
STOP_DIST (ATR×1.5): 0.0103
SUGGESTED_STOP: 0.1052
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.26 | S: 0.22 | 7D_AVG: 0.24
INVALIDATION: Break outside week range (0.22 – 0.26)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.24 is +0.29% vs 7D avg 0.24. 24h change: +2.88%. Trend: SIDEWAYS. 24h range: 8.51% vs avg daily range 7.92%.
--- Flow Analyst ---
RSI_14: 56.08
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.001538
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0203
STOP_DIST (ATR×1.5): 0.0304
SUGGESTED_STOP: 0.2092
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BEARISH
STRUCTURE: AT_WEEKLY_LOW — support zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 351.10 | S: 295.10 | 7D_AVG: 314.13
INVALIDATION: Close above 7D_AVG (314.13)
STATE: SETUP
SIGNAL: Price -16.05% from 7D avg with aligned trend
REASON: Current price 263.70 is -16.05% vs 7D avg 314.13. 24h change: -18.11%. Trend: BEARISH. 24h range: 29.65% vs avg daily range 8.06%.
--- Flow Analyst ---
RSI_14: 41.90
MACD_TREND: BEARISH
MACD_HISTOGRAM: -6.954809
OBV_TREND: FALLING
VOLUME_FLOW: STRONG
ATR_14: 27.7270
STOP_DIST (ATR×1.5): 41.5905
SUGGESTED_STOP: 222.3095
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-10 05:01 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 2.12 | S: 1.82 | 7D_AVG: 1.95
INVALIDATION: Close below 7D_AVG (1.95)
STATE: SETUP
SIGNAL: Price +4.43% from 7D avg with aligned trend
REASON: Current price 2.04 is +4.43% vs 7D avg 1.95. 24h change: +0.59%. Trend: BULLISH. 24h range: 4.95% vs avg daily range 7.22%.
--- Flow Analyst ---
RSI_14: 64.91
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.020295
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1321
STOP_DIST (ATR×1.5): 0.1982
SUGGESTED_STOP: 1.8408
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

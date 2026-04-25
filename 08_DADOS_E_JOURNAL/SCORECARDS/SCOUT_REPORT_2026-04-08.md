---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-08
scorecard_date: 2026-04-08
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-08
period_end: 2026-04-08

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
**Date:** 2026-04-08  
**Time:** 16:23 UTC  
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
| BTCUSDT |    71,416.17 | +4.84% | +4.35% | 57.42 | BULLISH | FLAT | 3,861.9091 | **28/35** | PREMIUM | **SETUP** |
| ETHUSDT |     2,218.78 | +6.78% | +5.13% | 58.92 | BULLISH | FLAT | 159.4112 | **29/35** | PREMIUM | **SETUP** |
| SOLUSDT |        83.29 | +5.83% | +2.50% | 47.57 | BULLISH | RISING | 6.8314 | **26/35** | BOA | **WATCHLIST** |
| BNBUSDT |       606.59 | +1.24% | +1.15% | 44.93 | BULLISH | FLAT | 30.8866 | **23/35** | BOA | **WATCHLIST** |
| AVAXUSDT |         9.22 | +7.46% | +2.15% | 50.62 | BULLISH | RISING | 0.8035 | **25/35** | BOA | **WATCHLIST** |
| DOTUSDT |         1.29 | +5.92% | +2.63% | 43.16 | BULLISH | FALLING | 0.1098 | **22/35** | BOA | **WATCHLIST** |
| LINKUSDT |         9.04 | +5.12% | +2.35% | 52.23 | BULLISH | RISING | 0.6852 | **24/35** | BOA | **WATCHLIST** |
| ADAUSDT |         0.25 | +5.00% | +2.13% | 48.97 | BULLISH | FLAT | 0.0221 | **24/35** | BOA | **WATCHLIST** |
| XRPUSDT |         1.36 | +4.75% | +1.85% | 47.87 | BULLISH | FLAT | 0.0880 | **24/35** | BOA | **WATCHLIST** |
| SUIUSDT |         0.93 | +8.16% | +5.65% | 52.69 | BULLISH | FLAT | 0.0840 | **28/35** | PREMIUM | **SETUP** |
| NEARUSDT |         1.34 | +8.47% | +9.18% | 61.57 | BULLISH | RISING | 0.1128 | **25/35** | BOA | **SETUP** |
| INJUSDT |         2.96 | +5.82% | +4.17% | 50.56 | BULLISH | RISING | 0.2262 | **22/35** | BOA | **SETUP** |
| ARBUSDT |         0.10 | +7.70% | +6.77% | 55.62 | BULLISH | FLAT | 0.0085 | **27/35** | BOA | **SETUP** |
| OPUSDT |         0.12 | +7.28% | +5.01% | 49.81 | BULLISH | FLAT | 0.0108 | **27/35** | BOA | **SETUP** |
| FETUSDT |         0.25 | +8.98% | +5.81% | 61.33 | BEARISH | FLAT | 0.0310 | **28/35** | PREMIUM | **SETUP** |
| TAOUSDT |       336.70 | +7.88% | +8.28% | 68.55 | BEARISH | RISING | 36.8142 | **28/35** | PREMIUM | **SETUP** |
| RENDERUSDT |         2.06 | +9.03% | +8.91% | 67.52 | BULLISH | RISING | 0.2052 | **26/35** | BOA | **SETUP** |

---

## Score Leaderboard

| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |
|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|
| 1 | ETHUSDT | **29/35** (83%) | **PREMIUM** | 5 | 5 | 5 | 5 | 3 | 5 | 1 |
| 2 | BTCUSDT | **28/35** (80%) | **PREMIUM** | 5 | 5 | 4 | 5 | 3 | 5 | 1 |
| 3 | SUIUSDT | **28/35** (80%) | **PREMIUM** | 3 | 5 | 5 | 4 | 4 | 5 | 2 |
| 4 | FETUSDT | **28/35** (80%) | **PREMIUM** | 3 | 5 | 5 | 5 | 4 | 5 | 1 |
| 5 | TAOUSDT | **28/35** (80%) | **PREMIUM** | 4 | 5 | 5 | 5 | 4 | 5 | 0 |
| 6 | ARBUSDT | **27/35** (77%) | **BOA** | 2 | 5 | 5 | 4 | 4 | 5 | 2 |
| 7 | OPUSDT | **27/35** (77%) | **BOA** | 2 | 5 | 5 | 4 | 4 | 5 | 2 |
| 8 | SOLUSDT | **26/35** (74%) | **BOA** | 4 | 5 | 2 | 5 | 3 | 5 | 2 |
| 9 | RENDERUSDT | **26/35** (74%) | **BOA** | 2 | 5 | 5 | 5 | 4 | 5 | 0 |
| 10 | AVAXUSDT | **25/35** (71%) | **BOA** | 3 | 5 | 2 | 4 | 4 | 5 | 2 |
| 11 | NEARUSDT | **25/35** (71%) | **BOA** | 3 | 5 | 5 | 3 | 4 | 5 | 0 |
| 12 | LINKUSDT | **24/35** (69%) | **BOA** | 3 | 5 | 2 | 4 | 3 | 5 | 2 |
| 13 | ADAUSDT | **24/35** (69%) | **BOA** | 3 | 5 | 2 | 3 | 3 | 5 | 3 |
| 14 | XRPUSDT | **24/35** (69%) | **BOA** | 4 | 5 | 2 | 4 | 2 | 5 | 2 |
| 15 | BNBUSDT | **23/35** (66%) | **BOA** | 4 | 5 | 2 | 4 | 1 | 5 | 2 |
| 16 | DOTUSDT | **22/35** (63%) | **BOA** | 2 | 5 | 2 | 3 | 3 | 5 | 2 |
| 17 | INJUSDT | **22/35** (63%) | **BOA** | 1 | 3 | 4 | 4 | 3 | 5 | 2 |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-08 16:23 UTC
OVERALL_SEVERITY: HIGH
TOP_HEADLINES:
  1. [HIGH] Bitcoin fades three-week highs as BTC price shrugs off Iran war ceasefire
  2. [HIGH] SEC admits certain crypto enforcement cases delivered no investor benefit
  3. [LOW] Here’s what happened in crypto today
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 72,761.00 | S: 65,712.12 | 7D_AVG: 68,441.81
INVALIDATION: Close below 7D_AVG (68,441.81)
STATE: SETUP
SIGNAL: Price +4.35% from 7D avg with aligned trend
REASON: Current price 71,416.17 is +4.35% vs 7D avg 68,441.81. 24h change: +4.84%. Trend: BULLISH. 24h range: 6.64% vs avg daily range 3.34%.
--- Flow Analyst ---
RSI_14: 57.42
MACD_TREND: BULLISH
MACD_HISTOGRAM: 462.296417
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 2574.6061
STOP_DIST (ATR×1.5): 3,861.9091
SUGGESTED_STOP: 67,554.2609
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,273.87 | S: 2,017.04 | 7D_AVG: 2,110.60
INVALIDATION: Close below 7D_AVG (2,110.60)
STATE: SETUP
SIGNAL: Price +5.13% from 7D avg with aligned trend
REASON: Current price 2,218.78 is +5.13% vs 7D avg 2,110.60. 24h change: +6.78%. Trend: BULLISH. 24h range: 8.84% vs avg daily range 4.76%.
--- Flow Analyst ---
RSI_14: 58.92
MACD_TREND: BULLISH
MACD_HISTOGRAM: 16.656557
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 106.2741
STOP_DIST (ATR×1.5): 159.4112
SUGGESTED_STOP: 2,059.3688
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 87.02 | S: 76.70 | 7D_AVG: 81.26
INVALIDATION: Close below 7D_AVG (81.26)
STATE: WATCHLIST
SIGNAL: Price +2.50% from 7D avg — monitoring for continuation
REASON: Current price 83.29 is +2.50% vs 7D avg 81.26. 24h change: +5.83%. Trend: BULLISH. 24h range: 10.01% vs avg daily range 5.39%.
--- Flow Analyst ---
RSI_14: 47.57
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.114268
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 4.5542
STOP_DIST (ATR×1.5): 6.8314
SUGGESTED_STOP: 76.4686
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 624.85 | S: 570.31 | 7D_AVG: 599.67
INVALIDATION: Close below 7D_AVG (599.67)
STATE: WATCHLIST
SIGNAL: Price +1.15% from 7D avg — monitoring for continuation
REASON: Current price 606.59 is +1.15% vs 7D avg 599.67. 24h change: +1.24%. Trend: BULLISH. 24h range: 4.25% vs avg daily range 3.27%.
--- Flow Analyst ---
RSI_14: 44.93
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.639014
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 20.5910
STOP_DIST (ATR×1.5): 30.8866
SUGGESTED_STOP: 575.7034
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.66 | S: 8.46 | 7D_AVG: 9.03
INVALIDATION: Close below 7D_AVG (9.03)
STATE: WATCHLIST
SIGNAL: Price +2.15% from 7D avg — monitoring for continuation
REASON: Current price 9.22 is +2.15% vs 7D avg 9.03. 24h change: +7.46%. Trend: BULLISH. 24h range: 11.50% vs avg daily range 6.68%.
--- Flow Analyst ---
RSI_14: 50.62
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.041133
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.5357
STOP_DIST (ATR×1.5): 0.8035
SUGGESTED_STOP: 8.4165
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.33 | S: 1.20 | 7D_AVG: 1.26
INVALIDATION: Close below 7D_AVG (1.26)
STATE: WATCHLIST
SIGNAL: Price +2.63% from 7D avg — monitoring for continuation
REASON: Current price 1.29 is +2.63% vs 7D avg 1.26. 24h change: +5.92%. Trend: BULLISH. 24h range: 9.24% vs avg daily range 5.14%.
--- Flow Analyst ---
RSI_14: 43.16
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.005485
OBV_TREND: FALLING
VOLUME_FLOW: DIVERGENCE
ATR_14: 0.0732
STOP_DIST (ATR×1.5): 0.1098
SUGGESTED_STOP: 1.1782
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.42 | S: 8.42 | 7D_AVG: 8.83
INVALIDATION: Close below 7D_AVG (8.83)
STATE: WATCHLIST
SIGNAL: Price +2.35% from 7D avg — monitoring for continuation
REASON: Current price 9.04 is +2.35% vs 7D avg 8.83. 24h change: +5.12%. Trend: BULLISH. 24h range: 9.18% vs avg daily range 5.01%.
--- Flow Analyst ---
RSI_14: 52.23
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.049016
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.4568
STOP_DIST (ATR×1.5): 0.6852
SUGGESTED_STOP: 8.3548
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.27 | S: 0.23 | 7D_AVG: 0.25
INVALIDATION: Close below 7D_AVG (0.25)
STATE: WATCHLIST
SIGNAL: Price +2.13% from 7D avg — monitoring for continuation
REASON: Current price 0.25 is +2.13% vs 7D avg 0.25. 24h change: +5.00%. Trend: BULLISH. 24h range: 9.72% vs avg daily range 5.80%.
--- Flow Analyst ---
RSI_14: 48.97
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001746
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0147
STOP_DIST (ATR×1.5): 0.0221
SUGGESTED_STOP: 0.2320
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.40 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Close below 7D_AVG (1.33)
STATE: WATCHLIST
SIGNAL: Price +1.85% from 7D avg — monitoring for continuation
REASON: Current price 1.36 is +1.85% vs 7D avg 1.33. 24h change: +4.75%. Trend: BULLISH. 24h range: 7.43% vs avg daily range 3.86%.
--- Flow Analyst ---
RSI_14: 47.87
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.003587
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0586
STOP_DIST (ATR×1.5): 0.0880
SUGGESTED_STOP: 1.2691
```

### SUIUSDT

```
AGENT: Scout
SYMBOL: SUIUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.98 | S: 0.84 | 7D_AVG: 0.88
INVALIDATION: Close below 7D_AVG (0.88)
STATE: SETUP
SIGNAL: Price +5.65% from 7D avg with aligned trend
REASON: Current price 0.93 is +5.65% vs 7D avg 0.88. 24h change: +8.16%. Trend: BULLISH. 24h range: 12.62% vs avg daily range 5.62%.
--- Flow Analyst ---
RSI_14: 52.69
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.008136
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0560
STOP_DIST (ATR×1.5): 0.0840
SUGGESTED_STOP: 0.8503
```

### NEARUSDT

```
AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: AT_WEEKLY_HIGH — resistance zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.34 | S: 1.14 | 7D_AVG: 1.23
INVALIDATION: Close below 7D_AVG (1.23)
STATE: SETUP
SIGNAL: Price +9.18% from 7D avg with aligned trend
REASON: Current price 1.34 is +9.18% vs 7D avg 1.23. 24h change: +8.47%. Trend: BULLISH. 24h range: 11.75% vs avg daily range 5.79%.
--- Flow Analyst ---
RSI_14: 61.57
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.012261
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.0752
STOP_DIST (ATR×1.5): 0.1128
SUGGESTED_STOP: 1.2322
```

### INJUSDT

```
AGENT: Scout
SYMBOL: INJUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 3.05 | S: 2.73 | 7D_AVG: 2.84
INVALIDATION: Close below 7D_AVG (2.84)
STATE: SETUP
SIGNAL: Price +4.17% from 7D avg with aligned trend
REASON: Current price 2.96 is +4.17% vs 7D avg 2.84. 24h change: +5.82%. Trend: BULLISH. 24h range: 8.30% vs avg daily range 4.69%.
--- Flow Analyst ---
RSI_14: 50.56
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.019961
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1508
STOP_DIST (ATR×1.5): 0.2262
SUGGESTED_STOP: 2.7368
```

### ARBUSDT

```
AGENT: Scout
SYMBOL: ARBUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.10 | S: 0.09 | 7D_AVG: 0.09
INVALIDATION: Close below 7D_AVG (0.09)
STATE: SETUP
SIGNAL: Price +6.77% from 7D avg with aligned trend
REASON: Current price 0.10 is +6.77% vs 7D avg 0.09. 24h change: +7.70%. Trend: BULLISH. 24h range: 11.02% vs avg daily range 5.82%.
--- Flow Analyst ---
RSI_14: 55.62
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.001410
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0057
STOP_DIST (ATR×1.5): 0.0085
SUGGESTED_STOP: 0.0922
```

### OPUSDT

```
AGENT: Scout
SYMBOL: OPUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.12 | S: 0.10 | 7D_AVG: 0.11
INVALIDATION: Close below 7D_AVG (0.11)
STATE: SETUP
SIGNAL: Price +5.01% from 7D avg with aligned trend
REASON: Current price 0.12 is +5.01% vs 7D avg 0.11. 24h change: +7.28%. Trend: BULLISH. 24h range: 10.91% vs avg daily range 5.65%.
--- Flow Analyst ---
RSI_14: 49.81
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.002303
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0072
STOP_DIST (ATR×1.5): 0.0108
SUGGESTED_STOP: 0.1056
```

### FETUSDT

```
AGENT: Scout
SYMBOL: FETUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.26 | S: 0.22 | 7D_AVG: 0.24
INVALIDATION: Close below 7D_AVG (0.24)
STATE: SETUP
SIGNAL: Price +5.81% from 7D avg with aligned trend
REASON: Current price 0.25 is +5.81% vs 7D avg 0.24. 24h change: +8.98%. Trend: BULLISH. 24h range: 11.76% vs avg daily range 8.19%.
--- Flow Analyst ---
RSI_14: 61.33
MACD_TREND: BEARISH
MACD_HISTOGRAM: -0.000977
OBV_TREND: FLAT
VOLUME_FLOW: WEAK
ATR_14: 0.0207
STOP_DIST (ATR×1.5): 0.0310
SUGGESTED_STOP: 0.2191
```

### TAOUSDT

```
AGENT: Scout
SYMBOL: TAOUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 345.00 | S: 292.60 | 7D_AVG: 310.96
INVALIDATION: Close below 7D_AVG (310.96)
STATE: SETUP
SIGNAL: Price +8.28% from 7D avg with aligned trend
REASON: Current price 336.70 is +8.28% vs 7D avg 310.96. 24h change: +7.88%. Trend: BULLISH. 24h range: 12.21% vs avg daily range 7.35%.
--- Flow Analyst ---
RSI_14: 68.55
MACD_TREND: BEARISH
MACD_HISTOGRAM: -1.698417
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 24.5428
STOP_DIST (ATR×1.5): 36.8142
SUGGESTED_STOP: 299.7858
```

### RENDERUSDT

```
AGENT: Scout
SYMBOL: RENDERUSDT
TIMEFRAME: 1D
DATE: 2026-04-08 16:23 UTC
TREND: BULLISH
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2.12 | S: 1.70 | 7D_AVG: 1.90
INVALIDATION: Close below 7D_AVG (1.90)
STATE: SETUP
SIGNAL: Price +8.91% from 7D avg with aligned trend
REASON: Current price 2.06 is +8.91% vs 7D avg 1.90. 24h change: +9.03%. Trend: BULLISH. 24h range: 11.53% vs avg daily range 7.65%.
--- Flow Analyst ---
RSI_14: 67.52
MACD_TREND: BULLISH
MACD_HISTOGRAM: 0.024046
OBV_TREND: RISING
VOLUME_FLOW: STRONG
ATR_14: 0.1368
STOP_DIST (ATR×1.5): 0.2052
SUGGESTED_STOP: 1.8588
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*

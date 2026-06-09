---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-06-09  
**Time:** 05:30 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** INACTIVE — BTC 4H state is GEM_ALERT; signals unmodified  

---

## System Health

```
TOTAL_ASSETS_REQUESTED:  18
TOTAL_ASSETS_FETCHED:    18
TOTAL_ASSETS_EXCLUDED:   0
FAILED_ASSETS:           none
STALE_ASSETS:            none
ANOMALOUS_ASSETS:        none
PIPELINE_STATUS:         HEALTHY
```

---

## Asset Summary

| Symbol | Price (USDT) | State |
|--------|-------------|-------|
| BTCUSDT |  63,320.3700 | **GEM_ALERT** |
| ETHUSDT |   1,687.9200 | **WATCHLIST** |
| SOLUSDT |      67.0800 | **WATCHLIST** |
| BNBUSDT |     603.8200 | **GEM_ALERT** |
| AVAXUSDT |       6.7660 | **NO_TRADE** |
| DOTUSDT |       0.9740 | **WATCHLIST** |
| LINKUSDT |       7.9940 | **WATCHLIST** |
| ADAUSDT |       0.1694 | **GEM_ALERT** |
| XRPUSDT |       1.1678 | **WATCHLIST** |
| WLDUSDT |       0.5049 | **WATCHLIST** |
| SUIUSDT |       0.7580 | **WATCHLIST** |
| NEARUSDT |       2.1430 | **GEM_ALERT** |
| INJUSDT |       5.6390 | **GEM_ALERT** |
| ARBUSDT |       0.0820 | **WATCHLIST** |
| OPUSDT |       0.0960 | **GEM_ALERT** |
| FETUSDT |       0.2104 | **GEM_ALERT** |
| TAOUSDT |     217.4000 | **WATCHLIST** |
| RENDERUSDT |       1.6430 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 63,320.3700
STATE: GEM_ALERT
SIGNAL: COIL: 4 shrinking candles (45.6% compression) + volume at 0.60x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 45.6% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 2,473 is 0.60x prior-5 avg 4,148 (threshold ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 1,687.9200
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.57, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 48,246 is 0.57x prior-5 avg 84,749 (threshold ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 67.0800
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (68.8%), volume not yet exhausted (ratio=0.73)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 68.9% of widest in window | Volume: No volume exhaustion: last-3 avg 396,437 is 0.73x prior-5 avg 545,216 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 603.8200
STATE: GEM_ALERT
SIGNAL: COIL: 2 shrinking candles (68.9% compression) + volume at 0.59x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 68.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 13,078 is 0.59x prior-5 avg 22,295 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 6.7660
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.80)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 375,257 is 0.80x prior-5 avg 471,490 (need ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.9740
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (63.0%), volume not yet exhausted (ratio=0.71)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 63.0% of widest in window | Volume: No volume exhaustion: last-3 avg 680,897 is 0.71x prior-5 avg 960,264 (need ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 7.9940
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.69, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 327,920 is 0.69x prior-5 avg 478,670 (threshold ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.1694
STATE: GEM_ALERT
SIGNAL: COIL: 5 shrinking candles (72.3% compression) + volume at 0.60x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 72.3% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 21,175,787 is 0.60x prior-5 avg 35,084,296 (threshold ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 1.1678
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.68, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 13,551,420 is 0.68x prior-5 avg 20,041,855 (threshold ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.5049
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (22.7%), volume not yet exhausted (ratio=0.71)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 22.7% of widest in window | Volume: No volume exhaustion: last-3 avg 24,595,138 is 0.71x prior-5 avg 34,448,002 (need ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.7580
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.56, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 5,922,146 is 0.56x prior-5 avg 10,532,298 (threshold ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 2.1430
STATE: GEM_ALERT
SIGNAL: COIL: 4 shrinking candles (58.8% compression) + volume at 0.56x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 58.8% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 4,234,593 is 0.56x prior-5 avg 7,539,685 (threshold ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 5.6390
STATE: GEM_ALERT
SIGNAL: COIL: 3 shrinking candles (51.7% compression) + volume at 0.54x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 51.7% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 203,813 is 0.54x prior-5 avg 377,854 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.0820
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (58.6%), volume not yet exhausted (ratio=0.86)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 58.6% of widest in window | Volume: No volume exhaustion: last-3 avg 7,145,808 is 0.86x prior-5 avg 8,282,889 (need ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.0960
STATE: GEM_ALERT
SIGNAL: COIL: 2 shrinking candles (60.0% compression) + volume at 0.65x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 60.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 3,917,749 is 0.65x prior-5 avg 6,059,683 (threshold ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 0.2104
STATE: GEM_ALERT
SIGNAL: COIL: 2 shrinking candles (62.9% compression) + volume at 0.63x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 62.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 7,055,955 is 0.63x prior-5 avg 11,181,010 (threshold ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 217.4000
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.61, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 10,450 is 0.61x prior-5 avg 17,051 (threshold ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-06-09 05:30 UTC
PRICE: 1.6430
STATE: WATCHLIST
SIGNAL: Compression only: 4 shrinking candles (74.2%), volume not yet exhausted (ratio=0.71)
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 74.2% of widest in window | Volume: No volume exhaustion: last-3 avg 548,138 is 0.71x prior-5 avg 772,035 (need ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*
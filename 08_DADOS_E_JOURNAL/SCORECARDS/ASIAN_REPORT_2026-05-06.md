---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-05-06  
**Time:** 00:00 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC 4H state is WATCHLIST; altcoin GEM_ALERTs downgraded to WATCHLIST  

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
| BTCUSDT |  80,884.8700 | **WATCHLIST** |
| ETHUSDT |   2,360.0500 | **WATCHLIST** |
| SOLUSDT |      86.3000 | **WATCHLIST** |
| BNBUSDT |     630.2800 | **WATCHLIST** |
| AVAXUSDT |       9.4000 | **WATCHLIST** |
| DOTUSDT |       1.2780 | **WATCHLIST** |
| LINKUSDT |       9.7700 | **WATCHLIST** |
| ADAUSDT |       0.2619 | **NO_TRADE** |
| XRPUSDT |       1.4128 | **NO_TRADE** |
| WLDUSDT |       0.2453 | **NO_TRADE** |
| SUIUSDT |       0.9663 | **WATCHLIST** |
| NEARUSDT |       1.2960 | **WATCHLIST** |
| INJUSDT |       3.7660 | **NO_TRADE** |
| ARBUSDT |       0.1197 | **NO_TRADE** |
| OPUSDT |       0.1284 | **WATCHLIST** |
| FETUSDT |       0.2150 | **NO_TRADE** |
| TAOUSDT |     292.3000 | **NO_TRADE** |
| RENDERUSDT |       1.8930 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 80,884.8700
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.54, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 1,509 is 0.54x prior-5 avg 2,818 (threshold ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 2,360.0500
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.66, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 28,688 is 0.66x prior-5 avg 43,725 (threshold ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 86.3000
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (2.6%), volume not yet exhausted (ratio=0.78)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 2.6% of widest in window | Volume: No volume exhaustion: last-3 avg 285,340 is 0.78x prior-5 avg 364,017 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 630.2800
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.69, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 15,386 is 0.69x prior-5 avg 22,387 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 9.4000
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.57, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 188,711 is 0.57x prior-5 avg 332,122 (threshold ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 1.2780
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (0.0% compression) + volume at 0.68x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 630,427 is 0.68x prior-5 avg 925,361 (threshold ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 9.7700
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.45, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 286,003 is 0.45x prior-5 avg 635,641 (threshold ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.2619
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.82)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 18,108,982 is 0.82x prior-5 avg 22,096,731 (need ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 1.4128
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.72)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 7,533,639 is 0.72x prior-5 avg 10,468,674 (need ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.2453
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.00)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 6,580,472 is 1.00x prior-5 avg 6,558,829 (need ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.9663
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.66, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 2,902,562 is 0.66x prior-5 avg 4,421,559 (threshold ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 1.2960
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (0.0%), volume not yet exhausted (ratio=0.79)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: No volume exhaustion: last-3 avg 1,662,803 is 0.79x prior-5 avg 2,099,524 (need ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 3.7660
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.84)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 154,743 is 0.84x prior-5 avg 183,866 (need ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.1197
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.80)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 5,031,119 is 0.80x prior-5 avg 6,306,859 (need ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.1284
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.65, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 4,232,838 is 0.65x prior-5 avg 6,496,982 (threshold ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 0.2150
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.27)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 10,657,616 is 1.27x prior-5 avg 8,416,116 (need ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 292.3000
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.89)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 25,269 is 1.89x prior-5 avg 13,404 (need ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-05-06 00:00 UTC
PRICE: 1.8930
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (2.0%), volume not yet exhausted (ratio=1.22)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 2.0% of widest in window | Volume: No volume exhaustion: last-3 avg 449,940 is 1.22x prior-5 avg 369,149 (need ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*
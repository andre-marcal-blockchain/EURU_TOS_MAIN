---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-05-31  
**Time:** 07:00 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC 4H state is NO_TRADE; altcoin GEM_ALERTs downgraded to WATCHLIST  

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
| BTCUSDT |  74,030.8600 | **NO_TRADE** |
| ETHUSDT |   2,028.3200 | **NO_TRADE** |
| SOLUSDT |      82.9100 | **WATCHLIST** |
| BNBUSDT |     735.5600 | **NO_TRADE** |
| AVAXUSDT |       9.0200 | **WATCHLIST** |
| DOTUSDT |       1.1910 | **WATCHLIST** |
| LINKUSDT |       9.2230 | **WATCHLIST** |
| ADAUSDT |       0.2377 | **WATCHLIST** |
| XRPUSDT |       1.3390 | **WATCHLIST** |
| WLDUSDT |       0.3398 | **WATCHLIST** |
| SUIUSDT |       0.9087 | **WATCHLIST** |
| NEARUSDT |       2.3220 | **NO_TRADE** |
| INJUSDT |       6.5110 | **WATCHLIST** |
| ARBUSDT |       0.1035 | **WATCHLIST** |
| OPUSDT |       0.1202 | **WATCHLIST** |
| FETUSDT |       0.2692 | **WATCHLIST** |
| TAOUSDT |     258.5000 | **NO_TRADE** |
| RENDERUSDT |       2.1260 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 74,030.8600
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.72)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 920 is 0.72x prior-5 avg 1,285 (need ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 2,028.3200
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.74)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 12,671 is 0.74x prior-5 avg 17,028 (need ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 82.9100
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (45.0%), volume not yet exhausted (ratio=0.73)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 45.0% of widest in window | Volume: No volume exhaustion: last-3 avg 128,906 is 0.73x prior-5 avg 176,607 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 735.5600
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.13)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 97,958 is 1.13x prior-5 avg 87,020 (need ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 9.0200
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (53.3%), volume not yet exhausted (ratio=0.72)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 53.3% of widest in window | Volume: No volume exhaustion: last-3 avg 118,839 is 0.72x prior-5 avg 165,925 (need ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 1.1910
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (42.9% compression) + volume at 0.52x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 42.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 451,710 is 0.52x prior-5 avg 871,903 (threshold ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 9.2230
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (46.1% compression) + volume at 0.66x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 46.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 210,626 is 0.66x prior-5 avg 319,934 (threshold ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.2377
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (48.4% compression) + volume at 0.59x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 48.4% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 8,320,982 is 0.59x prior-5 avg 14,125,211 (threshold ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 1.3390
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 3 shrinking candles (61.3% compression) + volume at 0.36x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 61.3% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 5,295,471 is 0.36x prior-5 avg 14,868,531 (threshold ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.3398
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (15.8%), volume not yet exhausted (ratio=0.90)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 15.8% of widest in window | Volume: No volume exhaustion: last-3 avg 23,999,780 is 0.90x prior-5 avg 26,731,816 (need ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.9087
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (50.0%), volume not yet exhausted (ratio=0.73)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 50.0% of widest in window | Volume: No volume exhaustion: last-3 avg 2,843,052 is 0.73x prior-5 avg 3,896,691 (need ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 2.3220
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=0, vol_ratio=0.79)
REASON: Lateralization: No qualifying compression: 0 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 3,352,746 is 0.79x prior-5 avg 4,267,057 (need ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 6.5110
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.43, no range compression detected
REASON: Lateralization: No qualifying compression: 0 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 328,149 is 0.43x prior-5 avg 755,105 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.1035
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (45.5% compression) + volume at 0.65x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 45.5% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 3,569,315 is 0.65x prior-5 avg 5,454,780 (threshold ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.1202
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (50.0% compression) + volume at 0.55x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 50.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 1,388,012 is 0.55x prior-5 avg 2,518,655 (threshold ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 0.2692
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.60, no range compression detected
REASON: Lateralization: No qualifying compression: 0 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 20,820,753 is 0.60x prior-5 avg 34,948,418 (threshold ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 258.5000
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.86)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 8,288 is 0.86x prior-5 avg 9,634 (need ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-05-31 07:00 UTC
PRICE: 2.1260
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (55.8%), volume not yet exhausted (ratio=0.91)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 55.8% of widest in window | Volume: No volume exhaustion: last-3 avg 966,006 is 0.91x prior-5 avg 1,064,239 (need ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*
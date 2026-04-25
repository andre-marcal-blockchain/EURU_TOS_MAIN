# STRUCTURE_HUNTER — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 02_STRUCTURE_HUNTER
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Structure Hunter receives a **Normalized Alert** from Alert Radar plus the price series for the alerted asset.

**Required input fields:**

```
normalized_alert:
  asset               : string
  alert_type          : BREAKOUT | SETUP | STRUCTURE
  direction           : LONG | SHORT | NEUTRAL
  timeframe           : 1D | 4H | 1H
  trigger_price       : float
  zone_id_hint        : string | null    — optional zone reference from alert

price_data:
  primary_tf_series   : list[OHLCV]     — minimum 30 candles on primary TF
  current_price       : float
  current_atr14       : float
  volume_ma20         : float

btc_context:
  btc_structural_status : SETUP | WATCHLIST | NO_TRADE | NOT_CHECKED
  btc_adx14             : float | null

asset_metadata:
  score_engine_tier   : TIER_1 | TIER_2 | TIER_3 | UNRANKED
  session             : MORNING | ASIAN | MANUAL
```

---

## OUTPUTS

A **Structural Map** sent to Breakout Confirmation. See OUTPUT_FORMAT.md for full schema.

Summary of what is produced:
- `structural_status`: BREAKOUT_READY | WATCHLIST | NO_STRUCTURE | INSUFFICIENT_DATA
- Up to 3 scored S/R zones with quality classification
- Formation type and maturity
- Compression assessment (active/inactive, strength)
- BTC alignment flag

---

## VALID SITUATIONS

**Scenario A — BREAKOUT_READY with compression:**
- ETHUSDT 4H alert at 3,200. Price has touched this level 4 times over 18 bars. Last 5 candles show contracting ranges (compression confirmed). One failed break on record. BTC aligned.
- Zone score = 9/10 → `BREAKOUT_READY`

**Scenario B — WATCHLIST (zone valid, no compression):**
- SOLUSDT 4H, clean resistance at 145 with 3 touches. No compression. Price 5% below zone. Zone age = 22 candles (within 30).
- Zone score = 6/10 → `WATCHLIST`

**Scenario C — Zone expired:**
- BNBUSDT: Level at 580 has 3 touches but last touch was 38 candles ago with no retest.
- Zone marked EXPIRED → excluded from active map. Output: `NO_STRUCTURE` (no other valid zones).

**Scenario D — Compression without valid zone:**
- 3 contracting candles present, but price level has only 1 prior touch.
- Report compression status separately. Do not elevate to BREAKOUT_READY. Output `WATCHLIST` with compression note.

---

## INVALID SITUATIONS

**Single-touch zone promotion:**
- Attempting to classify a single swing high as a resistance zone.
- Invalid. Minimum 2 distinct touches required. Output NO_STRUCTURE or WATCHLIST.

**Sub-1H zone definition:**
- Using 15M candle wicks to define zone boundaries for a 4H alert.
- Invalid. Zone boundaries must be defined from the primary TF (4H or higher).

**Score override request:**
- Upstream agent requests minimum zone score of 8 for a setup with only 2 touches and no compression.
- Invalid. Zone score follows the rubric. Cannot be manually elevated.

**Fabricating structure on trending impulse:**
- Asset in a clean uninterrupted trend, no consolidation, no flat zones.
- Output `NO_STRUCTURE`. Do not assign zones to trending impulse legs.

---

## NOTES

- Structure Hunter is an **analysis node**, not a decision gate. It maps; Breakout Confirmation decides.
- If OHLCV data has gaps, flag `DATA_GAPS_DETECTED` in failure flags but continue if ≥ 30 clean candles exist.
- BTC_STRUCTURE_MISSING is a warning, not a blocker. Continue analysis but reduce zone confidence by one tier.
- Pass ALL scored zones (up to 3 primary) to Breakout Confirmation — not just the highest-scoring one.

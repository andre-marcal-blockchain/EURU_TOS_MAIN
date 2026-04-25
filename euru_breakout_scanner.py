"""
Euru OS — Breakout Intelligence Scanner
Implements BL-02 Structure Hunter and BL-03 Breakout Confirmation agents from the
Breakout Intelligence Layer (04_AGENTES/BREAKOUT_LAYER/).

For each asset in the watchlist (4H timeframe, last 50 candles):
    — Structure Hunter: detects S/R zones, compression, proximity to key levels
    — Breakout Confirmation: classifies last closed 4H candle break quality
    — breakout_raw_score (0–100) across 4 scoring dimensions

Runs standalone or as a library imported by euru_morning_scan.py.

Output: 08_DADOS_E_JOURNAL/SCORECARDS/BREAKOUT_SCAN_<YYYY-MM-DD>.md
"""

import json
import math
import os
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SYMBOLS = [
    "BTCUSDT", "ETHUSDT",
    "SOLUSDT", "BNBUSDT", "AVAXUSDT", "DOTUSDT",
    "LINKUSDT", "ADAUSDT", "XRPUSDT", "WLDUSDT",
    "SUIUSDT", "NEARUSDT", "INJUSDT", "ARBUSDT",
    "OPUSDT", "FETUSDT", "TAOUSDT", "RENDERUSDT",
]
BINANCE_BASE = "https://api.binance.com/api/v3"
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "SCORECARDS")

# Structure Hunter parameters
ZONE_TOLERANCE_PCT   = 2.0    # % price tolerance for grouping touches into a zone
ZONE_MIN_TOUCHES     = 2      # min touches to qualify as a valid S/R zone
ATR_PROXIMITY_MULT   = 1.5    # flag if current price is within this many ATRs of a zone
ATR_PERIOD           = 14     # Wilder ATR period (same as euru_flow_analyst.py)
KLINES_LIMIT         = 50     # 4H candles to fetch per asset

# Compression parameters — fixed to match euru_asian_scan.py
COMPRESSION_RATIO       = 1.15  # range[i] <= range[i-1] * 1.15 counts as compressing
COMPRESSION_MIN_CANDLES = 3     # need this many consecutive compressing candles

# Breakout Confirmation thresholds
VOLUME_CONFIRM_RATIO = 0.8    # breakout volume must be >= 0.8x 5-period average
WICK_REJECT_MAX      = 0.40   # wick-to-body ratio threshold: <= 0.40 for CONFIRMED

# Error handling
RETRY_MAX           = 3
RETRY_DELAY_SECONDS = 5


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _fetch_json(url: str) -> dict | list:
    req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def _fetch_json_with_retry(url: str) -> dict | list:
    """Calls _fetch_json up to RETRY_MAX times with RETRY_DELAY_SECONDS between attempts."""
    last_exc: Exception | None = None
    for attempt in range(1, RETRY_MAX + 1):
        try:
            return _fetch_json(url)
        except Exception as e:
            last_exc = e
            if attempt < RETRY_MAX:
                print(f"    [Retry {attempt}/{RETRY_MAX}] {e} — retrying in {RETRY_DELAY_SECONDS}s...")
                time.sleep(RETRY_DELAY_SECONDS)
    raise last_exc  # type: ignore[misc]


def get_4h_klines(symbol: str, limit: int = KLINES_LIMIT) -> list[dict]:
    """
    Returns `limit` 4H candles from Binance (most recent last).
    Note: the last entry may still be forming (open candle).
    Uses base volume (k[5]) consistent with euru_asian_scan.py.
    """
    raw = _fetch_json_with_retry(
        f"{BINANCE_BASE}/klines?symbol={symbol}&interval=4h&limit={limit}"
    )
    candles = []
    for k in raw:
        candles.append({
            "open":       float(k[1]),
            "high":       float(k[2]),
            "low":        float(k[3]),
            "close":      float(k[4]),
            "volume":     float(k[5]),   # base volume
            "close_time": int(k[6]),
        })
    return candles


# ---------------------------------------------------------------------------
# ATR — Wilder smoothing on 4H candles
# ---------------------------------------------------------------------------

def _calculate_atr(candles: list[dict]) -> float:
    """
    Wilder ATR over ATR_PERIOD (14) bars. Ported from euru_flow_analyst.py,
    adapted for 4H candle input. Returns float('nan') if insufficient data.
    """
    if len(candles) < ATR_PERIOD + 1:
        return float("nan")

    tr_values = []
    for i in range(1, len(candles)):
        tr = max(
            candles[i]["high"]  - candles[i]["low"],
            abs(candles[i]["high"] - candles[i - 1]["close"]),
            abs(candles[i]["low"]  - candles[i - 1]["close"]),
        )
        tr_values.append(tr)

    atr = sum(tr_values[:ATR_PERIOD]) / ATR_PERIOD
    for tr in tr_values[ATR_PERIOD:]:
        atr = (atr * (ATR_PERIOD - 1) + tr) / ATR_PERIOD

    return atr


# ---------------------------------------------------------------------------
# Structure Hunter — Agent BL-02
# ---------------------------------------------------------------------------

def _detect_zones(candles: list[dict]) -> list[dict]:
    """
    Identifies support and resistance zones from the closed candle set.

    Method:
        1. Collect all candle highs and lows as candidate price levels.
        2. Sort by price and merge adjacent levels within ZONE_TOLERANCE_PCT
           using a linear chain merge (consecutive pair comparison). This handles
           crypto zones that span a few percent without artificial splits.
        3. Groups with ZONE_MIN_TOUCHES (2+) elements are valid S/R zones.

    Each zone is classified:
        RESISTANCE — zone level is above the most recent close price
        SUPPORT    — zone level is at or below the most recent close price

    Maturity score (0–1) weights: touches 50%, recency 30%, tightness 20%.

    Returns list of zone dicts sorted by maturity_score descending.
    """
    # Use only closed candles (exclude the still-forming last candle)
    closed = candles[:-1]
    if len(closed) < 2:
        return []

    current_close = candles[-1]["close"]
    n = len(closed)

    # Collect (price, candle_index, kind) for all highs and lows
    candidates: list[tuple[float, int, str]] = []
    for i, c in enumerate(closed):
        candidates.append((c["high"], i, "high"))
        candidates.append((c["low"],  i, "low"))

    # Sort by price ascending for linear chain merge
    candidates.sort(key=lambda x: x[0])

    if not candidates:
        return []

    # Linear chain merge: group consecutive levels within ZONE_TOLERANCE_PCT
    clusters: list[list[tuple[float, int, str]]] = [[candidates[0]]]
    for entry in candidates[1:]:
        level    = entry[0]
        prev_lvl = clusters[-1][-1][0]
        if prev_lvl > 0 and abs(level - prev_lvl) / prev_lvl * 100 <= ZONE_TOLERANCE_PCT:
            clusters[-1].append(entry)
        else:
            clusters.append([entry])

    zones = []
    for cluster in clusters:
        if len(cluster) < ZONE_MIN_TOUCHES:
            continue

        prices         = [p for p, _, _ in cluster]
        indices        = [i for _, i, _ in cluster]
        level          = sum(prices) / len(prices)
        last_touch_idx = max(indices)
        width          = max(prices) - min(prices)
        touches        = len(cluster)

        # Maturity score
        touch_score   = min(touches / 6.0, 1.0)
        recency_score = last_touch_idx / (n - 1) if n > 1 else 0.0
        tightness     = 1.0 - min((width / level if level > 0 else 0.05), 0.05) / 0.05
        maturity      = touch_score * 0.5 + recency_score * 0.3 + tightness * 0.2

        zone_type = "RESISTANCE" if level > current_close else "SUPPORT"

        zones.append({
            "level":          round(level, 8),
            "zone_type":      zone_type,
            "touches":        touches,
            "last_touch_idx": last_touch_idx,
            "width":          round(width, 8),
            "maturity_score": round(maturity, 4),
        })

    zones.sort(key=lambda z: z["maturity_score"], reverse=True)
    return zones


def _detect_compression(candles: list[dict]) -> dict:
    """
    Detects 4H range compression using the fixed parameters from euru_asian_scan.py.

    Inspects the last (COMPRESSION_MIN_CANDLES + 3) closed candles and counts
    consecutive pairs where range[i] <= range[i-1] * COMPRESSION_RATIO (1.15).
    Detected when consecutive_count >= COMPRESSION_MIN_CANDLES - 1 (2 pairs = 3 candles).

    Returns: detected (bool), consecutive_count (int), compression_pct (float), note (str).
    """
    closed = candles[:-1]
    window = closed[-(COMPRESSION_MIN_CANDLES + 3):]

    if len(window) < 2:
        return {
            "detected": False, "consecutive_count": 0,
            "compression_pct": 0.0, "note": "Insufficient candle data",
        }

    ranges = [c["high"] - c["low"] for c in window]

    consecutive_count = 0
    for i in range(len(ranges) - 1, 0, -1):
        if ranges[i] <= ranges[i - 1] * COMPRESSION_RATIO:
            consecutive_count += 1
        else:
            break

    detected = consecutive_count >= (COMPRESSION_MIN_CANDLES - 1)
    max_r = max(ranges)
    compression_pct = (min(ranges) / max_r * 100) if max_r > 0 else 0.0

    if detected:
        note = (
            f"Compression confirmed: {consecutive_count} consecutive compressing pairs "
            f"(tightest range = {compression_pct:.1f}% of widest in window)"
        )
    else:
        note = (
            f"No compression: {consecutive_count} compressing pair(s) "
            f"(need {COMPRESSION_MIN_CANDLES - 1})"
        )

    return {
        "detected":          detected,
        "consecutive_count": consecutive_count,
        "compression_pct":   round(compression_pct, 2),
        "note":              note,
    }


def _run_structure_hunter(candles: list[dict], atr: float) -> dict:
    """
    Structure Hunter (BL-02) — full assessment for one asset.

    Returns:
        zone_detected      (bool)   — at least one valid zone found
        zones              (list)   — all valid zones sorted by maturity descending
        best_zone          (dict)   — highest-maturity zone, or None
        near_zone          (bool)   — price is within ATR_PROXIMITY_MULT * ATR of best zone
        compression        (dict)   — from _detect_compression()
        structural_status  (str)    — "STRUCTURE" | "NO_STRUCTURE"
        notes              (str)    — human-readable summary
    """
    zones       = _detect_zones(candles)
    compression = _detect_compression(candles)
    best_zone   = zones[0] if zones else None
    near_zone   = False

    if best_zone and not math.isnan(atr) and atr > 0:
        distance  = abs(candles[-1]["close"] - best_zone["level"])
        near_zone = distance <= ATR_PROXIMITY_MULT * atr

    zone_detected     = len(zones) > 0
    structural_status = "STRUCTURE" if zone_detected else "NO_STRUCTURE"

    parts = [f"{len(zones)} zone(s) found"]
    if best_zone:
        parts.append(
            f"Best: {best_zone['level']:,.6f} ({best_zone['zone_type']}, "
            f"{best_zone['touches']} touches, maturity={best_zone['maturity_score']:.2f})"
        )
    if near_zone:
        parts.append(f"Price within {ATR_PROXIMITY_MULT}x ATR of best zone")
    parts.append(compression["note"])

    return {
        "zone_detected":     zone_detected,
        "zones":             zones,
        "best_zone":         best_zone,
        "near_zone":         near_zone,
        "compression":       compression,
        "structural_status": structural_status,
        "notes":             " | ".join(parts),
    }


# ---------------------------------------------------------------------------
# Breakout Confirmation — Agent BL-03
# ---------------------------------------------------------------------------

def _confirm_breakout(candles: list[dict], zones: list[dict]) -> dict:
    """
    Breakout Confirmation (BL-03).

    Uses the last CLOSED 4H candle (candles[-2]) as the breakout candle.
    candles[-1] is the still-forming current candle (excluded from classification).

    Three conditions evaluated:
        1. Close is OUTSIDE the zone (not just a wick pierce)
        2. Volume >= VOLUME_CONFIRM_RATIO (0.8x) of the 5-period average
        3. Wick rejection <= WICK_REJECT_MAX (40%) of candle body

    Classification:
        CONFIRMED — all three conditions met
        WEAK      — close outside zone, but volume or wick condition fails
        FAKEOUT   — wick pierced the zone but candle closed back inside
        NONE      — no zone was touched by last closed candle

    Zones are checked in maturity order (best first). First hit wins.

    Returns:
        breakout_status (str)   — CONFIRMED | WEAK | FAKEOUT | NONE
        direction       (str)   — LONG | SHORT | NONE
        key_level       (float) — zone level broken, or 0.0 if NONE
        candle_quality  (float) — body / total_range ratio (0–1)
        volume_ratio    (float) — breakout candle volume / 5-period avg
        wick_rejection  (float) — rejection wick / body ratio
        notes           (str)
    """
    if len(candles) < 7 or not zones:
        return {
            "breakout_status": "NONE", "direction": "NONE", "key_level": 0.0,
            "candle_quality": 0.0, "volume_ratio": 0.0, "wick_rejection": 0.0,
            "notes": "Insufficient candles or no zones detected",
        }

    candle = candles[-2]   # last fully closed 4H candle
    o, h, l, c = candle["open"], candle["high"], candle["low"], candle["close"]

    # Volume: compare against mean of the 5 closed candles preceding the breakout candle
    vol_window = candles[-7:-2]
    avg_vol_5  = sum(x["volume"] for x in vol_window) / len(vol_window) if vol_window else 0.0
    volume_ratio = candle["volume"] / avg_vol_5 if avg_vol_5 > 0 else 0.0

    # Candle body metrics
    body        = abs(c - o)
    total_range = h - l
    candle_quality = body / total_range if total_range > 0 else 0.0

    # Wick rejection: upper wick for bullish breakout, lower wick for bearish
    bullish = c >= o
    if bullish:
        wick_rejection = (h - c) / body if body > 0 else float("inf")
    else:
        wick_rejection = (c - l) / body if body > 0 else float("inf")

    # Find the highest-maturity zone breached by this candle
    broken_zone  = None
    direction    = "NONE"
    close_outside = False

    # --- Resistance breakout (LONG) ---
    for zone in zones:
        if zone["zone_type"] != "RESISTANCE":
            continue
        lvl = zone["level"]
        if h > lvl:                     # wick or close touches resistance
            broken_zone   = zone
            direction     = "LONG"
            close_outside = c > lvl     # True = clean close, False = wick-only (fakeout)
            break

    # --- Support breakdown (SHORT) — only if no resistance found ---
    if broken_zone is None:
        for zone in zones:
            if zone["zone_type"] != "SUPPORT":
                continue
            lvl = zone["level"]
            if l < lvl:                 # wick or close reaches support
                broken_zone   = zone
                direction     = "SHORT"
                close_outside = c < lvl
                break

    if broken_zone is None:
        return {
            "breakout_status": "NONE", "direction": "NONE", "key_level": 0.0,
            "candle_quality":  round(candle_quality, 4),
            "volume_ratio":    round(volume_ratio, 4),
            "wick_rejection":  round(min(wick_rejection, 99.0), 4),
            "notes": "No zone reached by last closed 4H candle",
        }

    lvl     = broken_zone["level"]
    vol_ok  = volume_ratio  >= VOLUME_CONFIRM_RATIO
    wick_ok = wick_rejection <= WICK_REJECT_MAX

    if not close_outside:
        status = "FAKEOUT"
        notes  = (
            f"Wick pierced {broken_zone['zone_type']} at {lvl:,.6f} "
            f"but closed back inside — FAKEOUT"
        )
    elif vol_ok and wick_ok:
        status = "CONFIRMED"
        notes  = (
            f"Close {c:,.6f} broke {broken_zone['zone_type']} {lvl:,.6f} — "
            f"vol {volume_ratio:.2f}x avg, wick_reject {wick_rejection:.2f} — CONFIRMED"
        )
    else:
        status = "WEAK"
        flags  = []
        if not vol_ok:
            flags.append(f"low vol ({volume_ratio:.2f}x < {VOLUME_CONFIRM_RATIO}x)")
        if not wick_ok:
            flags.append(f"high wick ({wick_rejection:.2f} > {WICK_REJECT_MAX})")
        notes = (
            f"Close {c:,.6f} broke {broken_zone['zone_type']} {lvl:,.6f} — "
            f"WEAK ({', '.join(flags)})"
        )

    return {
        "breakout_status": status,
        "direction":       direction,
        "key_level":       round(lvl, 8),
        "candle_quality":  round(candle_quality, 4),
        "volume_ratio":    round(volume_ratio, 4),
        "wick_rejection":  round(min(wick_rejection, 99.0), 4),
        "notes":           notes,
    }


# ---------------------------------------------------------------------------
# Breakout Raw Score (0–100)
# ---------------------------------------------------------------------------

def _calculate_raw_score(structure: dict, breakout: dict) -> int:
    """
    Calculates breakout_raw_score (0–100) across four dimensions:

        Zone touches (max 25)  — based on best_zone.touches
        Candle quality (max 30) — body/range quality + wick rejection quality
        Volume confirm (max 25) — volume_ratio vs graduated thresholds
        Compression (max 20)   — compression detected before breakout

    Returns 0 if breakout_status is NONE or FAKEOUT (no actionable signal).
    """
    if breakout["breakout_status"] in ("NONE", "FAKEOUT"):
        return 0

    # 1. Zone touches (max 25)
    touches = structure["best_zone"]["touches"] if structure["best_zone"] else 0
    if touches >= 5:
        touch_pts = 25
    elif touches == 4:
        touch_pts = 20
    elif touches == 3:
        touch_pts = 15
    else:
        touch_pts = 10   # minimum 2 touches required to reach this path

    # 2. Candle quality (max 30) — body quality (0–15) + wick quality (0–15)
    cq        = breakout["candle_quality"]          # 0–1, higher = cleaner body
    wr        = breakout["wick_rejection"]           # lower = less rejection
    body_pts  = round(cq * 15)
    wr_norm   = max(0.0, 1.0 - wr / max(WICK_REJECT_MAX, 0.001))
    wick_pts  = round(wr_norm * 15)
    candle_pts = body_pts + wick_pts                 # 0–30

    # 3. Volume confirmation (max 25)
    vr = breakout["volume_ratio"]
    if vr >= 2.0:
        vol_pts = 25
    elif vr >= 1.5:
        vol_pts = 20
    elif vr >= 1.0:
        vol_pts = 15
    elif vr >= VOLUME_CONFIRM_RATIO:
        vol_pts = 10
    else:
        vol_pts = 0

    # 4. Compression pre-breakout (max 20)
    comp = structure.get("compression", {})
    if comp.get("detected"):
        comp_pts = 20
    elif comp.get("consecutive_count", 0) >= 1:
        comp_pts = 10
    else:
        comp_pts = 0

    return min(touch_pts + candle_pts + vol_pts + comp_pts, 100)


# ---------------------------------------------------------------------------
# Full per-asset assessment
# ---------------------------------------------------------------------------

def assess_breakout(symbol: str, candles: list[dict]) -> dict:
    """
    Runs the full Breakout Intelligence pipeline for one asset.

    Returns a structured dict with all BL-02 + BL-03 output fields:
        symbol              (str)
        price               (float) — current price (last candle close)
        atr                 (float|None) — 4H ATR(14), None if insufficient data
        zone_detected       (bool)
        structural_status   (str)   — "STRUCTURE" | "NO_STRUCTURE"
        best_zone           (dict|None)
        near_zone           (bool)
        compression         (dict)
        breakout_status     (str)   — CONFIRMED | WEAK | FAKEOUT | NONE
        direction           (str)   — LONG | SHORT | NONE
        key_level           (float) — broken zone level, or best zone level if no break
        candle_quality      (float)
        volume_ratio        (float)
        wick_rejection      (float)
        breakout_raw_score  (int)   — 0–100
        notes               (str)
    """
    atr       = _calculate_atr(candles)
    structure = _run_structure_hunter(candles, atr)
    breakout  = _confirm_breakout(candles, structure["zones"])
    raw_score = _calculate_raw_score(structure, breakout)

    # key_level: use broken zone if breakout exists, else fall back to best zone
    key_level = breakout["key_level"]
    if key_level == 0.0 and structure["best_zone"]:
        key_level = structure["best_zone"]["level"]

    notes_parts = [breakout["notes"]]
    if structure["near_zone"] and breakout["breakout_status"] == "NONE":
        notes_parts.append("Price near key zone — watch for breakout")

    return {
        "symbol":             symbol,
        "price":              candles[-1]["close"],
        "atr":                round(atr, 8) if not math.isnan(atr) else None,
        "zone_detected":      structure["zone_detected"],
        "structural_status":  structure["structural_status"],
        "best_zone":          structure["best_zone"],
        "near_zone":          structure["near_zone"],
        "compression":        structure["compression"],
        "breakout_status":    breakout["breakout_status"],
        "direction":          breakout["direction"],
        "key_level":          round(key_level, 8),
        "candle_quality":     breakout["candle_quality"],
        "volume_ratio":       breakout["volume_ratio"],
        "wick_rejection":     breakout["wick_rejection"],
        "breakout_raw_score": raw_score,
        "notes":              " | ".join(notes_parts),
    }


# ---------------------------------------------------------------------------
# Public library interface (imported by euru_morning_scan.py)
# ---------------------------------------------------------------------------

def run_scan(symbols: list[str] | None = None, run_dt: datetime | None = None) -> dict:
    """
    Library entry point called by euru_morning_scan.py.

    Args:
        symbols: Symbols to scan. Defaults to SYMBOLS (same 18 as morning scan).
        run_dt:  Datetime for the report header. Defaults to now(UTC).

    Returns:
        dict with keys:
            assessments (list[dict]) — one entry per scanned asset
            failed      (list[str])  — symbols that errored out
            run_dt      (datetime)   — timestamp used
    """
    symbols = symbols or SYMBOLS
    run_dt  = run_dt  or datetime.now(timezone.utc)

    assessments: list[dict] = []
    failed: list[str] = []

    for symbol in symbols:
        try:
            candles = get_4h_klines(symbol, limit=KLINES_LIMIT)
            if len(candles) < ATR_PERIOD + 3:
                print(f"  [Breakout] {symbol}: insufficient candles ({len(candles)}), skipping")
                failed.append(symbol)
                continue

            result = assess_breakout(symbol, candles)
            assessments.append(result)

            print(
                f"  [Breakout] {symbol:10s}  "
                f"price={result['price']:>12,.4f}  "
                f"zones={'YES' if result['zone_detected'] else 'NO ':3s}  "
                f"status={result['breakout_status']:9s}  "
                f"dir={result['direction']:5s}  "
                f"score={result['breakout_raw_score']:3d}"
            )
        except urllib.error.URLError as e:
            print(f"  [Breakout] {symbol}: network error — {e}")
            failed.append(symbol)
        except Exception as e:
            print(f"  [Breakout] {symbol}: error — {e}")
            failed.append(symbol)

    return {"assessments": assessments, "failed": failed, "run_dt": run_dt}


def format_breakout_section(scan_results: dict) -> str:
    """
    Formats the Breakout Intelligence output as a Markdown section for
    insertion into the morning SCOUT_REPORT.

    Called by euru_morning_scan.py after run_scan() completes.
    """
    assessments = scan_results["assessments"]
    failed      = scan_results["failed"]
    run_dt      = scan_results["run_dt"]
    ts          = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "---",
        "",
        "## Breakout Intelligence Layer (4H)",
        "",
        f"*Scan: {ts} — BL-02 Structure Hunter + BL-03 Breakout Confirmation*  ",
        f"*Assets: {len(assessments)} scanned*"
        + (f" | *Failed: {', '.join(failed)}*" if failed else ""),
        "",
    ]

    # Summary table — sorted by score descending
    sorted_a = sorted(assessments, key=lambda a: a["breakout_raw_score"], reverse=True)

    lines += [
        "| Symbol | Price (USDT) | Zone | Breakout | Dir | Score | Key Level | Comp |",
        "|--------|-------------|------|----------|-----|-------|-----------|------|",
    ]
    for a in sorted_a:
        comp_str  = "YES" if a["compression"]["detected"] else "NO"
        score_str = f"**{a['breakout_raw_score']}**" if a["breakout_raw_score"] > 0 else "0"
        lines.append(
            f"| {a['symbol']} "
            f"| {a['price']:>12,.4f} "
            f"| {'YES' if a['zone_detected'] else 'NO'} "
            f"| **{a['breakout_status']}** "
            f"| {a['direction']} "
            f"| {score_str} "
            f"| {a['key_level']:,.4f} "
            f"| {comp_str} |"
        )

    # Active breakout detail blocks
    active = [a for a in sorted_a if a["breakout_status"] in ("CONFIRMED", "WEAK")]
    fakeouts = [a for a in sorted_a if a["breakout_status"] == "FAKEOUT"]

    if active:
        lines += ["", "### Active Breakouts", ""]
        for a in active:
            bz = a["best_zone"]
            lines.append(f"**{a['symbol']}** — `{a['breakout_status']}` `{a['direction']}` | Score: **{a['breakout_raw_score']}** | Key Level: {a['key_level']:,.4f}")
            lines.append("")
            lines.append("```")
            lines.append(f"BREAKOUT_STATUS:    {a['breakout_status']}")
            lines.append(f"DIRECTION:          {a['direction']}")
            lines.append(f"KEY_LEVEL:          {a['key_level']:,.6f}")
            lines.append(f"BREAKOUT_RAW_SCORE: {a['breakout_raw_score']}/100")
            lines.append(f"CANDLE_QUALITY:     {a['candle_quality']:.4f}  (body/range ratio)")
            lines.append(f"VOLUME_RATIO:       {a['volume_ratio']:.4f}x  (vs 5-period avg)")
            lines.append(f"WICK_REJECTION:     {a['wick_rejection']:.4f}  (<= {WICK_REJECT_MAX} = clean)")
            if bz:
                lines.append(f"BEST_ZONE:          {bz['level']:,.6f} ({bz['zone_type']}, {bz['touches']} touches, maturity={bz['maturity_score']:.2f})")
            lines.append(f"COMPRESSION:        {a['compression']['detected']} ({a['compression']['note']})")
            lines.append(f"ATR_4H:             {a['atr'] if a['atr'] is not None else 'N/A'}")
            lines.append(f"NOTES:              {a['notes']}")
            lines.append("```")
            lines.append("")
    else:
        lines += ["", "*No confirmed or weak breakouts in this scan.*", ""]

    if fakeouts:
        lines += ["", "### Fakeout Alerts", ""]
        for a in fakeouts:
            lines.append(
                f"- **{a['symbol']}**: {a['direction']} fakeout at {a['key_level']:,.4f} — {a['notes']}"
            )
        lines.append("")

    # Near-zone watch list (no breakout but price is close)
    near = [a for a in sorted_a if a["near_zone"] and a["breakout_status"] == "NONE"]
    if near:
        lines += ["", "### Near-Zone Watchlist", ""]
        for a in near:
            bz = a["best_zone"]
            dist_str = ""
            if bz and a["atr"]:
                dist = abs(a["price"] - bz["level"])
                dist_str = f" ({dist / a['atr']:.1f}x ATR away)"
            lines.append(
                f"- **{a['symbol']}**: price {a['price']:,.4f} near {bz['zone_type'] if bz else '?'} "
                f"at {a['key_level']:,.4f}{dist_str}"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Standalone report builder
# ---------------------------------------------------------------------------

def _build_full_report(scan_results: dict) -> str:
    """Builds the standalone BREAKOUT_SCAN_YYYY-MM-DD.md report."""
    assessments = scan_results["assessments"]
    failed      = scan_results["failed"]
    run_dt      = scan_results["run_dt"]

    date_str = run_dt.strftime("%Y-%m-%d")
    time_str = run_dt.strftime("%H:%M UTC")
    ts       = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    # Counts
    n_confirmed = sum(1 for a in assessments if a["breakout_status"] == "CONFIRMED")
    n_weak      = sum(1 for a in assessments if a["breakout_status"] == "WEAK")
    n_fakeout   = sum(1 for a in assessments if a["breakout_status"] == "FAKEOUT")
    n_near      = sum(1 for a in assessments if a["near_zone"] and a["breakout_status"] == "NONE")
    n_none      = len(assessments) - n_confirmed - n_weak - n_fakeout

    lines = [
        "# Euru OS — Breakout Intelligence Scan",
        f"**Date:** {date_str}  ",
        f"**Time:** {time_str}  ",
        f"**Timeframe:** 4H (last {KLINES_LIMIT} candles)  ",
        f"**Assets scanned:** {len(assessments)}  ",
        f"**Failed:** {len(failed)}  ",
        f"**Mode:** READ_ONLY  ",
        "",
        "```",
        f"CONFIRMED:  {n_confirmed}",
        f"WEAK:       {n_weak}",
        f"FAKEOUT:    {n_fakeout}",
        f"NONE:       {n_none}",
        f"NEAR_ZONE:  {n_near}  (no breakout but price within {ATR_PROXIMITY_MULT}x ATR of zone)",
        "```",
        "",
        "---",
        "",
    ]

    if failed:
        lines += [f"> **Failed symbols:** {', '.join(failed)}", ""]

    # Summary table sorted by score descending
    sorted_a = sorted(assessments, key=lambda a: a["breakout_raw_score"], reverse=True)

    lines += [
        "## Breakout Summary",
        "",
        "| Symbol | Price | Zone | Breakout | Dir | Score | Key Level | Comp | ATR(4H) |",
        "|--------|-------|------|----------|-----|-------|-----------|------|---------|",
    ]
    for a in sorted_a:
        atr_str  = f"{a['atr']:,.4f}" if a["atr"] is not None else "N/A"
        comp_str = "YES" if a["compression"]["detected"] else "NO"
        lines.append(
            f"| {a['symbol']} "
            f"| {a['price']:>12,.4f} "
            f"| {'YES' if a['zone_detected'] else 'NO'} "
            f"| **{a['breakout_status']}** "
            f"| {a['direction']} "
            f"| **{a['breakout_raw_score']}** "
            f"| {a['key_level']:,.4f} "
            f"| {comp_str} "
            f"| {atr_str} |"
        )

    lines.append("")   # blank line after table before next section

    # Active breakout detail blocks
    active = [a for a in sorted_a if a["breakout_status"] in ("CONFIRMED", "WEAK")]
    if active:
        lines += ["---", "", "## Active Breakouts", ""]
        for a in active:
            bz = a["best_zone"]
            lines.append(f"### {a['symbol']} — {a['breakout_status']} {a['direction']}")
            lines.append("")
            lines.append("```")
            lines.append(f"AGENT: Breakout Intelligence Layer (BL-02 + BL-03)")
            lines.append(f"SYMBOL: {a['symbol']}")
            lines.append(f"TIMEFRAME: 4H")
            lines.append(f"DATE: {ts}")
            lines.append(f"STRUCTURAL_STATUS:  {a['structural_status']}")
            lines.append(f"ZONE_DETECTED:      {a['zone_detected']}")
            if bz:
                lines.append(
                    f"BEST_ZONE:          {bz['level']:,.6f} ({bz['zone_type']}, "
                    f"{bz['touches']} touches, maturity={bz['maturity_score']:.2f}, "
                    f"width={bz['width']:,.6f})"
                )
            lines.append(f"COMPRESSION:        {a['compression']['detected']} | {a['compression']['note']}")
            lines.append(f"NEAR_ZONE:          {a['near_zone']}")
            lines.append(f"---")
            lines.append(f"BREAKOUT_STATUS:    {a['breakout_status']}")
            lines.append(f"DIRECTION:          {a['direction']}")
            lines.append(f"KEY_LEVEL:          {a['key_level']:,.6f}")
            lines.append(f"BREAKOUT_RAW_SCORE: {a['breakout_raw_score']}/100")
            lines.append(f"CANDLE_QUALITY:     {a['candle_quality']:.4f}  (body/range ratio; 1.0 = pure body)")
            lines.append(f"VOLUME_RATIO:       {a['volume_ratio']:.4f}x  (vs 5-candle avg; >= {VOLUME_CONFIRM_RATIO} required)")
            lines.append(f"WICK_REJECTION:     {a['wick_rejection']:.4f}  (<= {WICK_REJECT_MAX} = acceptable)")
            lines.append(f"ATR_4H:             {a['atr'] if a['atr'] is not None else 'N/A'}")
            lines.append(f"NOTES: {a['notes']}")
            lines.append("```")
            lines.append("")

    # Fakeout detail
    fakeouts = [a for a in sorted_a if a["breakout_status"] == "FAKEOUT"]
    if fakeouts:
        lines += ["---", "", "## Fakeout Alerts", ""]
        for a in fakeouts:
            lines.append(f"- **{a['symbol']}**: {a['direction']} fakeout at {a['key_level']:,.4f} — {a['notes']}")
        lines.append("")

    # Near-zone watchlist
    near = [a for a in sorted_a if a["near_zone"] and a["breakout_status"] == "NONE"]
    if near:
        lines += ["---", "", f"## Near-Zone Watchlist (within {ATR_PROXIMITY_MULT}x ATR)", ""]
        for a in near:
            bz = a["best_zone"]
            if bz and a["atr"]:
                dist   = abs(a["price"] - bz["level"])
                n_atrs = dist / a["atr"]
                lines.append(
                    f"- **{a['symbol']}**: price={a['price']:,.4f}, "
                    f"{bz['zone_type']}={bz['level']:,.4f}, "
                    f"distance={n_atrs:.2f}x ATR, "
                    f"compression={'YES' if a['compression']['detected'] else 'NO'}"
                )
        lines.append("")

    # All remaining assets (NONE, no near zone)
    others = [a for a in sorted_a if a["breakout_status"] == "NONE" and not a["near_zone"]]
    if others:
        lines += ["---", "", "## No Signal", ""]
        for a in others:
            bz = a["best_zone"]
            bz_str = f"best zone {bz['level']:,.4f}" if bz else "no zone"
            lines.append(
                f"- **{a['symbol']}**: {bz_str} | "
                f"compression={'YES' if a['compression']['detected'] else 'NO'} | "
                f"{a['notes']}"
            )
        lines.append("")

    lines += [
        "---",
        "",
        f"*Generated by euru_breakout_scanner.py — Euru OS READ_ONLY phase*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main — standalone execution
# ---------------------------------------------------------------------------

def main():
    run_dt   = datetime.now(timezone.utc)
    date_str = run_dt.strftime("%Y-%m-%d")

    print(f"Euru OS — Breakout Intelligence Scanner [{date_str}]")
    print(f"Agents: BL-02 Structure Hunter + BL-03 Breakout Confirmation")
    print(f"Timeframe: 4H | Assets: {len(SYMBOLS)} | Lookback: {KLINES_LIMIT} candles\n")

    scan_results = run_scan(SYMBOLS, run_dt)
    assessments  = scan_results["assessments"]
    failed       = scan_results["failed"]

    if not assessments:
        print("\nNo data retrieved. Aborting report.")
        return

    # Console summary
    confirmed = [a for a in assessments if a["breakout_status"] == "CONFIRMED"]
    weak      = [a for a in assessments if a["breakout_status"] == "WEAK"]
    fakeout   = [a for a in assessments if a["breakout_status"] == "FAKEOUT"]
    near      = [a for a in assessments if a["near_zone"] and a["breakout_status"] == "NONE"]

    print(f"\n{'='*60}")
    print(f"Breakout Summary [{date_str}]")
    print(f"  CONFIRMED: {len(confirmed)}")
    print(f"  WEAK:      {len(weak)}")
    print(f"  FAKEOUT:   {len(fakeout)}")
    print(f"  NEAR_ZONE: {len(near)}")
    print(f"  NONE:      {len(assessments) - len(confirmed) - len(weak) - len(fakeout)}")
    if failed:
        print(f"  FAILED:    {', '.join(failed)}")

    if confirmed or weak:
        print(f"\nActive Breakouts (sorted by score):")
        for a in sorted(confirmed + weak, key=lambda x: x["breakout_raw_score"], reverse=True):
            print(
                f"  {a['symbol']:12s}  {a['breakout_status']:9s}  "
                f"{a['direction']:5s}  score={a['breakout_raw_score']:3d}  "
                f"level={a['key_level']:,.4f}"
            )
    else:
        print("\nNo confirmed or weak breakouts in this scan.")

    if near:
        print(f"\nNear-Zone Watchlist:")
        for a in near:
            bz = a["best_zone"]
            if bz:
                print(f"  {a['symbol']:12s}  {bz['zone_type']:10s} at {bz['level']:,.4f}")

    # Build and save report
    report = _build_full_report(scan_results)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"BREAKOUT_SCAN_{date_str}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved => {output_path}")


if __name__ == "__main__":
    main()

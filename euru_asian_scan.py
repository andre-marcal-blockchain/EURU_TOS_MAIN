"""
Euru OS — Asian Session Scan
Designed to run at 00:00 UTC at the open of the Asian trading session.

Focus: Aguiar Protocol Module 05 — Lateralization & Compression Detection.
This scan looks for 5-6 consecutive 4H candles whose trading ranges are
progressively shrinking (body + wick compression), signalling a coil before
a potential directional breakout. Volume exhaustion at the compression point
is a secondary confirming signal. Assets meeting both criteria are flagged as
GEM_ALERT for manual review at the next session open.

Methodology differs from the Morning Scan (daily structure bias) — here every
assessment is done on the 4H timeframe. The BTC master filter still applies:
if BTC 4H trend is SIDEWAYS or BEARISH, all altcoin GEM_ALERTs are downgraded
to WATCHLIST.

Output: 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_<YYYY-MM-DD>.md
"""

import json
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

# Aguiar Protocol Module 05 — compression parameters
COMPRESSION_CANDLES      = 6    # total 4H candle window to inspect
COMPRESSION_MIN_CANDLES  = 3    # minimum consecutive "compressing" candles to qualify
COMPRESSION_RATIO        = 1.15 # candle counts as compressing if range ≤ previous * 1.15
                                 # (i.e. not expanding by more than 15% — relaxed for real markets)
VOLUME_RECENT_CANDLES    = 3    # candles in the recent (compression) window
VOLUME_BASELINE_CANDLES  = 5    # candles immediately before the recent window (baseline)
VOLUME_EXHAUSTION_RATIO  = 0.70 # exhaustion if recent_avg ≤ 70% of baseline_avg

# Error handling / validation thresholds
RETRY_MAX            = 3
RETRY_DELAY_SECONDS  = 5
STALE_MINUTES        = 10
ANOMALY_DEV_PCT      = 50.0
DEGRADED_FAIL_RATIO  = 0.30


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def fetch_json(url: str) -> dict | list:
    req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def fetch_json_with_retry(url: str) -> dict | list:
    """Calls fetch_json up to RETRY_MAX times with RETRY_DELAY_SECONDS between attempts."""
    last_exc: Exception | None = None
    for attempt in range(1, RETRY_MAX + 1):
        try:
            return fetch_json(url)
        except Exception as e:
            last_exc = e
            if attempt < RETRY_MAX:
                print(f"    [Retry {attempt}/{RETRY_MAX}] {e} — retrying in {RETRY_DELAY_SECONDS}s...")
                time.sleep(RETRY_DELAY_SECONDS)
    raise last_exc  # type: ignore[misc]


def get_ticker_4h(symbol: str) -> dict:
    """Returns the latest 4H candle data for staleness and price validation."""
    data = fetch_json_with_retry(f"{BINANCE_BASE}/ticker/24hr?symbol={symbol}")
    return {
        "price":         float(data["lastPrice"]),
        "change_pct":    float(data["priceChangePercent"]),
        "volume":        float(data["quoteVolume"]),
        "close_time_ms": int(data["closeTime"]),
    }


def get_4h_klines(symbol: str, limit: int = 20) -> list[dict]:
    """Returns `limit` 4H candles (most recent last)."""
    raw = fetch_json_with_retry(
        f"{BINANCE_BASE}/klines?symbol={symbol}&interval=4h&limit={limit}"
    )
    candles = []
    for k in raw:
        candles.append({
            "open":       float(k[1]),
            "high":       float(k[2]),
            "low":        float(k[3]),
            "close":      float(k[4]),
            "volume":     float(k[5]),
            "close_time": int(k[6]),
        })
    return candles


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def is_stale(close_time_ms: int, now: datetime) -> bool:
    close_dt = datetime.fromtimestamp(close_time_ms / 1000, tz=timezone.utc)
    return (now - close_dt).total_seconds() / 60 > STALE_MINUTES


def is_anomalous_price(price: float, avg: float) -> tuple[bool, str]:
    if price <= 0:
        return True, f"price={price} is zero or negative"
    dev = abs((price - avg) / avg) * 100
    if dev > ANOMALY_DEV_PCT:
        return True, f"price deviates {dev:+.2f}% from recent average"
    return False, ""


# ---------------------------------------------------------------------------
# Aguiar Protocol Module 05 — Lateralization & Compression
# ---------------------------------------------------------------------------

def detect_lateralization(symbol: str, candles: list[dict]) -> dict:
    """
    Aguiar Protocol Module 05 — Lateralization detector.

    Inspects the last COMPRESSION_CANDLES 4H candles. A candle is considered
    "compressing" if its range (high - low) is within 15% of the previous
    candle's range — i.e. range[i] <= range[i-1] * COMPRESSION_RATIO (1.15).
    This relaxed definition handles real markets where candles don't shrink
    perfectly each step but hover in a tightening band.

    The streak is measured ending at the most recent candle (walking backwards).
    Detection requires COMPRESSION_MIN_CANDLES (3) consecutive qualifying candles,
    which means COMPRESSION_MIN_CANDLES-1 (2) qualifying pairs.

    Args:
        symbol:  Trading pair, e.g. "BTCUSDT".
        candles: List of 4H candle dicts from get_4h_klines().

    Returns:
        dict with keys:
            detected (bool)        — True if compression pattern qualifies.
            consecutive_count (int)— Number of consecutive compressing candles found.
            range_series (list)    — Candle ranges for the window (oldest first).
            compression_pct (float)— Tightest range as % of the widest in the series.
            note (str)             — Human-readable summary.
    """
    window = candles[-COMPRESSION_CANDLES:]
    if len(window) < 2:
        return {
            "detected": False, "consecutive_count": 0,
            "range_series": [], "compression_pct": 0.0,
            "note": "Insufficient candle data",
        }

    ranges = [c["high"] - c["low"] for c in window]

    # Walk backwards from the newest candle, counting how many consecutive
    # pairs satisfy: range[i] <= range[i-1] * COMPRESSION_RATIO.
    # A ratio of 1.15 means the candle can be up to 15% wider than the prior —
    # any expansion larger than that breaks the streak.
    consecutive_count = 0
    for i in range(len(ranges) - 1, 0, -1):
        if ranges[i] <= ranges[i - 1] * COMPRESSION_RATIO:
            consecutive_count += 1
        else:
            break

    # N consecutive candles require N-1 qualifying pairs.
    detected = consecutive_count >= (COMPRESSION_MIN_CANDLES - 1)
    max_r = max(ranges)
    compression_pct = (min(ranges) / max_r * 100) if max_r > 0 else 0.0

    if detected:
        note = (
            f"Compression confirmed: {consecutive_count} consecutive compressing pairs "
            f"(need {COMPRESSION_MIN_CANDLES - 1}), tightest range is "
            f"{compression_pct:.1f}% of widest in window"
        )
    else:
        note = (
            f"No qualifying compression: {consecutive_count} consecutive compressing pairs "
            f"(need {COMPRESSION_MIN_CANDLES - 1})"
        )

    return {
        "detected":          detected,
        "consecutive_count": consecutive_count,
        "range_series":      [round(r, 6) for r in ranges],
        "compression_pct":   round(compression_pct, 2),
        "note":              note,
    }


def detect_volume_exhaustion(symbol: str, candles: list[dict]) -> dict:
    """
    Detects declining volume coinciding with the compression pattern.

    Compares the average volume of the last VOLUME_RECENT_CANDLES (3) candles
    to the average volume of the VOLUME_BASELINE_CANDLES (5) candles immediately
    before them. If recent_avg <= baseline_avg * VOLUME_EXHAUSTION_RATIO (0.70),
    exhaustion is confirmed — volume dried up by at least 30%.

    Uses a focused 3-vs-5 window rather than comparing against the entire
    lookback, so the baseline captures the same compression episode rather
    than long-run averages that dilute the signal.

    Args:
        symbol:  Trading pair.
        candles: List of 4H candle dicts from get_4h_klines(). Must contain at
                 least VOLUME_RECENT_CANDLES + VOLUME_BASELINE_CANDLES entries.

    Returns:
        dict with keys:
            detected (bool)            — True if volume is exhausting.
            recent_avg_volume (float)  — Average volume over last 3 candles.
            baseline_avg_volume (float)— Average volume over the prior 5 candles.
            exhaustion_ratio (float)   — recent / baseline (lower = more exhausted).
            note (str)                 — Human-readable summary.
    """
    needed = VOLUME_RECENT_CANDLES + VOLUME_BASELINE_CANDLES
    if len(candles) < needed:
        return {
            "detected": False, "recent_avg_volume": 0.0,
            "baseline_avg_volume": 0.0, "exhaustion_ratio": 1.0,
            "note": f"Insufficient candle data (need {needed}, got {len(candles)})",
        }

    # Slice from the tail: last 3 are "recent", the 5 before them are "baseline".
    recent_candles   = candles[-VOLUME_RECENT_CANDLES:]
    baseline_candles = candles[-(VOLUME_RECENT_CANDLES + VOLUME_BASELINE_CANDLES):-VOLUME_RECENT_CANDLES]

    recent_avg   = sum(c["volume"] for c in recent_candles)   / len(recent_candles)
    baseline_avg = sum(c["volume"] for c in baseline_candles) / len(baseline_candles)

    exhaustion_ratio = recent_avg / baseline_avg if baseline_avg > 0 else 1.0
    detected = exhaustion_ratio <= VOLUME_EXHAUSTION_RATIO

    if detected:
        note = (
            f"Volume exhaustion confirmed: last-3 avg {recent_avg:,.0f} is "
            f"{exhaustion_ratio:.2f}x prior-5 avg {baseline_avg:,.0f} "
            f"(threshold ≤{VOLUME_EXHAUSTION_RATIO})"
        )
    else:
        note = (
            f"No volume exhaustion: last-3 avg {recent_avg:,.0f} is "
            f"{exhaustion_ratio:.2f}x prior-5 avg {baseline_avg:,.0f} "
            f"(need ≤{VOLUME_EXHAUSTION_RATIO})"
        )

    return {
        "detected":            detected,
        "recent_avg_volume":   round(recent_avg, 2),
        "baseline_avg_volume": round(baseline_avg, 2),
        "exhaustion_ratio":    round(exhaustion_ratio, 4),
        "note":                note,
    }


def generate_gem_alert(symbol: str, lat: dict, vol: dict, price: float) -> dict:
    """
    Combines lateralization and volume exhaustion results into a final GEM_ALERT
    decision for the asset.

    A GEM_ALERT is raised only when both detect_lateralization and
    detect_volume_exhaustion return detected=True. If only one condition is met
    the state is WATCHLIST. Otherwise NO_TRADE.

    Args:
        symbol: Trading pair.
        lat:    Return dict from detect_lateralization().
        vol:    Return dict from detect_volume_exhaustion().
        price:  Current price.

    Returns:
        dict with keys:
            symbol (str)
            state (str)   — "GEM_ALERT" | "WATCHLIST" | "NO_TRADE"
            signal (str)  — One-line summary of the signal.
            reason (str)  — Full rationale.
            price (float)

    TODO: evaluate lat["detected"] and vol["detected"] to set state
    TODO: build signal and reason strings from lat/vol data
    """
    if lat["detected"] and vol["detected"]:
        state = "GEM_ALERT"
        signal = (
            f"COIL: {lat['consecutive_count']} shrinking candles "
            f"({lat['compression_pct']:.1f}% compression) + volume at "
            f"{vol['exhaustion_ratio']:.2f}x baseline — breakout candidate"
        )
    elif lat["detected"]:
        state = "WATCHLIST"
        signal = (
            f"Compression only: {lat['consecutive_count']} shrinking candles "
            f"({lat['compression_pct']:.1f}%), volume not yet exhausted "
            f"(ratio={vol['exhaustion_ratio']:.2f})"
        )
    elif vol["detected"]:
        state = "WATCHLIST"
        signal = (
            f"Volume exhaustion only: ratio={vol['exhaustion_ratio']:.2f}, "
            f"no range compression detected"
        )
    else:
        state = "NO_TRADE"
        signal = (
            f"No compression or volume exhaustion "
            f"(compression_pairs={lat['consecutive_count']}, "
            f"vol_ratio={vol['exhaustion_ratio']:.2f})"
        )

    reason = f"Lateralization: {lat['note']} | Volume: {vol['note']}"

    return {
        "symbol": symbol,
        "state":  state,
        "signal": signal,
        "reason": reason,
        "price":  price,
    }


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def format_asian_block(a: dict, ts: str) -> str:
    return f"""\
AGENT: Scout (Asian Session)
SYMBOL: {a['symbol']}
TIMEFRAME: 4H
DATE: {ts}
PRICE: {a['price']:,.4f}
STATE: {a['state']}
SIGNAL: {a['signal']}
REASON: {a['reason']}"""


def format_system_health_block(
    total_requested: int,
    assessments: list[dict],
    failed: list[str],
    stale: list[str],
    anomalous: list[str],
    pipeline_status: str,
) -> list[str]:
    total_fetched  = len(assessments)
    total_excluded = len(failed) + len(stale) + len(anomalous)

    lines = [
        "## System Health",
        "",
        "```",
        f"TOTAL_ASSETS_REQUESTED:  {total_requested}",
        f"TOTAL_ASSETS_FETCHED:    {total_fetched}",
        f"TOTAL_ASSETS_EXCLUDED:   {total_excluded}",
        f"FAILED_ASSETS:           {', '.join(failed)   or 'none'}",
        f"STALE_ASSETS:            {', '.join(stale)    or 'none'}",
        f"ANOMALOUS_ASSETS:        {', '.join(anomalous) or 'none'}",
        f"PIPELINE_STATUS:         {pipeline_status}",
        "```",
    ]

    if pipeline_status == "DEGRADED":
        lines += [
            "",
            f"> **WARNING:** Pipeline is DEGRADED — {total_excluded}/{total_requested} assets "
            f"excluded ({total_excluded / total_requested * 100:.0f}%). "
            f"Results are incomplete. Manual review required.",
        ]
    return lines


def build_report(
    assessments: list[dict],
    run_dt: datetime,
    btc_filter_active: bool,
    failed: list[str],
    stale: list[str],
    anomalous: list[str],
    pipeline_status: str,
) -> str:
    date_str = run_dt.strftime("%Y-%m-%d")
    time_str = run_dt.strftime("%H:%M UTC")
    ts       = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    btc_a      = next((a for a in assessments if a["symbol"] == "BTCUSDT"), None)
    btc_state  = btc_a["state"] if btc_a else "UNKNOWN"
    filter_txt = (
        f"ACTIVE — BTC 4H state is {btc_state}; altcoin GEM_ALERTs downgraded to WATCHLIST"
        if btc_filter_active
        else f"INACTIVE — BTC 4H state is {btc_state}; signals unmodified"
    )

    lines = [
        "---",
        "schema_type: asian_scan_report",
        "schema_version: 1.0",
        "---",
        "# Euru OS — Asian Session Scan Report",
        f"**Date:** {date_str}  ",
        f"**Time:** {time_str}  ",
        f"**Session:** Asian (00:00 UTC open)  ",
        f"**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  ",
        f"**Assets scanned:** {len(assessments)}  ",
        f"**Mode:** READ_ONLY  ",
        f"**BTC Master Filter (Module 01):** {filter_txt}  ",
        "",
        "---",
        "",
    ]

    lines += format_system_health_block(
        len(SYMBOLS), assessments, failed, stale, anomalous, pipeline_status
    )
    lines += ["", "---", "", "## Asset Summary", "",
              "| Symbol | Price (USDT) | State |",
              "|--------|-------------|-------|"]

    for a in assessments:
        lines.append(
            f"| {a['symbol']} | {a['price']:>12,.4f} | **{a['state']}** |"
        )

    lines += ["", "---", "", "## Asian Session Assessments", ""]

    for a in assessments:
        lines.append(f"### {a['symbol']}")
        lines.append("")
        lines.append("```")
        lines.append(format_asian_block(a, ts))
        lines.append("```")
        lines.append("")

    lines += [
        "---",
        "",
        "*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    run_dt   = datetime.now(timezone.utc)
    date_str = run_dt.strftime("%Y-%m-%d")

    print(f"Euru OS — Asian Session Scan [{date_str}  00:00 UTC]")
    print(f"Protocol: Aguiar Module 05 — Lateralization & Compression\n")

    assessments: list[dict] = []
    failed:      list[str]  = []
    stale:       list[str]  = []
    anomalous:   list[str]  = []

    for symbol in SYMBOLS:
        try:
            ticker  = get_ticker_4h(symbol)
            candles = get_4h_klines(symbol, limit=20)

            # Staleness check
            if is_stale(ticker["close_time_ms"], run_dt):
                print(f"  {symbol}: STALE — last update older than {STALE_MINUTES} min, excluding")
                stale.append(symbol)
                continue

            # Impossible value check
            avg_close = sum(c["close"] for c in candles[-7:]) / 7
            anomaly, reason = is_anomalous_price(ticker["price"], avg_close)
            if anomaly:
                print(f"  {symbol}: ANOMALY — {reason}, excluding")
                anomalous.append(symbol)
                continue

            lat   = detect_lateralization(symbol, candles)
            vol   = detect_volume_exhaustion(symbol, candles)
            alert = generate_gem_alert(symbol, lat, vol, ticker["price"])
            assessments.append(alert)

            print(
                f"  {symbol:10s}  price={ticker['price']:>12,.4f}  "
                f"compression={lat['consecutive_count']}c  "
                f"vol_ratio={vol['exhaustion_ratio']:.2f}  "
                f"=> {alert['state']}"
            )
        except urllib.error.URLError as e:
            print(f"  {symbol}: network error after {RETRY_MAX} attempts — {e}")
            failed.append(symbol)
        except Exception as e:
            print(f"  {symbol}: unexpected error — {e}")
            failed.append(symbol)

    if not assessments:
        print("\nNo data retrieved. Aborting report.")
        return

    # Pipeline status
    total_excluded = len(failed) + len(stale) + len(anomalous)
    pipeline_status = (
        "DEGRADED"
        if total_excluded / len(SYMBOLS) > DEGRADED_FAIL_RATIO
        else "HEALTHY"
    )

    print(f"\nPipeline status: {pipeline_status}")
    if stale:
        print(f"  Stale:     {', '.join(stale)}")
    if anomalous:
        print(f"  Anomalous: {', '.join(anomalous)}")
    if failed:
        print(f"  Failed:    {', '.join(failed)}")

    # BTC master filter — downgrade altcoin GEM_ALERTs if BTC is weak
    btc = next((a for a in assessments if a["symbol"] == "BTCUSDT"), None)
    btc_filter_active = btc is not None and btc["state"] in ("NO_TRADE", "WATCHLIST")
    if btc_filter_active:
        print(f"\n  [BTC Master Filter] BTC 4H state={btc['state']} — downgrading altcoin GEM_ALERT -> WATCHLIST")
        for a in assessments:
            if a["symbol"] != "BTCUSDT" and a["state"] == "GEM_ALERT":
                a["state"]  = "WATCHLIST"
                a["signal"] = f"[BTC filter] Downgraded from GEM_ALERT — BTC state is {btc['state']}. " + a["signal"]

    report = build_report(assessments, run_dt, btc_filter_active, failed, stale, anomalous, pipeline_status)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"ASIAN_REPORT_{date_str}.md")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\nReport saved => {output_path}")
    except (PermissionError, OSError) as e:
        # File is likely open in another application. Write to a timestamped
        # fallback so the run is never lost.
        ts_suffix  = run_dt.strftime("%H%M%S")
        fallback   = os.path.join(OUTPUT_DIR, f"ASIAN_REPORT_{date_str}_{ts_suffix}.md")
        with open(fallback, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n  WARNING: Could not write to {output_path} ({e})")
        print(f"  Report saved to fallback => {fallback}")


if __name__ == "__main__":
    main()
    try:
        from euru_git_sync import git_sync
        git_sync("asian session report")
    except Exception as _e:
        print(f"[git-sync] Skipped: {_e}")
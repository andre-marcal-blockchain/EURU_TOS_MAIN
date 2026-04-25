"""
Euru OS — Flow Analyst
Calculates RSI (14), MACD (12/26/9), OBV trend, and ATR (14) for any given
symbol using Binance daily klines data.

This script implements the Flow Analyst agent defined in 04_AGENTES/02_FLOW_ANALYST/.
It determines whether price momentum, volume flow, and volatility CONFIRM or
CONTRADICT a structural bias produced by the Scout agent.

All outputs use the official Euru OS status vocabulary from
01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS.md:
    ACCELERATION:  BULLISH | BEARISH | NEUTRAL
    CONFIRMATION:  CONFIRMS | CONTRADICTS | INCONCLUSIVE
    VOLUME_FLOW:   STRONG | WEAK | DIVERGENCE

Usage:
    python euru_flow_analyst.py                 # runs on all SYMBOLS
    python euru_flow_analyst.py BTCUSDT ETHUSDT # runs on specific symbols

Output: 08_DADOS_E_JOURNAL/SCORECARDS/FLOW_REPORT_<YYYY-MM-DD>.md
"""

import json
import math
import os
import sys
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
    "LINKUSDT", "ADAUSDT", "XRPUSDT", "MATICUSDT",
    "SUIUSDT", "NEARUSDT", "INJUSDT", "ARBUSDT",
    "OPUSDT", "FETUSDT", "TAOUSDT", "RENDERUSDT",
]
BINANCE_BASE = "https://api.binance.com/api/v3"
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "SCORECARDS")

# Indicator parameters
RSI_PERIOD    = 14
MACD_FAST     = 12
MACD_SLOW     = 26
MACD_SIGNAL   = 9
ATR_PERIOD    = 14
ATR_STOP_MULT = 1.5   # suggested stop = price - ATR * ATR_STOP_MULT (long bias)
KLINES_LIMIT  = 100   # candles to fetch — enough to warm up all indicators

# Thresholds for interpreting indicator values
RSI_OVERBOUGHT  = 70
RSI_OVERSOLD    = 30
RSI_BULLISH_MIN = 50  # RSI above this → bullish momentum

# Error handling
RETRY_MAX           = 3
RETRY_DELAY_SECONDS = 5
STALE_MINUTES       = 10
DEGRADED_FAIL_RATIO = 0.30


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def fetch_json(url: str) -> dict | list:
    req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def fetch_json_with_retry(url: str) -> dict | list:
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


def get_daily_klines(symbol: str, limit: int = KLINES_LIMIT) -> list[dict]:
    """Returns `limit` daily candles (most recent last)."""
    raw = fetch_json_with_retry(
        f"{BINANCE_BASE}/klines?symbol={symbol}&interval=1d&limit={limit}"
    )
    candles = []
    for k in raw:
        candles.append({
            "open":         float(k[1]),
            "high":         float(k[2]),
            "low":          float(k[3]),
            "close":        float(k[4]),
            "volume":       float(k[5]),
            "close_time":   int(k[6]),
        })
    return candles


def is_stale(close_time_ms: int, now: datetime) -> bool:
    close_dt = datetime.fromtimestamp(close_time_ms / 1000, tz=timezone.utc)
    return (now - close_dt).total_seconds() / 60 > STALE_MINUTES


# ---------------------------------------------------------------------------
# Indicator calculations
# ---------------------------------------------------------------------------

def _ema(values: list[float], period: int) -> list[float]:
    """
    Exponential Moving Average helper used internally by MACD and RSI.

    Args:
        values: List of floats (oldest first).
        period: EMA period.

    Returns:
        List of EMA values, same length as input. Values before index (period - 1)
        are seeded with the simple average of the first `period` values.

    TODO: implement Wilder / standard EMA
          k = 2 / (period + 1) for standard EMA
          k = 1 / period       for Wilder smoothing (used by RSI/ATR)
    """
    if len(values) < period:
        return [float("nan")] * len(values)

    ema_values: list[float] = [float("nan")] * len(values)
    # Seed with SMA of first `period` values
    seed = sum(values[:period]) / period
    ema_values[period - 1] = seed
    k = 2.0 / (period + 1)

    # TODO: replace loop body with: ema = value * k + prev_ema * (1 - k)
    for i in range(period, len(values)):
        ema_values[i] = values[i] * k + ema_values[i - 1] * (1 - k)

    return ema_values


def calculate_rsi(closes: list[float]) -> float:
    """
    Calculates Relative Strength Index using Wilder's smoothing (standard).

    Args:
        closes: List of closing prices (oldest first), minimum RSI_PERIOD + 1 values.

    Returns:
        RSI value (0.0–100.0) for the most recent candle, or float("nan") if
        insufficient data.

    Interpretation used downstream:
        RSI > RSI_OVERBOUGHT  → momentum overextended to upside
        RSI < RSI_OVERSOLD    → momentum overextended to downside
        RSI > RSI_BULLISH_MIN → bullish momentum bias
        RSI < RSI_BULLISH_MIN → bearish momentum bias

    TODO: compute gains and losses from consecutive close differences
    TODO: seed avg_gain / avg_loss with SMA of first RSI_PERIOD values
    TODO: apply Wilder smoothing: avg = (prev_avg * (RSI_PERIOD - 1) + current) / RSI_PERIOD
    TODO: RS = avg_gain / avg_loss; RSI = 100 - (100 / (1 + RS))
    """
    if len(closes) < RSI_PERIOD + 1:
        return float("nan")

    gains  = [max(closes[i] - closes[i - 1], 0.0) for i in range(1, len(closes))]
    losses = [max(closes[i - 1] - closes[i], 0.0) for i in range(1, len(closes))]

    avg_gain = sum(gains[:RSI_PERIOD])  / RSI_PERIOD
    avg_loss = sum(losses[:RSI_PERIOD]) / RSI_PERIOD

    for i in range(RSI_PERIOD, len(gains)):
        avg_gain = (avg_gain * (RSI_PERIOD - 1) + gains[i])  / RSI_PERIOD
        avg_loss = (avg_loss * (RSI_PERIOD - 1) + losses[i]) / RSI_PERIOD

    rs = avg_gain / avg_loss if avg_loss != 0 else float("inf")
    return 100.0 - (100.0 / (1.0 + rs))


def calculate_macd(closes: list[float]) -> dict:
    """
    Calculates MACD line, signal line, and histogram using standard EMA.

    Parameters: fast=MACD_FAST, slow=MACD_SLOW, signal=MACD_SIGNAL.

    Args:
        closes: List of closing prices (oldest first), minimum MACD_SLOW + MACD_SIGNAL values.

    Returns:
        dict with keys:
            macd_line   (float) — EMA(fast) − EMA(slow) for the latest bar
            signal_line (float) — EMA(macd_line, MACD_SIGNAL) for the latest bar
            histogram   (float) — macd_line − signal_line (positive = bullish)
            trend       (str)   — "BULLISH" | "BEARISH" | "NEUTRAL"

    Interpretation used downstream:
        histogram > 0 and rising → accelerating bullish momentum
        histogram < 0 and falling → accelerating bearish momentum
        histogram crossing zero → potential reversal

    TODO: compute fast_ema and slow_ema with _ema()
    TODO: compute macd_line = fast_ema[i] - slow_ema[i] for all valid i
    TODO: compute signal_line = _ema(macd_line_series, MACD_SIGNAL)
    TODO: histogram = macd_line[-1] - signal_line[-1]
    TODO: set trend from histogram sign and whether it is expanding
    """
    required = MACD_SLOW + MACD_SIGNAL
    if len(closes) < required:
        return {"macd_line": float("nan"), "signal_line": float("nan"),
                "histogram": float("nan"), "trend": "NEUTRAL"}

    fast_ema  = _ema(closes, MACD_FAST)
    slow_ema  = _ema(closes, MACD_SLOW)

    macd_series = [
        f - s
        for f, s in zip(fast_ema, slow_ema)
        if not math.isnan(f) and not math.isnan(s)
    ]

    if len(macd_series) < MACD_SIGNAL:
        return {"macd_line": float("nan"), "signal_line": float("nan"),
                "histogram": float("nan"), "trend": "NEUTRAL"}

    signal_series = _ema(macd_series, MACD_SIGNAL)

    macd_val   = macd_series[-1]
    signal_val = signal_series[-1]

    if math.isnan(signal_val):
        return {"macd_line": macd_val, "signal_line": float("nan"),
                "histogram": float("nan"), "trend": "NEUTRAL"}

    histogram = macd_val - signal_val
    trend = "BULLISH" if histogram > 0 else "BEARISH" if histogram < 0 else "NEUTRAL"

    return {
        "macd_line":   macd_val,
        "signal_line": signal_val,
        "histogram":   histogram,
        "trend":       trend,
    }


def calculate_obv(closes: list[float], volumes: list[float]) -> dict:
    """
    Calculates On-Balance Volume and determines its short-term trend.

    OBV accumulates volume positively on up-days and negatively on down-days.
    The trend is determined by comparing the slope of the last N OBV values.

    Args:
        closes:  List of closing prices (oldest first).
        volumes: List of volumes matching the closes list.

    Returns:
        dict with keys:
            obv_series      (list[float]) — Full OBV series.
            current_obv     (float)       — Most recent OBV value.
            trend           (str)         — "RISING" | "FALLING" | "FLAT"
            volume_flow     (str)         — "STRONG" | "WEAK" | "DIVERGENCE"
                                           DIVERGENCE when price and OBV disagree.

    Interpretation used downstream:
        OBV rising + price rising    → STRONG (volume confirms move)
        OBV falling + price falling  → STRONG (volume confirms move)
        OBV rising + price falling   → DIVERGENCE (accumulation signal)
        OBV falling + price rising   → DIVERGENCE (distribution signal)
        OBV flat                     → WEAK

    TODO: compute OBV series: obv[i] = obv[i-1] + vol[i] if close[i] > close[i-1] else obv[i-1] - vol[i]
    TODO: derive OBV trend from linear regression or simple slope over last 5 values
    TODO: determine divergence by comparing OBV trend direction vs price trend direction
    """
    if len(closes) < 2 or len(closes) != len(volumes):
        return {"obv_series": [], "current_obv": 0.0, "trend": "FLAT", "volume_flow": "WEAK"}

    obv = [0.0]
    for i in range(1, len(closes)):
        if closes[i] > closes[i - 1]:
            obv.append(obv[-1] + volumes[i])
        elif closes[i] < closes[i - 1]:
            obv.append(obv[-1] - volumes[i])
        else:
            obv.append(obv[-1])

    # Linear-regression slope over last 5 OBV values (normalised by magnitude)
    window = obv[-5:]
    n      = len(window)
    x_mean = (n - 1) / 2.0
    y_mean = sum(window) / n
    numer  = sum((i - x_mean) * (window[i] - y_mean) for i in range(n))
    denom  = sum((i - x_mean) ** 2                   for i in range(n))
    slope  = numer / denom if denom != 0 else 0.0

    scale     = abs(y_mean) if abs(y_mean) > 0 else 1.0
    rel_slope = slope / scale
    SLOPE_THRESH = 0.01  # 1 % per period

    if rel_slope > SLOPE_THRESH:
        obv_trend = "RISING"
    elif rel_slope < -SLOPE_THRESH:
        obv_trend = "FALLING"
    else:
        obv_trend = "FLAT"

    # Divergence: OBV direction vs price direction over the same 5-bar window
    price_up   = closes[-1] > closes[-5]
    price_down = closes[-1] < closes[-5]

    if obv_trend == "FLAT":
        volume_flow = "WEAK"
    elif (obv_trend == "RISING"  and price_up) or \
         (obv_trend == "FALLING" and price_down):
        volume_flow = "STRONG"
    else:
        volume_flow = "DIVERGENCE"

    return {
        "obv_series":  obv,
        "current_obv": obv[-1],
        "trend":       obv_trend,
        "volume_flow": volume_flow,
    }


def calculate_atr(highs: list[float], lows: list[float], closes: list[float]) -> float:
    """
    Calculates Average True Range using Wilder's smoothing over ATR_PERIOD.

    True Range (TR) = max of:
        high[i] - low[i]
        abs(high[i] - close[i-1])
        abs(low[i]  - close[i-1])

    Args:
        highs:  List of high prices (oldest first).
        lows:   List of low prices (oldest first).
        closes: List of closing prices (oldest first).

    Returns:
        ATR value (float) for the most recent bar, or float("nan") if insufficient data.
        The ATR is expressed in the same unit as the price (e.g. USDT).

    Usage downstream:
        SUGGESTED_STOP (long) = current_price - ATR * ATR_STOP_MULT
        SUGGESTED_STOP (short)= current_price + ATR * ATR_STOP_MULT

    TODO: compute TR for each bar starting at index 1 (needs previous close)
    TODO: seed ATR with SMA of first ATR_PERIOD TR values
    TODO: apply Wilder smoothing: atr = (prev_atr * (ATR_PERIOD - 1) + tr) / ATR_PERIOD
    """
    if len(closes) < ATR_PERIOD + 1:
        return float("nan")

    tr_values = []
    for i in range(1, len(closes)):
        tr = max(
            highs[i]  - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i]  - closes[i - 1]),
        )
        tr_values.append(tr)

    atr = sum(tr_values[:ATR_PERIOD]) / ATR_PERIOD
    for tr in tr_values[ATR_PERIOD:]:
        atr = (atr * (ATR_PERIOD - 1) + tr) / ATR_PERIOD

    return atr


# ---------------------------------------------------------------------------
# Flow assessment logic
# ---------------------------------------------------------------------------

def assess_flow(symbol: str, candles: list[dict]) -> dict:
    """
    Combines RSI, MACD, OBV and ATR into a single Flow Analyst output block.

    Derives ACCELERATION, CONFIRMATION, and VOLUME_FLOW using indicator consensus:
        ACCELERATION = BULLISH  if RSI > RSI_BULLISH_MIN and MACD trend = BULLISH
        ACCELERATION = BEARISH  if RSI < RSI_BULLISH_MIN and MACD trend = BEARISH
        ACCELERATION = NEUTRAL  otherwise

        CONFIRMATION = CONFIRMS      if ACCELERATION matches OBV volume_flow direction
        CONFIRMATION = CONTRADICTS   if they disagree
        CONFIRMATION = INCONCLUSIVE  if any indicator is NaN / placeholder

        VOLUME_FLOW  = directly from calculate_obv() return value

    SUGGESTED_STOP uses the long-bias formula: price - ATR * ATR_STOP_MULT.
    """
    closes  = [c["close"]  for c in candles]
    highs   = [c["high"]   for c in candles]
    lows    = [c["low"]    for c in candles]
    volumes = [c["volume"] for c in candles]

    price = closes[-1]

    rsi  = calculate_rsi(closes)
    macd = calculate_macd(closes)
    obv  = calculate_obv(closes, volumes)
    atr  = calculate_atr(highs, lows, closes)

    # Derive ACCELERATION from RSI + MACD consensus
    rsi_valid = not math.isnan(rsi)
    if rsi_valid and rsi > RSI_BULLISH_MIN and macd["trend"] == "BULLISH":
        acceleration = "BULLISH"
    elif rsi_valid and rsi < RSI_BULLISH_MIN and macd["trend"] == "BEARISH":
        acceleration = "BEARISH"
    else:
        acceleration = "NEUTRAL"

    # Derive CONFIRMATION from indicator agreement
    # TODO: once OBV and MACD are implemented, this logic will be meaningful
    if not rsi_valid or math.isnan(macd["histogram"]):
        confirmation = "INCONCLUSIVE"
    elif (acceleration == "BULLISH" and obv["volume_flow"] in ("STRONG", "DIVERGENCE")) or \
         (acceleration == "BEARISH" and obv["volume_flow"] in ("STRONG", "DIVERGENCE")):
        confirmation = "CONFIRMS"
    elif acceleration == "NEUTRAL":
        confirmation = "INCONCLUSIVE"
    else:
        confirmation = "CONTRADICTS"

    # Suggested stop (long bias default)
    if not math.isnan(atr):
        stop_dist      = atr * ATR_STOP_MULT
        suggested_stop = price - stop_dist
        atr_display    = f"{atr:.4f}"
        stop_dist_disp = f"{stop_dist:,.4f}"
        stop_display   = f"{suggested_stop:,.4f}"
    else:
        stop_dist      = float("nan")
        atr_display    = "N/A"
        stop_dist_disp = "N/A"
        stop_display   = "N/A"

    rsi_display = f"{rsi:.2f}" if not math.isnan(rsi) else "N/A"

    return {
        "symbol":         symbol,
        "price":          price,
        "rsi":            rsi_display,
        "rsi_raw":        rsi,
        "macd_trend":     macd["trend"],
        "macd_histogram": macd["histogram"],
        "obv_trend":      obv["trend"],
        "volume_flow":    obv["volume_flow"],
        "atr":            atr_display,
        "atr_raw":        atr,
        "stop_dist":      stop_dist_disp,
        "acceleration":   acceleration,
        "confirmation":   confirmation,
        "suggested_stop": stop_display,
    }


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def format_flow_block(a: dict, ts: str) -> str:
    hist = (
        f"{a['macd_histogram']:.6f}"
        if not isinstance(a["macd_histogram"], float) or not math.isnan(a["macd_histogram"])
        else "N/A (insufficient data)"
    )
    return f"""\
AGENT: Flow Analyst
SYMBOL: {a['symbol']}
TIMEFRAME: 1D
DATE: {ts}
RSI_14: {a['rsi']}
MACD_TREND: {a['macd_trend']}
MACD_HISTOGRAM: {hist}
OBV_TREND: {a['obv_trend']}
VOLUME_FLOW: {a['volume_flow']}
ATR_14: {a['atr']}
ACCELERATION: {a['acceleration']}
CONFIRMATION: {a['confirmation']}
ATR_VALUE: {a['atr']}
SUGGESTED_STOP: {a['suggested_stop']}"""


def format_system_health_block(
    total_requested: int,
    assessments: list[dict],
    failed: list[str],
    stale: list[str],
    pipeline_status: str,
) -> list[str]:
    total_excluded = len(failed) + len(stale)
    lines = [
        "## System Health",
        "",
        "```",
        f"TOTAL_ASSETS_REQUESTED:  {total_requested}",
        f"TOTAL_ASSETS_FETCHED:    {len(assessments)}",
        f"TOTAL_ASSETS_EXCLUDED:   {total_excluded}",
        f"FAILED_ASSETS:           {', '.join(failed) or 'none'}",
        f"STALE_ASSETS:            {', '.join(stale) or 'none'}",
        f"PIPELINE_STATUS:         {pipeline_status}",
        "```",
    ]
    if pipeline_status == "DEGRADED":
        lines += [
            "",
            f"> **WARNING:** Pipeline is DEGRADED — {total_excluded}/{total_requested} assets "
            f"excluded ({total_excluded / total_requested * 100:.0f}%). Manual review required.",
        ]
    return lines


def build_report(
    assessments: list[dict],
    run_dt: datetime,
    failed: list[str],
    stale: list[str],
    pipeline_status: str,
) -> str:
    date_str = run_dt.strftime("%Y-%m-%d")
    time_str = run_dt.strftime("%H:%M UTC")
    ts       = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Euru OS — Flow Analyst Report",
        f"**Date:** {date_str}  ",
        f"**Time:** {time_str}  ",
        f"**Assets analysed:** {len(assessments)}  ",
        f"**Mode:** READ_ONLY  ",
        "",
        "---",
        "",
    ]

    lines += format_system_health_block(
        len(SYMBOLS), assessments, failed, stale, pipeline_status
    )
    lines += ["", "---", "", "## Flow Summary", "",
              "| Symbol | Price | RSI | MACD | OBV | Acceleration | Confirmation |",
              "|--------|-------|-----|------|-----|-------------|-------------|"]

    for a in assessments:
        lines.append(
            f"| {a['symbol']} "
            f"| {a['price']:>12,.4f} "
            f"| {a['rsi']} "
            f"| {a['macd_trend']} "
            f"| {a['obv_trend']} "
            f"| **{a['acceleration']}** "
            f"| **{a['confirmation']}** |"
        )

    lines += ["", "---", "", "## Flow Analyst Assessments", ""]

    for a in assessments:
        lines.append(f"### {a['symbol']}")
        lines.append("")
        lines.append("```")
        lines.append(format_flow_block(a, ts))
        lines.append("```")
        lines.append("")

    lines += [
        "---",
        "",
        "*Generated by euru_flow_analyst.py — Euru OS READ_ONLY phase*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    run_dt   = datetime.now(timezone.utc)
    date_str = run_dt.strftime("%Y-%m-%d")

    # Allow overriding the symbol list from CLI: python euru_flow_analyst.py BTCUSDT ETHUSDT
    symbols = sys.argv[1:] if len(sys.argv) > 1 else SYMBOLS

    print(f"Euru OS — Flow Analyst [{date_str}]")
    print(f"Symbols: {', '.join(symbols)}\n")

    assessments: list[dict] = []
    failed:      list[str]  = []
    stale:       list[str]  = []

    for symbol in symbols:
        try:
            candles = get_daily_klines(symbol, limit=KLINES_LIMIT)

            if is_stale(candles[-1]["close_time"], run_dt):
                print(f"  {symbol}: STALE — last candle older than {STALE_MINUTES} min, excluding")
                stale.append(symbol)
                continue

            assessment = assess_flow(symbol, candles)
            assessments.append(assessment)
            print(
                f"  {symbol:10s}  price={assessment['price']:>12,.4f}  "
                f"RSI={assessment['rsi']}  "
                f"MACD={assessment['macd_trend']}  "
                f"OBV={assessment['obv_trend']}  "
                f"=> {assessment['acceleration']} / {assessment['confirmation']}"
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

    total_excluded = len(failed) + len(stale)
    pipeline_status = (
        "DEGRADED"
        if total_excluded / len(symbols) > DEGRADED_FAIL_RATIO
        else "HEALTHY"
    )

    print(f"\nPipeline status: {pipeline_status}")

    report = build_report(assessments, run_dt, failed, stale, pipeline_status)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"FLOW_REPORT_{date_str}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport saved => {output_path}")


if __name__ == "__main__":
    main()

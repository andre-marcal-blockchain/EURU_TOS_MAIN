"""
Euru OS — Morning Scan
Fetches BTCUSDT, ETHUSDT, and 18 altcoins from Binance public API and saves a Scout report.
BTC Module 01 master filter: if BTC trend is SIDEWAYS or BEARISH, all altcoin SETUP
signals are downgraded to WATCHLIST.
News Sentinel: fetches crypto headlines from CryptoPanic public API and assigns severity.
Output: 08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_<YYYY-MM-DD>.md
"""

import json
import math
import os
import re
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

from euru_flow_analyst import assess_flow as _run_flow_analyst
from euru_score_engine import compute_score as _run_score_engine

try:
    from euru_breakout_scanner import run_scan as _run_breakout_scan
    from euru_breakout_scanner import format_breakout_section as _fmt_breakout_section
    _BREAKOUT_AVAILABLE = True
except ImportError:
    _BREAKOUT_AVAILABLE = False

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
NEWS_RSS_SOURCES = [
    ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ("CoinDesk",      "https://www.coindesk.com/arc/outboundfeeds/rss/"),
]
# Browser UA needed — both feeds block generic bot agents
NEWS_RSS_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "SCORECARDS")

# News Sentinel keyword tiers (checked case-insensitively)
NEWS_HIGH_KEYWORDS    = {"war", "crash", "ban", "hack", "sec", "regulation", "liquidation", "collapse"}
NEWS_MEDIUM_KEYWORDS  = {"inflation", "rates", "geopolitical", "uncertainty", "tariff"}

# Scout state thresholds (price vs 7-day average)
SETUP_THRESHOLD = 3.0      # % deviation → SETUP
WATCHLIST_THRESHOLD = 1.0  # % deviation → WATCHLIST (below → NO_TRADE)

# Error handling / validation thresholds
RETRY_MAX = 3
RETRY_DELAY_SECONDS = 5
STALE_MINUTES = 10
ANOMALY_DEV_THRESHOLD_PCT = 50.0
DEGRADED_FAIL_THRESHOLD = 0.30   # fraction of assets that must fail to set pipeline DEGRADED


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


def get_ticker_24h(symbol: str) -> dict:
    """Returns 24h price stats for the symbol, including close_time_ms for staleness checks."""
    data = fetch_json_with_retry(f"{BINANCE_BASE}/ticker/24hr?symbol={symbol}")
    return {
        "price":         float(data["lastPrice"]),
        "change_pct":    float(data["priceChangePercent"]),
        "high_24h":      float(data["highPrice"]),
        "low_24h":       float(data["lowPrice"]),
        "volume":        float(data["quoteVolume"]),
        "close_time_ms": int(data["closeTime"]),
    }


def get_daily_klines(symbol: str, limit: int = 100) -> list[dict]:
    """Returns `limit` daily candles (most recent last)."""
    raw = fetch_json_with_retry(f"{BINANCE_BASE}/klines?symbol={symbol}&interval=1d&limit={limit}")
    candles = []
    for k in raw:
        candles.append({
            "open":       float(k[1]),
            "high":       float(k[2]),
            "low":        float(k[3]),
            "close":      float(k[4]),
            "volume":     float(k[7]),  # quote volume (USDT) — consistent with ticker quoteVolume
            "close_time": int(k[6]),
        })
    return candles


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def is_stale(close_time_ms: int, now: datetime) -> bool:
    """Returns True if the ticker's close time is older than STALE_MINUTES."""
    close_dt = datetime.fromtimestamp(close_time_ms / 1000, tz=timezone.utc)
    age_minutes = (now - close_dt).total_seconds() / 60
    return age_minutes > STALE_MINUTES


def is_anomalous_price(price: float, avg_7d: float) -> tuple[bool, str]:
    """
    Returns (True, reason) if the price is zero/negative or deviates more than
    ANOMALY_DEV_THRESHOLD_PCT from the 7-day average.
    """
    if price <= 0:
        return True, f"price={price} is zero or negative"
    dev_pct = ((price - avg_7d) / avg_7d) * 100
    if abs(dev_pct) > ANOMALY_DEV_THRESHOLD_PCT:
        return True, f"price deviation {dev_pct:+.2f}% exceeds {ANOMALY_DEV_THRESHOLD_PCT}% threshold vs 7D avg"
    return False, ""


# ---------------------------------------------------------------------------
# News Sentinel
# ---------------------------------------------------------------------------

def fetch_crypto_news() -> tuple[list[str], str]:
    """
    Fetches headlines from crypto RSS feeds (CoinTelegraph → CoinDesk fallback).
    Returns (titles, source_name). source_name is empty string if all sources failed.
    """
    for source_name, url in NEWS_RSS_SOURCES:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": NEWS_RSS_UA})
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
            items = re.findall(r"<item[\s>].*?</item>", raw, re.DOTALL)
            titles = []
            for item in items:
                m = re.search(r"<title[^>]*>(.*?)</title>", item, re.DOTALL)
                if m:
                    title = re.sub(r"<!\[CDATA\[|\]\]>", "", m.group(1)).strip()
                    if title:
                        titles.append(title)
            if titles:
                print(f"  [News Sentinel] Source: {source_name} ({len(titles)} headlines)")
                return titles, source_name
        except urllib.error.URLError as e:
            print(f"  [News Sentinel] {source_name} network error: {e}")
        except Exception as e:
            print(f"  [News Sentinel] {source_name} error: {e}")
    return [], ""


def classify_headline(title: str) -> str:
    """Returns HIGH, MEDIUM, or LOW severity for a single headline."""
    lower = title.lower()
    words = set(lower.replace(",", " ").replace(".", " ").split())
    if words & NEWS_HIGH_KEYWORDS:
        return "HIGH"
    if words & NEWS_MEDIUM_KEYWORDS:
        return "MEDIUM"
    return "LOW"


def run_news_sentinel() -> dict:
    """
    Fetches crypto news, scores each headline, and returns a summary dict with:
      - overall_severity: highest severity across all headlines (HIGH > MEDIUM > LOW)
      - top_headlines: list of up to 3 (title, severity) tuples
      - source: name of the news source that responded, or empty string
      - error: non-empty string if news could not be fetched
    """
    print("  Fetching crypto news headlines...")
    headlines, source = fetch_crypto_news()

    if not headlines:
        return {
            "overall_severity": "UNKNOWN",
            "top_headlines": [],
            "source": "",
            "error": "Could not retrieve headlines from any news source.",
        }

    ranked = []
    severity_order = {"HIGH": 2, "MEDIUM": 1, "LOW": 0}
    for title in headlines:
        sev = classify_headline(title)
        ranked.append((title, sev))

    # Sort: HIGH first, then MEDIUM, then LOW; preserve original order within tier
    ranked.sort(key=lambda x: severity_order[x[1]], reverse=True)

    top_3 = ranked[:3]
    overall = top_3[0][1] if top_3 else "LOW"

    return {
        "overall_severity": overall,
        "top_headlines": top_3,
        "source": source,
        "error": "",
    }


def format_news_sentinel_block(news: dict, ts: str) -> str:
    if news["error"]:
        return (
            f"AGENT: News Sentinel\n"
            f"DATE: {ts}\n"
            f"OVERALL_SEVERITY: {news['overall_severity']}\n"
            f"ERROR: {news['error']}"
        )

    lines = [
        f"AGENT: News Sentinel",
        f"DATE: {ts}",
        f"OVERALL_SEVERITY: {news['overall_severity']}",
        f"TOP_HEADLINES:",
    ]
    for i, (title, sev) in enumerate(news["top_headlines"], 1):
        lines.append(f"  {i}. [{sev}] {title}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Scout assessment logic
# ---------------------------------------------------------------------------

def seven_day_average(candles: list[dict]) -> float:
    """Average close of the 7 completed daily candles (excludes current/last candle)."""
    completed = candles[:-1]  # last candle is still open
    return sum(c["close"] for c in completed) / len(completed)


def assess_scout(ticker: dict, candles: list[dict], symbol: str) -> dict:
    price = ticker["price"]
    change_pct = ticker["change_pct"]
    high_24h = ticker["high_24h"]
    low_24h = ticker["low_24h"]

    avg_7d = seven_day_average(candles)
    dev_pct = ((price - avg_7d) / avg_7d) * 100  # + above avg, - below avg

    # Trend direction
    if dev_pct > 1.0 and change_pct > 0:
        trend = "BULLISH"
    elif dev_pct < -1.0 and change_pct < 0:
        trend = "BEARISH"
    elif abs(dev_pct) <= 1.0:
        trend = "SIDEWAYS"
    else:
        trend = "MIXED"  # price above avg but falling, or below avg but rising

    # Structure: simple high/low range of last 7 days
    all_highs = [c["high"] for c in candles[:-1]]
    all_lows  = [c["low"]  for c in candles[:-1]]
    week_high = max(all_highs)
    week_low  = min(all_lows)

    if price > week_high * 0.99:
        structure = "AT_WEEKLY_HIGH — resistance zone"
    elif price < week_low * 1.01:
        structure = "AT_WEEKLY_LOW — support zone"
    elif price > avg_7d:
        structure = "ABOVE_7D_AVG — upper half of range"
    else:
        structure = "BELOW_7D_AVG — lower half of range"

    # Compression: 24h range vs 7-day average daily range
    avg_daily_range_pct = sum(
        (c["high"] - c["low"]) / c["close"] * 100 for c in candles[:-1]
    ) / len(candles[:-1])
    current_range_pct = (high_24h - low_24h) / price * 100
    compression = (
        "YES — range contracting" if current_range_pct < avg_daily_range_pct * 0.7
        else "NO — normal range"
    )

    # Key levels
    key_levels = f"R: {week_high:,.2f} | S: {week_low:,.2f} | 7D_AVG: {avg_7d:,.2f}"

    # Invalidation
    if trend == "BULLISH":
        invalidation = f"Close below 7D_AVG ({avg_7d:,.2f})"
    elif trend == "BEARISH":
        invalidation = f"Close above 7D_AVG ({avg_7d:,.2f})"
    else:
        invalidation = f"Break outside week range ({week_low:,.2f} – {week_high:,.2f})"

    # STATE — based on deviation from 7D average
    abs_dev = abs(dev_pct)
    if abs_dev >= SETUP_THRESHOLD and trend in ("BULLISH", "BEARISH"):
        state = "SETUP"
        signal = f"Price {dev_pct:+.2f}% from 7D avg with aligned trend"
    elif abs_dev >= WATCHLIST_THRESHOLD:
        state = "WATCHLIST"
        signal = f"Price {dev_pct:+.2f}% from 7D avg — monitoring for continuation"
    else:
        state = "NO_TRADE"
        signal = f"Price within ±{WATCHLIST_THRESHOLD}% of 7D avg — no clear bias"

    reason = (
        f"Current price {price:,.2f} is {dev_pct:+.2f}% vs 7D avg {avg_7d:,.2f}. "
        f"24h change: {change_pct:+.2f}%. "
        f"Trend: {trend}. "
        f"24h range: {current_range_pct:.2f}% vs avg daily range {avg_daily_range_pct:.2f}%."
    )

    return {
        "symbol":       symbol,
        "price":        price,
        "change_pct":   change_pct,
        "avg_7d":       avg_7d,
        "dev_pct":      dev_pct,
        "week_high":    week_high,
        "week_low":     week_low,
        "trend":        trend,
        "structure":    structure,
        "compression":  compression,
        "key_levels":   key_levels,
        "invalidation": invalidation,
        "state":        state,
        "signal":       signal,
        "reason":       reason,
    }


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def format_scout_block(a: dict, ts: str) -> str:
    hist = a.get("macd_histogram", float("nan"))
    hist_str = f"{hist:.6f}" if not (isinstance(hist, float) and math.isnan(hist)) else "N/A"
    return f"""\
AGENT: Scout
SYMBOL: {a['symbol']}
TIMEFRAME: 1D
DATE: {ts}
TREND: {a['trend']}
STRUCTURE: {a['structure']}
COMPRESSION: {a['compression']}
KEY_LEVELS: {a['key_levels']}
INVALIDATION: {a['invalidation']}
STATE: {a['state']}
SIGNAL: {a['signal']}
REASON: {a['reason']}
--- Flow Analyst ---
RSI_14: {a.get('rsi', 'N/A')}
MACD_TREND: {a.get('macd_trend', 'N/A')}
MACD_HISTOGRAM: {hist_str}
OBV_TREND: {a.get('obv_trend', 'N/A')}
VOLUME_FLOW: {a.get('volume_flow', 'N/A')}
ATR_14: {a.get('atr', 'N/A')}
STOP_DIST (ATR×1.5): {a.get('stop_dist', 'N/A')}
SUGGESTED_STOP: {a.get('suggested_stop', 'N/A')}"""


def format_system_health_block(
    total_requested: int,
    assessments: list[dict],
    failed_symbols: list[str],
    stale_symbols: list[str],
    anomalous_symbols: list[str],
    news: dict,
    pipeline_status: str,
) -> list[str]:
    total_fetched = len(assessments)
    total_excluded = len(failed_symbols) + len(stale_symbols) + len(anomalous_symbols)

    news_source = news["source"] if news["source"] else "NONE"
    news_status = "OK" if not news["error"] else "FAILED"

    lines = [
        "## System Health",
        "",
        "```",
        f"TOTAL_ASSETS_REQUESTED:  {total_requested}",
        f"TOTAL_ASSETS_FETCHED:    {total_fetched}",
        f"TOTAL_ASSETS_EXCLUDED:   {total_excluded}",
    ]

    if failed_symbols:
        lines.append(f"FAILED_ASSETS:           {', '.join(failed_symbols)}")
    else:
        lines.append("FAILED_ASSETS:           none")

    if stale_symbols:
        lines.append(f"STALE_ASSETS:            {', '.join(stale_symbols)}")
    else:
        lines.append("STALE_ASSETS:            none")

    if anomalous_symbols:
        lines.append(f"ANOMALOUS_ASSETS:        {', '.join(anomalous_symbols)}")
    else:
        lines.append("ANOMALOUS_ASSETS:        none")

    lines += [
        f"NEWS_SENTINEL_SOURCE:    {news_source}",
        f"NEWS_SENTINEL_STATUS:    {news_status}",
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
    news: dict | None = None,
    failed_symbols: list[str] | None = None,
    stale_symbols: list[str] | None = None,
    anomalous_symbols: list[str] | None = None,
    pipeline_status: str = "HEALTHY",
) -> str:
    failed_symbols = failed_symbols or []
    stale_symbols = stale_symbols or []
    anomalous_symbols = anomalous_symbols or []

    date_str = run_dt.strftime("%Y-%m-%d")
    time_str = run_dt.strftime("%H:%M UTC")
    ts = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    btc_assessment = next((a for a in assessments if a["symbol"] == "BTCUSDT"), None)
    btc_trend = btc_assessment["trend"] if btc_assessment else "UNKNOWN"
    filter_status = (
        f"ACTIVE — BTC trend is {btc_trend}; altcoin SETUP signals downgraded to WATCHLIST"
        if btc_filter_active
        else f"INACTIVE — BTC trend is {btc_trend}; altcoin signals unmodified"
    )

    lines = [
        "---",
        "schema_type: scout_report",
        "schema_version: 1.0",
        "---",
        f"# Euru OS — Morning Scan Report",
        f"**Date:** {date_str}  ",
        f"**Time:** {time_str}  ",
        f"**Assets scanned:** {len(assessments)}  ",
        f"**Mode:** READ_ONLY  ",
        f"**BTC Master Filter (Module 01):** {filter_status}  ",
        "",
        "---",
        "",
    ]

    # System Health section (top of report)
    if news is not None:
        lines += format_system_health_block(
            total_requested=len(SYMBOLS),
            assessments=assessments,
            failed_symbols=failed_symbols,
            stale_symbols=stale_symbols,
            anomalous_symbols=anomalous_symbols,
            news=news,
            pipeline_status=pipeline_status,
        )
    lines += ["", "---", ""]

    lines += [
        "## Price Summary",
        "",
        "| Symbol | Price (USDT) | 24h | vs 7D | RSI | MACD | OBV | Stop Dist | Score | Tier | State |",
        "|--------|-------------|-----|-------|-----|------|-----|-----------|-------|------|-------|",
    ]

    for a in assessments:
        score_str = f"{a['score']}/{a['score_max']}" if "score" in a else "N/A"
        lines.append(
            f"| {a['symbol']} "
            f"| {a['price']:>12,.2f} "
            f"| {a['change_pct']:>+.2f}% "
            f"| {a['dev_pct']:>+.2f}% "
            f"| {a.get('rsi', 'N/A')} "
            f"| {a.get('macd_trend', 'N/A')} "
            f"| {a.get('obv_trend', 'N/A')} "
            f"| {a.get('stop_dist', 'N/A')} "
            f"| **{score_str}** "
            f"| {a.get('tier', 'N/A')} "
            f"| **{a['state']}** |"
        )

    # Score leaderboard — sorted by score descending
    scored_assets = [a for a in assessments if "score" in a]
    if scored_assets:
        sorted_by_score = sorted(scored_assets, key=lambda a: a["score"], reverse=True)
        from euru_score_engine import CRITERIA
        lines += [
            "", "---", "", "## Score Leaderboard", "",
            "| Rank | Symbol | Score | Tier | Liq | Vol | Str | Nar | RS | Exc | Pot |",
            "|------|--------|-------|------|-----|-----|-----|-----|----|-----|-----|",
        ]
        for rank, a in enumerate(sorted_by_score, 1):
            sb = a["score_breakdown"]
            lines.append(
                f"| {rank} "
                f"| {a['symbol']} "
                f"| **{a['score']}/{a['score_max']}** ({a['score_pct']:.0f}%) "
                f"| **{a['tier']}** "
                f"| {sb['Liquidity']} "
                f"| {sb['Volume']} "
                f"| {sb['Structure']} "
                f"| {sb['Narrative']} "
                f"| {sb['RelativeStrength']} "
                f"| {sb['Exchange']} "
                f"| {sb['Potential']} |"
            )

    # News Sentinel section
    lines += ["", "---", "", "## News Sentinel", ""]
    if news is not None:
        lines.append("```")
        lines.append(format_news_sentinel_block(news, ts))
        lines.append("```")
    else:
        lines.append("*News Sentinel not run.*")
    lines.append("")

    lines += ["---", "", "## Scout Assessments", ""]

    for a in assessments:
        lines.append(f"### {a['symbol']}")
        lines.append("")
        lines.append("```")
        lines.append(format_scout_block(a, ts))
        lines.append("```")
        lines.append("")

    lines += [
        "---",
        "",
        f"*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    run_dt = datetime.now(timezone.utc)
    date_str = run_dt.strftime("%Y-%m-%d")

    print(f"Euru OS — Morning Scan [{date_str}]")
    print(f"Fetching data from Binance public API...\n")

    assessments = []
    failed_symbols: list[str] = []
    stale_symbols: list[str] = []
    anomalous_symbols: list[str] = []
    btc_change_pct = 0.0  # baseline for relative strength; captured on first BTCUSDT pass

    for symbol in SYMBOLS:
        try:
            ticker = get_ticker_24h(symbol)

            # Staleness check — exclude asset if last update > STALE_MINUTES old
            if is_stale(ticker["close_time_ms"], run_dt):
                print(f"  {symbol}: STALE — last update older than {STALE_MINUTES} min, excluding from report")
                stale_symbols.append(symbol)
                continue

            # Zero / negative price check
            if ticker["price"] <= 0:
                print(f"  {symbol}: ANOMALY — price={ticker['price']} is zero or negative, excluding from report")
                anomalous_symbols.append(symbol)
                continue

            candles       = get_daily_klines(symbol, limit=100)
            scout_candles = candles[-8:]
            avg_7d        = seven_day_average(scout_candles)

            # Impossible deviation check — requires avg_7d
            anomaly, reason = is_anomalous_price(ticker["price"], avg_7d)
            if anomaly:
                print(f"  {symbol}: ANOMALY — {reason}, excluding from report")
                anomalous_symbols.append(symbol)
                continue

            assessment = assess_scout(ticker, scout_candles, symbol)

            # Capture BTC baseline for relative strength scoring
            if symbol == "BTCUSDT":
                btc_change_pct = ticker["change_pct"]

            # Flow Analyst — RSI, MACD, OBV, ATR
            flow = _run_flow_analyst(symbol, candles)
            assessment["rsi"]            = flow["rsi"]
            assessment["rsi_raw"]        = flow["rsi_raw"]
            assessment["macd_trend"]     = flow["macd_trend"]
            assessment["macd_histogram"] = flow["macd_histogram"]
            assessment["obv_trend"]      = flow["obv_trend"]
            assessment["volume_flow"]    = flow["volume_flow"]
            assessment["atr"]            = flow["atr"]
            assessment["stop_dist"]      = flow["stop_dist"]
            assessment["suggested_stop"] = flow["suggested_stop"]

            # Score Engine — 7-criterion composite score
            scored = _run_score_engine(symbol, ticker, candles[-8:], btc_change_pct)
            assessment["score"]       = scored["total"]
            assessment["score_max"]   = scored["max"]
            assessment["score_pct"]   = scored["pct"]
            assessment["tier"]        = scored["tier"]
            assessment["score_breakdown"] = scored["scores"]

            assessments.append(assessment)
            print(
                f"  {symbol:10s}  price={ticker['price']:>12,.2f}  "
                f"24h={ticker['change_pct']:>+6.2f}%  "
                f"dev={assessment['dev_pct']:>+6.2f}%  "
                f"RSI={assessment['rsi']:>6}  "
                f"MACD={assessment['macd_trend']:8s}  "
                f"OBV={assessment['obv_trend']:7s}  "
                f"score={assessment['score']:>2}/{assessment['score_max']} [{assessment['tier']:7s}]  "
                f"=> {assessment['state']}"
            )
        except urllib.error.URLError as e:
            print(f"  {symbol}: network error after {RETRY_MAX} attempts — {e}")
            failed_symbols.append(symbol)
        except Exception as e:
            print(f"  {symbol}: unexpected error — {e}")
            failed_symbols.append(symbol)

    if not assessments:
        print("\nNo data retrieved. Aborting report.")
        return

    # Pipeline status — DEGRADED if more than 30% of assets were excluded
    total_requested = len(SYMBOLS)
    total_excluded = len(failed_symbols) + len(stale_symbols) + len(anomalous_symbols)
    pipeline_status = (
        "DEGRADED"
        if total_excluded / total_requested > DEGRADED_FAIL_THRESHOLD
        else "HEALTHY"
    )

    # News Sentinel
    print("\nRunning News Sentinel...")
    news = run_news_sentinel()
    severity_icon = {"HIGH": "(!)", "MEDIUM": "(~)", "LOW": "( )", "UNKNOWN": "(?)"}
    icon = severity_icon.get(news["overall_severity"], "(?)")
    print(f"  Overall severity: {icon} {news['overall_severity']}")
    for i, (title, sev) in enumerate(news["top_headlines"], 1):
        print(f"  {i}. [{sev}] {title}")
    if news["error"]:
        print(f"  Warning: {news['error']}")

    # Pipeline status summary
    print(f"\nPipeline status: {pipeline_status}")
    if pipeline_status == "DEGRADED":
        print(
            f"  WARNING: {total_excluded}/{total_requested} assets excluded "
            f"({total_excluded / total_requested * 100:.0f}%) — report is incomplete"
        )
    if stale_symbols:
        print(f"  Stale: {', '.join(stale_symbols)}")
    if anomalous_symbols:
        print(f"  Anomalous: {', '.join(anomalous_symbols)}")
    if failed_symbols:
        print(f"  Failed: {', '.join(failed_symbols)}")

    # BTC Module 01 master filter
    btc = next((a for a in assessments if a["symbol"] == "BTCUSDT"), None)
    btc_filter_active = btc is not None and btc["trend"] in ("SIDEWAYS", "BEARISH")
    if btc_filter_active:
        print(f"\n  [BTC Master Filter] BTC trend={btc['trend']} -- downgrading altcoin SETUP -> WATCHLIST")
        for a in assessments:
            if a["symbol"] != "BTCUSDT" and a["state"] == "SETUP":
                a["state"] = "WATCHLIST"
                a["signal"] = (
                    f"[BTC filter] Downgraded from SETUP — BTC trend is {btc['trend']}. "
                    + a["signal"]
                )

    report = build_report(
        assessments=assessments,
        run_dt=run_dt,
        btc_filter_active=btc_filter_active,
        news=news,
        failed_symbols=failed_symbols,
        stale_symbols=stale_symbols,
        anomalous_symbols=anomalous_symbols,
        pipeline_status=pipeline_status,
    )

    # Breakout Intelligence Layer (4H)
    if _BREAKOUT_AVAILABLE:
        print("\nRunning Breakout Intelligence Scanner (4H)...")
        try:
            breakout_results = _run_breakout_scan(SYMBOLS, run_dt)
            breakout_section = _fmt_breakout_section(breakout_results)
            # Insert the Breakout section before the morning-scan footer line
            _footer = "*Generated by euru_morning_scan.py"
            if _footer in report:
                _split_idx = report.rfind(_footer)
                _line_start = report.rfind("\n", 0, _split_idx) + 1
                report = report[:_line_start] + breakout_section + "\n\n" + report[_line_start:]
            else:
                report += "\n\n" + breakout_section
        except Exception as _exc:
            print(f"  [Breakout] Scanner error: {_exc} — section omitted from report")
    else:
        print("\n  [Breakout] euru_breakout_scanner not available — skipping breakout layer")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"SCOUT_REPORT_{date_str}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport saved => {output_path}")


if __name__ == "__main__":
    main()
    try:
        from euru_trade_monitor import main as trade_monitor_main
        import sys as _sys
        _sys.argv = ['euru_trade_monitor.py']
        trade_monitor_main()
    except Exception as _te:
        print(f"[trade-monitor] Skipped: {_te}")
    try:
        from euru_git_sync import git_sync
        git_sync("morning scan report")
    except Exception as _e:
        print(f"[git-sync] Skipped: {_e}")
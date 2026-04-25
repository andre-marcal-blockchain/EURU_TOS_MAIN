"""
Euru OS — Score Engine
Calculates a 0–35 composite score for each asset on the watchlist based on
seven criteria, each scored 0–5. Classifies every asset into a tier and
produces a suggested action.

Scoring criteria (7 × 5 = 35 max):
    1. Liquidity       — 24h volume depth and bid/ask spread quality
    2. Volume          — volume trend: growing, shrinking, or flat vs 7-day avg
    3. Structure       — Scout state (SETUP=5, WATCHLIST=3, NO_TRADE=0) + key level proximity
    4. Narrative       — macro/sector relevance (AI, DeFi, L1, L2, RWA, etc.)
    5. RelativeStrength— performance vs BTC over the last 7 days
    6. Exchange        — exchange listing quality (Binance spot=5, Bybit=4, smaller=lower)
    7. Potential       — upside distance to next structural resistance level

Tier classification (total score out of 35):
    PREMIUM  — 28–35  (≥80%)  — highest conviction, priority watchlist
    BOA      — 21–27  (≥60%)  — good setup, secondary watchlist
    MEDIA    — 14–20  (≥40%)  — marginal, monitor only
    IGNORAR  —  0–13  (<40%)  — exclude from pipeline

Usage:
    python euru_score_engine.py                 # scores all SYMBOLS
    python euru_score_engine.py BTCUSDT ETHUSDT # scores specific symbols

Output: 08_DADOS_E_JOURNAL/SCORECARDS/SCORE_REPORT_<YYYY-MM-DD>.md
"""

import json
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

# Tier thresholds (inclusive lower bound)
TIER_PREMIUM = 28
TIER_BOA     = 21
TIER_MEDIA   = 14
# below TIER_MEDIA → IGNORAR

# Per-criterion max score
CRITERION_MAX = 5
CRITERIA = [
    "Liquidity",
    "Volume",
    "Structure",
    "Narrative",
    "RelativeStrength",
    "Exchange",
    "Potential",
]
MAX_SCORE = CRITERION_MAX * len(CRITERIA)  # 35

# Narrative tags — assigned per symbol for scoring purposes
# Update this map as sector relevance changes.
# 3 = moderate relevance, 5 = strong narrative (AI/DeFi trend, recent news driver)
NARRATIVE_SCORES: dict[str, int] = {
    "BTCUSDT":    5,  # digital gold, macro narrative
    "ETHUSDT":    5,  # L1 ecosystem, restaking narrative
    "SOLUSDT":    5,  # high-throughput L1, retail favourite
    "BNBUSDT":    4,  # exchange token
    "AVAXUSDT":   4,  # L1, institutional subnet use-case
    "DOTUSDT":    3,  # parachain interoperability
    "LINKUSDT":   4,  # oracle infrastructure
    "ADAUSDT":    3,  # L1
    "XRPUSDT":    4,  # payments, ETF narrative
    "MATICUSDT":  4,  # L2 / Polygon
    "SUIUSDT":    4,  # new L1
    "NEARUSDT":   3,  # L1
    "INJUSDT":    4,  # DeFi/derivatives L1
    "ARBUSDT":    4,  # L2
    "OPUSDT":     4,  # L2
    "FETUSDT":    5,  # AI agent narrative
    "TAOUSDT":    5,  # AI / decentralised ML narrative
    "RENDERUSDT": 5,  # AI / GPU compute narrative
}

# Exchange tier scores — Binance spot is best available for this watchlist
EXCHANGE_SCORES: dict[str, int] = {s: 5 for s in SYMBOLS}  # all on Binance spot

# Error handling
RETRY_MAX           = 3
RETRY_DELAY_SECONDS = 5
STALE_MINUTES       = 10
DEGRADED_FAIL_RATIO = 0.30

# Volume trend thresholds (today vs 7-day avg)
VOLUME_STRONG_RATIO = 1.20   # today 20%+ above avg → score 5
VOLUME_ABOVE_RATIO  = 1.05   # today 5–20% above avg → score 4
VOLUME_FLAT_LOW     = 0.90   # today within ±10% of avg → score 3; below 90% → lower

# Liquidity thresholds (daily USDT volume)
LIQUIDITY_TIERS = [
    (500_000_000, 5),   # > $500M
    (100_000_000, 4),   # $100M – $500M
    (25_000_000,  3),   # $25M – $100M
    (5_000_000,   2),   # $5M – $25M
    (0,           1),   # > $0
]


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


def get_ticker_24h(symbol: str) -> dict:
    data = fetch_json_with_retry(f"{BINANCE_BASE}/ticker/24hr?symbol={symbol}")
    return {
        "price":         float(data["lastPrice"]),
        "change_pct":    float(data["priceChangePercent"]),
        "volume":        float(data["quoteVolume"]),
        "close_time_ms": int(data["closeTime"]),
    }


def get_daily_klines(symbol: str, limit: int = 8) -> list[dict]:
    raw = fetch_json_with_retry(
        f"{BINANCE_BASE}/klines?symbol={symbol}&interval=1d&limit={limit}"
    )
    return [{"close": float(k[4]), "volume": float(k[7])} for k in raw]


def is_stale(close_time_ms: int, now: datetime) -> bool:
    close_dt = datetime.fromtimestamp(close_time_ms / 1000, tz=timezone.utc)
    return (now - close_dt).total_seconds() / 60 > STALE_MINUTES


# ---------------------------------------------------------------------------
# Scoring functions (0–5 each)
# ---------------------------------------------------------------------------

def score_liquidity(volume_usdt: float) -> int:
    """
    Scores 24h USDT trading volume against LIQUIDITY_TIERS.

    Higher volume = higher score. A score of 1 means tradeable but thin.
    A score of 5 means deep liquidity, minimal slippage expected.

    Args:
        volume_usdt: 24h quote volume in USDT.

    Returns:
        Integer score 0–5.
    """
    for threshold, score in LIQUIDITY_TIERS:
        if volume_usdt >= threshold:
            return score
    return 0


def score_volume(today_volume: float, avg_7d_volume: float) -> int:
    """
    Scores the ratio of today's volume vs the 7-day average daily volume.

    Rising volume during a move is a confirmation signal; shrinking volume
    suggests the move is losing participation.

    Args:
        today_volume:   Today's USDT volume.
        avg_7d_volume:  Average daily USDT volume over the last 7 days.

    Returns:
        Integer score 0–5.

    TODO: implement ratio comparison against VOLUME_STRONG_RATIO, VOLUME_ABOVE_RATIO,
          VOLUME_FLAT_LOW thresholds. Return 0 if avg_7d_volume is 0.
    """
    if avg_7d_volume <= 0:
        return 0

    ratio = today_volume / avg_7d_volume
    if ratio >= VOLUME_STRONG_RATIO:
        return 5
    if ratio >= VOLUME_ABOVE_RATIO:
        return 4
    if ratio >= VOLUME_FLAT_LOW:
        return 3
    if ratio >= 0.70:
        return 2
    return 1


def score_structure(scout_state: str, dev_pct: float) -> int:
    """
    Scores the asset's structural position using Scout output and price deviation.

    SETUP assets with strong deviation score highest. Assets at NO_TRADE
    score 0 — they do not belong in the scored pipeline.

    Args:
        scout_state: "SETUP" | "WATCHLIST" | "NO_TRADE"
        dev_pct:     Price deviation from 7-day average (signed %).

    Returns:
        Integer score 0–5.

    TODO: base score from scout_state: SETUP=4, WATCHLIST=2, NO_TRADE=0
    TODO: add +1 bonus if |dev_pct| >= 5% (strong deviation from mean)
    TODO: cap at 5
    """
    base  = {"SETUP": 4, "WATCHLIST": 2, "NO_TRADE": 0}.get(scout_state, 0)
    bonus = 1 if abs(dev_pct) >= 5.0 else 0
    return min(base + bonus, CRITERION_MAX)


def score_narrative(symbol: str) -> int:
    """
    Returns the narrative score for the symbol from NARRATIVE_SCORES map.

    Narrative reflects macro/sector relevance at the time of the last map
    update. This is the only criterion that is manually maintained and
    does not pull live data.

    Args:
        symbol: Trading pair, e.g. "BTCUSDT".

    Returns:
        Integer score 0–5 from NARRATIVE_SCORES, or 2 as a conservative default.
    """
    return NARRATIVE_SCORES.get(symbol, 2)


def score_relative_strength(symbol_change_pct: float, btc_change_pct: float) -> int:
    """
    Scores how the asset's 24h performance compares to BTC's 24h performance.

    An asset that outperforms BTC in a rising market, or holds better in a
    falling market, demonstrates relative strength — a bullish signal.

    Args:
        symbol_change_pct: Asset's 24h price change %.
        btc_change_pct:    BTC's 24h price change %.

    Returns:
        Integer score 0–5.

    TODO: diff = symbol_change_pct - btc_change_pct
    TODO: score based on diff magnitude:
          diff >= +5%  → 5 (strongly outperforming)
          diff >= +2%  → 4
          diff >= 0%   → 3 (keeping pace)
          diff >= -2%  → 2 (mild underperformance)
          diff >= -5%  → 1
          diff <  -5%  → 0 (strongly underperforming)
    """
    diff = symbol_change_pct - btc_change_pct
    if diff >= 5.0:
        return 5
    if diff >= 2.0:
        return 4
    if diff >= 0.0:
        return 3
    if diff >= -2.0:
        return 2
    if diff >= -5.0:
        return 1
    return 0


def score_exchange(symbol: str) -> int:
    """
    Returns the exchange listing quality score for the symbol.

    All symbols in the current watchlist are on Binance spot (score 5).
    This function is a hook for future expansion when non-Binance assets
    are added.

    Args:
        symbol: Trading pair.

    Returns:
        Integer score 0–5 from EXCHANGE_SCORES, or 3 as default.
    """
    return EXCHANGE_SCORES.get(symbol, 3)


def score_potential(price: float, week_high: float, week_low: float) -> int:
    """
    Scores the upside potential based on proximity to weekly resistance.

    An asset sitting near its weekly low with resistance far above has more
    upside potential than one already at the weekly high.

    Args:
        price:     Current price.
        week_high: Highest price over the last 7 daily candles.
        week_low:  Lowest price over the last 7 daily candles.

    Returns:
        Integer score 0–5.

    TODO: distance_to_r = (week_high - price) / price * 100
    TODO: score from distance:
          >= 10%  → 5 (plenty of room)
          >= 6%   → 4
          >= 3%   → 3
          >= 1%   → 2
          >= 0%   → 1 (at or near resistance)
          < 0%    → 0 (above recent high, anomalous)
    """
    if week_high <= 0:
        return 0
    distance_to_r = (week_high - price) / price * 100
    if distance_to_r >= 10.0:
        return 5
    if distance_to_r >= 6.0:
        return 4
    if distance_to_r >= 3.0:
        return 3
    if distance_to_r >= 1.0:
        return 2
    if distance_to_r >= 0.0:
        return 1
    return 0  # price above recent high


# ---------------------------------------------------------------------------
# Score aggregation and tier classification
# ---------------------------------------------------------------------------

def classify_tier(total_score: int) -> tuple[str, str]:
    """
    Maps a total score (0–35) to a tier name and a suggested action.

    Returns:
        Tuple of (tier: str, action: str).
    """
    if total_score >= TIER_PREMIUM:
        return "PREMIUM", "Add to priority watchlist. Monitor for entry trigger."
    if total_score >= TIER_BOA:
        return "BOA",     "Add to secondary watchlist. Wait for Scout SETUP signal."
    if total_score >= TIER_MEDIA:
        return "MEDIA",   "Monitor only. Do not allocate attention until score improves."
    return "IGNORAR",     "Exclude from pipeline. Revisit next weekly review."


def compute_score(
    symbol: str,
    ticker: dict,
    candles: list[dict],
    btc_change_pct: float,
) -> dict:
    """
    Computes all 7 criterion scores and the total for a single asset.

    Args:
        symbol:         Trading pair.
        ticker:         Output of get_ticker_24h().
        candles:        Output of get_daily_klines(limit=8).
        btc_change_pct: BTC's 24h change % for relative strength comparison.

    Returns:
        dict with individual criterion scores, total, tier, and action.
    """
    price      = ticker["price"]
    change_pct = ticker["change_pct"]
    volume_24h = ticker["volume"]

    completed = candles[:-1]  # exclude still-open current candle
    avg_7d_vol = sum(c["volume"] for c in completed) / len(completed) if completed else 0.0
    avg_7d_close = sum(c["close"] for c in completed) / len(completed) if completed else price
    dev_pct      = ((price - avg_7d_close) / avg_7d_close) * 100 if avg_7d_close > 0 else 0.0
    week_high    = max(c["close"] for c in completed) if completed else price
    week_low     = min(c["close"] for c in completed) if completed else price

    # Derive a lightweight Scout state for the structure criterion
    # (mirrors morning scan logic — avoids importing the full scout module)
    if abs(dev_pct) >= 3.0 and ((dev_pct > 0 and change_pct > 0) or (dev_pct < 0 and change_pct < 0)):
        scout_state = "SETUP"
    elif abs(dev_pct) >= 1.0:
        scout_state = "WATCHLIST"
    else:
        scout_state = "NO_TRADE"

    scores = {
        "Liquidity":        score_liquidity(volume_24h),
        "Volume":           score_volume(volume_24h, avg_7d_vol),
        "Structure":        score_structure(scout_state, dev_pct),
        "Narrative":        score_narrative(symbol),
        "RelativeStrength": score_relative_strength(change_pct, btc_change_pct),
        "Exchange":         score_exchange(symbol),
        "Potential":        score_potential(price, week_high, week_low),
    }

    total = sum(scores.values())
    tier, action = classify_tier(total)

    return {
        "symbol":       symbol,
        "price":        price,
        "change_pct":   change_pct,
        "scout_state":  scout_state,
        "scores":       scores,
        "total":        total,
        "max":          MAX_SCORE,
        "pct":          total / MAX_SCORE * 100,
        "tier":         tier,
        "action":       action,
    }


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def format_score_block(r: dict, ts: str) -> str:
    score_lines = "\n".join(
        f"  {crit:<20} {r['scores'][crit]}/{CRITERION_MAX}"
        for crit in CRITERIA
    )
    return f"""\
AGENT: Score Engine
SYMBOL: {r['symbol']}
DATE: {ts}
PRICE: {r['price']:,.4f}
SCOUT_STATE: {r['scout_state']}
--- SCORES ---
{score_lines}
--------------
TOTAL: {r['total']}/{r['max']} ({r['pct']:.1f}%)
TIER: {r['tier']}
ACTION: {r['action']}"""


def format_system_health_block(
    total_requested: int,
    results: list[dict],
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
        f"TOTAL_ASSETS_SCORED:     {len(results)}",
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
    results: list[dict],
    run_dt: datetime,
    failed: list[str],
    stale: list[str],
    pipeline_status: str,
) -> str:
    date_str = run_dt.strftime("%Y-%m-%d")
    time_str = run_dt.strftime("%H:%M UTC")
    ts       = run_dt.strftime("%Y-%m-%d %H:%M UTC")

    # Sort by total score descending
    sorted_results = sorted(results, key=lambda r: r["total"], reverse=True)

    tier_counts = {"PREMIUM": 0, "BOA": 0, "MEDIA": 0, "IGNORAR": 0}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1

    lines = [
        "# Euru OS — Score Engine Report",
        f"**Date:** {date_str}  ",
        f"**Time:** {time_str}  ",
        f"**Assets scored:** {len(results)}  ",
        f"**Mode:** READ_ONLY  ",
        f"**Tier summary:** "
        f"PREMIUM={tier_counts['PREMIUM']}  "
        f"BOA={tier_counts['BOA']}  "
        f"MEDIA={tier_counts['MEDIA']}  "
        f"IGNORAR={tier_counts['IGNORAR']}  ",
        "",
        "---",
        "",
    ]

    lines += format_system_health_block(
        len(SYMBOLS), results, failed, stale, pipeline_status
    )

    lines += [
        "", "---", "", "## Score Leaderboard", "",
        f"| Rank | Symbol | Score | Tier | Scout State | Action |",
        f"|------|--------|-------|------|------------|--------|",
    ]

    for rank, r in enumerate(sorted_results, 1):
        lines.append(
            f"| {rank} "
            f"| {r['symbol']} "
            f"| {r['total']}/{r['max']} ({r['pct']:.0f}%) "
            f"| **{r['tier']}** "
            f"| {r['scout_state']} "
            f"| {r['action']} |"
        )

    # Criterion breakdown table
    lines += ["", "---", "", "## Criterion Breakdown", "",
              "| Symbol | " + " | ".join(CRITERIA) + " | Total |",
              "|--------|" + "|".join("---" for _ in CRITERIA) + "|-------|"]

    for r in sorted_results:
        cells = " | ".join(str(r["scores"][c]) for c in CRITERIA)
        lines.append(f"| {r['symbol']} | {cells} | **{r['total']}** |")

    lines += ["", "---", "", "## Detailed Score Blocks", ""]

    for r in sorted_results:
        lines.append(f"### {r['symbol']}  ({r['tier']})")
        lines.append("")
        lines.append("```")
        lines.append(format_score_block(r, ts))
        lines.append("```")
        lines.append("")

    lines += [
        "---",
        "",
        "*Generated by euru_score_engine.py — Euru OS READ_ONLY phase*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    run_dt   = datetime.now(timezone.utc)
    date_str = run_dt.strftime("%Y-%m-%d")

    symbols = sys.argv[1:] if len(sys.argv) > 1 else SYMBOLS

    print(f"Euru OS — Score Engine [{date_str}]")
    print(f"Scoring {len(symbols)} assets against 7 criteria (max {MAX_SCORE} points)\n")

    # Fetch BTC data first — needed for relative strength comparison
    btc_change_pct = 0.0
    if "BTCUSDT" in symbols or not sys.argv[1:]:
        try:
            btc_ticker = get_ticker_24h("BTCUSDT")
            btc_change_pct = btc_ticker["change_pct"]
            print(f"  BTC baseline 24h change: {btc_change_pct:+.2f}%\n")
        except Exception as e:
            print(f"  WARNING: could not fetch BTC baseline — relative strength scores will be 0: {e}\n")

    results: list[dict] = []
    failed:  list[str]  = []
    stale:   list[str]  = []

    for symbol in symbols:
        try:
            ticker  = get_ticker_24h(symbol)
            candles = get_daily_klines(symbol, limit=8)

            if is_stale(ticker["close_time_ms"], run_dt):
                print(f"  {symbol}: STALE — last update older than {STALE_MINUTES} min, excluding")
                stale.append(symbol)
                continue

            result = compute_score(symbol, ticker, candles, btc_change_pct)
            results.append(result)

            scores_str = "  ".join(f"{c[:3]}={result['scores'][c]}" for c in CRITERIA)
            print(
                f"  {symbol:10s}  {scores_str}  "
                f"total={result['total']}/{result['max']}  "
                f"=> {result['tier']}"
            )
        except urllib.error.URLError as e:
            print(f"  {symbol}: network error after {RETRY_MAX} attempts — {e}")
            failed.append(symbol)
        except Exception as e:
            print(f"  {symbol}: unexpected error — {e}")
            failed.append(symbol)

    if not results:
        print("\nNo data retrieved. Aborting report.")
        return

    total_excluded = len(failed) + len(stale)
    pipeline_status = (
        "DEGRADED"
        if total_excluded / len(symbols) > DEGRADED_FAIL_RATIO
        else "HEALTHY"
    )

    print(f"\nPipeline status: {pipeline_status}")

    report = build_report(results, run_dt, failed, stale, pipeline_status)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"SCORE_REPORT_{date_str}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport saved => {output_path}")


if __name__ == "__main__":
    main()

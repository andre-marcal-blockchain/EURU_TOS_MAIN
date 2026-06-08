"""
AGuia / MAC Asian Session Scanner

READ_ONLY scanner for Binance public market data. It fetches candles, computes
RSI, MACD, OBV, ATR, evaluates the MAC pillars, and writes a Markdown report.

No API keys are used. No orders are placed.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SPOT_BASE = "https://api.binance.com/api/v3"
FUTURES_BASE = "https://fapi.binance.com/fapi/v1"
DEFAULT_SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
SCRIPT_DIR = Path(__file__).resolve().parent
REPORT_DIR = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "SCORECARDS"


@dataclass(frozen=True)
class Candle:
    open_time: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    close_time: int


@dataclass(frozen=True)
class IndicatorState:
    rsi: float
    rsi_prev: float
    macd: float
    macd_signal: float
    macd_hist: float
    macd_hist_prev: float
    obv: float
    obv_prev: float
    atr: float
    volume_ratio: float


def has_invalid_loopback_proxy() -> bool:
    for env_name in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy"):
        proxy = os.environ.get(env_name, "").strip()
        if not proxy:
            continue
        parsed = urllib.parse.urlparse(proxy)
        host = (parsed.hostname or "").lower()
        port = parsed.port
        if host in {"127.0.0.1", "localhost", "::1"} and port == 9:
            return True
    return False


def fetch_json(base_url: str, path: str, params: dict[str, object]) -> object:
    query = urllib.parse.urlencode(params)
    url = f"{base_url}{path}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "AGuiaScanner/1.0"})
    if has_invalid_loopback_proxy():
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(req, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_klines(base_url: str, symbol: str, interval: str, limit: int) -> list[Candle]:
    raw = fetch_json(base_url, "/klines", {"symbol": symbol, "interval": interval, "limit": limit})
    candles: list[Candle] = []
    if not isinstance(raw, list):
        raise ValueError(f"Unexpected kline response for {symbol} {interval}: {raw!r}")
    for row in raw:
        candles.append(
            Candle(
                open_time=int(row[0]),
                open=float(row[1]),
                high=float(row[2]),
                low=float(row[3]),
                close=float(row[4]),
                volume=float(row[5]),
                close_time=int(row[6]),
            )
        )
    return candles


def sma(values: list[float], period: int) -> float:
    if len(values) < period:
        return float("nan")
    return sum(values[-period:]) / period


def ema_series(values: list[float], period: int) -> list[float]:
    if not values:
        return []
    alpha = 2 / (period + 1)
    result = [values[0]]
    for value in values[1:]:
        result.append((value * alpha) + (result[-1] * (1 - alpha)))
    return result


def rsi_series(closes: list[float], period: int = 14) -> list[float]:
    if len(closes) < period + 1:
        return []
    gains: list[float] = []
    losses: list[float] = []
    for prev, current in zip(closes, closes[1:]):
        delta = current - prev
        gains.append(max(delta, 0.0))
        losses.append(abs(min(delta, 0.0)))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    values: list[float] = []
    for i in range(period, len(gains)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period
        if avg_loss == 0:
            values.append(100.0)
        else:
            rs = avg_gain / avg_loss
            values.append(100 - (100 / (1 + rs)))
    return values


def macd_values(closes: list[float]) -> tuple[float, float, float, float]:
    if len(closes) < 35:
        return (float("nan"), float("nan"), float("nan"), float("nan"))
    fast = ema_series(closes, 12)
    slow = ema_series(closes, 26)
    macd_line = [f - s for f, s in zip(fast, slow)]
    signal = ema_series(macd_line, 9)
    hist = [m - s for m, s in zip(macd_line[-len(signal):], signal)]
    return macd_line[-1], signal[-1], hist[-1], hist[-2]


def obv_series(candles: list[Candle]) -> list[float]:
    if not candles:
        return []
    values = [0.0]
    for prev, current in zip(candles, candles[1:]):
        if current.close > prev.close:
            values.append(values[-1] + current.volume)
        elif current.close < prev.close:
            values.append(values[-1] - current.volume)
        else:
            values.append(values[-1])
    return values


def atr(candles: list[Candle], period: int = 14) -> float:
    if len(candles) < period + 1:
        return float("nan")
    true_ranges: list[float] = []
    for prev, current in zip(candles, candles[1:]):
        true_ranges.append(
            max(
                current.high - current.low,
                abs(current.high - prev.close),
                abs(current.low - prev.close),
            )
        )
    return sma(true_ranges, period)


def indicator_state(candles: list[Candle]) -> IndicatorState:
    closes = [c.close for c in candles]
    rsi_vals = rsi_series(closes)
    macd, signal, hist, hist_prev = macd_values(closes)
    obv_vals = obv_series(candles)
    recent_volume = sma([c.volume for c in candles], 3)
    baseline_volume = sma([c.volume for c in candles[:-3]], 20)
    volume_ratio = recent_volume / baseline_volume if baseline_volume and not math.isnan(baseline_volume) else 0.0
    return IndicatorState(
        rsi=rsi_vals[-1] if rsi_vals else float("nan"),
        rsi_prev=rsi_vals[-2] if len(rsi_vals) > 1 else float("nan"),
        macd=macd,
        macd_signal=signal,
        macd_hist=hist,
        macd_hist_prev=hist_prev,
        obv=obv_vals[-1] if obv_vals else float("nan"),
        obv_prev=obv_vals[-4] if len(obv_vals) > 4 else float("nan"),
        atr=atr(candles),
        volume_ratio=volume_ratio,
    )


def trend(candles: list[Candle]) -> str:
    closes = [c.close for c in candles]
    if len(closes) < 55:
        return "UNKNOWN"
    ema20 = ema_series(closes, 20)[-1]
    ema50 = ema_series(closes, 50)[-1]
    last = closes[-1]
    if last > ema20 > ema50:
        return "BULLISH"
    if last < ema20 < ema50:
        return "BEARISH"
    return "SIDEWAYS"


def support_resistance(candles: list[Candle], lookback: int = 20) -> tuple[float, float]:
    window = candles[-lookback - 1 : -1]
    return min(c.low for c in window), max(c.high for c in window)


def compression(candles: list[Candle], length: int = 6) -> tuple[bool, str]:
    window = candles[-length:]
    if len(window) < length:
        return False, "insufficient data"
    ranges = [c.high - c.low for c in window]
    first_half = sum(ranges[:3]) / 3
    second_half = sum(ranges[3:]) / 3
    compressed = second_half <= first_half * 0.85
    return compressed, f"range compression {second_half / first_half:.2f}x recent/base"


def classify_setup(direction: str, candles_4h: list[Candle], state_4h: IndicatorState) -> str:
    support, resistance = support_resistance(candles_4h)
    last = candles_4h[-1]
    compressed, _ = compression(candles_4h)
    near_support = abs(last.close - support) / last.close <= 0.015
    near_resistance = abs(resistance - last.close) / last.close <= 0.015

    if direction == "LONG":
        if last.close > resistance and state_4h.volume_ratio >= 1.2:
            return "Breakout"
        if near_support and state_4h.rsi > 50:
            return "Retest"
        if trend(candles_4h) == "BULLISH" and state_4h.rsi > 50 and state_4h.macd_hist > 0:
            return "Continuation"
        if compressed and state_4h.macd_hist > state_4h.macd_hist_prev:
            return "Sweep+Reversal"
    if direction == "SHORT":
        if last.close < support and state_4h.volume_ratio >= 1.2:
            return "Breakout"
        if near_resistance and state_4h.rsi < 50:
            return "Retest"
        if trend(candles_4h) == "BEARISH" and state_4h.rsi < 50 and state_4h.macd_hist < 0:
            return "Continuation"
        if compressed and state_4h.macd_hist < state_4h.macd_hist_prev:
            return "Sweep+Reversal"
    return "None"


def mac_pillars(direction: str, candles_4h: list[Candle], state_4h: IndicatorState) -> dict[str, bool]:
    current_trend = trend(candles_4h)
    if direction == "LONG":
        return {
            "Movimento": current_trend == "BULLISH",
            "Aceleracao": state_4h.rsi > 50 and state_4h.rsi >= state_4h.rsi_prev and state_4h.macd_hist > 0,
            "Confirmacao": state_4h.obv > state_4h.obv_prev and state_4h.volume_ratio >= 0.85,
        }
    return {
        "Movimento": current_trend == "BEARISH",
        "Aceleracao": state_4h.rsi < 50 and state_4h.rsi <= state_4h.rsi_prev and state_4h.macd_hist < 0,
        "Confirmacao": state_4h.obv < state_4h.obv_prev and state_4h.volume_ratio >= 0.85,
    }


def risk_plan(direction: str, candles_4h: list[Candle], state_4h: IndicatorState) -> dict[str, float | str | bool]:
    entry = candles_4h[-1].close
    stop_distance = state_4h.atr * 1.5
    if math.isnan(stop_distance) or stop_distance <= 0:
        return {"valid": False, "reason": "ATR unavailable"}
    support, resistance = support_resistance(candles_4h)
    if direction == "LONG":
        stop = entry - stop_distance
        target_1 = entry + (stop_distance * 2)
        target_2 = entry + (stop_distance * 3)
        structure_room_r = (resistance - entry) / stop_distance
    else:
        stop = entry + stop_distance
        target_1 = entry - (stop_distance * 2)
        target_2 = entry - (stop_distance * 3)
        structure_room_r = (entry - support) / stop_distance
    return {
        "valid": structure_room_r >= 1.5,
        "entry": entry,
        "stop": stop,
        "target_1": target_1,
        "target_2": target_2,
        "risk_pct_price": (stop_distance / entry) * 100,
        "structure_room_r": structure_room_r,
    }


def verdict_for_symbol(symbol: str, candles_4h: list[Candle], candles_1h: list[Candle]) -> dict[str, object]:
    state_4h = indicator_state(candles_4h)
    state_1h = indicator_state(candles_1h)
    direction = "LONG" if state_4h.macd_hist >= 0 else "SHORT"
    long_pillars = mac_pillars("LONG", candles_4h, state_4h)
    short_pillars = mac_pillars("SHORT", candles_4h, state_4h)
    if sum(short_pillars.values()) > sum(long_pillars.values()):
        direction = "SHORT"
        pillars = short_pillars
    else:
        direction = "LONG"
        pillars = long_pillars
    setup = classify_setup(direction, candles_4h, state_4h)
    plan = risk_plan(direction, candles_4h, state_4h)
    mac_ok = all(pillars.values())
    setup_ok = setup in {"Breakout", "Sweep+Reversal", "Retest", "Continuation", "Narrative+Chart"}
    one_hour_confirms = (state_1h.macd_hist > 0 and direction == "LONG") or (state_1h.macd_hist < 0 and direction == "SHORT")
    decision = "NO_ENTRY"
    reason = "structure_or_confirmation_block"
    if not mac_ok:
        decision = "WAIT"
        reason = "mac_incomplete"
    elif not setup_ok:
        reason = "setup_none"
    elif not plan.get("valid"):
        reason = "risk_plan_invalid"
        if plan.get("reason") == "ATR unavailable":
            reason = "atr_unavailable"
        elif isinstance(plan.get("structure_room_r"), (int, float)):
            reason = "room_r_below_1_5"
    elif not one_hour_confirms:
        reason = "one_hour_not_confirmed"
    if mac_ok and setup_ok and plan.get("valid") and one_hour_confirms:
        decision = "PAPER_ENTRY"
        reason = "all_gates_passed"
    return {
        "symbol": symbol,
        "direction": direction,
        "decision": decision,
        "decision_reason": reason,
        "btc_filter": "SELF" if symbol == "BTCUSDT" else "NOT_APPLIED",
        "setup": setup,
        "trend_4h": trend(candles_4h),
        "pillars": pillars,
        "state_4h": state_4h,
        "state_1h": state_1h,
        "plan": plan,
    }


def fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, float):
        if math.isnan(value):
            return "n/a"
        return f"{value:.{digits}f}"
    return str(value)


def render_report(market: str, results: list[dict[str, object]], errors: list[str]) -> str:
    now = datetime.now(timezone.utc)
    paper_entries = [r for r in results if r["decision"] == "PAPER_ENTRY"]
    reason_counts: dict[str, int] = {}
    for result in results:
        reason = str(result.get("decision_reason", "unknown"))
        reason_counts[reason] = reason_counts.get(reason, 0) + 1
    if errors and len(errors) == len(results) + len(errors):
        top_verdict = "DATA_UNAVAILABLE"
    elif paper_entries:
        top_verdict = "PAPER_ENTRY"
    elif any(r["decision"] == "WAIT" for r in results):
        top_verdict = "WAIT"
    else:
        top_verdict = "NO_ENTRY"

    lines = [
        "# AGuia Asian Session Scan",
        "",
        f"- Generated UTC: {now.isoformat(timespec='seconds')}",
        f"- Market data: Binance {market}",
        "- Mode: READ_ONLY",
        f"- Top verdict: **{top_verdict}**",
        "",
        "## Pair Verdicts",
        "",
        "| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |",
        "|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for result in results:
        state = result["state_4h"]
        plan = result["plan"]
        pillars = result["pillars"]
        mac = "/".join("Y" if pillars[name] else "N" for name in ("Movimento", "Aceleracao", "Confirmacao"))
        lines.append(
            "| {symbol} | {decision} | {reason} | {direction} | {btc_filter} | {setup} | {trend_4h} | {mac} | {rsi} | {hist} | {vol} | {risk} | {room} |".format(
                symbol=result["symbol"],
                decision=result["decision"],
                reason=result["decision_reason"],
                direction=result["direction"],
                btc_filter=result["btc_filter"],
                setup=result["setup"],
                trend_4h=result["trend_4h"],
                mac=mac,
                rsi=fmt(state.rsi, 2),
                hist=fmt(state.macd_hist, 6),
                vol=fmt(state.volume_ratio, 2),
                risk=fmt(plan.get("risk_pct_price", float("nan")), 2),
                room=fmt(plan.get("structure_room_r", float("nan")), 2),
            )
        )
    lines.extend(["", "## Decision Summary", ""])
    for reason, count in sorted(reason_counts.items()):
        lines.append(f"- {reason}: {count}")
    lines.extend(["", "## Trade Plans", ""])
    for result in results:
        plan = result["plan"]
        lines.extend(
            [
                f"### {result['symbol']} - {result['decision']}",
                "",
                f"- Decision reason: {result['decision_reason']}",
                f"- Direction: {result['direction']}",
                f"- Setup: {result['setup']}",
                f"- MAC pillars: {result['pillars']}",
                f"- Entry: {fmt(plan.get('entry', 'n/a'))}",
                f"- Stop: {fmt(plan.get('stop', 'n/a'))}",
                f"- Target 1: {fmt(plan.get('target_1', 'n/a'))}",
                f"- Target 2: {fmt(plan.get('target_2', 'n/a'))}",
                "- Live execution: BLOCKED",
                "",
            ]
        )
    if errors:
        lines.extend(["## Data Errors", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    lines.extend(
        [
            "## Execution Rule",
            "",
            "This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.",
            "",
        ]
    )
    return "\n".join(lines)


def scan(symbols: Iterable[str], market: str) -> tuple[list[dict[str, object]], list[str]]:
    base_url = FUTURES_BASE if market == "futures" else SPOT_BASE
    results: list[dict[str, object]] = []
    errors: list[str] = []
    for symbol in symbols:
        try:
            candles_4h = fetch_klines(base_url, symbol, "4h", 120)
            candles_1h = fetch_klines(base_url, symbol, "1h", 120)
            results.append(verdict_for_symbol(symbol, candles_4h, candles_1h))
        except Exception as exc:
            errors.append(f"{symbol}: {exc}")
    apply_btc_filter(results)
    return results, errors


def apply_btc_filter(results: list[dict[str, object]]) -> None:
    btc = next((result for result in results if result["symbol"] == "BTCUSDT"), None)
    if not btc:
        for result in results:
            if result["symbol"] != "BTCUSDT":
                result["btc_filter"] = "UNKNOWN"
                if result["decision"] == "PAPER_ENTRY":
                    result["decision"] = "WAIT"
                    result["decision_reason"] = "btc_filter_unknown"
        return

    btc_trend = str(btc["trend_4h"])
    for result in results:
        if result["symbol"] == "BTCUSDT":
            continue
        direction = result["direction"]
        if btc_trend == "SIDEWAYS":
            result["btc_filter"] = "ACTIVE_SIDEWAYS"
            if result["decision"] == "PAPER_ENTRY":
                result["decision"] = "WAIT"
                result["decision_reason"] = "btc_filter_active_sideways"
        elif direction == "LONG" and btc_trend != "BULLISH":
            result["btc_filter"] = f"ACTIVE_{btc_trend}"
            if result["decision"] == "PAPER_ENTRY":
                result["decision"] = "WAIT"
                result["decision_reason"] = f"btc_filter_active_{btc_trend.lower()}"
        elif direction == "SHORT" and btc_trend != "BEARISH":
            result["btc_filter"] = f"ACTIVE_{btc_trend}"
            if result["decision"] == "PAPER_ENTRY":
                result["decision"] = "WAIT"
                result["decision_reason"] = f"btc_filter_active_{btc_trend.lower()}"
        else:
            result["btc_filter"] = "INACTIVE"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Run AGuia/MAC Asian Session scanner in READ_ONLY mode.")
    parser.add_argument("--symbols", nargs="+", default=list(DEFAULT_SYMBOLS))
    parser.add_argument("--market", choices=("futures", "spot"), default="futures")
    parser.add_argument("--out-dir", default=str(REPORT_DIR))
    parser.add_argument("--print", action="store_true", help="Print the report to stdout.")
    args = parser.parse_args(argv)

    results, errors = scan(args.symbols, args.market)
    report = render_report(args.market, results, errors)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / f"AGUIA_ASIAN_SCAN_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    report_path.write_text(report, encoding="utf-8")

    if args.print:
        print(report)
    else:
        print(f"Wrote {report_path}")
        if errors:
            print("Completed with data errors:")
            for error in errors:
                print(f"- {error}")
    return 0 if results else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

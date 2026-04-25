#!/usr/bin/env python3
"""
Euru OS - Continuous Learning Engine

Scans closed paper trades and daily journals, computes performance metrics,
identifies patterns, compares Score Engine predictions vs results, and writes a
learning report.

Designed to be tolerant of Markdown variations. It supports:
- key/value lines, e.g. "Symbol: BTCUSDT"
- Markdown tables, e.g. "| Symbol | BTCUSDT |"
- bullet-style fields, e.g. "- P&L: +12.4%"

Default repo layout (relative to script location):
- 08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_*.md
- 08_DADOS_E_JOURNAL/JOURNALS/JOURNAL_*.md (or recursive JOURNAL_*.md fallback)
- 08_DADOS_E_JOURNAL/SCORECARDS/

Usage:
    python euru_learning_engine.py
    python euru_learning_engine.py --root C:\\path\\to\\Euru_TOS
    python euru_learning_engine.py --dry-run
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


# -----------------------------
# Data models
# -----------------------------

@dataclass
class TradeRecord:
    file_name: str
    trade_id: str = ""
    status: str = ""
    symbol: str = "UNKNOWN"
    entry_price: Optional[float] = None
    exit_price: Optional[float] = None
    pnl: Optional[float] = None               # normalized numeric value when possible
    pnl_text: str = ""
    pnl_pct: Optional[float] = None
    rr_achieved: Optional[float] = None
    exit_reason: str = "UNKNOWN"
    score_at_entry: Optional[float] = None
    mac_state: str = "UNKNOWN"
    risk_state: str = "UNKNOWN"
    news_severity: str = "UNKNOWN"
    setup_type: str = "UNKNOWN"
    days_held: Optional[float] = None
    direction: str = "UNKNOWN"
    asset_classification: str = "UNKNOWN"
    notes: List[str] = field(default_factory=list)

    @property
    def is_win(self) -> Optional[bool]:
        if self.pnl is not None:
            return self.pnl > 0
        if self.rr_achieved is not None:
            return self.rr_achieved > 0
        return None


@dataclass
class JournalObservation:
    file_name: str
    date: Optional[str] = None
    observations: List[str] = field(default_factory=list)
    lessons: List[str] = field(default_factory=list)
    raw_excerpt: str = ""


@dataclass
class PerformanceMetrics:
    total_closed_trades: int = 0
    wins: int = 0
    losses: int = 0
    win_rate: float = 0.0
    avg_rr: Optional[float] = None
    expectancy: Optional[float] = None
    avg_win: Optional[float] = None
    avg_loss: Optional[float] = None
    avg_score_winners: Optional[float] = None
    avg_score_losers: Optional[float] = None
    best_setup_types: List[Tuple[str, float, int]] = field(default_factory=list)
    worst_setup_types: List[Tuple[str, float, int]] = field(default_factory=list)
    best_assets: List[Tuple[str, float, int]] = field(default_factory=list)
    worst_assets: List[Tuple[str, float, int]] = field(default_factory=list)


@dataclass
class LearningSuggestion:
    governance_type: str   # Type 1 / Type 2 / Type 3
    area: str
    recommendation: str
    reason: str
    severity: str = "MEDIUM"


# -----------------------------
# Parsing helpers
# -----------------------------

FIELD_ALIASES: Dict[str, Sequence[str]] = {
    "trade_id": ["trade id", "paper trade id", "id", "pt id"],
    "status": ["status", "trade status", "result status"],
    "symbol": ["symbol", "asset", "pair", "coin", "ticker"],
    "entry_price": ["entry price", "entry", "entry value", "buy price", "sell price"],
    "exit_price": ["exit price", "exit", "close price", "target exit", "close value"],
    "pnl": ["p&l", "pnl", "profit and loss", "resultado", "resultado final"],
    "rr_achieved": ["r/r achieved", "rr achieved", "rr", "r:r", "risk reward", "risk/reward", "rr result"],
    "exit_reason": ["exit reason", "reason for exit", "close reason", "motivo da saída", "motivo da saida"],
    "score_at_entry": ["score at entry", "entry score", "score engine", "score", "score engine at entry"],
    "mac_state": ["mac state", "market state", "mac regime", "mac"],
    "risk_state": ["risk state", "risk", "risk regime", "risk level"],
    "news_severity": ["news severity", "news", "news impact", "severity", "news risk"],
    "setup_type": ["setup type", "setup", "entry setup", "playbook setup"],
    "days_held": ["days held", "holding days", "duration days", "days in trade", "held for"],
    "direction": ["direction", "side", "bias", "long/short"],
}

OBSERVATION_HEADERS = [
    "daily observations", "observations", "notas do dia", "daily notes", "market observations"
]
LESSON_HEADERS = [
    "lessons learned", "lessons", "lições", "licoes", "insights", "aprendizados"
]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.strip().lower()).strip()


def parse_number(value: str) -> Optional[float]:
    if value is None:
        return None
    text = value.strip()
    if not text:
        return None
    text = text.replace("\u2212", "-")
    text = text.replace(" ", "")
    # Keep percentage marker separate
    is_percent = "%" in text
    text = text.replace("%", "")
    # Brazilian/European decimal handling
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")

    # Extract first signed number
    m = re.search(r"[-+]?\d*\.?\d+(?:e[-+]?\d+)?", text, re.IGNORECASE)
    if not m:
        return None
    try:
        num = float(m.group(0))
    except ValueError:
        return None
    return num if not is_percent else num


def parse_rr(value: str) -> Optional[float]:
    if not value:
        return None
    text = value.strip().lower().replace(" ", "")
    # Match 1:2 or 2/1 etc.
    m = re.match(r"([-+]?\d*\.?\d+)[:/]([-+]?\d*\.?\d+)", text)
    if m:
        left = float(m.group(1))
        right = float(m.group(2))
        if left == 0:
            return None
        return right / left
    num = parse_number(value)
    return num


def canonical_field(label: str) -> Optional[str]:
    s = slug(label)
    for canonical, aliases in FIELD_ALIASES.items():
        if s == canonical:
            return canonical
        for alias in aliases:
            if s == slug(alias):
                return canonical
    return None


def extract_key_values(text: str) -> Dict[str, str]:
    values: Dict[str, str] = {}
    lines = text.splitlines()

    # 1) Plain key: value / bullet key: value
    for raw in lines:
        line = raw.strip().strip("-*• ")
        if ":" in line:
            left, right = line.split(":", 1)
            cf = canonical_field(left)
            if cf and right.strip():
                values.setdefault(cf, right.strip())

    # 2) Two-column markdown table rows: | key | value |
    for raw in lines:
        line = raw.strip()
        if line.startswith("|") and line.endswith("|"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 2:
                cf = canonical_field(parts[0])
                if cf and parts[1] and not re.fullmatch(r"[-: ]+", parts[1]):
                    values.setdefault(cf, parts[1])

    # 3) Headings followed by value on next line
    for i, raw in enumerate(lines[:-1]):
        header = raw.strip().strip("# ")
        cf = canonical_field(header)
        if cf:
            nxt = lines[i + 1].strip().strip("-*• ")
            if nxt and not nxt.startswith("#"):
                values.setdefault(cf, nxt)

    return values


def is_closed_trade(values: Dict[str, str], text: str) -> bool:
    status = values.get("status", "").lower()
    if any(word in status for word in ["closed", "encerr", "fechado", "done", "completed"]):
        return True
    if "exit price" in text.lower() or values.get("exit_price"):
        # Heuristic: if there is an exit and a pnl, likely closed.
        return bool(values.get("pnl") or values.get("rr_achieved") or values.get("exit_reason"))
    return False


def parse_trade_file(path: Path) -> Optional[TradeRecord]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    values = extract_key_values(text)
    if not is_closed_trade(values, text):
        return None

    trade = TradeRecord(file_name=path.name)
    trade.trade_id = values.get("trade_id") or re.search(r"PT\d+", path.stem, re.IGNORECASE).group(0) if re.search(r"PT\d+", path.stem, re.IGNORECASE) else path.stem
    trade.status = values.get("status", "CLOSED")
    trade.symbol = values.get("symbol", trade.symbol).upper().replace("/", "").replace(" ", "")
    trade.entry_price = parse_number(values.get("entry_price", ""))
    trade.exit_price = parse_number(values.get("exit_price", ""))
    trade.pnl_text = values.get("pnl", "")
    trade.pnl = parse_number(values.get("pnl", ""))
    if trade.pnl_text and "%" in trade.pnl_text:
        trade.pnl_pct = trade.pnl
    trade.rr_achieved = parse_rr(values.get("rr_achieved", ""))
    trade.exit_reason = values.get("exit_reason", trade.exit_reason)
    trade.score_at_entry = parse_number(values.get("score_at_entry", ""))
    trade.mac_state = values.get("mac_state", trade.mac_state)
    trade.risk_state = values.get("risk_state", trade.risk_state)
    trade.news_severity = values.get("news_severity", trade.news_severity)
    trade.setup_type = values.get("setup_type", trade.setup_type)
    trade.days_held = parse_number(values.get("days_held", ""))
    trade.direction = values.get("direction", trade.direction).upper()
    if trade.symbol.endswith("USDT"):
        trade.asset_classification = "USDT_PERP"

    # Add lightweight note for missing critical fields
    for field_name in [
        "symbol", "entry_price", "exit_price", "pnl", "rr_achieved", "score_at_entry",
        "mac_state", "risk_state", "news_severity", "setup_type", "days_held"
    ]:
        if getattr(trade, field_name) in [None, "", "UNKNOWN"]:
            trade.notes.append(f"Missing/unclear {field_name} in {path.name}")

    return trade


def find_section(text: str, headers: Sequence[str]) -> List[str]:
    lines = text.splitlines()
    idx = None
    for i, raw in enumerate(lines):
        normalized = slug(raw.strip("# "))
        if any(normalized == slug(h) for h in headers):
            idx = i
            break
    if idx is None:
        return []

    collected: List[str] = []
    for raw in lines[idx + 1:]:
        stripped = raw.strip()
        if stripped.startswith("#") and collected:
            break
        if stripped:
            collected.append(stripped.strip("-*• "))
    return collected


def parse_journal_file(path: Path) -> JournalObservation:
    text = path.read_text(encoding="utf-8", errors="ignore")
    date_match = re.search(r"(20\d{2}-\d{2}-\d{2})", path.name + "\n" + text)
    obs = JournalObservation(file_name=path.name, date=date_match.group(1) if date_match else None)
    obs.observations = find_section(text, OBSERVATION_HEADERS)
    obs.lessons = find_section(text, LESSON_HEADERS)
    if not obs.observations and not obs.lessons:
        # fallback: take first non-empty lines excluding title
        lines = [ln.strip().strip("-*• ") for ln in text.splitlines() if ln.strip()]
        obs.raw_excerpt = " ".join(lines[:8])[:600]
    return obs


# -----------------------------
# Analytics helpers
# -----------------------------


def mean_or_none(values: Sequence[float]) -> Optional[float]:
    vals = [v for v in values if v is not None]
    return statistics.mean(vals) if vals else None


def safe_win_rate(wins: int, total: int) -> float:
    return (wins / total) if total else 0.0


def normalize_outcome_value(trade: TradeRecord) -> Optional[float]:
    # Prefer RR when available since it is normalized by risk.
    if trade.rr_achieved is not None:
        return trade.rr_achieved
    return trade.pnl


def summarize_group_performance(trades: Sequence[TradeRecord], key_fn) -> List[Tuple[str, float, int]]:
    groups: Dict[str, List[TradeRecord]] = defaultdict(list)
    for tr in trades:
        groups[key_fn(tr)].append(tr)
    ranked: List[Tuple[str, float, int]] = []
    for key, group in groups.items():
        vals = [normalize_outcome_value(t) for t in group if normalize_outcome_value(t) is not None]
        if not vals:
            continue
        ranked.append((key, float(statistics.mean(vals)), len(group)))
    ranked.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return ranked


def compute_metrics(trades: Sequence[TradeRecord]) -> PerformanceMetrics:
    metrics = PerformanceMetrics(total_closed_trades=len(trades))
    outcomes = [normalize_outcome_value(t) for t in trades if normalize_outcome_value(t) is not None]
    wins = [v for v in outcomes if v > 0]
    losses = [v for v in outcomes if v <= 0]
    metrics.wins = len(wins)
    metrics.losses = len(losses)
    metrics.win_rate = safe_win_rate(metrics.wins, metrics.total_closed_trades)
    metrics.avg_rr = mean_or_none([t.rr_achieved for t in trades if t.rr_achieved is not None])
    metrics.avg_win = mean_or_none(wins)
    metrics.avg_loss = abs(mean_or_none(losses)) if losses else None
    if metrics.avg_win is not None and metrics.avg_loss is not None:
        loss_rate = 1.0 - metrics.win_rate
        metrics.expectancy = metrics.win_rate * metrics.avg_win - loss_rate * metrics.avg_loss
    metrics.avg_score_winners = mean_or_none([t.score_at_entry for t in trades if t.is_win and t.score_at_entry is not None])
    metrics.avg_score_losers = mean_or_none([t.score_at_entry for t in trades if t.is_win is False and t.score_at_entry is not None])

    setups = summarize_group_performance(trades, lambda t: t.setup_type or "UNKNOWN")
    assets = summarize_group_performance(trades, lambda t: t.symbol or "UNKNOWN")
    metrics.best_setup_types = setups[:5]
    metrics.worst_setup_types = list(reversed(setups[-5:])) if setups else []
    metrics.best_assets = assets[:5]
    metrics.worst_assets = list(reversed(assets[-5:])) if assets else []
    return metrics


def score_bands(score: Optional[float]) -> str:
    if score is None:
        return "UNKNOWN"
    if score >= 85:
        return "85-100"
    if score >= 70:
        return "70-84"
    if score >= 55:
        return "55-69"
    return "0-54"


def compare_predictions(trades: Sequence[TradeRecord]) -> Dict[str, Any]:
    by_asset: Dict[str, Dict[str, Any]] = defaultdict(lambda: {"correct": 0, "total": 0})
    by_setup: Dict[str, Dict[str, Any]] = defaultdict(lambda: {"correct": 0, "total": 0})

    # Simple proxy: treat score >= 70 as a "predicted winner" and below 70 as lower quality.
    # Accuracy = score prediction aligned with actual outcome.
    for tr in trades:
        if tr.score_at_entry is None or tr.is_win is None:
            continue
        predicted_win = tr.score_at_entry >= 70
        actual_win = tr.is_win
        correct = predicted_win == actual_win
        by_asset[tr.symbol]["total"] += 1
        by_asset[tr.symbol]["correct"] += int(correct)
        by_setup[tr.setup_type]["total"] += 1
        by_setup[tr.setup_type]["correct"] += int(correct)

    def finalize(d: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        rows = []
        for k, v in d.items():
            if v["total"] == 0:
                continue
            rows.append({
                "name": k,
                "accuracy": v["correct"] / v["total"],
                "correct": v["correct"],
                "total": v["total"],
            })
        rows.sort(key=lambda x: (x["accuracy"], x["total"]), reverse=True)
        return rows

    return {
        "by_asset": finalize(by_asset),
        "by_setup": finalize(by_setup),
    }


def identify_patterns(trades: Sequence[TradeRecord]) -> Dict[str, Any]:
    patterns: Dict[str, Any] = {}

    # Score Engine values/bands that predicted winners
    band_counter = defaultdict(lambda: {"wins": 0, "total": 0})
    for tr in trades:
        band = score_bands(tr.score_at_entry)
        if band == "UNKNOWN":
            continue
        band_counter[band]["total"] += 1
        band_counter[band]["wins"] += int(bool(tr.is_win))
    score_band_summary = []
    for band, stats in band_counter.items():
        total = stats["total"]
        win_rate = stats["wins"] / total if total else 0.0
        score_band_summary.append({"band": band, "win_rate": win_rate, "sample": total})
    score_band_summary.sort(key=lambda x: (x["win_rate"], x["sample"]), reverse=True)
    patterns["score_bands"] = score_band_summary

    # Setup win rates
    setup_stats = defaultdict(lambda: {"wins": 0, "total": 0})
    for tr in trades:
        setup_stats[tr.setup_type]["total"] += 1
        setup_stats[tr.setup_type]["wins"] += int(bool(tr.is_win))
    setups = []
    for setup, stats in setup_stats.items():
        total = stats["total"]
        setups.append({"setup": setup, "win_rate": stats["wins"] / total if total else 0.0, "sample": total})
    setups.sort(key=lambda x: (x["win_rate"], x["sample"]), reverse=True)
    patterns["setup_win_rates"] = setups

    # News severity blocking quality
    news_stats = defaultdict(lambda: {"wins": 0, "losses": 0, "total": 0})
    for tr in trades:
        sev = tr.news_severity or "UNKNOWN"
        news_stats[sev]["total"] += 1
        if tr.is_win:
            news_stats[sev]["wins"] += 1
        elif tr.is_win is False:
            news_stats[sev]["losses"] += 1
    news_summary = []
    for sev, stats in news_stats.items():
        total = stats["total"]
        loss_rate = stats["losses"] / total if total else 0.0
        news_summary.append({"severity": sev, "loss_rate": loss_rate, "sample": total})
    news_summary.sort(key=lambda x: (x["loss_rate"], x["sample"]), reverse=True)
    patterns["news_severity_effect"] = news_summary

    # Repeated failures by asset
    asset_failures = defaultdict(lambda: {"losses": 0, "total": 0})
    for tr in trades:
        asset_failures[tr.symbol]["total"] += 1
        if tr.is_win is False:
            asset_failures[tr.symbol]["losses"] += 1
    asset_failure_summary = []
    for asset, stats in asset_failures.items():
        total = stats["total"]
        loss_rate = stats["losses"] / total if total else 0.0
        asset_failure_summary.append({"asset": asset, "loss_rate": loss_rate, "sample": total})
    asset_failure_summary.sort(key=lambda x: (x["loss_rate"], x["sample"]), reverse=True)
    patterns["repeated_asset_failures"] = asset_failure_summary

    return patterns


def build_suggestions(trades: Sequence[TradeRecord], metrics: PerformanceMetrics, patterns: Dict[str, Any]) -> List[LearningSuggestion]:
    suggestions: List[LearningSuggestion] = []

    # Type 1: immediate adjustments
    if metrics.win_rate < 0.5:
        suggestions.append(LearningSuggestion(
            governance_type="Type 1",
            area="Thresholds",
            recommendation="Raise the minimum Score Engine threshold for new entries in SIMULATE until win rate improves.",
            reason=f"Current win rate is {metrics.win_rate:.1%}, below the 50% SIMULATE readiness threshold.",
            severity="HIGH",
        ))
    if metrics.avg_score_winners is not None and metrics.avg_score_losers is not None and metrics.avg_score_winners <= metrics.avg_score_losers:
        suggestions.append(LearningSuggestion(
            governance_type="Type 1",
            area="Score Engine",
            recommendation="Recalibrate score weighting immediately; winners are not scoring higher than losers.",
            reason=f"Avg winner score={metrics.avg_score_winners:.2f}, avg loser score={metrics.avg_score_losers:.2f}.",
            severity="HIGH",
        ))

    # Type 1 from asset failures
    repeated_failures = [x for x in patterns.get("repeated_asset_failures", []) if x["sample"] >= 2 and x["loss_rate"] >= 0.7]
    for row in repeated_failures[:3]:
        suggestions.append(LearningSuggestion(
            governance_type="Type 1",
            area="Watchlist",
            recommendation=f"Temporarily downgrade or remove {row['asset']} from the active watchlist.",
            reason=f"{row['asset']} shows repeated failure: loss rate {row['loss_rate']:.1%} over {row['sample']} closed trades.",
            severity="MEDIUM",
        ))

    # Type 2: 24h review
    bad_setups = [x for x in patterns.get("setup_win_rates", []) if x["sample"] >= 2 and x["win_rate"] < 0.4]
    for row in bad_setups[:3]:
        suggestions.append(LearningSuggestion(
            governance_type="Type 2",
            area="Checklist / Setup Governance",
            recommendation=f"Review setup '{row['setup']}' within 24h and add checklist rules or disqualifiers before allowing new trades.",
            reason=f"Win rate for setup '{row['setup']}' is only {row['win_rate']:.1%} across {row['sample']} trades.",
            severity="MEDIUM",
        ))

    # Type 3: strategic
    if metrics.expectancy is not None and metrics.expectancy <= 0:
        suggestions.append(LearningSuggestion(
            governance_type="Type 3",
            area="Strategy Calibration",
            recommendation="Run a 48h strategic review on the full SIMULATE playbook, including risk budget, setup taxonomy, and score weights.",
            reason=f"Expectancy is non-positive ({metrics.expectancy:.3f}), indicating the current process is not compounding edge.",
            severity="HIGH",
        ))

    # News severity patterns
    news_bad = [x for x in patterns.get("news_severity_effect", []) if x["sample"] >= 2 and x["loss_rate"] >= 0.6]
    for row in news_bad[:2]:
        suggestions.append(LearningSuggestion(
            governance_type="Type 2",
            area="News Guardrails",
            recommendation=f"Tighten or enforce trade blocking rules when news severity is '{row['severity']}'.",
            reason=f"Trades with news severity '{row['severity']}' show {row['loss_rate']:.1%} loss rate over {row['sample']} trades.",
            severity="MEDIUM",
        ))

    # Keep deterministic order: Type 1, Type 2, Type 3
    type_order = {"Type 1": 1, "Type 2": 2, "Type 3": 3}
    suggestions.sort(key=lambda s: (type_order.get(s.governance_type, 99), s.area, s.recommendation))
    return suggestions


def readiness_check(trades: Sequence[TradeRecord], metrics: PerformanceMetrics) -> Dict[str, Any]:
    total = len(trades)
    rr_ok = (metrics.avg_rr is not None and metrics.avg_rr >= 2.0)
    win_ok = metrics.win_rate >= 0.5
    expectancy_ok = metrics.expectancy is not None and metrics.expectancy > 0
    enough_sample = total >= 20
    ready = enough_sample and win_ok and rr_ok and expectancy_ok
    return {
        "sample_size": total,
        "enough_sample": enough_sample,
        "win_rate_ok": win_ok,
        "rr_ok": rr_ok,
        "expectancy_ok": expectancy_ok,
        "suggestion": "SUGGEST EXECUTE PHASE" if ready else "CONTINUE SIMULATE",
        "details": {
            "win_rate": metrics.win_rate,
            "avg_rr": metrics.avg_rr,
            "expectancy": metrics.expectancy,
        },
    }


def format_pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value:.1%}"


def format_num(value: Optional[float], digits: int = 2) -> str:
    return "n/a" if value is None else f"{value:.{digits}f}"


def markdown_table(rows: Sequence[Sequence[Any]], headers: Sequence[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def generate_report(
    trades: Sequence[TradeRecord],
    journals: Sequence[JournalObservation],
    metrics: PerformanceMetrics,
    patterns: Dict[str, Any],
    prediction_accuracy: Dict[str, Any],
    suggestions: Sequence[LearningSuggestion],
    readiness: Dict[str, Any],
    output_path: Path,
) -> None:
    today = dt.date.today().isoformat()

    watchlist_alerts = [
        x for x in patterns.get("repeated_asset_failures", [])
        if x["sample"] >= 2 and x["loss_rate"] >= 0.7
    ]
    pending_human = [s for s in suggestions if s.governance_type in {"Type 2", "Type 3"}]

    setup_rows_best = [(n, format_num(avg, 2), sample) for n, avg, sample in metrics.best_setup_types]
    setup_rows_worst = [(n, format_num(avg, 2), sample) for n, avg, sample in metrics.worst_setup_types]
    asset_rows_best = [(n, format_num(avg, 2), sample) for n, avg, sample in metrics.best_assets]
    asset_rows_worst = [(n, format_num(avg, 2), sample) for n, avg, sample in metrics.worst_assets]
    pred_asset_rows = [(r["name"], format_pct(r["accuracy"]), r["correct"], r["total"]) for r in prediction_accuracy["by_asset"][:10]]
    pred_setup_rows = [(r["name"], format_pct(r["accuracy"]), r["correct"], r["total"]) for r in prediction_accuracy["by_setup"][:10]]

    lines: List[str] = []
    lines.append(f"# LEARNING_REPORT_{today}")
    lines.append("")
    lines.append(f"Generated on: **{today}**")
    lines.append("")
    lines.append("## 1. Performance Summary")
    lines.append("")
    lines.append(markdown_table([
        ["Closed trades", metrics.total_closed_trades],
        ["Wins", metrics.wins],
        ["Losses", metrics.losses],
        ["Win rate", format_pct(metrics.win_rate)],
        ["Average R/R", format_num(metrics.avg_rr, 2)],
        ["Average win", format_num(metrics.avg_win, 2)],
        ["Average loss", format_num(metrics.avg_loss, 2)],
        ["Expectancy", format_num(metrics.expectancy, 3)],
        ["Avg score of winners", format_num(metrics.avg_score_winners, 2)],
        ["Avg score of losers", format_num(metrics.avg_score_losers, 2)],
    ], ["Metric", "Value"]))
    lines.append("")

    lines.append("## 2. Best / Worst Setups and Assets")
    lines.append("")
    if setup_rows_best:
        lines.append("### Best setup types")
        lines.append(markdown_table(setup_rows_best, ["Setup", "Avg outcome", "Trades"]))
        lines.append("")
    if setup_rows_worst:
        lines.append("### Worst setup types")
        lines.append(markdown_table(setup_rows_worst, ["Setup", "Avg outcome", "Trades"]))
        lines.append("")
    if asset_rows_best:
        lines.append("### Best assets")
        lines.append(markdown_table(asset_rows_best, ["Asset", "Avg outcome", "Trades"]))
        lines.append("")
    if asset_rows_worst:
        lines.append("### Worst assets")
        lines.append(markdown_table(asset_rows_worst, ["Asset", "Avg outcome", "Trades"]))
        lines.append("")

    lines.append("## 3. Patterns Identified")
    lines.append("")
    score_band_rows = [(r["band"], format_pct(r["win_rate"]), r["sample"]) for r in patterns.get("score_bands", [])]
    if score_band_rows:
        lines.append("### Score Engine bands vs winners")
        lines.append(markdown_table(score_band_rows, ["Score band", "Win rate", "Sample"]))
        lines.append("")
    setup_rate_rows = [(r["setup"], format_pct(r["win_rate"]), r["sample"]) for r in patterns.get("setup_win_rates", [])]
    if setup_rate_rows:
        lines.append("### Setup win rates")
        lines.append(markdown_table(setup_rate_rows, ["Setup", "Win rate", "Sample"]))
        lines.append("")
    news_rows = [(r["severity"], format_pct(r["loss_rate"]), r["sample"]) for r in patterns.get("news_severity_effect", [])]
    if news_rows:
        lines.append("### News severity effect")
        lines.append(markdown_table(news_rows, ["News severity", "Loss rate", "Sample"]))
        lines.append("")
    asset_fail_rows = [(r["asset"], format_pct(r["loss_rate"]), r["sample"]) for r in patterns.get("repeated_asset_failures", [])]
    if asset_fail_rows:
        lines.append("### Repeated asset failures")
        lines.append(markdown_table(asset_fail_rows, ["Asset", "Loss rate", "Sample"]))
        lines.append("")

    lines.append("## 4. Score Engine Prediction Accuracy")
    lines.append("")
    if pred_asset_rows:
        lines.append("### Per asset")
        lines.append(markdown_table(pred_asset_rows, ["Asset", "Accuracy", "Correct", "Total"]))
        lines.append("")
    if pred_setup_rows:
        lines.append("### Per setup type")
        lines.append(markdown_table(pred_setup_rows, ["Setup", "Accuracy", "Correct", "Total"]))
        lines.append("")

    lines.append("## 5. Agent Deviation Analysis")
    lines.append("")
    deviations = [note for tr in trades for note in tr.notes]
    if deviations:
        for note in deviations[:20]:
            lines.append(f"- {note}")
    else:
        lines.append("- No major field extraction deviations detected.")
    lines.append("")

    lines.append("## 6. Watchlist Alerts")
    lines.append("")
    if watchlist_alerts:
        for alert in watchlist_alerts:
            lines.append(f"- **{alert['asset']}**: repeated failure pattern ({format_pct(alert['loss_rate'])} loss rate across {alert['sample']} trades).")
    else:
        lines.append("- No watchlist alerts triggered this cycle.")
    lines.append("")

    lines.append("## 7. Governance Suggestions")
    lines.append("")
    if suggestions:
        for s in suggestions:
            lines.append(f"- **{s.governance_type} | {s.area} | {s.severity}** — {s.recommendation}  ")
            lines.append(f"  Reason: {s.reason}")
    else:
        lines.append("- No governance suggestions generated.")
    lines.append("")

    lines.append("## 8. Pending Decisions for Human Approval")
    lines.append("")
    if pending_human:
        for s in pending_human:
            lines.append(f"- **{s.governance_type}** — {s.recommendation}")
    else:
        lines.append("- No pending strategic or 24h decisions.")
    lines.append("")

    lines.append("## 9. Journal Observations and Lessons")
    lines.append("")
    if journals:
        for j in journals[:10]:
            label = j.date or j.file_name
            lines.append(f"### {label}")
            if j.observations:
                for item in j.observations[:6]:
                    lines.append(f"- Observation: {item}")
            if j.lessons:
                for item in j.lessons[:6]:
                    lines.append(f"- Lesson: {item}")
            if j.raw_excerpt:
                lines.append(f"- Excerpt: {j.raw_excerpt}")
            lines.append("")
    else:
        lines.append("- No journal files found.")
        lines.append("")

    lines.append("## 10. SIMULATE Readiness Check")
    lines.append("")
    lines.append(markdown_table([
        ["Closed trade sample >= 20", readiness["enough_sample"]],
        ["Win rate >= 50%", readiness["win_rate_ok"]],
        ["Average R/R >= 1:2", readiness["rr_ok"]],
        ["Expectancy > 0", readiness["expectancy_ok"]],
        ["Recommendation", readiness["suggestion"]],
    ], ["Check", "Result"]))
    lines.append("")
    if readiness["suggestion"] == "SUGGEST EXECUTE PHASE":
        lines.append("System signal: **SIMULATE appears ready to graduate toward EXECUTE**, subject to human approval and governance review.")
    else:
        lines.append("System signal: **Continue SIMULATE** and apply the listed improvements before considering EXECUTE.")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


# -----------------------------
# Discovery helpers
# -----------------------------


def discover_trade_files(root: Path) -> List[Path]:
    primary = root / "08_DADOS_E_JOURNAL" / "JOURNAL_TRADES"
    if primary.exists():
        files = sorted(primary.glob("PAPER_TRADE_*.md"))
        if files:
            return files
    return sorted(root.rglob("PAPER_TRADE_*.md"))


def discover_journal_files(root: Path) -> List[Path]:
    preferred = [
        root / "08_DADOS_E_JOURNAL" / "JOURNALS",
        root / "08_DADOS_E_JOURNAL",
    ]
    collected: List[Path] = []
    for base in preferred:
        if base.exists():
            collected.extend(sorted(base.rglob("JOURNAL_*.md")))
    if collected:
        # de-duplicate while keeping order
        seen = set()
        unique = []
        for p in collected:
            if p not in seen:
                unique.append(p)
                seen.add(p)
        return unique
    return sorted(root.rglob("JOURNAL_*.md"))


# -----------------------------
# Main
# -----------------------------


def run(root: Path, dry_run: bool = False, verbose: bool = False) -> Dict[str, Any]:
    trade_files = discover_trade_files(root)
    journal_files = discover_journal_files(root)

    trades: List[TradeRecord] = []
    skipped: List[str] = []
    for f in trade_files:
        try:
            record = parse_trade_file(f)
            if record is None:
                skipped.append(f.name)
            else:
                trades.append(record)
        except Exception as exc:
            skipped.append(f"{f.name} (parse error: {exc})")

    journals: List[JournalObservation] = []
    for f in journal_files:
        try:
            journals.append(parse_journal_file(f))
        except Exception:
            continue

    metrics = compute_metrics(trades)
    patterns = identify_patterns(trades)
    prediction_accuracy = compare_predictions(trades)
    suggestions = build_suggestions(trades, metrics, patterns)
    readiness = readiness_check(trades, metrics)

    today = dt.date.today().isoformat()
    report_path = root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / f"LEARNING_REPORT_{today}.md"
    if not dry_run:
        generate_report(
            trades=trades,
            journals=journals,
            metrics=metrics,
            patterns=patterns,
            prediction_accuracy=prediction_accuracy,
            suggestions=suggestions,
            readiness=readiness,
            output_path=report_path,
        )

    result = {
        "root": str(root),
        "trade_files_found": len(trade_files),
        "closed_trades_parsed": len(trades),
        "trade_files_skipped": skipped,
        "journal_files_found": len(journal_files),
        "metrics": asdict(metrics),
        "patterns": patterns,
        "prediction_accuracy": prediction_accuracy,
        "suggestions": [asdict(s) for s in suggestions],
        "readiness": readiness,
        "report_path": str(report_path),
        "test_targets": {
            "PT001_detected": any("PT001" in t.trade_id.upper() or "PT001" in t.file_name.upper() for t in trades),
            "PT002_detected": any("PT002" in t.trade_id.upper() or "PT002" in t.file_name.upper() for t in trades),
            "PT003_detected": any("PT003" in t.trade_id.upper() or "PT003" in t.file_name.upper() for t in trades),
        },
    }

    if verbose:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Euru continuous learning engine")
    parser.add_argument("--root", type=str, default=None, help="Path to Euru_TOS root. Defaults to this script's parent directory.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write report file.")
    parser.add_argument("--verbose", action="store_true", help="Print JSON summary.")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    script_root = Path(__file__).resolve().parent
    root = Path(args.root).resolve() if args.root else script_root
    run(root=root, dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    main()

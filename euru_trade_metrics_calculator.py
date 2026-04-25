#!/usr/bin/env python3
"""
Euru OS - Trade Metrics Calculator

Read-only calculator for closed PAPER_TRADE files. It does not modify trade
records. It writes a metrics report under 08_DADOS_E_JOURNAL/METRICS.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required. Install with: pip install pyyaml") from exc

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
EXCLUSION_TAGS = {"governance_breach", "rule_8_violation_closed", "excluded_from_stats"}


@dataclass
class TradeMetrics:
    file: str
    trade_id: str
    symbol: str
    status: str
    side: str
    setup_type: str
    entry_datetime: str
    exit_datetime: Optional[str]
    entry_score: Optional[float]
    news_severity_at_entry: str
    exit_reason: Optional[str]
    pnl_usdt: Optional[float]
    rr_achieved: Optional[float]
    days_held: Optional[float]
    tags: List[str]
    included_in_official_stats: bool
    exclusion_reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate Euru trade metrics from PAPER_TRADE files.")
    parser.add_argument("--root", default=".", help="Path to Euru root")
    parser.add_argument("--json", action="store_true", help="Print JSON summary")
    parser.add_argument("--no-write", action="store_true", help="Do not write markdown report")
    return parser.parse_args()


def load_front_matter(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError(f"Missing YAML front matter: {path}")
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML front matter is not a mapping: {path}")
    return data


def as_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def parse_trade(path: Path, root: Path) -> TradeMetrics:
    fm = load_front_matter(path)
    tags = [str(t) for t in (fm.get("tags") or [])]
    tag_set = {t.lower() for t in tags}
    status = str(fm.get("status", "")).lower()
    schema_type = str(fm.get("schema_type", "")).lower()

    exclusion_reason = ""
    included = True
    if schema_type != "paper_trade":
        included = False
        exclusion_reason = "not_paper_trade"
    elif status != "closed":
        included = False
        exclusion_reason = "not_closed"
    elif tag_set.intersection(EXCLUSION_TAGS):
        included = False
        exclusion_reason = "governance_breach_or_excluded_tag"
    elif str(fm.get("news_severity_at_entry", "")).lower() in {"high", "critical"} and "governance_breach" in tag_set:
        included = False
        exclusion_reason = "high_news_governance_breach"

    return TradeMetrics(
        file=str(path.relative_to(root)),
        trade_id=str(fm.get("trade_id", path.stem)),
        symbol=str(fm.get("symbol", "unknown")),
        status=status,
        side=str(fm.get("side", "unknown")),
        setup_type=str(fm.get("setup_type", "unknown")),
        entry_datetime=str(fm.get("entry_datetime", "")),
        exit_datetime=str(fm.get("exit_datetime")) if fm.get("exit_datetime") is not None else None,
        entry_score=as_float(fm.get("entry_score")),
        news_severity_at_entry=str(fm.get("news_severity_at_entry", "unknown")),
        exit_reason=str(fm.get("exit_reason")) if fm.get("exit_reason") is not None else None,
        pnl_usdt=as_float(fm.get("pnl_usdt")),
        rr_achieved=as_float(fm.get("rr_achieved")),
        days_held=as_float(fm.get("days_held")),
        tags=tags,
        included_in_official_stats=included,
        exclusion_reason=exclusion_reason,
    )


def mean(values: Iterable[Optional[float]]) -> Optional[float]:
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def sum_values(values: Iterable[Optional[float]]) -> float:
    return sum(v for v in values if v is not None)


def pct(part: int, total: int) -> Optional[float]:
    if total == 0:
        return None
    return round((part / total) * 100.0, 2)


def summarize_group(trades: List[TradeMetrics]) -> Dict[str, Any]:
    wins = [t for t in trades if (t.pnl_usdt or 0) > 0]
    losses = [t for t in trades if (t.pnl_usdt or 0) < 0]
    return {
        "count": len(trades),
        "wins": len(wins),
        "losses": len(losses),
        "win_rate_pct": pct(len(wins), len(trades)),
        "total_pnl_usdt": round(sum_values(t.pnl_usdt for t in trades), 4),
        "average_rr": round(mean(t.rr_achieved for t in trades) or 0.0, 4),
        "average_win_rr": round(mean(t.rr_achieved for t in wins) or 0.0, 4),
        "average_loss_rr": round(mean(t.rr_achieved for t in losses) or 0.0, 4),
        "average_days_held": round(mean(t.days_held for t in trades) or 0.0, 2),
    }


def by_field(trades: List[TradeMetrics], field: str) -> Dict[str, Dict[str, Any]]:
    groups: Dict[str, List[TradeMetrics]] = defaultdict(list)
    for t in trades:
        groups[str(getattr(t, field) or "unknown")].append(t)
    return {k: summarize_group(v) for k, v in sorted(groups.items())}


def build_summary(trades: List[TradeMetrics]) -> Dict[str, Any]:
    official = [t for t in trades if t.included_in_official_stats]
    excluded = [t for t in trades if not t.included_in_official_stats]
    summary = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "total_trade_files": len(trades),
        "official_trades_count": len(official),
        "excluded_trades_count": len(excluded),
        "official": summarize_group(official),
        "all_closed_including_excluded": summarize_group([t for t in trades if t.status == "closed"]),
        "by_symbol": by_field(official, "symbol"),
        "by_setup_type": by_field(official, "setup_type"),
        "by_news_severity": by_field(official, "news_severity_at_entry"),
        "by_exit_reason": by_field(official, "exit_reason"),
        "trades": [asdict(t) for t in trades],
    }
    # Euru North Star currently measures monthly performance. This calculator
    # reports trade-level P&L only until official capital curve rules are finalized.
    summary["north_star_note"] = "Monthly 5-8% benchmark requires official capital curve definition."
    return summary


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def markdown_table_for_trades(trades: List[TradeMetrics]) -> List[str]:
    lines = [
        "| Trade | Symbol | Status | Included | P&L USDT | RR | Exit | Days | Exclusion |",
        "|---|---|---|---|---:|---:|---|---:|---|",
    ]
    for t in trades:
        lines.append(
            f"| {t.trade_id} | {t.symbol} | {t.status} | {'yes' if t.included_in_official_stats else 'no'} "
            f"| {fmt(t.pnl_usdt)} | {fmt(t.rr_achieved)} | {t.exit_reason or 'n/a'} | {fmt(t.days_held)} | {t.exclusion_reason or '-'} |"
        )
    return lines


def markdown_group_table(title: str, groups: Dict[str, Dict[str, Any]]) -> List[str]:
    lines = [f"## {title}", "", "| Group | Count | Win Rate | P&L USDT | Avg RR | Avg Days |", "|---|---:|---:|---:|---:|---:|"]
    if not groups:
        lines.append("| n/a | 0 | n/a | 0 | 0 | 0 |")
        return lines
    for key, s in groups.items():
        lines.append(
            f"| {key} | {s['count']} | {fmt(s['win_rate_pct'])} | {fmt(s['total_pnl_usdt'])} | {fmt(s['average_rr'])} | {fmt(s['average_days_held'])} |"
        )
    return lines


def build_markdown(summary: Dict[str, Any]) -> str:
    official = summary["official"]
    lines = [
        "---",
        "schema_type: trade_metrics_report",
        "schema_version: 1.0",
        f"report_date: '{date.today().isoformat()}'",
        "---",
        "",
        f"# Euru Trade Metrics Report — {date.today().isoformat()}",
        "",
        "## Executive Summary",
        "",
        f"- Total trade files: {summary['total_trade_files']}",
        f"- Official trades included: {summary['official_trades_count']}",
        f"- Trades excluded from official stats: {summary['excluded_trades_count']}",
        f"- Official P&L: {fmt(official['total_pnl_usdt'])} USDT",
        f"- Official win rate: {fmt(official['win_rate_pct'])}%",
        f"- Official average RR: {fmt(official['average_rr'])}R",
        f"- Average days held: {fmt(official['average_days_held'])}",
        "",
        "## North Star Note",
        "",
        summary["north_star_note"],
        "",
        "## Trade Table",
        "",
    ]
    trades = [TradeMetrics(**t) for t in summary["trades"]]
    lines.extend(markdown_table_for_trades(trades))
    lines.extend([""])
    for title, key in [
        ("By Symbol", "by_symbol"),
        ("By Setup Type", "by_setup_type"),
        ("By News Severity", "by_news_severity"),
        ("By Exit Reason", "by_exit_reason"),
    ]:
        lines.extend(markdown_group_table(title, summary[key]))
        lines.extend([""])
    lines.extend([
        "## Interpretation",
        "",
        "Current sample is too small for statistical confidence. PT004 is preserved as an incident record but excluded from official performance metrics due to governance breach tags.",
        "",
        "## Next Metric Improvements",
        "",
        "- Define official capital curve rules for monthly 5-8% benchmark.",
        "- Add fees, funding, and slippage assumptions.",
        "- Add max drawdown calculation once capital curve is canonical.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def write_report(root: Path, markdown: str) -> Path:
    out_dir = root / "08_DADOS_E_JOURNAL" / "METRICS"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"TRADE_METRICS_REPORT_{date.today().isoformat()}.md"
    out_path.write_text(markdown, encoding="utf-8", newline="\n")
    return out_path


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    trade_dir = root / "08_DADOS_E_JOURNAL" / "JOURNAL_TRADES"
    files = sorted(trade_dir.glob("PAPER_TRADE_*.md"))
    trades = [parse_trade(path, root) for path in files]
    summary = build_summary(trades)
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    markdown = build_markdown(summary)
    if not args.no_write:
        out = write_report(root, markdown)
        print(f"Trade metrics report written: {out}")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Dedicated multidimensional scorecard engine for EURU_TOS.

Generates schema-compliant SCORECARD files from the latest LEARNING_REPORT and
closed PAPER_TRADE files. Supports system, asset, setup, agent, and score_engine
scopes.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to run euru_scorecard_engine.py") from exc


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SUPPORTED_SCOPES = ["system", "asset", "setup", "agent", "score_engine"]
DEFAULT_MIN_SAMPLE = 2
DEFAULT_SCORE_ENGINE_ID = "score_engine_v1"
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

@dataclass
class TradeEnvelope:
    trade: Any
    path: Path
    front_matter: Dict[str, Any]
    entry_date: Optional[date]
    exit_date: Optional[date]
    agent_name: Optional[str]


@dataclass
class ThresholdContext:
    scope: str
    profile_id: str
    version: Optional[str]
    thresholds: Dict[str, Any]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")



def local_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")



def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path



def load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module



def resolve_script(root: Path, file_name: str) -> Path:
    candidate = root / file_name
    if candidate.exists():
        return candidate
    here_candidate = Path(__file__).resolve().parent / file_name
    if here_candidate.exists():
        return here_candidate
    return candidate



def week_ref_from_date(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"



def slugify(value: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower())
    return s.strip("_") or "unknown"



def parse_iso_date(value: Any) -> Optional[date]:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    if ISO_DATE_RE.match(text):
        try:
            return datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            return None
    # try datetime
    try:
        text = text.replace("Z", "+00:00")
        return datetime.fromisoformat(text).date()
    except ValueError:
        return None



def load_markdown_with_front_matter(path: Path) -> Tuple[Optional[Dict[str, Any]], str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None, text
    front_raw = parts[0][4:]
    body = parts[1]
    try:
        data = yaml.safe_load(front_raw) or {}
    except Exception:
        return None, body
    return data if isinstance(data, dict) else None, body



def write_markdown_with_front_matter(path: Path, front_matter: Dict[str, Any], body: str) -> Path:
    ensure_dir(path.parent)
    fm = yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True).strip()
    path.write_text(f"---\n{fm}\n---\n\n{body.strip()}\n", encoding="utf-8")
    return path



def markdown_bullets(lines: List[str], default: str = "- none") -> str:
    cleaned = [ln.rstrip() for ln in lines if str(ln).strip()]
    return "\n".join(cleaned) if cleaned else default



def mean(values: Iterable[Optional[float]]) -> Optional[float]:
    vals = [float(v) for v in values if v is not None]
    return round(sum(vals) / len(vals), 4) if vals else None



def metric_status(value: float, target: float, op: str) -> str:
    if op == ">=":
        return "pass" if value >= target else "breach"
    if op == ">":
        return "pass" if value > target else "breach"
    return "watch"



def compute_prediction_accuracy_pct(prediction_accuracy: Dict[str, Any]) -> float:
    correct = 0
    total = 0
    for bucket in prediction_accuracy.get("by_asset", []):
        correct += int(bucket.get("correct", 0))
        total += int(bucket.get("total", 0))
    return round((correct / total) * 100.0, 2) if total else 0.0



def find_latest_learning_report(root: Path) -> Optional[Path]:
    candidates: List[Path] = []
    official = root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / "LEARNING_REPORTS"
    fallback = root / "08_DADOS_E_JOURNAL" / "SCORECARDS"
    for base in [official, fallback]:
        if base.exists():
            candidates.extend(sorted(base.rglob("LEARNING_REPORT_*.md")))
    if not candidates:
        return None

    def sort_key(path: Path):
        data, _ = load_markdown_with_front_matter(path)
        report_date = parse_iso_date((data or {}).get("report_date"))
        return (report_date or date.min, path.stat().st_mtime)

    return sorted(set(candidates), key=sort_key, reverse=True)[0]



def load_learning_context(path: Optional[Path]) -> Dict[str, Any]:
    if path is None or not path.exists():
        today = date.today()
        return {
            "path": None,
            "data": {},
            "body": "",
            "period_start": today,
            "period_end": today,
            "period_ref": week_ref_from_date(today),
            "period_type": "weekly",
        }
    data, body = load_markdown_with_front_matter(path)
    data = data or {}
    period_end = parse_iso_date(data.get("period_end")) or parse_iso_date(data.get("report_date")) or date.today()
    period_start = parse_iso_date(data.get("period_start")) or period_end
    period_type = data.get("period_type") or "weekly"
    period_ref = data.get("period_ref")
    if not period_ref:
        period_ref = week_ref_from_date(period_end) if period_type == "weekly" else period_end.isoformat()
    return {
        "path": path,
        "data": data,
        "body": body,
        "period_start": period_start,
        "period_end": period_end,
        "period_ref": period_ref,
        "period_type": period_type,
    }



def load_trade_envelopes(root: Path, learning_mod, period_start: Optional[date], period_end: Optional[date]) -> List[TradeEnvelope]:
    envelopes: List[TradeEnvelope] = []
    for path in learning_mod.discover_trade_files(root):
        trade = learning_mod.parse_trade_file(path)
        if trade is None:
            continue
        front, _ = load_markdown_with_front_matter(path)
        front = front or {}
        entry_date = parse_iso_date(front.get("entry_datetime"))
        exit_date = parse_iso_date(front.get("exit_datetime"))
        agent_name = front.get("agent_name") or front.get("agent")

        include = True
        if period_start and period_end:
            if exit_date:
                include = period_start <= exit_date <= period_end
            elif entry_date:
                include = period_start <= entry_date <= period_end
        if include:
            envelopes.append(TradeEnvelope(trade=trade, path=path, front_matter=front, entry_date=entry_date, exit_date=exit_date, agent_name=agent_name))
    return envelopes



def default_thresholds(scope: str, min_sample: int) -> ThresholdContext:
    return ThresholdContext(
        scope=scope,
        profile_id="default",
        version=None,
        thresholds={
            "readiness": {
                "min_closed_trades": min_sample,
                "min_win_rate_pct": 50.0,
                "min_average_rr": 2.0,
                "min_expectancy": 0.01,
            },
            "score_engine": {
                "min_prediction_accuracy_pct": 60.0,
            },
        },
    )



def resolve_threshold_context(root: Path, scope: str, on_date: date, min_sample: int) -> ThresholdContext:
    registry_path = resolve_script(root, "euru_threshold_registry.py")
    if not registry_path.exists():
        return default_thresholds(scope, min_sample)
    try:
        registry = load_module(f"euru_threshold_registry_runtime_{scope}", registry_path)
        profiles = registry.discover_profiles(root)
        profile = registry.resolve_active_profile(profiles, scope, "default", on_date)
        if profile is None and scope != "system":
            profile = registry.resolve_active_profile(profiles, "system", "default", on_date)
        if profile is None:
            return default_thresholds(scope, min_sample)
        return ThresholdContext(
            scope=profile.scope or scope,
            profile_id=profile.profile_id or "default",
            version=profile.version,
            thresholds=profile.data.get("thresholds", {}) or {},
        )
    except Exception:
        return default_thresholds(scope, min_sample)



def thresholds_for_context(ctx: ThresholdContext, min_sample: int) -> Dict[str, float]:
    readiness = ctx.thresholds.get("readiness", {}) if isinstance(ctx.thresholds, dict) else {}
    score_engine = ctx.thresholds.get("score_engine", {}) if isinstance(ctx.thresholds, dict) else {}
    return {
        "min_closed_trades": float(readiness.get("min_closed_trades", min_sample)),
        "min_win_rate_pct": float(readiness.get("min_win_rate_pct", 50.0)),
        "min_average_rr": float(readiness.get("min_average_rr", 2.0)),
        "min_expectancy": float(readiness.get("min_expectancy", 0.01)),
        "min_prediction_accuracy_pct": float(score_engine.get("min_prediction_accuracy_pct", 60.0)),
    }



def group_envelopes(envelopes: Sequence[TradeEnvelope], key_func) -> Dict[str, List[TradeEnvelope]]:
    grouped: Dict[str, List[TradeEnvelope]] = {}
    for env in envelopes:
        key = key_func(env)
        if not key:
            continue
        grouped.setdefault(str(key), []).append(env)
    return grouped



def derive_decision(metrics: Dict[str, Any], thresholds: Dict[str, float], prediction_accuracy_pct: float) -> Tuple[str, str, str, int]:
    closed_trades = int(metrics.get("total_closed_trades", 0) or 0)
    win_rate_pct = round(float(metrics.get("win_rate", 0.0) or 0.0) * 100.0, 2)
    average_rr = round(float(metrics.get("avg_rr", 0.0) or 0.0), 2)
    expectancy = round(float(metrics.get("expectancy", 0.0) or 0.0), 4)

    breaches = 0
    breaches += int(closed_trades < thresholds["min_closed_trades"])
    breaches += int(win_rate_pct < thresholds["min_win_rate_pct"])
    breaches += int(average_rr < thresholds["min_average_rr"])
    breaches += int(expectancy < thresholds["min_expectancy"])
    breaches += int(prediction_accuracy_pct < thresholds["min_prediction_accuracy_pct"])

    if closed_trades == 0:
        return "warning", "watch", "medium", breaches
    if breaches == 0:
        return "healthy", "keep", "none", 0
    if breaches == 1:
        return "warning", "watch", "low", breaches
    if breaches == 2:
        return "warning", "adjust", "medium", breaches
    if breaches >= 3 and expectancy < 0:
        return "critical", "block", "critical", breaches
    return "warning", "adjust", "high", breaches



def build_scorecard_front(
    *,
    scope: str,
    subject_id: str,
    subject_label: str,
    period_ref: str,
    period_start: date,
    period_end: date,
    period_type: str,
    metrics: Dict[str, Any],
    prediction_accuracy_pct: float,
    learning_report_name: Optional[str],
    thresholds_ctx: ThresholdContext,
    human_approval_required: bool = False,
    extra_tags: Optional[List[str]] = None,
    deviation_count: int = 0,
    blocked_trades_count: int = 0,
    watchlist_alert_count: int = 0,
) -> Dict[str, Any]:
    thresholds = thresholds_for_context(thresholds_ctx, DEFAULT_MIN_SAMPLE)
    health_status, decision_status, deviation_severity, threshold_breach_count = derive_decision(metrics, thresholds, prediction_accuracy_pct)
    avg_scores = [x for x in [metrics.get("avg_score_winners"), metrics.get("avg_score_losers")] if x is not None]
    average_entry_score = round(sum(avg_scores) / len(avg_scores), 2) if avg_scores else 0.0
    front = {
        "schema_type": "scorecard",
        "schema_version": 1.0,
        "scorecard_id": f"SC_{scope.upper()}_{slugify(subject_id).upper()}_{period_ref}",
        "scorecard_date": period_end.isoformat(),
        "period_type": period_type,
        "period_ref": period_ref,
        "period_start": period_start.isoformat(),
        "period_end": period_end.isoformat(),
        "system_phase": "simulate",
        "scope": scope,
        "subject_id": subject_id,
        "subject_label": subject_label,
        "health_status": health_status,
        "decision_status": decision_status,
        "deviation_severity": deviation_severity,
        "closed_trades_count": int(metrics.get("total_closed_trades", 0) or 0),
        "win_rate_pct": round(float(metrics.get("win_rate", 0.0) or 0.0) * 100.0, 2),
        "average_rr": round(float(metrics.get("avg_rr", 0.0) or 0.0), 2),
        "expectancy": round(float(metrics.get("expectancy", 0.0) or 0.0), 4),
        "prediction_accuracy_pct": prediction_accuracy_pct,
        "average_entry_score": average_entry_score,
        "average_entry_score_winners": round(float(metrics.get("avg_score_winners", 0.0) or 0.0), 2),
        "average_entry_score_losers": round(float(metrics.get("avg_score_losers", 0.0) or 0.0), 2),
        "threshold_breach_count": threshold_breach_count,
        "deviation_count": deviation_count,
        "blocked_trades_count": blocked_trades_count,
        "watchlist_alert_count": watchlist_alert_count,
        "human_approval_required": human_approval_required,
        "linked_learning_report": learning_report_name,
        "active_threshold_scope": thresholds_ctx.scope,
        "active_threshold_profile_id": thresholds_ctx.profile_id,
        "active_threshold_version": thresholds_ctx.version,
        "tags": ["scorecard", "governance", period_type, scope] + (extra_tags or []),
    }
    return front



def build_scorecard_body(subject_summary_lines: List[str], metrics: Dict[str, Any], thresholds_ctx: ThresholdContext, prediction_accuracy_pct: float, deviations: List[str], action_lines: List[str]) -> str:
    thresholds = thresholds_for_context(thresholds_ctx, DEFAULT_MIN_SAMPLE)
    closed_trades = int(metrics.get("total_closed_trades", 0) or 0)
    win_rate_pct = round(float(metrics.get("win_rate", 0.0) or 0.0) * 100.0, 2)
    average_rr = round(float(metrics.get("avg_rr", 0.0) or 0.0), 2)
    expectancy = round(float(metrics.get("expectancy", 0.0) or 0.0), 4)

    threshold_lines = [
        f"- min_closed_trades: {'pass' if closed_trades >= thresholds['min_closed_trades'] else 'breach'} (value={closed_trades}, target={int(thresholds['min_closed_trades'])})",
        f"- win_rate_pct: {'pass' if win_rate_pct >= thresholds['min_win_rate_pct'] else 'breach'} (value={win_rate_pct}, target={thresholds['min_win_rate_pct']})",
        f"- average_rr: {'pass' if average_rr >= thresholds['min_average_rr'] else 'breach'} (value={average_rr}, target={thresholds['min_average_rr']})",
        f"- expectancy: {'pass' if expectancy >= thresholds['min_expectancy'] else 'breach'} (value={expectancy}, target={thresholds['min_expectancy']})",
        f"- prediction_accuracy_pct: {'pass' if prediction_accuracy_pct >= thresholds['min_prediction_accuracy_pct'] else 'breach'} (value={prediction_accuracy_pct}, target={thresholds['min_prediction_accuracy_pct']})",
    ]

    health_status, decision_status, _, _ = derive_decision(metrics, thresholds, prediction_accuracy_pct)
    threshold_version = thresholds_ctx.version or "built_in_defaults"

    return f"""
# Scorecard Snapshot

## Subject Summary
{markdown_bullets(subject_summary_lines)}
- active_threshold_profile: {thresholds_ctx.scope}/{thresholds_ctx.profile_id} v{threshold_version}

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| closed_trades_count | {closed_trades} | {int(thresholds['min_closed_trades'])} | {metric_status(closed_trades, thresholds['min_closed_trades'], '>=')} |
| win_rate_pct | {win_rate_pct} | {thresholds['min_win_rate_pct']} | {metric_status(win_rate_pct, thresholds['min_win_rate_pct'], '>=')} |
| average_rr | {average_rr} | {thresholds['min_average_rr']} | {metric_status(average_rr, thresholds['min_average_rr'], '>=')} |
| expectancy | {expectancy} | {thresholds['min_expectancy']} | {metric_status(expectancy, thresholds['min_expectancy'], '>=')} |
| prediction_accuracy_pct | {prediction_accuracy_pct} | {thresholds['min_prediction_accuracy_pct']} | {metric_status(prediction_accuracy_pct, thresholds['min_prediction_accuracy_pct'], '>=')} |

## Threshold Review
{markdown_bullets(threshold_lines)}

## Deviations
{markdown_bullets(deviations)}

## Decision
- {decision_status}
- health_status: {health_status}

## Action Plan
{markdown_bullets(action_lines)}
"""



def scorecard_output_path(root: Path, scope: str, subject_id: str, period_ref: str) -> Path:
    out_dir = root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / "SCORECARDS"
    return out_dir / f"SCORECARD_{scope}_{slugify(subject_id)}_{period_ref}.md"



def generate_system_scorecard(root: Path, learning_ctx: Dict[str, Any], envelopes: List[TradeEnvelope], learning_mod, min_sample: int) -> Optional[Path]:
    data = learning_ctx["data"]
    learning_report_name = learning_ctx["path"].name if learning_ctx.get("path") else None
    period_start = learning_ctx["period_start"]
    period_end = learning_ctx["period_end"]
    period_ref = learning_ctx["period_ref"]
    period_type = learning_ctx["period_type"]
    thresholds_ctx = resolve_threshold_context(root, "system", period_end, min_sample)

    if data.get("schema_type") == "learning_report":
        metrics = {
            "total_closed_trades": int(data.get("closed_trades_analyzed", 0) or 0),
            "win_rate": float(data.get("win_rate_pct", 0.0) or 0.0) / 100.0,
            "avg_rr": float(data.get("average_rr", 0.0) or 0.0),
            "expectancy": float(data.get("expectancy", 0.0) or 0.0),
            "avg_score_winners": float(data.get("average_entry_score_winners", 0.0) or 0.0),
            "avg_score_losers": float(data.get("average_entry_score_losers", 0.0) or 0.0),
        }
        prediction_accuracy_pct = round(float(data.get("prediction_accuracy_overall_pct", 0.0) or 0.0), 2)
        watchlist_alert_count = 1 if data.get("worst_asset") else 0
        human_approval_required = bool(data.get("human_approval_required", False))
        deviations = ["- none"]
        if int(data.get("invalid_files_count", 0) or 0) > 0:
            deviations = [f"- schema/data quality risk: invalid_files_count={int(data.get('invalid_files_count', 0) or 0)}"]
        action_lines = [
            f"- follow readiness_status: {data.get('readiness_status', 'continue_simulate')}",
            "- use this system scorecard as the governance baseline for the week",
        ]
    else:
        trades = [env.trade for env in envelopes]
        metrics = vars(learning_mod.compute_metrics(trades))
        prediction_accuracy_pct = compute_prediction_accuracy_pct(learning_mod.compare_predictions(trades))
        watchlist_alert_count = 0
        human_approval_required = False
        deviations = ["- no learning report front matter detected; scorecard generated from closed trades only"]
        action_lines = ["- generate a canonical LEARNING_REPORT before using this scorecard in governance"]

    subject_summary = [
        "- Weekly governance snapshot for EURU_TOS.",
        "- Built from the current learning report and filtered closed trades for the analysis period.",
    ]
    front = build_scorecard_front(
        scope="system",
        subject_id="euru_tos",
        subject_label="EURU_TOS",
        period_ref=period_ref,
        period_start=period_start,
        period_end=period_end,
        period_type=period_type,
        metrics=metrics,
        prediction_accuracy_pct=prediction_accuracy_pct,
        learning_report_name=learning_report_name,
        thresholds_ctx=thresholds_ctx,
        human_approval_required=human_approval_required,
        watchlist_alert_count=watchlist_alert_count,
        extra_tags=["system"],
    )
    body = build_scorecard_body(subject_summary, metrics, thresholds_ctx, prediction_accuracy_pct, deviations, action_lines)
    path = scorecard_output_path(root, "system", "euru_tos", period_ref)
    return write_markdown_with_front_matter(path, front, body)



def generate_group_scorecards(root: Path, scope: str, groups: Dict[str, List[TradeEnvelope]], learning_ctx: Dict[str, Any], learning_mod, min_sample: int) -> List[Path]:
    out: List[Path] = []
    learning_report_name = learning_ctx["path"].name if learning_ctx.get("path") else None
    period_start = learning_ctx["period_start"]
    period_end = learning_ctx["period_end"]
    period_ref = learning_ctx["period_ref"]
    period_type = learning_ctx["period_type"]
    thresholds_ctx = resolve_threshold_context(root, scope, period_end, min_sample)

    for raw_key, envs in sorted(groups.items()):
        if len(envs) < min_sample:
            continue
        trades = [env.trade for env in envs]
        metrics = vars(learning_mod.compute_metrics(trades))
        prediction_accuracy = learning_mod.compare_predictions(trades)
        prediction_accuracy_pct = compute_prediction_accuracy_pct(prediction_accuracy)
        asset_failures = learning_mod.identify_patterns(trades).get("repeated_asset_failures", [])
        watchlist_alert_count = len([x for x in asset_failures if x.get("sample", 0) >= 2 and x.get("loss_rate", 0) >= 0.7])
        subject_id = slugify(raw_key) if scope != "setup" else raw_key
        subject_label = raw_key.upper() if scope == "asset" else raw_key
        deviations = ["- none"]
        if scope == "agent" and not any(env.agent_name for env in envs):
            deviations = ["- agent attribution is partially missing in source trades"]
        action_lines = [
            f"- maintain governance watch on {raw_key}",
            f"- compare {raw_key} against the next Friday cycle before changing thresholds",
        ]
        if watchlist_alert_count:
            action_lines.insert(0, f"- repeated failure pattern detected for {raw_key}; consider watchlist or setup review")
        subject_summary = [
            f"- {scope} governance snapshot for {raw_key}.",
            f"- sample size: {len(envs)} closed trades in analysis period.",
        ]
        front = build_scorecard_front(
            scope=scope,
            subject_id=subject_id,
            subject_label=subject_label,
            period_ref=period_ref,
            period_start=period_start,
            period_end=period_end,
            period_type=period_type,
            metrics=metrics,
            prediction_accuracy_pct=prediction_accuracy_pct,
            learning_report_name=learning_report_name,
            thresholds_ctx=thresholds_ctx,
            watchlist_alert_count=watchlist_alert_count,
            extra_tags=[scope, slugify(raw_key)],
        )
        body = build_scorecard_body(subject_summary, metrics, thresholds_ctx, prediction_accuracy_pct, deviations, action_lines)
        path = scorecard_output_path(root, scope, subject_id, period_ref)
        out.append(write_markdown_with_front_matter(path, front, body))
    return out



def generate_score_engine_scorecard(root: Path, envelopes: List[TradeEnvelope], learning_ctx: Dict[str, Any], learning_mod, min_sample: int, subject_id: str = DEFAULT_SCORE_ENGINE_ID) -> Optional[Path]:
    trades = [env.trade for env in envelopes]
    if len(trades) < min_sample:
        return None
    metrics = vars(learning_mod.compute_metrics(trades))
    prediction_accuracy = learning_mod.compare_predictions(trades)
    prediction_accuracy_pct = compute_prediction_accuracy_pct(prediction_accuracy)
    period_start = learning_ctx["period_start"]
    period_end = learning_ctx["period_end"]
    period_ref = learning_ctx["period_ref"]
    period_type = learning_ctx["period_type"]
    learning_report_name = learning_ctx["path"].name if learning_ctx.get("path") else None
    thresholds_ctx = resolve_threshold_context(root, "score_engine", period_end, min_sample)

    deviations = ["- none"]
    if prediction_accuracy_pct < thresholds_for_context(thresholds_ctx, min_sample)["min_prediction_accuracy_pct"]:
        deviations = [f"- score engine predictive quality is below threshold at {prediction_accuracy_pct}%"]
    action_lines = [
        "- review false positives and false negatives from the latest learning report",
        "- keep the threshold profile version attached to this scorecard for auditability",
    ]
    subject_summary = [
        "- Governance snapshot for the active Score Engine profile.",
        f"- score_engine_subject_id: {subject_id}",
    ]
    front = build_scorecard_front(
        scope="score_engine",
        subject_id=subject_id,
        subject_label=subject_id.upper(),
        period_ref=period_ref,
        period_start=period_start,
        period_end=period_end,
        period_type=period_type,
        metrics=metrics,
        prediction_accuracy_pct=prediction_accuracy_pct,
        learning_report_name=learning_report_name,
        thresholds_ctx=thresholds_ctx,
        extra_tags=["score_engine"],
    )
    body = build_scorecard_body(subject_summary, metrics, thresholds_ctx, prediction_accuracy_pct, deviations, action_lines)
    path = scorecard_output_path(root, "score_engine", subject_id, period_ref)
    return write_markdown_with_front_matter(path, front, body)



def write_run_report(root: Path, payload: Dict[str, Any]) -> Path:
    out_dir = ensure_dir(root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / "SCORECARD_RUN_REPORTS")
    ts = local_timestamp()
    path = out_dir / f"SCORECARD_RUN_REPORT_{ts}.md"
    lines = [
        "# EURU Scorecard Engine Run Report",
        "",
        f"- generated_at: {utc_now()}",
        f"- root: `{root}`",
        f"- learning_report: `{payload.get('learning_report')}`",
        f"- total_generated: {payload.get('total_generated', 0)}",
        f"- scopes_generated: {', '.join(payload.get('scopes_generated', [])) or 'none'}",
        "",
        "## Generated Files",
        "",
    ]
    generated = payload.get("generated_files", [])
    if generated:
        for item in generated:
            lines.append(f"- `{item}`")
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## Summary JSON",
        "",
        "```json",
        json.dumps(payload, indent=2, ensure_ascii=False),
        "```",
    ])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Public runner
# ---------------------------------------------------------------------------


def run(
    *,
    root: Path,
    learning_report_path: Optional[Path] = None,
    scopes: Optional[Sequence[str]] = None,
    min_sample: int = DEFAULT_MIN_SAMPLE,
    write_run_report_flag: bool = True,
    verbose: bool = False,
) -> Dict[str, Any]:
    scopes = list(scopes or SUPPORTED_SCOPES)
    invalid = [s for s in scopes if s not in SUPPORTED_SCOPES]
    if invalid:
        raise ValueError(f"Unsupported scopes requested: {invalid}")

    learning_engine_path = resolve_script(root, "euru_learning_engine.py")
    if not learning_engine_path.exists():
        raise FileNotFoundError(f"Required script not found: {learning_engine_path}")
    learning_mod = load_module("euru_learning_engine_runtime_for_scorecards", learning_engine_path)

    learning_report_path = learning_report_path or find_latest_learning_report(root)
    learning_ctx = load_learning_context(learning_report_path)

    envelopes = load_trade_envelopes(root, learning_mod, learning_ctx["period_start"], learning_ctx["period_end"])
    generated: List[Path] = []

    if "system" in scopes:
        system_path = generate_system_scorecard(root, learning_ctx, envelopes, learning_mod, min_sample)
        if system_path:
            generated.append(system_path)

    if "asset" in scopes:
        asset_groups = group_envelopes(envelopes, lambda env: env.trade.symbol.lower() if getattr(env.trade, "symbol", None) else None)
        generated.extend(generate_group_scorecards(root, "asset", asset_groups, learning_ctx, learning_mod, min_sample))

    if "setup" in scopes:
        setup_groups = group_envelopes(envelopes, lambda env: getattr(env.trade, "setup_type", None))
        generated.extend(generate_group_scorecards(root, "setup", setup_groups, learning_ctx, learning_mod, min_sample))

    if "agent" in scopes:
        agent_groups = group_envelopes(envelopes, lambda env: env.agent_name or None)
        generated.extend(generate_group_scorecards(root, "agent", agent_groups, learning_ctx, learning_mod, min_sample))

    if "score_engine" in scopes:
        sc_path = generate_score_engine_scorecard(root, envelopes, learning_ctx, learning_mod, min_sample)
        if sc_path:
            generated.append(sc_path)

    payload = {
        "root": str(root),
        "learning_report": str(learning_ctx["path"]) if learning_ctx.get("path") else None,
        "period_ref": learning_ctx["period_ref"],
        "period_start": learning_ctx["period_start"].isoformat(),
        "period_end": learning_ctx["period_end"].isoformat(),
        "scopes_requested": scopes,
        "scopes_generated": sorted({load_markdown_with_front_matter(Path(p))[0].get("scope", "unknown") for p in generated}) if generated else [],
        "closed_trades_considered": len(envelopes),
        "total_generated": len(generated),
        "generated_files": [str(p) for p in generated],
    }
    if write_run_report_flag:
        report_path = write_run_report(root, payload)
        payload["run_report_path"] = str(report_path)
    if verbose:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    return payload


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate dedicated EURU scorecards from learning outputs")
    parser.add_argument("--root", default=".", help="Path to Euru_TOS root")
    parser.add_argument("--learning-report", default=None, help="Explicit path to LEARNING_REPORT markdown file")
    parser.add_argument("--scopes", default=",".join(SUPPORTED_SCOPES), help="Comma-separated scorecard scopes to generate")
    parser.add_argument("--min-sample", type=int, default=DEFAULT_MIN_SAMPLE, help="Minimum closed trades required to generate group scorecards")
    parser.add_argument("--no-run-report", action="store_true", help="Do not write SCORECARD_RUN_REPORT markdown")
    parser.add_argument("--json", action="store_true", help="Print JSON payload")
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    learning_report = Path(args.learning_report).resolve() if args.learning_report else None
    scopes = [s.strip() for s in args.scopes.split(",") if s.strip()]
    payload = run(
        root=root,
        learning_report_path=learning_report,
        scopes=scopes,
        min_sample=max(1, int(args.min_sample)),
        write_run_report_flag=not args.no_run_report,
        verbose=args.json,
    )
    if not args.json:
        print(f"Generated {payload['total_generated']} scorecard(s).")
        for path in payload["generated_files"]:
            print(path)
        if payload.get("run_report_path"):
            print(f"Run report: {payload['run_report_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

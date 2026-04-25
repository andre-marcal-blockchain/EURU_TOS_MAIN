#!/usr/bin/env python3
"""
EURU_TOS Friday Cycle Orchestrator

Official weekly pipeline:
GitHub Sync -> Schema Validator -> Learning Preflight -> Learning Engine
-> Learning Report -> Scorecards -> Human Governance Review -> Weekly Close

This runner is the single entrypoint for the Friday cycle.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone, date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


# -----------------------------
# Models
# -----------------------------

@dataclass
class StepResult:
    name: str
    status: str
    started_at: str
    ended_at: str
    details: Dict[str, Any] = field(default_factory=dict)
    artifacts: List[str] = field(default_factory=list)


# -----------------------------
# Helpers
# -----------------------------


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


def week_ref_from_date(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def resolve_script(root: Path, file_name: str) -> Path:
    candidate = root / file_name
    if candidate.exists():
        return candidate
    here_candidate = Path(__file__).resolve().parent / file_name
    if here_candidate.exists():
        return here_candidate
    return candidate


def write_markdown_with_front_matter(path: Path, front_matter: Dict[str, Any], body: str) -> Path:
    ensure_dir(path.parent)
    if yaml is None:
        raise RuntimeError("PyYAML is required to write front matter. Install with: pip install pyyaml")
    fm = yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True).strip()
    path.write_text(f"---\n{fm}\n---\n\n{body.strip()}\n", encoding="utf-8")
    return path


def parse_front_matter(path: Path) -> Tuple[Optional[Dict[str, Any]], str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None, text
    front = parts[0][4:]
    body = parts[1]
    if yaml is None:
        return None, body
    try:
        data = yaml.safe_load(front) or {}
    except Exception:
        return None, body
    return data, body


def extract_learning_report_sections(path: Path) -> Dict[str, List[str]]:
    _, body = parse_front_matter(path)
    if not body:
        body = path.read_text(encoding="utf-8", errors="ignore")
    sections: Dict[str, List[str]] = {}
    current = None
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            current = stripped[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return sections


def markdown_bullets(lines: List[str], default: str = "- none") -> str:
    cleaned = [ln.rstrip() for ln in lines if ln.strip()]
    return "\n".join(cleaned) if cleaned else default


# -----------------------------
# Step implementations
# -----------------------------


def step_git_sync(root: Path, git_pull: bool, allow_non_git_root: bool, require_clean_worktree: bool) -> StepResult:
    started = utc_now()
    details: Dict[str, Any] = {"root": str(root), "git_pull": git_pull}
    artifacts: List[str] = []

    def finish(status: str) -> StepResult:
        return StepResult("github_sync", status, started, utc_now(), details, artifacts)

    try:
        check = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError:
        details["reason"] = "git executable not found"
        return finish("BLOCKED")

    if check.returncode != 0 or check.stdout.strip().lower() != "true":
        details["reason"] = "root is not a git repository"
        return finish("PASS_WITH_WARNINGS" if allow_non_git_root else "BLOCKED")

    branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root, capture_output=True, text=True, timeout=30)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, timeout=30)
    status = subprocess.run(["git", "status", "--short"], cwd=root, capture_output=True, text=True, timeout=30)

    details["branch"] = branch.stdout.strip()
    details["commit"] = commit.stdout.strip()
    details["dirty_files"] = [ln for ln in status.stdout.splitlines() if ln.strip()]
    details["dirty_count"] = len(details["dirty_files"])

    if git_pull:
        pull = subprocess.run(["git", "pull", "--ff-only"], cwd=root, capture_output=True, text=True, timeout=120)
        details["git_pull_return_code"] = pull.returncode
        details["git_pull_stdout"] = pull.stdout.strip()
        details["git_pull_stderr"] = pull.stderr.strip()
        if pull.returncode != 0:
            details["reason"] = "git pull failed"
            return finish("BLOCKED")

    if require_clean_worktree and details["dirty_count"] > 0:
        details["reason"] = "working tree is not clean"
        return finish("PASS_WITH_WARNINGS")

    details["reason"] = "git repository inspected successfully"
    return finish("PASS")



def step_schema_validation(root: Path, validator_mod, write_report: bool = True) -> Tuple[StepResult, Dict[str, Any], List[Any], Optional[Path]]:
    started = utc_now()
    files = validator_mod.discover_markdown_files(root, None)
    results = [validator_mod.validate_file(path) for path in files]
    summary = validator_mod.summarize(results)
    report_path = None
    if write_report:
        report_text = validator_mod.make_markdown_report(summary, results, root)
        report_path = validator_mod.write_report(root, report_text)
    status = "PASS"
    if summary["invalid_files"] > 0 or summary["error_count"] > 0:
        status = "BLOCKED"
    elif summary["warning_count"] > 0:
        status = "PASS_WITH_WARNINGS"
    step = StepResult(
        name="schema_validation",
        status=status,
        started_at=started,
        ended_at=utc_now(),
        details=summary,
        artifacts=[str(report_path)] if report_path else [],
    )
    return step, summary, results, report_path



def step_learning_preflight(root: Path, preflight_mod, summary: Dict[str, Any], results: List[Any], strict_warnings: bool) -> Tuple[StepResult, str, str, Optional[Path]]:
    started = utc_now()
    has_errors = summary.get("invalid_files", 0) > 0 or summary.get("error_count", 0) > 0
    has_warnings = summary.get("warning_count", 0) > 0

    status = "PASS"
    reason = "Schema validation passed. Learning engine may run."
    if has_errors:
        status = "BLOCKED"
        reason = "Invalid schema files detected. Learning engine blocked to protect data integrity."
    elif has_warnings and strict_warnings:
        status = "BLOCKED"
        reason = "Warnings detected in strict-warnings mode. Learning engine blocked until reviewed."
    elif has_warnings:
        status = "PASS_WITH_WARNINGS"
        reason = "Schema validation passed with warnings. Learning engine may run, but review is recommended."

    report_path = preflight_mod.write_preflight_report(root, summary, results, status, reason, "")
    step = StepResult(
        name="learning_preflight",
        status=status,
        started_at=started,
        ended_at=utc_now(),
        details={
            "reason": reason,
            "strict_warnings": strict_warnings,
            "summary": summary,
        },
        artifacts=[str(report_path)] if report_path else [],
    )
    return step, status, reason, report_path



def step_learning_engine(root: Path, learning_mod, dry_run: bool) -> Tuple[StepResult, Optional[Dict[str, Any]]]:
    started = utc_now()
    try:
        result = learning_mod.run(root=root, dry_run=dry_run, verbose=False)
    except Exception as exc:
        return StepResult(
            name="learning_engine",
            status="FAILED",
            started_at=started,
            ended_at=utc_now(),
            details={"error": repr(exc)},
            artifacts=[],
        ), None

    report_path = result.get("report_path")
    details = {
        "trade_files_found": result.get("trade_files_found"),
        "closed_trades_parsed": result.get("closed_trades_parsed"),
        "journal_files_found": result.get("journal_files_found"),
        "readiness": result.get("readiness"),
    }
    status = "PASS"
    if not dry_run and report_path and not Path(report_path).exists():
        status = "FAILED"
        details["error"] = "learning report path returned, but file was not created"
    step = StepResult(
        name="learning_engine",
        status=status,
        started_at=started,
        ended_at=utc_now(),
        details=details,
        artifacts=[report_path] if report_path and Path(report_path).exists() else [],
    )
    return step, result



def step_learning_report_presence(root: Path, learning_result: Optional[Dict[str, Any]], dry_run: bool, validation_summary: Dict[str, Any]) -> Tuple[StepResult, Optional[Path]]:
    started = utc_now()
    report_path: Optional[Path] = None
    status = "MISSING"
    details: Dict[str, Any] = {}
    if learning_result:
        raw = learning_result.get("report_path")
        if raw:
            report_path = Path(raw)
            details["report_path"] = str(report_path)
    if dry_run:
        status = "SKIPPED"
        details["reason"] = "learning engine executed in dry-run mode"
    elif report_path and report_path.exists() and learning_result:
        report_path = build_canonical_learning_report(root, learning_result, validation_summary, report_path)
        status = "GENERATED"
        details["canonicalized"] = True
    else:
        details["reason"] = "learning report file not found"
    step = StepResult(
        name="learning_report",
        status=status,
        started_at=started,
        ended_at=utc_now(),
        details=details,
        artifacts=[str(report_path)] if report_path and report_path.exists() else [],
    )
    return step, report_path





def governance_counts(suggestions: List[Dict[str, Any]]) -> Tuple[int, int, int]:
    t1 = sum(1 for s in suggestions if s.get("governance_type") == "Type 1")
    t2 = sum(1 for s in suggestions if s.get("governance_type") == "Type 2")
    t3 = sum(1 for s in suggestions if s.get("governance_type") == "Type 3")
    return t1, t2, t3


def build_canonical_learning_report(root: Path, learning_result: Dict[str, Any], validation_summary: Dict[str, Any], target_path: Path) -> Path:
    metrics = learning_result.get("metrics", {})
    patterns = learning_result.get("patterns", {})
    prediction_accuracy = learning_result.get("prediction_accuracy", {})
    suggestions = learning_result.get("suggestions", [])
    readiness = learning_result.get("readiness", {})

    today = date.today()
    t1, t2, t3 = governance_counts(suggestions)
    prediction_accuracy_overall = compute_prediction_accuracy_pct(prediction_accuracy)
    best_setup_pred = prediction_accuracy.get("by_setup", [])
    prediction_accuracy_best_setup = round(float(best_setup_pred[0].get("accuracy", 0.0))*100.0, 2) if best_setup_pred else 0.0
    prediction_accuracy_worst_setup = round(float(best_setup_pred[-1].get("accuracy", 0.0))*100.0, 2) if best_setup_pred else 0.0
    repeated_failures = [x for x in patterns.get("repeated_asset_failures", []) if x.get("sample", 0) >= 2 and x.get("loss_rate", 0) >= 0.7]
    pending_human = [s for s in suggestions if s.get("governance_type") in {"Type 2", "Type 3"}]

    readiness_status = "execute_candidate" if readiness.get("suggestion") == "SUGGEST EXECUTE PHASE" else "continue_simulate"
    system_status = "critical" if validation_summary.get("invalid_files", 0) > 0 else ("warning" if validation_summary.get("warning_count", 0) > 0 else "healthy")
    front = {
        "schema_type": "learning_report",
        "schema_version": 1.0,
        "report_date": today.isoformat(),
        "period_start": today.isoformat(),
        "period_end": today.isoformat(),
        "period_type": "weekly",
        "system_phase": "simulate",
        "system_status": system_status,
        "readiness_status": readiness_status,
        "source_trade_files_count": int(learning_result.get("trade_files_found", 0) or 0),
        "closed_trades_analyzed": int(learning_result.get("closed_trades_parsed", 0) or 0),
        "journal_files_analyzed": int(learning_result.get("journal_files_found", 0) or 0),
        "invalid_files_count": int(validation_summary.get("invalid_files", 0) or 0),
        "legacy_format_detected_count": 0,
        "win_rate_pct": round(float(metrics.get("win_rate", 0.0) or 0.0) * 100.0, 2),
        "average_rr": round(float(metrics.get("avg_rr", 0.0) or 0.0), 2),
        "expectancy": round(float(metrics.get("expectancy", 0.0) or 0.0), 4),
        "average_win_rr": round(float(metrics.get("avg_win", 0.0) or 0.0), 2),
        "average_loss_rr": round(float(metrics.get("avg_loss", 0.0) or 0.0), 2),
        "best_setup_type": metrics.get("best_setup_types", [[None]])[0][0] if metrics.get("best_setup_types") else None,
        "worst_setup_type": metrics.get("worst_setup_types", [[None]])[0][0] if metrics.get("worst_setup_types") else None,
        "best_asset": metrics.get("best_assets", [[None]])[0][0].lower() if metrics.get("best_assets") else None,
        "worst_asset": metrics.get("worst_assets", [[None]])[0][0].lower() if metrics.get("worst_assets") else None,
        "average_entry_score_winners": round(float(metrics.get("avg_score_winners", 0.0) or 0.0), 2),
        "average_entry_score_losers": round(float(metrics.get("avg_score_losers", 0.0) or 0.0), 2),
        "prediction_accuracy_overall_pct": prediction_accuracy_overall,
        "prediction_accuracy_best_setup_pct": prediction_accuracy_best_setup,
        "prediction_accuracy_worst_setup_pct": prediction_accuracy_worst_setup,
        "governance_type_1_count": t1,
        "governance_type_2_count": t2,
        "governance_type_3_count": t3,
        "human_approval_required": bool(pending_human or readiness_status == "execute_candidate"),
        "execute_candidate": readiness_status == "execute_candidate",
        "tags": ["weekly_learning", "governance", "score_engine"],
    }

    performance_lines = [
        f"- closed_trades_analyzed: {front['closed_trades_analyzed']}",
        f"- win_rate_pct: {front['win_rate_pct']}",
        f"- average_rr: {front['average_rr']}",
        f"- expectancy: {front['expectancy']}",
    ]

    pattern_lines = []
    for row in patterns.get("score_bands", [])[:4]:
        pattern_lines.append(f"- score band {row.get('band')}: win_rate={round(float(row.get('win_rate',0))*100,2)} sample={row.get('sample')}")
    for row in patterns.get("setup_win_rates", [])[:4]:
        pattern_lines.append(f"- setup {row.get('setup')}: win_rate={round(float(row.get('win_rate',0))*100,2)} sample={row.get('sample')}")
    if not pattern_lines:
        pattern_lines.append("- none")

    score_lines = [
        f"- overall prediction accuracy: {prediction_accuracy_overall}%",
    ]
    for row in prediction_accuracy.get("by_asset", [])[:5]:
        score_lines.append(f"- asset {row.get('name')}: accuracy={round(float(row.get('accuracy',0))*100,2)} correct={row.get('correct')}/{row.get('total')}")
    for row in prediction_accuracy.get("by_setup", [])[:5]:
        score_lines.append(f"- setup {row.get('name')}: accuracy={round(float(row.get('accuracy',0))*100,2)} correct={row.get('correct')}/{row.get('total')}")

    asset_alert_lines = [f"- {row.get('asset','unknown')}: repeated failure pattern" for row in repeated_failures] or ["- none"]
    setup_alert_lines = []
    if front['best_setup_type']:
        setup_alert_lines.append(f"- best_setup_type: {front['best_setup_type']}")
    if front['worst_setup_type']:
        setup_alert_lines.append(f"- worst_setup_type: {front['worst_setup_type']}")
    if not setup_alert_lines:
        setup_alert_lines.append("- none")

    deviation_lines = []
    for note in learning_result.get("trade_files_skipped", [])[:10]:
        deviation_lines.append(f"- skipped trade file: {note}")
    if not deviation_lines:
        deviation_lines.append("- none")

    t1_lines = [f"- {s.get('recommendation')}" for s in suggestions if s.get("governance_type") == "Type 1"] or ["- none"]
    t2_lines = [f"- {s.get('recommendation')}" for s in suggestions if s.get("governance_type") == "Type 2"] or ["- none"]
    t3_lines = [f"- {s.get('recommendation')}" for s in suggestions if s.get("governance_type") == "Type 3"] or ["- none"]
    pending_lines = [f"- {s.get('recommendation')}" for s in pending_human] or ["- none"]
    next_lines = []
    if readiness_status == "execute_candidate":
        next_lines.append("- prepare human governance review for EXECUTE transition")
    else:
        next_lines.append("- continue SIMULATE and apply governance suggestions from this report")
    next_lines.append("- keep schema validator and preflight as mandatory gatekeepers")

    body = f"""
# Executive Summary

## Performance Summary
{markdown_bullets(performance_lines)}

## Patterns Identified
{markdown_bullets(pattern_lines)}

## Score Engine vs Actual Results
{markdown_bullets(score_lines)}

## Asset Alerts
{markdown_bullets(asset_alert_lines)}

## Setup Alerts
{markdown_bullets(setup_alert_lines)}

## Agent Deviation Analysis
{markdown_bullets(deviation_lines)}

## Governance Suggestions
### Type 1 — Immediate Adjustment
{markdown_bullets(t1_lines)}

### Type 2 — 24h Review
{markdown_bullets(t2_lines)}

### Type 3 — 48h Strategic
{markdown_bullets(t3_lines)}

## Pending Decisions for Human Approval
{markdown_bullets(pending_lines)}

## SIMULATE Readiness Check
- {readiness_status}

## Next Learning Actions
{markdown_bullets(next_lines)}
"""

    return write_markdown_with_front_matter(target_path, front, body)

def compute_prediction_accuracy_pct(prediction_accuracy: Dict[str, Any]) -> float:
    correct = 0
    total = 0
    for bucket in prediction_accuracy.get("by_asset", []):
        correct += int(bucket.get("correct", 0))
        total += int(bucket.get("total", 0))
    return round((correct / total) * 100.0, 2) if total else 0.0



def derive_decision_status(learning_result: Dict[str, Any], preflight_status: str) -> Tuple[str, str, str]:
    metrics = learning_result.get("metrics", {})
    readiness = learning_result.get("readiness", {})
    win_rate = float(metrics.get("win_rate", 0.0) or 0.0) * 100.0
    avg_rr = float(metrics.get("avg_rr", 0.0) or 0.0)
    expectancy = float(metrics.get("expectancy", 0.0) or 0.0)

    if preflight_status == "BLOCKED":
        return "critical", "block", "critical"
    if readiness.get("suggestion") == "SUGGEST EXECUTE PHASE":
        return "healthy", "keep", "none"
    if win_rate >= 50.0 and avg_rr >= 2.0 and expectancy > 0:
        return "healthy", "keep", "low"
    if expectancy > 0:
        return "warning", "watch", "medium"
    return "warning", "adjust", "high"



def build_system_scorecard(root: Path, learning_result: Dict[str, Any], learning_report_path: Optional[Path], preflight_status: str) -> Path:
    cycle_date = date.today()
    period_ref = week_ref_from_date(cycle_date)
    metrics = learning_result.get("metrics", {})
    readiness = learning_result.get("readiness", {})
    prediction_accuracy = learning_result.get("prediction_accuracy", {})
    suggestions = learning_result.get("suggestions", [])

    win_rate_pct = round(float(metrics.get("win_rate", 0.0) or 0.0) * 100.0, 2)
    avg_rr = round(float(metrics.get("avg_rr", 0.0) or 0.0), 2)
    expectancy = round(float(metrics.get("expectancy", 0.0) or 0.0), 4)
    prediction_accuracy_pct = compute_prediction_accuracy_pct(prediction_accuracy)
    average_entry_score = round((float(metrics.get("avg_score_winners", 0.0) or 0.0) + float(metrics.get("avg_score_losers", 0.0) or 0.0)) / 2.0, 2)
    average_entry_score_winners = round(float(metrics.get("avg_score_winners", 0.0) or 0.0), 2)
    average_entry_score_losers = round(float(metrics.get("avg_score_losers", 0.0) or 0.0), 2)
    threshold_breach_count = int(win_rate_pct < 50.0) + int(avg_rr < 2.0) + int(expectancy <= 0)

    health_status, decision_status, deviation_severity = derive_decision_status(learning_result, preflight_status)
    human_approval_required = bool(readiness.get("suggestion") == "SUGGEST EXECUTE PHASE" or any(s.get("governance_type") in {"Type 2", "Type 3"} for s in suggestions))

    front = {
        "schema_type": "scorecard",
        "schema_version": 1.0,
        "scorecard_id": f"SC_SYSTEM_EURU_TOS_{period_ref}",
        "scorecard_date": cycle_date.isoformat(),
        "period_type": "weekly",
        "period_ref": period_ref,
        "period_start": cycle_date.isoformat(),
        "period_end": cycle_date.isoformat(),
        "system_phase": "simulate",
        "scope": "system",
        "subject_id": "euru_tos",
        "subject_label": "EURU_TOS",
        "health_status": health_status,
        "decision_status": decision_status,
        "deviation_severity": deviation_severity,
        "closed_trades_count": int(metrics.get("total_closed_trades", 0) or 0),
        "win_rate_pct": win_rate_pct,
        "average_rr": avg_rr,
        "expectancy": expectancy,
        "prediction_accuracy_pct": prediction_accuracy_pct,
        "average_entry_score": average_entry_score,
        "average_entry_score_winners": average_entry_score_winners,
        "average_entry_score_losers": average_entry_score_losers,
        "threshold_breach_count": threshold_breach_count,
        "deviation_count": 0,
        "blocked_trades_count": 0,
        "watchlist_alert_count": len([x for x in learning_result.get("patterns", {}).get("repeated_asset_failures", []) if x.get("sample", 0) >= 2 and x.get("loss_rate", 0) >= 0.7]),
        "human_approval_required": human_approval_required,
        "linked_learning_report": learning_report_path.name if learning_report_path else None,
        "tags": ["scorecard", "governance", "weekly", "system"],
    }

    threshold_lines = []
    threshold_lines.append(f"- win_rate_pct: {'pass' if win_rate_pct >= 50.0 else 'breach'} (value={win_rate_pct}, target=50.0)")
    threshold_lines.append(f"- average_rr: {'pass' if avg_rr >= 2.0 else 'breach'} (value={avg_rr}, target=2.0)")
    threshold_lines.append(f"- expectancy: {'pass' if expectancy > 0 else 'breach'} (value={expectancy}, target=>0)")

    action_lines = []
    for suggestion in suggestions[:8]:
        action_lines.append(f"- {suggestion.get('governance_type', 'Type ?')} — {suggestion.get('recommendation', 'no recommendation text')}")
    if not action_lines:
        action_lines.append("- maintain current SIMULATE governance and continue collecting clean data")

    body = f"""
# Scorecard Snapshot

## Subject Summary
- Weekly governance snapshot for EURU_TOS Friday cycle.
- Generated automatically from the latest learning result.

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | {win_rate_pct} | 50.0 | {'pass' if win_rate_pct >= 50.0 else 'breach'} |
| average_rr | {avg_rr} | 2.0 | {'pass' if avg_rr >= 2.0 else 'breach'} |
| expectancy | {expectancy} | 0.01 | {'pass' if expectancy > 0 else 'breach'} |
| prediction_accuracy_pct | {prediction_accuracy_pct} | 60.0 | {'pass' if prediction_accuracy_pct >= 60.0 else 'watch'} |

## Threshold Review
{markdown_bullets(threshold_lines)}

## Deviations
- none

## Decision
- {decision_status}

## Action Plan
{markdown_bullets(action_lines)}
"""

    path = root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / "SCORECARDS" / f"SCORECARD_system_euru_tos_{period_ref}.md"
    return write_markdown_with_front_matter(path, front, body)



def step_scorecards(root: Path, learning_result: Optional[Dict[str, Any]], learning_report_path: Optional[Path], preflight_status: str) -> Tuple[StepResult, List[Path]]:
    started = utc_now()
    artifacts: List[Path] = []
    details: Dict[str, Any] = {}
    if not learning_result or not learning_report_path or not learning_report_path.exists():
        return StepResult(
            name="scorecards",
            status="FAILED",
            started_at=started,
            ended_at=utc_now(),
            details={"reason": "cannot generate scorecards without a learning report"},
            artifacts=[],
        ), []

    scorecard_engine = resolve_script(root, "euru_scorecard_engine.py")
    if scorecard_engine.exists():
        details["engine_mode"] = "external_engine_present_but_not_invoked_by_default"

    system_scorecard = build_system_scorecard(root, learning_result, learning_report_path, preflight_status)
    artifacts.append(system_scorecard)
    details["generated_count"] = len(artifacts)
    details["engine_mode"] = details.get("engine_mode", "built_in_fallback")
    return StepResult(
        name="scorecards",
        status="GENERATED",
        started_at=started,
        ended_at=utc_now(),
        details=details,
        artifacts=[str(p) for p in artifacts],
    ), artifacts



def step_human_governance_review(learning_result: Optional[Dict[str, Any]], scorecard_paths: List[Path]) -> StepResult:
    started = utc_now()
    pending: List[str] = []
    execute_candidate = False
    if learning_result:
        readiness = learning_result.get("readiness", {})
        execute_candidate = readiness.get("suggestion") == "SUGGEST EXECUTE PHASE"
        for suggestion in learning_result.get("suggestions", []):
            if suggestion.get("governance_type") in {"Type 2", "Type 3"}:
                pending.append(suggestion.get("recommendation", "pending governance decision"))
    if execute_candidate:
        pending.append("SIMULATE readiness suggests EXECUTE candidate — human approval required.")

    status = "APPROVED" if not pending else "REVIEW_REQUIRED"
    return StepResult(
        name="human_governance_review",
        status=status,
        started_at=started,
        ended_at=utc_now(),
        details={
            "pending_decisions": pending,
            "scorecards_reviewed": [str(p) for p in scorecard_paths],
        },
        artifacts=[],
    )



def write_cycle_report(root: Path, steps: List[StepResult], overall_status: str, cycle_started_at: str) -> Path:
    report_dir = ensure_dir(root / "08_DADOS_E_JOURNAL" / "SCORECARDS" / "FRIDAY_CYCLE_REPORTS")
    ts = local_timestamp()
    report_path = report_dir / f"FRIDAY_CYCLE_REPORT_{ts}.md"

    lines = [
        "# EURU Friday Cycle Report",
        "",
        f"- cycle_started_at: {cycle_started_at}",
        f"- cycle_finished_at: {utc_now()}",
        f"- overall_status: {overall_status}",
        "",
        "## Step Summary",
        "",
        "| step | status | started_at | ended_at | artifacts |",
        "|---|---|---|---|---:|",
    ]
    for step in steps:
        lines.append(
            f"| {step.name} | {step.status} | {step.started_at} | {step.ended_at} | {len(step.artifacts)} |"
        )

    for step in steps:
        lines.extend([
            "",
            f"## {step.name}",
            "",
            f"- status: {step.status}",
            f"- started_at: {step.started_at}",
            f"- ended_at: {step.ended_at}",
            "",
            "### Details",
            "",
            "```json",
            json.dumps(step.details, indent=2, ensure_ascii=False),
            "```",
            "",
            "### Artifacts",
            "",
        ])
        if step.artifacts:
            for artifact in step.artifacts:
                lines.append(f"- `{artifact}`")
        else:
            lines.append("- none")

    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return report_path


# -----------------------------
# Orchestration
# -----------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the official EURU Friday cycle pipeline")
    parser.add_argument("--root", default=".", help="Path to Euru_TOS root")
    parser.add_argument("--git-pull", action="store_true", help="Run git pull --ff-only during GitHub Sync")
    parser.add_argument("--allow-non-git-root", action="store_true", help="Allow execution when root is not a git repository")
    parser.add_argument("--require-clean-worktree", action="store_true", help="Warn if there are uncommitted changes")
    parser.add_argument("--strict-warnings", action="store_true", help="Block on schema warnings during preflight")
    parser.add_argument("--dry-run-learning", action="store_true", help="Run learning engine without writing LEARNING_REPORT")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON summary")
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    cycle_started_at = utc_now()
    steps: List[StepResult] = []

    validator_path = resolve_script(root, "euru_schema_validator.py")
    preflight_path = resolve_script(root, "euru_learning_preflight.py")
    learning_path = resolve_script(root, "euru_learning_engine.py")

    for required in [validator_path, preflight_path, learning_path]:
        if not required.exists():
            raise SystemExit(f"Required script not found: {required}")

    validator_mod = load_module("euru_schema_validator_runtime", validator_path)
    preflight_mod = load_module("euru_learning_preflight_runtime", preflight_path)
    learning_mod = load_module("euru_learning_engine_runtime", learning_path)

    # Step 0: GitHub Sync / inspection
    git_step = step_git_sync(root, args.git_pull, args.allow_non_git_root, args.require_clean_worktree)
    steps.append(git_step)
    if git_step.status == "BLOCKED":
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {git_step.name}. Report: {cycle_report}")
        return 1

    # Step 1: Schema validation
    schema_step, summary, results, _ = step_schema_validation(root, validator_mod, write_report=True)
    steps.append(schema_step)
    if schema_step.status == "BLOCKED":
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {schema_step.name}. Report: {cycle_report}")
        return 1

    # Step 2: Learning preflight
    preflight_step, preflight_status, _reason, _preflight_report = step_learning_preflight(root, preflight_mod, summary, results, args.strict_warnings)
    steps.append(preflight_step)
    if preflight_step.status == "BLOCKED":
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {preflight_step.name}. Report: {cycle_report}")
        return 1

    # Step 3: Learning engine
    learning_step, learning_result = step_learning_engine(root, learning_mod, args.dry_run_learning)
    steps.append(learning_step)
    if learning_step.status == "FAILED":
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {learning_step.name}. Report: {cycle_report}")
        return 1

    # Step 4: Learning report verification
    learning_report_step, learning_report_path = step_learning_report_presence(root, learning_result, args.dry_run_learning, summary)
    steps.append(learning_report_step)
    if learning_report_step.status not in {"GENERATED", "SKIPPED"}:
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {learning_report_step.name}. Report: {cycle_report}")
        return 1

    # Step 5: Scorecards
    scorecard_step, scorecard_paths = step_scorecards(root, learning_result, learning_report_path, preflight_status) if not args.dry_run_learning else (
        StepResult("scorecards", "SKIPPED", utc_now(), utc_now(), {"reason": "learning dry-run mode"}, []), []
    )
    steps.append(scorecard_step)
    if scorecard_step.status == "FAILED":
        overall = "CLOSED_BLOCKED"
        cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)
        if args.json:
            print(json.dumps({"overall_status": overall, "steps": [asdict(s) for s in steps], "cycle_report": str(cycle_report)}, indent=2, ensure_ascii=False))
        else:
            print(f"Friday cycle blocked at {scorecard_step.name}. Report: {cycle_report}")
        return 1

    # Step 6: Human governance review gate
    human_step = step_human_governance_review(learning_result, scorecard_paths)
    steps.append(human_step)

    # Step 7: Weekly close
    overall = "CLOSED_SUCCESS"
    if any(step.status == "PASS_WITH_WARNINGS" for step in steps) or human_step.status == "REVIEW_REQUIRED":
        overall = "CLOSED_WITH_WARNINGS"
    cycle_report = write_cycle_report(root, steps, overall, cycle_started_at)

    payload = {
        "overall_status": overall,
        "root": str(root),
        "cycle_report": str(cycle_report),
        "steps": [asdict(step) for step in steps],
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Friday cycle completed with status: {overall}")
        print(f"Cycle report: {cycle_report}")
    return 0 if overall != "CLOSED_BLOCKED" else 1


if __name__ == "__main__":
    _rc = main()
    try:
        from euru_git_sync import git_sync
        git_sync("friday cycle report")
    except Exception as _e:
        print(f"[git-sync] Skipped: {_e}")
    raise SystemExit(_rc)

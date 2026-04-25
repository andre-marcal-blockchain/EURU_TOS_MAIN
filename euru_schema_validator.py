#!/usr/bin/env python3
"""
EURU_TOS Schema Validator

Validates Markdown files with YAML front matter for the official Euru schemas:
- paper_trade
- daily_journal
- learning_report
- scorecard

Usage:
    python euru_schema_validator.py --root .
    python euru_schema_validator.py --root . --write-report
    python euru_schema_validator.py --root . --json
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install with: pip install pyyaml"
    ) from exc

SCHEMA_VERSION = "1.0"

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ISO_WEEK_RE = re.compile(r"^\d{4}-W\d{2}$")
ISO_MONTH_RE = re.compile(r"^\d{4}-\d{2}$")
ISO_DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$"
)

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


@dataclass
class ValidationMessage:
    severity: str  # error | warning | info
    code: str
    message: str


@dataclass
class ValidationResult:
    file_path: str
    schema_type: Optional[str] = None
    valid: bool = True
    messages: List[ValidationMessage] = field(default_factory=list)

    def add(self, severity: str, code: str, message: str) -> None:
        self.messages.append(ValidationMessage(severity, code, message))
        if severity == "error":
            self.valid = False


ENUMS: Dict[str, set[str]] = {
    "trade_status": {"planned", "open", "closed", "cancelled", "invalidated"},
    "side": {"long", "short"},
    "intent_type": {"open", "add", "hedge", "reduce", "close", "recovery_3x", "unwind"},
    "margin_mode": {"cross", "isolated"},
    "position_mode": {"one_way", "hedge"},
    "risk_state": {"low", "medium", "high", "critical"},
    "news_severity": {"none", "low", "medium", "high", "critical"},
    "mac_state": {"bullish", "bearish", "neutral", "transition", "countertrend", "invalid"},
    "setup_type": {
        "trend_continuation", "trend_reversal", "breakout", "pullback", "range_reclaim",
        "range_rejection", "mean_reversion", "news_reaction", "hedge_management",
        "recovery_3x", "unwind_exit", "custom",
    },
    "exit_reason": {
        "take_profit", "stop_loss", "manual_close", "time_stop", "thesis_invalidated",
        "hedge_adjustment", "recovery_3x_exit", "unwind_exit", "risk_off", "news_risk",
        "system_rule", "other",
    },
    "system_phase": {"simulate", "execute"},
    "market_regime": {"bull_trend", "bear_trend", "range", "volatile", "unclear", "event_driven"},
    "health_status": {"healthy", "warning", "critical"},
    "readiness_status": {"continue_simulate", "execute_candidate", "hold", "review_required", "blocked"},
    "governance_type": {
        "type_1_immediate_adjustment", "type_2_review_24h", "type_3_strategic_48h",
    },
    "scorecard_scope": {"system", "agent", "asset", "setup", "portfolio", "watchlist", "risk", "score_engine"},
    "period_type": {"daily", "weekly", "monthly", "cycle"},
    "outcome_status": {"positive", "neutral", "negative"},
    "decision_status": {"keep", "watch", "adjust", "block", "retire", "escalate"},
    "prediction_quality": {"aligned", "false_positive", "false_negative", "insufficient_data"},
    "deviation_severity": {"none", "low", "medium", "high", "critical"},
    "schema_type": {"paper_trade", "daily_journal", "learning_report", "scorecard",
                    "scout_report", "asian_scan_report", "breakout_scan_report", "trade_monitor_report"},
}

BODY_HEADINGS: Dict[str, List[str]] = {
    "paper_trade": [
        "# Trade Summary",
        "## Thesis",
        "## Entry Reasoning",
        "## Risk Plan",
        "## Management Notes",
        "## Exit Notes",
        "## Lessons Learned",
    ],
    "daily_journal": [
        "# Daily Summary",
        "## Daily Observations",
        "## Lessons Learned",
        "## Deviations",
        "## Watchlist Changes",
        "## Pending Decisions for Human Approval",
        "## Next-Day Focus",
    ],
    "learning_report": [
        "# Executive Summary",
        "## Performance Summary",
        "## Patterns Identified",
        "## Score Engine vs Actual Results",
        "## Asset Alerts",
        "## Setup Alerts",
        "## Agent Deviation Analysis",
        "## Governance Suggestions",
        "### Type 1 — Immediate Adjustment",
        "### Type 2 — 24h Review",
        "### Type 3 — 48h Strategic",
        "## Pending Decisions for Human Approval",
        "## SIMULATE Readiness Check",
        "## Next Learning Actions",
    ],
    "scorecard": [
        "# Scorecard Snapshot",
        "## Subject Summary",
        "## KPI Table",
        "## Threshold Review",
        "## Deviations",
        "## Decision",
        "## Action Plan",
    ],
}

SCHEMA_REQUIRED: Dict[str, Dict[str, Any]] = {
    "paper_trade": {
        "required": [
            "schema_type", "schema_version", "trade_id", "status", "system_phase", "symbol", "venue",
            "contract_type", "market_type", "asset_class", "side", "intent_type", "setup_type",
            "entry_datetime", "entry_price", "entry_score", "mac_state_at_entry", "risk_state_at_entry",
            "news_severity_at_entry", "margin_mode", "position_mode", "leverage", "quantity",
            "notional_usdt", "stop_loss", "take_profit", "planned_rr", "exit_datetime", "exit_price",
            "pnl_usdt", "pnl_pct", "rr_achieved", "exit_reason", "days_held",
            "score_prediction_label", "score_prediction_confidence", "linked_trade_ids", "tags",
        ],
        "enums": {
            "schema_type": "schema_type",
            "status": "trade_status",
            "system_phase": "system_phase",
            "side": "side",
            "intent_type": "intent_type",
            "setup_type": "setup_type",
            "mac_state_at_entry": "mac_state",
            "risk_state_at_entry": "risk_state",
            "news_severity_at_entry": "news_severity",
            "margin_mode": "margin_mode",
            "position_mode": "position_mode",
            "exit_reason": "exit_reason",
        },
        "numbers": {
            "entry_price", "entry_score", "leverage", "quantity", "notional_usdt", "stop_loss",
            "take_profit", "planned_rr", "exit_price", "pnl_usdt", "pnl_pct", "rr_achieved",
            "days_held", "score_prediction_confidence",
        },
        "dates": {"entry_datetime": "datetime", "exit_datetime": "datetime"},
        "arrays": {"linked_trade_ids", "tags"},
    },
    "daily_journal": {
        "required": [
            "schema_type", "schema_version", "journal_date", "system_phase", "system_status",
            "market_regime", "btc_macro_state", "portfolio_risk_state", "news_severity_max",
            "open_positions_count", "new_trades_count", "closed_trades_count", "watchlist_changes_count",
            "blockers_count", "key_theme_of_day", "summary_score", "tags",
        ],
        "enums": {
            "schema_type": "schema_type",
            "system_phase": "system_phase",
            "system_status": "health_status",
            "market_regime": "market_regime",
            "portfolio_risk_state": "risk_state",
            "news_severity_max": "news_severity",
        },
        "numbers": {
            "open_positions_count", "new_trades_count", "closed_trades_count", "watchlist_changes_count",
            "blockers_count", "summary_score",
        },
        "dates": {"journal_date": "date"},
        "arrays": {"tags"},
    },
    "learning_report": {
        "required": [
            "schema_type", "schema_version", "report_date", "period_start", "period_end", "period_type",
            "system_phase", "system_status", "readiness_status", "source_trade_files_count",
            "closed_trades_analyzed", "journal_files_analyzed", "invalid_files_count",
            "legacy_format_detected_count", "win_rate_pct", "average_rr", "expectancy",
            "average_win_rr", "average_loss_rr", "best_setup_type", "worst_setup_type",
            "best_asset", "worst_asset", "average_entry_score_winners", "average_entry_score_losers",
            "prediction_accuracy_overall_pct", "prediction_accuracy_best_setup_pct",
            "prediction_accuracy_worst_setup_pct", "governance_type_1_count", "governance_type_2_count",
            "governance_type_3_count", "human_approval_required", "execute_candidate", "tags",
        ],
        "enums": {
            "schema_type": "schema_type",
            "period_type": "period_type",
            "system_phase": "system_phase",
            "system_status": "health_status",
            "readiness_status": "readiness_status",
            "best_setup_type": "setup_type",
            "worst_setup_type": "setup_type",
        },
        "numbers": {
            "source_trade_files_count", "closed_trades_analyzed", "journal_files_analyzed",
            "invalid_files_count", "legacy_format_detected_count", "win_rate_pct", "average_rr",
            "expectancy", "average_win_rr", "average_loss_rr", "average_entry_score_winners",
            "average_entry_score_losers", "prediction_accuracy_overall_pct",
            "prediction_accuracy_best_setup_pct", "prediction_accuracy_worst_setup_pct",
            "governance_type_1_count", "governance_type_2_count", "governance_type_3_count",
        },
        "dates": {"report_date": "date", "period_start": "date", "period_end": "date"},
        "arrays": {"tags"},
        "booleans": {"human_approval_required", "execute_candidate"},
    },
    "scorecard": {
        "required": [
            "schema_type", "schema_version", "scorecard_id", "scorecard_date", "period_type", "period_ref",
            "period_start", "period_end", "system_phase", "scope", "subject_id", "subject_label",
            "health_status", "decision_status", "deviation_severity", "closed_trades_count",
            "win_rate_pct", "average_rr", "expectancy", "prediction_accuracy_pct", "average_entry_score",
            "average_entry_score_winners", "average_entry_score_losers", "threshold_breach_count",
            "deviation_count", "blocked_trades_count", "watchlist_alert_count", "human_approval_required",
            "linked_learning_report", "tags",
        ],
        "enums": {
            "schema_type": "schema_type",
            "period_type": "period_type",
            "system_phase": "system_phase",
            "scope": "scorecard_scope",
            "health_status": "health_status",
            "decision_status": "decision_status",
            "deviation_severity": "deviation_severity",
        },
        "numbers": {
            "closed_trades_count", "win_rate_pct", "average_rr", "expectancy", "prediction_accuracy_pct",
            "average_entry_score", "average_entry_score_winners", "average_entry_score_losers",
            "threshold_breach_count", "deviation_count", "blocked_trades_count", "watchlist_alert_count",
        },
        "dates": {"scorecard_date": "date", "period_start": "date", "period_end": "date", "period_ref": "period_ref"},
        "arrays": {"tags"},
        "booleans": {"human_approval_required"},
    },
}

for _st in ("scout_report", "asian_scan_report", "breakout_scan_report", "trade_monitor_report"):
    SCHEMA_REQUIRED[_st] = {"required": ["schema_type", "schema_version"], "enums": {"schema_type": "schema_type"}}

DEFAULT_SCAN_DIRS = [
    "08_DADOS_E_JOURNAL/JOURNAL_TRADES",
    "08_DADOS_E_JOURNAL/JOURNAL_DAILY",
    "08_DADOS_E_JOURNAL/SCORECARDS",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Euru markdown schema files.")
    parser.add_argument("--root", default=".", help="Path to Euru_TOS root")
    parser.add_argument("--write-report", action="store_true", help="Write markdown validation report")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--strict", action="store_true", help="Return non-zero exit code on warnings too")
    parser.add_argument("--paths", nargs="*", help="Optional specific paths to validate")
    return parser.parse_args()


def load_markdown_with_front_matter(path: Path) -> Tuple[Optional[Dict[str, Any]], str, bool]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None, text, False
    front_raw = match.group(1)
    body = text[match.end():]
    data = yaml.safe_load(front_raw) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML front matter must parse to a mapping")
    return data, body, True


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def validate_date(value: Any, mode: str) -> bool:
    if value is None:
        return True

    if mode == "date":
        if hasattr(value, "year") and hasattr(value, "month") and hasattr(value, "day") and not hasattr(value, "hour"):
            return True
        if not isinstance(value, str):
            return False
        if not ISO_DATE_RE.match(value):
            return False
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    if mode == "datetime":
        if isinstance(value, datetime):
            return True
        if not isinstance(value, str):
            return False
        if not ISO_DATETIME_RE.match(value):
            return False
        try:
            normalized = value.replace("Z", "+00:00")
            datetime.fromisoformat(normalized)
            return True
        except ValueError:
            return False

    if mode == "period_ref":
        if not isinstance(value, str):
            return False
        return bool(ISO_WEEK_RE.match(value) or ISO_MONTH_RE.match(value) or ISO_DATE_RE.match(value))

    return False


def validate_body_headings(schema_type: str, body: str, result: ValidationResult) -> None:
    headings = BODY_HEADINGS.get(schema_type, [])
    normalized_body = body.replace("\r\n", "\n")
    cursor = 0
    for heading in headings:
        pos = normalized_body.find(heading, cursor)
        if pos == -1:
            result.add("error", "missing_heading", f"Missing official heading: {heading}")
        else:
            cursor = pos + len(heading)


def validate_required(data: Dict[str, Any], fields: Iterable[str], result: ValidationResult) -> None:
    for field in fields:
        if field not in data:
            result.add("error", "missing_field", f"Missing required field: {field}")


def validate_enums(data: Dict[str, Any], mapping: Dict[str, str], result: ValidationResult) -> None:
    for field, enum_name in mapping.items():
        if field not in data:
            continue
        value = data[field]
        if value is None:
            continue
        if not isinstance(value, str):
            result.add("error", "invalid_enum_type", f"Field '{field}' must be a string enum value")
            continue
        allowed = ENUMS[enum_name]
        if value not in allowed:
            result.add("error", "invalid_enum_value", f"Field '{field}' has invalid value '{value}'. Allowed: {sorted(allowed)}")


def validate_numbers(data: Dict[str, Any], fields: Iterable[str], result: ValidationResult) -> None:
    for field in fields:
        if field not in data:
            continue
        value = data[field]
        if value is None:
            continue
        if not is_number(value):
            result.add("error", "invalid_number", f"Field '{field}' must be numeric")


def validate_booleans(data: Dict[str, Any], fields: Iterable[str], result: ValidationResult) -> None:
    for field in fields:
        if field not in data:
            continue
        value = data[field]
        if value is None:
            continue
        if not isinstance(value, bool):
            result.add("error", "invalid_boolean", f"Field '{field}' must be true or false")


def validate_arrays(data: Dict[str, Any], fields: Iterable[str], result: ValidationResult) -> None:
    for field in fields:
        if field not in data:
            continue
        value = data[field]
        if value is None:
            continue
        if not isinstance(value, list):
            result.add("error", "invalid_array", f"Field '{field}' must be a YAML list")


def validate_dates(data: Dict[str, Any], mapping: Dict[str, str], result: ValidationResult) -> None:
    for field, mode in mapping.items():
        if field not in data:
            continue
        value = data[field]
        if value is None:
            continue
        if not validate_date(value, mode):
            result.add("error", "invalid_date", f"Field '{field}' is not valid {mode} format")


def validate_common(data: Dict[str, Any], result: ValidationResult) -> Optional[str]:
    schema_type = data.get("schema_type")
    result.schema_type = schema_type
    if schema_type is None:
        result.add("error", "missing_schema_type", "Missing schema_type")
        return None
    if schema_type not in ENUMS["schema_type"]:
        result.add("error", "invalid_schema_type", f"Unsupported schema_type '{schema_type}'")
        return None
    version = data.get("schema_version")
    version_normalized = str(version) if version is not None else None
    if version_normalized != SCHEMA_VERSION:
        result.add("error", "invalid_schema_version", f"schema_version must be '{SCHEMA_VERSION}'")
    return schema_type


def validate_schema_specific(schema_type: str, data: Dict[str, Any], body: str, result: ValidationResult) -> None:
    spec = SCHEMA_REQUIRED[schema_type]
    validate_required(data, spec.get("required", []), result)
    validate_enums(data, spec.get("enums", {}), result)
    validate_numbers(data, spec.get("numbers", set()), result)
    validate_arrays(data, spec.get("arrays", set()), result)
    validate_booleans(data, spec.get("booleans", set()), result)
    validate_dates(data, spec.get("dates", {}), result)
    validate_body_headings(schema_type, body, result)

    if schema_type == "paper_trade":
        validate_paper_trade_logic(data, result)
    elif schema_type == "learning_report":
        validate_learning_report_logic(data, result)
    elif schema_type == "scorecard":
        validate_scorecard_logic(data, result)


def validate_paper_trade_logic(data: Dict[str, Any], result: ValidationResult) -> None:
    status = data.get("status")
    exit_fields = ["exit_datetime", "exit_price", "pnl_usdt", "pnl_pct", "rr_achieved", "exit_reason", "days_held"]
    if status == "open":
        for field in exit_fields:
            if data.get(field) is not None:
                result.add("error", "open_trade_exit_data", f"Open trade must have {field}: null")
    if status == "closed":
        for field in exit_fields:
            if field not in data or data.get(field) is None:
                result.add("error", "closed_trade_missing_exit_data", f"Closed trade must include {field}")


def validate_learning_report_logic(data: Dict[str, Any], result: ValidationResult) -> None:
    closed_trades = data.get("closed_trades_analyzed")
    execute_candidate = data.get("execute_candidate")
    readiness_status = data.get("readiness_status")
    win_rate = data.get("win_rate_pct")
    average_rr = data.get("average_rr")
    expectancy = data.get("expectancy")

    if is_number(closed_trades) and closed_trades < 20 and execute_candidate is True:
        result.add("error", "readiness_rule", "execute_candidate must be false when closed_trades_analyzed < 20")

    if readiness_status == "execute_candidate":
        if not (is_number(win_rate) and win_rate >= 50 and is_number(average_rr) and average_rr >= 2.0 and is_number(expectancy) and expectancy > 0):
            result.add("error", "readiness_rule", "readiness_status execute_candidate requires win_rate >= 50, average_rr >= 2.0, expectancy > 0")

    if is_number(data.get("invalid_files_count")) and data.get("invalid_files_count", 0) > 0:
        if "schema/data quality risk" not in body_lower_safe(data):
            # rely on body text search separately in report body via crude warning; not fatal
            result.add("warning", "quality_risk_note_missing", "Learning report has invalid_files_count > 0; ensure schema/data quality risk is mentioned in the body")


def validate_scorecard_logic(data: Dict[str, Any], result: ValidationResult) -> None:
    scope = data.get("scope")
    subject_id = data.get("subject_id")
    if scope == "system" and subject_id != "euru_tos":
        result.add("error", "scope_subject_mismatch", "System scorecard subject_id must be 'euru_tos'")
    if scope == "asset" and isinstance(subject_id, str) and subject_id != subject_id.lower():
        result.add("error", "scope_subject_mismatch", "Asset scorecard subject_id must be lowercase")
    if scope == "setup":
        allowed = ENUMS["setup_type"]
        if subject_id not in allowed:
            result.add("error", "scope_subject_mismatch", f"Setup scorecard subject_id must be one of official setup enums: {sorted(allowed)}")


def body_lower_safe(data: Dict[str, Any]) -> str:
    # placeholder helper for compatibility with current validator logic
    return ""


def validate_file(path: Path) -> ValidationResult:
    result = ValidationResult(file_path=str(path))
    try:
        data, body, has_front_matter = load_markdown_with_front_matter(path)
    except Exception as exc:
        result.add("error", "parse_error", f"Failed to parse file: {exc}")
        return result

    if not has_front_matter or data is None:
        result.add("error", "missing_front_matter", "Missing YAML front matter")
        return result

    schema_type = validate_common(data, result)
    if schema_type is None:
        return result

    validate_schema_specific(schema_type, data, body, result)
    return result


def should_skip_file(path: Path) -> bool:
    name = path.name.upper()
    admin_prefixes = (
        "SCHEMA_VALIDATION_REPORT_",
        "LEARNING_PREFLIGHT_REPORT_",
        "FRIDAY_CYCLE_REPORT_",
    )
    return name.startswith(admin_prefixes)


def discover_markdown_files(root: Path, explicit_paths: Optional[List[str]] = None) -> List[Path]:
    if explicit_paths:
        files: List[Path] = []
        for item in explicit_paths:
            p = (root / item).resolve() if not Path(item).is_absolute() else Path(item)
            if p.is_file() and p.suffix.lower() == ".md" and not should_skip_file(p):
                files.append(p)
            elif p.is_dir():
                files.extend(sorted(x for x in p.rglob("*.md") if x.is_file() and not should_skip_file(x)))
        return sorted(set(files))

    files = []
    for rel in DEFAULT_SCAN_DIRS:
        directory = root / rel
        if directory.exists():
            files.extend(sorted(x for x in directory.rglob("*.md") if x.is_file() and not should_skip_file(x)))
    return sorted(set(files))


def summarize(results: List[ValidationResult]) -> Dict[str, Any]:
    total = len(results)
    valid = sum(1 for r in results if r.valid)
    invalid = total - valid
    warning_count = sum(1 for r in results for m in r.messages if m.severity == "warning")
    error_count = sum(1 for r in results for m in r.messages if m.severity == "error")
    by_schema: Dict[str, Dict[str, int]] = {}
    for r in results:
        key = r.schema_type or "unknown"
        by_schema.setdefault(key, {"total": 0, "valid": 0, "invalid": 0})
        by_schema[key]["total"] += 1
        by_schema[key]["valid" if r.valid else "invalid"] += 1
    return {
        "total_files": total,
        "valid_files": valid,
        "invalid_files": invalid,
        "warning_count": warning_count,
        "error_count": error_count,
        "by_schema": by_schema,
    }


def make_markdown_report(summary: Dict[str, Any], results: List[ValidationResult], root: Path) -> str:
    now = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    lines = [
        "# EURU Schema Validation Report",
        "",
        f"- generated_at: {now}",
        f"- root: `{root}`",
        f"- total_files: {summary['total_files']}",
        f"- valid_files: {summary['valid_files']}",
        f"- invalid_files: {summary['invalid_files']}",
        f"- warning_count: {summary['warning_count']}",
        f"- error_count: {summary['error_count']}",
        "",
        "## Summary by Schema",
        "",
        "| schema | total | valid | invalid |",
        "|---|---:|---:|---:|",
    ]
    for schema, stats in sorted(summary["by_schema"].items()):
        lines.append(f"| {schema} | {stats['total']} | {stats['valid']} | {stats['invalid']} |")

    lines.extend(["", "## File Results", ""])
    for r in results:
        status = "VALID" if r.valid else "INVALID"
        lines.append(f"### {status} — `{r.file_path}`")
        if not r.messages:
            lines.append("- no issues")
        else:
            for m in r.messages:
                lines.append(f"- [{m.severity.upper()}] {m.code}: {m.message}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_report(root: Path, report_text: str) -> Path:
    output_dir = root / "08_DADOS_E_JOURNAL" / "SCORECARDS"
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    report_path = output_dir / f"SCHEMA_VALIDATION_REPORT_{today}.md"
    report_path.write_text(report_text, encoding="utf-8")
    return report_path


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    files = discover_markdown_files(root, args.paths)

    if not files:
        payload = {"summary": {"total_files": 0, "valid_files": 0, "invalid_files": 0, "warning_count": 0, "error_count": 0, "by_schema": {}}, "results": []}
        if args.json:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print("No markdown files found for validation.")
        return 0

    results = [validate_file(path) for path in files]
    summary_data = summarize(results)

    if args.json:
        payload = {
            "summary": summary_data,
            "results": [
                {
                    "file_path": r.file_path,
                    "schema_type": r.schema_type,
                    "valid": r.valid,
                    "messages": [m.__dict__ for m in r.messages],
                }
                for r in results
            ],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Validated {summary_data['total_files']} files")
        print(f"Valid: {summary_data['valid_files']} | Invalid: {summary_data['invalid_files']} | Warnings: {summary_data['warning_count']} | Errors: {summary_data['error_count']}")

    report_path: Optional[Path] = None
    if args.write_report:
        report_text = make_markdown_report(summary_data, results, root)
        report_path = write_report(root, report_text)
        if not args.json:
            print(f"Report written to: {report_path}")

    has_errors = any(not r.valid for r in results)
    has_warnings = any(any(m.severity == "warning" for m in r.messages) for r in results)

    if report_path and args.json:
        pass

    if has_errors:
        return 1
    if args.strict and has_warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

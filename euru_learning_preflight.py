#!/usr/bin/env python3
"""
EURU_TOS Learning Preflight

Mandatory governance gate before running euru_learning_engine.py.

What it does:
1. Runs schema validation over official markdown sources.
2. Writes a validation report when warnings/errors exist (or when requested).
3. Blocks the learning engine if invalid schema files are found.
4. Optionally blocks on warnings in strict mode.
5. Runs euru_learning_engine.py only if preflight passes.

Usage:
    python euru_learning_preflight.py --root .
    python euru_learning_preflight.py --root . --strict-warnings
    python euru_learning_preflight.py --root . --dry-run-learning
    python euru_learning_preflight.py --root . --json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def _load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mandatory preflight before Euru learning engine.")
    parser.add_argument("--root", default=".", help="Path to Euru_TOS root")
    parser.add_argument("--validator", default="euru_schema_validator.py", help="Validator script name or path")
    parser.add_argument("--engine", default="euru_learning_engine.py", help="Learning engine script name or path")
    parser.add_argument("--strict-warnings", action="store_true", help="Block the learning engine when warnings exist")
    parser.add_argument("--write-report", action="store_true", help="Always write validation report")
    parser.add_argument("--json", action="store_true", help="Print structured JSON output")
    parser.add_argument("--dry-run-learning", action="store_true", help="Pass --dry-run to learning engine if preflight passes")
    parser.add_argument("--python-exe", default=sys.executable, help="Python executable used to run learning engine")
    return parser.parse_args()


def resolve_script(root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        return p
    return (root / p).resolve()


def write_preflight_report(root: Path, summary: Dict[str, Any], results: list[Any], status: str, reason: str, report_text: str) -> Path:
    output_dir = root / "08_DADOS_E_JOURNAL" / "SCORECARDS"
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_path = output_dir / f"LEARNING_PREFLIGHT_REPORT_{stamp}.md"

    lines = [
        "# EURU Learning Preflight Report",
        "",
        f"- generated_at: {datetime.now().astimezone().isoformat()}",
        f"- status: {status}",
        f"- reason: {reason}",
        f"- total_files: {summary.get('total_files', 0)}",
        f"- valid_files: {summary.get('valid_files', 0)}",
        f"- invalid_files: {summary.get('invalid_files', 0)}",
        f"- warning_count: {summary.get('warning_count', 0)}",
        f"- error_count: {summary.get('error_count', 0)}",
        "",
        "## Validator Summary",
        "",
        report_text.rstrip(),
        "",
        "## Preflight Decision",
        "",
        f"- status: **{status}**",
        f"- reason: {reason}",
        "",
        "## Blocking Rules Applied",
        "",
        "- Invalid schema files always block the learning engine.",
        "- Warnings block only when strict-warnings mode is enabled.",
        "- Learning may continue only when preflight reaches PASS or PASS_WITH_WARNINGS.",
        "",
    ]
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    validator_path = resolve_script(root, args.validator)
    engine_path = resolve_script(root, args.engine)

    if not validator_path.exists():
        raise SystemExit(f"Validator script not found: {validator_path}")
    if not engine_path.exists():
        raise SystemExit(f"Learning engine script not found: {engine_path}")

    validator = _load_module("euru_schema_validator_runtime", validator_path)

    files = validator.discover_markdown_files(root, None)
    results = [validator.validate_file(path) for path in files]
    summary = validator.summarize(results)
    report_text = validator.make_markdown_report(summary, results, root)

    has_errors = summary["invalid_files"] > 0 or summary["error_count"] > 0
    has_warnings = summary["warning_count"] > 0

    status = "PASS"
    reason = "Schema validation passed. Learning engine may run."
    if has_errors:
        status = "BLOCKED"
        reason = "Invalid schema files detected. Learning engine blocked to protect data integrity."
    elif has_warnings and args.strict_warnings:
        status = "BLOCKED"
        reason = "Warnings detected in strict-warnings mode. Learning engine blocked until reviewed."
    elif has_warnings:
        status = "PASS_WITH_WARNINGS"
        reason = "Schema validation passed with warnings. Learning engine may run, but review is recommended."

    should_write_report = args.write_report or has_errors or has_warnings
    report_path: Optional[Path] = None
    if should_write_report:
        report_path = write_preflight_report(root, summary, results, status, reason, report_text)

    payload = {
        "preflight": {
            "status": status,
            "reason": reason,
            "root": str(root),
            "validator": str(validator_path),
            "engine": str(engine_path),
            "strict_warnings": args.strict_warnings,
            "report_path": str(report_path) if report_path else None,
        },
        "validation_summary": summary,
        "validation_results": [
            {
                "file_path": r.file_path,
                "schema_type": r.schema_type,
                "valid": r.valid,
                "messages": [asdict(m) for m in r.messages],
            }
            for r in results
        ],
        "learning_engine": {
            "executed": False,
            "return_code": None,
            "stdout": "",
            "stderr": "",
        },
    }

    if status == "BLOCKED":
        if args.json:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(f"Preflight status: {status}")
            print(reason)
            if report_path:
                print(f"Report written to: {report_path}")
        return 1

    cmd = [args.python_exe, str(engine_path), "--root", str(root)]
    if args.dry_run_learning:
        cmd.append("--dry-run")

    proc = subprocess.run(cmd, capture_output=True, text=True)
    payload["learning_engine"] = {
        "executed": True,
        "return_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "command": cmd,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Preflight status: {status}")
        print(reason)
        if report_path:
            print(f"Report written to: {report_path}")
        print("Learning engine executed." if proc.returncode == 0 else "Learning engine executed with errors.")
        if proc.stdout.strip():
            print(proc.stdout.strip())
        if proc.stderr.strip():
            print(proc.stderr.strip(), file=sys.stderr)

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())

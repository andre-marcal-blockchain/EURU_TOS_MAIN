#!/usr/bin/env python3
"""Versioned governance threshold registry for Euru_TOS.

Features
--------
- Discover threshold profiles in 00_GOVERNANCA/THRESHOLDS
- Validate official threshold schema
- Resolve active profile by date/scope/profile_id
- Compare profile versions
- Generate markdown changelogs
- Emit JSON for integration with other agents
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to run euru_threshold_registry.py") from exc

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

ALLOWED_SCHEMA_TYPES = {"governance_threshold_profile", "governance_threshold_changelog"}
ALLOWED_SCOPES = {"system", "agent", "asset", "setup", "score_engine", "watchlist", "risk"}
ALLOWED_STATUSES = {"draft", "active", "deprecated", "archived"}
ALLOWED_APPROVAL = {"pending", "approved", "rejected"}

DEFAULT_DIR = Path("00_GOVERNANCA/THRESHOLDS")
PROFILES_DIRNAME = "PROFILES"
CHANGELOGS_DIRNAME = "CHANGELOGS"


@dataclass
class ValidationIssue:
    level: str
    message: str


@dataclass
class ThresholdProfile:
    path: Path
    data: Dict[str, Any]
    body: str
    issues: List[ValidationIssue]

    @property
    def is_valid(self) -> bool:
        return not any(i.level == "error" for i in self.issues)

    @property
    def scope(self) -> Optional[str]:
        return self.data.get("scope")

    @property
    def profile_id(self) -> Optional[str]:
        return self.data.get("profile_id")

    @property
    def version(self) -> Optional[str]:
        return self.data.get("version")

    @property
    def status(self) -> Optional[str]:
        return self.data.get("status")

    @property
    def effective_from(self) -> Optional[str]:
        return self.data.get("effective_from")

    @property
    def effective_to(self) -> Optional[str]:
        return self.data.get("effective_to")




def to_json_safe(value: Any) -> Any:
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: to_json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_json_safe(v) for v in value]
    return value

def load_markdown_with_front_matter(path: Path) -> Tuple[Optional[Dict[str, Any]], str, List[ValidationIssue]]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None, text, [ValidationIssue("error", "Missing YAML front matter")]
    front_matter_raw = match.group(1)
    body = text[match.end():].strip()
    try:
        data = yaml.safe_load(front_matter_raw) or {}
    except yaml.YAMLError as exc:
        return None, body, [ValidationIssue("error", f"Invalid YAML front matter: {exc}")]
    if not isinstance(data, dict):
        return None, body, [ValidationIssue("error", "Front matter must be a YAML mapping")]
    return data, body, []


def parse_semver(value: str) -> Optional[Tuple[int, int, int]]:
    m = SEMVER_RE.match(str(value))
    if not m:
        return None
    return tuple(int(x) for x in m.groups())


def parse_iso_date(value: Any) -> Optional[date]:
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or not ISO_DATE_RE.match(value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def flatten_dict(prefix: str, obj: Dict[str, Any], acc: Dict[str, Any]) -> None:
    for key, value in obj.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flatten_dict(path, value, acc)
        else:
            acc[path] = value


def validate_profile(data: Dict[str, Any], body: str) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []

    required = [
        "schema_type", "schema_version", "profile_id", "scope", "version", "status",
        "effective_from", "effective_to", "owner", "change_reason", "approval_status",
        "approved_by", "approval_date", "inherits_from", "supersedes_version",
        "thresholds", "notes_tags",
    ]
    for key in required:
        if key not in data:
            issues.append(ValidationIssue("error", f"Missing required field: {key}"))

    if data.get("schema_type") != "governance_threshold_profile":
        issues.append(ValidationIssue("error", "schema_type must be governance_threshold_profile"))

    scope = data.get("scope")
    if scope is not None and scope not in ALLOWED_SCOPES:
        issues.append(ValidationIssue("error", f"Invalid scope: {scope}"))

    status = data.get("status")
    if status is not None and status not in ALLOWED_STATUSES:
        issues.append(ValidationIssue("error", f"Invalid status: {status}"))

    approval = data.get("approval_status")
    if approval is not None and approval not in ALLOWED_APPROVAL:
        issues.append(ValidationIssue("error", f"Invalid approval_status: {approval}"))

    version = data.get("version")
    if version is not None and parse_semver(str(version)) is None:
        issues.append(ValidationIssue("error", f"Invalid semantic version: {version}"))

    eff_from = parse_iso_date(data.get("effective_from"))
    if data.get("effective_from") is not None and eff_from is None:
        issues.append(ValidationIssue("error", "effective_from must be ISO date YYYY-MM-DD"))

    eff_to_raw = data.get("effective_to")
    eff_to = parse_iso_date(eff_to_raw) if eff_to_raw is not None else None
    if eff_to_raw is not None and eff_to is None:
        issues.append(ValidationIssue("error", "effective_to must be null or ISO date YYYY-MM-DD"))
    if eff_from and eff_to and eff_to < eff_from:
        issues.append(ValidationIssue("error", "effective_to cannot be earlier than effective_from"))

    approval_date_raw = data.get("approval_date")
    approval_date = parse_iso_date(approval_date_raw) if approval_date_raw is not None else None
    if approval_date_raw is not None and approval_date is None:
        issues.append(ValidationIssue("error", "approval_date must be null or ISO date YYYY-MM-DD"))

    thresholds = data.get("thresholds")
    if thresholds is not None and not isinstance(thresholds, dict):
        issues.append(ValidationIssue("error", "thresholds must be a mapping"))
    elif isinstance(thresholds, dict):
        flat: Dict[str, Any] = {}
        flatten_dict("", thresholds, flat)
        if not flat:
            issues.append(ValidationIssue("error", "thresholds cannot be empty"))
        for key, value in flat.items():
            if not (is_number(value) or isinstance(value, bool) or value is None):
                issues.append(ValidationIssue("error", f"Threshold value must be numeric/boolean/null: {key}={value!r}"))

    notes_tags = data.get("notes_tags")
    if notes_tags is not None and not isinstance(notes_tags, list):
        issues.append(ValidationIssue("error", "notes_tags must be a list"))

    required_headings = [
        "# Profile Summary",
        "## Purpose",
        "## Threshold Rationale",
        "## Changes vs Previous Version",
        "## Expected Operational Impact",
        "## Human Governance Notes",
    ]
    for heading in required_headings:
        if heading not in body:
            issues.append(ValidationIssue("warning", f"Missing recommended heading: {heading}"))

    if data.get("approval_status") == "approved":
        if not data.get("approved_by"):
            issues.append(ValidationIssue("error", "approved profile requires approved_by"))
        if approval_date is None:
            issues.append(ValidationIssue("error", "approved profile requires approval_date"))

    return issues


def discover_profiles(root: Path) -> List[ThresholdProfile]:
    base = root / DEFAULT_DIR
    search_roots = [base / PROFILES_DIRNAME, base]
    seen: set[Path] = set()
    profiles: List[ThresholdProfile] = []
    for search_root in search_roots:
        if not search_root.exists():
            continue
        for path in sorted(search_root.rglob("THRESHOLDS_PROFILE_*.md")):
            if path in seen:
                continue
            seen.add(path)
            data, body, load_issues = load_markdown_with_front_matter(path)
            if data is None:
                profiles.append(ThresholdProfile(path=path, data={}, body=body, issues=load_issues))
                continue
            issues = load_issues + validate_profile(data, body)
            profiles.append(ThresholdProfile(path=path, data=data, body=body, issues=issues))
    return profiles


def group_profiles(profiles: Iterable[ThresholdProfile]) -> Dict[Tuple[str, str], List[ThresholdProfile]]:
    grouped: Dict[Tuple[str, str], List[ThresholdProfile]] = {}
    for p in profiles:
        key = (p.scope or "", p.profile_id or "")
        grouped.setdefault(key, []).append(p)
    for key in grouped:
        grouped[key].sort(key=lambda x: parse_semver(x.version or "0.0.0") or (0, 0, 0))
    return grouped


def validate_overlaps(profiles: List[ThresholdProfile]) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    grouped = group_profiles([p for p in profiles if p.is_valid])
    for (scope, profile_id), items in grouped.items():
        active_items = [p for p in items if p.status == "active"]
        for i, a in enumerate(active_items):
            a_from = parse_iso_date(a.effective_from)
            a_to = parse_iso_date(a.effective_to) or date.max
            for b in active_items[i + 1:]:
                b_from = parse_iso_date(b.effective_from)
                b_to = parse_iso_date(b.effective_to) or date.max
                if a_from and b_from and not (a_to < b_from or b_to < a_from):
                    issues.append(ValidationIssue(
                        "error",
                        f"Overlapping active profiles for {scope}/{profile_id}: {a.path.name} and {b.path.name}",
                    ))
    return issues


def resolve_active_profile(
    profiles: List[ThresholdProfile],
    scope: str,
    profile_id: str,
    on_date: date,
) -> Optional[ThresholdProfile]:
    matches: List[ThresholdProfile] = []
    for p in profiles:
        if not p.is_valid or p.scope != scope or p.profile_id != profile_id or p.status != "active":
            continue
        eff_from = parse_iso_date(p.effective_from)
        eff_to = parse_iso_date(p.effective_to) or date.max
        if eff_from and eff_from <= on_date <= eff_to:
            matches.append(p)
    matches.sort(key=lambda p: parse_semver(p.version or "0.0.0") or (0, 0, 0), reverse=True)
    return matches[0] if matches else None


def compare_profiles(old: ThresholdProfile, new: ThresholdProfile) -> Dict[str, Any]:
    old_flat: Dict[str, Any] = {}
    new_flat: Dict[str, Any] = {}
    flatten_dict("", old.data.get("thresholds", {}), old_flat)
    flatten_dict("", new.data.get("thresholds", {}), new_flat)

    old_keys = set(old_flat)
    new_keys = set(new_flat)

    added = {k: new_flat[k] for k in sorted(new_keys - old_keys)}
    removed = {k: old_flat[k] for k in sorted(old_keys - new_keys)}
    changed = {}
    for key in sorted(old_keys & new_keys):
        if old_flat[key] != new_flat[key]:
            changed[key] = {"old": old_flat[key], "new": new_flat[key]}

    return {
        "scope": new.scope,
        "profile_id": new.profile_id,
        "from_version": old.version,
        "to_version": new.version,
        "added": added,
        "removed": removed,
        "changed": changed,
        "summary": {
            "added_keys_count": len(added),
            "removed_keys_count": len(removed),
            "changed_keys_count": len(changed),
        },
    }


def generate_changelog_markdown(diff: Dict[str, Any], impact_level: str = "medium") -> str:
    today = date.today().isoformat()
    added = diff["added"]
    removed = diff["removed"]
    changed = diff["changed"]
    lines = [
        "---",
        "schema_type: governance_threshold_changelog",
        "schema_version: 1.0",
        "",
        f"profile_id: {diff['profile_id']}",
        f"scope: {diff['scope']}",
        f"from_version: {diff['from_version']}",
        f"to_version: {diff['to_version']}",
        f"change_date: {today}",
        "",
        "generated_by: euru_threshold_registry.py",
        "approval_status: pending",
        f"impact_level: {impact_level}",
        "",
        f"changed_keys_count: {diff['summary']['changed_keys_count']}",
        f"added_keys_count: {diff['summary']['added_keys_count']}",
        f"removed_keys_count: {diff['summary']['removed_keys_count']}",
        "---",
        "",
        "# Change Summary",
        "",
        "## Version Transition",
        f"- from {diff['from_version']} to {diff['to_version']}",
        "",
        "## Added Keys",
    ]
    if added:
        for key, value in added.items():
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- none")

    lines.extend(["", "## Removed Keys"])
    if removed:
        for key, value in removed.items():
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- none")

    lines.extend(["", "## Changed Values"])
    if changed:
        for key, payload in changed.items():
            lines.append(f"- `{key}`: {payload['old']} -> {payload['new']}")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Governance Interpretation",
        "- pending human interpretation",
        "",
        "## Human Approval Notes",
        "- pending",
        "",
    ])
    return "\n".join(lines)


def write_changelog(root: Path, diff: Dict[str, Any], impact_level: str = "medium") -> Path:
    changelog_dir = root / DEFAULT_DIR / CHANGELOGS_DIRNAME
    changelog_dir.mkdir(parents=True, exist_ok=True)
    from_v = diff["from_version"]
    to_v = diff["to_version"]
    filename = f"THRESHOLDS_CHANGELOG_{diff['scope']}_{diff['profile_id']}_v{from_v}_to_v{to_v}.md"
    path = changelog_dir / filename
    path.write_text(generate_changelog_markdown(diff, impact_level=impact_level), encoding="utf-8")
    return path


def cmd_list(args: argparse.Namespace) -> int:
    profiles = discover_profiles(args.root)
    issues = validate_overlaps(profiles)
    payload = {
        "profiles": [
            {
                "file": str(p.path.relative_to(args.root)),
                "scope": p.scope,
                "profile_id": p.profile_id,
                "version": p.version,
                "status": p.status,
                "effective_from": p.effective_from,
                "effective_to": p.effective_to,
                "valid": p.is_valid,
                "issues": [{"level": i.level, "message": i.message} for i in p.issues],
            }
            for p in profiles
        ],
        "global_issues": [{"level": i.level, "message": i.message} for i in issues],
    }
    print(json.dumps(to_json_safe(payload), indent=2))
    return 1 if any(i.level == "error" for i in issues) else 0


def cmd_validate(args: argparse.Namespace) -> int:
    profiles = discover_profiles(args.root)
    issues = validate_overlaps(profiles)
    has_errors = False
    for p in profiles:
        print(f"[{ 'OK' if p.is_valid else 'ERROR' }] {p.path.relative_to(args.root)}")
        for issue in p.issues:
            print(f"  - {issue.level.upper()}: {issue.message}")
        has_errors = has_errors or not p.is_valid
    for issue in issues:
        print(f"GLOBAL {issue.level.upper()}: {issue.message}")
        has_errors = has_errors or issue.level == "error"
    return 1 if has_errors else 0


def cmd_active(args: argparse.Namespace) -> int:
    profiles = discover_profiles(args.root)
    issues = validate_overlaps(profiles)
    if any(i.level == "error" for i in issues):
        print(json.dumps({"status": "blocked", "issues": [i.message for i in issues]}, indent=2))
        return 1
    on_date = parse_iso_date(args.date) or date.today()
    profile = resolve_active_profile(profiles, args.scope, args.profile_id, on_date)
    payload = {
        "date": on_date.isoformat(),
        "scope": args.scope,
        "profile_id": args.profile_id,
        "found": profile is not None,
        "profile": None if profile is None else {
            "file": str(profile.path.relative_to(args.root)),
            "version": profile.version,
            "status": profile.status,
            "effective_from": profile.effective_from,
            "effective_to": profile.effective_to,
            "thresholds": profile.data.get("thresholds", {}),
        },
    }
    print(json.dumps(to_json_safe(payload), indent=2))
    return 0 if profile else 1


def select_profile_by_version(profiles: List[ThresholdProfile], scope: str, profile_id: str, version: str) -> Optional[ThresholdProfile]:
    for p in profiles:
        if p.is_valid and p.scope == scope and p.profile_id == profile_id and p.version == version:
            return p
    return None


def cmd_compare(args: argparse.Namespace) -> int:
    profiles = discover_profiles(args.root)
    old = select_profile_by_version(profiles, args.scope, args.profile_id, args.from_version)
    new = select_profile_by_version(profiles, args.scope, args.profile_id, args.to_version)
    if not old or not new:
        print(json.dumps({
            "status": "error",
            "message": "Could not find both profile versions",
        }, indent=2))
        return 1
    diff = compare_profiles(old, new)
    if args.write_changelog:
        path = write_changelog(args.root, diff, impact_level=args.impact_level)
        diff["changelog_path"] = str(path.relative_to(args.root))
    print(json.dumps(to_json_safe(diff), indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Euru governance threshold registry")
    parser.add_argument("--root", type=Path, default=Path("."), help="Root of Euru_TOS")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List threshold profiles")
    sub.add_parser("validate", help="Validate threshold profiles")

    active = sub.add_parser("active", help="Resolve active profile for a date")
    active.add_argument("--scope", required=True)
    active.add_argument("--profile-id", required=True)
    active.add_argument("--date", required=False)

    compare = sub.add_parser("compare", help="Compare two profile versions")
    compare.add_argument("--scope", required=True)
    compare.add_argument("--profile-id", required=True)
    compare.add_argument("--from-version", required=True)
    compare.add_argument("--to-version", required=True)
    compare.add_argument("--write-changelog", action="store_true")
    compare.add_argument("--impact-level", default="medium")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.root = args.root.resolve()

    if args.command == "list":
        return cmd_list(args)
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "active":
        return cmd_active(args)
    if args.command == "compare":
        return cmd_compare(args)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())

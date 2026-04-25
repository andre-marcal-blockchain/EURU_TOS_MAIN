"""
Euru OS — Daily + Weekly Audit
==============================
Read-only audit script that verifies system health across 8 dimensions.
Sends email only on anomalies (daily) or always (weekly).

Governance: Type 2 — approved 2026-04-21, cooling-off completed.
Proposal:   DECISOES_ESTRATEGICAS_REVISADO.md entry 2026-04-20.

Daily mode (08:30 every day):
  - 8 checks, each returning PASS/WARN/FAIL/INFO
  - Email only if >=1 FAIL or >=3 WARN
  - Report: AUDIT_REPORTS/DAILY_AUDIT_REPORT_YYYY-MM-DD.md

Weekly mode (Saturdays 09:00):
  - Consolidates last 7 daily audits
  - Stats: trades opened/closed, P&L, anomaly counts
  - Manual "Aprendizado" field for human reflection
  - Email always sent
  - Report: AUDIT_REPORTS/WEEKLY_AUDIT_REPORT_YYYY-W##.md

Usage:
  python euru_daily_audit.py                 # daily mode (default)
  python euru_daily_audit.py --mode daily
  python euru_daily_audit.py --mode weekly
  python euru_daily_audit.py --dry-run       # don't send email, don't write report
"""

import os
import sys
import re
import glob
import json
import argparse
import datetime
import smtplib
import ssl
import subprocess
from email.message import EmailMessage

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCORECARDS_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "SCORECARDS")
TRADES_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "JOURNAL_TRADES")
JOURNAL_DAILY_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "JOURNAL_DAILY")
AUDIT_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "AUDIT_REPORTS")
ENV_PATH = r"C:\Users\andre\.euru_secrets\euru.env"

# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------

def load_config():
    """Load email credentials from .env file outside the Git repo."""
    if not os.path.exists(ENV_PATH):
        return None
    config = {}
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            config[k.strip()] = v.strip()
    return config


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def read_file_safe(path):
    """Try multiple encodings to read a file."""
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception:
            return None, None
    return None, None


def has_bom(path):
    """Check if file starts with UTF-8 BOM."""
    try:
        with open(path, "rb") as f:
            return f.read(3) == b"\xef\xbb\xbf"
    except Exception:
        return False


def parse_yaml_front_matter(content):
    """Extract YAML front matter as dict."""
    if not content:
        return None
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    yaml_text = match.group(1)
    result = {}
    for line in yaml_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if v in ("null", ""):
                result[k] = None
            elif v == "true":
                result[k] = True
            elif v == "false":
                result[k] = False
            else:
                try:
                    result[k] = float(v) if "." in v else int(v)
                except ValueError:
                    result[k] = v.strip("'\"")
    return result


def run_git(args):
    """Run git command and return stdout, stderr, returncode."""
    try:
        result = subprocess.run(
            ["git"] + args, cwd=SCRIPT_DIR, capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), -1


# ---------------------------------------------------------------------------
# Check functions — each returns (status, details)
# status: PASS | WARN | FAIL | INFO
# ---------------------------------------------------------------------------

def check_morning_scan(today_str):
    path = os.path.join(SCORECARDS_DIR, f"SCOUT_REPORT_{today_str}.md")
    if os.path.exists(path):
        return ("PASS", f"SCOUT_REPORT_{today_str}.md exists")
    return ("FAIL", f"Missing SCOUT_REPORT_{today_str}.md — morning scan did not run today")


def check_asian_scan(today_str):
    path = os.path.join(SCORECARDS_DIR, f"ASIAN_REPORT_{today_str}.md")
    if os.path.exists(path):
        return ("PASS", f"ASIAN_REPORT_{today_str}.md exists")
    return ("FAIL", f"Missing ASIAN_REPORT_{today_str}.md — asian scan did not run today")


def check_trade_monitor(today_str):
    path = os.path.join(SCORECARDS_DIR, f"TRADE_MONITOR_REPORT_{today_str}.md")
    if os.path.exists(path):
        return ("PASS", f"TRADE_MONITOR_REPORT_{today_str}.md exists")
    return ("WARN", f"Missing TRADE_MONITOR_REPORT_{today_str}.md — trade monitor did not run")


def check_git_sync():
    # Check if any uncommitted changes
    stdout, _, rc = run_git(["status", "--porcelain"])
    if rc != 0:
        return ("FAIL", "git status failed — not a git repo or git unavailable")
    # Fetch latest refs
    run_git(["fetch", "origin", "main"])
    # Check local ahead
    ahead_out, _, _ = run_git(["rev-list", "--count", "origin/main..HEAD"])
    behind_out, _, _ = run_git(["rev-list", "--count", "HEAD..origin/main"])
    try:
        ahead = int(ahead_out or "0")
        behind = int(behind_out or "0")
    except ValueError:
        ahead = behind = 0
    msgs = []
    if ahead > 0:
        msgs.append(f"{ahead} local commit(s) not pushed")
    if behind > 0:
        msgs.append(f"{behind} remote commit(s) not pulled")
    if msgs:
        return ("WARN", " | ".join(msgs))
    return ("PASS", "Git synchronized with origin/main")


def check_schema_integrity():
    """Check PAPER_TRADE, JOURNAL, LEARNING_REPORT, SCORECARD files for valid YAML."""
    patterns = [
        os.path.join(TRADES_DIR, "PAPER_TRADE_*.md"),
        os.path.join(JOURNAL_DAILY_DIR, "JOURNAL_*.md"),
        os.path.join(SCORECARDS_DIR, "LEARNING_REPORT_*.md"),
        os.path.join(SCORECARDS_DIR, "SCORECARDS", "SCORECARD_*.md"),
    ]
    invalid = []
    checked = 0
    for pat in patterns:
        for f in glob.glob(pat):
            checked += 1
            content, _ = read_file_safe(f)
            if content is None:
                invalid.append(f"{os.path.basename(f)}: cannot read")
                continue
            fm = parse_yaml_front_matter(content)
            if fm is None:
                invalid.append(f"{os.path.basename(f)}: missing YAML front matter")
                continue
            if "schema_type" not in fm:
                invalid.append(f"{os.path.basename(f)}: missing schema_type field")
    if not invalid:
        return ("PASS", f"All {checked} critical files have valid schema")
    if len(invalid) <= 2:
        return ("WARN", f"{len(invalid)}/{checked} invalid: " + " | ".join(invalid))
    return ("FAIL", f"{len(invalid)}/{checked} invalid: " + " | ".join(invalid[:3]) + " ...")


def check_open_trades():
    """Check if any open trade has been open >7 days (time stop violation)."""
    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    trade_files = glob.glob(os.path.join(TRADES_DIR, "PAPER_TRADE_*.md"))
    open_trades = []
    for f in trade_files:
        content, _ = read_file_safe(f)
        if not content:
            continue
        fm = parse_yaml_front_matter(content)
        if not fm or fm.get("status") != "open":
            continue
        entry_dt_str = fm.get("entry_datetime")
        days = None
        if entry_dt_str:
            try:
                dt = datetime.datetime.fromisoformat(str(entry_dt_str).replace("Z", "+00:00"))
                if dt.tzinfo:
                    dt = dt.replace(tzinfo=None)
                days = (now - dt).days
            except Exception:
                days = None
        open_trades.append({
            "id": fm.get("trade_id", "?"),
            "symbol": fm.get("symbol", "?"),
            "days": days,
        })
    if not open_trades:
        return ("PASS", "No open trades")
    expired = [t for t in open_trades if t["days"] is not None and t["days"] >= 7]
    if expired:
        details = ", ".join([f"{t['id']} {t['symbol']} ({t['days']}d)" for t in expired])
        return ("FAIL", f"{len(expired)} trade(s) past time_stop: {details}")
    details = ", ".join([f"{t['id']} {t['symbol']} ({t['days']}d)" for t in open_trades])
    return ("PASS", f"{len(open_trades)} open trade(s) within time_stop: {details}")


def check_encoding():
    """Check critical files for BOM or encoding issues."""
    patterns = [
        os.path.join(TRADES_DIR, "PAPER_TRADE_*.md"),
        os.path.join(JOURNAL_DAILY_DIR, "JOURNAL_*.md"),
    ]
    issues = []
    checked = 0
    for pat in patterns:
        for f in glob.glob(pat):
            checked += 1
            if has_bom(f):
                issues.append(f"{os.path.basename(f)}: has BOM")
                continue
            _, enc = read_file_safe(f)
            if enc not in ("utf-8", "utf-8-sig"):
                issues.append(f"{os.path.basename(f)}: encoding={enc}")
    if not issues:
        return ("PASS", f"All {checked} critical files UTF-8 clean")
    if len(issues) <= 2:
        return ("WARN", " | ".join(issues))
    return ("FAIL", f"{len(issues)} encoding issues: " + " | ".join(issues[:3]) + " ...")


def check_news_streak():
    """Info-only: count consecutive days with HIGH severity news."""
    scout_files = sorted(
        glob.glob(os.path.join(SCORECARDS_DIR, "SCOUT_REPORT_*.md")),
        reverse=True,
    )
    streak = 0
    for f in scout_files[:10]:
        content, _ = read_file_safe(f)
        if not content:
            break
        # Look for severity marker
        if "OVERALL_SEVERITY: HIGH" in content or "Overall severity: (!) HIGH" in content:
            streak += 1
        else:
            break
    if streak >= 5:
        return ("INFO", f"News Sentinel HIGH for {streak} consecutive days — Rule 8 active")
    return ("INFO", f"News Sentinel HIGH streak: {streak} day(s)")


# ---------------------------------------------------------------------------
# Daily report
# ---------------------------------------------------------------------------

def run_daily_checks(today_str):
    """Run all 8 checks and return list of (name, status, details)."""
    checks = [
        ("Morning Scan", *check_morning_scan(today_str)),
        ("Asian Scan", *check_asian_scan(today_str)),
        ("Trade Monitor", *check_trade_monitor(today_str)),
        ("Git Sync", *check_git_sync()),
        ("Schema Integrity", *check_schema_integrity()),
        ("Open Trades Health", *check_open_trades()),
        ("Encoding Check", *check_encoding()),
        ("News Sentinel Streak", *check_news_streak()),
    ]
    return checks


def summarize(checks):
    fails = sum(1 for _, s, _ in checks if s == "FAIL")
    warns = sum(1 for _, s, _ in checks if s == "WARN")
    passes = sum(1 for _, s, _ in checks if s == "PASS")
    infos = sum(1 for _, s, _ in checks if s == "INFO")
    return {"FAIL": fails, "WARN": warns, "PASS": passes, "INFO": infos}


def generate_daily_report(today_str, checks, summary):
    lines = [
        "---",
        "schema_type: daily_audit",
        "schema_version: 1.0",
        f"audit_date: '{today_str}'",
        f"fails: {summary['FAIL']}",
        f"warns: {summary['WARN']}",
        f"passes: {summary['PASS']}",
        "---",
        "",
        f"# Euru OS — Daily Audit Report",
        f"**Date:** {today_str}",
        f"**Fails:** {summary['FAIL']} | **Warns:** {summary['WARN']} | **Passes:** {summary['PASS']}",
        "",
        "## Check Results",
        "",
        "| # | Check | Status | Details |",
        "|---|---|---|---|",
    ]
    for i, (name, status, details) in enumerate(checks, 1):
        lines.append(f"| {i} | {name} | **{status}** | {details} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by euru_daily_audit.py — Euru OS SIMULATE phase*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Weekly report
# ---------------------------------------------------------------------------

def generate_weekly_report(week_str, start_date, end_date, daily_summaries, trade_stats):
    lines = [
        "---",
        "schema_type: weekly_audit",
        "schema_version: 1.0",
        f"audit_week: '{week_str}'",
        f"period_start: '{start_date}'",
        f"period_end: '{end_date}'",
        "---",
        "",
        f"# Euru OS — Weekly Audit Report {week_str}",
        f"**Period:** {start_date} to {end_date}",
        "",
        "## Week at a Glance",
        "",
        "| Day | Fails | Warns | Passes | Status |",
        "|---|---:|---:|---:|---|",
    ]
    total_fails = total_warns = 0
    for ds in daily_summaries:
        date = ds["date"]
        if ds["found"]:
            f = ds["fails"]
            w = ds["warns"]
            p = ds["passes"]
            status = "🔴" if f > 0 else ("🟡" if w >= 3 else "🟢")
            total_fails += f
            total_warns += w
        else:
            f = w = p = "-"
            status = "⚫ MISSING"
        lines.append(f"| {date} | {f} | {w} | {p} | {status} |")
    lines.append("")
    lines.append("## Trade Statistics")
    lines.append("")
    lines.append(f"- **Opened this week:** {trade_stats['opened']}")
    lines.append(f"- **Closed this week:** {trade_stats['closed']}")
    lines.append(f"- **Total P&L:** {trade_stats['pnl']} USDT")
    lines.append(f"- **Win rate:** {trade_stats['win_rate']}")
    lines.append("")
    lines.append("## Anomalies Detected")
    lines.append("")
    anomalies = [ds for ds in daily_summaries if ds["found"] and (ds["fails"] > 0 or ds["warns"] >= 3)]
    if not anomalies:
        lines.append("No anomalies detected this week. Clean run.")
    else:
        for ds in anomalies:
            lines.append(f"### {ds['date']}")
            for name, status, details in ds["checks"]:
                if status in ("FAIL", "WARN"):
                    lines.append(f"- **[{status}] {name}:** {details}")
            lines.append("")
    lines.append("")
    lines.append("## Aprendizado da Semana")
    lines.append("")
    lines.append("[PREENCHER MANUALMENTE — esta secção é para reflectires sobre o que a semana te ensinou sobre o sistema e o mercado. O script não preenche isto automaticamente.]")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by euru_daily_audit.py --mode weekly — Euru OS SIMULATE phase*")
    return "\n".join(lines)


def collect_daily_summaries(end_date, days=7):
    """Read last N daily audit reports."""
    summaries = []
    for i in range(days - 1, -1, -1):
        date = end_date - datetime.timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        path = os.path.join(AUDIT_DIR, f"DAILY_AUDIT_REPORT_{date_str}.md")
        if not os.path.exists(path):
            summaries.append({"date": date_str, "found": False})
            continue
        content, _ = read_file_safe(path)
        fm = parse_yaml_front_matter(content) if content else None
        if not fm:
            summaries.append({"date": date_str, "found": False})
            continue
        # Re-parse checks from table
        checks = []
        for line in content.split("\n"):
            m = re.match(r"\|\s*\d+\s*\|\s*(.+?)\s*\|\s*\*\*(PASS|WARN|FAIL|INFO)\*\*\s*\|\s*(.+?)\s*\|", line)
            if m:
                checks.append((m.group(1), m.group(2), m.group(3)))
        summaries.append({
            "date": date_str,
            "found": True,
            "fails": fm.get("fails", 0),
            "warns": fm.get("warns", 0),
            "passes": fm.get("passes", 0),
            "checks": checks,
        })
    return summaries


def compute_trade_stats(start_date, end_date):
    """Compute trade statistics for the week."""
    trade_files = glob.glob(os.path.join(TRADES_DIR, "PAPER_TRADE_*.md"))
    opened = closed = 0
    pnl = 0.0
    wins = 0
    for f in trade_files:
        content, _ = read_file_safe(f)
        if not content:
            continue
        fm = parse_yaml_front_matter(content)
        if not fm:
            continue
        # Check entry date
        entry_str = fm.get("entry_datetime")
        if entry_str:
            try:
                edt = datetime.datetime.fromisoformat(str(entry_str).replace("Z", "+00:00")).replace(tzinfo=None).date()
                if start_date <= edt <= end_date:
                    opened += 1
            except Exception:
                pass
        # Check exit date
        exit_str = fm.get("exit_datetime")
        if exit_str and fm.get("status") == "closed":
            try:
                xdt = datetime.datetime.fromisoformat(str(exit_str).replace("Z", "+00:00")).replace(tzinfo=None).date()
                if start_date <= xdt <= end_date:
                    closed += 1
                    p = fm.get("pnl_usdt", 0) or 0
                    pnl += float(p)
                    if float(p) > 0:
                        wins += 1
            except Exception:
                pass
    win_rate = f"{(wins/closed*100):.0f}%" if closed > 0 else "n/a"
    return {"opened": opened, "closed": closed, "pnl": round(pnl, 2), "win_rate": win_rate}


# ---------------------------------------------------------------------------
# Email sender
# ---------------------------------------------------------------------------

def send_email(config, subject, body):
    """Send email via Gmail SMTP."""
    if not config:
        print("  [audit] Email config not loaded — email not sent")
        return False
    required = ("EURU_EMAIL_FROM", "EURU_EMAIL_TO", "EURU_SMTP_HOST", "EURU_SMTP_PORT", "EURU_SMTP_PASSWORD")
    for k in required:
        if k not in config or not config[k]:
            print(f"  [audit] Missing config {k} — email not sent")
            return False
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config["EURU_EMAIL_FROM"]
    msg["To"] = config["EURU_EMAIL_TO"]
    msg.set_content(body)
    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP(config["EURU_SMTP_HOST"], int(config["EURU_SMTP_PORT"])) as s:
            s.starttls(context=ctx)
            s.login(config["EURU_EMAIL_FROM"], config["EURU_SMTP_PASSWORD"])
            s.send_message(msg)
        print(f"  [audit] Email sent: {subject}")
        return True
    except Exception as e:
        print(f"  [audit] Email error: {e}")
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Euru OS Daily/Weekly Audit")
    parser.add_argument("--mode", choices=["daily", "weekly"], default="daily")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    today_str = now.strftime("%Y-%m-%d")

    os.makedirs(AUDIT_DIR, exist_ok=True)
    config = load_config()

    if args.mode == "daily":
        print(f"\nEuru OS — Daily Audit [{today_str}]")
        if args.dry_run:
            print("Mode: DRY-RUN")

        checks = run_daily_checks(today_str)
        summary = summarize(checks)

        print(f"\n  Results: FAIL={summary['FAIL']} WARN={summary['WARN']} PASS={summary['PASS']} INFO={summary['INFO']}")
        for name, status, details in checks:
            print(f"  [{status}] {name}: {details}")

        report = generate_daily_report(today_str, checks, summary)
        if not args.dry_run:
            path = os.path.join(AUDIT_DIR, f"DAILY_AUDIT_REPORT_{today_str}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\n  Report saved: {path}")

        # Email logic: FAIL>=1 or WARN>=3
        if summary["FAIL"] >= 1 or summary["WARN"] >= 3:
            severity = "CRITICAL" if summary["FAIL"] >= 1 else "WARNING"
            subject = f"[Euru OS] Daily Audit {today_str} — {summary['FAIL']} FAIL, {summary['WARN']} WARN"
            body_lines = [
                f"Euru OS Daily Audit — {today_str}",
                f"Severity: {severity}",
                "",
                f"Results: FAIL={summary['FAIL']} WARN={summary['WARN']} PASS={summary['PASS']}",
                "",
                "Detailed findings:",
                "",
            ]
            for name, status, details in checks:
                if status in ("FAIL", "WARN"):
                    body_lines.append(f"  [{status}] {name}")
                    body_lines.append(f"    {details}")
                    body_lines.append("")
            body_lines.append("---")
            body_lines.append(f"Full report: AUDIT_REPORTS/DAILY_AUDIT_REPORT_{today_str}.md")
            if not args.dry_run:
                send_email(config, subject, "\n".join(body_lines))
            else:
                print(f"  [audit] DRY-RUN: would send email with subject '{subject}'")
        else:
            print("  [audit] All clean — no email sent")

    else:  # weekly
        # Compute week range (last 7 days ending today)
        end_date = now.date()
        start_date = end_date - datetime.timedelta(days=6)
        week_str = end_date.strftime("%Y-W%V")

        print(f"\nEuru OS — Weekly Audit [{week_str}]")
        print(f"Period: {start_date} to {end_date}")
        if args.dry_run:
            print("Mode: DRY-RUN")

        daily_summaries = collect_daily_summaries(end_date, days=7)
        trade_stats = compute_trade_stats(start_date, end_date)

        report = generate_weekly_report(week_str, start_date, end_date, daily_summaries, trade_stats)

        if not args.dry_run:
            path = os.path.join(AUDIT_DIR, f"WEEKLY_AUDIT_REPORT_{week_str}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\n  Report saved: {path}")

        total_fails = sum(ds.get("fails", 0) for ds in daily_summaries if ds["found"])
        total_warns = sum(ds.get("warns", 0) for ds in daily_summaries if ds["found"])
        missing_days = sum(1 for ds in daily_summaries if not ds["found"])

        subject_tag = "Clean week" if (total_fails == 0 and total_warns == 0) else f"{total_fails} FAIL, {total_warns} WARN"
        subject = f"[Euru OS] Weekly Audit {week_str} — {subject_tag}"

        body_lines = [
            f"Euru OS Weekly Audit — {week_str}",
            f"Period: {start_date} to {end_date}",
            "",
            f"Summary:",
            f"  Total FAILs: {total_fails}",
            f"  Total WARNs: {total_warns}",
            f"  Missing daily reports: {missing_days}",
            "",
            f"Trade stats:",
            f"  Opened: {trade_stats['opened']}",
            f"  Closed: {trade_stats['closed']}",
            f"  P&L: {trade_stats['pnl']} USDT",
            f"  Win rate: {trade_stats['win_rate']}",
            "",
            "Full report in AUDIT_REPORTS/WEEKLY_AUDIT_REPORT_" + week_str + ".md",
            "",
            "Remember to fill the 'Aprendizado da Semana' section manually.",
        ]
        if not args.dry_run:
            send_email(config, subject, "\n".join(body_lines))
        else:
            print(f"  [audit] DRY-RUN: would send email with subject '{subject}'")


if __name__ == "__main__":
    main()
    # Trigger git sync after report
    try:
        from euru_git_sync import git_sync
        git_sync("audit report")
    except Exception as _e:
        print(f"[git-sync] Skipped: {_e}")

"""
Euru OS — Journal Auditor (AGT-07)
Automatically creates a daily journal entry by reading the most recent
Scout Report and Asian Report, summarising open positions, and writing
a schema-compliant JOURNAL_<date>.md to 08_DADOS_E_JOURNAL/JOURNAL_DAILY/.

Designed to run automatically at the end of each operational session,
after the Morning Scan and Asian Scan have completed.

Usage:
    python euru_journal_auditor.py                  # journals today
    python euru_journal_auditor.py --date 2026-04-13
    python euru_journal_auditor.py --dry-run         # print without writing
    python euru_journal_auditor.py --cycle morning   # tag cycle
    python euru_journal_auditor.py --cycle asian

Output:
    08_DADOS_E_JOURNAL/JOURNAL_DAILY/JOURNAL_<YYYY-MM-DD>.md
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(os.path.dirname(os.path.abspath(__file__)))
SCORECARDS  = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "SCORECARDS"
TRADES_DIR  = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "JOURNAL_TRADES"
JOURNAL_DIR = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "JOURNAL_DAILY"
SYSTEM_PHASE = "simulate"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def find_latest_report(prefix: str, date: str) -> Optional[Path]:
    """Find most recent report of a given prefix on or before date."""
    pattern = str(SCORECARDS / f"{prefix}_*.md")
    files = sorted(glob.glob(pattern))
    # Filter: only files with date <= target date
    candidates = []
    for f in files:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", Path(f).name)
        if m and m.group(1) <= date:
            candidates.append(Path(f))
    return candidates[-1] if candidates else None


def extract_btc_state(scout_path: Optional[Path]) -> str:
    """Extract BTC trend from scout report."""
    if not scout_path or not scout_path.exists():
        return "neutral"
    content = scout_path.read_text(encoding="utf-8")
    # Look for BTC master filter state
    m = re.search(r"BTC.*?(?:BULLISH|BEARISH|SIDEWAYS|NO_TRADE)", content, re.IGNORECASE)
    if m:
        text = m.group(0).upper()
        if "BULLISH" in text:
            return "bullish"
        if "BEARISH" in text:
            return "bearish"
    return "neutral"


def extract_market_regime(scout_path: Optional[Path]) -> str:
    """Infer market regime from scout report."""
    if not scout_path or not scout_path.exists():
        return "unclear"
    content = scout_path.read_text(encoding="utf-8")
    bullish = len(re.findall(r"\bBULLISH\b", content))
    bearish = len(re.findall(r"\bBEARISH\b", content))
    setup   = len(re.findall(r"\bSETUP\b", content))
    no_trade = len(re.findall(r"\bNO_TRADE\b", content))
    if bullish > bearish * 2 and setup > 2:
        return "bull_trend"
    if bearish > bullish * 2 or no_trade > setup:
        return "bear_trend"
    if "COMPRESS" in content.upper() or "LATERAL" in content.upper():
        return "range"
    return "unclear"


def extract_news_severity(scout_path: Optional[Path]) -> str:
    """Extract max news severity from scout report."""
    if not scout_path or not scout_path.exists():
        return "none"
    content = scout_path.read_text(encoding="utf-8").upper()
    if "CRITICAL" in content:
        return "critical"
    if "HIGH" in content and "NEWS" in content:
        return "high"
    if "MEDIUM" in content and "NEWS" in content:
        return "medium"
    if "LOW" in content and "NEWS" in content:
        return "low"
    return "none"


def count_open_positions() -> int:
    """Count open paper trades."""
    count = 0
    if not TRADES_DIR.exists():
        return 0
    for f in TRADES_DIR.glob("PAPER_TRADE_*.md"):
        content = f.read_text(encoding="utf-8")
        if re.search(r"^status:\s*open", content, re.MULTILINE):
            count += 1
    return count


def extract_setups_from_scout(scout_path: Optional[Path]) -> list[str]:
    """Extract SETUP signals from scout report."""
    if not scout_path or not scout_path.exists():
        return []
    content = scout_path.read_text(encoding="utf-8")
    setups = re.findall(r"\|\s*(\w+USDT)\s*\|[^|]*\|\s*\*\*SETUP\*\*", content)
    return setups


def extract_gem_alerts_from_asian(asian_path: Optional[Path]) -> list[str]:
    """Extract GEM_ALERT signals from asian report."""
    if not asian_path or not asian_path.exists():
        return []
    content = asian_path.read_text(encoding="utf-8")
    gems = re.findall(r"\|\s*(\w+USDT)\s*\|[^|]*GEM_ALERT", content)
    return gems


def determine_key_theme(
    btc_state: str,
    regime: str,
    news_severity: str,
    setups: list,
    open_positions: int,
) -> str:
    """Determine the key theme of the day."""
    if news_severity in ("high", "critical"):
        return "risk_management"
    if btc_state == "bearish" or regime == "bear_trend":
        return "capital_preservation"
    if open_positions > 0 and not setups:
        return "position_monitoring"
    if setups:
        return "setup_identification"
    if regime == "range":
        return "patience"
    return "discipline"


def build_observations(
    date: str,
    cycle: str,
    scout_path: Optional[Path],
    asian_path: Optional[Path],
    setups: list,
    gems: list,
    btc_state: str,
    regime: str,
    news_severity: str,
    open_positions: int,
) -> str:
    """Build the observations section."""
    lines = []

    # Scout summary
    if scout_path:
        lines.append(f"- Morning Scan executado: {scout_path.name}")
        lines.append(f"- BTC macro state: {btc_state.upper()}")
        lines.append(f"- Market regime: {regime}")
        if setups:
            lines.append(f"- Setups identificados pelo Scout: {', '.join(setups)}")
        else:
            lines.append("- Nenhum setup identificado pelo Scout neste ciclo.")
    else:
        lines.append("- Morning Scan não encontrado para hoje.")

    # Asian summary
    if asian_path:
        lines.append(f"- Asian Scan executado: {asian_path.name}")
        if gems:
            lines.append(f"- GEM_ALERTs identificados: {', '.join(gems)}")
        else:
            lines.append("- Nenhum GEM_ALERT na sessão asiática.")
    else:
        if cycle == "asian":
            lines.append("- Asian Scan não encontrado para hoje.")

    # News
    lines.append(f"- News severity máxima: {news_severity.upper()}")

    # Positions
    if open_positions > 0:
        lines.append(f"- Posições abertas activas: {open_positions}")
    else:
        lines.append("- Nenhuma posição aberta neste ciclo.")

    return "\n".join(lines)


def build_next_day_focus(
    setups: list,
    gems: list,
    btc_state: str,
    news_severity: str,
) -> str:
    """Build next day focus section."""
    lines = []
    if btc_state == "bearish":
        lines.append("- Manter postura conservadora — BTC em tendência baixista.")
    if news_severity in ("high", "critical"):
        lines.append("- Monitorar desenvolvimento do evento de alta severidade.")
    if setups:
        lines.append(f"- Acompanhar setups identificados: {', '.join(setups[:3])}")
    if gems:
        lines.append(f"- Rever GEM_ALERTs da sessão asiática: {', '.join(gems[:3])}")
    if not lines:
        lines.append("- Continuar em READ_ONLY / SIMULATE — aguardar próximo ciclo.")
    return "\n".join(lines)


def estimate_summary_score(
    btc_state: str,
    setups: list,
    gems: list,
    news_severity: str,
    open_positions: int,
) -> float:
    """Estimate a summary score for the day (0-10)."""
    score = 5.0
    if btc_state == "bullish":
        score += 1.5
    elif btc_state == "bearish":
        score -= 1.0
    score += min(len(setups) * 0.3, 1.5)
    score += min(len(gems) * 0.2, 1.0)
    if news_severity in ("high", "critical"):
        score -= 1.5
    elif news_severity == "medium":
        score -= 0.5
    if open_positions > 0:
        score += 0.5
    return round(max(0.0, min(10.0, score)), 1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_journal(date: str, cycle: str) -> str:
    """Build the complete journal markdown string."""
    scout_path = find_latest_report("SCOUT_REPORT", date)
    asian_path = find_latest_report("ASIAN_REPORT", date)

    btc_state      = extract_btc_state(scout_path)
    regime         = extract_market_regime(scout_path)
    news_severity  = extract_news_severity(scout_path)
    open_positions = count_open_positions()
    setups         = extract_setups_from_scout(scout_path)
    gems           = extract_gem_alerts_from_asian(asian_path)
    key_theme      = determine_key_theme(btc_state, regime, news_severity, setups, open_positions)
    summary_score  = estimate_summary_score(btc_state, setups, gems, news_severity, open_positions)
    new_trades     = 0  # only manual entries increment this
    watchlist_changes = len(setups) + len(gems)

    observations   = build_observations(
        date, cycle, scout_path, asian_path,
        setups, gems, btc_state, regime, news_severity, open_positions
    )
    next_day_focus = build_next_day_focus(setups, gems, btc_state, news_severity)

    # Linked reports
    linked = []
    if scout_path:
        linked.append(f"- Scout: {scout_path.name}")
    if asian_path:
        linked.append(f"- Asian: {asian_path.name}")
    linked_str = "\n".join(linked) if linked else "- none"

    content = f"""---
schema_type: daily_journal
schema_version: 1.0

journal_date: {date}
system_phase: {SYSTEM_PHASE}
system_status: healthy

market_regime: {regime}
btc_macro_state: {btc_state}
portfolio_risk_state: medium
news_severity_max: {news_severity}

open_positions_count: {open_positions}
new_trades_count: {new_trades}
closed_trades_count: 0
watchlist_changes_count: {watchlist_changes}
blockers_count: 0

key_theme_of_day: {key_theme}
summary_score: {summary_score}

tags:
  - daily_journal
  - auto_generated
  - {cycle}_cycle
---

# Daily Summary

## Daily Observations
{observations}

## Lessons Learned
- Journal gerado automaticamente pelo AGT-07 Journal Auditor.
- Actualizar manualmente com aprendizagens específicas da sessão.

## Deviations
- none

## Watchlist Changes
{f"- Setups identificados para monitorização: {', '.join(setups)}" if setups else "- none"}
{f"- GEM_ALERTs asiáticos: {', '.join(gems)}" if gems else ""}

## Pending Decisions for Human Approval
- none

## Next-Day Focus
{next_day_focus}

---

## Linked Reports
{linked_str}
"""
    return content.strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Euru Journal Auditor — AGT-07")
    parser.add_argument("--date",    default=today_str(), help="Date YYYY-MM-DD (default: today)")
    parser.add_argument("--cycle",   default="morning",   choices=["morning", "asian", "manual"])
    parser.add_argument("--dry-run", action="store_true", help="Print journal without writing")
    parser.add_argument("--root",    default=".",         help="Path to Euru_TOS root")
    args = parser.parse_args()

    # Allow --root to override script dir
    global SCRIPT_DIR, SCORECARDS, TRADES_DIR, JOURNAL_DIR
    SCRIPT_DIR  = Path(args.root).resolve()
    SCORECARDS  = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "SCORECARDS"
    TRADES_DIR  = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "JOURNAL_TRADES"
    JOURNAL_DIR = SCRIPT_DIR / "08_DADOS_E_JOURNAL" / "JOURNAL_DAILY"

    journal_content = build_journal(args.date, args.cycle)

    if args.dry_run:
        print(journal_content)
        return 0

    JOURNAL_DIR.mkdir(parents=True, exist_ok=True)
    output_path = JOURNAL_DIR / f"JOURNAL_{args.date}.md"

    if output_path.exists():
        print(f"Journal already exists: {output_path}")
        print("Use --dry-run to preview or delete the existing file to regenerate.")
        return 1

    output_path.write_text(journal_content, encoding="utf-8")
    print(f"Journal Auditor — journal written: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

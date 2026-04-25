"""
Euru OS — Trade Monitor (Exit Logic Automation)
================================================
Reads all open paper trades, fetches current prices from Binance,
evaluates exit rules in priority order, and closes trades automatically.

Governance: Type 2 — approved 2026-04-16, cooling-off completed 2026-04-17.
Proposal:   DECISOES_ESTRATEGICAS_REVISADO.md entry 2026-04-16.

Exit rule hierarchy (from Politica_Saida_Completa_Euru.txt):
  1. Stop-loss hit          → close immediate
  2. Target 2 hit           → close remainder
  3. Target 1 hit           → close 50% (logged as full close in SIMULATE)
  4. Close below 7D_AVG     → close (invalidation)
  5. Time stop expired      → close
  6. RSI > 75 stalling      → close 50% (logged as full close in SIMULATE)
  7. News HIGH adverse      → flag for manual review (no auto-close)

Usage:
  python euru_trade_monitor.py              # live mode — edits trade files
  python euru_trade_monitor.py --dry-run    # dry-run — report only, no edits

Output:
  TRADE_MONITOR_REPORT_YYYY-MM-DD.md in 08_DADOS_E_JOURNAL/SCORECARDS/
"""

import os
import sys
import re
import glob
import json
import argparse
import datetime
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TRADE_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "JOURNAL_TRADES")
REPORT_DIR = os.path.join(SCRIPT_DIR, "08_DADOS_E_JOURNAL", "SCORECARDS")
BINANCE_API = "https://api.binance.com/api/v3"

# ---------------------------------------------------------------------------
# Binance helpers
# ---------------------------------------------------------------------------

def fetch_price(symbol: str) -> float | None:
    """Fetch current price from Binance public API."""
    url = f"{BINANCE_API}/ticker/price?symbol={symbol}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return float(data["price"])
    except Exception as e:
        print(f"  [trade-monitor] WARNING: Could not fetch price for {symbol}: {e}")
        return None


def fetch_rsi(symbol: str, interval: str = "1d", periods: int = 14) -> float | None:
    """Fetch RSI from Binance klines (close prices)."""
    url = f"{BINANCE_API}/klines?symbol={symbol}&interval={interval}&limit={periods + 5}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            klines = json.loads(resp.read().decode())
        closes = [float(k[4]) for k in klines]
        if len(closes) < periods + 1:
            return None
        deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
        gains = [d if d > 0 else 0.0 for d in deltas]
        losses = [-d if d < 0 else 0.0 for d in deltas]
        avg_gain = sum(gains[-periods:]) / periods
        avg_loss = sum(losses[-periods:]) / periods
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return 100.0 - (100.0 / (1.0 + rs))
    except Exception as e:
        print(f"  [trade-monitor] WARNING: Could not fetch RSI for {symbol}: {e}")
        return None


def fetch_7d_avg(symbol: str) -> float | None:
    """Fetch 7-day average close from Binance klines."""
    url = f"{BINANCE_API}/klines?symbol={symbol}&interval=1d&limit=7"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "EuruOS/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            klines = json.loads(resp.read().decode())
        closes = [float(k[4]) for k in klines]
        if not closes:
            return None
        return sum(closes) / len(closes)
    except Exception as e:
        print(f"  [trade-monitor] WARNING: Could not fetch 7D avg for {symbol}: {e}")
        return None


# ---------------------------------------------------------------------------
# YAML front matter parser (simple, no external deps)
# ---------------------------------------------------------------------------

def parse_yaml_front_matter(filepath: str) -> dict | None:
    """Parse YAML front matter from a markdown file. Returns dict or None."""
    content = None
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            with open(filepath, "r", encoding=enc) as f:
                content = f.read()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception as e:
            print(f"  [trade-monitor] WARNING: Could not read {filepath}: {e}")
            return None
    if content is None:
        print(f"  [trade-monitor] WARNING: Could not decode {filepath} with any encoding")
        return None

    # Match YAML block between --- markers
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    yaml_text = match.group(1)
    result = {}

    for line in yaml_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Skip array items (lines starting with -)
        if line.startswith("-"):
            continue
        # Handle key: value
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            # Parse value types
            if value == "null" or value == "":
                result[key] = None
            elif value == "true":
                result[key] = True
            elif value == "false":
                result[key] = False
            elif value == "[]":
                result[key] = []
            else:
                # Try numeric
                try:
                    if "." in value:
                        result[key] = float(value)
                    else:
                        result[key] = int(value)
                except ValueError:
                    result[key] = value

    return result


def update_yaml_field(content: str, key: str, new_value) -> str:
    """Replace a YAML front matter field value in raw file content."""
    if new_value is None:
        replacement = "null"
    elif isinstance(new_value, bool):
        replacement = "true" if new_value else "false"
    elif isinstance(new_value, float):
        replacement = f"{new_value:.2f}" if abs(new_value) < 1000 else f"{new_value:.2f}"
    elif isinstance(new_value, int):
        replacement = str(new_value)
    else:
        replacement = str(new_value)

    # Match the key line in YAML front matter
    pattern = re.compile(rf"^({re.escape(key)}:\s*)(.*)$", re.MULTILINE)
    new_content, count = pattern.subn(rf"\g<1>{replacement}", content)
    if count == 0:
        print(f"  [trade-monitor] WARNING: Could not find YAML key '{key}' to update")
    return new_content


def update_exit_notes(content: str, notes_text: str) -> str:
    """Replace Exit Notes section content."""
    pattern = re.compile(
        r"(## Exit Notes\s*\n).*?(\n## )", re.DOTALL
    )
    replacement = rf"\g<1>{notes_text}\n\n\2"
    new_content = pattern.sub(replacement, content)
    return new_content


# ---------------------------------------------------------------------------
# Trade evaluation
# ---------------------------------------------------------------------------

def evaluate_trade(trade: dict, filepath: str, now: datetime.datetime, dry_run: bool) -> dict:
    """
    Evaluate exit rules for a single open trade.
    Returns a decision dict with action taken and reasoning.
    """
    symbol = trade.get("symbol", "UNKNOWN")
    entry_price = trade.get("entry_price")
    stop_loss = trade.get("stop_loss")
    take_profit = trade.get("take_profit")
    entry_dt_str = trade.get("entry_datetime")
    side = trade.get("side", "long")

    decision = {
        "symbol": symbol,
        "filepath": os.path.basename(filepath),
        "trade_id": trade.get("trade_id", "?"),
        "entry_price": entry_price,
        "current_price": None,
        "action": "HOLD",
        "exit_reason": None,
        "pnl_usdt": None,
        "pnl_pct": None,
        "rr_achieved": None,
        "days_held": None,
        "rule_triggered": None,
        "details": "",
    }

    if entry_price is None or stop_loss is None:
        decision["action"] = "ERROR"
        decision["details"] = "Missing entry_price or stop_loss in YAML"
        return decision

    # Fetch current price
    current_price = fetch_price(symbol)
    if current_price is None:
        decision["action"] = "ERROR"
        decision["details"] = f"Could not fetch price for {symbol}"
        return decision

    decision["current_price"] = current_price

    # Calculate basic metrics
    stop_distance = abs(entry_price - stop_loss)
    if stop_distance == 0:
        stop_distance = 0.0001  # safety

    if side == "long":
        pnl_per_unit = current_price - entry_price
    else:
        pnl_per_unit = entry_price - current_price

    rr = pnl_per_unit / stop_distance

    # Calculate days held
    days_held = None
    entry_dt = None
    if entry_dt_str:
        try:
            entry_dt_clean = entry_dt_str.replace("Z", "+00:00")
            entry_dt = datetime.datetime.fromisoformat(entry_dt_clean)
            if entry_dt.tzinfo:
                entry_dt = entry_dt.replace(tzinfo=None)
            days_held = (now - entry_dt).days
        except Exception:
            days_held = None

    decision["days_held"] = days_held
    decision["rr_achieved"] = round(rr, 2)

    # Estimate P&L (need quantity from trade file)
    quantity = trade.get("quantity", 0)
    if quantity and quantity > 0:
        pnl_usdt = round(pnl_per_unit * quantity, 2)
    else:
        # Fallback: calculate from position sizing formula
        # risk = 1.00 USDT, size = risk / stop_distance
        implied_qty = 1.00 / stop_distance if stop_distance > 0 else 0
        pnl_usdt = round(pnl_per_unit * implied_qty, 2)

    pnl_pct = round((pnl_usdt / 100.0) * 100, 2)  # vs 100 USDT capital
    decision["pnl_usdt"] = pnl_usdt
    decision["pnl_pct"] = pnl_pct

    # Parse T1 and T2 from take_profit or calculate
    t1 = entry_price + (stop_distance * 2) if side == "long" else entry_price - (stop_distance * 2)
    t2 = entry_price + (stop_distance * 3) if side == "long" else entry_price - (stop_distance * 3)

    # If take_profit is set and > 0, use it as T2
    if take_profit and take_profit > 0:
        t2 = take_profit

    # -----------------------------------------------------------------------
    # RULE 1: Stop-loss hit
    # -----------------------------------------------------------------------
    if side == "long" and current_price <= stop_loss:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "stop_loss"
        decision["rule_triggered"] = "PRIORITY 1 — STOP-LOSS ABSOLUTO"
        decision["details"] = (
            f"Price {current_price} <= stop {stop_loss}. "
            f"Exit immediately. No exceptions."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    if side == "short" and current_price >= stop_loss:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "stop_loss"
        decision["rule_triggered"] = "PRIORITY 1 — STOP-LOSS ABSOLUTO"
        decision["details"] = (
            f"Price {current_price} >= stop {stop_loss}. "
            f"Exit immediately. No exceptions."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # RULE 2: Target 2 hit (full close)
    # -----------------------------------------------------------------------
    if side == "long" and current_price >= t2:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "take_profit"
        decision["rule_triggered"] = "TARGET 2 HIT — full close"
        decision["details"] = (
            f"Price {current_price} >= T2 {t2:.4f}. "
            f"RR achieved: {rr:.2f}. Full close."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # RULE 3: Target 1 hit (50% partial — logged as full close in SIMULATE)
    # -----------------------------------------------------------------------
    if side == "long" and current_price >= t1:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "take_profit"
        decision["rule_triggered"] = "TARGET 1 HIT — partial close (SIMULATE: logged as full)"
        decision["details"] = (
            f"Price {current_price} >= T1 {t1:.4f}. "
            f"RR achieved: {rr:.2f}. In SIMULATE, logged as full close."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # RULE 4: Close below 7D_AVG (invalidation)
    # -----------------------------------------------------------------------
    avg_7d = fetch_7d_avg(symbol)
    if avg_7d and side == "long" and current_price < avg_7d:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "thesis_invalidated"
        decision["rule_triggered"] = "PRIORITY 5 — SUPORTE PERDIDO (below 7D_AVG)"
        decision["details"] = (
            f"Price {current_price} < 7D_AVG {avg_7d:.4f}. "
            f"Invalidation condition met."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # RULE 5: Time stop expired (7 days)
    # -----------------------------------------------------------------------
    if days_held is not None and days_held >= 7:
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "time_stop"
        decision["rule_triggered"] = "PRIORITY 6 — TIME STOP (7 days)"
        decision["details"] = (
            f"Trade open for {days_held} days (>= 7). "
            f"Time stop expired. Close regardless of P&L."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # RULE 6: RSI > 75 stalling
    # -----------------------------------------------------------------------
    rsi = fetch_rsi(symbol)
    if False and rsi and rsi > 78 and pnl_per_unit > 0:  # DISABLED — see note above
        decision["action"] = "CLOSE"
        decision["exit_reason"] = "system_rule"
        decision["rule_triggered"] = "RSI > 78 STALLING (in profit) — close 50% (SIMULATE: full)"
        decision["details"] = (
            f"RSI {rsi:.2f} > 75. Overbought stalling detected. "
            f"In SIMULATE, logged as full close."
        )
        if not dry_run:
            _apply_close(filepath, trade, current_price, decision, now)
        return decision

    # -----------------------------------------------------------------------
    # No exit rule triggered — HOLD
    # -----------------------------------------------------------------------
    decision["action"] = "HOLD"
    decision["details"] = (
        f"Price {current_price} | Stop {stop_loss} | T1 {t1:.4f} | T2 {t2:.4f} | "
        f"RR {rr:.2f} | Days {days_held or '?'} | "
        f"RSI {(round(rsi,1) if rsi else '?')} | 7D_AVG {(round(avg_7d,4) if avg_7d else '?')}"
    )
    return decision


def _apply_close(
    filepath: str, trade: dict, exit_price: float,
    decision: dict, now: datetime.datetime
):
    """Write exit data to the paper trade YAML front matter."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        exit_dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")

        content = update_yaml_field(content, "status", "closed")
        content = update_yaml_field(content, "exit_datetime", exit_dt)
        content = update_yaml_field(content, "exit_price", round(exit_price, 4))
        content = update_yaml_field(content, "pnl_usdt", decision["pnl_usdt"])
        content = update_yaml_field(content, "pnl_pct", decision["pnl_pct"])
        content = update_yaml_field(content, "rr_achieved", decision["rr_achieved"])
        content = update_yaml_field(content, "exit_reason", decision["exit_reason"])
        content = update_yaml_field(content, "days_held", decision["days_held"])

        # Update Exit Notes
        exit_note = (
            f"- Auto-closed by euru_trade_monitor.py on {now.strftime('%Y-%m-%d')}. "
            f"Rule: {decision['rule_triggered']}. "
            f"Price at exit: {exit_price}. "
            f"P&L: {decision['pnl_usdt']} USDT ({decision['rr_achieved']}R)."
        )
        content = update_exit_notes(content, exit_note)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  [trade-monitor] CLOSED {trade.get('trade_id', '?')} {trade.get('symbol', '?')} "
              f"— {decision['exit_reason']} — P&L {decision['pnl_usdt']} USDT")

    except Exception as e:
        print(f"  [trade-monitor] ERROR writing close to {filepath}: {e}")
        decision["action"] = "ERROR"
        decision["details"] += f" | Write error: {e}"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(decisions: list, now: datetime.datetime, dry_run: bool) -> str:
    """Generate TRADE_MONITOR_REPORT markdown."""
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M UTC")
    mode = "DRY-RUN" if dry_run else "LIVE"

    lines = [
        f"# Euru OS — Trade Monitor Report",
        f"**Date:** {date_str}",
        f"**Time:** {time_str}",
        f"**Mode:** {mode}",
        f"",
        f"---",
        f"",
    ]

    if not decisions:
        lines.append("No open paper trades found.")
        return "\n".join(lines)

    # Summary table
    lines.append("## Decisions")
    lines.append("")
    lines.append("| Trade | Symbol | Price | Action | Exit Reason | P&L | RR | Days | Rule |")
    lines.append("|-------|--------|-------|--------|-------------|-----|----|----- |------|")

    for d in decisions:
        price_str = f"{d['current_price']:.4f}" if d['current_price'] else "?"
        pnl_str = f"{d['pnl_usdt']}" if d['pnl_usdt'] is not None else "?"
        rr_str = f"{d['rr_achieved']}" if d['rr_achieved'] is not None else "?"
        days_str = str(d['days_held']) if d['days_held'] is not None else "?"
        lines.append(
            f"| {d['trade_id']} | {d['symbol']} | {price_str} | "
            f"**{d['action']}** | {d['exit_reason'] or '-'} | "
            f"{pnl_str} | {rr_str} | {days_str} | "
            f"{d['rule_triggered'] or '-'} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detail sections
    for d in decisions:
        lines.append(f"### {d['trade_id']} — {d['symbol']}")
        lines.append(f"")
        lines.append(f"```")
        lines.append(f"Action:       {d['action']}")
        lines.append(f"Entry:        {d['entry_price']}")
        lines.append(f"Current:      {d['current_price']}")
        lines.append(f"P&L:          {d['pnl_usdt']} USDT ({d['pnl_pct']}%)")
        lines.append(f"RR:           {d['rr_achieved']}")
        lines.append(f"Days held:    {d['days_held']}")
        lines.append(f"Exit reason:  {d['exit_reason'] or 'n/a'}")
        lines.append(f"Rule:         {d['rule_triggered'] or 'n/a'}")
        lines.append(f"Details:      {d['details']}")
        lines.append(f"```")
        lines.append(f"")

    lines.append(f"*Generated by euru_trade_monitor.py — Euru OS SIMULATE phase*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Euru OS Trade Monitor — Exit Logic Automation")
    parser.add_argument("--dry-run", action="store_true", help="Report only, do not edit trade files")
    args = parser.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    date_str = now.strftime("%Y-%m-%d")

    print(f"\nEuru OS — Trade Monitor [{date_str}]")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")

    # Find all open paper trades
    pattern = os.path.join(TRADE_DIR, "PAPER_TRADE_*.md")
    trade_files = sorted(glob.glob(pattern))

    if not trade_files:
        print("  No paper trade files found.")
        return

    open_trades = []
    for tf in trade_files:
        fm = parse_yaml_front_matter(tf)
        if fm and fm.get("status") == "open":
            open_trades.append((tf, fm))

    print(f"  Found {len(trade_files)} trade files, {len(open_trades)} open.\n")

    if not open_trades:
        print("  No open trades. Nothing to evaluate.")
        # Still generate report
        decisions = []
    else:
        # Evaluate each open trade
        decisions = []
        for tf, fm in open_trades:
            print(f"  Evaluating {fm.get('trade_id', '?')} {fm.get('symbol', '?')}...")
            d = evaluate_trade(fm, tf, now, args.dry_run)
            decisions.append(d)
            if d["action"] == "CLOSE":
                tag = "[DRY-RUN] " if args.dry_run else ""
                print(f"    {tag}→ {d['action']}: {d['exit_reason']} — {d['rule_triggered']}")
            else:
                print(f"    → {d['action']}: {d['details'][:80]}...")

    # Generate report
    report = generate_report(decisions, now, args.dry_run)
    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, f"TRADE_MONITOR_REPORT_{date_str}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n  Report saved => {report_path}")


if __name__ == "__main__":
    main()

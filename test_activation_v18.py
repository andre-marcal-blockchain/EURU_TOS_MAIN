import datetime
import unittest
from pathlib import Path
from unittest.mock import patch

import euru_journal_auditor as journal
from euru_trade_monitor import generate_report


class ActivationV18Tests(unittest.TestCase):
    def test_journal_uses_exact_date_reports(self):
        with (
            patch.object(journal, "find_report_for_date", return_value=None),
            patch.object(journal, "count_open_positions", return_value=0),
        ):
            content = journal.build_journal("2026-06-10", "morning")

        self.assertIn("input_status: STALE_INPUT", content)
        self.assertIn("system_status: warning", content)
        self.assertIn("blockers_count: 2", content)
        self.assertNotIn("SCOUT_REPORT_2026-06-09.md", content)

    def test_journal_marks_current_when_both_exact_reports_exist(self):
        scout = Path("SCOUT_REPORT_2026-06-10.md")
        asian = Path("ASIAN_REPORT_2026-06-10.md")
        with (
            patch.object(
                journal, "find_report_for_date", side_effect=[scout, asian]
            ),
            patch.object(journal, "extract_btc_state", return_value="bullish"),
            patch.object(journal, "extract_market_regime", return_value="bull_trend"),
            patch.object(journal, "extract_news_severity", return_value="none"),
            patch.object(journal, "count_open_positions", return_value=0),
            patch.object(journal, "extract_setups_from_scout", return_value=[]),
            patch.object(journal, "extract_gem_alerts_from_asian", return_value=[]),
        ):
            content = journal.build_journal("2026-06-10", "morning")

        self.assertIn("input_status: CURRENT", content)
        self.assertIn("system_status: healthy", content)
        self.assertIn("blockers_count: 0", content)

    def test_trade_monitor_uses_simulate_mode_labels(self):
        now = datetime.datetime(2026, 6, 10, 12, 0)

        self.assertIn(
            "**Mode:** SIMULATE_WRITE", generate_report([], now, dry_run=False)
        )
        self.assertIn(
            "**Mode:** SIMULATE_DRY_RUN", generate_report([], now, dry_run=True)
        )


if __name__ == "__main__":
    unittest.main()

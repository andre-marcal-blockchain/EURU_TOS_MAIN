2026-06-05

- Automation: `EURU AGuia Asian Scanner Cron`
- Canonical command: `python .\euru_aguia_asian_scanner.py --market futures --symbols BTCUSDT ETHUSDT SOLUSDT --print`
- Mode: `READ_ONLY`
- Scorecard: [AGUIA_ASIAN_SCAN_2026-06-05.md](C:\Users\andre\Desktop\EURU TOS MAIN\08_DADOS_E_JOURNAL\SCORECARDS\AGUIA_ASIAN_SCAN_2026-06-05.md)
- Top verdict: `NO_ENTRY`
- Pair verdicts:
  - `BTCUSDT`: `NO_ENTRY`, `SHORT`, `Continuation`, BTC filter `SELF`, room `0.15R`
  - `ETHUSDT`: `NO_ENTRY`, `SHORT`, `Continuation`, BTC filter `INACTIVE`, room `0.05R`
  - `SOLUSDT`: `NO_ENTRY`, `SHORT`, `Breakout`, BTC filter `INACTIVE`, room `-0.03R`
- Safety: no live orders placed, no Binance API keys used, live execution remained blocked
- Note: external automation memory path under `$CODEX_HOME` was not available in this session, so this workspace-local fallback record was written instead

2026-06-05 follow-up

- Prevention steps identified:
  - Ensure the automation runtime exports `$CODEX_HOME` before launching Codex or the scanner workflow
  - Ensure the runtime can write to `C:\Users\andre\.codex\automations\euru-aguia-asian-scanner-cron\memory.md`
  - Add a preflight check that fails fast when `$CODEX_HOME` is missing
  - Keep the repo-local fallback memory file until the external path is consistently available
- Current run time: ~1 minute

2026-06-05 launcher remediation progress

- `Euru_Asian_Scan` scheduled task action runs `python` directly with argument `euru_asian_scan.py`
- User persisted `CODEX_HOME` with `setx CODEX_HOME "C:\Users\andre\.codex"`
- Verification via child PowerShell from the same terminal still returned empty, which is consistent with the parent session not having refreshed its environment block yet
- Registry check confirmed `HKCU\Environment\CODEX_HOME = C:\Users\andre\.codex`
- Follow-up shell checks still returned empty, indicating the visible session likely has not been restarted into a refreshed environment yet

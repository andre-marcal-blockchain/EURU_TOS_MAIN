# 03_NEWS_SENTINEL — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: News Sentinel
SYMBOL: [ex: NEARUSDT | MARKET_WIDE]
TIMEFRAME: [1D]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

OVERALL_SEVERITY: [INFO | NEUTRA | MEDIA_SEVERIDADE | ALTA_SEVERIDADE | SEM_NOVIDADE | REVIEW]

TOP_HEADLINES:
  1. [HIGH|MEDIUM|LOW] [Headline] — SOURCE: [fonte]
  2. [HIGH|MEDIUM|LOW] [Headline] — SOURCE: [fonte]
  3. [HIGH|MEDIUM|LOW] [Headline] — SOURCE: [fonte]

ACTIVE_NARRATIVES:
  AI:       [STRONG | MODERATE | WEAK | ABSENT]
  RWA:      [STRONG | MODERATE | WEAK | ABSENT]
  DePIN:    [STRONG | MODERATE | WEAK | ABSENT]
  Gaming:   [STRONG | MODERATE | WEAK | ABSENT]
  Macro:    [STRONG | MODERATE | WEAK | ABSENT]

ASSETS_AFFECTED: [lista de activos da watchlist afectados | none]

ALERT_REQUIRED: [YES | NO]
SUMMARY: [1-2 frases resumindo o contexto de notícias]
REASON: [explicação de por que a severidade foi seleccionada]
NEXT_AGENT: [Score Engine | Execution Orchestrator (se ALTA_SEVERIDADE)]

## Rules
- Populate each field; use SEM_NOVIDADE when no events are relevant.
- Do not include speculation or unverified rumours.
- Ensure sources are cited (URL or publication name).
- Keep SUMMARY and REASON concise (1-3 sentences).
- CONFIDENCE: 0-3 single unverified source | 4-6 multiple sources no consensus | 7-8 credible sources agree | 9-10 official confirmed sources.

## Example

AGENT: News Sentinel
SYMBOL: MARKET_WIDE
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 8

OVERALL_SEVERITY: ALTA_SEVERIDADE

TOP_HEADLINES:
  1. [HIGH] Bitcoin shorts risk $2.5B liquidation at $72K — SOURCE: CoinTelegraph
  2. [HIGH] Nevada judge extends ban on Kalshi event contracts — SOURCE: CoinTelegraph
  3. [LOW] Ethereum Foundation reaches 70K staked ETH goal — SOURCE: CoinTelegraph

ACTIVE_NARRATIVES:
  AI:     MODERATE
  Macro:  STRONG
  RWA:    WEAK

ASSETS_AFFECTED: BTCUSDT ($72K liquidation level critical), NEARUSDT (AI narrative active)

ALERT_REQUIRED: YES
SUMMARY: HIGH severity macro environment. $2.5B short squeeze possible if BTC breaks $72K. Regulatory news adds uncertainty.
REASON: Two HIGH severity headlines in same session — war/macro + regulatory ban keywords triggered.
NEXT_AGENT: Execution Orchestrator

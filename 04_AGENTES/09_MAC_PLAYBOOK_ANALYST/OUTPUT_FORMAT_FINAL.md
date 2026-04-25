# 09_MAC/PLAYBOOK ANALYST — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: MAC/Playbook Analyst
SYMBOL: [ex: NEARUSDT]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

MOVIMENTO:    [alta | baixa | lateral]
ACELERACAO:   [positiva | negativa | nula]
CONFIRMACAO:  [confirmada | fraca | ausente]
MAC_VALID:    [YES | NO | PARTIAL]

SETUP_IDENTIFIED: [Breakout | Sweep+Reversal | Reteste | Continuação | Narrativa+Gráfico | NONE]
SETUP_QUALITY:    [CLEAN | MARGINAL | INVALID]

PLAYBOOK_CHECKLIST:
  PONTO_1_NARRATIVA:         [OK | FAIL]
  PONTO_2_BTC_CONTEXT:       [OK | FAIL]
  PONTO_3_MAJORS:            [OK | FAIL]
  PONTO_4_ESTRUTURA:         [OK | FAIL]
  PONTO_5_ROMPIMENTO:        [OK | FAIL]
  PONTO_6_VOLUME:            [OK | FAIL]
  PONTO_7_LIQUIDEZ:          [OK | FAIL]
  PONTO_8_INVALIDACAO:       [OK | FAIL]
  PONTO_9_RISCO:             [OK | FAIL]
  PONTO_10_ALVO:             [OK | FAIL]
  PONTO_11_RR_RATIO:         [OK | FAIL]
  PONTO_12_PLANO_NAO_EMOCAO: [OK | FAIL]
  CHECKLIST_SCORE: [n/12]

EXIT_POLICY:
  STOP_LOSS:     [nível — ex: abaixo suporte ou 1.5xATR]
  TAKE_PROFIT:   [níveis — ex: 161.8% Fib, 2x risco]
  TRAILING_STOP: [estratégia ou não aplicável]
  TIME_STOP:     [dias ou não aplicável]
  RR_RATIO:      [ratio — mínimo 1:2]

PLAYBOOK_STATE: [PLAYBOOK_OK | PLAYBOOK_REJECT | REVIEW]
REASON: [justificação — quais pilares ou checklist items passaram ou falharam]
NEXT_AGENT: [Score Engine | Execution Orchestrator]

## Rules
- Fill all fields; use the provided options for enumerated fields.
- MAC pillars must each be assessed independently.
- PLAYBOOK_STATE follows MAC validity + checklist score + Exit Policy completeness.
- REASON must identify specifically which pillar or checklist item caused the decision.
- CONFIDENCE: 0-3 pillars in conflict checklist <6/12 | 4-6 checklist 7-9/12 | 7-8 checklist 10-11/12 | 9-10 checklist 12/12 all pillars CONFIRMED.

## Example

AGENT: MAC/Playbook Analyst
SYMBOL: NEARUSDT
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 5

MOVIMENTO:    alta
ACELERACAO:   positiva
CONFIRMACAO:  confirmada
MAC_VALID:    PARTIAL

SETUP_IDENTIFIED: Breakout
SETUP_QUALITY:    MARGINAL

PLAYBOOK_CHECKLIST:
  PONTO_1_NARRATIVA:         OK
  PONTO_2_BTC_CONTEXT:       FAIL
  PONTO_3_MAJORS:            FAIL
  PONTO_4_ESTRUTURA:         OK
  PONTO_5_ROMPIMENTO:        OK
  PONTO_6_VOLUME:            OK
  PONTO_7_LIQUIDEZ:          OK
  PONTO_8_INVALIDACAO:       OK
  PONTO_9_RISCO:             OK
  PONTO_10_ALVO:             OK
  PONTO_11_RR_RATIO:         OK
  PONTO_12_PLANO_NAO_EMOCAO: OK
  CHECKLIST_SCORE: 10/12

EXIT_POLICY:
  STOP_LOSS:     1.1512 (ATR x 1.5 below entry)
  TAKE_PROFIT:   1.4720 (1:2), 1.5828 (1:3)
  TRAILING_STOP: não aplicável (awaiting SIMULATE)
  TIME_STOP:     7 days
  RR_RATIO:      1:2.5

PLAYBOOK_STATE: REVIEW
REASON: MAC PARTIAL — Aceleração positive but MACD still lagging. Checklist 10/12 (BTC context and market alignment fail). Exit Policy defined. Revisit when BTC filter lifts and MACD confirms bullish crossover.
NEXT_AGENT: Score Engine

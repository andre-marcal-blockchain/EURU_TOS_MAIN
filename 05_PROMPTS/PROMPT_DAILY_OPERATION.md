# PROMPT_DAILY_OPERATION — Euru OS
**Versão:** 1.0 (Week 5+)
**Última actualização:** 2026-04-05
**Duração estimada:** 30 minutos
**Referência:** `07_OPERACAO/SOP_DIARIO_v2.txt`

---

## REGRA DE OURO
Se qualquer agente produzir resultado inesperado — PARA. Regista o incidente. Não avances.

---

## BLOCO 1 — ABERTURA (2 min)

```
Sistema: READ_ONLY / SIMULATE / EXECUTE  →  ___________
Pipeline status:                          →  HEALTHY / DEGRADED / CRITICAL
Asian scan gerado (00:00 UTC)?            →  SIM / NÃO
Ficheiro: 08_DADOS_E_JOURNAL/SCORECARDS/ASIAN_REPORT_YYYY-MM-DD.md
```

---

## BLOCO 2 — MORNING SCAN (10 min)

**Comando:** `python euru_morning_scan.py`

Após execução, abre `08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_YYYY-MM-DD.md` e verifica:

```
Assets scanned:       ___ / 20
Pipeline status:      HEALTHY / DEGRADED
News severity:        LOW / MEDIUM / HIGH / CRITICAL
BTC Master Filter:    ACTIVE (bearish/sideways) / INACTIVE (bullish)
SETUPs detectados:    ___________
```

---

## BLOCO 3 — AGENTE: SCOUT (01)

**O que perguntar:** Qual é a estrutura de mercado de cada asset hoje?

```
Prompt:
"Scout, analisa [ASSET] no timeframe diário.
Identifica: estrutura (suporte/resistência), padrão de compressão, breakout ou reteste.
Output: NO_TRADE / WATCHLIST / SETUP"
```

**Registo de outputs Scout:**

| Asset | Status | Score | Observação |
|---|---|---|---|
| | NO_TRADE / WATCHLIST / SETUP | /35 | |
| | | | |
| | | | |

**Nota BTC Filter:**
- ACTIVE → todos os SETUPs rebaixados para WATCHLIST. Modo conservador.
- INACTIVE → pipeline completo. Avaliar SETUPs normalmente.

---

## BLOCO 4 — AGENTE: FLOW ANALYST (02)

**O que perguntar:** O fluxo confirma ou contradiz a estrutura?

```
Prompt:
"Flow Analyst, analisa o fluxo de [ASSET].
RSI (14), MACD (12/26/9), OBV trend, ATR (14).
Output: CONFIRMS / CONTRADICTS / INCONCLUSIVE
CONFIDENCE: [0-10]"
```

**Registo de outputs Flow Analyst:**

| Asset | Flow Status | RSI | MACD | OBV | ATR | CONFIDENCE |
|---|---|---|---|---|---|---|
| | CONFIRMS / CONTRADICTS / INCONCLUSIVE | | bull/bear | RISING/FALLING | | /10 |
| | | | | | | |

---

## BLOCO 5 — AGENTE: NEWS SENTINEL (03)

**O que perguntar:** Há eventos que bloqueiam ou alteram a análise?

```
Prompt:
"News Sentinel, qual é o contexto de notícias para [ASSET / mercado crypto] hoje?
Identifica eventos com severidade: LOW / MEDIUM / HIGH / CRITICAL.
Narrativas emergentes activas?"
```

**Registo News Sentinel:**

```
Severidade geral:    LOW / MEDIUM / HIGH / CRITICAL
Assets afectados:    ___________
Narrativas activas:  ___________
Bloqueia pipeline?   SIM / NÃO
```

> CRITICAL ou HIGH adverso → NO_ENTRY. Não abrir novas posições.

---

## BLOCO 6 — SCORE LEADERBOARD

**Resumo de scores do dia (do SCOUT_REPORT):**

| Tier | Assets | Score Range |
|---|---|---|
| PREMIUM | | 28–35 |
| BOA | | 22–27 |
| MÉDIA | | 16–21 |
| IGNORAR | | 0–15 |

**Asset com score mais alto hoje:** ___________ (score: ___ / 35)

---

## BLOCO 7 — DECISÃO OPERACIONAL

### Se SYSTEM_MODE = READ_ONLY

```
O que faria se estivesse em SIMULATE?

Asset:        ___________
Setup type:   Breakout / Sweep+Reversal / Reteste / Continuação / Narrativa+Gráfico
Entrada:      ___________
Stop-loss:    ___________ (ATR × 1.5)
Target 1:     ___________ (1:2)
Target 2:     ___________ (1:3)
Motivo:       ___________
Decisão:      ENTRARIA / NÃO ENTRARIA
Porquê:       ___________
```

### Se SYSTEM_MODE = SIMULATE

→ Preenche `PROMPT_PRE_TRADE.md` antes de qualquer entrada.
→ Todos os 12 pontos do checklist devem passar.

---

## BLOCO 8 — FECHO E MANUTENÇÃO (5 min)

```
[ ] Relatório guardado em 08_DADOS_E_JOURNAL/SCORECARDS/
[ ] Observações registadas no diário (08_DADOS_E_JOURNAL/)
[ ] Incidente técnico? → regista em 09_LOGS_E_INCIDENTES/INCIDENTES.md
[ ] Changelog actualizado (se houve mudança no sistema)
[ ] Se sexta-feira → preenche PROMPT_WEEKLY_REVIEW.md
```

---

## CONDIÇÕES DE NO_TRADE (verificar antes de qualquer acção)

- [ ] Operador cansado ou sem foco → NO_TRADE
- [ ] 2+ stops consecutivos recentes → PAUSA 24h
- [ ] BTC com volatilidade errática → NO_TRADE
- [ ] News severity HIGH adverso → NO_TRADE
- [ ] Score < 22/35 → IGNORAR
- [ ] Pipeline DEGRADED ou CRITICAL → READ_ONLY imediato

---

## REFERÊNCIAS

| Documento | Localização |
|---|---|
| SOP Diário | `07_OPERACAO/SOP_DIARIO_v2.txt` |
| Padrão de Status | `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md` |
| Regras Mãe | `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` |
| Watchlist Oficial | `08_DADOS_E_JOURNAL/WATCHLISTS/WATCHLIST_OFICIAL.md` |
| Incidentes | `09_LOGS_E_INCIDENTES/INCIDENTES.md` |

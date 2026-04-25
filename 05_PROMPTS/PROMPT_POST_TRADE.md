# PROMPT_POST_TRADE — Euru OS
**Versão:** 1.0 (Week 5+)
**Última actualização:** 2026-04-05
**Referência:** `04_AGENTES/07_JOURNAL_AUDITOR/`, `07_OPERACAO/Politica_Saida_Completa_Euru.txt`

---

## REGRA DE OURO
Cada trade encerrada — win ou loss — DEVE ser registada e auditada.
Sem registo = sem aprendizagem = sem evolução do sistema.

---

## IDENTIFICAÇÃO DA TRADE

```
Data entrada:      ___________  UTC
Data saída:        ___________  UTC
Duração:           ___________  dias
Asset:             ___________
Setup type:        Breakout / Sweep+Reversal / Reteste / Continuação / Narrativa+Gráfico
Timeframe:         Daily / 4H
System mode:       SIMULATE / EXECUTE
Trade ID:          ___________  (referência para o journal)
```

---

## BLOCO 1 — DADOS DE EXECUÇÃO

```
Entry price:             ___________
Exit price:              ___________
Stop-loss definido:      ___________
Target 1 (1:2):          ___________
Target 2 (1:3):          ___________

Position size:           ___________  USDT
Resultado (USDT):        ___________  (+ ganho / – perda)
Resultado (R):           ___________  R  (resultado / stop distance)
R/R planeado:            1 : ___
R/R alcançado:           1 : ___

WIN / LOSS / BREAKEVEN
```

---

## BLOCO 2 — MOTIVO DE SAÍDA

```
Saída por (assinala o que aplica):
[ ] Stop-loss atingido (PRIORIDADE 1)
[ ] Evento macro adverso HIGH (PRIORIDADE 2)
[ ] Divergência OBV + RSI (PRIORIDADE 3)
[ ] MACD crossover negativo (PRIORIDADE 4)
[ ] Suporte perdido (PRIORIDADE 5)
[ ] Time stop — 7 dias (PRIORIDADE 6)
[ ] Target 1 atingido (1:2) — saída parcial 50%
[ ] Target 2 atingido (1:3)
[ ] Fibonacci 0.382 — saída parcial
[ ] Fibonacci 0.618 — core position
[ ] 50% securing activado (ROI ≥ 50%)
[ ] 10% harvesting activado (ROI ≥ 300%)
[ ] Saída manual por outro motivo: ___________

Agente que despoletou a saída:
Scout / Flow Analyst / News Sentinel / Quant/Risk / Execution Orch / Journal/Auditor
```

---

## BLOCO 3 — VERIFICAÇÃO DO PLAYBOOK

```
Setup era um dos 5 oficiais?               SIM / NÃO
Checklist 12 pontos foi completado?        SIM / NÃO
MAC 3 pilares estavam confirmados?         SIM / NÃO
R/R foi >= 1:2 no plano original?          SIM / NÃO
Exit rules estavam definidas antes da entrada? SIM / NÃO
Stop-loss foi movido contra as regras?     SIM / NÃO
Trade foi encerrada por emoção?            SIM / NÃO

PLAYBOOK_COMPLIANCE:   FULL / PARTIAL / VIOLATION
```

> VIOLATION → regista em `09_LOGS_E_INCIDENTES/INCIDENTES.md` e agenda revisão.

---

## BLOCO 4 — OUTPUTS DOS AGENTES (verificação pós-trade)

**O que cada agente dizia no momento da entrada:**

```
Scout (01):            NO_TRADE / WATCHLIST / SETUP
Flow Analyst (02):     CONFIRMS / CONTRADICTS / INCONCLUSIVE    CONFIDENCE: /10
News Sentinel (03):    LOW / MEDIUM / HIGH / CRITICAL
Score Engine (08):     Score: /35   Tier: PREMIUM / BOA / MÉDIA
MAC Playbook (09):     PLAYBOOK_OK / PLAYBOOK_REJECT             CONFIDENCE: /10
```

**O sinal estava correcto?**

```
Scout estava certo?        SIM / NÃO / PARCIALMENTE
Flow Analyst estava certo? SIM / NÃO / PARCIALMENTE
News impactou o resultado? SIM / NÃO
Score reflectia qualidade? SIM / NÃO
```

---

## BLOCO 5 — ANÁLISE DE QUALIDADE

```
O que correu bem:
___________

O que correu mal:
___________

O que faria diferente:
___________

Padrão de erro detectado (se loss):
[ ] Entrada cedo demais (estrutura não confirmada)
[ ] Stop muito apertado
[ ] R/R insuficiente (< 1:2)
[ ] BTC Filter ignorado
[ ] News severity ignorada
[ ] Emoção na decisão (não seguiu plano)
[ ] Setup fora do playbook
[ ] Outro: ___________
```

---

## BLOCO 6 — LIÇÃO APRENDIDA

```
Lição principal desta trade:
___________

Ajuste ao sistema proposto (se aplicável):
Tipo de mudança: Type 1 (Light) / Type 2 (Moderate) / Type 3 (Critical)
Descrição:       ___________
Aguarda aprovação: SIM / NÃO (Type 2/3 requerem espera)

CONFIDENCE no setup de entrada (retrospectiva): /10
```

---

## BLOCO 7 — REGISTO OBRIGATÓRIO NO JOURNAL

```
Guardar em: 08_DADOS_E_JOURNAL/JOURNAL_TRADES/JOURNAL_YYYY-MM-DD_[ASSET].md

Campos obrigatórios:
  TRADE_ID:          ___________
  DATE_ENTRY:        ___________
  DATE_EXIT:         ___________
  ASSET:             ___________
  SETUP:             ___________
  RESULT_R:          ___________
  RESULT_USDT:       ___________
  PLAYBOOK:          FULL / PARTIAL / VIOLATION
  LESSON:            ___________
```

---

## REFERÊNCIAS

| Documento | Localização |
|---|---|
| Política de Saída | `07_OPERACAO/Politica_Saida_Completa_Euru.txt` |
| Journal Auditor Output | `04_AGENTES/07_JOURNAL_AUDITOR/OUTPUT_FORMAT_FINAL.md` |
| Checklist Pré-Trade | `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt` |
| Incidentes | `09_LOGS_E_INCIDENTES/INCIDENTES.md` |
| Regras Mãe | `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` |

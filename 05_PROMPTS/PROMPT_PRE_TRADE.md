# PROMPT_PRE_TRADE — Euru OS
**Versão:** 1.0 (Week 5+)
**Última actualização:** 2026-04-05
**Referência:** `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt`

---

## REGRA ABSOLUTA
Este template DEVE ser preenchido antes de TODA e QUALQUER entrada (simulada ou real).
Se QUALQUER ponto = FAIL → **NO_ENTRY**. A ausência de trade é uma decisão válida e disciplinada.

---

## IDENTIFICAÇÃO DA TRADE

```
Data/Hora:       ___________  UTC
Asset:           ___________
Setup type:      Breakout / Sweep+Reversal / Reteste / Continuação / Narrativa+Gráfico
Timeframe:       Daily / 4H
System mode:     SIMULATE / EXECUTE
```

---

## OS 12 PONTOS DO CHECKLIST

| # | Campo MAC | Pergunta | Resposta | PASS / FAIL |
|---|---|---|---|---|
| 1 | PONTO_1_NARRATIVA | Qual é a narrativa da moeda? Está activa no mercado agora? | | |
| 2 | PONTO_2_BTC_CONTEXT | Qual o contexto do BTC? Filter ACTIVE ou INACTIVE? | | |
| 3 | PONTO_3_MAJORS | ETH e majors estão ajudando ou atrapalhando? | | |
| 4 | PONTO_4_ESTRUTURA | A estrutura está clara? Scout confirma SETUP? | | |
| 5 | PONTO_5_ROMPIMENTO | Há rompimento real ou só ruído? OBV confirma? | | |
| 6 | PONTO_6_VOLUME | O volume confirma? VOLUME_FLOW = STRONG? | | |
| 7 | PONTO_7_LIQUIDEZ | Existe liquidez próxima? Spread aceitável na Binance? | | |
| 8 | PONTO_8_INVALIDACAO | Onde está a minha invalidação? Stop definido? | | |
| 9 | PONTO_9_RISCO | Quanto vou arriscar? Position size calculado com ATR? | | |
| 10 | PONTO_10_ALVO | Qual o alvo mínimo? Target 1 definido (1:2)? | | |
| 11 | PONTO_11_RR_RATIO | A relação risco-retorno compensa? R/R >= 1:2? | | |
| 12 | PONTO_12_PLANO_NAO_EMOCAO | Estou a entrar por plano ou emoção? | | |

**Score: ___ / 12**
**Score mínimo para entrada: 12/12**

> Se qualquer ponto = FAIL → **NO_ENTRY**

---

## VERIFICAÇÃO MAC (3 PILARES)

```
M (Movimento):     Tendência clara na direcção do trade?        SIM / NÃO
A (Aceleração):    RSI > 50 subindo + MACD bullish?             SIM / NÃO
C (Confirmação):   OBV RISING + volume confirma?                SIM / NÃO
```

**Os 3 pilares devem ser SIM para PLAYBOOK_OK.**
Se qualquer pilar = NÃO → PLAYBOOK_REJECT → NO_ENTRY

```
Resultado MAC:   PLAYBOOK_OK / PLAYBOOK_REJECT
```

---

## OUTPUTS DOS AGENTES (confirmar antes de entrar)

```
Scout (01):              NO_TRADE / WATCHLIST / SETUP
Flow Analyst (02):       CONFIRMS / CONTRADICTS / INCONCLUSIVE    CONFIDENCE: /10
News Sentinel (03):      LOW / MEDIUM / HIGH / CRITICAL
Score Engine (08):       Score: /35   Tier: PREMIUM / BOA / MÉDIA / IGNORAR
MAC Playbook (09):       PLAYBOOK_OK / PLAYBOOK_REJECT             CONFIDENCE: /10
```

> CONTRADICTS ou CRITICAL → bloqueiam a entrada.
> Score < 22 → NÃO ENTRAR.

---

## EXIT RULES — preencher ANTES de entrar

```
Entry price:          ___________
Stop-loss:            ___________  (ATR × 1.5 abaixo da entrada)
ATR value:            ___________
Stop distance:        ___________  (ATR × 1.5)

Target 1 (1:2):       ___________  (entrada + stop distance × 2)
Target 2 (1:3):       ___________  (entrada + stop distance × 3)

R/R calculado:        1 : ___

Fibonacci 0.382:      ___________
Fibonacci 0.618:      ___________

Gestão de posição:
  50% securing:       ao atingir ROI ≥ 50%
  10% harvesting:     ao atingir ROI ≥ 300%

Trailing stop:
  +1R → stop para break-even
  +2R → stop para +1R
  +3R → stop para +2R

Time stop:            7 dias (posições MAC tácticas)
Position size:        ___________  USDT
% do capital:         ___________  %
```

---

## DECISÃO FINAL

```
Todos os 12 pontos:    PASS / FAIL
MAC 3 pilares:         PLAYBOOK_OK / PLAYBOOK_REJECT
R/R >= 1:2:            SIM / NÃO
Score >= 22/35:        SIM / NÃO

DECISÃO FINAL:         EXECUTION_ALLOWED / EXECUTION_BLOCKED / MANUAL_REVIEW_REQUIRED
```

---

## PROTOCOLO DE EMERGÊNCIA

| Situação | Acção |
|---|---|
| 2 stops consecutivos | Pausa. Espera 24h. Revê o que aconteceu. |
| 3 stops num dia | Stop trading para o dia. Regista incidente. |
| Modo vingança detectado | NO_ENTRY imediato. Fecha o terminal. |
| News HIGH severity | Aguarda normalização. Não abre novas posições. |
| Pipeline DEGRADED | Entra READ_ONLY. Não executa nada. |

---

## REFERÊNCIAS

| Documento | Localização |
|---|---|
| Checklist Pré-Trade | `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt` |
| Política de Saída | `07_OPERACAO/Politica_Saida_Completa_Euru.txt` |
| Regras Mãe | `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` |
| MAC Analyst Output | `04_AGENTES/09_MAC_PLAYBOOK_ANALYST/OUTPUT_FORMAT_FINAL.md` |
| Padrão de Status | `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md` |

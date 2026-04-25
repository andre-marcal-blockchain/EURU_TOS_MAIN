# SIMULATE_SETUP — Euru OS
**Versão:** 1.0
**Última actualização:** 2026-04-05
**Tipo de mudança:** Type 3 (Critical) — requer 48h de espera + aprovação formal
**Referências:** `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md`, `07_OPERACAO/SOP_SEMANAL.txt`

---

## REGRA DE OURO
SIMULATE só activa após o checklist Type 3 estar completamente preenchido e o período de 48h ter decorrido.
Nenhuma paper trade é registada antes da activação formal.

---

## SECÇÃO 1 — O QUE MUDA NO SIMULATE

### 1.1 Diferença fundamental

| Dimensão | READ_ONLY | SIMULATE |
|---|---|---|
| Capital real | Zero | Zero |
| Ordens reais | Proibido | Proibido |
| Registo de trades | Hipóteses informais | Paper trades formais obrigatórias |
| Checklist pré-trade | Opcional (referência) | Obrigatório (12/12 ou NO_ENTRY) |
| Agentes automáticos | Scout, Flow, News, Score | Idem |
| Agentes manuais activos | Quant/Risk (referência) | Quant/Risk + MAC Playbook (formais) |
| Execution Orchestrator | Sempre EXECUTION_BLOCKED | EXECUTION_ALLOWED possível |
| Quality Control (10) | Pós-ciclo ocasional | Obrigatório após cada trade |
| Journal Auditor | Diário (observações) | Diário + auditoria por trade |
| Performance tracking | Não aplicável | Obrigatório (win rate, R/R, drawdown) |

---

### 1.2 Agentes que activam formalmente no SIMULATE

**Já activos (sem mudança de papel):**

| Agente | Papel no SIMULATE |
|---|---|
| Scout (01) | Idem READ_ONLY — estrutura e classificação |
| Flow Analyst (02) | Idem READ_ONLY — CONFIRMS / CONTRADICTS / INCONCLUSIVE |
| News Sentinel (03) | Idem READ_ONLY — severidade e bloqueio de pipeline |
| Score Engine (08) | Idem READ_ONLY — score 0–35 e tier |

**Activação formal no SIMULATE:**

| Agente | Papel activado | Output obrigatório |
|---|---|---|
| Quant/Risk Officer (04) | Risk scoring estruturado em cada SETUP candidato. Calcula position size real (capital × 1% / ATR × 1.5). Valida R/R >= 1:2. | `APPROVE / REJECT / REVIEW` + position size calculado |
| MAC Playbook Analyst (09) | Validação MAC (Movimento + Aceleração + Confirmação) obrigatória antes de cada entrada. Veto de playbook. | `PLAYBOOK_OK / PLAYBOOK_REJECT` + CONFIDENCE 0–10 |
| Execution Orchestrator (05) | Decisão final go/no-go de cada paper trade. Recebe todos os agentes acima. | `EXECUTION_ALLOWED / EXECUTION_BLOCKED / MANUAL_REVIEW_REQUIRED` |
| Journal Auditor (07) | Auditoria formal de cada trade encerrada. Compliance check e registo permanente. | Scorecard por trade + scorecard semanal |
| Quality Control (10) | Validação dos outputs de todos os agentes contra o schema oficial. Corre após cada ciclo de pipeline. | `VALIDATED / SCHEMA_ERROR / MISSING_FIELD` por agente |
| DevOps Guardian (06) | Monitorização 24/7 enquanto paper trades estiverem abertas. Pode forçar READ_ONLY se infra instável. | `HEALTHY / DEGRADED / CRITICAL` contínuo |

---

### 1.3 Novos outputs produzidos no SIMULATE

Além dos relatórios existentes do READ_ONLY, passam a existir:

```
08_DADOS_E_JOURNAL/JOURNAL_TRADES/
  PAPER_TRADE_YYYY-MM-DD_[ASSET].md    — registo por trade (ver Secção 3)

08_DADOS_E_JOURNAL/SCORECARDS/
  SIMULATE_TRACKER.md                  — tabela de performance acumulada (ver Secção 4)
  WEEKLY_SCORECARD_WXX.md              — scorecard semanal do Journal Auditor

09_LOGS_E_INCIDENTES/
  INCIDENTES.md                        — incidentes técnicos e violações de playbook
```

---

### 1.4 O que NÃO muda no SIMULATE

- `SYSTEM_MODE = SIMULATE` em `.env` — nunca usar a `euru_trade_key` para execução real
- Regras Mãe permanecem intactas (risco 1%, max 3 trades/dia, max 2 posições abertas)
- Limites de perda: máximo 2% simulado ao dia, 5% simulado na semana
- Qualquer violação das Regras Mãe em SIMULATE → incidente → revisão obrigatória

---

## SECÇÃO 2 — CHECKLIST TYPE 3 PARA ACTIVAR SIMULATE

**Tipo de mudança:** Type 3 — Estratégico Crítico
**Tempo de espera mínimo:** 48 horas a partir da data de proposta
**Aprovação:** Risk/Product Owner + Automation Engineer em sessões separadas

---

### 2.1 Data e controlo do processo

```
Data de proposta:               ___________
Data mínima de activação:       ___________  (proposta + 48h)
Data efectiva de activação:     ___________
Proposto por:                   Risk/Product Owner (Andre)
Aprovado por (Sessão A):        Risk/Product Owner — ___________  (data + hora)
Aprovado por (Sessão B):        Automation Engineer — ___________  (data + hora, sessão distinta)
```

> Sessão A e Sessão B devem ocorrer em momentos separados.
> A aprovação na mesma sessão invalida o checklist.

---

### 2.2 Critérios de infra-estrutura

```
[ ] Pipeline HEALTHY durante 3+ semanas consecutivas
    Evidência: últimos relatórios SCOUT_REPORT sem DEGRADED
    Semanas verificadas: Week ___, Week ___, Week ___

[ ] Asian scan correu sem falha em 5+ noites consecutivas
    Evidência: ASIAN_REPORT gerado em ___________

[ ] Zero incidentes CRITICAL não resolvidos em aberto
    Verificar: 09_LOGS_E_INCIDENTES/INCIDENTES.md

[ ] Scripts sem erros não tratados nas últimas 2 semanas
    Verificar: logs de execução do euru_morning_scan.py
```

---

### 2.3 Critérios de agentes e outputs

```
[ ] Todos os 10 agentes têm BRIEFING_FINAL.md + PROMPT_REVISADO.md + OUTPUT_FORMAT_FINAL.md
    Verificar: 04_AGENTES/0X_*/

[ ] Scout produz NO_TRADE / WATCHLIST / SETUP consistentemente (sem erros de enum)
[ ] Flow Analyst produz CONFIRMS / CONTRADICTS / INCONCLUSIVE + CONFIDENCE
[ ] News Sentinel produz LOW / MEDIUM / HIGH / CRITICAL sem falsos positivos sistémicos
[ ] Score Engine produz score 0–35 e tier classification correctamente
[ ] Quant/Risk Officer testado manualmente em 3+ cenários SETUP com output APPROVE/REJECT/REVIEW
[ ] MAC Playbook Analyst testado manualmente em 3+ cenários com output PLAYBOOK_OK/PLAYBOOK_REJECT
[ ] Quality Control (10) validado contra schema em pelo menos 1 ciclo completo de pipeline
```

---

### 2.4 Critérios de disciplina operacional

```
[ ] Journal preenchido todos os dias nas últimas 3 semanas
    Verificar: 08_DADOS_E_JOURNAL/JOURNAL_TRADES/

[ ] Nenhuma tentativa de pular etapas documentada
    Verificar: 09_LOGS_E_INCIDENTES/INCIDENTES.md

[ ] Score Engine calibrado — score PREMIUM (28–35) corresponde a assets
    com estrutura e fluxo efectivamente fortes (validado retroactivamente)

[ ] Operador demonstra entendimento do racional de 5+ candidatos WATCHLIST/SETUP
    das últimas semanas (capacidade de articular porquê cada agente decidiu o que decidiu)
```

---

### 2.5 Critérios de governança

```
[ ] DECISOES_ESTRATEGICAS_REVISADO.md actualizado com esta proposta de transição
[ ] Changelog actualizado com a decisão
[ ] .env.example confirma SYSTEM_MODE=SIMULATE (não commitar .env real)
[ ] PROMPT_PRE_TRADE.md preenchido e testado com pelo menos 1 simulação manual
[ ] PROMPT_POST_TRADE.md preenchido e testado com pelo menos 1 simulação manual
[ ] Este ficheiro (SIMULATE_SETUP.md) lido e aprovado por ambos os responsáveis
```

---

### 2.6 Assinatura formal

```
DECISÃO FINAL:   APROVADO / REJEITADO / AGUARDA MAIS EVIDÊNCIA

Risk/Product Owner:
  Nome:           Andre
  Data:           ___________
  Assinatura:     ___________  (texto ou iniciais)
  Observações:    ___________

Automation Engineer:
  Nome:           Andre (sessão distinta)
  Data:           ___________
  Assinatura:     ___________
  Observações:    ___________

Registo obrigatório em:
  [ ] 01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md
  [ ] CHANGELOG.md  (entrada: "YYYY-MM-DD — Transição READ_ONLY → SIMULATE aprovada")
  [ ] Ficheiro dedicado: 01_GOVERNANCA/TRANSICAO_SIMULATE_YYYY-MM-DD.md
```

---

## SECÇÃO 3 — TEMPLATE DE PAPER TRADE

**Guardar em:** `08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_YYYY-MM-DD_[ASSET].md`

---

### 3.1 Cabeçalho

```
TRADE_ID:         PT-YYYY-MM-DD-[ASSET]-[SEQ]   ex: PT-2026-05-10-SOL-001
DATE_ENTRY:       ___________  UTC
DATE_EXIT:        ___________  UTC  (preencher ao fechar)
DURATION:         ___  dias
ASSET:            ___________
TIMEFRAME:        Daily / 4H
SETUP_TYPE:       Breakout / Sweep+Reversal / Reteste / Continuação / Narrativa+Gráfico
SYSTEM_MODE:      SIMULATE
```

---

### 3.2 Plano de entrada

```
ENTRY_PRICE:          ___________
ENTRY_RATIONALE:      ___________  (por que entrar aqui, não 5% acima ou abaixo)

ATR_VALUE:            ___________
STOP_DISTANCE:        ___________  (ATR × 1.5)
STOP_LOSS:            ___________  (entry - stop distance)

TARGET_1:             ___________  (entry + stop distance × 2)   R/R 1:2
TARGET_2:             ___________  (entry + stop distance × 3)   R/R 1:3
FIBONACCI_0382:       ___________
FIBONACCI_0618:       ___________

POSITION_SIZE_USDT:   ___________  (capital × 1% / stop distance)
CAPITAL_BASE:         ___________  USDT (capital simulado total)
PCT_OF_CAPITAL:       ___________  %  (deve ser ~1% de risco)
R/R_PLANNED:          1 : ___
```

---

### 3.3 Outputs dos agentes no momento da entrada

```
Scout (01):
  STATUS:         NO_TRADE / WATCHLIST / SETUP
  OBSERVACAO:     ___________

Flow Analyst (02):
  FLOW_STATUS:    CONFIRMS / CONTRADICTS / INCONCLUSIVE
  RSI:            ___  (> 50 e subindo?)
  MACD:           bullish / bearish / neutral
  OBV:            RISING / FALLING / FLAT
  ATR:            ___
  CONFIDENCE:     /10

News Sentinel (03):
  SEVERITY:       LOW / MEDIUM / HIGH / CRITICAL
  EVENTOS:        ___________
  BLOQUEIA:       SIM / NÃO

Score Engine (08):
  SCORE:          /35
  TIER:           PREMIUM / BOA / MÉDIA / IGNORAR
  ACÇÃO:          ___________

Quant/Risk Officer (04):
  DECISÃO:        APPROVE / REJECT / REVIEW
  POSITION_SIZE:  ___________  USDT
  MAX_LOSS:       ___________  USDT  (1% do capital)
  OBSERVACAO:     ___________

MAC Playbook Analyst (09):
  MOVIMENTO:      SIM / NÃO  (tendência clara?)
  ACELERAÇÃO:     SIM / NÃO  (RSI > 50 + MACD bullish?)
  CONFIRMAÇÃO:    SIM / NÃO  (OBV RISING + volume?)
  DECISÃO:        PLAYBOOK_OK / PLAYBOOK_REJECT
  CONFIDENCE:     /10

Execution Orchestrator (05):
  DECISÃO_FINAL:  EXECUTION_ALLOWED / EXECUTION_BLOCKED / MANUAL_REVIEW_REQUIRED
  MOTIVO:         ___________

Quality Control (10):
  VALIDAÇÃO:      VALIDATED / SCHEMA_ERROR / MISSING_FIELD
  ERROS:          ___________  (se existirem)
```

---

### 3.4 Gestão durante a trade

```
TRAILING_STOP_ACTIVADO:   SIM / NÃO
  +1R → stop para break-even:    ___________  (data/preço)
  +2R → stop para +1R:           ___________
  +3R → stop para +2R:           ___________

50%_SECURING_ACTIVADO:    SIM / NÃO   (ROI ≥ 50%)
  Data:  ___________   Preço:  ___________   USDT liberados:  ___________

10%_HARVESTING_ACTIVADO:  SIM / NÃO   (ROI ≥ 300%)
  Data:  ___________   ROI:  ___________

NOTAS_DURANTE_TRADE:
  ___________
```

---

### 3.5 Fecho da trade

```
EXIT_PRICE:           ___________
EXIT_REASON:          Stop-loss / Target 1 / Target 2 / Time stop / Macro adverso /
                      OBV+RSI divergência / MACD crossover / Suporte perdido / Manual

RESULT_USDT:          ___________  (+ ganho / – perda, simulado)
RESULT_R:             ___________  R
R/R_ACHIEVED:         1 : ___
WIN / LOSS / BREAKEVEN

PLAYBOOK_COMPLIANCE:  FULL / PARTIAL / VIOLATION
  (VIOLATION se: stop movido contra regras, entrada sem checklist, setup fora dos 5 oficiais,
   entrada por emoção, R/R < 1:2 aceite, posição aumentada para recuperar perda)
```

---

### 3.6 Auditoria pós-trade (Journal Auditor)

```
Scout estava certo?         SIM / NÃO / PARCIALMENTE
Flow Analyst estava certo?  SIM / NÃO / PARCIALMENTE
News impactou resultado?    SIM / NÃO
Score reflectia qualidade?  SIM / NÃO

LIÇÃO_PRINCIPAL:    ___________
PADRÃO_ERRO:        ___________  (se loss)
AJUSTE_PROPOSTO:    ___________
TIPO_MUDANÇA:       Type 1 / Type 2 / Type 3 / Nenhum
```

---

## SECÇÃO 4 — TABELA DE PERFORMANCE (SIMULATE TRACKER)

**Ficheiro:** `08_DADOS_E_JOURNAL/SCORECARDS/SIMULATE_TRACKER.md`
**Actualizar:** após cada trade encerrada e no fecho semanal.

---

### 4.1 Tabela de trades

| Trade ID | Data | Asset | Setup | Entry | Exit | Result R | Result USDT | W/L | R/R Plan | R/R Achiev | Compliance | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PT-... | | | | | | | | W/L/BE | 1:_ | 1:_ | FULL/PARTIAL/VIOLATION | /35 |

---

### 4.2 Métricas acumuladas (actualizar semanalmente)

```
PERÍODO:                ___________  a  ___________
TRADES_TOTAL:           ___
TRADES_WIN:             ___
TRADES_LOSS:            ___
TRADES_BREAKEVEN:       ___

WIN_RATE:               ____%   (trades_win / trades_total)
AVG_R_WIN:              ___  R
AVG_R_LOSS:             ___  R  (valor absoluto)
EXPECTANCY:             ___  R  (win_rate × avg_R_win - loss_rate × avg_R_loss)
  > 0 = edge positivo   ≤ 0 = sistema sem edge

AVG_RR_ACHIEVED:        1 : ___  (média de todos os R/R alcançados)
AVG_RR_PLANNED:         1 : ___  (média de todos os R/R planeados)
RR_DEVIATION:           ____%   (diferença — sinaliza saídas prematuras se negativo)

TRADES_OFF_PLAYBOOK:    ___   (deve ser 0 para avançar de fase)
VIOLATIONS:             ___   (FULL → PARTIAL → VIOLATION — tendência deve ser para FULL)

MAX_CONSECUTIVE_LOSS:   ___
MAX_DAILY_LOSS_HIT:     SIM / NÃO   (limite: 2% simulado)
MAX_WEEKLY_LOSS_HIT:    SIM / NÃO   (limite: 5% simulado)

CAPITAL_SIMULADO_INICIAL:   ___________  USDT
CAPITAL_SIMULADO_ACTUAL:    ___________  USDT
NET_RETURN:                 ____%
MAX_DRAWDOWN:               ____%
```

---

### 4.3 Score médio dos setups operados

```
Score médio dos assets em que se entrou:   /35
Score mínimo registado numa entrada:       /35
% das entradas com score >= 22:            ____%  (meta: 100%)
% das entradas com score >= 28 (PREMIUM):  ____%
```

---

### 4.4 Distribuição por setup type

| Setup | Trades | Win | Loss | Win Rate | Avg R/R |
|---|---|---|---|---|---|
| Breakout | | | | | |
| Sweep+Reversal | | | | | |
| Reteste | | | | | |
| Continuação | | | | | |
| Narrativa+Gráfico | | | | | |

> Usar esta tabela para identificar qual setup produz melhor expectância no contexto actual do mercado.

---

### 4.5 Análise de qualidade semanal (resumo rápido)

```
Week ___  (YYYY-MM-DD a YYYY-MM-DD):
  Trades:          ___
  Win rate:        ____%
  Avg R/R:         1 : ___
  Expectancy:      ___  R
  Violations:      ___
  Mercado:         fácil / misto / difícil
  Nota geral:      /10
```

---

## SECÇÃO 5 — CRITÉRIOS PARA CONCLUIR SIMULATE E AVANÇAR PARA EXECUTE

**Tipo de mudança:** Type 3 — requer 48h de espera + aprovação formal (processo idêntico à Secção 2)

A transição SIMULATE → EXECUTE só ocorre quando **todos** os critérios abaixo estiverem satisfeitos.
Não há atalhos. Critérios parciais não contam.

---

### 5.1 Critérios quantitativos mínimos

```
[ ] Mínimo de 3 meses de SIMULATE contínuo
    Data de início SIMULATE:    ___________
    Data mínima de avaliação:   ___________  (+ 90 dias)

[ ] Win rate >= 50% ao longo de toda a amostra
    Win rate actual:            ____%

[ ] R/R médio alcançado >= 1:2
    R/R médio actual:           1 : ___

[ ] Expectancy > 0 R (edge positivo confirmado)
    Expectancy actual:          ___  R

[ ] Zero trades fora do playbook (TRADES_OFF_PLAYBOOK = 0)
    Violations acumuladas:      ___  (deve ser 0)

[ ] Máximo drawdown simulado < 15% do capital
    Max drawdown actual:        ____%

[ ] Limite diário (2%) e semanal (5%) nunca atingidos por imprudência
    (Atingir por mercado adverso com disciplina é aceitável — atingir por excesso de trades não é)
```

---

### 5.2 Critérios qualitativos

```
[ ] Operador consegue articular o racional de cada trade antes de a registar
    (não só depois — prova de processo, não de resultado)

[ ] Pelo menos 3 semanas seguidas com PLAYBOOK_COMPLIANCE = FULL em todas as trades

[ ] Score Engine demonstrou correlação positiva:
    assets com score PREMIUM performaram melhor em média que assets com score BOA/MÉDIA

[ ] Nenhum padrão de revenge trading ou euforia detectado no journal

[ ] Quality Control (10) validou todos os outputs dos últimos 30 ciclos sem SCHEMA_ERROR

[ ] Infraestrutura HEALTHY durante todo o período de SIMULATE
    (máximo: 1–2 episódios DEGRADED recuperados, zero CRITICAL)
```

---

### 5.3 Critérios de governança

```
[ ] Journal Auditor produziu scorecard semanal completo em todas as semanas de SIMULATE
[ ] DECISOES_ESTRATEGICAS_REVISADO.md tem registo de todas as semanas
[ ] Sem violações das Regras Mãe documentadas como não resolvidas
[ ] Protocolo Aguiar (módulos 08–10) integrado e testado em pelo menos 5 trades
[ ] Checklist Type 3 para EXECUTE preenchido (documento separado)
[ ] Aprovação formal Risk/Product Owner + Automation Engineer em sessões distintas
```

---

### 5.4 O que acontece se os critérios não forem atingidos

| Situação | Acção |
|---|---|
| Win rate < 50% após 3 meses | Rever os 5 setups — qual está a falhar? Ajuste Type 2 nos prompts dos agentes. |
| R/R médio < 1:2 | Rever política de saída — saídas prematuras? Trailing stop mal calibrado? |
| Trades off playbook > 0 | SIMULATE não avança. Corrigir disciplina. Novo período mínimo de 4 semanas limpo. |
| Drawdown > 15% | Congelar SIMULATE. Rever limites de risco. Aprovação Type 3 para retomar. |
| Expectancy ≤ 0 | Sistema sem edge — rever Score Engine, Flow Analyst e critérios de entrada. |
| Infraestrutura CRITICAL | Voltar a READ_ONLY até estabilizar. SIMULATE reinicia o contador de tempo. |

---

### 5.5 O que muda ao activar EXECUTE (referência futura)

Ao activar EXECUTE, os seguintes elementos são desbloqueados (apenas após Type 3):

- `euru_trade_key` activada com permissão de execução (actualmente EXECUTION_BLOCKED)
- `SYSTEM_MODE=EXECUTE` no `.env`
- Position sizes com capital real (mantendo exactamente os mesmos parâmetros do SIMULATE)
- Execution Orchestrator passa a enviar ordens reais via API Binance
- DevOps Guardian em modo de vigilância activa 24/7

**Os parâmetros de risco não mudam na transição para EXECUTE.** A única diferença é que o capital é real.

---

## REFERÊNCIAS

| Documento | Localização |
|---|---|
| Governança de Mudanças | `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md` |
| Modo READ_ONLY | `07_OPERACAO/MODO_READ_ONLY.txt` |
| SOP Semanal | `07_OPERACAO/SOP_SEMANAL.txt` |
| Checklist Pré-Trade | `07_OPERACAO/CHECKLIST_PRE_TRADE_v2.txt` |
| Política de Saída | `07_OPERACAO/Politica_Saida_Completa_Euru.txt` |
| Regras Mãe | `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` |
| Decisões Estratégicas | `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` |
| Padrão de Status | `01_GOVERNANCA/PADRAO_UNIFICADO_DE_STATUS_REVISADO.md` |
| Template Pré-Trade | `05_PROMPTS/PROMPT_PRE_TRADE.md` |
| Template Pós-Trade | `05_PROMPTS/PROMPT_POST_TRADE.md` |
| SIMULATE Tracker | `08_DADOS_E_JOURNAL/SCORECARDS/SIMULATE_TRACKER.md` |

# EURU OS — Handoff Definitivo
## Para o chat "Fundação sólida"
### Versão: 2026-04-13 — Pós automação completa

---

## LEIA ISTO PRIMEIRO

Este documento é o ponto de entrada obrigatório para qualquer sessão
de trabalho sobre o Euru OS. Antes de qualquer acção, leia este
documento na íntegra.

---

## 1. Pasta oficial — regra absoluta

```
PASTA OFICIAL DO EURU OS:
C:\Users\andre\Desktop\EURO MAIN

REGRA: Todo o material do Euru — ZIPs, scripts, relatórios,
documentos, ficheiros de governança — vive nesta pasta.
Nunca noutra. Sem excepções.
```

Quando receberes ficheiros para instalar no Euru:
1. Guardar em `EURO MAIN`
2. Extrair em `EURO MAIN`
3. Fazer `cd "C:\Users\andre\Desktop\EURO MAIN"` antes de qualquer comando Git

---

## 2. Repositório GitHub

```
URL:     github.com/andre-marcal-blockchain/Euru_TOS
Branch:  main
Commit:  c7e7858
```

Comandos Git sempre com:
```powershell
cd "C:\Users\andre\Desktop\EURO MAIN"
git add .
git commit -m "..."
git push origin main
```

---

## 3. Estado canônico actual

```
Modo operacional:  READ_ONLY (ADR_0001)
Registry activo:   EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3
Sistema:           TOTALMENTE AUTOMATIZADO
Schema:            22/22 válidos
Agentes:           11/11 OFFICIAL
```

---

## 4. Os 11 agentes — todos OFFICIAL

| Nº | Agente | Ficheiro canônico |
|---|---|---|
| 01 | Scout | EURU_AGENTS_SCOUT_PROMPT_OFFICIAL_v1.0.md |
| 02 | Flow Analyst | EURU_AGENTS_FLOW_ANALYST_PROMPT_OFFICIAL_v1.0.md |
| 03 | News Sentinel | EURU_AGENTS_NEWS_SENTINEL_PROMPT_OFFICIAL_v1.0.md |
| 04 | Quant Risk Officer | EURU_AGENTS_QUANT_RISK_OFFICER_PROMPT_OFFICIAL_v1.0.md |
| 05 | Execution Orchestrator | EURU_AGENTS_EXECUTION_ORCHESTRATOR_PROMPT_OFFICIAL_v1.0.md |
| 06 | DevOps Guardião | EURU_AGENTS_DEVOPS_GUARDIAO_PROMPT_OFFICIAL_v1.0.md |
| 07 | Journal Auditor | EURU_AGENTS_JOURNAL_AUDITOR_PROMPT_OFFICIAL_v1.0.md |
| 08 | Score Engine | EURU_AGENTS_SCORE_ENGINE_PROMPT_OFFICIAL_v1.0.md |
| 09 | Watchdog | EURU_AGENTS_WATCHDOG_PROMPT_OFFICIAL_v1.0.md |
| 10 | MAC Playbook Analyst | EURU_AGENTS_MAC_PLAYBOOK_ANALYST_PROMPT_OFFICIAL_v1.0.md |
| 11 | Quality Control | EURU_AGENTS_QUALITY_CONTROL_PROMPT_OFFICIAL_v1.0.md |

Todos os prompts estão em `04_AGENTES/<pasta_agente>/`.
Nenhum agente usa ficheiros `_REVISADO` — esses são legacy e ignorados.

---

## 5. Scripts operacionais activos

| Script | Função |
|---|---|
| `euru_morning_scan.py` | Scout 18 ativos + BTC filter + score diário |
| `euru_asian_scan.py` | Compressão e coil na sessão asiática |
| `euru_journal_auditor.py` | Journal diário automático (AGT-07) |
| `euru_friday_cycle.py` | Pipeline semanal completo (entrypoint oficial) |
| `euru_schema_validator.py` | Validação YAML de todos os ficheiros |
| `euru_learning_preflight.py` | Gate de governança antes do learning |
| `euru_learning_engine.py` | Motor de aprendizagem semanal |
| `euru_scorecard_engine.py` | Scorecards multidimensionais (5 dimensões) |
| `euru_threshold_registry.py` | Thresholds versionados |
| `euru_flow_analyst.py` | Análise de flow (usado pelo morning scan) |

**Regra absoluta:** o agendador aponta SEMPRE para `euru_friday_cycle.py`.
Nunca directamente para learning, scorecard ou preflight.

---

## 6. Agendamento Windows activo

| Tarefa | Horário | Script |
|---|---|---|
| Euru_Asian_Scan | 02:00 diário | euru_asian_scan.py |
| Euru_Morning_Scan | 07:00 diário | euru_morning_scan.py |
| Euru_Journal_Auditor | 07:30 diário | euru_journal_auditor.py |
| Euru_Friday_Cycle | 20:30 sextas | euru_friday_cycle.py |
| Euru_GitHub_Sync | automático | — |
| Euru_Smoke_Test_Night | automático | — |

Todos apontam para `C:\Users\andre\Desktop\EURO MAIN`.

---

## 7. Friday Cycle v1.1 — pipeline oficial

```
GitHub Sync
    ↓
Schema Validator (22/22 obrigatório)
    ↓
Learning Preflight (gate obrigatório)
    ↓
Learning Engine
    ↓
Learning Report
    ↓
Scorecard Engine (5 dimensões)
    ↓
Human Governance Review
    ↓
Weekly Close
```

Nenhuma fase pode ser saltada.
Schema inválido bloqueia tudo.
Preflight é a permissão oficial para o learning correr.

---

## 8. Scorecards multidimensionais (v1.1)

O Scorecard Engine gera 5 tipos de scorecard por semana:

```
SCORECARD_system_euru_tos_<semana>.md      ← sistema global
SCORECARD_asset_<symbol>_<semana>.md       ← por ativo
SCORECARD_setup_<setup>_<semana>.md        ← por setup
SCORECARD_agent_<agente>_<semana>.md       ← por agente
SCORECARD_score_engine_<perfil>_<semana>.md ← qualidade do scoring
```

Localização: `08_DADOS_E_JOURNAL/SCORECARDS/SCORECARDS/`

---

## 9. Setup activo — trend_continuation

Definido em `00_GOVERNANCA/SCHEMAS/EURU_SETUP_TREND_CONTINUATION_OFFICIAL_v1.0.md`

Checklist de 14 critérios obrigatórios.
10 disqualificadores explícitos.
Qualquer entrada deve passar 14/14 antes de ser executada.

---

## 10. Watchlist activa

Ficheiro: `08_DADOS_E_JOURNAL/WATCHLISTS/EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2.md`

```
TIER_1_PREMIUM:  18 ativos (análise diária)
TIER_2_MONITOR:  10 ativos (monitorização semanal)
TIER_3_BULL_CYCLE: 5 ativos (2027+)
LISTA_PROIBIDA:  9 ativos (nunca operar)
```

Todos os 33 ativos activos validados na Binance Futures em Abril 2026.

---

## 11. Roadmap para SIMULATE e EXECUTE

### Critérios para SIMULATE (estimativa: Junho 2026)

| # | Critério | Estado |
|---|---|---|
| 1 | 10 ciclos Friday sem falhas críticas | ⏳ acumula automaticamente |
| 2 | Todos os agentes OFFICIAL | ✅ 11/11 |
| 3 | 20 trades fechados com métricas reais | ⏳ acumula automaticamente |
| 4 | Schema quality válida | ✅ 22/22 |
| 5 | Registry actualizado | ✅ |
| 6 | ADR_0003 + documento OFFICIAL | ⏳ criar quando 1+3 prontos |

### Thresholds mínimos para EXECUTE

```
win_rate       ≥ 52%
average_rr     ≥ 2.1
expectancy     ≥ 0.05
prediction_acc ≥ 62.5%
```

### Critérios para EXECUTE (estimativa: Set/Out 2026)
SIMULATE activo + 20 trades com métricas acima dos thresholds + ADR_0004

---

## 12. O que o operador faz

```
Diário    → Verificar SCOUT_REPORT (5 min — opcional)
Semanal   → Verificar FRIDAY_CYCLE_REPORT (10 min)
Por trade → Quando fechar, comunicar preço/data para actualizar YAML
Quando REVIEW_REQUIRED → aprovar ou rejeitar
```

O sistema faz tudo o resto automaticamente.

---

## 13. Hierarquia documental — em caso de conflito

1. EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
2. EURU_DOCUMENT_POLICY_OFFICIAL_v1.0
3. ADRs (01_GOVERNANCA/ADR_*)
4. Governance / Policies
5. Agent Prompts OFFICIAL
6. Briefings / Output Formats
7. Drafts / Logs / Notes

---

## 14. Regras que nunca podem ser violadas

```
1. Nunca aprender de ficheiros com schema inválido
2. Nunca gerar scorecards sem learning report
3. Nunca saltar o preflight
4. Nunca tratar warnings como sucesso silencioso
5. Nunca alterar estado operacional sem ADR + documento OFFICIAL
6. Nunca criar documentos OFFICIAL sem cabeçalho canônico
7. Nunca usar prompts _REVISADO — apenas _OFFICIAL
8. Nunca apontar o agendador directamente para learning ou scorecard
9. Todo o material Euru vai para EURO MAIN — sem excepções
10. Sempre fazer git push após qualquer alteração
```

---

## 15. Instrução para a IA que receber este handoff

```
Você está a continuar o projecto EURU OS após a sessão de
automação completa de 2026-04-12/13.

ESTADO: READ_ONLY — sistema totalmente automatizado.

PASTA OFICIAL: C:\Users\andre\Desktop\EURO MAIN
Qualquer ficheiro, script ou ZIP gerado vai para esta pasta.
Qualquer comando Git começa com:
cd "C:\Users\andre\Desktop\EURO MAIN"

AGENTES: 11/11 OFFICIAL — não regredir para _REVISADO.

PIPELINE: Friday Cycle v1.1 é o entrypoint oficial.
Nunca chamar learning, scorecard ou preflight directamente.

QUALIDADE: Schema deve estar sempre 22/22 válidos.
Se um ficheiro novo for criado, deve ter cabeçalho YAML correcto.

PRÓXIMAS PRIORIDADES:
1. Monitorizar ciclos e trades (automático)
2. Criar AGT-12 Altcoin Futures Portfolio Orchestrator
3. Quando critérios 1+3 cumpridos → ADR_0003 → SIMULATE

COMUNICAÇÃO ENTRE AGENTES:
Todos os agentes falam a mesma língua — os schemas YAML.
Qualquer output de agente que não respeite o schema é inválido.
O validator é a fonte de verdade — 22/22 é o mínimo aceitável.

QUANDO RECEBERES UM FICHEIRO NOVO:
1. Verificar se tem cabeçalho YAML correcto
2. Correr euru_schema_validator.py
3. Confirmar 22/22 antes de qualquer commit
4. Fazer git push para EURO MAIN
```

---

## 16. Ficheiros de referência obrigatórios para nova sessão

Entregar sempre estes ficheiros no início de cada sessão:

| # | Ficheiro | Onde está |
|---|---|---|
| 1 | EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1.md | 00_MASTER/ |
| 2 | EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md | 00_MASTER/ |
| 3 | EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.md | 01_GOVERNANCA/ |
| 4 | Este handoff | — |

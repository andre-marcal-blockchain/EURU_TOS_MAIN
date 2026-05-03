# EURU_PLANO_FASE1_OBSERVACAO_2026-04-29.md

**Sistema:** Euru OS
**Repositório:** EURU TOS MAIN
**Data de redacção:** 2026-04-29
**Status:** PROPOSTA — pendente aprovação Type 2
**Fase do sistema:** SIMULATE (transitando para SIMULATE-OBSERVATION)
**Operador:** André Marçal
**Tipo de mudança:** Type 2 (reactivação de scheduled tasks em modo READ_ONLY)
**Período de cooling-off:** 24h após registo formal como Type 2
**Autoridade de execução:** Nenhuma. Este documento autoriza apenas observação. Nenhuma entrada (paper trade ou real) é autorizada por este plano.

---

## 1. CONTEXTO

A migração Type 3 (EURO MAIN → EURU TOS MAIN) foi executada em 2026-04-27 e validada em E2 T+24h em 2026-04-28 com status GREEN. O sistema autónomo confirmou-se funcional (Daily Audit e Journal Auditor a correr automaticamente, com push para o repositório canónico).

Em paralelo, foram commitados dois documentos canónicos:

- `00_MASTER/EURU_BRUNO_AGUIAR_MAC_KNOWLEDGE_BASE.md` (commit 87f787f) — knowledge base do método operacional
- `00_MASTER/EURU_SYSTEM_AUDIT_BRUNO_MAC_2026-04-28.md` (commit e19ca02) — auditoria honesta do estado actual versus método

A auditoria identificou que:

- A infra-estrutura pós-migração está GREEN.
- Vários scripts de mercado existem mas estão parcialmente implementados.
- As tasks operacionais de mercado (Morning Scan, Asian Scan, Trade Monitor) estão actualmente DISABLED.
- Componentes-chave do método (MAC_VALID, Two-Day OBV, LONG_CANDIDATE/SHORT_CANDIDATE no Core, Quant/Risk Officer, Execution Orchestrator) NÃO estão implementados como código executável.

A recomendação final do System Audit (Secção 11) foi:

> "Reactivar olhos em modo READ_ONLY/SIMULATE-observation controlado, depois implementar MAC_VALID, long/short candidates, Two-Day OBV e auditoria de coerência metodológica antes de qualquer lógica de entrada em paper-trade ser confiável."

Este plano formaliza a primeira fase desse caminho: **observação READ_ONLY durante 14 dias antes de qualquer enhancement técnico.**

---

## 2. REFERÊNCIAS

| Documento | Commit | Função |
|---|---|---|
| EURU_BRUNO_AGUIAR_MAC_KNOWLEDGE_BASE.md | 87f787f | Definição metodológica |
| EURU_SYSTEM_AUDIT_BRUNO_MAC_2026-04-28.md | e19ca02 | Estado actual do sistema |
| DECISOES_ESTRATEGICAS_REVISADO.md (Type 3 entry) | c55639e | Migração executada |
| EURU_AICollaboration_Policy_DRAFT_v0.3 | (pendente Type 2 separado) | Governança Codex/Claude |

---

## 3. OBJECTIVO DA FASE 1

Reactivar os "olhos de mercado" do Euru OS em modo READ_ONLY durante 14 dias para:

1. Confirmar que a infra-estrutura pós-migração suporta operação contínua sem intervenção.
2. Acumular dados reais de mercado (Morning, Asian, Trade Monitor) gerados pelo sistema.
3. Permitir ao operador avaliar qualitativamente se os candidatos LONG/SHORT detectados pelo sistema são coerentes com a metodologia Bruno Aguiar / MAC.
4. Identificar gaps concretos entre o que o sistema gera e o que o método exige, para informar prioridades da Fase 2 (enhancements técnicos).
5. Gerar trilha de auditoria completa (reports diários + revisão do operador) que serve como ground truth para implementação futura.

**Esta fase NÃO autoriza:**

- Abertura de paper trades novos.
- Modificação de código.
- Reactivação de tasks fora do escopo deste plano.
- Transição para SIMULATE com entradas (mesmo simuladas) ou EXECUTE.

---

## 4. DURAÇÃO E CALENDÁRIO

| Marco | Data | O que acontece |
|---|---|---|
| Aprovação Type 2 | T+0 (≥24h após registo) | Cooling-off completo, plano aprovado |
| Início Fase 1 | T+0 (mesmo dia da aprovação) | Reactivação das 3 tasks |
| Checkpoint intermédio | T+7d | Revisão do operador: continuar, recalibrar ou abortar |
| Fim Fase 1 | T+14d | Avaliação final dos 8 critérios |
| Decisão pós-Fase 1 | T+14d | Avançar Fase 2, prolongar Fase 1, ou recalibrar |

**Início proposto:** 2026-04-29 (hoje), condicional a aprovação Type 2 com cooling-off de 24h. Se aprovado em 2026-04-30 (manhã), Fase 1 corre de 2026-04-30 a 2026-05-14.

**Nota:** se cooling-off ainda não cumprido, início desliza proporcionalmente.

---

## 5. TASKS REACTIVADAS

As 3 tasks abaixo serão reactivadas no início da Fase 1.

| Task | Estado actual | Estado durante Fase 1 | Modo | Frequência |
|---|---|---|---|---|
| Euru_Morning_Scan | Disabled | Ready | READ_ONLY (gera report, não opera) | Daily 07:00 |
| Euru_Asian_Scan | Disabled | Ready | READ_ONLY (gera report) | Daily 02:00 |
| Euru_Trade_Monitor | Disabled (sem task scheduled actual) | Ready ou execução manual diária | `--dry-run` obrigatório | Daily |

**Notas operacionais:**

- Trade Monitor deve correr com flag `--dry-run` para garantir que não fecha paper trades existentes nem cria estado novo.
- Se Trade Monitor não tem task scheduled definida, decidir antes de Fase 1: criar task nova ou execução manual operacional.
- Reactivação faz-se via `Enable-ScheduledTask` em PowerShell elevado (Run as Administrator real, validado pelo title da janela).

---

## 6. TASKS QUE PERMANECEM DISABLED

Decisão consciente do operador, registada para auditoria:

| Task | Razão para manter Disabled |
|---|---|
| Euru_GitHub_Sync | Push automático já ocorre via Daily_Audit. Reactivar criaria risco de commits duplicados. Investigação técnica antes de qualquer reactivação. |
| Euru_Friday_Cycle | Falhou última execução (24 Abr, Result=1). Bug não investigado. Não faz sentido sem paper trades activos. |
| EuruLearningEngine | Aprende de paper trades fechados. Em Fase 1 (READ_ONLY) não há paper trades novos. Reactivar quando entrar em SIMULATE com paper trades. |

**Implicação:** estas tasks ficam Disabled durante toda a Fase 1. Reactivação só acontece em fase posterior, com nova governança.

---

## 7. CRITÉRIOS DE SUCESSO (8)

Para a Fase 1 ser considerada bem-sucedida (e portanto avançar para Fase 2), os 8 critérios abaixo devem ser satisfeitos ao fim de 14 dias:

| # | Critério | Como medir |
|---|---|---|
| A | Sistema correu 14 dias sem falhas críticas | Tasks Ready com Result=0 na maioria dos dias |
| B | Daily Audit sem incidentes graves | Zero CRITICAL, poucos FAIL nos audit reports |
| C | Reports gerados consistentemente cada dia útil | Morning, Asian, Trade Monitor presentes nos paths esperados |
| D | Git sync automático funcional | Commits diários a aparecer em origin EURU_TOS_MAIN |
| E | Avaliação qualitativa de candidatos coerente com método | Operador valida cada candidato gerado, opinião documentada |
| F | Sistema não gera candidatos quando BTC SIDEWAYS | BTC Master Filter a comportar-se conforme Knowledge Base |
| H | Operador preencheu CANDIDATES_REVIEW.md | Tabela de revisão actualizada conforme protocolo |
| J | Zero modificações de código durante observação | git log mostra apenas reports automáticos, nenhum commit de código |

**Critério E (avaliação qualitativa):** sem mínimo numérico de candidatos. Se o sistema gerar zero candidatos em 14 dias, é motivo de investigação técnica (pode ser bug, não calibração legítima do método).

---

## 8. GATILHOS DE ABORT (4)

Se qualquer um dos 4 gatilhos abaixo ocorrer durante a Fase 1, observação é PAUSADA imediatamente.

| # | Gatilho | Acção |
|---|---|---|
| A | Falhas técnicas críticas (tasks Ready falham 2 dias consecutivos, Daily Audit reporta CRITICAL, git sync deixa de funcionar) | PAUSE imediato. Investigar. Reiniciar contagem se possível. |
| B | Sinais metodológicos errados (sistema gera LONG com BTC BEARISH, OBV FALLING para LONG, inconsistências graves) | PAUSE. Registar finding. Decidir se enhancement Fase 2 é prioritário antes de continuar. |
| C | Drift do operador (não leu reports há 5+ dias, tabela CANDIDATES_REVIEW.md por preencher) | PAUSE consciente. Retomar quando operador tiver bandwidth. |
| D | Modificação não-autorizada de código (Codex, Claude, outra IA, ou operador por engano) | PAUSE imediato. Reverter mudança. Investigar antes de retomar. |

**PAUSE significa:**

- Tasks reactivadas voltam a Disabled (manualmente).
- Contagem de 14 dias é interrompida.
- Documento de incident report é criado.
- Operador decide: retomar (com correcção), recalibrar, ou abortar definitivamente.

---

## 9. COMPROMISSO DO OPERADOR

Para o critério H (tabela CANDIDATES_REVIEW.md preenchida) ser cumprido, o operador compromete-se a:

**Frequência mínima sugerida:** 3 vezes por semana (terça, quinta, sábado).

> NOTA AO OPERADOR: confirmar ou ajustar esta frequência durante revisão deste documento. Pode ser diária, 3x/semana, ou outra. Realista é melhor que ambicioso.

**Tarefas em cada sessão de revisão:**

1. Ler reports gerados desde a sessão anterior (Morning Scan, Asian Scan, Trade Monitor).
2. Para cada candidato detectado pelo sistema, preencher uma linha em `EURU_FASE1_CANDIDATES_REVIEW.md`.
3. Validar consistência metodológica: BTC context, MAC alinhado, OBV, RSI, MACD, narrativa.
4. Anotar quaisquer inconsistências graves para potencial gatilho B.

**Se o operador não conseguir manter este compromisso durante 5 dias consecutivos, gatilho C é accionado.**

---

## 10. ARTEFACTOS A PRODUZIR DURANTE FASE 1

| Artefacto | Localização | Gerado por |
|---|---|---|
| Morning Scan reports diários | `08_DADOS_E_JOURNAL/SCORECARDS/SCOUT_REPORT_*.md` | Sistema (automático) |
| Asian Scan reports diários | `08_DADOS_E_JOURNAL/ASIAN_REPORTS/ASIAN_REPORT_*.md` | Sistema (automático) |
| Trade Monitor reports diários | `08_DADOS_E_JOURNAL/SCORECARDS/TRADE_MONITOR_REPORT_*.md` | Sistema (automático, dry-run) |
| Daily Audit reports diários | `08_DADOS_E_JOURNAL/AUDIT_REPORTS/DAILY_AUDIT_REPORT_*.md` | Sistema (automático) |
| Journal diários | `08_DADOS_E_JOURNAL/JOURNAL_DAILY/JOURNAL_*.md` | Sistema (automático) |
| Tabela de revisão Bruno-style | `00_MASTER/EURU_FASE1_CANDIDATES_REVIEW.md` | **Operador** (manual) |
| Incident reports (se PAUSE) | `00_MASTER/INCIDENTS/INCIDENT_FASE1_*.md` | Operador / Codex / Claude |
| Checkpoint intermédio T+7d | `00_MASTER/EURU_FASE1_CHECKPOINT_T7D_*.md` | Operador (com input Codex) |
| Avaliação final T+14d | `00_MASTER/EURU_FASE1_AVALIACAO_FINAL_*.md` | Operador (com input Codex e Claude) |

---

## 11. ESTRUTURA DA TABELA `EURU_FASE1_CANDIDATES_REVIEW.md`

Template a criar no início da Fase 1:

```markdown
# EURU_FASE1_CANDIDATES_REVIEW.md

**Período:** YYYY-MM-DD a YYYY-MM-DD (14 dias)
**Operador:** André Marçal
**Status:** ACTIVE / PAUSED / COMPLETED

## Tabela de Revisão

| Date | Asset | TF | BTC State | Sistema (Candidate) | Eu (Bruno-style) | Razão | Concorda? |
|------|-------|----|-----------|--------------------|--------------------|-------|-----------|
| 2026-04-30 | (exemplo) | 4H | SIDEWAYS | LONG_CANDIDATE WLDUSDT | NO_TRADE | BTC sideways, deveria ser WATCHLIST | ❌ |

## Notas e Findings
- (notas qualitativas do operador)

## Inconsistências Detectadas
- (inputs para potential gatilho B)
```

Tabela é actualizada manualmente pelo operador conforme protocolo da Secção 9.

---

## 12. DECISÃO PÓS-FASE 1

Ao fim de 14 dias, operador toma decisão consciente baseada nos critérios:

**Cenário 1 — Todos os 8 critérios cumpridos:**
→ Avançar para Fase 2 (implementação técnica de MAC_VALID, Two-Day OBV, LONG/SHORT_CANDIDATE no Core, etc.). Submeter Type 2 separado para cada enhancement.

**Cenário 2 — 5-7 critérios cumpridos:**
→ Avaliar quais critérios falharam. Se gaps são técnicos (B, F), priorizar enhancements relacionados antes de prolongar observação. Se gaps são humanos (C, H), prolongar Fase 1 com compromisso revisto.

**Cenário 3 — Menos de 5 critérios cumpridos OU gatilho de abort accionado:**
→ Investigar causa-raiz. Recalibrar plano. Não avançar para Fase 2 sem nova auditoria.

**Em todos os cenários:** decisão pós-Fase 1 é registada formalmente em `DECISOES_ESTRATEGICAS_REVISADO.md` antes de qualquer próximo passo.

---

## 13. RISCOS E MITIGAÇÕES

| Risco | Mitigação |
|---|---|
| Operador esquece de ler reports | Gatilho C, frequência mínima clara, alertas se 3 dias sem leitura |
| Sistema gera candidatos errados não detectados | Gatilho B, comparação com Knowledge Base, revisão Codex no T+7d |
| Tasks reactivadas falham silenciosamente | Daily Audit detecta, gatilho A, alerta diário |
| Modificação acidental de código | Gatilho D, .gitignore não toca scripts, audit periódico |
| Drift de escopo (alguém adiciona "só mais uma task") | Plano explícito sobre as 6 tasks, qualquer mudança = novo Type 2 |
| Cooling-off não respeitado | Submissão como Type 2 força cooling-off, registo formal antes de início |

---

## 14. APROVAÇÃO

**Status:** PROPOSTA — pendente revisão e aprovação

**Para aprovação como Type 2:**

- [ ] Operador revê documento integralmente
- [ ] Operador confirma frequência de revisão (Secção 9)
- [ ] Documento commitado em `00_MASTER/`
- [ ] Entrada formal em `DECISOES_ESTRATEGICAS_REVISADO.md` como "Type 2 — Plano Fase 1 — em cooling-off"
- [ ] Cooling-off de 24h cumprido
- [ ] Aprovação registada em `DECISOES_ESTRATEGICAS_REVISADO.md`
- [ ] Reactivação técnica das 3 tasks executada
- [ ] Tabela `EURU_FASE1_CANDIDATES_REVIEW.md` criada
- [ ] Início Fase 1 marcado em log

**Aprovação humana explícita exigida antes de cada um destes passos.**

---

## 15. NOTAS FINAIS

Este plano foi co-redigido pelo operador André Marçal e Claude (assistente IA externa, sob governança documentada). Codex será solicitado a fazer revisão técnica antes da aprovação final como Type 2.

A intenção é manter o ritmo da migração — pequeno, auditável, reversível — agora aplicado à reactivação metodológica.

**Lembrete operacional:** quando em dúvida durante a Fase 1, o padrão é PAUSE (gatilhos) e NO_TRADE (método). Velocidade não é objectivo. Trilha de auditoria é.

---

**Operador:** André Marçal (Risk/Product Owner, decisão final)
**Suporte governança:** Claude (análise estratégica, framing)
**Suporte técnico:** Codex (revisão técnica, auditoria, implementação)
**Memória comum:** repositório EURU TOS MAIN
**Trilha de auditoria:** Git

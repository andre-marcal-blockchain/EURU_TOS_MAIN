\# EURU\_PLANO\_FASE1\_OBSERVACAO\_2026-04-29\_v0.3.1.md



\*\*Sistema:\*\* Euru OS

\*\*Repositório:\*\* EURU TOS MAIN

\*\*Data de redacção (v0.1):\*\* 2026-04-29

\*\*Data desta revisão (v0.3.1):\*\* 2026-04-29

\*\*Status:\*\* APROVADO TECNICAMENTE — pendente registo Type 2 e cooling-off

\*\*Fase do sistema:\*\* SIMULATE (transitando para SIMULATE-OBSERVATION)

\*\*Operador:\*\* André Marçal

\*\*Tipo de mudança:\*\* Type 2 (reactivação de scheduled tasks em modo READ\_ONLY + criação de task Trade Monitor)

\*\*Período de cooling-off:\*\* 24h após registo formal como Type 2

\*\*Autoridade de execução:\*\* Nenhuma. Este documento autoriza apenas observação. Nenhuma entrada (paper trade ou real) é autorizada por este plano.



\*\*Revisão v0.3.1 — alteração vs v0.3:\*\* correcção cosmética sobre identificação da janela PowerShell elevada (texto agora language-agnostic). Detalhe na Secção 16.



\*\*Convenção de fuso horário:\*\* todos os horários neste documento são em \*\*Europe/Madrid\*\* (CEST/CET conforme época), salvo indicação contrária explícita.



\---



\## 1. CONTEXTO



A migração Type 3 (EURO MAIN → EURU TOS MAIN) foi executada em 2026-04-27 e validada em E2 T+24h em 2026-04-28 com status GREEN. O sistema autónomo confirmou-se funcional (Daily Audit e Journal Auditor a correr automaticamente, com push para o repositório canónico). T+48h checkpoint em 2026-04-29 também GREEN.



Em paralelo, foram commitados dois documentos canónicos:



\- `00\_MASTER/EURU\_BRUNO\_AGUIAR\_MAC\_KNOWLEDGE\_BASE.md` (commit 87f787f) — knowledge base do método operacional

\- `00\_MASTER/EURU\_SYSTEM\_AUDIT\_BRUNO\_MAC\_2026-04-28.md` (commit e19ca02) — auditoria honesta do estado actual versus método



A auditoria identificou que:



\- A infra-estrutura pós-migração está GREEN.

\- Vários scripts de mercado existem mas estão parcialmente implementados.

\- As tasks operacionais de mercado (Morning Scan, Asian Scan) estão actualmente DISABLED.

\- Trade Monitor existe como script (`euru\_trade\_monitor.py`) mas \*\*não tem scheduled task definida\*\* — exige criação de task nova ou execução manual diária.

\- Componentes-chave do método (MAC\_VALID, Two-Day OBV, LONG\_CANDIDATE/SHORT\_CANDIDATE no Core, Quant/Risk Officer, Execution Orchestrator) NÃO estão implementados como código executável. Apenas o Breakout Scanner (`euru\_breakout\_scanner.py`) tem direccionalidade LONG/SHORT explícita.



A recomendação final do System Audit (Secção 11) foi:



> "Reactivar olhos em modo READ\_ONLY/SIMULATE-observation controlado, depois implementar MAC\_VALID, long/short candidates, Two-Day OBV e auditoria de coerência metodológica antes de qualquer lógica de entrada em paper-trade ser confiável."



Este plano formaliza a primeira fase desse caminho: \*\*observação READ\_ONLY durante 14 dias antes de qualquer enhancement técnico.\*\*



\---



\## 2. REFERÊNCIAS



| Documento | Commit | Função |

|---|---|---|

| EURU\_BRUNO\_AGUIAR\_MAC\_KNOWLEDGE\_BASE.md | 87f787f | Definição metodológica |

| EURU\_SYSTEM\_AUDIT\_BRUNO\_MAC\_2026-04-28.md | e19ca02 | Estado actual do sistema |

| DECISOES\_ESTRATEGICAS\_REVISADO.md (Type 3 entry) | c55639e | Migração executada |

| EURU\_AICollaboration\_Policy\_DRAFT\_v0.3 | (pendente Type 2 separado) | Governança Codex/Claude |



\---



\## 3. OBJECTIVO DA FASE 1



Reactivar os "olhos de mercado" do Euru OS em modo READ\_ONLY durante 14 dias para:



1\. Confirmar que a infra-estrutura pós-migração suporta operação contínua sem intervenção.

2\. Acumular dados reais de mercado (Morning, Asian, Trade Monitor) gerados pelo sistema.

3\. Permitir ao operador avaliar qualitativamente se os sinais detectados pelo sistema (SETUP, WATCHLIST, GEM\_ALERT, Breakout LONG/SHORT quando aplicável) são coerentes com a metodologia Bruno Aguiar / MAC.

4\. Identificar gaps concretos entre o que o sistema gera e o que o método exige, para informar prioridades da Fase 2 (enhancements técnicos).

5\. Gerar trilha de auditoria completa (reports diários + revisão do operador) que serve como ground truth para implementação futura.



\*\*Importante — sobre direccionalidade:\*\* o sistema actual gera estados como `SETUP`, `WATCHLIST`, `NO\_TRADE`, `GEM\_ALERT` no Core Pipeline. Apenas o Breakout Scanner (se for executado) gera `direction = LONG / SHORT / NONE`. O Core ainda não distingue formalmente `LONG\_CANDIDATE` vs `SHORT\_CANDIDATE`. Esta ausência é precisamente um dos gaps a observar e potencialmente endereçar em Fase 2.



\*\*Esta fase NÃO autoriza:\*\*



\- Abertura de paper trades novos.

\- Modificação de código.

\- Reactivação de tasks fora do escopo deste plano.

\- Transição para SIMULATE com entradas (mesmo simuladas) ou EXECUTE.



\---



\## 4. DURAÇÃO E CALENDÁRIO



Todos os horários em \*\*Europe/Madrid\*\*.



| Marco | Data | O que acontece |

|---|---|---|

| Aprovação Type 2 | T+0 (≥24h após registo) | Cooling-off completo, plano aprovado |

| Início Fase 1 | T+0 (mesmo dia da aprovação) | Reactivação das tasks + criação de Trade Monitor task |

| Checkpoint intermédio | T+7d | Revisão do operador: continuar, recalibrar ou abortar |

| Fim Fase 1 | T+14d | Avaliação final dos 8 critérios |

| Decisão pós-Fase 1 | T+14d | Avançar Fase 2, prolongar Fase 1, ou recalibrar |



\*\*Início proposto:\*\* 2026-04-30 (após cooling-off de 24h sobre registo de 2026-04-29). Fase 1 corre nominalmente de 2026-04-30 a 2026-05-14.



\*\*Nota:\*\* se cooling-off ainda não cumprido, início desliza proporcionalmente.



\---



\## 5. TASKS A REACTIVAR OU CRIAR



A Fase 1 envolve \*\*duas operações técnicas distintas\*\*, não apenas reactivação:



\### 5.1 Reactivação de tasks existentes (Enable-ScheduledTask)



| Task | Estado actual | Estado durante Fase 1 | Modo | Frequência | Hora (Europe/Madrid) |

|---|---|---|---|---|---|

| Euru\_Morning\_Scan | Disabled (existe) | Ready | READ\_ONLY (gera report, não opera) | Daily | 07:00 |

| Euru\_Asian\_Scan | Disabled (existe) | Ready | READ\_ONLY (gera report) | Daily | 02:00 |



\*\*Acção técnica:\*\* `Enable-ScheduledTask -TaskName Euru\_Morning\_Scan` e `Enable-ScheduledTask -TaskName Euru\_Asian\_Scan`, em PowerShell elevado real (Run as Administrator), confirmado antes da execução.



\### 5.2 Criação de task nova (Register-ScheduledTask)



| Task | Estado actual | Estado durante Fase 1 | Modo | Frequência | Hora (Europe/Madrid) |

|---|---|---|---|---|---|

| Euru\_Trade\_Monitor | \*\*NÃO EXISTE\*\* | A criar Ready | `--dry-run` obrigatório | Daily | 07:30 (após Morning Scan) |



\*\*Sequência operacional obrigatória (em ordem):\*\*



\*\*Passo 5.2.1 — Validação manual primeiro (sem scheduler):\*\*



Antes de criar a task scheduled, executar manualmente uma vez para validar Python, paths, dependências e geração de relatório:



```powershell

cd "C:\\Users\\andre\\Desktop\\EURU TOS MAIN"

python .\\euru\_trade\_monitor.py --dry-run

```



\*\*Critério de validação:\*\* o comando deve completar sem erros e gerar `08\_DADOS\_E\_JOURNAL/SCORECARDS/TRADE\_MONITOR\_REPORT\_\*.md`. Se falhar, \*\*PARAR\*\* e investigar antes de qualquer Register-ScheduledTask.



\*\*Passo 5.2.2 — Criação da task (apenas se 5.2.1 validou):\*\*



Executar comando Register-ScheduledTask conforme \*\*Apêndice A\*\* deste documento, em PowerShell elevado real.



\*\*Passo 5.2.3 — Verificação imediata da task criada:\*\*



```powershell

Get-ScheduledTask -TaskName Euru\_Trade\_Monitor | Select-Object TaskName, State

Get-ScheduledTaskInfo -TaskName Euru\_Trade\_Monitor

```



Estado esperado: `Ready`. NextRunTime apontando para 07:30 do dia seguinte (ou hoje se ainda não passou).



\*\*Alternativa contingente:\*\* se Passo 5.2.1 falhar e investigação demorar, executar Trade Monitor manualmente cada dia útil (operador) durante Fase 1, com criação de task adiada para depois.



\---



\## 6. TASKS QUE PERMANECEM DISABLED



Decisão consciente do operador, registada para auditoria:



| Task | Razão para manter Disabled |

|---|---|

| Euru\_GitHub\_Sync | Push automático já ocorre via Daily\_Audit. Reactivar criaria risco de commits duplicados. Investigação técnica antes de qualquer reactivação. |

| Euru\_Friday\_Cycle | Falhou última execução (24 Abr, Result=1). Bug não investigado. Não faz sentido sem paper trades activos. |

| EuruLearningEngine | Aprende de paper trades fechados. Em Fase 1 (READ\_ONLY) não há paper trades novos. Reactivar quando entrar em SIMULATE com paper trades. |



\*\*Implicação:\*\* estas tasks ficam Disabled durante toda a Fase 1. Reactivação só acontece em fase posterior, com nova governança.



\---



\## 7. CRITÉRIOS DE SUCESSO (8)



Para a Fase 1 ser considerada bem-sucedida (e portanto avançar para Fase 2), os 8 critérios abaixo devem ser satisfeitos ao fim de 14 dias:



| Critério | Descrição | Como medir |

|---|---|---|

| A | Sistema correu 14 dias sem falhas críticas | Tasks Ready com Result=0 na maioria dos dias |

| B | Daily Audit sem incidentes graves | Zero CRITICAL, poucos FAIL nos audit reports |

| C | Reports gerados consistentemente cada dia útil | Morning, Asian, Trade Monitor presentes nos paths esperados |

| D | Git sync automático funcional | Commits diários a aparecer em origin EURU\_TOS\_MAIN |

| E | Avaliação qualitativa de sinais coerente com método | Operador valida cada sinal SETUP/WATCHLIST/GEM\_ALERT/Breakout gerado, opinião documentada |

| F | BTC Master Filter comporta-se conforme método | Sistema \*\*não promove\*\* sinais para SETUP/entrada quando BTC SIDEWAYS; sinais devem ser downgraded para WATCHLIST salvo excepção manual justificada. NO\_TRADE para sinais LONG quando BTC BEARISH (e vice-versa). |

| G | Operador preencheu CANDIDATES\_REVIEW.md | Tabela de revisão actualizada conforme protocolo da Secção 9 |

| H | Zero modificações de código durante observação | git log mostra apenas reports automáticos, nenhum commit de código fora deste plano |



\*\*Critério E (avaliação qualitativa):\*\* sem mínimo numérico de sinais. Se o sistema gerar zero sinais em 14 dias, é motivo de investigação técnica (pode ser bug, não calibração legítima do método).



\*\*Critério F (clarificação):\*\* o objectivo não é silenciar o sistema em BTC SIDEWAYS. O objectivo é validar que o BTC Master Filter está a fazer o downgrade correcto (SETUP → WATCHLIST), não a deixar sinais LONG promovidos a SETUP em condições adversas. Observação activa permanece em todos os regimes BTC.



\---



\## 8. GATILHOS DE ABORT (4)



Se qualquer um dos 4 gatilhos abaixo ocorrer durante a Fase 1, observação é PAUSADA imediatamente.



| Gatilho | Descrição | Acção |

|---|---|---|

| A | Falhas técnicas críticas (tasks Ready falham 2 dias consecutivos, Daily Audit reporta CRITICAL, git sync deixa de funcionar) | PAUSE imediato. Investigar. Reiniciar contagem se possível. |

| B | Sinais metodológicos errados (sistema promove SETUP LONG com BTC BEARISH; OBV FALLING para sinal LONG; inconsistências graves vs Knowledge Base) | PAUSE. Registar finding. Decidir se enhancement Fase 2 é prioritário antes de continuar. |

| C | Drift do operador (não leu reports há 5+ dias consecutivos, tabela CANDIDATES\_REVIEW.md por preencher) | PAUSE consciente. Retomar quando operador tiver bandwidth. |

| D | Modificação não-autorizada de código (Codex, Claude, outra IA, ou operador por engano) | PAUSE imediato. Reverter mudança. Investigar antes de retomar. |



\*\*PAUSE significa:\*\*



\- Tasks reactivadas voltam a Disabled (manualmente, em PowerShell elevado).

\- Trade Monitor task é Disabled (se foi criada).

\- Contagem de 14 dias é interrompida.

\- Documento de incident report é criado em `00\_MASTER/INCIDENTS/`.

\- Operador decide: retomar (com correcção), recalibrar, ou abortar definitivamente.



\---



\## 9. COMPROMISSO DO OPERADOR



Para o critério G (tabela CANDIDATES\_REVIEW.md preenchida) ser cumprido, o operador compromete-se a:



\*\*Frequência:\*\* \*\*diariamente, antes das 09:00 hora local Madrid.\*\*



\*\*Racional desta janela:\*\* Daily Audit corre às 08:30. Operador lê reports e preenche tabela entre 08:30 e 09:00 (ou antes das 08:30 com reports do dia anterior). A leitura \*\*precede\*\* o início do dia operacional.



\*\*Tarefas em cada sessão de revisão:\*\*



1\. Ler reports gerados desde a sessão anterior (Morning Scan, Asian Scan, Trade Monitor).

2\. Para cada sinal detectado pelo sistema (SETUP, WATCHLIST, GEM\_ALERT, Breakout direction), preencher uma linha em `EURU\_FASE1\_CANDIDATES\_REVIEW.md`.

3\. Validar consistência metodológica: BTC context, MAC alinhado (M/A/C qualitativo), OBV, RSI, MACD, narrativa.

4\. Anotar quaisquer inconsistências graves para potencial gatilho B.



\*\*Se o operador não conseguir manter este compromisso durante 5 dias consecutivos, gatilho C é accionado.\*\*



\*\*Realismo:\*\* o operador reconhece que dias de viagem, indisponibilidade ou esquecimento podem ocorrer. Até 4 dias consecutivos de não-leitura são tolerados (reset da contagem ao retomar). Acima de 5 dias consecutivos = PAUSE consciente, não falha.



\---



\## 10. ARTEFACTOS A PRODUZIR DURANTE FASE 1



| Artefacto | Localização | Gerado por |

|---|---|---|

| Morning Scan reports diários | `08\_DADOS\_E\_JOURNAL/SCORECARDS/SCOUT\_REPORT\_\*.md` | Sistema (automático) |

| Asian Scan reports diários | `08\_DADOS\_E\_JOURNAL/SCORECARDS/ASIAN\_REPORT\_\*.md` | Sistema (automático) |

| Trade Monitor reports diários | `08\_DADOS\_E\_JOURNAL/SCORECARDS/TRADE\_MONITOR\_REPORT\_\*.md` | Sistema (automático, dry-run) ou operador (manual, dry-run) |

| Daily Audit reports diários | `08\_DADOS\_E\_JOURNAL/AUDIT\_REPORTS/DAILY\_AUDIT\_REPORT\_\*.md` | Sistema (automático) |

| Journal diários | `08\_DADOS\_E\_JOURNAL/JOURNAL\_DAILY/JOURNAL\_\*.md` | Sistema (automático) |

| Tabela de revisão Bruno-style | `00\_MASTER/EURU\_FASE1\_CANDIDATES\_REVIEW.md` | \*\*Operador\*\* (manual) |

| Incident reports (se PAUSE) | `00\_MASTER/INCIDENTS/INCIDENT\_FASE1\_\*.md` | Operador / Codex / Claude |

| Checkpoint intermédio T+7d | `00\_MASTER/EURU\_FASE1\_CHECKPOINT\_T7D\_\*.md` | Operador (com input Codex) |

| Avaliação final T+14d | `00\_MASTER/EURU\_FASE1\_AVALIACAO\_FINAL\_\*.md` | Operador (com input Codex e Claude) |



\*\*Nota sobre paths:\*\* todos os reports do sistema (Morning, Asian, Trade Monitor) escrevem em `SCORECARDS/`. Não existe pasta `ASIAN\_REPORTS/` separada.



\---



\## 11. ESTRUTURA DA TABELA `EURU\_FASE1\_CANDIDATES\_REVIEW.md`



Template a criar no início da Fase 1:



```markdown

\# EURU\_FASE1\_CANDIDATES\_REVIEW.md



\*\*Período:\*\* YYYY-MM-DD a YYYY-MM-DD (14 dias)

\*\*Operador:\*\* André Marçal

\*\*Status:\*\* ACTIVE / PAUSED / COMPLETED

\*\*Timezone:\*\* Europe/Madrid



\## Tabela de Revisão



| Date | Asset | TF | BTC State | Sinal Sistema | Eu (Bruno-style) | Razão | Concorda? |

|------|-------|----|-----------|----------------|--------------------|-------|-----------|

| 2026-04-30 | (exemplo) | 4H | SIDEWAYS | SETUP WLDUSDT | NO\_TRADE / WATCHLIST | BTC sideways, deveria ter sido downgraded a WATCHLIST | NO |



\## Notas e Findings

\- (notas qualitativas do operador)



\## Inconsistências Detectadas

\- (inputs para potential gatilho B)

```



\*\*Coluna "Sinal Sistema"\*\* captura o estado tal como o sistema actual o emite: `SETUP`, `WATCHLIST`, `GEM\_ALERT`, `NO\_TRADE`, ou `BREAKOUT\_LONG/SHORT` (Breakout Scanner). Não força nomenclatura `LONG\_CANDIDATE/SHORT\_CANDIDATE` que ainda não existe no Core.



\*\*Coluna "Eu (Bruno-style)"\*\* captura a opinião do operador como se fosse Bruno Aguiar a olhar para o mesmo dado.



Tabela é actualizada manualmente pelo operador conforme protocolo da Secção 9.



\---



\## 12. DECISÃO PÓS-FASE 1



Ao fim de 14 dias, operador toma decisão consciente baseada nos critérios:



\*\*Cenário 1 — Todos os 8 critérios cumpridos:\*\*

→ Avançar para Fase 2 (implementação técnica de MAC\_VALID, Two-Day OBV, LONG\_CANDIDATE/SHORT\_CANDIDATE no Core, etc.). Submeter Type 2 separado para cada enhancement.



\*\*Cenário 2 — 5-7 critérios cumpridos:\*\*

→ Avaliar quais critérios falharam. Se gaps são técnicos (B, F), priorizar enhancements relacionados antes de prolongar observação. Se gaps são humanos (C, G), prolongar Fase 1 com compromisso revisto.



\*\*Cenário 3 — Menos de 5 critérios cumpridos OU gatilho de abort accionado:\*\*

→ Investigar causa-raiz. Recalibrar plano. Não avançar para Fase 2 sem nova auditoria.



\*\*Em todos os cenários:\*\* decisão pós-Fase 1 é registada formalmente em `DECISOES\_ESTRATEGICAS\_REVISADO.md` antes de qualquer próximo passo.



\---



\## 13. RISCOS E MITIGAÇÕES



| Risco | Mitigação |

|---|---|

| Operador esquece de ler reports | Gatilho C, frequência diária clara, tolerância de 4 dias |

| Sistema gera sinais errados não detectados | Gatilho B, comparação com Knowledge Base, revisão Codex no T+7d |

| Tasks reactivadas falham silenciosamente | Daily Audit detecta, gatilho A, alerta diário |

| Modificação acidental de código | Gatilho D, audit periódico, .gitignore não toca scripts |

| Drift de escopo (alguém adiciona "só mais uma task") | Plano explícito sobre as 6 tasks + Trade Monitor novo, qualquer mudança = novo Type 2 |

| Cooling-off não respeitado | Submissão como Type 2 força cooling-off, registo formal antes de início |

| Trade Monitor task nova introduz bugs | Validação manual obrigatória antes de Register-ScheduledTask (Secção 5.2.1); Codex valida XML/comando |



\---



\## 14. APROVAÇÃO



\*\*Status:\*\* APROVADO TECNICAMENTE PELO CODEX (v0.3.1) — pendente registo Type 2 e cooling-off



\*\*Para aprovação como Type 2:\*\*



\- \[x] Codex revê v0.2 e confirma correcções aplicadas

\- \[x] Codex fornece comando completo para criação de Trade Monitor task (Apêndice A)

\- \[x] Operador revê documento integralmente

\- \[x] Operador confirma frequência de revisão (Secção 9): diariamente antes 09:00

\- \[ ] Documento commitado em `00\_MASTER/` como v0.3.1

\- \[ ] Entrada formal em `DECISOES\_ESTRATEGICAS\_REVISADO.md` como "Type 2 — Plano Fase 1 — em cooling-off"

\- \[ ] Cooling-off de 24h cumprido

\- \[ ] Aprovação registada em `DECISOES\_ESTRATEGICAS\_REVISADO.md`

\- \[ ] Validação manual de Trade Monitor (Secção 5.2.1) — `python .\\euru\_trade\_monitor.py --dry-run` sem erros

\- \[ ] Reactivação técnica das 2 tasks existentes executada (Morning\_Scan, Asian\_Scan)

\- \[ ] Criação técnica da Trade Monitor task executada (Apêndice A) — apenas se validação manual passou

\- \[ ] Verificação pós-criação da Trade Monitor task (Secção 5.2.3)

\- \[ ] Tabela `EURU\_FASE1\_CANDIDATES\_REVIEW.md` criada

\- \[ ] Início Fase 1 marcado em log



\*\*Aprovação humana explícita exigida antes de cada um destes passos.\*\*



\---



\## 15. NOTAS FINAIS



Este plano foi co-redigido pelo operador André Marçal e Claude (assistente IA externa, sob governança documentada). Codex fez revisão técnica em 2026-04-29:



\- v0.1 → v0.2: 6 correcções factuais e metodológicas.

\- v0.2 → v0.3: incorporação de validação manual antes do scheduler + comando Register-ScheduledTask completo no Apêndice A.

\- v0.3 → v0.3.1: correcção cosmética sobre identificação da janela PowerShell elevada (language-agnostic).



Codex aprovou tecnicamente v0.3.1 como pronta para submissão Type 2.



A intenção é manter o ritmo da migração — pequeno, auditável, reversível — agora aplicado à reactivação metodológica.



\*\*Lembrete operacional:\*\* quando em dúvida durante a Fase 1, o padrão é PAUSE (gatilhos) e NO\_TRADE (método). Velocidade não é objectivo. Trilha de auditoria é.



\---



\## 16. CHANGELOG



\### v0.3.1 — 2026-04-29 (correcção cosmética language-agnostic)



\*\*Correcções de robustez:\*\*



1\. \*\*Secção 5.1:\*\* referência ao título da janela PowerShell elevada removida. Texto antigo "PowerShell elevado real (Run as Administrator com title 'Administrador: Windows PowerShell')" substituído por "PowerShell elevado real (Run as Administrator), confirmado antes da execução". Razão: título da janela varia por idioma do SO (espanhol, português, inglês) e por versão (PowerShell 5 vs PowerShell 7). Codex levantou esta observação durante revisão final de v0.3.



2\. \*\*Apêndice A:\*\* mesma correcção aplicada à pré-condição da sessão.



\*\*Sem alterações ao comando técnico, à lógica do plano, aos critérios ou aos gatilhos.\*\* Esta é uma revisão exclusivamente cosmética.



\### v0.3 — 2026-04-29 (após aprovação técnica Codex de v0.2)



\*\*Adições:\*\*



1\. \*\*Secção 5.2 expandida em sub-passos sequenciais:\*\*

&#x20;  - 5.2.1: Validação manual obrigatória antes do scheduler

&#x20;  - 5.2.2: Criação da task via Register-ScheduledTask (Apêndice A)

&#x20;  - 5.2.3: Verificação imediata pós-criação

&#x20;  - Alternativa contingente clarificada (execução manual diária se validação falhar)



2\. \*\*Apêndice A adicionado\*\* com comando PowerShell completo para criação de Euru\_Trade\_Monitor task (fornecido pelo Codex).



3\. \*\*Secção 14 (checklist)\*\* actualizada para incluir validação manual antes de Register-ScheduledTask e verificação imediata pós-criação.



4\. \*\*Secção 13 (Riscos)\*\* actualizada: mitigation de "Trade Monitor task nova introduz bugs" agora inclui validação manual obrigatória.



\*\*Decisões do operador incorporadas em v0.3:\*\*



5\. \*\*Apêndice A em vez de inline\*\* — opção B escolhida pelo operador (manter Secção 5.2 legível, comando completo auditável no Apêndice).



\### v0.2 — 2026-04-29 (após revisão Codex de v0.1)



\*\*Correcções factuais:\*\*



1\. \*\*Path do Asian Scan corrigido:\*\* `08\_DADOS\_E\_JOURNAL/ASIAN\_REPORTS/` → `08\_DADOS\_E\_JOURNAL/SCORECARDS/`. Path real do script `euru\_asian\_scan.py`.

2\. \*\*Trade Monitor distinguido:\*\* Secção 5 dividida em 5.1 (reactivação tasks existentes) e 5.2 (criação de task nova). Trade Monitor não tem task scheduled actualmente; exige Register-ScheduledTask, não Enable-ScheduledTask.

3\. \*\*Substituição de "LONG\_CANDIDATE/SHORT\_CANDIDATE":\*\* estes estados não existem no Core actual. Substituídos por nomenclatura real do sistema: `SETUP`, `WATCHLIST`, `GEM\_ALERT`, `NO\_TRADE`, `BREAKOUT\_LONG/SHORT` (este último apenas no Breakout Scanner).



\*\*Correcções metodológicas:\*\*



4\. \*\*Critério F suavizado:\*\* "Sistema não gera candidatos quando BTC SIDEWAYS" alterado para "BTC Master Filter comporta-se conforme método: downgrade SETUP → WATCHLIST em SIDEWAYS, NO\_TRADE para sinais contrários ao regime BTC". Alinhado com Knowledge Base (Módulo 01).



\*\*Correcções de governança:\*\*



5\. \*\*Numeração dos critérios limpa:\*\* A-J com saltos → A-H consecutivo. Coerente com numeração A-D dos gatilhos de abort.

6\. \*\*Timezone explícito:\*\* todos os horários agora declarados como Europe/Madrid. Cabeçalho do documento e secção de duração explicitam convenção.



\*\*Decisões do operador incorporadas em v0.2:\*\*



7\. \*\*Frequência de revisão:\*\* diariamente, antes das 09:00 hora local Madrid (Secção 9).



\### v0.1 — 2026-04-29 (versão inicial)



Versão inicial co-redigida pelo operador e Claude. Incompleta tecnicamente em pontos detectados pelo Codex; substituída por v0.2.



\---



\## APÊNDICE A — COMANDO DE CRIAÇÃO DA TASK Euru\_Trade\_Monitor



\*\*Origem:\*\* fornecido pelo Codex em 2026-04-29 durante revisão técnica do plano.



\*\*Pré-condição obrigatória:\*\* Passo 5.2.1 (validação manual `python .\\euru\_trade\_monitor.py --dry-run`) deve ter passado sem erros antes de executar este comando.



\*\*Sessão obrigatória:\*\* PowerShell elevado real (Run as Administrator), confirmado antes da execução.



\*\*Comando completo:\*\*



```powershell

$EuruRoot   = "C:\\Users\\andre\\Desktop\\EURU TOS MAIN"

$TaskName   = "Euru\_Trade\_Monitor"

$ScriptPath = Join-Path $EuruRoot "euru\_trade\_monitor.py"

$PythonExe  = (Get-Command python).Source



if (-not (Test-Path $ScriptPath)) {

&#x20;   throw "Script not found: $ScriptPath"

}



$Action = New-ScheduledTaskAction `

&#x20;   -Execute $PythonExe `

&#x20;   -Argument "`"$ScriptPath`" --dry-run" `

&#x20;   -WorkingDirectory $EuruRoot



$Trigger = New-ScheduledTaskTrigger -Daily -At "07:30"



$Settings = New-ScheduledTaskSettingsSet `

&#x20;   -StartWhenAvailable `

&#x20;   -AllowStartIfOnBatteries `

&#x20;   -DontStopIfGoingOnBatteries `

&#x20;   -MultipleInstances IgnoreNew



$Principal = New-ScheduledTaskPrincipal `

&#x20;   -UserId "$env:USERDOMAIN\\$env:USERNAME" `

&#x20;   -LogonType Interactive `

&#x20;   -RunLevel Highest



Register-ScheduledTask `

&#x20;   -TaskName $TaskName `

&#x20;   -Action $Action `

&#x20;   -Trigger $Trigger `

&#x20;   -Settings $Settings `

&#x20;   -Principal $Principal `

&#x20;   -Description "Runs Euru Trade Monitor in dry-run/report-only mode daily at 07:30 Europe/Madrid." `

&#x20;   -Force

```



\*\*Verificação imediata após execução (Passo 5.2.3):\*\*



```powershell

Get-ScheduledTask -TaskName Euru\_Trade\_Monitor | Select-Object TaskName, State

Get-ScheduledTaskInfo -TaskName Euru\_Trade\_Monitor

```



\*\*Resultado esperado:\*\*



\- `State`: `Ready`

\- `NextRunTime`: 07:30 do dia seguinte (ou hoje se ainda não passou)

\- `LastRunTime`: vazio (nunca correu via scheduler — só via validação manual)

\- `LastTaskResult`: irrelevante na primeira verificação



\*\*Em caso de falha do Register-ScheduledTask:\*\*



1\. NÃO criar task com método alternativo improvisado.

2\. Capturar mensagem de erro completa.

3\. Incluir em incident report `00\_MASTER/INCIDENTS/INCIDENT\_FASE1\_\*.md`.

4\. Activar alternativa contingente (Secção 5.2): execução manual diária pelo operador.

5\. Registar como gap para investigação técnica em Fase 2.



\---



\*\*Operador:\*\* André Marçal (Risk/Product Owner, decisão final)

\*\*Suporte governança:\*\* Claude (análise estratégica, framing)

\*\*Suporte técnico:\*\* Codex (revisão técnica, auditoria, implementação)

\*\*Memória comum:\*\* repositório EURU TOS MAIN

\*\*Trilha de auditoria:\*\* Git


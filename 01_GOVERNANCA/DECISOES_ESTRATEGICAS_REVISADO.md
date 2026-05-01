# Decisões Estratégicas — Euru OS (Revisado)
Este documento consolida de forma clara e cronológica as decisões estratégicas tomadas para o Euru OS. Cada entrada especifica a data, o assunto, o estado e um breve resumo, facilitando o acompanhamento e auditoria.
## 27 de Março de 2026
### Criação da estrutura inicial
- **Estado:** aprovado.  
- **Resumo:** criação do Euru OS em modo `READ_ONLY`, estabelecendo a base do projecto.
### Eliminação de chaves API pré‑existentes
- **Estado:** executado.  
- **Resumo:** chaves de origem desconhecida (AndreMarcal e AndreGottardi) foram eliminadas para evitar riscos de acesso não autorizado.
### Criação de três chaves API
- **Estado:** aprovado.  
- **Resumo:** criadas `euru_research_key`, `euru_userdata_key` e `euru_trade_key` com permissão apenas de leitura. A chave de trade está com execução bloqueada até transição de fase.
### Revisão de documentos de governança
- **Estado:** aprovado.  
- **Resumo:** os cinco documentos de governança foram lidos e aprovados, validando a estrutura inicial de regras.
## 28 de Março de 2026
### Reorganização da estrutura de pastas
- **Estado:** executado.  
- **Resumo:** a pasta do projecto foi reorganizada para uma estrutura mais lógica e navegável.
## 29 de Março de 2026
### Reescrita do SOP_DIARIO em formato de checklist
- **Estado:** aprovado (mudança tipo 1).  
- **Resumo:** o SOP_DIARIO será convertido num checklist conciso que possa ser executado em 30 minutos sem consultar outros documentos.  
- **Espera mínima:** 1 dia antes da execução.
## 30 de Março de 2026
### Direção estratégica para automatização total
- **Estado:** intenção declarada.  
- **Resumo:** o Euru passará progressivamente por cinco etapas: (1) `READ_ONLY` manual → (2) `READ_ONLY` automatizado → (3) `SIMULATE` manual → (4) `SIMULATE` automatizado → (5) `EXECUTE`.  O princípio é automatizar apenas o que foi validado manualmente.
### Identificação da ferramenta Paperclip
- **Estado:** pendente.  
- **Resumo:** considerar a adopção da plataforma Paperclip (paperclipai/paperclip) para orquestrar os agentes após concluir a fase de Claude Code (semanas 6–8).
### Estudo do Protocolo Aguiar
- **Estado:** em estudo.  
- **Resumo:** investigar o framework de 10 módulos que inclui filtros de tendência, arquitectura de capital 5/5/90, escalonamento dinâmico de risco, daemons de segurança, confirmação de volume, gatilhos de recuperação, protocolos de travamento e colheita.  
  - **Fase 1 (Semanas 3–4):** estudo dos módulos.  
  - **Fase 2 (Semanas 5–6):** aplicação em modo `SIMULATE`.  
  - **Fase 3 (Semanas 6–7):** codificação nas prompts dos agentes.  
  - **Fase 4 (Semanas 7–8):** automatização via Claude Code.
### Referências de Bruno Aguiar e Claude Code
- **Estado:** conteúdos analisados.  
- **Resumo:** vídeos sobre gestão emocional e uso de Claude com Pine Script foram estudados. Conclusões principais:  
  - Perder dinheiro decorre de abandonar a gestão de risco.  
  - Equilíbrio emocional é mais importante que estratégia.  
  - Automatização ajuda a reduzir o viés emocional.  
  - Backtests não garantem performance futura; é necessário validar estratégias em modo `SIMULATE`.
## 1 de Abril de 2026
### Plano de expansão de alt‑coins
- **Estado:** planeado.  
- **Resumo:** adicionar as 20 principais alt‑coins ao *morning scan* nas semanas 5–6, e incorporar a sessão asiática de 4 horas nas semanas 7–8. No modo `SIMULATE`, implementar a detecção de “gemas” segundo o Protocolo Aguiar.
## 2 de Abril de 2026
### Pesquisa sobre watchlist de alt‑coins
- **Estado:** em revisão.  
- **Resumo:** análise de lista com top 50 alt‑coins categorizadas em blue chips, infra‑estrutura, utilidade, etc., para definir novas watchlists.
### Método MAC e Trading Playbook profissional
- **Estado:** aprovado para integração gradual.  
- **Resumo:** integrar o Método MAC (Movimento + Aceleração + Confirmação) nas sessões asiáticas e incorporar setups e checklists de um playbook profissional.
### Aprovação da distribuição de capital 50/25/15/10
- **Estado:** aprovada.  
- **Resumo:** distribuir a carteira entre categorias Core (50 %), Crescimento (25 %), Assimétrico (15 %) e Especulativo (10 %), alinhando com o playbook.
## 3 de Abril de 2026
### Dream Team — 11 perfis especializados
- **Estado:** aprovado para integração gradual.  
- **Resumo:** mapear 11 perfis (8 já cobertos pelos 7 agentes existentes). Identificadas lacunas em Tokenomics/On‑chain, Compliance/Legal e Gestor de Relacionamento, a serem preenchidas em fases futuras (Execução e escala 2027–2028).
### Expansão operacional da semana 4
- **Estado:** executado.  
- **Resumo:**  
  - *Morning scan* expandido para 20 activos.  
  - News Sentinel integrado ao CoinTelegraph.  
  - REGRAS_MAE codificadas em YAML.  
  - Criado `CHECKLIST_PRE_TRADE.md` em `07_OPERACAO`.  
  - Watchlist oficial dividida em quatro níveis.  
  - Dream Team validado.  
  - Lista de activos Binance Perpetual guardada.
### Definição dos indicadores técnicos do Flow Analyst
- **Estado:** aprovado para implementação na semana 5.  
- **Resumo:**  
  - **RSI 14 períodos** para medir momentum e aceleração.  
  - **MACD 12/26/9** para confirmar a direcção.  
  - **OBV** para avaliar o fluxo de volume.  
  - **ATR 14** para medir a volatilidade e ajustar stops.  
  - **Fórmula de dimensionamento:** posição = capital × 1 % / (ATR × 1,5).  
  - *Pipeline* definido: **Scout → Flow Analyst → News Sentinel → Quant/Risk → Execução**.  
  - Próximo passo: implementar o Flow Analyst na semana 5.
## 2026-04-06 - PROPOSTA FORMAL: Transicao para SIMULATE
Tipo de mudanca: Type 3 (Estrategico Critico)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-06
Periodo de espera: 48 horas
Activacao prevista: 2026-04-08 (nao antes)

CRITERIOS VERIFICADOS:
- Infraestrutura: HEALTHY 6+ semanas
- 10 agentes definidos com documentacao completa
- Score Engine calibrado com dados reais
- Journal consistente
- CHECKLIST_PRE_TRADE v2 pronto
- REGRAS_MAE_REVISADO.yaml codificado

CRITERIOS PENDENTES:
- Quant/Risk Officer nao automatizado (calculos manuais)
- MAC Analyst nao automatizado (validacao manual)
- Execution Orchestrator nao automatizado

DECISAO: Activar SIMULATE em modo SEMI-MANUAL
- Scout + Flow + News + Score: automaticos
- Quant/Risk + MAC + Execution: manuais via Claude Code
- Journal: manual diario

Operador: Andre (Risk/Product Owner)

## 2026-04-08 - SIMULATE ACTIVADO
Tipo: Type 3 executado
Data activacao: 2026-04-08
Periodo 48h: cumprido (proposta 2026-04-06)
Autorizacao: Risk/Product Owner Andre
Modo: SIMULATE semi-manual
Primeiro paper trade: PAPER_TRADE_001 AVAXUSDT
BTC em  - aproximando  short squeeze zone
System status: SIMULATE - HEALTHY

## 2026-04-08 - SIMULATE ACTIVADO - Primeiros paper trades
SIMULATE activado formalmente (48h governance cumprida)
PAPER_TRADE_001 AVAXUSDT: entry 9.22 stop 8.501 T1 10.658
PAPER_TRADE_002 NEARUSDT: entry 1.34 stop 1.2272 T1 1.5656
Exposicao combinada: 24.71% capital
Risco total: 2% (1% por trade)
System status: SIMULATE - HEALTHY

## 2026-04-15 - Breakout Intelligence Layer integrado
9 novos agentes: Alert Radar, Structure Hunter, Breakout Confirmation
Market Regime, Risk Guardian, Tactical Execution
Compounding Governor, Journal Learning, Promise Auditor
27 ficheiros de agentes (PROMPT + BRIEFING + OUTPUT_FORMAT)
8 ficheiros tecnicos (schema, weights, scoring, flow, governance, learning, handoff)
CLAUDE.md actualizado com Breakout Layer section
EURU_AGENT_MAP.md criado em 00_MASTER
Total agentes Euru OS: 20 (11 core + 9 breakout)
System status: SIMULATE - HEALTHY

## 2026-04-16 - PROPOSTA FORMAL: Automacao de Exit Logic (euru_trade_monitor.py)
Tipo de mudanca: Type 2 (Moderada - Automacao de logica de estrategia)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-16
Periodo de espera: 24 horas
Activacao prevista: 2026-04-17 (nao antes das 08:00)

CONTEXTO:
- Entry logic totalmente automatizada (morning/asian scan)
- Exit logic documentada em PAPER_TRADE_*.md mas executada manualmente
- PT001/PT002 fechados manualmente 2026-04-15 (time stop)
- PT003 ARBUSDT com time stop em 2026-04-18 - sem automacao de fecho

OBJECTIVO:
Criar euru_trade_monitor.py que aplica automaticamente as regras de saida
documentadas em Politica_Saida_Completa_Euru.txt a todos os paper trades
com status: open.

REGRAS A AUTOMATIZAR (por ordem de prioridade):
1. Stop loss hit -> close imediato (exit_reason: stop_loss)
2. Target 1 hit -> close 50% + trail stop (exit_reason: target_1_partial)
3. Target 2 hit -> close remainder (exit_reason: target_2)
4. Close abaixo do 7D_AVG -> close (exit_reason: invalidation)
5. Time stop expirado -> close (exit_reason: time_stop)
6. RSI > 75 stalling -> close 50% (exit_reason: rsi_overbought_partial)
7. News HIGH adverse asset-specific -> alert (manual review flag)

ARQUITECTURA:
- Script independente: euru_trade_monitor.py
- Le PAPER_TRADE_*.md com status: open via YAML front matter
- Fetcha preco actual da Binance (API publica, read-only)
- Avalia regras em ordem de prioridade; primeira que accionar = decisao
- Edita YAML do ficheiro (status, exit_datetime, exit_price, pnl_usdt,
  pnl_pct, rr_achieved, exit_reason, days_held)
- Gera TRADE_MONITOR_REPORT_YYYY-MM-DD.md com decisoes
- Commit + push via euru_git_sync

INTEGRACAO:
- Chamado no final de euru_morning_scan.py apos scan principal
- Antes de euru_git_sync.git_sync()
- Modo --dry-run para teste antes de activacao real

SAFETY NET:
- Primeira execucao em --dry-run contra PT003 para validar logica
- Revisao humana do TRADE_MONITOR_REPORT antes de activar escrita real
- 18 Abr: time stop PT003 = primeiro teste live com supervisao humana

CRITERIOS DE APROVACAO (apos 24h cooling-off):
- Logica implementada conforme documentacao
- Dry-run produz decisoes coerentes com regras
- Ficheiros YAML mantem integridade apos edicao automatica
- Nao ha conflitos com schema validator

Operador: Andre (Risk/Product Owner)
Status: PENDING (24h wait ate 2026-04-17 08:00)

## 2026-04-18 - INCIDENT REPORT: Rule 8 Violation (PT004 XRPUSDT)

Tipo: Incident Report
Data: 2026-04-18
Operador: Andre Marcal
Severidade: HIGH
Status: RESOLVED

RESUMO:
PT004 XRPUSDT foi aberto em 2026-04-18T08:35:00Z com 
news_severity_at_entry: high, violando a Regra 8 das regras 
inviolaveis ("Never act on HIGH severity news. Extra cautious 
mode - no new entries").

CONTEXTO:
- Entry price: 1.4700 | Stop: 1.3725 | Planned RR: 2.0
- News Sentinel HIGH activo (3o dia consecutivo)
- A documentacao do trade foi gerada por uma IA auxiliar externa 
  (nao-Claude) que reinterpretou "HIGH severity" como aceitavel 
  por nao ser asset-specific adverse. Essa interpretacao nao esta 
  suportada pela redaccao literal da Regra 8.

ACCAO TOMADA:
- PT004 fechado em 2026-04-18T09:00:00Z apos identificacao do breach
- Exit price: 1.4706 | P&L: +0.01 USDT | RR: 0.06R
- Trade tagged: governance_breach + rule_8_violation_closed
- Incidente reconhecido pelo operador

LICOES:
1. Regras inviolaveis sao literais e nao devem ser reinterpretadas 
   por IAs auxiliares.
2. Trades iniciados fora do pipeline validado do Euru OS carregam 
   risco de governanca adicional.
3. A disciplina de admitir e corrigir o erro preserva a integridade 
   do sistema.

FOLLOW-UP:
- Type 2 proposal pendente: Definir protocolo para trades iniciados 
  por IAs auxiliares externas ao pipeline do Euru OS.
- Revisao da Regra 8 pode ser proposta separadamente se o operador 
  considerar que o criterio "HIGH global" e demasiado restritivo - 
  mas atraves de governanca formal, nao por interpretacao ad-hoc.

Operador: Andre Marcal
Status: CLOSED - Incident resolved, follow-up pending

## 2026-04-20 - PROPOSTA FORMAL: External AI Governance Protocol

Tipo de mudanca: Type 2 (Moderada - Protocolo de governanca de IAs auxiliares)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-20
Periodo de espera: 24 horas
Activacao prevista: 2026-04-21 (nao antes das 10:00)

CONTEXTO:
Dois incidentes recentes motivam esta proposta:

1. 2026-04-18 - PT004 XRPUSDT: IA auxiliar externa abriu paper trade 
   violando Regra 8 (news HIGH). Fechado imediatamente. Incident 
   report registado.

2. 2026-04-19 - GitHub commits: ChatGPT via web criou 8 commits no 
   repositorio Euru_TOS (docs/ files) durante uma sessao de ajuste 
   de perfil GitHub, sem conhecimento explicito do operador sobre o 
   impacto no Euru.

Ambos os incidentes partilham o mesmo padrao: IAs auxiliares actuam 
em recursos do Euru fora do pipeline validado.

OBJECTIVO:
Estabelecer protocolo formal que delimite o que IAs auxiliares 
externas podem e nao podem fazer no ecossistema Euru OS.

REGRAS PROPOSTAS:

1. TRADES (lesson from PT004):
   - Nenhuma IA auxiliar pode abrir paper trades directamente
   - Trades vem apenas do pipeline validado: morning scan -> agents 
     -> trade creation with full checklist 12/12
   - Sugestoes de trade por IAs externas sao tratadas como input, 
     nao decisao. Requerem validacao manual contra as 10 regras 
     inviolaveis antes de qualquer accao.

2. REPOSITORIO GIT (lesson from ChatGPT commits):
   - Apenas o utilizador local (andregottardimarcal@gmail.com) faz 
     commits ao Euru_TOS
   - IAs externas via web (ChatGPT, Gemini, Copilot, etc.) nao devem 
     ter acesso de escrita ao repositorio
   - Conteudo sugerido por IAs externas passa por revisao humana 
     antes de ser integrado via commit local

3. FICHEIROS DO SISTEMA:
   - Edicoes a ficheiros criticos (agentes em 04_AGENTES/, governanca 
     em 01_GOVERNANCA/, schemas em 00_GOVERNANCA/SCHEMAS/) apenas via 
     pipeline validado
   - Documentos complementares (docs/, README.md) - decisao do 
     operador caso a caso

APLICACAO PRATICA:
- Quando operador quiser ajuda de IA externa, usar em modo somente 
  leitura: copy-paste manual do input/output, sem integracao directa 
  com Git, trades, ou sistema de ficheiros do Euru
- Cada incidente futuro deve ser registado neste documento com o 
  mesmo formato usado para PT004 e para esta proposta
- O protocolo aplica-se a TODAS as IAs auxiliares externas, incluindo 
  sessoes futuras de Claude fora do Claude Code oficial

STATUS ACTUAL:
- ChatGPT nao tem token de acesso ao GitHub do operador (confirmado 
  em 2026-04-20)
- Nenhuma outra IA externa tem credenciais activas ao Euru_TOS

CRITERIOS DE APROVACAO (apos 24h cooling-off):
- Protocolo claro e aplicavel
- Nao cria friccao desnecessaria com uso legitimo de IAs para 
  pesquisa e aprendizagem
- Compatível com as 10 regras inviolaveis existentes

Operador: Andre (Risk/Product Owner)
Status: PENDING (24h wait ate 2026-04-21 10:00)

## 2026-04-20 - PROPOSTA FORMAL: Daily Audit + Weekly Audit (euru_daily_audit.py)

Tipo de mudanca: Type 2 (Moderada - Automacao de auditoria com notificacao por email)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-20
Periodo de espera: 24 horas
Activacao prevista: 2026-04-21 (nao antes das 09:00)

CONTEXTO:
O operador reconheceu que mesmo com o sistema a correr automaticamente,
nao ha visao consolidada sobre se tudo funcionou como deveria em cada
dia. Incidentes recentes (PT004 rule 8 violation, commits ChatGPT em
repositorio) mostram que falhas podem ocorrer sem deteccao imediata.

Nao se trata de automatizar resolucao de problemas - trata-se de
garantir visibilidade consistente sobre o estado do sistema, com
minimo esforco humano em dias normais.

OBJECTIVO:
Criar euru_daily_audit.py com dois modos operacionais:

MODO A - DAILY AUDIT (todos os dias as 08:30):
8 verificacoes objectivas com PASS/WARN/FAIL:
1. Morning scan de hoje - SCOUT_REPORT_YYYY-MM-DD.md existe
2. Asian scan de hoje - ASIAN_REPORT_YYYY-MM-DD.md existe
3. Trade monitor de hoje - TRADE_MONITOR_REPORT_YYYY-MM-DD.md existe
4. Git sincronizado - sem commits locais por enviar ou remoto a frente
5. Schema integrity - PAPER_TRADE_*.md e JOURNAL_*.md validos
6. Trades abertos saudaveis - sem trade aberto > 7 dias (time_stop)
7. Encoding check - ficheiros criticos sem BOM nem encoding non-UTF8
8. News Sentinel streak - alerta se HIGH >= 5 dias consecutivos (info)

Regra de email:
- >= 1 FAIL -> email critico
- >= 3 WARN -> email informativo
- 0 FAIL e < 3 WARN -> silencioso (sem email)

Output: AUDIT_REPORTS/DAILY_AUDIT_REPORT_YYYY-MM-DD.md

MODO B - WEEKLY AUDIT (sabados as 09:00):
- Consolida os 7 ultimos daily audits
- Lista todas as anomalias da semana (detalhe + resolucao)
- Estatisticas: trades abertos/fechados, P&L semanal, FAILs/WARNs
- Campo "Aprendizado" em formato [PREENCHER MANUALMENTE] para
  reflexao humana do operador
- Email SEMPRE enviado (com ou sem anomalias)

Output: AUDIT_REPORTS/WEEKLY_AUDIT_REPORT_YYYY-W##.md

ARQUITECTURA:
- Script Python unico com --mode daily (default) e --mode weekly
- Le credenciais de C:\Users\andre\.euru_secrets\euru.env
- Envio SMTP via Gmail (infraestrutura ja configurada em 2026-04-20)
- Commit + push via euru_git_sync apos gerar report

SCHEDULED TASKS:
- Euru_Daily_Audit: diaria 08:30, LogonType S4U, RunLevel Highest
- Euru_Weekly_Audit: sabados 09:00, LogonType S4U, RunLevel Highest

SAFETY:
- Script e SOMENTE LEITURA em relacao a dados criticos (trades,
  governanca, schemas). Nao altera nada.
- Credenciais SMTP fora do repositorio Git (C:\Users\andre\.euru_secrets\)
- App Password rotacionavel se comprometida
- Aprendizado semanal depende de input humano (campo manual),
  evitando pretensao de IA gerar insights automaticos

CRITERIOS DE APROVACAO (apos 24h cooling-off):
- Script implementado, testado em modo dry-run
- Daily e Weekly reports geram ficheiros validos
- Email de teste chega em ambos os modos
- Integracao com scheduled tasks funcional

LIMITACOES RECONHECIDAS:
- O script nao resolve problemas, apenas reporta
- "Effortless experience" e parcial: esforco zero em dias bons,
  2-5 minutos em dias com anomalias
- Nao substitui supervisao humana em decisoes criticas

Operador: Andre (Risk/Product Owner)
Status: PENDING (24h wait ate 2026-04-21 09:00)

## 2026-04-21 - PROPOSTA FORMAL: Nova North Star Metric do Euru OS

Tipo de mudanca: Type 3 (Critica - Redefinicao estrategica da meta do sistema)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-21 08:48 (hora local Espanha)
Periodo de espera: 48 horas
Activacao prevista: 2026-04-23 (nao antes das 08:48)

CONTEXTO:
Ao longo de varias conversas, o operador manifestou como objetivo
alcancar 1,000,000 EUR ate final de 2029, partindo de capital inicial
de 100-200 EUR. Apos analise matematica honesta e discussao sobre
realismo versus aspiracao, ficou claro que:

1. A matematica nao fecha com esse capital inicial em 3.5 anos usando
   metodologias disciplinadas
2. Uma North Star impossivel gera pressao sistemica que leva a
   violacoes de regras (vide incidente PT004)
3. Uma North Star realista permite otimizar para consistencia, nao
   para velocidade

Apos dialogo com o operador, foi acordado redefinir a North Star para
algo matematicamente alcancavel e psicologicamente saudavel.

NOVA NORTH STAR METRIC:

"Provar que o Euru gera 5-8% mensal medio sustentado em SIMULATE.
Em EXECUTE com 100 EUR inicial, atingir 1000 EUR em 12 meses."

JUSTIFICACAO:

Meta de 5-8% mensal em SIMULATE:
- Consistente com top 20% dos traders sistematicos de altcoins
- Alcancavel com metodologia Aguiar + MAC + disciplina Euru
- Permite validacao estatistica antes de escalar
- Compativel com regras existentes (1% risco/trade, RR minimo 1:2)

Meta de 100 EUR -> 1000 EUR em 12 meses em EXECUTE:
- Requer aproximadamente 21% mensal composto (agressivo mas possivel)
- 10x em 12 meses como prova de conceito antes de escalar capital
- Se atingida, justifica adicionar capital de outros negocios
  (pAIq, Tokengeist, consultoria) para compounding em escala maior
- Se nao atingida, diagnostico e ajuste antes de escalar capital

RELACAO COM OBJETIVO PESSOAL DE 1,000,000 EUR:

A meta de 1,000,000 EUR ate 2029 permanece como ASPIRACAO PESSOAL do
operador, nao como metrica operacional do Euru. O caminho para
essa aspiracao combina:

1. Euru OS prova conceito em SIMULATE (fase atual)
2. Euru OS em EXECUTE atinge 10x em 12 meses com 100 EUR (nova meta)
3. Capital adicional de outros negocios do operador e injetado
   no sistema validado
4. Compounding sobre capital maior caminha para aspiracao de longo
   prazo

Separar meta operacional do Euru da aspiracao pessoal do operador:
- Protege o sistema de pressao irrealista
- Permite avaliar Euru pelos seus proprios meritos
- Mantem objetivo de vida sem comprometer disciplina tecnica

CRITERIOS PARA TRANSITAR SIMULATE -> EXECUTE (actualizados):
- 20+ trades fechados
- Expectancy positiva em 3 meses consecutivos
- Zero violacoes de regras inviolaveis no ultimo trimestre
- Win rate >= 50% e RR medio >= 2.0

IMPACTO EM DOCUMENTACAO EXISTENTE:
- Learning Engine passa a medir contra esta nova meta
- Scorecards mensais podem incluir distancia a meta
- Se existir meta de 1M EUR em outros documentos (ex:
  EURU_NEW_CHAT_PROMPT_MASTER.md), actualizar para clarificar
  separacao entre aspiracao pessoal e meta operacional

CRITERIOS DE APROVACAO (apos 48h cooling-off):
- Operador confirma alinhamento apos 48h de reflexao
- Nenhuma objecao tecnica ou psicologica identificada
- Meta mantida ou ajustada conforme reflexao do operador

Operador: Andre (Risk/Product Owner)
Status: PENDING (48h wait ate 2026-04-23 08:48)

## 2026-04-21 09:02 - APROVACAO: Daily + Weekly Audit (Type 2)

Tipo: Aprovacao de Type 2 apos cooling-off
Referencia: Proposta 2026-04-20 (entrada anterior)
Data de aprovacao: 2026-04-21 09:02 (hora local Espanha)
Cooling-off: cumprido (24h, expirou 2026-04-21 09:00)

STATUS: APPROVED

NOTA OPERACIONAL IMPORTANTE:
Durante o periodo de cooling-off, o script euru_daily_audit.py foi
colocado na pasta EURO MAIN (apos instrucao do Claude para download
e deploy local). Uma scheduled task existente (Euru_Journal_Auditor)
executou o script automaticamente as 07:30 de 2026-04-21, antes do
fim do cooling-off as 09:00.

Esta execucao nao foi acao intencional do operador nem do Claude,
mas uma race condition causada por integracao com agente automatico
existente. A licao tecnica e: durante cooling-off, nao colocar novos
ficheiros no sistema - apenas preparar em ambiente externo.

O resultado foi: script funcionou correctamente, email foi enviado,
report foi gerado. Os findings foram validos (1 FAIL + 1 WARN
legitimos). Nao houve dano ao sistema.

A aprovacao actual ratifica o funcionamento verificado.

PROXIMOS PASSOS OPERACIONAIS:
1. Criar scheduled tasks dedicadas:
   - Euru_Daily_Audit: diaria 08:30
   - Euru_Weekly_Audit: sabados 09:00
2. Validar primeira execucao agendada natural
3. Corrigir BOM em ficheiros futuros via encoding-safe defaults

Operador: Andre (Risk/Product Owner)

## 2026-04-21 10:00 - APROVACAO: External AI Governance Protocol (Type 2)

Tipo: Aprovacao de Type 2 apos cooling-off
Referencia: Proposta 2026-04-20 (External AI Governance Protocol)
Data de aprovacao: 2026-04-21 10:00 (hora local Espanha)
Cooling-off: cumprido (24h, expirou 2026-04-21 10:00)

STATUS: APPROVED

PROTOCOLO EM VIGOR A PARTIR DESTE MOMENTO:

1. TRADES:
   - Nenhuma IA auxiliar pode abrir paper trades directamente
   - Trades vem apenas do pipeline validado: morning scan -> agents
     -> trade creation with full checklist 12/12
   - Sugestoes de trade por IAs externas sao input, nao decisao

2. REPOSITORIO GIT:
   - Apenas o utilizador local (andregottardimarcal@gmail.com) faz
     commits ao Euru_TOS
   - IAs externas via web (ChatGPT, Gemini, Copilot, etc.) nao
     devem ter acesso de escrita ao repositorio
   - Conteudo sugerido por IAs externas passa por revisao humana
     antes de ser integrado via commit local

3. FICHEIROS DO SISTEMA:
   - Edicoes a ficheiros criticos (agentes em 04_AGENTES/, governanca
     em 01_GOVERNANCA/, schemas em 00_GOVERNANCA/SCHEMAS/) apenas via
     pipeline validado
   - Documentos complementares (docs/, README.md) - decisao do
     operador caso a caso

4. APLICACAO:
   - IAs externas em modo somente leitura: copy-paste manual
   - Cada incidente futuro registado neste documento
   - Protocolo aplica-se a TODAS as IAs auxiliares externas

Este protocolo e parte das regras de governanca do Euru OS e sera
referenciado em incidentes futuros para determinar severidade.

Operador: Andre (Risk/Product Owner)

## 2026-04-23 09:06 - APROVACAO: Nova North Star Metric (Type 3)

Tipo: Aprovacao de Type 3 apos cooling-off
Referencia: Proposta 2026-04-21 08:48 (New North Star Metric)
Data de aprovacao: 2026-04-23 09:06 (hora local Espanha)
Cooling-off: cumprido (48h, expirou 2026-04-23 08:48)

STATUS: APPROVED

REFLEXAO APOS 48H:
Durante o periodo de cooling-off, operador teve tempo para considerar
a mudanca com clareza. Discussao subsequente confirmou alinhamento:

1. A meta de 1,000,000 EUR ate 2029 permanece como aspiracao pessoal
   mas nao como metrica operacional do Euru
2. Meta realista de 5-8% mensal em SIMULATE aceita como alcancavel
3. Meta de 100 EUR -> 1000 EUR em EXECUTE aceita como prova de
   conceito antes de escalar capital
4. Separacao entre aspiracao pessoal e metrica operacional protege
   sistema de pressao irrealista (licao PT004)

NORTH STAR METRIC OFICIAL DO EURU OS:

"Provar que o Euru gera 5-8% mensal medio sustentado em SIMULATE.
 Em EXECUTE com 100 EUR inicial, atingir 1000 EUR em 12 meses."

CRITERIOS ACTUALIZADOS PARA TRANSITAR SIMULATE -> EXECUTE:
- 20+ trades fechados
- Expectancy positiva em 3 meses consecutivos
- Zero violacoes de regras inviolaveis no ultimo trimestre
- Win rate >= 50% e RR medio >= 2.0

Estes criterios substituem quaisquer criterios anteriores baseados
em prazos calendario ou em valores monetarios absolutos.

ACCOES IMEDIATAS:
- Nenhuma. A meta passa a ser referencia para Learning Reports,
  Friday Cycles, e Weekly Audits a partir deste momento.
- Learning Engine (AGT-04) passa a medir expectancy mensal contra
  range 5-8% como benchmark primario.
- Documentacao existente que mencione meta de 1M EUR sera
  actualizada gradualmente quando identificada.

Operador: Andre (Risk/Product Owner)

## 2026-04-25 13:30 - PROPOSTA FORMAL: Migracao Operacional para EURU TOS MAIN (Type 3)

Tipo de mudanca: Type 3 (Critica - Mudanca de repositorio operacional canonico)
Proposto por: Risk/Product Owner (Andre)
Data da proposta: 2026-04-25 13:30 (hora local Espanha)
Periodo de espera: 48 horas
Activacao prevista: 2026-04-27 (nao antes das 13:30)

CONTEXTO:
A partir de 2026-04-25 existem dois repositorios paralelos com codigo
e documentacao do Euru:

1. C:\Users\andre\Desktop\EURO MAIN
   - Repositorio operacional historico (Euru_TOS no GitHub)
   - Scheduled tasks activas escrevem aqui
   - Documentacao acumulada com algumas duplicacoes e legacy
   - Foi onde o sistema operou de forma autonoma desde Marco 2026

2. C:\Users\andre\Desktop\EURU TOS MAIN
   - Novo repositorio (EURU_TOS_MAIN no GitHub)
   - Documentacao consolidada e organizada por Codex (2026-04-25)
   - Source of Truth e Operational State formalmente declarados
   - Estrutura limpa, ADRs, hierarquia clara
   - Inclui scripts ja revistos pela Codex

Este estado de paralelismo cria divergencia operacional crescente:
- Sistema escreve em EURO MAIN
- Codex actualiza scripts em EURU TOS MAIN
- Diferentes versoes podem coexistir sem reconciliacao

Esta proposta resolve o paralelismo definitivamente.

DECISAO PROPOSTA:

A partir de 2026-04-27 (apos cooling-off):

1. EURU TOS MAIN passa a ser o REPOSITORIO OPERACIONAL OFICIAL
2. EURO MAIN passa a estado ARQUIVADO READ-ONLY
3. Repositorio GitHub Euru_TOS passa a estado legacy (read-only, mantido para historico)
4. Repositorio GitHub EURU_TOS_MAIN torna-se o novo origem oficial

JUSTIFICACAO:

A migracao realiza a intencao do operador de ter "estrutura limpa,
transparente, sem duplicacao, com IAs auxiliares trabalhando em
sincronia sobre uma fonte unica". Nao realiza essa intencao manter
o status quo (dois repositorios em paralelo).

Optar por substituir documentacao dentro de EURO MAIN (variante 2B)
mantém o repositorio antigo com nome desactualizado e nao aproveita
o trabalho de consolidacao formal feito por Codex.

PLANO DE EXECUCAO (apos aprovacao em 2026-04-27):

Fase A - Preparacao (sem disruption):
- Backup completo de EURO MAIN como ZIP em local seguro fora do repo
- Backup completo de EURU TOS MAIN equivalente
- Verificar integridade de ambos antes de qualquer accao

Fase B - Migracao de dados operacionais:
- Migrar PAPER_TRADE_001.md a 004.md de EURO MAIN para EURU TOS MAIN
  (verificar que sao os mesmos ou identificar diferencas primeiro)
- Migrar JOURNAL_DAILY entries unicos de EURO MAIN
- Migrar AUDIT_REPORTS unicos de EURO MAIN
- Migrar SCOUT_REPORT, ASIAN_REPORT, TRADE_MONITOR_REPORT historicos
- Verificar que nao ha duplicados ou versoes conflitantes

Fase C - Migracao de scheduled tasks:
- Listar todas as scheduled tasks Euru_* activas
- Para cada uma:
  * Modificar Action path para apontar EURU TOS MAIN
  * Modificar WorkingDirectory para EURU TOS MAIN
  * Validar manualmente que executa correctamente
- Tasks afectadas (9 total):
  * Euru_Morning_Scan
  * Euru_Asian_Scan
  * Euru_Journal_Auditor
  * Euru_Smoke_Test_Night
  * Euru_GitHub_Sync
  * Euru_Friday_Cycle
  * EuruLearningEngine
  * Euru_Daily_Audit
  * Euru_Weekly_Audit

Fase D - Arquivamento:
- Renomear C:\Users\andre\Desktop\EURO MAIN para
  C:\Users\andre\Desktop\EURO MAIN_ARCHIVED_2026-04-27
- Atributo somente leitura na pasta inteira
- README claro a apontar EURU TOS MAIN como sucessor
- No GitHub, repositorio Euru_TOS recebe README a apontar EURU_TOS_MAIN

Fase E - Validacao pos-migracao:
- Executar manualmente euru_morning_scan.py em EURU TOS MAIN
- Executar manualmente euru_daily_audit.py
- Esperar primeira execucao agendada natural (proximo dia)
- Confirmar commits chegam ao novo repositorio remoto
- Confirmar emails de notificacao continuam a funcionar

CRITERIOS DE SUCESSO:

A migracao e considerada bem-sucedida se ao fim de 7 dias (2026-05-04):
- Sistema operacional escreve apenas em EURU TOS MAIN
- Scheduled tasks executam sem erros
- Audit reports diarios sao gerados normalmente
- Weekly Audit do proximo sabado (2026-05-02) executa sem incidente
- Friday Cycle do proximo sexta (2026-05-01) tenta executar
- Nenhum commit autonomo aparece em Euru_TOS legacy

CRITERIOS DE ROLLBACK:

Se durante Fase B, C ou D ocorrer erro grave (perda de dados, sistema
inoperacional, scheduled tasks quebradas e sem recuperacao em 1 hora):

- Pasta EURO MAIN_ARCHIVED_2026-04-27 e renomeada de volta para EURO MAIN
- Scheduled tasks revertidas para paths originais
- EURU TOS MAIN e mantido como existe mas desconectado da operacao
- Incidente formal registado neste documento
- Nova proposta de migracao com correcao do problema identificado

RISCOS RECONHECIDOS:

1. Scripts em EURU TOS MAIN podem ter sido modificados por Codex e
   nao terem sido testados em producao
   Mitigacao: validacao manual antes de activar scheduled tasks

2. .euru_secrets/euru.env esta em C:\Users\andre\.euru_secrets - fora
   de ambos os repositorios. Migracao nao afecta credenciais.

3. Historico Git de EURO MAIN nao e migrado, fica em Euru_TOS legacy
   Mitigacao: aceitavel - novo historico comeca em EURU TOS MAIN com
   referencia ao repositorio legado

4. Race condition se houver scheduled task durante a migracao
   Mitigacao: executar Fase C com todas as tasks paradas temporariamente

CRITERIOS DE APROVACAO (apos 48h cooling-off):

- Operador confirma alinhamento apos 48h de reflexao
- Codex confirma alinhamento (atraves do operador como canal)
- Plano de execucao continua aplicavel sem alteracoes
- Nenhum incidente novo identificado que altere a analise

Operador: Andre (Risk/Product Owner)
Status: PENDING (48h wait ate 2026-04-27 13:30)

## 2026-04-27 13:37 - APROVACAO: Migracao Operacional para EURU TOS MAIN (Type 3)

Tipo: Aprovacao de Type 3 apos cooling-off
Referencia: Proposta 2026-04-25 13:30 (commit 10673d7)
Suplementos:
  - Migration Runbook v0.3 (produzido 2026-04-27 manha)
  - Migration Rollback v0.3 (produzido 2026-04-27 manha)
Data de aprovacao: 2026-04-27 13:37 (hora local Espanha)
Cooling-off: cumprido (48h, expirou 2026-04-27 13:30)

STATUS: APPROVED

REFLEXAO APOS 48H:
Durante o cooling-off, operador descansou domingo (sistema autonomo).
Manha de 27 Abr foi dedicada a preparacao colaborativa Claude+Codex:

- Codex executou validacao de backups (SHA256 GREEN), criou tags Git
  pre-migration-2026-04-27-* em ambos os repos, exportou XMLs das 9
  scheduled tasks, fez backup do PowerShell profile, produziu delta
  inventory e MIGRATION_PREFLIGHT_2026-04-27.md.

- Claude reformulou Fases A-E em formato de gates explicitos
  (objetivo, comandos, sucesso, abort, evidencia, rollback) e adicionou
  Fase B0a (non-destructive checkpoint) e Fase E2 (post-migration audit).

- Tres rondas de revisao tecnica entre Claude e Codex produziram
  Runbook v0.3 e Rollback v0.3 com 7 ajustes incorporados.

DESCOBERTA OPERACIONAL DURANTE B0a:
Cinco das nove scheduled tasks Euru_* estavam Disabled antes do B0a:
  - Euru_Morning_Scan (Disabled)
  - Euru_Asian_Scan (Disabled)
  - Euru_GitHub_Sync (Disabled)
  - Euru_Friday_Cycle (Disabled)
  - EuruLearningEngine (Disabled)

Operador confirmou nao ter desactivado. Codex confirmou apenas leitura
no B0a (sem Disable). Origem desta desactivacao e desconhecida e sera
investigada pos-migracao como possivel incidente de governanca.

Implicacao para Fase C1: redesenhada para preservar estados originais.
Migracao nao faz Enable/Disable. Tasks Disabled migram path mas continuam
Disabled. Reactivacao consciente sera trabalho separado pos-migracao.

ESTADO DE PRE-MIGRACAO CONFIRMADO:
- Backups validados GREEN com SHA256:
  * BACKUP_EURO_MAIN_2026-04-27_0934.zip (246 MB)
    SHA256: 1216223F5434ED19EDCA7A9FD1A953475A5FC8E36E138274BAE6C61A82D39A99
  * BACKUP_EURU_TOS_MAIN_2026-04-27_0936.zip (5 MB)
    SHA256: 115D749B6303661E5B859D89C377598A03EDA34C7364A65A4531D34EF2C09EBA
- B0a artifacts: C:\Users\andre\Desktop\EURU_MIGRATION_B0_2026-04-27\
- Preflight report: 00_MASTER\MIGRATION_PREFLIGHT_2026-04-27.md (untracked esperado)
- Git tags: pre-migration-2026-04-27-euro-main, pre-migration-2026-04-27-euru-tos-main
- Scheduled tasks XML export: 9 ficheiros em scheduled_tasks_before/
- PowerShell profile backup: WindowsPowerShell_profile.ps1 (PS7 nao existia)
- Nenhuma task Euru_* em estado Running

CRITERIOS DE APROVACAO CUMPRIDOS:
- Operador confirma alinhamento apos 48h de reflexao: SIM
- Codex confirmou alinhamento atraves do operador: SIM
- Plano de execucao com refinamentos do Runbook v0.3 e Rollback v0.3: SIM
- Warnings B0a aceites pelo operador: SIM (5 tasks Disabled identificadas)

EXECUCAO IMEDIATA:
A migracao inicia agora pela B0a verification. Cada fase passa pelos
seus 6 gates. Fase seguinte so e iniciada apos a anterior estar GREEN.

Sequencia: B0a verify -> B (manifest+migrate) -> C dry-run -> C apply
-> D -> E -> E2 (T+24h e T+7d).

Operador: Andre (Risk/Product Owner)

## 2026-04-27 14:35 - MIGRACAO TYPE 3 EXECUTADA: EURU TOS MAIN agora operacional

Tipo: Registo de execucao bem-sucedida
Referencia: Type 3 aprovado 2026-04-27 13:37 (commit 6fe5477)
Suplementos: Migration Runbook v0.3, Migration Rollback v0.3
Data de execucao: 2026-04-27 13:37 - 14:35 (1 hora)

STATUS: COMPLETED

FASES EXECUTADAS:

Fase B0a (Non-destructive checkpoint) - GREEN
  - Backups SHA256 validados
  - 9 XML exports das scheduled tasks
  - Backup PS profile
  - Tags Git em ambos repos
  - Delta inventory CSV gerado

Fase B-minimal (Operational delta) - GREEN
  - 6 ficheiros operacionais de 26-27 Abr migrados
  - + run_smoke_test.bat (suplemento descoberto durante validacao)
  - + MIGRATION_PREFLIGHT_2026-04-27.md
  - Commits: 3de0e28, ea506f7
  - Migration manifest registado em B0 artifacts
  - 1259 ficheiros legacy NAO migrados (deferred to post-migration triage)

Fase C (Scheduled tasks) - GREEN
  - 9 tasks migradas: paths EURO MAIN -> EURU TOS MAIN
  - States preservados: 5 Disabled (Morning_Scan, Asian_Scan, GitHub_Sync,
    Friday_Cycle, EuruLearningEngine), 4 Ready (Daily_Audit, Journal_Auditor,
    Smoke_Test_Night, Weekly_Audit)
  - Bug detectado no script: 'Applied' mascarando 'Acceso denegado' em
    sessao nao-elevada. Mitigacao: re-execucao em PS Run as Administrator
    real. Documentar como finding pos-migracao.

Fase D (Archive + PS profile) - GREEN
  - Pasta renomeada: EURO MAIN -> EURO MAIN_ARCHIVED_2026-04-27
  - IsReadOnly attribute applicado (marcador apenas, nao protecao real)
  - README_ARCHIVED.md criado dentro da pasta arquivada
  - WindowsPowerShell profile actualizado: EURO MAIN -> EURU TOS MAIN
  - PowerShell 7 profile nao existia (skip)
  - Verificacao: nova janela PS abre directamente em EURU TOS MAIN

Fase E (Validation manual) - GREEN
  - Morning scan executado em EURU TOS MAIN com sucesso
  - SCOUT_REPORT_2026-04-27.md e TRADE_MONITOR_REPORT_2026-04-27.md
    gerados em paths novos
  - Git sync automatico push commit 357e1fa para origin EURU_TOS_MAIN.git
  - News Sentinel: LOW
  - BTC Master Filter: SIDEWAYS
  - 0 trades abertos, 0 setups validos

Fase E2 (Post-migration audit) - PENDING
  - T+24h checkpoint: 2026-04-28 manha
  - T+7d checkpoint: 2026-05-04

DESCOBERTAS DURANTE MIGRACAO:

1. 5 das 9 tasks estavam Disabled antes do B0a (Morning_Scan, Asian_Scan,
   GitHub_Sync, Friday_Cycle, EuruLearningEngine). Operador nao recordou
   ter desactivado. Codex confirmou nao ter desactivado. Origem desconhecida.
   IMPLICACAO: Pode explicar bug recorrente de NextRunTime saltar dias.
   ACCAO: Reactivacao consciente como trabalho pos-migracao, decidindo
   task a task.

2. Task Euru_Smoke_Test_Night apontava para C:\Users\andre\Desktop\Euru_TOS\
   (path legacy que ja nao existia). Ficheiro run_smoke_test.bat foi
   localizado em EURO MAIN\Euru_TOS\scripts\ e migrado para EURU TOS MAIN\
   scripts\. Fase C apply usou path correcto.

3. Bug em phase_c_apply_paths.ps1: Set-ScheduledTask falhou com Acceso
   denegado em sessao com IsInRole=True mas sem elevacao real. Script
   continuou e imprimiu 'Applied' enganadoramente. Detectado por verificacao
   pos-execucao via Get-ScheduledTask. Corrigido com re-execucao em janela
   PS Run as Administrator.

4. EURO MAIN continha 2123 ficheiros SOURCE_ONLY no delta inventory.
   Apos filtrar __pycache__, _EURU_TOS_MAIN_BUILD, Euru_TOSOld, Euru_TOS_GITHUB,
   restavam 1259. Maioria sao multiplas pastas legacy (Euru_TOS_FINAL,
   Euru_TOS_MIGRATED, Euru_TOS_NEW, Euru_TOS, docxwork\node_modules,
   ZIPs antigos). Decisao do operador: Phase B-minimal (6 ficheiros
   operacionais), triagem detalhada deferred.

ARTIFACTS GERADOS:

- C:\Users\andre\Desktop\BACKUP_EURO_MAIN_2026-04-27_0934.zip (246 MB)
- C:\Users\andre\Desktop\BACKUP_EURU_TOS_MAIN_2026-04-27_0936.zip (5 MB)
- C:\Users\andre\Desktop\EURU_MIGRATION_B0_2026-04-27\ (B0a artifacts)
- C:\Users\andre\Desktop\EURO MAIN_ARCHIVED_2026-04-27\ (legacy folder)
- 4 commits em EURU_TOS_MAIN: 6fe5477, 3de0e28, ea506f7, 357e1fa

ESTADO FINAL:

- Repositorio operacional canonico: EURU TOS MAIN -> github.com/andre-marcal-blockchain/EURU_TOS_MAIN
- Repositorio legacy READ-ONLY: EURO MAIN_ARCHIVED_2026-04-27 (folder) e
  github.com/andre-marcal-blockchain/Euru_TOS (GitHub - sem novos commits)
- 9 scheduled tasks operam contra EURU TOS MAIN
- Sistema autonomo confirmado funcional (commit 357e1fa)

PROXIMOS PASSOS POS-MIGRACAO:

1. Submeter EURU AI Collaboration Policy v0.3 como Type 2 (24h cooling-off)
2. T+24h checkpoint da E2 (manha 28 Abr)
3. Decisao consciente sobre tasks Disabled (reactivar quais? quais ficam?)
4. Triagem dos 1259 ficheiros legacy (manter? arquivar? descartar?)
5. Investigar quem desactivou tasks pre-B0a (possivel incidente governanca)
6. Corrigir bug do phase_c_apply_paths.ps1 (Applied mascarando errors)
7. Adicionar __pycache__ ao .gitignore
8. Reconciliar CLAUDE.md (READ_ONLY -> SIMULATE)
9. Repair PT004 structure (heading missing)

Operador: Andre (Risk/Product Owner)

## 2026-04-29 09:29 - Type 2 - Plano Fase 1 Observacao - EM COOLING-OFF

Tipo: Proposta Type 2
Documento: 00_MASTER/EURU_PLANO_FASE1_OBSERVACAO_2026-04-29_v0.3.1.md
Commit do documento: 01d1a0e
Versao: v0.3.1 (apos 4 iteracoes: v0.1, v0.2, v0.3, v0.3.1)

STATUS: COOLING-OFF (24h)

ESCOPO DA PROPOSTA:

Reactivacao de scheduled tasks em modo READ_ONLY durante 14 dias para
observacao do mercado conforme metodologia Bruno Aguiar / MAC, antes
de qualquer enhancement tecnico ou paper trade.

Tasks a reactivar (existentes, Enable-ScheduledTask):
- Euru_Morning_Scan (daily 07:00 Europe/Madrid)
- Euru_Asian_Scan (daily 02:00 Europe/Madrid)

Task a criar (Register-ScheduledTask, Apendice A do plano):
- Euru_Trade_Monitor (daily 07:30 Europe/Madrid, --dry-run obrigatorio)

Tasks que permanecem Disabled (decisao consciente):
- Euru_GitHub_Sync, Euru_Friday_Cycle, EuruLearningEngine

CRITERIOS DE SUCESSO: 8 criterios (A-H)
GATILHOS DE ABORT: 4 gatilhos (A-D)
COMPROMISSO DO OPERADOR: revisao diaria antes 09:00 Europe/Madrid

REVISAO PRE-APROVACAO:
- Codex auditou v0.1, identificou 6 correcoes -> v0.2
- Codex revisou v0.2, sugeriu validacao manual + comando completo -> v0.3
- Codex apontou texto language-specific da janela PS -> v0.3.1
- Codex aprovou tecnicamente v0.3.1
- Operador revisou v0.3.1 e aprovou

COOLING-OFF:
- Inicio: 2026-04-29 09:29 Europe/Madrid
- Fim previsto: 2026-04-30 09:29 Europe/Madrid
- Acao na fase de cooling-off: aguardar, nao executar nenhum comando do
  Apendice A nem Enable-ScheduledTask, nao criar tabela CANDIDATES_REVIEW.md

PROXIMA ENTRADA: registar APROVACAO formal Type 2 apos cooling-off cumprido,
incluindo timestamp da aprovacao e plano de execucao operacional para o
mesmo dia.

Operador: Andre (Risk/Product Owner)

## 2026-04-30 14:00 - Type 2 - Plano Fase 1 Observacao - APROVADO

Tipo: Aprovacao formal Type 2
Documento: 00_MASTER/EURU_PLANO_FASE1_OBSERVACAO_2026-04-29_v0.3.1.md
Commit do documento: 01d1a0e
Registo COOLING-OFF: commit d4fad08 (2026-04-29 09:29 Madrid)

STATUS: APROVADO - autorizada execucao operacional

COOLING-OFF CUMPRIDO:
- Inicio: 2026-04-29 09:29 Europe/Madrid
- Fim cumprido: 2026-04-30 09:29 Europe/Madrid
- Duracao: 24h conforme governanca Type 2
- Sem alteracoes ao plano durante cooling-off
- Sem accoes operacionais durante cooling-off
- Aprovacao registada apos retorno do operador (~14:00 Madrid)

NOTA DE TRANSPARENCIA - VALIDACAO MANUAL ANTECIPADA:

Em 2026-04-30 (manha, antes da aprovacao formal), o Codex executou
validacao manual do Trade Monitor:

  python .\euru_trade_monitor.py --dry-run

Resultado: schema valid, mode DRY-RUN, 0 open trades, gerou
TRADE_MONITOR_REPORT_2026-04-30.md em SCORECARDS/.

Esta validacao corresponde ao Passo 1 do plano operacional (Seccao 5.2.1),
que tecnicamente devia preceder apenas o Passo 2 (Register-ScheduledTask),
nao a aprovacao Type 2 inteira.

Pragmatica: --dry-run e 100% READ-ONLY, sem efeito secundario, e o report
gerado e identico ao que o scheduler produziria. Operador aceita esta
validacao antecipada como pragmatica e zero-risco.

Para futuro: validacoes manuais devem seguir ordem do plano (apos aprovacao
Type 2). Codex registou recomendacao para si proprio.

PROXIMOS PASSOS OPERACIONAIS (5 passos com pausa entre cada):

Passo 1: Validacao manual python euru_trade_monitor.py --dry-run
  -> JA FEITO PELO CODEX em 2026-04-30 manha. Report disponivel.

Passo 2: Enable-ScheduledTask em PowerShell elevado real
  -> Euru_Morning_Scan
  -> Euru_Asian_Scan

Passo 3: Register-ScheduledTask Euru_Trade_Monitor
  -> Conforme Apendice A do plano (v0.3.1)
  -> --dry-run obrigatorio
  -> Daily 07:30 Europe/Madrid

Passo 4: Verificacao consolidada com Get-ScheduledTask
  -> Confirmar 3 tasks Ready, paths corretos

Passo 5: Criar tabela EURU_FASE1_CANDIDATES_REVIEW.md em 00_MASTER/
  -> Template da Seccao 11 do plano
  -> Marcar inicio oficial Fase 1

ESCOPO REAFIRMADO:
- 14 dias de observacao READ_ONLY
- 8 criterios de sucesso (A-H)
- 4 gatilhos de abort (A-D)
- Compromisso operador: revisao diaria antes 09:00 Europe/Madrid

Operador: Andre (Risk/Product Owner)

## 2026-04-30 14:17 - INICIO FORMAL FASE 1 OBSERVACAO

Tipo: Marco operacional (apos aprovacao Type 2)
Referencia: Plano Fase 1 v0.3.1 (commit 01d1a0e), Aprovacao Type 2 (commit ba557b0)
Tabela operacional: 00_MASTER/EURU_FASE1_CANDIDATES_REVIEW.md

STATUS: FASE 1 ACTIVE

PERIODO:
- Inicio: 2026-04-30 14:17 Europe/Madrid
- Checkpoint T+7d: 2026-05-07
- Fim previsto T+14d: 2026-05-14

5 PASSOS OPERACIONAIS EXECUTADOS:

Passo 1 - Validacao manual python euru_trade_monitor.py --dry-run
  -> Executado por Codex em 2026-04-30 manha (antes da aprovacao formal,
     registado como nota de transparencia em entrada anterior).
  -> Schema valid, mode DRY-RUN, 0 open trades.

Passo 2 - Enable das tasks existentes (PowerShell elevado real)
  -> Euru_Morning_Scan: Disabled -> Ready
  -> Euru_Asian_Scan: Disabled -> Ready
  -> Sem erros.

Passo 3 - Register Euru_Trade_Monitor (PowerShell elevado real)
  -> NOTA IMPORTANTE: comando do Apendice A original falhou com 
     "Acceso denegado" mesmo em PS elevado.
  -> Diagnostico: New-ScheduledTaskPrincipal com -RunLevel Highest 
     requer credenciais explicitas (password) que nao temos como 
     fornecer; UAC bloqueia criacao de task elevated sem password.
  -> Solucao aplicada: removido  customizado. Task usa 
     defaults (current interactive user, normal level).
  -> Justificacao tecnica: Trade Monitor com --dry-run e READ-ONLY,
     escreve apenas em pasta do user, nao requer privilegios elevados.
     Equivalente operacional ao Daily Audit (que tambem nao corre 
     elevated). Zero perda de capacidade.
  -> Resultado: task criada com sucesso. State: Ready.
  -> NextRun: 2026-05-01 07:30:00 Europe/Madrid.

Passo 4 - Verificacao consolidada
  -> 3 tasks da Fase 1 Ready, paths corretos para EURU TOS MAIN
  -> Outras tasks Euru no estado esperado:
     * Daily_Audit Ready, Journal_Auditor Ready, Smoke_Test Ready, 
       Weekly_Audit Ready
     * Friday_Cycle Disabled, GitHub_Sync Disabled, 
       EuruLearningEngine Disabled (decisao consciente)

Passo 5 - Tabela EURU_FASE1_CANDIDATES_REVIEW.md criada em 00_MASTER/
  -> Template conforme Seccao 11 do plano
  -> Status ACTIVE
  -> Pronta para preenchimento diario antes 09:00 Madrid

DESVIO DO PLANO REGISTADO:

Apendice A do plano (v0.3.1) especificava New-ScheduledTaskPrincipal 
com -RunLevel Highest. Esse parametro foi removido por incompatibilidade 
com criacao via PS elevado sem credenciais explicitas. Resultado 
operacional e tecnicamente equivalente para o objectivo (Trade Monitor 
em dry-run nao precisa elevation).

Acao corretiva futura: actualizar Apendice A do plano para v0.3.2 ou 
nota de erratum, removendo Principal customizado. NAO criar Type 2 
separado para isto - e desvio nao-substantive (mesmo comportamento 
operacional, syntax diferente).

Codex deve registar correccao para futura reutilizacao do template.

GATILHOS DE ABORT ACTIVOS (4):
- A: Falhas tecnicas criticas
- B: Sinais metodologicos errados
- C: Drift do operador (5+ dias sem leitura)
- D: Modificacao nao-autorizada de codigo

PROXIMA ACCAO:
- 2026-05-01 manha: Daily Audit corre 08:30 (autonomo)
- 2026-05-01 ~07:00-07:30: Asian Scan + Morning Scan + Trade Monitor 
  rodam autonomamente
- Operador le reports antes 09:00 e preenche tabela CANDIDATES_REVIEW
- Sistema gera trilha de auditoria para 14 dias

Operador: Andre (Risk/Product Owner)

## 2026-04-30 14:43 - NOTA TECNICA: Corrupcao de encoding em v0.3.1 e v0.3.2

Tipo: Nota tecnica nao-critica
Status: Reconhecido, regeneracao adiada

DESCOBERTA:

Apos execucao da Fase 1, ao revisar v0.3.1 commitada (commit 01d1a0e),
identificada corrupcao de encoding e markdown escapado:

- Caracteres especiais corrompidos: 'â€"' em vez de '-', 'â†'' em vez 
  de '->', 'Ã§' em vez de 'c-cedilha', etc.
- Markdown escaped: '\#' em vez de '#', '\*\*' em vez de '**'

CAUSA-RAIZ PROVAVEL:

Encoding mismatch no momento da gravacao via Notepad em 2026-04-29.
Conteudo colado do chat para Notepad gravou possivelmente em 
Windows-1252 lido como UTF-8 ou similar. Markdown escaping pode 
ter ocorrido em algum passo intermedio (chat -> clipboard -> Notepad).

IMPACTO OPERACIONAL:

Zero. Conteudo e legivel para auditor humano. Plano foi compreendido,
discutido, revisado em multiplas iteracoes (v0.1, v0.2, v0.3, v0.3.1).
Aprovacao Type 2 foi sobre conteudo substantivo, nao representacao
visual.

IMPACTO DE GOVERNANCA:

Documento canonico fica feio quando renderizado em GitHub. Auditor 
futuro consegue ler mas requer esforco visual extra.

DECISAO PRAGMATICA:

Direccao C (operador, 2026-04-30 ~14:45 Madrid):
- Nao regenerar v0.3.1 (mantem-se como prova historica do que foi 
  aprovado)
- Nao criar v0.3.2 limpa hoje
- v0.3.2 que Codex tinha criado (com mesma corrupcao herdada) 
  apagada do filesystem (nao tinha sido commitada)
- Regeneracao de v0.3.2 limpa adiada para data futura quando operador 
  tiver bandwidth e metodo robusto (nao Notepad)

ACCAO PENDENTE FUTURA:

- Regenerar v0.3.2 limpa com metodo que preserve UTF-8 (Set-Content 
  via PowerShell directo, ou VS Code com encoding explicito, etc.)
- Manter v0.3.1 corrupta como historica
- Cross-reference em ambos os documentos

NOTA OPERACIONAL:

Fase 1 esta ACTIVE e nao depende destes documentos serem cosmeticamente
perfeitos. Sistema corre autonomamente amanha 1 Maio (Asian 02:00, 
Morning 07:00, Trade Monitor 07:30, Journal 07:30, Daily Audit 08:30).

Codex registou-se a si proprio para revisar metodo de criacao de 
documentos no futuro (evitar Notepad sem encoding controlado).

Operador: Andre (Risk/Product Owner)

## 2026-05-01 10:02 - DIA 1 FASE 1: timing imperfeito + decisao PC 24/7

Tipo: Marco operacional + decisao de governanca
Status: Fase 1 ACTIVE, dia 1/14

OBSERVACAO TECNICA:

Computador estava DESLIGADO durante a noite de 30 Abr para 1 Maio.
Tasks scheduled (Asian 02:00, Morning 07:00, Trade Monitor 07:30, 
Journal 07:30, Daily Audit 08:30) nao correram nas horas previstas.

Quando operador ligou o PC em 2026-05-01 ~09:26 Madrid, todas as 
5 tasks correram em batch devido a flag StartWhenAvailable.

Resultados:
- Todas com Result=0 (sucesso tecnico)
- Reports gerados correctamente em paths esperados
- Daily Audit detectou que Morning Scan e Asian Scan correram hoje
  (mesmo que tarde) e nao reportou FAIL para 2026-05-01
- Commits autonomos: bafca0f (audit), 22adf44 (asian), cba673c (morning)

IMPACTO METODOLOGICO:

Asian Scan e Morning Scan correm idealmente em horas fixas para 
capturar momentos especificos do mercado:
- Asian (02:00 Madrid = 00:00 UTC): captura sessao asiatica real
- Morning (07:00 Madrid): captura overnight + pre-abertura europeia

Correndo as 09:26, dados podem estar a analisar candles diferentes.
BTC Master Filter funcionou correctamente (downgrade a WATCHLIST 
em SIDEWAYS), mas valor analitico das sessoes especificas e reduzido.

DECISAO: PC 24/7 durante Fase 1

Para garantir que tasks correm nas horas previstas durante o resto
da Fase 1 (2 Maio - 14 Maio):

- Computador permanecera ligado 24/7
- Custo eletrico estimado: 2-5 EUR para 14 dias
- Zero configuracao adicional necessaria (vs Wake-on-Schedule)
- Decisao temporaria, reavaliar pos-Fase 1

ALTERNATIVAS REJEITADAS:

- Wake-on-Schedule: exigiria configuracao BIOS + flag tasks, risco
  de edge cases durante Fase 1, melhor explorar pos-Fase 1
- Cloud/VPS: trabalho fora de escopo Fase 1, considerar Fase 2

IMPACTO NOS CRITERIOS DE SUCESSO:

- Criterio A (sem falhas criticas): PASS - tasks correram, Result=0
- Criterio B (Daily Audit sem incidentes graves): PASS para 1 Maio
- Criterio C (reports consistentes): PASS - reports gerados
- Criterio D (git sync): PASS - commits autonomos pushed
- Criterio E (avaliacao qualitativa): PENDING - operador vai 
  preencher CANDIDATES_REVIEW
- Criterio F (BTC Master Filter): PASS - filtro funcionou (BTC 
  SIDEWAYS, todos sinais downgraded WATCHLIST)
- Criterio G (CANDIDATES_REVIEW preenchido): PENDING - operador 
  vai preencher hoje
- Criterio H (zero modificacoes codigo): PASS

Dia 1 conta como dia operacional valido apesar do timing imperfeito.
A partir de 2 Maio, com PC 24/7, tasks deverao correr nas horas
exactas previstas.

Operador: Andre (Risk/Product Owner)
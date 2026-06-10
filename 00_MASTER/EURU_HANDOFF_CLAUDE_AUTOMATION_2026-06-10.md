# EURU Handoff — Ativação da Camada de Revisão Headless (Claude)

DATE: 2026-06-10
AI: Claude (chat review session)
OBJECTIVE: Entregar pacote 09_AI_AUTOMATION (revisões diária e semanal headless,
Type 1, advisory) e integrar Codex ao novo loop.

EVIDENCE READ:
- AGUIA_EURU_CODEX_CLAUDE_MASTER.md (upload do operador)
- EURU_CLAUDE_PAIRING_MASTER_BRIEF.md (upload do operador)
- Clone público de EURU_TOS_MAIN @ HEAD 3240ca0
- 00_MASTER/EURU_OPERATIONAL_STATE.md, CLAUDE.md,
  00_MASTER/EURU_CONSOLIDATION_ROADMAP.md, SCORECARDS recentes

FILES CHANGED (a serem adicionados pelo operador):
- 09_AI_AUTOMATION/EURU_DAILY_REVIEW_PROMPT.md
- 09_AI_AUTOMATION/EURU_WEEKLY_LEARNING_PROMPT.md
- 09_AI_AUTOMATION/euru_claude_daily_review.ps1
- 09_AI_AUTOMATION/euru_claude_weekly_review.ps1
- 09_AI_AUTOMATION/euru_claude_tasks_setup.ps1
- 09_AI_AUTOMATION/README.md
- Nova pasta de saída: 08_DADOS_E_JOURNAL/AI_REVIEWS/

TESTS: Nenhum executado ainda no ambiente local. Smoke test obrigatório:
Start-ScheduledTask "EURU Claude Daily Review" e verificação do arquivo
DAILY_REVIEW_<data>.md + log em 09_AI_AUTOMATION/LOGS/.

RESULT: Pacote pronto. Classificação de mudança: Type 1 (relatório/documentação;
nenhuma lógica de decisão tocada). Registro recomendado em
01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md.

RISKS:
1. Uptime da máquina às 21:35 e domingo 10:45 — mesmo gargalo dos scans
   perdidos (jun 2, 6, 8). A automação vai MEDIR esse gap, não escondê-lo.
2. Modo -p desabilita trust verification; o guardrail é o allowlist de
   ferramentas (Read/Glob/Grep/Write, Bash git/python apenas). Ampliar
   allowlist = decisão Type 2 com cooling-off.
3. Conflito documental aberto: AGUIA master declara "Operational mode:
   READ_ONLY" enquanto o canônico EURU_OPERATIONAL_STATE.md define SIMULATE.
   Correção Type 1 pendente (renomear campo para "Scanner data mode").

GIT STATUS: Limpo no clone remoto verificado (HEAD == origin/main @ 3240ca0).
COMMIT: Pendente — operador fará o commit de 09_AI_AUTOMATION.
REVIEW REQUIRED: SIM — Codex deve revisar os dois .ps1 e os dois prompts
antes do primeiro run agendado (rotação de papéis: Claude implementou,
Codex revisa). Resposta esperada: APPROVE / APPROVE_WITH_CONDITIONS /
REJECT / NEEDS_MORE_EVIDENCE, com achados concretos.

NEXT ACTION (ordem):
1. Operador: unzip do pacote, criar AI_REVIEWS/, autenticar claude no repo.
2. Codex: revisar pacote (foco: paths, allowlist, exit codes, não-interferência
   com crons existentes 21:05 e domingo 10:00).
3. Operador: registrar ativação em DECISOES_ESTRATEGICAS_REVISADO.md e
   rodar setup + smoke test.
4. Codex: corrigir o conflito READ_ONLY/SIMULATE no AGUIA master (Type 1).
5. Ambos: a partir do primeiro DAILY_REVIEW, Codex lê os arquivos de
   AI_REVIEWS/ no início de cada sessão e trata GOVERNANCE_FLAG ou
   OPERATIONAL_FAILURE como item de abertura obrigatório.

## Modelo operacional conjunto (resumo para o Codex)

- Codex = agente de execução local: implementa, roda testes, mantém crons,
  reporta estado exato de arquivos e git.
- Claude headless = verificador agendado: escreve DAILY_REVIEW_* e
  WEEKLY_REVIEW_* em AI_REVIEWS/ e faz commit apenas desses arquivos.
- Claude chat = revisor profundo sob demanda (lê o repo público no GitHub).
- Operador = autoridade final. Nada vira canônico sem aprovação dele.
- Canal de comunicação entre as IAs = o próprio repositório: arquivos em
  AI_REVIEWS/, este handoff, e commits com mensagens padronizadas.
- Rotação: quem implementa não aprova o próprio trabalho.

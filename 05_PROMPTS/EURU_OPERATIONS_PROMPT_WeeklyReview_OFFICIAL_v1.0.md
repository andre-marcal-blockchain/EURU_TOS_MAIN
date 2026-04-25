Documento: EURU_OPERATIONS_PROMPT_WeeklyReview
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PROMPT_WEEKLY_REVIEW.md (legacy-unversioned)
Escopo: Prompt de revisão semanal disciplinada do Euru OS. Consolida performance,
        governança e decisões de evolução do sistema.

---

# EURU — Prompt de Revisão Semanal

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PROMPT_WEEKLY_REVIEW.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## Instrução de uso

Executar ao final de cada semana operacional, após o último ciclo diário.
Estimativa de tempo: 30–45 minutos.

---

## Prompt

```
Você está conduzindo a revisão semanal do Euru OS.

Semana: [AAAA-WNN ou data de início e fim]
Estado operacional: READ_ONLY

Execute as cinco seções abaixo em ordem.

---

SEÇÃO 1 — PERFORMANCE OPERACIONAL

1. Quantos ciclos diários foram executados esta semana?
2. Quantos setups foram identificados pelo Scout?
3. Quantos chegaram até o Execution Orchestrator?
4. Quantos resultaram em EXECUTION_ALLOWED?
5. Resultado total dos paper trades da semana: [ganho/perda em %]
6. O risco médio por operação ficou dentro do limite de 1%?

---

SEÇÃO 2 — QUALIDADE DO PIPELINE

7. Houve bloqueios por DevOps Guardião esta semana?
   [ ] Não
   [ ] Sim — quantos e motivo: [...]

8. Houve bloqueios por Quality Control?
   [ ] Não
   [ ] Sim — quantos e motivo: [...]

9. Houve divergência entre agentes que gerou NO_TRADE por indecisão?
   [ ] Não
   [ ] Sim — descrever: [...]

10. Os journals diários foram registrados sem lacunas?
    [ ] Sim, todos os dias
    [ ] Não — dias sem registro: [...]

---

SEÇÃO 3 — GOVERNANÇA E DOCUMENTAÇÃO

11. Algum documento precisa ser atualizado esta semana?
    [ ] Não
    [ ] Sim — listar: [...]

12. Alguma decisão arquitetural nova foi tomada e precisa de ADR?
    [ ] Não
    [ ] Sim — descrever: [...]

13. O Document Registry está alinhado com o estado atual do repositório?
    [ ] Sim
    [ ] Não — o que diverge: [...]

---

SEÇÃO 4 — EVOLUÇÃO DO SISTEMA

14. O sistema está pronto para avançar de fase operacional?
    [ ] Não — manter READ_ONLY
    [ ] Talvez — critérios parcialmente cumpridos: [...]
    [ ] Sim — propor formalização de SIMULATE

15. Há algum agente cujo prompt precisa de revisão?
    [ ] Não
    [ ] Sim — qual e por quê: [...]

16. Há algum artefato legado que pode ser normalizado esta semana?
    [ ] Não
    [ ] Sim — listar IDs da triagem: [...]

---

SEÇÃO 5 — PRÓXIMA SEMANA

17. Quais ativos permanecem na watchlist?
18. Há alguma configuração macro relevante para a próxima semana?
19. Qual é a prioridade de governança para os próximos 7 dias?

---

AÇÃO DO JOURNAL AUDITOR
- Gerar entrada de revisão semanal com respostas consolidadas.
- Registrar decisões relevantes em DECISOES_ESTRATEGICAS se aplicável.
- Atualizar watchlist com base nos ativos da resposta 17.
```

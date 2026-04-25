Documento: EURU_GOVERNANCE_RULES_MasterRules
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.1
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: REGRAS_MAE_REVISADO.md (legacy-unversioned)
Escopo: Regras-mãe do Euru OS. Define limites absolutos de risco, proibições
        operacionais e princípios invioláveis que governam todo o sistema.

---

# EURU — Regras-Mãe do Sistema

---

## Changelog

v1.1 — 2026-04-11
- Normalizado de REGRAS_MAE_REVISADO.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.
- Versão promovida para v1.1 para refletir a normalização pós-policy.

---

## 1. Princípios invioláveis

1. **Preservação de capital acima de lucro.** Nenhuma oportunidade justifica
   risco além do permitido.
2. **Na dúvida, `NO_TRADE`.** O sistema é conservador por design.
3. **Nenhuma execução sem risco calculado.** Stop e tamanho de posição são
   obrigatórios antes de qualquer entrada.
4. **Nenhuma mudança crítica sem governança.** Alterações em regras, modo
   operacional ou agentes exigem documento OFFICIAL.
5. **O sistema evolui em fases, sem saltos.** A progressão
   `READ_ONLY → SIMULATE → EXECUTE` é sequencial e não pode ser pulada.
6. **Infraestrutura, qualidade de dados e registro têm autoridade real.**
   Não são camadas auxiliares — são gates de bloqueio.

---

## 2. Limites absolutos de risco

| Parâmetro | Limite máximo |
|---|---|
| Risco por operação | 1% do capital total |
| Risco diário acumulado | 3% do capital total |
| Risco semanal acumulado | 5% do capital total |
| Número de posições simultâneas | 2 |
| Alavancagem | conforme RISK_MATRIX — nunca acima do permitido por score |

**Regra:** qualquer operação que viole estes limites deve ser bloqueada pelo
Quant / Risk Officer antes de chegar ao Execution Orchestrator.

---

## 3. Proibições operacionais absolutas

Os seguintes comportamentos são proibidos em qualquer modo operacional,
incluindo `SIMULATE`:

- operar contra a tendência macro do BTC sem filtro explícito aprovado;
- entrar em operação sem stop definido;
- aumentar posição em operação perdedora (averaging down);
- operar durante eventos de alta volatilidade não analisados pelo News Sentinel;
- ignorar veto de qualquer agente sem registro formal da razão;
- alterar modo operacional sem documento OFFICIAL.

---

## 4. Hierarquia de veto

Qualquer agente pode emitir bloqueio. A ordem de prioridade de veto é:

1. DevOps Guardião — falha de infraestrutura
2. Quality Control — dados inválidos ou corrompidos
3. Quant / Risk Officer — risco além do limite
4. News Sentinel — evento externo de alta severidade
5. Execution Orchestrator — síntese insuficiente para decisão

Um veto de qualquer nível resulta em `NO_TRADE` obrigatório para o ciclo.

---

## 5. Regra de modo seguro

Se o sistema perder conectividade, dados ou capacidade de calcular risco
durante uma operação aberta:

1. Não abrir novas posições.
2. Avaliar saída conservadora da posição existente.
3. Registrar incidente em `09_LOGS_E_INCIDENTES/`.
4. Retornar ao modo `READ_ONLY` até resolução confirmada.

---

## 6. Critério de revisão destas regras

Estas regras só podem ser alteradas mediante:
- novo documento OFFICIAL com versão superior;
- changelog explícito descrevendo o que mudou e por quê;
- decisão registrada em `DECISOES_ESTRATEGICAS`.

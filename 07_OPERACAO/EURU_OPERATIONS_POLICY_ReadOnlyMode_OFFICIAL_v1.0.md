Documento: EURU_OPERATIONS_POLICY_ReadOnlyMode
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0
Substitui: MODO_READ_ONLY.txt (legacy-unversioned)
Escopo: Definição operacional completa do modo READ_ONLY. Especifica o que é
        permitido, o que é proibido, e como sair deste modo com governança.

---

# EURU — Política do Modo READ_ONLY

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de MODO_READ_ONLY.txt (.txt → .md) para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo revisado e alinhado com EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0.
- Declaração de estado canônico atual adicionada explicitamente.
- Critério de saída formalizado segundo padrão ADR.

---

## 1. Declaração de estado

**O modo READ_ONLY é o estado operacional canônico atual do Euru OS.**

Referência: EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0 e ADR_0001.

---

## 2. O que READ_ONLY significa

O sistema opera em modo de observação e análise. Nenhuma ordem real é enviada
à exchange. Nenhuma simulação formal de paper trade é contabilizada como
resultado oficial do sistema.

O modo READ_ONLY serve para:
- validar o pipeline de agentes em condições reais de mercado;
- construir historial de leituras antes de avançar;
- identificar e corrigir inconsistências de governança;
- calibrar scores e outputs dos agentes sem risco de capital.

---

## 3. O que é permitido em READ_ONLY

| Ação | Permitido |
|---|---|
| Executar ciclos diários completos | ✅ |
| Registrar setups identificados | ✅ |
| Fazer paper trades informais para aprendizado | ✅ |
| Atualizar documentos e normalizar artefatos | ✅ |
| Revisar e calibrar prompts dos agentes | ✅ |
| Observar mercado e registrar análises | ✅ |

---

## 4. O que é proibido em READ_ONLY

| Ação | Proibido |
|---|---|
| Enviar ordens reais à exchange | ❌ |
| Tratar paper trades como resultado oficial do sistema | ❌ |
| Declarar SIMULATE como estado vigente sem documento OFFICIAL | ❌ |
| Alterar chaves de API para permissão de saque ou execução | ❌ |

---

## 5. Critério para sair do modo READ_ONLY

A transição para `SIMULATE` só é válida quando **todos** os critérios abaixo
forem cumpridos simultaneamente:

- [ ] Pipeline completo executado por no mínimo 10 ciclos sem falhas críticas
- [ ] Todos os agentes com prompts canônicos em status OFFICIAL
- [ ] Document Registry atualizado e alinhado com repositório real
- [ ] Todos os artefatos críticos normalizados (Tracks 01 e 02 concluídos)
- [ ] Decisão formalizada em novo documento OFFICIAL com versão, data e changelog
- [ ] ADR registrando a mudança de estado

Sem esses critérios, qualquer menção a SIMULATE é tratada como referência
não canônica (conforme ADR_0001).

---

## 6. Como retornar ao READ_ONLY (modo seguro)

O sistema deve retornar a READ_ONLY imediatamente se qualquer das condições
abaixo ocorrer:

- DevOps Guardião emite `CRITICAL_FAILURE`;
- drawdown acumulado atinge 10% do capital;
- Quality Control emite `DATA_BLOCKED` em dois ciclos consecutivos;
- falha de infraestrutura não resolvida em 24h;
- decisão humana explícita do Risk / Product Owner.

O retorno ao READ_ONLY não requer documento novo — é automático pelas condições
acima. A saída do READ_ONLY requer documento OFFICIAL.

Documento: EURU_GOVERNANCE_POLICY_HumanResponsibilities
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: RESPONSABILIDADES_HUMANOS_REVISADO.md (legacy-unversioned)
Escopo: Define o papel dos humanos na governança e operação do Euru OS.
        Estabelece o que nunca pode ser delegado a agentes ou automações.

---

# EURU — Responsabilidades Humanas

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de RESPONSABILIDADES_HUMANOS_REVISADO.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## 1. O que nunca pode ser delegado

As seguintes decisões são exclusivamente humanas e não podem ser executadas
por agente, script ou automação, em nenhum modo operacional:

- alterar o modo operacional do sistema (`READ_ONLY → SIMULATE → EXECUTE`);
- aprovar qualquer documento como OFFICIAL;
- definir ou alterar limites de risco;
- autorizar execução real de ordens na exchange;
- revogar ou substituir uma ADR;
- decidir sobre reversão de mudança crítica.

---

## 2. Papéis humanos no sistema

| Papel | Responsabilidades |
|---|---|
| **Risk / Product Owner** | Valida regras, fase operacional e política de risco. Aprova documentos OFFICIAL. |
| **Operator / Maintainer** | Executa SOPs diários e semanais. Atualiza Registry e artefatos legados. Registra incidentes. |
| **DevOps / Repository Custodian** | Garante que estrutura do repositório reflete o que está documentado. Gerencia scripts e automações. |

---

## 3. Ciclo de responsabilidade diária

O operador humano é responsável por:

1. Iniciar a sessão com verificação do checklist pré-operação.
2. Confirmar o output do DevOps Guardião antes de prosseguir.
3. Revisar os relatórios dos agentes e validar a decisão de `TRADE` ou `NO_TRADE`.
4. Registrar a sessão no journal ao final.
5. Escalar qualquer incidente não resolvido antes de encerrar o dia.

---

## 4. Ciclo de responsabilidade semanal

1. Revisar o journal da semana.
2. Avaliar performance dos paper trades ou operações reais.
3. Verificar se algum documento requer atualização.
4. Confirmar que o Registry está alinhado com o estado real do repositório.
5. Decidir se há mudança de fase operacional a formalizar.

---

## 5. Princípio fundamental

O Euru OS é um sistema de **apoio à decisão**, não de **substituição da decisão**.

Nenhum output de agente, por mais convergente que seja, substitui a leitura
final do operador humano. O sistema maximiza a qualidade da informação disponível
— a responsabilidade pela ação é sempre humana.

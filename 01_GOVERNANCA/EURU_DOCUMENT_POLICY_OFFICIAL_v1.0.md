# EURU_DOCUMENT_POLICY — Política única de versionamento documental

**Status:** OFFICIAL  
**Versão:** v1.0  
**Owner:** Governança EURU  
**Última atualização:** 2026-04-11  
**Documento pai:** EURU_MASTER_DOCUMENTO

## 1. Objetivo e escopo

Esta política estabelece uma regra única para criação, nomeação, revisão, aprovação, versionamento, arquivamento e uso de documentos do EURU, inclusive quando o material for interpretado por outras IAs.

Aplica-se a documentos estratégicos, operacionais, arquiteturais, prompts de agentes, briefings, formatos de saída, playbooks, logs, notas e arquivos produzidos com apoio de IA.

## 2. Princípios de governança

1. **Fonte única de verdade:** o Master Documento orienta a leitura sistêmica.
2. **Rastreabilidade:** toda mudança relevante precisa deixar rastro legível.
3. **Separação entre oficial e trabalho:** rascunhos e testes não competem com documentos oficiais.
4. **Conflito explícito:** quando houver divergência, deve-se sinalizar o conflito, não decidir silenciosamente.
5. **Compatibilidade homem + IA:** a redação deve ser compreensível para humanos e interpretável por IA.

## 3. Hierarquia documental

Em caso de conflito, siga esta ordem de autoridade:

1. EURU_MASTER_DOCUMENTO
2. Governance / Policies
3. Architecture / Operational Framework
4. Agent Prompts
5. Briefings / Output Formats
6. Drafts / Logs / Notes

## 4. Status documentais

- **DRAFT** — em construção
- **REVIEW** — pronto para revisão
- **OFFICIAL** — válido e aplicável
- **DEPRECATED** — não usar mais, mas manter para histórico

## 5. Política de versionamento

Modelo adotado: **vMAJOR.MINOR**

- **v1.0** = primeira versão oficial
- **v1.1** = ajuste menor, melhoria textual, nomenclatura, clareza
- **v1.2** = refinamento incremental
- **v2.0** = mudança estrutural de regra, fluxo, responsabilidade ou arquitetura

## 6. Convenção de nomes

Padrão:

`EURU_[AREA]_[SUBAREA]_[NOME]_[STATUS]_vX.Y.ext`

Exemplos:

- `EURU_GOVERNANCE_MASTER_DOCUMENT_OFFICIAL_v1.0.docx`
- `EURU_AGENTS_FLOW_ANALYST_PROMPT_OFFICIAL_v2.1.md`
- `EURU_RISK_EXIT_POLICY_REVIEW_v0.8.md`

## 7. Metadados mínimos obrigatórios

Todo documento deve conter no topo:

```txt
Documento: EURU_[AREA]_[SUBAREA]_[NOME]
Owner: [responsável]
Status: [DRAFT | REVIEW | OFFICIAL | DEPRECATED]
Versão: vX.Y
Última atualização: AAAA-MM-DD
Documento pai: [nome do documento superior]
Substitui: [versão anterior ou N/A]
Escopo: [o que este documento cobre]
Observações: [opcional]
```

## 8. Fluxo de alteração e aprovação

1. Criar ou editar em **DRAFT**
2. Submeter para **REVIEW**
3. Validar consistência com documentos superiores
4. Promover para **OFFICIAL**
5. Registrar changelog
6. Atualizar o Master Documento se a mudança afetar a lógica do sistema

## 9. Changelog obrigatório

Modelo:

```txt
Changelog

v1.2 — AAAA-MM-DD
- O que mudou
- Impacto principal

v1.1 — AAAA-MM-DD
- O que mudou
- Impacto principal
```

## 10. Estrutura recomendada de repositório

```txt
/EURU
  /00_MASTER
  /01_GOVERNANCE
  /02_ARCHITECTURE
  /03_AGENTS
  /04_OPERATIONS
  /05_RISK
  /06_DATA
  /07_LOGS
  /08_WORKING_DRAFTS
  /09_DEPRECATED
```

Regra: documentos válidos ficam fora de `WORKING_DRAFTS`. Documentos aposentados vão para `DEPRECATED`.

## 11. Uso com outras IAs

Sempre fornecer à outra IA:

1. O Master Documento
2. A regra de autoridade
3. O objetivo da tarefa
4. A regra de saída esperada

## 12. Prompt mestre para outra IA

```txt
Você está analisando a documentação do projeto EURU.

Use o Master Documento como fonte principal de verdade.
Em caso de conflito entre arquivos, siga esta hierarquia:
1. Master Documento
2. Governance / Policies
3. Architecture
4. Agent Prompts
5. Briefings / Output Formats
6. Drafts / Logs / Notes

Sua função é:
- identificar inconsistências
- propor melhorias sem quebrar a lógica atual
- separar o que é oficial do que é rascunho
- preservar nomenclatura, governança e rastreabilidade

Regras:
- não invente estruturas não suportadas pelos documentos
- toda sugestão nova deve ser marcada como PROPOSTA
- toda mudança relevante deve citar impacto no sistema
- quando houver dúvida, sinalize o conflito em vez de assumir

Formato de resposta:
1. Resumo executivo
2. Inconsistências encontradas
3. Riscos
4. Melhorias sugeridas
5. Versão consolidada proposta
6. Changelog sugerido
```

## 13. Checklist de promoção para OFFICIAL

- O documento tem owner, status, versão e data
- O documento não contradiz um nível superior da hierarquia
- O changelog foi atualizado
- O nome do arquivo segue a convenção padrão
- O documento foi colocado na pasta correta do repositório
- O Master Documento foi atualizado, se necessário

---
**Fim do documento oficial v1.0**

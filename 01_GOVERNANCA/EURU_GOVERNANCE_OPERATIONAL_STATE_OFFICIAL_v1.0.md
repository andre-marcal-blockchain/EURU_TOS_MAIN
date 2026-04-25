# EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0

**Documento:** EURU_GOVERNANCE_OPERATIONAL_STATE  
**Owner:** Andrezão / Governança Euru  
**Status:** OFFICIAL  
**Versão:** v1.0  
**Última atualização:** 2026-04-11  
**Documento pai:** EURU_MASTER_DOCUMENTO  
**Escopo:** Definir o estado operacional canônico do Euru OS e a regra de tratamento para conflitos futuros.

---

## 1. Decisão oficial

Após revisão da documentação atualmente consolidada do projeto, foi identificado conflito entre referências aos estados operacionais **READ_ONLY** e **SIMULATE**.

Na ausência de um documento posterior, versionado, aprovado e explicitamente publicado como **OFFICIAL** que substitua o modo **READ_ONLY**, fica definido que:

> **O estado operacional canônico atual do Euru OS é READ_ONLY.**

---

## 2. Classificação do modo SIMULATE

O modo **SIMULATE** não é reconhecido, neste momento, como estado operacional oficial vigente.

Ele deve ser tratado como uma das seguintes classificações, conforme contexto do arquivo analisado:

- referência experimental
- estado proposto
- menção não canônica
- hipótese operacional
- candidato a formalização futura

Em nenhuma hipótese uma menção isolada a **SIMULATE** deve ser interpretada como mudança oficial de estado.

---

## 3. Regra de decisão

Sempre que houver conflito entre estados operacionais em documentos diferentes, aplicar a seguinte regra:

1. prevalece o documento de maior autoridade documental;
2. na ausência de ratificação formal, prevalece o estado mais conservador;
3. nenhuma alteração de estado é válida sem documento **OFFICIAL**, versão, data e changelog;
4. referências dispersas em prompts, notas, rascunhos ou logs não alteram o estado canônico do sistema.

---

## 4. Hierarquia usada para resolver conflito

A seguinte ordem de autoridade documental deve ser usada para resolver qualquer conflito relacionado ao estado operacional:

1. Master Documento
2. Governance / Policies
3. Architecture / Operational Framework
4. Agent Prompts
5. Briefings / Outputs Formats
6. Logs / Notes / Drafts

---

## 5. Regra de normalização do repositório

Até nova deliberação oficial:

- **READ_ONLY** deve aparecer como estado vigente;
- toda menção a **SIMULATE** deve ser revista e marcada como:
  - `PROPOSED_STATE`, ou
  - `NON_CANONICAL_REFERENCE`, ou
  - `EXPERIMENTAL_MODE_REFERENCE`
- documentos que contradigam esta decisão devem entrar em fila de revisão.

---

## 6. Regra para uso por outras IAs

Qualquer IA que receba documentação do Euru deve obedecer à seguinte instrução:

- tratar **READ_ONLY** como estado canônico atual;
- tratar **SIMULATE** como referência não ratificada;
- sinalizar conflito sempre que encontrar menção a **SIMULATE** como se fosse estado vigente;
- nunca promover mudança de estado sem documento oficial posterior.

---

## 7. Critério para futura mudança de estado

O estado operacional só poderá mudar de **READ_ONLY** para outro modo se existirem, ao mesmo tempo:

- documento formal **OFFICIAL**
- versão nova
- data de aprovação
- changelog explícito
- indicação clara de substituição do estado anterior

---

## 8. Texto oficial de normalização

Use o texto abaixo para colar em documentos, prompts, repositórios ou briefings:

> Após revisão da documentação consolidada do projeto, o estado operacional canônico atual do Euru OS é **READ_ONLY**. O modo **SIMULATE** permanece classificado como referência não ratificada, proposta experimental ou menção não canônica, até publicação de documento **OFFICIAL** que formalize a mudança de estado.

---

## 9. Impacto prático

Esta decisão destrava imediatamente:

- revisão documental
- reorganização do repositório
- auditoria de prompts
- uso coordenado com outras IAs
- padronização de outputs e briefings
- limpeza de inconsistências sem reabrir discussão de estado

---

## 10. Changelog

**v1.0 - 2026-04-11**
- Formalizada a decisão canônica de estado operacional do Euru OS
- Definido READ_ONLY como estado vigente
- Classificado SIMULATE como referência não ratificada
- Criadas regras de uso compartilhável entre IAs

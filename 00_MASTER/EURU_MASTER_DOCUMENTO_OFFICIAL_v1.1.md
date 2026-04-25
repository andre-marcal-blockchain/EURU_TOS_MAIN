# EURU OS — MASTER DOCUMENTO
## Mapa Mestre de Governança, Arquitetura, Operação e Registro Documental

**Documento:** `EURU_MASTER_DOCUMENTO`  
**Owner:** `Andrezão / Governança Euru`  
**Status:** `OFFICIAL`  
**Versão:** `v1.1`  
**Última atualização:** `2026-04-11`  
**Documento pai:** `EURU_DOCUMENT_POLICY_OFFICIAL_v1.0`  
**Substitui:** `EURU_MASTER_DOCUMENTO v1.0 (REVIEW)`  
**Estado operacional canônico:** `READ_ONLY`  
**Snapshot analisado:** `Euru_TOS.zip`  

---

## 1. Objetivo

Este documento existe para funcionar como a **fonte-mãe de interpretação do Euru OS**.

Ele responde a quatro perguntas fundamentais:
- o que é o sistema;
- como ele está organizado;
- qual é a leitura canônica dos agentes e do estado operacional;
- quais documentos devem ser consultados primeiro.

---

## 2. Leitura executiva do Euru OS

O Euru OS é um sistema de decisão e governança para trading de criptoativos. O snapshot mostra um projeto que já combina:
- documentação de governança;
- artefatos operacionais de uso diário;
- agentes especializados com papéis distintos;
- scripts práticos de automação;
- trilha de evidência em watchlists, scorecards, journals e incidentes.

A leitura oficial desta versão é:
- o sistema **não** deve ser interpretado como um bot livre de restrições;
- o sistema existe para favorecer disciplina, veto, rastreabilidade e preservação de capital;
- em caso de conflito documental, prevalece a governança formal e o modo mais conservador.

---

## 3. Estrutura-base identificada no snapshot

| Pasta | Papel no sistema |
|---|---|
| `01_GOVERNANCA` | regras, decisões, mudanças e responsabilidades |
| `02_BINANCE_SETUP` | setup operacional de exchange e segurança |
| `03_ARQUITETURA` | visão lógica do pipeline |
| `04_AGENTES` | briefings, outputs e prompts dos agentes |
| `05_PROMPTS` | prompts operacionais de uso diário, pré, pós e semanal |
| `06_RISCO_E_EXECUCAO` | racional quantitativo de risco |
| `07_OPERACAO` | SOPs, modo seguro e política de saída |
| `08_DADOS_E_JOURNAL` | evidência viva do sistema |
| `09_LOGS_E_INCIDENTES` | trilha de problemas e mudanças |
| `11_CONFIG_PLACEHOLDERS` | placeholders e separação de segredos |
| `99_PRIVATE_NOTES` | notas estratégicas e material ainda não institucionalizado |

---

## 4. Estado operacional canônico

A decisão formal já consolidada fora deste documento e incorporada aqui é a seguinte:

**Estado operacional canônico atual do Euru OS: `READ_ONLY`.**

Leitura complementar:
- referências a `SIMULATE` existem no snapshot;
- essas referências são tratadas como **não ratificadas**;
- nenhuma IA ou humano deve tratar `SIMULATE` como vigente sem documento `OFFICIAL` posterior.

---

## 5. Pipeline lógico de decisão

A arquitetura observada aponta para uma cadeia de decisão em que agentes posteriores podem confirmar, contradizer ou vetar agentes anteriores.

Em termos simples, a lógica é:
1. leitura estrutural do mercado;
2. validação técnica do setup;
3. leitura de contexto e narrativa;
4. cálculo de risco e viabilidade;
5. checagem metodológica;
6. orquestração final da decisão;
7. validação de infraestrutura, qualidade e rastreabilidade.

A interpretação oficial é: **quando houver dúvida, o sistema favorece `NO_TRADE`.**

---

## 6. Mapa canônico dos agentes

### 6.1 Numeração canônica oficial

| Nº canônico | Agente | Papel principal |
|---|---|---|
| 01 | Scout | leitura estrutural e filtro inicial |
| 02 | Flow Analyst | confirmação ou invalidação técnica |
| 03 | News Sentinel | contexto informacional e severidade |
| 04 | Quant / Risk Officer | cálculo de posição, stop, alvo e aderência ao risco |
| 05 | Execution Orchestrator | síntese final e decisão integrada |
| 06 | DevOps Guardião | saúde técnica, APIs, latência e segurança |
| 07 | Journal Auditor | rastreabilidade, registro e auditoria |
| 08 | Score Engine | consolidação quantitativa dos sinais |
| 09 | Watchdog | heartbeat, falhas silenciosas e recuperação |
| 10 | MAC / Playbook Analyst | aderência ao método MAC e setups oficiais |
| 11 | Quality Control | integridade e schema dos dados |

### 6.2 Registro do conflito observado no snapshot bruto

O snapshot original contém inconsistências de nomenclatura e numeração, incluindo:
- `08_SCORE_ENGINE`
- `08_WATCHDOG`
- `09_MAC_PLAYBOOK_ANALYST`
- `09_QUALITY_CONTROL`
- `10_QUALITY_CONTROL`

Nesta versão `v1.1 OFFICIAL`, a leitura canônica fica formalizada assim:
- `08` = Score Engine
- `09` = Watchdog
- `10` = MAC / Playbook Analyst
- `11` = Quality Control

O snapshot bruto permanece como evidência histórica. A interpretação operacional do sistema deve obedecer à numeração acima.

---

## 7. Documentos que sustentam a governança atual

| Camada | Documento-chave |
|---|---|
| Policy | `EURU_DOCUMENT_POLICY_OFFICIAL_v1.0` |
| Estado operacional | `EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0` |
| ADR | `ADR_0001_EURU_CANONICAL_OPERATIONAL_STATE_READ_ONLY` |
| Registry | `EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.0` |
| Snapshot-governança | `REGRAS_MAE_REVISADO.md` |
| Snapshot-operação | `MODO_READ_ONLY.txt` |

---

## 8. Uso obrigatório com outras IAs

Qualquer outra IA que entre no projeto deve iniciar por esta ordem:
1. `EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1`
2. `EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.0`
3. `EURU_DOCUMENT_POLICY_OFFICIAL_v1.0`
4. decisão canônica do estado operacional
5. documentos específicos da tarefa

Nenhuma IA deve:
- promover um modo operacional sem ratificação formal;
- ignorar o Registry ao escolher um arquivo vigente;
- reinterpretar a numeração dos agentes fora do padrão acima.

---

## 9. O que foi resolvido nesta versão

Esta versão fecha duas lacunas críticas:
1. corrige a numeração canônica dos agentes em `§6.1`;
2. transforma o Registry em catálogo operacional obrigatório.

O que permanece como manutenção contínua:
- normalização final dos nomes legados de prompts e outputs;
- consolidação física futura das pastas duplicadas de `Quality Control`;
- revisão periódica do Registry sempre que um documento oficial mudar.

---

## 10. Changelog

### v1.1 — 2026-04-11
- Corrigida a numeração canônica dos agentes.
- Formalizado o uso do Registry como catálogo obrigatório.
- Promovido o Master Documento para `OFFICIAL`.
- Incorporado `READ_ONLY` como estado operacional canônico vigente.

### v1.0 — 2026-04-11
- Primeira consolidação do material do snapshot.

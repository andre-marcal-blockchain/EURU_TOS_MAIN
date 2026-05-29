---
schema_type: design_spec_validation
schema_version: 1.0
document_id: EURU-DESIGN-SPEC-v0.1-VALIDATION-2026-05-29
created: 2026-05-29
timezone: Europe/Madrid
system: Euru OS
phase_context: Fase 2 Design
operational_mode: READ_ONLY
gate_reference: T+28D / 2026-05-28
gate_decision: Opcao A hibrida controlada
target_artifact: EURU_DESIGN_SPEC_v0.1.md
target_artifact_commit: 8ca60a3
validation_basis:
  - EURU_MASTER_HANDOFF_CONTINUIDADE_2026-05-29.md
  - EURU_DESIGN_SPEC_v0.1.md
  - EURU_FASE1_CANDIDATES_REVIEW.md
  - EURU_TYPE2_DECISION_FASE2_2026-05-14.md
  - EURU_OPERATIONAL_RUNBOOK_FASE2_2026-05-14.md
regime_scope: bearish-derived (D15-D28)
bull_regime_validation: pending
canonical_status: DRAFT_PENDING_OPERATOR_REVIEW
authors: Claude (proposta), Codex (tensao e preenchimento), Andre Marcal (decisao)
---

# EURU Design Spec v0.1 - Validation

**Status:** DRAFT_PENDING_OPERATOR_REVIEW  
**Target:** `EURU_DESIGN_SPEC_v0.1.md`  
**Scope:** completude da spec v0.1 + cobertura empirica D15-D28  
**Modo:** READ_ONLY, documento nao-executavel

---

## 1. Proposito e Escopo

Este documento valida a `EURU_DESIGN_SPEC_v0.1.md` em dois eixos: completude como artefato de design nao-executavel e cobertura empirica das quatro dimensoes contra os casos D15-D28.

O escopo e especifico: validar a spec v0.1 como artefato bearish-derived, nascido do gate T+28D e da Opcao A hibrida controlada.

Este documento nao e process spec generico, nao substitui o protocolo Claude+Codex+Operador, e nao autoriza execucao, implementacao, paper trading, rule promotion ou alteracao de Core.

---

## 2. Exclusoes Declaradas

Licoes incorporadas do draft rejeitado `EURU_POST_GATE_SPEC_VALIDATION_2026-05-29.REJECTED_DRAFT.md`:

- Nao cria taxonomia nova.
- Nao substitui o protocolo de trabalho do handoff mestre secao 17.
- Nao estabelece novas regras quantitativas de promocao.
- Nao prescreve workflow pos-gate generico.
- Nao valida execucao, paper trading, rule promotion ou alteracao de Core.
- Nao e process spec; e validation report sobre artefato especifico.
- Nao altera EXCLUDE list.
- Nao transforma gate em permissao de implementacao.

---

## 3. Criterios de Completude

### 3.1 Criterio Nativo da Spec v0.1

A propria spec v0.1 define o criterio interno de completude por dimensao:

> cada dimensao tem os 4 elementos (a) definicao, (b) inputs/sinais, (c) regra de leitura, (d) tag de validade por regime.

Aplicacao contra a spec primaria:

| Dimensao | (a) Definicao | (b) Inputs/sinais | (c) Regra de leitura | (d) Tag de validade por regime | Resultado |
|---|---|---|---|---|---|
| `macro_permission` | Presente na secao 3.1 | Presente: Morning/Asian Master Filter | Presente: VETOED/CONDITIONAL/PERMITTED | Presente: bearish true, bull pending, SIDEWAYS_as_VETOED pending | PASS |
| `directional_bias` | Presente na secao 3.2 | Presente: MACD/trend/OBV/duracao | Presente: BULLISH/BEARISH/MIXED + qualifier | Presente: BEARISH validado, BULLISH pending, MIXED parcial | PASS |
| `technical_strength_score` | Presente na secao 3.3 | Presente: Core score/tier/RSI/compressao | Presente: magnitude + load_type | Presente: bearish true, bull pending, load_type parcial | PASS |
| `operable_quality` | Presente na secao 3.4 | Presente: coerencia/state/risco/limpeza | Presente: CLEAN/NOISY/INSUFFICIENT_DATA | Presente: bearish parcial, bull pending | PASS |

Resultado: a spec v0.1 satisfaz o criterio nativo de completude formal por dimensao.

### 3.2 Criterios deste Validation Report

Estes criterios avaliam o artefato spec v0.1 como um todo. Eles nao substituem o criterio interno (a)/(b)/(c)/(d); sao complementares.

| Criterio | Definicao | Resultado | Evidencia |
|---|---|---|---|
| C1 - Cobertura dimensional | 4 dimensoes presentes com pergunta, funcao, estados e principio | PASS | Spec v0.1 secoes 2 e 3.1-3.4 |
| C2 - Ordenacao justificada | Ordem global para local declarada: regime -> direcao -> carga tecnica -> limpeza local | PASS | Handoff mestre secao 9; spec v0.1 separa macro_permission de operable_quality |
| C3 - Travas anti-gate-creep | Cada dimensao declara o que nao faz | PASS | directional_bias nao concede permissao; technical_strength nao e oportunidade; operable_quality nao e gate/media/veredito |
| C4 - Honestidade epistemica | Estados validated/pending/parcial declarados | PASS | Tags `validated_in_bearish`, `bull_regime_validation`, slots pendentes e notas de under-validation |
| C5 - Ancora empirica minima | Pelo menos um caso por dimensao no artefato original | PARTIAL | Secao 4 da spec lista casos vivos, mas ainda marcada como `_ [a desenvolver] _` |

### 3.3 Nota sobre C5

A secao "Casos vivos de validacao (D15-D28)" da spec v0.1 esta marcada como `_ [a desenvolver] _`.

Este validation report complementa essa secao mapeando casos D15-D28 contra as dimensoes, mas nao declara que a spec original ja cobria esse mapeamento em detalhe. Assim, C5 e `PARTIAL` no artefato original, com este documento servindo como registro externo de cobertura empirica.

---

## 4. Validacao Dimensional contra D15-D28

Esta secao aplica os casos D15-D28 do `EURU_FASE1_CANDIDATES_REVIEW.md` contra as quatro dimensoes da spec v0.1. Cada dimensao recebe estado de validacao, tensao/limitacao e carry-forward.

Estados usados neste relatorio:

- `VALIDATED_IN_BEARISH`
- `PARTIALLY_VALIDATED`
- `ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING`
- `PENDING_BULL_REGIME`

Nenhum estado adicional e criado. Tensoes sao registradas em coluna propria.

### 4.1 macro_permission

Resumo: `macro_permission` e permissao de regime, universal ao universo observado. A spec define os estados `VETOED`, `CONDITIONAL` e `PERMITTED`.

Evidencia primaria:

- D14-D28: Morning Master Filter ACTIVE continuamente, chegando ao 22o dia consecutivo em D28.
- D21-D22/D24-D26: BTC SIDEWAYS ainda manteve Morning ACTIVE; SIDEWAYS funcionou como bloqueio.
- D28: 18/18 ativos negativos, BTC novo low 73,181.94, BTC `PREMIUM / SETUP` 31/35 sob Morning ACTIVE e trend BEARISH.
- Sintese T+28D: "Morning Master Filter: ACTIVE continuo TODA a janela".

Leitura: `VETOED` esta validado na janela bearish. `CONDITIONAL` e `PERMITTED` existem como slots arquiteturais, mas nao foram observados em D15-D28.

| Estado | Validation | Tension / Limitation | Carry-forward |
|---|---|---|---|
| `VETOED` | VALIDATED_IN_BEARISH | 100% da janela ficou sob veto; nao houve transicao out-of-VETOED | Observar proxima janela nao-vetada |
| `CONDITIONAL` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Regra preliminar; nunca observado D15-D28 | Calibrar quando Morning INACTIVE + 4H incerto/comprimido |
| `PERMITTED` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Nunca observado D15-D28 | Validar em bull/neutral regime |
| `SIDEWAYS_as_VETOED` | PENDING_BULL_REGIME | Bearish-derived; pode ser artefato do regime bearish | Validar se SIDEWAYS deve bloquear igual a BEARISH noutro regime |

Conclusao: `macro_permission` e completa como dimensao e fortemente validada para o estado `VETOED`, mas seus estados permissivos continuam pendentes por ausencia empirica.

### 4.2 directional_bias

Resumo: `directional_bias` mede inclinacao direcional por ativo via MACD + trend, com OBV como confirmacao/divergencia e duracao como qualifier. A spec declara a trava anti-gate: `directional_bias` nunca concede permissao operacional.

Evidencia primaria:

- D22: OBV RISING expandiu para 7/9 priorizados, mas todos os sete continuavam MACD BEARISH; a propria entrada registra divergencia flow/trend e design evidence para separar OBV de MACD/trend.
- D24-D28: FET foi caso de bolso `BULLISH/SUSTAINED`: MACD BULLISH por quatro dias, mas quebrou no D28 com -9.10%, perdendo PREMIUM. Isto confirma que `SUSTAINED` descreve persistencia ate entao, nao previsao.
- D28: 13/18 MACD BEARISH e 18/18 ativos negativos; `BEARISH` permaneceu dominante.
- Spec v0.1: OBV/MACD divergence D22/D24 e citado como caso de `MIXED / unresolved directional bias`.

Leitura: a dimensao separa direcao de permissao. Um bolso bullish em FET nao abriu permissao porque `macro_permission` permaneceu `VETOED`.

| Estado / qualifier | Validation | Tension / Limitation | Carry-forward |
|---|---|---|---|
| `BEARISH` | VALIDATED_IN_BEARISH | Dominante na janela; nao tensiona a arquitetura | Continuar observacao leve |
| `BULLISH` | PARTIALLY_VALIDATED | FET D24-D28 confirma categoria, mas quebrou sob macro VETOED; falta bullish sob PERMITTED | Validar em regime permissivo |
| `MIXED / unresolved` | PARTIALLY_VALIDATED | Divergencias OBV/MACD D22/D24 citadas como observadas; catalogo incompleto | Catalogar configuracoes MIXED em regimes variados |
| `SUSTAINED` | PARTIALLY_VALIDATED | FET aplica; N de dias nao calibrado | Definir N a calibrar por evidencia |
| `TRANSIENT` | PARTIALLY_VALIDATED | INJ bounce/re-heating D26 arrefeceu D27-D28; N nao calibrado | Definir N a calibrar por evidencia |

Conclusao: `directional_bias` esta validado como separacao necessaria sob regime bearish, parcialmente validado para bolsos bullish/mixed, e pendente para calibracao de qualifiers.

### 4.3 technical_strength_score

Resumo: `technical_strength_score` mede magnitude tecnica sem direcao e sem operabilidade. O Core score entra como `legacy composite proxy for technical load`, nao como autoridade operacional. Principio central: forca tecnica nao e operabilidade.

Evidencia primaria:

- D28: BTC `PREMIUM / SETUP` 31/35 com -3.17%, RSI 34.68, novo low da janela e Morning ACTIVE. Caso-limite: `technical_strength` alto + `directional_bias` BEARISH + `macro_permission` VETOED.
- D18/D23/D28: score-directionality gap amplificado; D28 teve 18/18 ativos negativos e 7/9 scores subindo.
- ARB D18/D21: score subindo enquanto o ativo piorava; caso de instabilidade oscilatoria.
- INJ D14-D20: RSI extremo e drawdown validaram RC001-R1 como risk flag retrospectivo.
- D16-D22/D26: GEM_ALERT recorrente no 4H documentou compressao tatica, mas sem daily unlock.

Fronteira textual da spec: `EXTENDED_DOWN` nao significa `BEARISH`; `BEARISH` pertence a `directional_bias`. `EXTENDED_DOWN` descreve carga tecnica/oversold apos movimento para baixo.

| Estado / load_type | Validation | Tension / Limitation | Carry-forward |
|---|---|---|---|
| `EXTENDED_DOWN` | VALIDATED_IN_BEARISH | BTC D28 e ARB reforcam forca != operavel | Continuar mapear casos oversold sob veto |
| `EXTENDED_UP` | PARTIALLY_VALIDATED | INJ D14-D20 validou episodio de risco; sem 2o episodio confirmado | Monitorar 2-3 ocorrencias adicionais para RC001-R1 |
| `COMPRESSED` | PARTIALLY_VALIDATED | GEM_ALERT recorrente observado; fronteiras de resolucao ainda pending | Calibrar compressao que resolve para breakout vs WATCHLIST/NO_TRADE |
| `NEUTRAL` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Janela dominada por extremos bearish/compressao; pouca evidencia neutra | Validar em regime menos extremo |
| RC001-R1 risk flag | PARTIALLY_VALIDATED | PROVISIONALLY_VALIDATED como risk flag, nao regra oficial; 1 episodio confirmado | Requer 2-3 ocorrencias adicionais + operator review |

Conclusao: `technical_strength_score` e a dimensao empiricamente mais reforcada por D15-D28, especialmente pelo caso BTC D28. A validacao nao promove o score a sinal; faz o contrario, documenta por que ele deve ser separado.

### 4.4 operable_quality

Resumo: `operable_quality` e a qualidade local da leitura/setup, ultima dimensao a ler. A spec estabelece tripla trava: nao e gate, nao e media, nao e veredito.

Evidencia primaria:

- D28: BTC state SETUP, mas leitura 4-D e nao-operavel por veto macro; o state isolado nao basta.
- D22/D24: divergencias OBV/MACD geram friccao inter-dimensional, parcialmente validando `NOISY`.
- Toda a janela D15-D28 ficou sob `macro_permission=VETOED`; `operable_quality` nunca esteve no assento do condutor.
- Spec v0.1 declara `INSUFFICIENT_DATA` como estado honesto dominante e `operable_quality` como empiricamente under-validated.

| Estado | Validation | Tension / Limitation | Carry-forward |
|---|---|---|---|
| `CLEAN` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Quase totalmente pending; 100% VETOED impediu validacao de clean setup operavel | Validar quando macro_permission != VETOED |
| `NOISY` | PARTIALLY_VALIDATED | MIXED/divergencias OBV/MACD D22/D24 observadas; catalogo incompleto | Mapear friccoes inter-dimensionais futuras |
| `INSUFFICIENT_DATA` | VALIDATED_IN_BEARISH | Validado como estado honesto dominante, nao como capacidade operacional validada | Reduzir insuficiencia com inputs de risco/invalidacao |

Conclusao: `operable_quality` e arquiteturalmente necessaria e honestamente under-validated. O gap empirico e propriedade da janela, nao falha da spec.

---

## 5. Matriz Consolidada de Validacao

| Dimensao | Estado/sub-estado | Validation | Tension / Limitation | Carry para v0.2 |
|---|---|---|---|---|
| `macro_permission` | `VETOED` | VALIDATED_IN_BEARISH | Sem out-of-VETOED na janela | Observar transicao |
| `macro_permission` | `CONDITIONAL` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Regra preliminar | Calibrar criterio |
| `macro_permission` | `PERMITTED` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Nunca observado | Bull/neutral regime |
| `macro_permission` | `SIDEWAYS_as_VETOED` | PENDING_BULL_REGIME | Bearish-derived | Neutral validation |
| `directional_bias` | `BEARISH` | VALIDATED_IN_BEARISH | Dominante D15-D28 | Continuar observar |
| `directional_bias` | `BULLISH` | PARTIALLY_VALIDATED | FET quebrou sob VETOED | Bullish sob PERMITTED |
| `directional_bias` | `MIXED / unresolved` | PARTIALLY_VALIDATED | D22/D24 observados; catalogo incompleto | Regimes variados |
| `directional_bias` | `SUSTAINED` qualifier | PARTIALLY_VALIDATED | N de dias nao calibrado | N a calibrar |
| `directional_bias` | `TRANSIENT` qualifier | PARTIALLY_VALIDATED | N de dias nao calibrado | N a calibrar |
| `technical_strength_score` | `EXTENDED_DOWN` | VALIDATED_IN_BEARISH | BTC D28 caso-limite | Continuar mapear |
| `technical_strength_score` | `EXTENDED_UP` | PARTIALLY_VALIDATED | INJ D14-D20 unico episodio confirmado | Novas ocorrencias |
| `technical_strength_score` | `COMPRESSED` | PARTIALLY_VALIDATED | GEM_ALERT recorrente; fronteiras pending | Calibrar resolucoes |
| `technical_strength_score` | `NEUTRAL` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Pouco observado | Regime diversificado |
| `operable_quality` | `CLEAN` | ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | Depende de out-of-VETOED | Bull/neutral validation |
| `operable_quality` | `NOISY` | PARTIALLY_VALIDATED | D22/D24 friccao observada | Catalogo de ruido |
| `operable_quality` | `INSUFFICIENT_DATA` | VALIDATED_IN_BEARISH | Estado honesto dominante, nao capacidade operacional | Inputs de risco/invalidacao |

Contagem consolidada:

| Validation | Contagem |
|---|---:|
| VALIDATED_IN_BEARISH | 4 |
| PARTIALLY_VALIDATED | 7 |
| ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING | 4 |
| PENDING_BULL_REGIME | 1 |

Leitura: a spec v0.1 e completa como arquitetura bearish-derived, com validacao forte nos estados expostos pela janela bearish e pendencias explicitas onde a janela nao forneceu evidencia.

---

## 6. Carry-forward para v0.2

Cada item declara o que falta, que evidencia destrava, e o que nao destrava.

### 6.1 Bull/neutral regime validation de `macro_permission`

- Falta: observacao de janela com Morning Filter nao-ACTIVE sustentado.
- Destrava: nova janela observacional com `macro_permission != VETOED`, testando `CONDITIONAL` e `PERMITTED`.
- Nao destrava: extrapolacao a partir da janela bearish ou mudanca de regime puramente narrativa.

### 6.2 Validacao plena de `operable_quality CLEAN`

- Falta: casos com macro_permission permissivo onde setup limpo possa ser observado e classificado.
- Destrava: `macro_permission` sair de `VETOED` + casos com `directional_bias` resolvido + `technical_strength` legivel.
- Nao destrava: declarar CLEAN validado por similaridade com janela bearish.

### 6.3 Calibracao de `SUSTAINED` vs `TRANSIENT`

- Falta: criterio numerico explicito; N a calibrar.
- Destrava: revisao de multiplos casos com duracao variavel, com decisao do operador.
- Nao destrava: escolher N por convencao sem evidencia.

### 6.4 Secao "Casos vivos de validacao" da spec v0.1

- Falta: preencher a secao marcada `_ [a desenvolver] _` dentro da propria spec.
- Destrava: incorporar os mapeamentos deste validation report como referencia interna em uma iteracao v0.2.
- Nao destrava: tratar este validation report como substituto automatico da secao interna sem ato explicito.

### 6.5 Criterios de reabertura da maturation hypothesis

- Falta: definicao prospectiva de janela, metricas e thresholds para reabrir hipotese rejeitada.
- Destrava: decisao do operador definindo criterios antes da observacao.
- Nao destrava: reabertura ad hoc baseada em impressao narrativa.

### 6.6 Promocao RC001-R1

- Falta: 2-3 ocorrencias adicionais alem do episodio INJ D14-D20.
- Destrava: episodios novos documentados + operator review.
- Nao destrava: re-heating D26 que nao consolidou, ou similaridade conceitual sem ocorrencia discreta.

---

## 7. Hipoteses Nao Promovidas

Este documento nao promove:

- RC001-R1: continua risk flag, nao regra oficial.
- Maturation hypothesis: continua rejeitada apenas para a janela D15-D28; reabertura futura possivel com criterios.
- Finding 004+: nenhum criado.
- Rule Candidate 002+: nenhum criado.
- Watchlist: permanece conforme documento canonico `L-13 | EURU_DATA_WATCHLIST_OfficialWatchlist` no `EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md`; este relatorio nao altera escopo.
- Spec v0.1: permanece DRAFT / bearish-derived; nao promovida a STABLE.

Nota: "D28 = 18/18 ativos negativos" e evidencia empirica da janela, nao regra de watchlist.

---

## 8. Validation Summary / Operator Acceptance Required

Este relatorio documenta que a spec v0.1, conforme leitura primaria e mapeamento de casos D15-D28, satisfaz os criterios C1-C4 deste validation report e satisfaz parcialmente C5.

C5 permanece `PARTIAL` porque a secao "Casos vivos de validacao" na propria spec v0.1 esta marcada como `_ [a desenvolver] _`. Este relatorio supre externamente o mapeamento empirico, mas nao altera automaticamente a spec primaria.

Este relatorio recomenda classificar a spec v0.1 como:

`COMPLETE_AS_BEARISH_DERIVED_ARTIFACT`

no momento de aceitacao pelo operador, com a matriz consolidada:

- 4 estados/sub-estados em `VALIDATED_IN_BEARISH`
- 7 estados/sub-estados em `PARTIALLY_VALIDATED`
- 4 estados/sub-estados em `ARCHITECTURALLY_NECESSARY_EMPIRICALLY_PENDING`
- 1 estado/sub-estado em `PENDING_BULL_REGIME`

A decisao de aceitar esta classificacao cabe ao operador. Este documento nao se auto-promove a fonte canonica de classificacao. A aceitacao do operador e o ato que torna a classificacao operativa.

Bull regime validation permanece pending. Esta classificacao nao autoriza execucao, implementacao, rule promotion ou alteracao de Core.

---

## 9. Estado Pos-Validacao

Independentemente da decisao final do operador:

- READ_ONLY permanece intacto.
- EXCLUDE list permanece intacta.
- Spec v0.1 permanece DRAFT / bearish-derived ate ato explicito do operador.
- Observacao diaria leve continua como input de validacao.
- Proximas frentes permanecem alinhadas ao handoff mestre secao 19.
- Nenhuma task Disabled e reativada.
- Nenhum sinal se torna acionavel.

---

## 10. Operator Acceptance Block

```yaml
acceptance_status: pending
acceptance_date:
acceptance_decision_record:
operator_signature: Andre Marcal
```

Este bloco deve permanecer `pending` ate revisao explicita do operador.

---

## 11. Fecho

Este documento existe para validar sem surpreender: separar o que a spec v0.1 ja resolve, o que a janela bearish permitiu validar, e o que permanece honestamente pendente.

**"Trust is built when there are no surprises."**

Fim.

# EURU OS — Design Spec 3-D/4-D
## Score Decomposition Architecture — v0.1 (bearish-derived)

---

## 0. Metadados e governança

- **Versão:** v0.1
- **Estado:** DRAFT / bearish-derived
- **validated_in_bearish:** true
- **bull_regime_validation:** pending
- **Origem:** Decisão gate T+28D (Andre Marcal, 2026-05-28), Opcao A hibrida controlada
- **Natureza:** documento de design e criterios de leitura. NAO-EXECUTAVEL.
- **NAO inclui:** implementacao, automacao, backtest executavel, sinal acionavel, alteracao de Core.
- **Modo:** READ_ONLY mantido. EXCLUDE list ativa.
- **Base empirica:** janela Fase 2 Design D15-D28, Finding 002b FINAL.

---

## 1. Problema (o que esta spec resolve)

Finding 002b (FINAL): o Core score e direction-agnostic sob movimento bearish — mistura quatro dimensoes num so numero (technical_strength, directional_bias, macro_permission, operable_quality). Caso-ancora: BTC SETUP D28 (PREMIUM 31/35 em -3.17%, RSI 34.68 oversold, macro-vetoed). Esta spec separa o score unico em 4 dimensoes legiveis independentemente.

---

## 2. Principio de separacao (nao-redundancia)

As 4 dimensoes respondem a 4 perguntas distintas:

- **macro_permission** — "o mercado deixa jogar?" (regime BTC/Master Filter)
- **directional_bias** — "para onde esta inclinado?" (trend/MACD/estrutura)
- **technical_strength_score** — "quao forte/estendido/comprimido esta, tecnicamente?" (sem direcao)
- **operable_quality** — "este setup especifico e limpo o suficiente?" (qualidade local, dado o resto)

Regra de nao-sobreposicao: macro_permission e permissao de REGIME (universal ao universo observado); operable_quality e limpeza LOCAL (por ativo, condicional as outras tres).

---

## 3. As 4 dimensoes

> Criterio de spec completa v0.x: cada dimensao tem os 4 elementos (a) definicao, (b) inputs/sinais, (c) regra de leitura, (d) tag de validade por regime.

### 3.1 macro_permission

- (a) Definicao: Estado de permissao do regime macro para considerar setups no universo observado. Responde se BTC (ancora do regime, via Master Filter) permite ou veta a leitura de setups, independentemente da forca ou direcao de qualquer ativo individual. Dimensao de REGIME, nao de ativo: mesmo valor para os 18 ativos num dado dia. Nao mede direcao (directional_bias) nem qualidade local (operable_quality); mede apenas o estado do portao macro.

- (b) Inputs/sinais:
  - Morning Master Filter (BTC trend 1D): estado primario/dominante. ACTIVE quando BTC 1D BEARISH ou SIDEWAYS.
  - Asian Master Filter (BTC 4H state): secundario/tatico. Estados: GEM_ALERT, WATCHLIST, NO_TRADE.
  - Precedencia (assimetrica): Morning 1D domina. O 4H pode REBAIXAR um estado permissivo (PERMITTED -> CONDITIONAL), mas NUNCA promover um regime bloqueado (VETOED -> PERMITTED). O 4H modula para baixo, nunca para cima.

- (c) Regra de leitura (3 estados):
  - VETOED: Morning ACTIVE (BTC 1D BEARISH/SIDEWAYS). Regime nao permite jogar. [empiricamente validado - dominante D14-D28, 22 dias.]
  - CONDITIONAL: Morning INACTIVE, mas Asian 4H mostra compressao, indecisao ou estado tatico nao-confirmado; ou divergencia entre horizontes. Permissao parcial/incerta. [slot arquitetural; regra preliminar; calibracao pendente - nao observado D15-D28.]
  - PERMITTED: Morning INACTIVE e Asian permissivo. Portao aberto. [slot arquitetural; regra preliminar; validacao pendente - nunca observado D15-D28.]
  - Mapa de leitura:
    - Morning ACTIVE -> VETOED (4H irrelevante para promocao)
    - Morning INACTIVE + Asian incerto/comprimido -> CONDITIONAL
    - Morning INACTIVE + Asian permissivo -> PERMITTED
  - Nota arquitetural: CONDITIONAL e PERMITTED sao estados definidos por logica de design, NAO por validacao empirica na janela D15-D28. A janela foi 100% VETOED; estes slots completam a arquitetura mas aguardam dados nao-bearish para calibracao.
  - Caso-ancora (VETOED): BTC SETUP D28 - technical_strength produziu PREMIUM SETUP (31/35) mas macro_permission = VETOED (Morning ACTIVE, BTC 1D BEARISH). A separacao torna legivel o que o score unico escondia: "forca tecnica maxima sob portao macro fechado".

- (d) Tag de validade por regime:
  - validated_in_bearish: true - apenas o estado VETOED (22 dias ACTIVE, sell-off D28, todos os casos SETUP-em-veto).
  - bull_regime_validation: pending - CONDITIONAL e PERMITTED nunca observados; definidos por logica de design, nao empiricos.
  - SIDEWAYS_as_VETOED: bearish-derived - tratar SIDEWAYS como bloqueio (igual a BEARISH) foi como o sistema operou e a janela validou, MAS pode ser artefacto do regime bearish; pending neutral/bull validation (num regime neutro, SIDEWAYS pode nao dever bloquear tao fortemente como BEARISH).
  - Limiar pendente: fronteira CONDITIONAL<->PERMITTED precisa de casos nao-bearish para calibracao.

### 3.2 directional_bias

- (a) Definicao: _[a preencher]_
- (b) Inputs/sinais: _[a preencher]_
- (c) Regra de leitura: _[a preencher]_
- (d) Validade por regime: _[a preencher]_

### 3.3 technical_strength_score

- (a) Definicao: _[a preencher]_
- (b) Inputs/sinais: _[a preencher]_
- (c) Regra de leitura: _[a preencher]_
- (d) Validade por regime: _[a preencher]_

### 3.4 operable_quality

- (a) Definicao: _[a preencher]_
- (b) Inputs/sinais: _[a preencher]_
- (c) Regra de leitura: _[a preencher]_
- (d) Validade por regime: _[a preencher]_

---

## 4. Casos vivos de validacao (D15-D28)

> Mapear casos da janela a cada dimensao, mostrando que a separacao os torna legiveis.

- BTC SETUP D28 -> macro_permission veta technical_strength alto _[a desenvolver]_
- FET sustained-then-broke D24-D28 -> directional_bias com duracao _[a desenvolver]_
- INJ re-heating D26 -> technical_strength != operable_quality _[a desenvolver]_
- OBV/MACD divergence D22/D24 -> technical_strength vs directional_bias _[a desenvolver]_

---

## 5. Limitacoes e validade por regime

- Spec bearish-derived: todos os limiares/leituras derivam de regime BEARISH (22 dias ACTIVE).
- Campos marcados bull_regime_validation=pending onde aplicavel.
- v0.x NAO especifica execucao, pesos de agregacao acionaveis, nem reconstituicao do score unico.

---

## 6. Carry-forward / proximas versoes

- v0.2: validacao bull-regime quando surgirem casos vivos nao-bearish.
- Criterio de promocao bearish-derived -> validated.
- Fora de escopo v0.x: agregacao executavel, implementacao.

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

- (a) Definicao: Inclinacao direcional de um ativo, com base em trend, MACD e estrutura de preco. Responde "para onde aponta?". Dimensao de ATIVO (cada ativo tem o seu), ao contrario de macro_permission (de regime). Nao mede forca (technical_strength) nem permissao (macro_permission) nem limpeza local (operable_quality).
  - TRAVA ANTI-GATE: directional_bias NUNCA concede permissao operacional. Apenas descreve inclinacao direcional. Permissao pertence EXCLUSIVAMENTE a macro_permission. Um bias BULLISH nao "abre" nada se macro_permission estiver VETOED.

- (b) Inputs/sinais (hierarquia):
  - Direcao primaria: MACD state (BULLISH/BEARISH) + Trend (BEARISH/SIDEWAYS/BULLISH). Sao o motor da direcao.
  - Confirmacao/divergencia: OBV direction (RISING/FLAT/FALLING). NAO e motor primario; confirma ou diverge da direcao primaria. Pode converter uma leitura BULLISH/BEARISH em MIXED quando diverge materialmente.
  - Duracao: ha quantos dias o bias se mantem (alimenta o confidence qualifier).

- (c) Regra de leitura - direcao (3 estados) + confidence qualifier:
  - Direcao primaria (MACD + trend):
    - BULLISH: MACD BULLISH + trend nao-bearish.
    - BEARISH: MACD BEARISH + trend bearish. [dominante na janela, 13-17/18.]
    - MIXED / unresolved directional bias: conflito entre direcao primaria e confirmacao (ex.: MACD BULLISH mas OBV FALLING; ou trend SIDEWAYS com MACD/OBV em desacordo). NAO e uma "terceira direcao positiva"; e direcao nao-resolvida - a leitura direcional esta genuinamente ambigua, nao apenas fraca.
  - Confidence qualifier (descritivo, NAO threshold operacional):
    - SUSTAINED: persistencia multi-dia observada. Significa "persistiu ate agora", NAO "deve continuar". [limiar N pending calibration.]
    - TRANSIENT: leitura curta/recente, pode desinflar. [limiar pending.]
  - Leitura combinada: ex. "BULLISH/SUSTAINED" (FET D24-D27), "BULLISH/TRANSIENT" (INJ bounce D26 que arrefeceu).
  - Casos-ancora:
    - FET D24-D28: BULLISH/SUSTAINED 4 dias (MACD BULLISH mantido), mas quebrou D28 (-9.10%). SUSTAINED capturou a persistencia ate ao momento; a quebra confirma que SUSTAINED e descricao, nao previsao.
    - OBV/MACD divergence D22, D24: MACD sem confirmacao OBV -> MIXED (direcao nao-resolvida). O caso onde a hierarquia (OBV como confirmacao, nao motor) torna a ambiguidade legivel.

- (d) Tag de validade por regime:
  - validated_in_bearish: true - BEARISH extensivamente validado (13-17/18 MACD BEARISH, dominante toda a janela).
  - bull_regime_validation: pending - BULLISH/SUSTAINED so observado em bolsoes isolados (FET, WLD, NEAR, RENDER), nunca como regime. BULLISH generalizado nunca visto.
  - MIXED: parcialmente validado (divergencias OBV/MACD D22/D24 observadas); catalogo de configuracoes MIXED incompleto sem regime variado.
  - Limiar SUSTAINED<->TRANSIENT (N dias): pending calibracao. A janela sugere 1-2 dias = transient, 4 dias = sustained-mas-fragil (FET quebrou ao 5º), mas N nao esta fixado.

### 3.3 technical_strength_score

- (a) Definicao: Magnitude da condicao tecnica de um ativo - forca, extensao, compressao - independentemente de direcao, permissao de regime ou qualidade de entrada. Responde "quao carregada esta a mola?", nao "para onde aponta?" (directional_bias), nao "o mercado deixa jogar?" (macro_permission), nao "setup limpo?" (operable_quality). E a dimensao que mais corresponde ao score numerico original do Core (0-35) - e por isso onde o Finding 002b se manifesta.
  - TRAVA DE HERANCA: reutiliza o score original como INPUT PRINCIPAL, mas NAO herda o seu significado operacional. O score entra como materia-prima, nao como autoridade.
  - PRINCIPIO: direction-agnostic e operability-agnostic por design. Score alto = condicao tecnica carregada, NAO oportunidade.

- (b) Inputs/sinais:
  - Core score (0-35): input central, marcado como legacy composite proxy for technical load, pending decomposition. Em v0.1 usado inteiro (sem subcomponentes formais ainda); em versao futura deve ser decomposto, nao usado como bloco opaco. Entra com caveat explicito para nao re-importar contaminacao.
  - Tier (MEDIA/BOA/PREMIUM): banda qualitativa.
  - RSI (nivel e extremos): RSI>70/75 sobre-extensao; RSI<30 sobre-venda.
  - Compressao/extensao (Aguiar Module 05): estado de mola.

- (c) Regra de leitura - magnitude + load_type:
  - Banda de magnitude: tier (MEDIA/BOA/PREMIUM) + score (0-35) = nivel de carga.
  - load_type:
    - EXTENDED_UP: esticado para cima, energia gasta a subir (sobre-extensao de alta; ex. INJ D14 RSI 84.86). Liga RC001-R1 quando RSI>75.
    - EXTENDED_DOWN: esticado para baixo, energia gasta a cair / oversold (ex. BTC D28 RSI 34.68).
    - COMPRESSED: compressao/lateralizacao, energia acumulada (GEM_ALERT 4H, mola carregada).
    - NEUTRAL: sem extremo nem compressao saliente.
  - LEITURA CRITICA (Finding 002b): technical_strength alto NAO implica operavel. O score pode subir enquanto o preco cai - mede carga, nao direcao nem permissao. FORCA != OPERAVEL.
  - FRONTEIRA load_type vs directional_bias: EXTENDED_DOWN nao significa BEARISH. BEARISH pertence a directional_bias e descreve inclinacao direcional. EXTENDED_DOWN pertence a technical_strength e descreve tipo de carga tecnica: condicao esticada/oversold apos movimento para baixo. Um ativo pode ser BEARISH sem estar EXTENDED_DOWN, e pode estar EXTENDED_DOWN enquanto a direcao comeca a neutralizar ou reverter.
  - Caso-ancora: BTC D28 - technical_strength PREMIUM (31/35) / EXTENDED_DOWN (RSI 34.68 oversold), pior dia de preco (-3.17%). No score unico aparecia como "SETUP forte" (enganador). Decomposto: directional_bias BEARISH + technical_strength PREMIUM/EXTENDED_DOWN + macro_permission VETOED. A coincidencia BEARISH/EXTENDED_DOWN no mesmo dia nao e redundancia - sao duas dimensoes independentes a apontar leituras compativeis: direcao para baixo + carga esticada para baixo.

- (d) Tag de validade por regime:
  - validated_in_bearish: true (paradoxo "score alto em queda" validado: D18/D23/D28, >=10 estados Finding 002b).
  - bull_regime_validation: pending (janela viu technical_strength alto sobretudo DURANTE quedas; comportamento bullish - score alto com preco a subir - sub-observado; em PERMITTED score alto pode significar oportunidade, nunca testado).
  - load_type: EXTENDED_UP validado (INJ>80 D14); EXTENDED_DOWN validado (BTC<35 D28); COMPRESSED parcial (GEM_ALERT recorrente); NEUTRAL implicito; fronteiras pending.
  - Ligacao RC001-R1 (cross-reference, nao duplicacao): technical_strength identifica condicoes extremas; RC001-R1 interpreta um subconjunto (EXTENDED_UP com RSI>75) como risk flag contextual. RC001-R1 NAO pertence a technical_strength; consome o seu padrao extremo.

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

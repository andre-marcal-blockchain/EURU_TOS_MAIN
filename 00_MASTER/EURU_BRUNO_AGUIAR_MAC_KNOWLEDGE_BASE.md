# EURU_BRUNO_AGUIAR_MAC_KNOWLEDGE_BASE.md

**Sistema:** Euru OS  
**Escopo:** Knowledge base operacional sobre Metodo Aguia Cripto (MAC), leitura de mercado no estilo Bruno Aguiar e traducao dessa metodologia para os agentes Euru OS.  
**Status:** KNOWLEDGE_BASE / REFERENCE  
**Uso:** Documento de transferencia de conhecimento para humanos, Codex, Claude e futuras IAs externas que trabalhem no Euru OS.  
**Nota de governanca:** Este documento nao autoriza execucao real, abertura de posicoes, uso de futures, hedge, alavancagem ou alteracao de risco. Qualquer transicao para SIMULATE ou EXECUTE exige governanca propria, validacao tecnica, cooling-off quando aplicavel e aprovacao humana explicita.

---

## 1. QUEM E BRUNO AGUIAR

Bruno Aguiar e a referencia metodologica usada pelo operador Andre para orientar a forma como o Euru OS deve ler o mercado cripto. A ideia nao e copiar decisoes pessoais de Bruno, mas transformar a sua forma de analise em regras, filtros, agentes, checklists e criterios auditaveis.

O nucleo do metodo e conhecido como **Metodo Aguia Cripto (MAC)**. Ele combina leitura top-down do mercado, analise tecnica, fluxo de volume, contexto macro, gestao de risco e disciplina operacional. A intencao e encontrar oportunidades assimetricas em criptoativos, especialmente altcoins, sem depender de uma visao simplista de mercado bullish.

O principio fundamental e:

> BTC define o clima macro; altcoins sao o campo tatico.

Isso significa que o Bitcoin funciona como termometro geral de risco. Ele indica se o ambiente favorece agressividade, paciencia, reducao de exposicao ou foco em operacoes vendidas. Mas as oportunidades taticas podem surgir em altcoins mesmo quando o mercado amplo esta lateral, fraco ou em queda.

Frase operacional que resume a filosofia:

> O mercado compra e vende, lateral, em canal. A volatilidade cria oportunidades.

O metodo nao deve ser interpretado como um sistema apenas de compra. Ele e direcional. A depender da estrutura, uma altcoin pode ser candidata a:

- `LONG / BUY`: quando ha estrutura positiva, acumulacao, rompimento, momentum e relacao risco-retorno favoravel.
- `SHORT / SELL`: quando ha fraqueza, perda de suporte, rejeicao, breakdown, distribuicao ou assimetria para queda.
- `WATCHLIST`: quando ha potencial, mas falta confirmacao.
- `NO_TRADE`: quando a assimetria, a estrutura ou o risco nao justificam acao.

O horizonte temporal preferencial e de **dias a semanas**, com regra forte de **time stop ate 7 dias** para evitar capital preso em posicoes que nao desenvolvem.

A filosofia central e assimetria:

> Antes de entrar, deve haver mais a ganhar do que a perder.

Se a operacao nao tem alvo claro, invalidacao clara, risco controlado e justificativa tecnica, a decisao padrao e `NO_TRADE`.

---

## 2. METODO MAC — MOVIMENTO, ACELERACAO, CONFIRMACAO

O MAC organiza a leitura tecnica em tres pilares: **Movimento**, **Aceleracao** e **Confirmacao**. O objetivo e evitar entradas baseadas em apenas uma pista isolada.

### 2.1 Os 3 Pilares

#### M — Movimento

Movimento responde a pergunta:

> O ativo esta se deslocando na direcao certa dentro de uma estrutura negociavel?

Sinais principais:

- Tendencia alinhada no timeframe relevante.
- Preco acima de regioes de suporte quando o vies e long.
- Preco abaixo de suporte perdido ou rejeitando resistencia quando o vies e short.
- OBV acompanhando a direcao esperada.
- Estrutura nao esta em zona aleatoria ou sem liquidez.

Para longs:

- Tendencia de alta ou recuperacao estrutural.
- OBV rising ou ao menos nao falling.
- Preco rompendo, retestando ou continuando estrutura positiva.

Para shorts:

- Tendencia de baixa, perda de suporte ou rejeicao relevante.
- OBV falling ou divergindo negativamente.
- Preco falhando em recuperar regioes-chave.

#### A — Aceleracao

Aceleracao responde a pergunta:

> O movimento tem momentum suficiente para continuar?

Para longs:

- RSI > 50.
- RSI preferencialmente entre 50 e 65, pois ha momentum com espaco para continuar.
- MACD bullish.
- Preco ganhando velocidade sem estar excessivamente esticado.

Para shorts:

- RSI < 50 ou rejeitando zonas superiores.
- MACD bearish.
- Perda de momentum comprador.
- Repique fraco contra resistencia.

#### C — Confirmacao

Confirmacao responde a pergunta:

> O volume confirma a tese ou o preco esta andando sem participacao real?

Sinais principais:

- Volume `STRONG` confirmando o movimento.
- OBV nao caindo em setup long.
- OBV nao subindo em setup short.
- Fechamento acima/abaixo do nivel relevante, nao apenas wick ou spike.
- Ausencia de noticia adversa forte.

OBV tem peso especial porque revela acumulacao/distribuicao. No metodo, OBV e considerado um dos indicadores mais honestos: preco pode enganar, volume tende a denunciar a intencao do mercado.

### 2.2 Como validar MAC_VALID

A classificacao MAC deve ser objetiva:

| Estado | Criterio | Decisao |
|---|---|---|
| `MAC_VALID = YES` | Movimento, Aceleracao e Confirmacao alinhados | Pode avancar para risco/playbook |
| `MAC_VALID = PARTIAL` | 2 de 3 pilares alinhados | `REVIEW` ou `WATCHLIST` |
| `MAC_VALID = NO` | 0 ou 1 pilar alinhado | Rejeitar / `NO_TRADE` |

Regra importante:

> 2/3 nao e sinal suficiente para entrada automatica. E sinal de interesse, revisao ou espera.

### 2.3 Os 5 Setups Oficiais

#### 1. Breakout

Ocorre quando o preco rompe uma resistencia relevante com volume e fechamento confirmado.

Criterios desejados:

- Resistencia claramente mapeada.
- Fechamento acima do nivel, nao apenas wick.
- Volume forte ou crescente.
- OBV rising.
- RSI acima de 50.
- Risco-retorno minimo aceitavel.

Risco principal: fakeout.

#### 2. Sweep + Reversal

Ocorre quando o preco faz uma varredura para baixo, captura liquidez, falha em continuar caindo e reverte com forca.

Criterios desejados:

- Wick ou queda abaixo de suporte anterior.
- Recuperacao rapida do nivel perdido.
- Candle de reversao forte.
- OBV nao confirma a queda ou volta a subir.
- Volume relevante na recuperacao.

Risco principal: confundir repique tecnico com reversao real.

#### 3. Reteste

Ocorre quando o preco volta ao nivel rompido para confirmar suporte/resistencia antes de continuar.

Para long:

- Rompeu resistencia.
- Voltou ao nivel.
- Segurou como suporte.
- Mostrou candle de reacao.
- OBV nao desabou no retorno.

Para short:

- Perdeu suporte.
- Voltou ao nivel.
- Rejeitou como resistencia.
- Momentum comprador falhou.

#### 4. Continuacao

Ocorre quando ha pullback saudavel dentro de tendencia ativa.

Criterios desejados:

- Tendencia principal intacta.
- Pullback sem quebra estrutural.
- Volume vendedor fraco no recuo para longs.
- OBV estavel ou rising.
- RSI resfria sem perder zonas-chave.

Risco principal: entrar em pullback que virou reversao.

#### 5. Narrativa + Grafico

Ocorre quando um tema forte encontra estrutura tecnica favoravel.

Narrativas comuns:

- AI.
- L2.
- DePIN.
- Gaming.
- RWA.
- Macro/ETF/liquidez.

A narrativa so importa se o grafico confirma. Hype sem estrutura e risco, nao setup.

### 2.4 Checklist de 12 Pontos (Playbook)

Antes de qualquer operacao, o setup deve passar por um checklist estruturado.

| # | Ponto | Pergunta operacional |
|---|---|---|
| 1 | Narrativa | Existe narrativa ativa e relevante para o ativo/setor? |
| 2 | BTC context | O BTC permite exposicao, exige cautela ou bloqueia? |
| 3 | Majors | ETH e principais majors confirmam ou contradizem o ambiente? |
| 4 | Estrutura | O ativo esta em tendencia, range, canal, compressao ou rompimento? |
| 5 | Rompimento | Houve close confirmado acima/abaixo do nivel relevante? |
| 6 | Volume | O volume confirma ou enfraquece o movimento? |
| 7 | Liquidez | Spread, profundidade e volatilidade permitem operar com seguranca? |
| 8 | Invalidacao | O ponto de invalidacao esta claro antes da entrada? |
| 9 | Risco | O risco por trade respeita os limites do sistema? |
| 10 | Alvo | Existem alvos tecnicos claros e realistas? |
| 11 | R/R | A relacao risco-retorno justifica a operacao? |
| 12 | Plano, nao emocao | A entrada segue plano objetivo ou impulso? |

Regra: se nao ha plano antes da entrada, nao ha operacao.

---

## 3. PROTOCOLO AGUIAR — 10 MODULOS

### Modulo 01 — BTC Master Filter

O Bitcoin define o clima macro. O BTC Master Filter nao serve para impedir todas as operacoes, mas para ajustar lado, agressividade e permissao.

| Estado BTC | Interpretacao | Decisao para altcoins |
|---|---|---|
| `BTC_BULLISH` | Ambiente favoravel a risco | Altcoins liberadas, desde que tenham setup proprio |
| `BTC_SIDEWAYS` | Mercado indefinido/lateral | Downgrade de `SETUP` para `WATCHLIST`, salvo excecoes fortes |
| `BTC_BEARISH` | Ambiente adverso a longs | Apenas shorts, hedges ou `NO_TRADE` |

Principio:

> BTC e o clima; altcoin e a oportunidade tática.

### Modulo 02 — 5/5/90 Capital Structure

Estrutura de capital conservadora:

- 5% em BTC/ETH como reserva estrategica.
- 5% em operacoes ativas, onde existe risco tatico.
- 90% em stablecoins como reserva tática e protecao.

Dentro dos 5% ativos:

| Categoria | Alocacao interna | Caracteristica |
|---|---:|---|
| Core | 50% | Ativos mais fortes/liquidos |
| Growth | 25% | Crescimento com narrativa e estrutura |
| Asymmetric | 15% | Maior assimetria, maior risco |
| Speculative | 10% | Alto risco, tamanho reduzido |

Esse modulo protege o operador de transformar uma tese em concentracao excessiva.

### Modulo 03 — Dynamic Risk Scaling

Limites de risco:

- Maximo de 1% por trade.
- Maximo de 2% por dia.
- Maximo de 5% por semana.

Formula base:

```text
Position Size = Capital x 1% / (ATR x 1.5)
```

O ATR define volatilidade e distancia de stop. Quanto maior a volatilidade, menor deve ser o tamanho da posicao.

### Modulo 04 — Overnight Daemon

A sessao asiatica e usada como filtro de qualidade.

Funcoes:

- Observar lateralizacao.
- Detectar acumulacao silenciosa.
- Identificar compressao.
- Medir exaustao de volume.
- Gerar `GEM_ALERT` quando compressao e volume exhaustion aparecem juntos.

A sessao asiatica nao e apenas ruido; ela pode revelar preparacao antes do movimento europeu/americano.

### Modulo 05 — Lateralization Patience

Nao entrar durante lateralizacao ativa.

Regra:

> Esperar a compressao resolver.

Resolucao pode ocorrer por:

- Breakout.
- Breakdown.
- Sweep + reversal.
- Rejeicao clara.

O Asian Scan deve detectar automaticamente esse estado por volta de 00:00 UTC.

### Modulo 06 — Volume Matrix

Volume confirma ou invalida a leitura do preco.

| Estado | Interpretacao |
|---|---|
| `Volume STRONG` | Confirma o movimento |
| `Volume WEAK` | Sinal de fraqueza mesmo com preco subindo |
| `OBV RISING` | Acumulacao / pressao compradora |
| `OBV FALLING` | Distribuicao / pressao vendedora |
| `OBV FLAT` | Confirmacao insuficiente |

OBV e indicador primario de acumulacao/distribuicao.

### Modulo 07 — 3X Recovery Protocol

O 3X Recovery Protocol nao e uma entrada normal. E uma cirurgia de emergencia para posicao perdedora em futures.

Quando usar:

- Posicao muito negativa, como -400% a -1000% em futures.
- Tese original ainda nao completamente invalidada.
- Existem sinais tecnicos de reacao.
- Ha margem suficiente.
- Existe plano de desmontagem.
- Ha aprovacao humana explicita.

Como fazer:

1. Esperar sinais de reacao, como candles positivos.
2. Aumentar a posicao em 3X para melhorar preco medio.
3. Abrir short de 90% simultaneamente como protecao.
4. Usar saida com intencao `REDUCE` / `CLOSE` e protecao operacional.
5. Objetivo: sair no zero ou com lucro pequeno.

Binance Hedge Mode e obrigatorio para manter long e short simultaneos.

Reduce Only e conceito essencial para evitar erro operacional na saida. No entanto, em Hedge Mode a API da Binance pode ter restricoes especificas sobre `reduceOnly`; por isso o Euru deve tratar isso como regra operacional revisada por humano e nunca como automacao cega.

As 4 pecas do protocolo:

- Price averaging.
- Hedge.
- Reduce-only exit / saida sem aumento acidental de exposicao.
- Hard stop.

### Modulo 08 — 50% Securing

Quando o ROI atinge 50% do risco planejado, tirar 50% da posicao.

Objetivo:

- Proteger lucro parcial.
- Reduzir pressao emocional.
- Deixar a outra metade correr.
- Ativar trailing stop no restante.

### Modulo 09 — Fibonacci Exits

Niveis de Fibonacci usados como zonas de parcial:

| Nivel | Uso |
|---|---|
| Fib 0.382 | Primeira resistencia parcial |
| Fib 0.500 | Segundo parcial |
| Fib 0.618 | Terceiro parcial / confluencia com T1 |

Regras de alvo:

- T1 = minimo 1:2 R/R.
- T2 = preferido 1:3 R/R.

### Modulo 10 — 10% Harvesting

Apos atingir targets, retirar 10% do lucro para stablecoins.

Principio:

> Nunca reinvestir tudo.

Objetivo:

- Proteger curva de capital.
- Evitar devolucao integral de ganhos.
- Criar reserva tática.

---

## 4. COMO BRUNO ANALISA ALTCOINS

### 4.1 Top-Down Analysis

Sequencia top-down:

1. BTC no diario para clima macro.
2. ETH e majors para confirmacao do mercado amplo.
3. Altcoin no 4H para timing de entrada.

O BTC responde se o ambiente permite risco. A altcoin responde se existe oportunidade. O 4H responde quando agir.

### 4.2 O que ele olha no BTC

Indicadores e ferramentas:

- SMA: tendencia estrutural.
- SuperTrend: direcao do mercado.
- Fibonacci: niveis de suporte e resistencia.
- RSI: momentum.
- Volume: forca do movimento.

BTC pode liberar, reduzir ou bloquear o apetite por risco, mas nao substitui a analise especifica da altcoin.

### 4.3 Selecao de Altcoins

Filtros principais:

- Liquidez: spread baixo, volume suficiente, profundidade aceitavel.
- Narrativa ativa: AI, L2, DePIN, Gaming, RWA ou outra narrativa relevante.
- Alinhamento com BTC.
- Tecnico: OBV RISING, MACD BULLISH, RSI > 50 para longs.
- Tecnico inverso para shorts: OBV FALLING, MACD BEARISH, perda de suporte ou rejeicao.

### 4.4 Timeframes

| Funcao | Timeframe |
|---|---|
| Analise macro | 1D |
| Timing de entrada | 4H |
| Gestao da posicao | Fechamentos 4H |
| Time stop | Ate 7 dias |

### 4.5 Como identifica oportunidades

Sinais de oportunidade:

- Ativos que sobem enquanto o mercado cai: forca relativa.
- Desvio positivo vs media de 7 dias, por exemplo `dev > +5%`.
- OBV RISING por 2 ou mais sessoes consecutivas.
- Score >= 24/35 no sistema Euru.
- Compressao com volume exhaustion.
- Breakout com fechamento confirmado.
- Breakdown para short quando BTC e estrutura favorecem queda.

---

## 5. COMO ENTRA

### 5.1 Criterios de Entrada Obrigatorios

Para entrada long:

- Score >= 22/35 como minimo.
- Score >= 25/35 como preferido.
- RSI entre 50 e 65.
- MACD BULLISH.
- OBV RISING, idealmente por 2 dias consecutivos.
- Nao entrar em resistencia sem fechamento confirmado acima.
- News Sentinel diferente de `HIGH` com novo catalisador adverso.
- BTC filter nao bloqueando.

Para entrada short:

- Score/estrutura especifica de short deve indicar assimetria para queda.
- RSI abaixo de 50 ou rejeitando zona superior.
- MACD BEARISH.
- OBV FALLING ou divergencia negativa.
- Perda de suporte com fechamento confirmado.
- BTC bearish ou contexto de fraqueza suficiente.
- Risco de short/futures validado manualmente.

### 5.2 Two-Day OBV Protocol

Regra para longs:

- Dia 1: identificar OBV RISING. Nao entrar ainda.
- Dia 2: confirmar OBV RISING novamente. Entrada pode ser considerada.

Razao:

> O protocolo elimina spikes de um dia e confirma acumulacao real.

Para shorts, o equivalente pode ser usado como protocolo de distribuicao:

- Dia 1: identificar OBV FALLING.
- Dia 2: confirmar OBV FALLING novamente.
- Entrada short so pode ser considerada com estrutura e risco alinhados.

### 5.3 Position Sizing

Formula:

```text
Position Size = Capital x 1% / (ATR x 1.5)
```

Regras:

- Nunca mais de 1% de risco por posicao.
- Stop definido antes de entrar.
- Tamanho reduzido em alta volatilidade.
- Alavancagem nao aumenta tolerancia de risco; apenas aumenta perigo operacional.

### 5.4 Tipos de Entrada

| Tipo | Uso |
|---|---|
| Market order | Setup claro, momentum ativo, risco de perder entrada |
| Limit order | Resistencia proxima, busca de preco melhor, controle de slippage |
| Retest entry | Esperar preco voltar ao nivel rompido e confirmar suporte/resistencia |

A escolha da entrada deve respeitar liquidez, volatilidade, spread e invalidacao.

---

## 6. COMO SAI

### 6.1 Hierarquia de Saida (por prioridade)

1. Stop-loss absoluto: ATR x 1.5 abaixo da entrada para longs, acima da entrada para shorts.
2. Reversao macro adversa: BTC perde suporte chave ou recupera nivel contra short.
3. Divergencia OBV + RSI: volume nao confirma preco.
4. MACD crossover contrario.
5. Suporte perdido no fechamento diario para long, resistencia recuperada para short.
6. Time stop: 7 dias sem desenvolvimento exige fechamento.

### 6.2 Saidas Parciais

- Fib 0.618: primeiro parcial de 50% da posicao quando aplicavel.
- T1 em 1:2 R/R: segundo parcial.
- T2 em 1:3 R/R: fechar restante ou trailing agressivo.
- Apos +1R: mover stop para break-even quando o contexto permitir.

### 6.3 Saidas de Emergencia

- OBV vira FALLING em qualquer fechamento diario de posicao long: reavaliar.
- OBV vira RISING contra short: reavaliar.
- RSI sustentado acima de 75 com preco estagnado: reduzir 50% em longs.
- Nova noticia adversa especifica ao ativo: exit imediato ou reducao emergencial.
- Liquidez seca ou spread explode: reduzir risco.

### 6.4 Time Stop — Regra Fundamental

Maximo de 7 dias em qualquer posicao.

Se a posicao nao desenvolveu em 7 dias:

- Capital esta preso.
- Oportunidade alternativa esta sendo perdida.
- A permanencia tende a virar emocao, nao plano.

Regra:

> Saida disciplinada antes do time stop e melhor do que esperar por esperanca.

---

## 7. PROTOCOLO 3X — DETALHE COMPLETO

### 7.1 O que e

O Protocolo 3X e uma tecnica de recuperacao de posicao perdedora em futures.

Ele nao e:

- Entrada normal.
- Martingale simples.
- Triplicar porque caiu.
- Estrategia de lucro.
- Automacao permitida por padrao.

Ele e:

- Cirurgia de emergencia.
- Estrutura composta de recuperacao.
- Procedimento de alto risco.
- Acao que exige aprovacao humana.

### 7.2 Quando ativar

Todos estes criterios devem ser verdadeiros:

1. Posicao original ainda nao invalidada na tese.
2. Sinais tecnicos de reacao, como candles positivos no 4H.
3. Conta tem margem suficiente.
4. Existe plano claro de desmontagem por pernas.
5. Ha aprovacao humana explicita.
6. Ha consciencia de risco de liquidacao, funding e execucao.
7. O objetivo e sobrevivencia, nao ganho agressivo.

### 7.3 Como executar

Passo 1: Posicao original long muito negativa.  
Passo 2: Detectar reacao tecnica, como 2 ou mais candles positivos no 4H.  
Passo 3: Aumentar posicao em 3X para melhorar preco medio.  
Passo 4: Abrir short de 90% como contencao/protecao.  
Passo 5: Usar intencao de ordem `REDUCE` / `CLOSE` para evitar nova exposicao acidental.  
Passo 6: Objetivo: break-even ou lucro pequeno.  
Passo 7: Desmontar por pernas, sem improviso.

### 7.4 Binance Hedge Mode

Hedge Mode permite manter long e short simultaneos.

Conceitos:

- `positionSide = LONG` ou `SHORT`, nao `BOTH`.
- A intencao semantica da ordem precisa estar clara.
- Reduce Only previne aumento acidental de exposicao, mas a API pode ter restricoes especificas em Hedge Mode.
- O Euru deve validar regras atuais da Binance antes de qualquer implementacao.

### 7.5 Regras Absolutas do 3X

1. Nunca como primeira entrada.
2. Nunca sem sinal tecnico de reacao.
3. Nunca sem margem suficiente.
4. Nunca para salvar ego.
5. Nunca sem aprovacao humana.
6. Sempre com hedge ratio calculado.
7. Sempre com plano de saida por pernas.
8. Sempre tratado como excecao governada.
9. Nunca automatico em fase READ_ONLY ou SIMULATE sem regra explicita aprovada.

### 7.6 Position Intent Model

Cada ordem deve ter intencao semantica:

| Intent | Significado |
|---|---|
| `OPEN` | Abrir nova tese |
| `ADD` | Reforcar tese valida |
| `HEDGE` | Contencao de risco |
| `REDUCE` | Diminuir exposicao |
| `CLOSE` | Fechar totalmente |
| `RECOVERY_3X` | Cirurgia de emergencia |
| `UNWIND` | Desmontar estrutura composta |

Sem intent claro, nenhuma ordem deve existir.

---

## 8. COMO OS AGENTES EURU REPLICAM OS OLHOS DO BRUNO AGUIAR

O Euru OS foi desenhado para transformar a leitura de Bruno em pipeline de agentes. Cada agente representa uma parte do raciocinio que um operador experiente faria antes de entrar, evitar, revisar ou sair de uma operacao.

### 8.1 Scout (01) — Os olhos macro do Bruno

Replica como Bruno olha primeiro para o contexto estrutural e para o BTC.

Responsabilidades:

- Identificar tendencia: `BULLISH`, `SIDEWAYS`, `BEARISH`.
- Aplicar BTC Master Filter.
- Classificar ativos como `NO_TRADE`, `WATCHLIST` ou `SETUP`.
- Detectar estrutura acima/abaixo da media de 7 dias.
- Separar altcoins com forca relativa das que apenas acompanham ruido.

Interpretacao:

- Se BTC esta bullish, Scout pode liberar setups long.
- Se BTC esta sideways, Scout deve preferir watchlist e esperar confirmacao.
- Se BTC esta bearish, Scout deve bloquear longs fracos e permitir apenas shorts ou zero trade quando governado.

### 8.2 Flow Analyst (02) — O analista tecnico do Bruno

Replica o uso de indicadores para confirmar se a estrutura tem fluxo real.

Responsabilidades:

- RSI 14: momentum.
- MACD 12/26/9: direcao e aceleracao.
- OBV: acumulacao/distribuicao.
- ATR 14: volatilidade, stop e position sizing.

Estados:

- `CONFIRMS`: indicadores confirmam Scout.
- `CONTRADICTS`: indicadores contradizem Scout.
- `INCONCLUSIVE`: dados mistos ou insuficientes.

### 8.3 News Sentinel (03) — O filtro de contexto do Bruno

Replica a leitura de narrativas, noticias e risco externo.

Responsabilidades:

- Classificar severidade: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.
- Monitorar narrativas: AI, L2, DePIN, Gaming, RWA, Macro.
- Bloquear entradas quando ha noticia `HIGH` com catalisador adverso novo.
- Permitir que narrativa positiva conte apenas quando grafico confirma.

### 8.4 Quant/Risk Officer (04) — A disciplina de risco do Bruno

Replica o calculo de risco, sizing e stop antes da decisao.

Responsabilidades:

- Aplicar formula ATR-based.
- Verificar limite de 1% por trade.
- Verificar limite diario de 2%.
- Verificar limite semanal de 5%.
- Classificar como `APPROVE`, `REJECT` ou `REVIEW`.

Regra:

> Score alto nao justifica risco excessivo.

### 8.5 MAC/Playbook Analyst (09) — O analista MAC do Bruno

Replica a validacao metodologica.

Responsabilidades:

- Validar os 3 pilares MAC.
- Aplicar checklist de 12 pontos.
- Classificar setup entre os 5 oficiais.
- Produzir `PLAYBOOK_OK`, `PLAYBOOK_REJECT` ou `REVIEW`.

Regra:

> 2/3 pilares MAC e `PARTIAL`, nao entrada automatica.

### 8.6 Score Engine (08) — O ranking do Bruno

Replica a priorizacao entre multiplas oportunidades.

Responsabilidades:

- Pontuar ativos em 7 criterios.
- Produzir score 0-35.
- Gerar leaderboard diario.
- Separar setups ideais de setups apenas interessantes.

Referencias:

- Minimo: >= 22/35.
- Preferido: >= 25/35.
- Forte: >= 24/35 com OBV rising e MAC valid.

### 8.7 Execution Orchestrator (05) — A decisao final do Bruno

Replica o momento final de decisao.

Responsabilidades:

- Consolidar todos os agentes.
- Resolver conflitos.
- Aplicar hierarquia de veto.
- Produzir `EXECUTION_ALLOWED`, `EXECUTION_BLOCKED` ou `MANUAL_REVIEW_REQUIRED`.

Regra:

> Execution Orchestrator nao existe para forcar trades; existe para impedir trades ruins.

### 8.8 Journal Auditor (07) — A memoria do Bruno

Replica o habito de registrar e aprender.

Responsabilidades:

- Journal diario estruturado.
- Auditoria pos-trade.
- Registro de licoes.
- Time stop tracker.
- Identificacao de violacoes de regra.

Regra:

> O sistema aprende mais com as perdas do que com os ganhos.

### 8.9 Breakout Layer — Os olhos avancados do Bruno

Replica a leitura antecipada de rompimentos, compressao, fakeouts e execucao tatica.

Componentes:

- Alert Radar: recebe sinais externos e normaliza eventos.
- Structure Hunter: mapeia zonas de suporte/resistencia.
- Breakout Confirmation: distingue rompimento real de fakeout.
- Market Regime: classifica ambiente.
- Risk Guardian: protege capital antes de tudo.
- Tactical Execution: constroi plano preciso de trade.
- Compounding Governor: escala apenas quando o sistema merece.
- Journal Learning: registra eventos e resultados.
- Promise Auditor: combate vies, drift e overconfidence.

A Breakout Layer deve funcionar como extensao, nao substituicao, do Core Pipeline.

---

## 9. INDICADORES USADOS PELO METODO

| Indicador | Periodo | Uso |
|---|---:|---|
| RSI | 14 | Momentum; acima de 50 favorece long |
| MACD | 12/26/9 | Direcao e aceleracao da tendencia |
| OBV | N/A | Acumulacao/distribuicao; indicador central |
| ATR | 14 | Volatilidade, stop e sizing |
| SMA | Variavel | Tendencia macro e referencia estrutural |
| SuperTrend | Variavel | Direcao de mercado |
| Fibonacci | N/A | Suporte, resistencia e alvos |
| VPVR | N/A | Volume por nivel de preco |
| Volume MA | 20 | Comparacao de volume atual vs media |

---

## 10. FILOSOFIA E MINDSET

Princípios operacionais:

- Capital preservation e a prioridade absoluta.
- Quando em duvida, o padrao e `NO_TRADE`.
- A paciencia na entrada e vantagem competitiva.
- Nao perseguir hype de curto prazo.
- Pessoas ficam ricas no bear market, nao apenas no bull.
- OBV e o indicador mais honesto; volume nao mente.
- Two-day OBV confirmation elimina spikes falsos.
- Stop-loss e regra, nao sugestao.
- Time stop: capital preso e oportunidade perdida.
- Proactive exit e melhor que reactive exit.
- O 3X nao e para ganhar; e para sobreviver.
- Score alto nao justifica risco excessivo.
- O sistema aprende mais com as perdas do que com os ganhos.
- Uma boa operacao pode ser nao operar.
- Operar menor e sobreviver vale mais do que acertar grande e quebrar.

---

## 11. COMO PASSAR ESTE CONHECIMENTO A OUTRA IA

Instrucoes para qualquer nova IA que receba este documento:

1. Bruno Aguiar analisa top-down: BTC primeiro, depois ETH/majors, depois altcoins.
2. O BTC define o clima macro, mas as altcoins sao o campo tatico.
3. O OBV e o indicador mais importante porque confirma acumulacao ou distribuicao real.
4. Two-day protocol: so considerar entrada long no segundo dia de OBV RISING.
5. Para shorts, procurar distribuicao, perda de suporte, OBV FALLING e contexto bearish.
6. Nunca entrar em resistencia sem fechamento confirmado acima.
7. Nunca entrar short em suporte sem fechamento confirmado abaixo ou rejeicao clara.
8. Time stop de 7 dias e absoluto; nao prorrogar por emocao.
9. 3X e emergencia, nao estrategia; nunca automatico e nunca sem aprovacao humana.
10. MAC precisa dos 3 pilares para `MAC_VALID = YES`.
11. 2/3 pilares MAC e `PARTIAL`, portanto `REVIEW`, nao entrada automatica.
12. BTC filter vem primeiro; se BTC esta sideways, altcoins normalmente viram `WATCHLIST`.
13. News `HIGH` com novo catalisador adverso bloqueia entrada.
14. Score >= 25/35 + OBV RISING + RSI 50-65 + MACD BULLISH e setup long ideal.
15. Score alto sem risco-retorno claro nao autoriza operacao.
16. Todo plano precisa conter entrada, invalidacao, stop, alvo, R/R, time stop e regra de saida.
17. Euru OS deve observar por alguns dias antes de simular entradas.
18. Euru OS deve operar primeiro como analista, depois como simulador, e so depois como executor se a governanca aprovar.
19. Codex e Claude sao IAs externas; nao devem transformar este conhecimento em execucao real sem operador e governanca.
20. O objetivo e replicar os olhos analiticos do Bruno, nao substituir responsabilidade humana.

---

## 12. TRADUCAO OPERACIONAL PARA O EURU OS

Para o Euru OS, este conhecimento deve virar comportamento mensuravel.

### 12.1 Estados esperados por ativo

Cada ativo analisado deve terminar em um destes estados:

| Estado | Significado |
|---|---|
| `LONG_CANDIDATE` | Setup comprador potencial |
| `SHORT_CANDIDATE` | Setup vendedor potencial |
| `WATCHLIST` | Potencial existe, confirmacao insuficiente |
| `NO_TRADE` | Sem assimetria ou risco inadequado |
| `MANUAL_REVIEW` | Condicao complexa exige humano |

### 12.2 Campos minimos de analise por ativo

Cada output de agente ou scan deve buscar, gradualmente, conter:

- Asset.
- Timeframe.
- BTC regime.
- ETH/majors confirmation.
- Structure state.
- MAC state.
- OBV state.
- RSI state.
- MACD state.
- Volume state.
- Narrative state.
- Liquidity/spread note.
- Score 0-35.
- Directional bias: `LONG`, `SHORT`, `NEUTRAL`.
- Setup type.
- Invalidacao.
- Stop model.
- Target model.
- R/R.
- Time stop date.
- Final action.

### 12.3 Regra de fase

Em `READ_ONLY`:

- O Euru observa.
- O Euru classifica.
- O Euru cria reports.
- O Euru nao abre trade.

Em `SIMULATE`:

- O Euru pode criar paper trades.
- O Euru mede assertividade.
- O Euru registra entradas/saidas simuladas.
- O Euru ainda nao envia ordens reais.

Em `EXECUTE`:

- Apenas apos governanca, evidencias e aprovacao humana.
- Futures/short/3X exigem regras adicionais e limites especificos.

### 12.4 Proxima evolucao esperada

Para operar com os olhos do Bruno, os proximos passos tecnicos devem ser:

1. Reativar Morning Scan em READ_ONLY.
2. Reativar Asian Scan em READ_ONLY.
3. Reativar Trade Monitor em READ_ONLY.
4. Adaptar outputs para distinguir `LONG_CANDIDATE` e `SHORT_CANDIDATE`.
5. Adicionar `MAC_VALID` explicito.
6. Adicionar Two-Day OBV Protocol.
7. Adicionar BTC Master Filter mais claro.
8. Adicionar time stop tracker por ativo/paper trade.
9. Rodar por alguns dias sem operar.
10. Auditar se os sinais parecem coerentes com a metodologia.

---

## 13. RESUMO EXECUTIVO

O Euru OS nao deve ser apenas um sistema de compra de altcoins em mercado bullish. Ele deve ser um sistema de leitura direcional de oportunidades em altcoins, inspirado no metodo MAC de Bruno Aguiar, capaz de reconhecer quando comprar, quando vender/short, quando esperar e quando nao operar.

A essencia do metodo e:

```text
BTC define o clima.
Altcoins oferecem o campo tatico.
OBV confirma a intencao.
MAC valida a estrutura.
Risco decide o tamanho.
Playbook impede emocao.
Journal transforma experiencia em aprendizado.
```

A prioridade do Euru agora e ligar novamente os olhos de mercado em READ_ONLY, observar por alguns dias, calibrar os agentes e so depois avancar para simulacao.

Documento: EURU_DATA_WATCHLIST_OfficialWatchlist
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.3
Última atualização: 2026-04-15
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.1.md
Escopo: Watchlist oficial de ativos do Euru OS. Documento vivo actualizado
        semanalmente. Esta versão formaliza o sistema de scoring operacional
        0–35 (7 critérios) como mecanismo canónico de avaliação, incorpora
        a Lista Proibida como secção oficial, e migra os ativos validados
        do snapshot legacy para estado ACTIVE.

---

# EURU — Watchlist Oficial

---

## Changelog

v1.2 — 2026-04-11
- Sistema de scoring 0–35 (7 critérios) adoptado como mecanismo canónico,
  substituindo os 5 critérios binários da v1.1.
- Thresholds de tier actualizados para reflectir o sistema 0–35.
- Lista Proibida incorporada como Secção 7 — status OFFICIAL.
- Ativos herdados do snapshot legacy migrados de PENDING_OPERATOR_REVIEW
  para ACTIVE após validação do operador em 2026-04-11.
- Decisão de adopção do sistema legacy documentada como Opção 2
  aprovada pelo operador.

v1.1 — 2026-04-11
- Validação de estrutura concluída. Ativos marcados PENDING_OPERATOR_REVIEW.

v1.0 — 2026-04-11
- Normalizado de WATCHLIST_OFICIAL.md para formato canônico.

---

## 1. Sistema de scoring canónico (0–35)

Cada ativo é avaliado com base em **7 critérios**, cada um pontuado de **0 a 5**:

| Critério | Descrição |
|---|---|
| **Liquidez** | Profundidade de order book, spread bid/ask, impacto de mercado |
| **Volume** | Volume médio diário (USD), consistência, ausência de wash trading |
| **Estrutura** | Qualidade técnica do setup: suporte/resistência, price action, padrão |
| **Narrativa** | Força do tema/sector: AI, L2, DeFi, RWA — relevância actual de mercado |
| **Forca_Relativa** | Desempenho vs. BTC e vs. sector; liderança ou fraqueza relativa |
| **Exchange** | Listado em Binance Spot/Futures com contrato perpétuo activo e confiável |
| **Potencial** | Assimetria risco/retorno, upside estimado, catalisadores futuros |

---

## 2. Tiers de prioridade

| Tier | Score mínimo | Acção no ciclo diário |
|---|---|---|
| **TIER_1_PREMIUM** | ≥ 28 / 35 | Analisar em todo ciclo diário |
| **TIER_2_MONITOR** | ≥ 20 / 35 | Monitorar semanalmente; promover se score subir |
| **TIER_3_BULL_CYCLE** | ≥ 15 / 35 | Revisão activa prevista a partir de 2027 |
| **LISTA_PROIBIDA** | Score irrelevante | Banidos permanentemente — ver Secção 7 |

---

## 3. Critérios de remoção

- Score abaixo de 15 por 3 ciclos de revisão consecutivos
- Estrutura técnica deteriorada sem sinal de recuperação
- Narrativa invertida ou esgotada
- Liquidez abaixo do mínimo operacional por 3 dias consecutivos
- Qualquer condição de banimento listada na Secção 7

---

## 4. Regras de atualização

- Revisão obrigatória na revisão semanal (Prompt WeeklyReview §17)
- Entradas e saídas registadas no log de movimentações (Secção 8)
- Decisão de inclusão, remoção ou mudança de tier é sempre humana
- Nenhuma IA altera a watchlist sem confirmação do operador
- Alterações nos critérios de score ou movimentação entre tiers requerem aprovação Type 2 (24h)
- Adições à Lista Proibida podem ser feitas imediatamente pelo operador de plantão

---

## 5. TIER_1_PREMIUM

> Ativos activos no scan matinal. Alta liquidez, narrativa forte, estrutura técnica confiável.
> Monitorados diariamente.

| Símbolo | Sector | Observação | Status |
|---|---|---|---|
| BTCUSDT | Store of Value / L1 | Referência principal do mercado | ACTIVE |
| ETHUSDT | Smart Contract / L1 | Referência de altcoins e DeFi | ACTIVE |
| SOLUSDT | L1 / Alta Performance | Liquidez e ecossistema em expansão | ACTIVE |
| BNBUSDT | Exchange Token / L1 | Binance ecosystem, alta liquidez | ACTIVE |
| AVAXUSDT | L1 / Subnet | Institucional, ecossistema activo | ACTIVE |
| DOTUSDT | Interoperabilidade | Parachain ecosystem | ACTIVE |
| LINKUSDT | Oracles / DeFi infra | Líder em oráculos on-chain | ACTIVE |
| ADAUSDT | L1 / Cardano | Liquidez elevada, comunidade forte | ACTIVE |
| XRPUSDT | Pagamentos / Remessa | Alta liquidez, caso legal resolvido | ACTIVE |
| WLDUSDT | AI / Identity | Worldcoin — biometria + AI, narrativa forte | ACTIVE |
| SUIUSDT | L1 / Move VM | Alto potencial de crescimento | ACTIVE |
| NEARUSDT | L1 / AI infra | Narrativa AI + blockchain | ACTIVE |
| INJUSDT | DeFi / Derivatives | Líder em on-chain derivatives | ACTIVE |
| ARBUSDT | L2 / Ethereum | Principal L2 por TVL | ACTIVE |
| OPUSDT | L2 / Ethereum | Optimism ecosystem, governança activa | ACTIVE |
| FETUSDT | AI / Agentes | Narrativa AI forte, Fetch.ai | ACTIVE |
| TAOUSDT | AI / DePin | Bittensor — AI descentralizada | ACTIVE |
| RENDERUSDT | AI / GPU / DePin | GPU marketplace descentralizado | ACTIVE |

---

## 6. TIER_2_MONITOR

> Ativos com potencial identificado, mas liquidez menor ou narrativa em desenvolvimento.
> Monitorados semanalmente; podem ser promovidos ao TIER_1 mediante reavaliação de score.

| Símbolo | Sector | Observação | Status |
|---|---|---|---|
| DYDXUSDT | DeFi / DEX Derivativos | Protocolo de derivativos descentralizados | ACTIVE |
| EIGENUSDT | Restaking / EigenLayer | Narrativa restaking Ethereum | ACTIVE |
| PENDLEUSDT | DeFi / Yield Trading | Tokenização de yield, nicho mas sólido | ACTIVE |
| KASUSDT | L1 / DAG | Kaspa — alta velocidade, comunidade crescente | ACTIVE |
| QNTUSDT | Interoperabilidade / Enterprise | Quant Network — foco institucional | ACTIVE |
| GMXUSDT | DeFi / Perpetuals | DEX de futuros, liderança em Arbitrum | ACTIVE |
| IMXUSDT | Gaming / L2 | Immutable X — NFT/gaming scaling | ACTIVE |
| AXSUSDT | Gaming / P2E | Axie Infinity — referência em GameFi | ACTIVE |
| STRKUSDT | L2 / ZK | Starknet — ZK rollup com ecossistema | ACTIVE |
| RONINUSDT | Gaming / Sidechain | Ronin Network — gaming blockchain | ACTIVE |

---

## 6.1 TIER_3_BULL_CYCLE

> Ativos para observação de médio/longo prazo.
> **Revisão activa prevista a partir de 2027.**
> Não incluir no scan diário até reavaliação formal.

| Símbolo | Sector | Observação | Status |
|---|---|---|---|
| ORDIUSDT | Bitcoin / Ordinals | Inscrições Bitcoin, dependente de bull cycle | ACTIVE |
| MOVEUSDT | L1 / Move VM | Movement Labs — novo ecossistema Move | ACTIVE |
| TAIKOUSDT | L2 / ZK-EVM | Taiko — ZK-EVM equivalente ao Ethereum | ACTIVE |
| MORPHOUSDT | DeFi / Lending | Morpho — lending optimizado, crescimento gradual | ACTIVE |
| DRIFTUSDT | DeFi / Perpetuals | Drift Protocol — DEX de derivativos em Solana | ACTIVE |

---

## 7. Lista Proibida

> Ativos **banidos permanentemente** do sistema.
> **Nenhuma excepção. Nenhuma reavaliação sem aprovação Type 3.**

| Símbolo | Motivo do Banimento |
|---|---|
| USELESSUSDT | Token sem utilidade, liquidez artificial, risco de rug pull |
| GIGGLEUSDT | Memecoin com manipulação confirmada, sem fundamentos |
| JELLYJELLYUSDT | Manipulação de mercado documentada em exchange |
| DUSDT | Identificador ambíguo, risco de confusão / token predatório |
| HUSDT | Identificador ambíguo, risco de confusão / token predatório |
| BUSDT | Identificador ambíguo, risco de confusão / token predatório |
| QUSDT | Identificador ambíguo, risco de confusão / token predatório |
| 4USDT | Identificador inválido / token de teste não regulamentado |
| TSLAUSDT | Token sintético não autorizado, risco regulatório elevado |

---

## 8. Log de movimentações

| Data | Ativo | Acção | Motivo | Operador |
|---|---|---|---|---|
| 2026-04-11 | — | Normalização v1.0 | Migração legacy-unversioned | Governança |
| 2026-04-11 | — | Validação v1.1 | Critérios confirmados; ativos pendentes de revisão | Governança |
| 2026-04-11 | Todos os ativos legacy | Migração v1.2 — ACTIVE | Validação pelo operador; sistema 0–35 adoptado | Operador |
| 2026-04-11 | Lista Proibida (9 ativos) | Incorporação v1.2 — BANNED | Formalização de secção oficial a partir de legacy | Operador |
| 2026-04-15 | MATICUSDT | Removido TIER_1 | Substituido por WLDUSDT — narrativa enfraquecida, rebrand para POL | Operador |
| 2026-04-15 | WLDUSDT | Adicionado TIER_1 | Narrativa AI/Identity forte, activo nos scans desde 2026-04-15 | Operador |

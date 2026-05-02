# EURU_FASE1_CANDIDATES_REVIEW.md

**Periodo:** 2026-04-30 a 2026-05-14 (14 dias)
**Operador:** Andre Marcal
**Status:** ACTIVE
**Timezone:** Europe/Madrid
**Inicio formal Fase 1:** 2026-04-30 14:15 Madrid

**Plano de referencia:** 00_MASTER/EURU_PLANO_FASE1_OBSERVACAO_2026-04-29_v0.3.1.md (commit 01d1a0e)
**Aprovacao Type 2:** commit ba557b0 (2026-04-30)

---

## Compromisso do Operador

- Frequencia de revisao: diariamente, antes das 09:00 Europe/Madrid
- Tolerancia: ate 4 dias consecutivos sem leitura (5 dias = gatilho C)
- Validacao por sinal: BTC context, MAC qualitativo, OBV, RSI, MACD, narrativa

---

## Tabela de Revisao

| Date | Asset | TF | BTC State | Sinal Sistema | Eu (Bruno-style) | Razao | Concorda? |
|------|-------|----|-----------|----------------|--------------------|-------|-----------|
| 2026-05-01 | BTCUSDT | 1D | SIDEWAYS | NO_TRADE (23/35) | NO_TRADE | Preco -0.08% do 7D avg, sem direccao clara, MACD BEARISH, OBV FALLING. Filtro funcionou. | YES |
| 2026-05-01 | ETHUSDT | 1D | SIDEWAYS | WATCHLIST (23/35) | WATCHLIST | Score alto mas BTC filter activo. Compression YES, RSI 50 neutro. Aguardar. | YES |
| 2026-05-01 | RENDERUSDT | 1D | SIDEWAYS | WATCHLIST (23/35) | WATCHLIST | Downgraded de SETUP por BTC filter. -4.23% 7D, BEARISH, OBV FALLING. Concorda metodo. | YES |
| 2026-05-01 | SOLUSDT | 1D | SIDEWAYS | WATCHLIST (22/35) | WATCHLIST | Score 22, BEARISH, FALLING OBV. Sem trigger especifico. | YES |
| 2026-05-01 | BNBUSDT | 1D | SIDEWAYS | WATCHLIST (22/35) | WATCHLIST | Compression YES, mas BTC filter dominante. Watchlist correcto. | YES |
| 2026-05-01 | ADAUSDT | 4H | SIDEWAYS | WEAK breakout LONG (49/100) | WATCHLIST | Breakout fraco (wick 0.64 high) sobre resistance, sem compression. Score 49 baixo. Bruno-style: nao actuar. | YES |
| 2026-05-01 | TAOUSDT | 1D | SIDEWAYS | WATCHLIST (21/35) | WATCHLIST | Unico BULLISH no scan (+1.66% 7D, MACD BULLISH). Mas FAKEOUT short detectado. Aguardar resolucao. | YES |
| 2026-05-02 | BTCUSDT | 1D | BULLISH | WATCHLIST (26/35) | WATCHLIST | BTC virou BULLISH. OBV RISING confirma volume, MACD lag BEARISH. Aguardar viragem MACD ou breakout sobre 79,485. | YES |
| 2026-05-02 | TAOUSDT | 1D | BULLISH | SETUP (28/35 PREMIUM) | NO_TRADE | OBV FLAT + VOLUME_FLOW WEAK = movimento sem confirmacao. Range 8.31% vs 5.25% medio = potencial fakeout. Bruno-style: WATCHLIST. | NO |
| 2026-05-02 | INJUSDT | 1D | BULLISH | SETUP (21/35) | NO_TRADE | Subiu 8.17% 24h sem volume confirmacao. RSI 65.76 quase overbought. Late entry. OBV FLAT, VOLUME WEAK. | NO |
| 2026-05-02 | WLDUSDT | 1D | BEARISH | SETUP (23/35) | BEARISH_WATCHLIST_PENDING_BREAKDOWN | Setup short tecnicamente valido AT_WEEKLY_LOW + Volume STRONG. Mas RSI 33.89 oversold = risco bounce. Aguardar quebra confirmada 4H. | PARCIAL |
| 2026-05-02 | NEARUSDT | 1D | BEARISH | SETUP (22/35) | BEARISH_WATCHLIST | Similar a WLD mas momentum frouxo (-1% 24h). Volume STRONG mas movimento tepid. | PARCIAL |
| 2026-05-02 | ARBUSDT | 1D | BEARISH | SETUP (20/35) | NO_TRADE | Score 20 baixo (MEDIA), RSI 54 nem oversold nem bearish forte, BELOW_7D mas nao AT_WEEKLY_LOW. Setup fraco. | NO |

---

## Notas e Findings

### Dia 1 - 2026-05-01 (PC ligado as 09:26 Madrid; tasks correram em batch)

**Nota de timing:** PC desligado durante a noite, todas as 5 tasks correram entre 09:26-09:27 em batch (Asian deveria ter sido 02:00, Morning 07:00, Trade Monitor 07:30). Decisao registada: PC 24/7 a partir de hoje (ver DECISOES_ESTRATEGICAS_REVISADO.md).

**Estado do mercado:** BTC em SIDEWAYS (4H NO_TRADE, 1D SIDEWAYS), -0.08% do 7D avg. BTC Master Filter activo - todos os sinais SETUP altcoin foram downgraded a WATCHLIST automaticamente.

**Padroes observados:**
- Score range 18-23/35 (sem score alto excepcional)
- Top 3 score (23): BTC, ETH, RENDER - todos NO_TRADE ou WATCHLIST
- 3 ativos downgraded explicitamente: WLDUSDT, NEARUSDT, RENDERUSDT (todos com SIGNAL [BTC filter])
- Volume exhaustion comum mas sem compressao de range (need 2 consecutive pairs, todos com 1)
- News Sentinel HIGH severity (crypto hacks 630M April; Kast hire SEC official)

**Breakout layer (4H):**
- 1 WEAK breakout: ADAUSDT LONG (score 49/100, wick alto 0.64)
- 3 FAKEOUTS detectados: BTC LONG, OP LONG, TAO SHORT
- 6 ativos near-zone: ETH, SOL, LINK, SUI, INJ, ARB

**Bruno-style assessment:** mercado em modo de espera. Volume cai mas range nao comprime ao nivel necessario. Zero setup metodologicamente valido. Zero accao operacional. Filtros funcionaram conforme esperado.

**Concordancia operador-sistema:** 7/7 sinais revistos = 7 YES. Sistema esta a aplicar metodo correctamente.

---

### Dia 2 - 2026-05-02 (PC 24/7 funcionou, timing perfeito; mercado mudou de regime)

**Nota de timing:** PC permaneceu ligado durante a noite. Tasks correram nas horas exactas previstas (Asian 02:00:01, Morning 07:00:01, Trade Monitor 07:30:01, Journal 07:30:01, Daily Audit 08:30:01). Decisao PC 24/7 validada empiricamente. Critério F: PASS (timing).

**Mudanca de regime BTC:**
- Dia 1 (1 Mai): BTC 1D SIDEWAYS, Master Filter ACTIVE em ambos os scans
- Dia 2 (2 Mai): BTC 1D BULLISH, BTC 4H WATCHLIST
- Asian Master Filter: ACTIVE (BTC 4H WATCHLIST)
- Morning Master Filter: INACTIVE (BTC 1D BULLISH)
- Discrepancia 4H vs 1D - feature incompleta (ver Inconsistencias)

**Sinais promovidos a SETUP (5):**
- TAOUSDT (28/35 PREMIUM, +6.96% 7D, BULLISH, mas OBV FLAT + VOLUME WEAK)
- INJUSDT (21/35, +8.17% 24h, BULLISH, mas OBV FLAT + VOLUME WEAK, RSI 65.76)
- WLDUSDT (23/35, BEARISH, AT_WEEKLY_LOW, Volume STRONG, RSI 33.89 oversold)
- NEARUSDT (22/35, BEARISH, AT_WEEKLY_LOW, Volume STRONG, momentum tepid)
- ARBUSDT (20/35, BEARISH, BELOW_7D_AVG, score baixo)

**News Sentinel:** (verificar morning report - pendente nesta nota)

**CROSS-CHECK CLAUDE + CODEX (6/6 concordancia):**

| Sinal | Claude | Codex | Final |
|---|---|---|---|
| BTC | YES | YES | YES |
| TAO | NO | NO | NO |
| INJ | NO | NO | NO |
| WLD | PARCIAL | PARCIAL | PARCIAL |
| NEAR | PARCIAL | PARCIAL | PARCIAL |
| ARB | NO | NO | NO |

Convergencia perfeita entre dois agentes Bruno-style independentes. Validacao do
metodo de cross-check operador-Claude-Codex.

**Concordancia operador-sistema Dia 2:** 1/6 YES + 2/6 PARCIAL + 3/6 NO. Contraste
forte com Dia 1 (7/7 YES). **Primeira divergencia metodologica observada.**

---

### Sintese das respostas Codex (Dia 2 cross-check)

**Pergunta 1 - Concordas com leitura Bruno-style?**
> Codex confirma. Classificacao identica em 6/6 ativos. TAO e INJ classicos de 
> "preco andou mas fluxo nao confirmou" - RSI/MACD bonitos mas OBV FLAT + 
> VOLUME WEAK nao passam pelo olhar MAC. WLD/NEAR interessantes para continuation
> bearish mas precisam quebra limpa do weekly low. ARB rejeitado por score 
> insuficiente e localizacao ambigua.

**Pergunta 2 - Discrepancia 4H vs 1D: bug ou feature?**
> "Feature incompleta", nao bug. 4H = timing/curto prazo; 1D = clima/regime 
> estrutural. Falta regra de reconciliacao multi-timeframe. Estado futuro 
> desejado: MTF_ALIGNMENT = FULL/PARTIAL/CONFLICTING gerando "Final posture = 
> WATCHLIST / reduced conviction" quando ha conflito. Hoje sistema trata 
> filtros separadamente. Ambiguidade operacional esperada - Fase 1 deve 
> capturar exactamente este tipo de coisa.

**Pergunta 3 - Adicionar OBV/Volume check antes de SETUP?**
> Sim mas NAO durante observacao. SETUP atual = movimento/estrutura. SETUP 
> Bruno-style = movimento + aceleracao + confirmacao. Check ideal futuro: se 
> OBV FLAT ou VOLUME_FLOW WEAK, downgrade automatico SETUP -> WATCHLIST ou 
> SETUP_QUALITY = PARTIAL. Plus: MAC_VALID e Two-Day OBV explicitos. Por enquanto 
> registar como finding, nao mexer no sistema. Divergencia operador-sistema e 
> material de estudo da Fase 1.

**Pergunta 4 - Entrarias em algum se fosse SIMULATE/EXECUTE?**
> Nenhum dos 5. TAO: nao (movimento esticado sem volume). INJ: nao (RSI quase
> overbought, late entry). WLD: nao ainda (watchlist bearish ate quebra weekly 
> low). NEAR: nao ainda (momentum frouxo). ARB: nao (score/estrutura 
> insuficientes). Se obrigado a escolher "menos ruim": WLD como 
> BEARISH_WATCHLIST_PENDING_BREAKDOWN, nunca como entrada.

**Pergunta 5 - Observacoes adicionais para CANDIDATES_REVIEW?**
> Dia 2 mostra overpromotion de SETUP quando BTC 1D fica BULLISH e BTC filter 
> desativa. Sistema confunde movimento de preco com confirmacao de fluxo em 
> TAO/INJ. OBV FLAT + VOLUME WEAK deveria impedir SETUP no metodo MAC. SETUP 
> bearish em WLD/NEAR/ARB e semanticamente ambiguo porque Core nao separa 
> LONG_CANDIDATE vs SHORT_CANDIDATE. Discrepancia BTC 4H WATCHLIST vs BTC 1D 
> BULLISH deve gerar MTF_ALIGNMENT = PARTIAL no futuro.

**Conclusao Codex:** Dia 2 nao e mau sinal do sistema, e bom sinal da Fase 1. 
Encontramos exactamente o que queriamos encontrar: onde o sistema actual ve 
"setup" cedo demais comparado ao metodo Bruno/MAC.

**Severidade do finding:** medium  
**Accao recomendada agora:** observar, nao corrigir  
**Critério F:** PASS (filtro Asian funcionou; Morning desactivou correctamente; ausencia de OBV/MAC check e finding, nao falha)  
**Critério E:** PASS (revisao humana feita) com discordancia metodologica documentada

---
## Inconsistencias Detectadas

### Finding 001 - 2026-05-02: Overpromotion de SETUP sem confirmacao MAC

**Detectado em:** Dia 2 (2026-05-02), Morning Scan
**Severidade:** medium
**Reporters:** Claude + Codex (cross-check, 6/6 concordancia)
**Status:** Observar, nao corrigir durante Fase 1

**Descricao:**
Quando BTC Master Filter desactiva (BTC 1D BULLISH), sistema promove ativos a SETUP
baseando-se em estrutura/desvio/preco mas sem exigir confirmacao de fluxo (OBV,
VOLUME_FLOW). Resultado: 5 SETUPs promovidos no Dia 2, mas 3/5 (TAO, INJ, ARB) com
OBV FLAT + VOLUME_FLOW WEAK que Bruno-style classificaria WATCHLIST.

**Lacuna metodologica:**
- SETUP actual = movimento + estrutura
- SETUP Bruno-style = movimento + aceleracao + confirmacao (MAC)

**Discrepancia MTF (multi-timeframe):**
- BTC 4H state WATCHLIST (Master Filter Asian ACTIVE)
- BTC 1D state BULLISH (Master Filter Morning INACTIVE)
- Falta regra de reconciliacao: MTF_ALIGNMENT = FULL/PARTIAL/CONFLICTING

**Recomendacoes para Fase 2 (NAO accionar agora):**
1. Implementar check explicito MAC_VALID = YES/PARTIAL/NO
2. Implementar Two-Day OBV protocol explicito
3. Adicionar campo SETUP_QUALITY (FULL/PARTIAL) baseado em OBV/Volume
4. Implementar MTF_ALIGNMENT field para reconciliacao 4H/1D
5. Separar LONG_CANDIDATE vs SHORT_CANDIDATE no Core (resolve ambiguidade
   semantica de SETUP em ativos bearish como WLD/NEAR/ARB)

**Accao Fase 1:** continuar observacao, acumular dados ate 14 Mai. Findings
similares em dias subsequentes solidificam evidencia para Type 2 ou Type 3 pos-Fase 1.


---

## Checkpoint Intermedio T+7d

**Data prevista:** 2026-05-07
**Status:** PENDING

(Operador preenche em T+7d com revisao do estado e decisao continuar/recalibrar/abortar.)

---

## Avaliacao Final T+14d

**Data prevista:** 2026-05-14
**Status:** PENDING

(Operador preenche em T+14d com avaliacao dos 8 criterios de sucesso.)

### Criterios de Sucesso

- [ ] A: 14 dias sem falhas criticas
- [ ] B: Daily Audit sem incidentes graves
- [ ] C: Reports gerados consistentemente cada dia util
- [ ] D: Git sync automatico funcional
- [ ] E: Avaliacao qualitativa de sinais coerente com metodo
- [ ] F: BTC Master Filter comporta-se conforme metodo
- [ ] G: Tabela CANDIDATES_REVIEW.md preenchida regularmente
- [ ] H: Zero modificacoes de codigo durante observacao

### Decisao Pos-Fase 1

(Cenario 1, 2 ou 3 conforme Seccao 12 do plano.)

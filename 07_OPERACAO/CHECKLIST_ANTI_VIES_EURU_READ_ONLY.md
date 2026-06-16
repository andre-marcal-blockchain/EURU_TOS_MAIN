# CHECKLIST OPERACIONAL ANTI-VIES - EURU OS
**Versao:** 1.0  
**Modo alvo:** READ_ONLY primeiro; reutilizavel em SIMULATE com governanca propria  
**Base canonica:** `00_MASTER/EURU_BRUNO_AGUIAR_MAC_KNOWLEDGE_BASE.md`

---

## Objetivo

Esta checklist existe para impedir que o EURU confunda:

- leitura tecnica com permissao operacional
- conviccao com evidencia
- marketing com validacao
- score alto com trade bom
- um caso bonito com expectativa positiva real

Regra-matriz:

> Se houver conflito entre entusiasmo e evidencia, vence a evidencia.  
> Se houver conflito entre evidencia e risco, vence o risco.

---

## Como usar

Esta checklist deve ser usada:

- junto com `CHECKLIST_PRE_TRADE_v2.txt`
- antes de promover qualquer ativo de observacao para candidato operacional
- sempre que um output parecer "bom demais"
- sempre que houver pressao para acelerar fase, risco ou confianca

Se qualquer item critico falhar, a decisao padrao e:

- `NO_ENTRY`, ou
- `WAIT`, ou
- `READY_FOR_MANUAL_REVIEW`

Nunca usar esta checklist para justificar execucao real.

---

## Bloco A - Regime e permissao

| # | Pergunta anti-vies | Passa quando... | Falha quando... |
|---|---|---|---|
| A1 | Estou a separar `macro_permission` de `directional_bias`? | Regime macro e direcao foram avaliados separadamente. | Um bias bullish/bearish esta a ser tratado como permissao operacional. |
| A2 | O BTC esta a definir clima, nao a forcar narrativa? | BTC serve como filtro de regime. | A leitura de BTC esta a ser usada para "inventar" oportunidade em altcoin. |
| A3 | O contexto macro foi lido ou ignorado? | Liquidez, ETFs, politica monetaria e eventos relevantes foram considerados. | O setup parece forte, mas o ambiente macro foi omitido. |
| A4 | O sistema esta em READ_ONLY e comporta-se como READ_ONLY? | Saida permanece observacional e bloqueada para execucao. | O texto ou a interpretacao desliza para recomendacao de trade real. |

---

## Bloco B - Estrutura antes de indicador

| # | Pergunta anti-vies | Passa quando... | Falha quando... |
|---|---|---|---|
| B1 | Existem zonas claras, e nao linhas magicas? | Suporte/resistencia foram tratados como faixas de decisao. | O racional depende de um preco exato como se fosse absoluto. |
| B2 | A leitura comeca no diario? | Diario definiu zonas-mestre e contexto. | A analise comecou no 2H/4H sem contexto macro-estrutural. |
| B3 | O 4H/2H esta a ler reacao dentro da zona? | Ha rompimento, rejeicao ou pullback legivel. | O timeframe menor esta a ser usado para forcar uma narrativa. |
| B4 | A estrutura e clara ou apenas interessante? | Topos, fundos, invalidacao e espaco ate a proxima zona estao claros. | O grafico parece "promissor", mas continua ambiguo. |

---

## Bloco C - Congruencia de evidencias

| # | Pergunta anti-vies | Passa quando... | Falha quando... |
|---|---|---|---|
| C1 | Ha congruencia real ou um unico argumento dominante? | Zona, estrutura, volume e confirmadores apontam na mesma direcao. | O caso depende de um unico indicador. |
| C2 | O volume confirma ou apenas acompanha? | Ha participacao suficiente para sustentar o movimento. | Houve rompimento sem combustivel real. |
| C3 | MAC esta completo ou parcial? | Movimento, Aceleracao e Confirmacao estao alinhados. | `2/3` pilares estao a ser tratados como entrada pronta. |
| C4 | O setup pertence mesmo a um dos 5 oficiais? | Breakout, Sweep+Reversal, Reteste, Continuacao ou Narrativa+Grafico. | O ativo parece bom, mas o setup nao fecha em playbook conhecido. |

---

## Bloco D - Risco e operabilidade

| # | Pergunta anti-vies | Passa quando... | Falha quando... |
|---|---|---|---|
| D1 | A invalidacao esta clara antes da tese? | Stop logico existe antes de qualquer entusiasmo. | O alvo foi debatido antes da invalidacao. |
| D2 | Existe `Room R` suficiente ate a proxima zona? | O espaco justifica a operacao. | A proxima barreira esta demasiado perto. |
| D3 | Estou a separar `technical_strength` de `operable_quality`? | Forca tecnica alta nao virou permissao automatica. | Score alto esta a ser confundido com trade bom. |
| D4 | O risco continua dominante sobre a conviccao? | Mesmo um caso forte continua subordinado a risco fixo. | O racional inclui excecao emocional tipo "desta vez vale aumentar". |

---

## Bloco E - Rigor estatistico e anti-marketing

| # | Pergunta anti-vies | Passa quando... | Falha quando... |
|---|---|---|---|
| E1 | Ha dado auditavel ou apenas frase forte? | Afirmacoes de probabilidade estao ligadas a amostra verificavel. | Surgem frases como "80% de chance" sem base medida. |
| E2 | Estou a avaliar media ou caso exemplar? | O raciocinio considera serie de trades, payoff e drawdown. | Um trade bonito esta a ser usado como prova do metodo. |
| E3 | O texto parece analise ou promocao? | O output descreve condicoes, limites e incerteza. | O output enfatiza ganhos rapidos, hero trade ou urgencia. |
| E4 | A linguagem preserva probabilidade condicionada? | O sistema diz "aumenta probabilidade" e "merece observacao". | O sistema diz "vai acontecer" ou "funciona". |

---

## Bloco F - Controlo de vies cognitivo

| # | Pergunta anti-vies | Sinal verde | Sinal vermelho |
|---|---|---|---|
| F1 | Confirmation bias | Procurei contraevidencia real. | So reuni sinais que apoiam a tese preferida. |
| F2 | Recency bias | O contexto olha mais do que o ultimo candle. | O ultimo movimento dominou toda a leitura. |
| F3 | Outcome bias | Julguei o processo, nao apenas o resultado anterior. | O ultimo trade vencedor/perdedor esta a contaminar a decisao. |
| F4 | Overconfidence | O output mantem humildade probabilistica. | A tese ficou mais forte do que os dados permitem. |
| F5 | Narrative bias | A narrativa ajuda, mas nao substitui grafico. | Tema forte esta a mascarar estrutura fraca. |
| F6 | Action bias | Aceitei que nao operar pode ser a melhor decisao. | Existe pressa em produzir "algo acionavel". |

---

## Regras de decisao

1. Se qualquer item de `A1-A4`, `C3`, `D3` ou `E1-E4` falhar, o minimo e `READY_FOR_MANUAL_REVIEW`.
2. Se houver conflito entre estrutura, volume e contexto macro, a decisao padrao e `WAIT`.
3. Se a tese depender de promessa estatistica nao validada, a decisao padrao e `NO_ENTRY`.
4. Se o ativo tiver score alto mas `operable_quality` fraca, manter observacao e nao promover sinal.
5. Em READ_ONLY, qualquer conclusao deve terminar bloqueada para execucao.

---

## Template de preenchimento rapido

```text
Asset:
Data:
Regime macro:
Directional bias:
Technical strength:
Operable quality:
Setup oficial:
Zona diaria:
Confirmacao por volume:
Contraevidencia principal:
Risco/invalidacao claro:
Ha afirmacao nao validada?:
Decisao final:
Motivo:
```

---

## Saidas permitidas

Use apenas:

- `NO_ENTRY`
- `WAIT`
- `PAPER_ENTRY`
- `READY_FOR_MANUAL_REVIEW`
- `DATA_UNAVAILABLE`
- `WRITE_FAILED`

`PAPER_ENTRY` so pode existir em contexto governado de SIMULATE. Em READ_ONLY, a saida pratica esperada continua a ser observacional.

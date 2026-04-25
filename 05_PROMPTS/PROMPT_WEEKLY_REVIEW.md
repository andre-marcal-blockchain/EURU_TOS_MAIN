# PROMPT_WEEKLY_REVIEW — Euru OS
**Versão:** 1.0 (Week 5+)
**Última actualização:** 2026-04-05
**Frequência:** Sexta-feira
**Duração estimada:** 45–60 minutos
**Referência:** `07_OPERACAO/SOP_SEMANAL.txt`

---

## REGRA DE OURO
A semana só fecha quando este SOP estiver completo e registado no Changelog.

---

## IDENTIFICAÇÃO DA SEMANA

```
Semana:          Week ___
Período:         YYYY-MM-DD  a  YYYY-MM-DD
Data da revisão: ___________
Operador:        Risk/Product Owner (Andre)
```

---

## BLOCO 1 — VISÃO GERAL DA SEMANA (10 min)

```
Dias operacionais analisados:      ___
Assets em triage (Score Engine):   ___
Assets em WATCHLIST:               ___
Assets em SETUP:                   ___
Incidentes técnicos ocorridos:     ___
BTC Master Filter (maioria):       ACTIVE / INACTIVE

Classificação do mercado esta semana:
[ ] Mercado fácil    — BTC bullish, sinais claros
[ ] Mercado misto    — BTC sideways, sinais ambíguos
[ ] Mercado difícil  — BTC bearish, alta severidade notícias
```

---

## BLOCO 2 — QUALIDADE DAS LEITURAS (15 min)

### Scout (01)
```
Assets com melhor estrutura esta semana:   ___________
Assets com pior estrutura:                 ___________
Padrões que se repetiram:                  ___________
Erros de leitura estrutural detectados:    SIM / NÃO
Descrição (se SIM):                        ___________
```

### Flow Analyst (02)
```
Vezes que o fluxo CONFIRMOU a estrutura do Scout:   ___
Vezes que CONTRADISSE:                              ___
Vezes INCONCLUSIVE (ruído sem sinal):               ___
Divergências OBV + RSI detectadas:                  SIM / NÃO
Detalhe:                                            ___________
```

### News Sentinel (03)
```
Eventos mais importantes da semana:   ___________
Impacto real no mercado:              ___________
Falsos alarmes HIGH sem impacto real: SIM / NÃO
Narrativas emergentes identificadas:  ___________
  (ex: AI, RWA, DePIN, L2, outros)
```

### Score Engine (08)
```
Asset com score mais alto da semana:  ___________  (score: /35)
Score médio do leaderboard:           ___________
Assets promovidos de tier:            ___________
Assets rebaixados de tier:            ___________
```

**Padrões confiáveis desta semana:**
```
___________
```

**Padrões duvidosos a evitar:**
```
___________
```

---

## BLOCO 3 — SAÚDE DA INFRAESTRUTURA (10 min)

```
Pipeline DEGRADED algum dia?           SIM / NÃO    Dia(s): ___________
Assets STALE recorrentes (além MATIC): SIM / NÃO    Asset(s): ___________
Falhas de script ou timeout:           SIM / NÃO    Detalhe: ___________
Asian scan correu todas as noites?     SIM / NÃO    Falhou em: ___________
Todos os relatórios gerados?           SIM / NÃO
Incidentes sem postmortem registado?   SIM / NÃO

Classificação da infraestrutura esta semana:
[ ] Estável        — zero falhas críticas
[ ] Aceitável      — 1–2 falhas recuperadas
[ ] Instável       — falhas frequentes ou não recuperadas
```

---

## BLOCO 4 — GOVERNANÇA E ADERÊNCIA (5 min)

```
Sistema respeitou SYSTEM_MODE actual?       SIM / NÃO
Tentativa de pular etapas?                  SIM / NÃO    Detalhe: ___________
Violações das Regras Mãe?                   SIM / NÃO    Detalhe: ___________
Changelog actualizado correctamente?        SIM / NÃO
Decisões estratégicas registadas?           SIM / NÃO
Journal preenchido todos os dias?           SIM / NÃO    Faltou: ___________

Aderência esta semana:
[ ] Alta   — zero violações
[ ] Média  — 1–2 desvios menores corrigidos
[ ] Baixa  — desvios sistemáticos → rever playbook
```

---

## BLOCO 5 — DECISÕES PARA A PRÓXIMA SEMANA (10 min)

Para cada item avaliar: **manter / ajustar / congelar / promover / remover**

```
Agentes (algum precisa revisão de prompt?):
  → ___________  Tipo de mudança: Type 1 / Type 2 / Type 3

Watchlist (algum asset a promover ou rebaixar?):
  → ___________

Scripts (algum bug ou melhoria identificada?):
  → ___________  Tipo de mudança: Type 1 / Type 2 / Type 3

Regras Mãe (algum parâmetro a ajustar?):
  → ___________  Tipo de mudança: Type 2 / Type 3 (24h/48h espera)

Fase do sistema — pronto para avançar?
  READ_ONLY → SIMULATE:
  [ ] Infraestrutura estável 3+ semanas
  [ ] Agentes com outputs consistentes
  [ ] Journal preenchido diariamente
  [ ] Score Engine calibrado
  [ ] Aprovação formal Risk/Product Owner
  Resultado: SIM — avançar / NÃO — manter fase actual
```

---

## BLOCO 6 — SCORECARD SEMANAL

```
WEEK:                    [data início] to [data fim]
TOTAL_SETUPS_ANALYSED:   ___
NET_RESULT:              ___ USDT (simulado)
WIN_RATE:                ___%
TRADES_OFF_PLAYBOOK:     ___  (deve ser 0)

QUALITATIVE:
  Discipline:              /10
  Patience:                /10
  Playbook_adherence:      /10

MAIN_ERROR_PATTERN:      ___________
NEXT_WEEK_ADJUSTMENTS:   ___________
```

---

## BLOCO 7 — PERGUNTAS FINAIS DA SEMANA

```
1. O Euru ficou mais claro ou mais confuso esta semana?
   → ___________

2. O sistema está mais forte ou mais frágil?
   → ___________

3. O operador entendeu melhor o mercado?
   → ___________

4. Há base para evoluir de fase?
   → SIM / NÃO   Justificação: ___________

5. O que deve ser evitado na próxima semana?
   → ___________
```

---

## REGISTO OBRIGATÓRIO NO CHANGELOG

```
Guardar em: 01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md

## YYYY-MM-DD — Week [N] fechada
Mercado:          fácil / misto / difícil
Infraestrutura:   estável / aceitável / instável
Aderência:        alta / média / baixa
Decisões:         [lista resumida]
Próxima semana:   [prioridades]
```

---

## REFERÊNCIAS

| Documento | Localização |
|---|---|
| SOP Semanal | `07_OPERACAO/SOP_SEMANAL.txt` |
| Journal Auditor Output | `04_AGENTES/07_JOURNAL_AUDITOR/OUTPUT_FORMAT_FINAL.md` |
| Decisões Estratégicas | `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` |
| Governança de Mudanças | `01_GOVERNANCA/GOVERNANCA_DE_MUDANCAS_REVISADO.md` |
| Regras Mãe | `01_GOVERNANCA/REGRAS_MAE_REVISADO.md` |
| Watchlist Oficial | `08_DADOS_E_JOURNAL/WATCHLISTS/WATCHLIST_OFICIAL.md` |
| Incidentes | `09_LOGS_E_INCIDENTES/INCIDENTES.md` |

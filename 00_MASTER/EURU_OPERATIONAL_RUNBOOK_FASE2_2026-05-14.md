---
schema_type: operational_runbook
schema_version: 1.0
runbook_id: EURU-RUNBOOK-FASE2-2026-05-14
purpose: Manual operacional completo para Fase 2 - comandos, sequencias, templates
created: 2026-05-14
author: Andre Marcal
ai_collaborators: Claude (Anthropic), Codex (OpenAI)
companion_document: EURU_CHAT_HANDOFF_FASE2_2026-05-14.md
---

# Euru OS - Operational Runbook Fase 2

**Propósito:** Manual operacional completo. O HANDOFF document define O QUE; este define COMO.

---

## 1. Rotina Matinal Diaria (Madrid Time)

### 1.1 Timing das Tasks Automaticas

| Hora Madrid | Task | O que faz |
|---|---|---|
| 02:00 | Euru_Asian_Scan | Asian session scan (BTC 4H state) |
| 07:00 | Euru_Morning_Scan | Morning scout report (18 ativos) |
| 07:30 | Euru_Trade_Monitor | Trade monitor |
| 07:30 | Euru_Journal_Auditor | Daily journal |
| 08:30 | Euru_Daily_Audit | Daily audit + auto-commit |

**Recomendado:** Operador verifica apos 08:35 Madrid (depois do Daily Audit).

### 1.2 Comando de Verificacao Matinal Standard

Copia e cola integralmente:

```powershell
cd "C:\Users\andre\Desktop\EURU TOS MAIN"

$today = Get-Date -Format "yyyy-MM-dd"
Write-Host "`n=== VERIFICACAO MATINAL - $today ===" -ForegroundColor Cyan

# 1. Tasks - LastRun
Write-Host "`n[1] Tasks Status:" -ForegroundColor Yellow
Get-ScheduledTask | Where-Object {
    $_.TaskName -in "Euru_Asian_Scan", "Euru_Morning_Scan", "Euru_Trade_Monitor",
                    "Euru_Journal_Auditor", "Euru_Daily_Audit"
} | Sort-Object TaskName | ForEach-Object {
    $info = Get-ScheduledTaskInfo -TaskName $_.TaskName -TaskPath $_.TaskPath
    [PSCustomObject]@{
        Task = $_.TaskName
        State = $_.State
        LastRun = $info.LastRunTime
        Result = $info.LastTaskResult
    }
} | Format-Table -AutoSize

# 2. Reports gerados hoje
Write-Host "`n[2] Reports hoje:" -ForegroundColor Yellow
Get-ChildItem -Path "08_DADOS_E_JOURNAL" -Recurse -Filter "*$today*" -ErrorAction SilentlyContinue |
    Select-Object Name, LastWriteTime | Sort-Object LastWriteTime | Format-Table -AutoSize

# 3. Git status
Write-Host "`n[3] Git log + status:" -ForegroundColor Yellow
git log --oneline -6
git status --short

# 4. Asian Scan header
Write-Host "`n[4] Asian Scan header (BTC 4H state + Master Filter):" -ForegroundColor Yellow
Get-Content "08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_$today.md" -ErrorAction SilentlyContinue | Select-Object -First 13

# 5. Morning Scan header
Write-Host "`n[5] Morning Scan header (BTC trend 1D + Master Filter):" -ForegroundColor Yellow
Get-Content "08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_$today.md" -ErrorAction SilentlyContinue | Select-Object -First 13

# 6. Watch points - 9 ativos prioritarios
Write-Host "`n[6] Watch Points (9 ativos prioritarios):" -ForegroundColor Yellow
Get-Content "08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_$today.md" -ErrorAction SilentlyContinue |
    Select-String "BTCUSDT|ETHUSDT|SOLUSDT|TAOUSDT|OPUSDT|INJUSDT|ARBUSDT|FETUSDT|LINKUSDT" |
    Where-Object { $_ -match "^\| " } | Select-Object -First 9
```

### 1.3 Interpretacao dos Resultados

**Critério F (Master Filter):**
- Headers Asian/Morning indicam estado Master Filter
- "ACTIVE" = altcoin SETUPs downgraded to WATCHLIST
- "INACTIVE" = altcoin signals passam normal
- BTC trend SIDEWAYS/BEARISH = Morning ACTIVE
- BTC 4H NO_TRADE = Asian ACTIVE

**Tasks LastRun:**
- Esperado: HH:MM:01 ou HH:MM:02 (timing perfeito)
- Se tasks nao correu OU LastRun e de ontem -> investigar (sleep recovery? bug?)
- StartWhenAvailable flag deve recuperar se PC adormeceu

**Reports:**
- 5 reports esperados: ASIAN, SCOUT, JOURNAL, TRADE_MONITOR, DAILY_AUDIT
- Se algum faltar -> verificar log task scheduler

---

## 2. Analise do Dia (Bruno-Style)

### 2.1 Sequencia de Analise Standard

Apos verificacao matinal OK:

1. **Comparar D-1 vs D (todos 9 ativos):**
   - Score: subiu, manteve, caiu?
   - 24h %: positivo/negativo?
   - RSI: zona (overbought >70, neutral 30-70, oversold <30)?
   - OBV: RISING / FALLING / FLAT?
   - Trend: BULLISH / SIDEWAYS / BEARISH?

2. **Identificar eventos majores:**
   - Algum ativo mudou trend?
   - Algum tocou threshold RC001 (RSI > 70 + 7D > 15%)?
   - Algum tocou RC001-R1 (RSI > 75)?
   - Algum tocou BLOW_OFF (RSI > 80)?
   - Algum REVERSAL_UNDER_TEST / FAILED / RESUMED transition?
   - BTC matriz: qual sub-cenario materializou?

3. **Watch points abertos:**
   - INJ blow-off: cai/consolida/continua subir? (stress-test RC001-R1)
   - OP: trajectoria descendente persistente?
   - ARB: REVERSAL_FAILED standby / RESUMED_BEARISH transition?
   - BTC: BEARISH_EMERGING confirmou / TACTICAL_RESET / retomada?
   - Outros emergentes

4. **Cross-check com Codex** (3 perguntas focadas)

### 2.2 Watch Points Iniciais (carry-over D14)

| Watch point | Status D14 | O que monitorar |
|---|---|---|
| INJ BLOW_OFF stress-test | RSI 84.86 (4o dia) | Cair / consolidar / RSI > 90? |
| BTC BEARISH_EMERGING | Trend BEARISH (1a vez) | Score < 20? Trend confirma? |
| ARB RESUMED_BEARISH | Trend virou BEARISH | Trend volta BULLISH ou afunda? |
| OP descendente persistente | Score 22 (recuperacao lenta) | Recupera ou afunda? |
| Master Filter Morning | ACTIVE 8 dias consecutivos | Quando desactiva? |

---

## 3. Cross-check com Codex (Protocolo)

### 3.1 Quando perguntar ao Codex

**SEMPRE pergunta antes de:**
- Criar Finding novo
- Criar Rule Candidate nova
- Criar Refinement Candidate
- Adicionar nova taxonomia
- Mudar classificacao de watch point
- Atualizar score-state-operability hipotese
- Construir documento standalone
- Tomar Type 2 Decision

**NAO precisa perguntar para:**
- Verificacao matinal rotineira
- Listing de ativos
- Commits autonomos

### 3.2 Template Mensagem para Codex (3 perguntas)
### 3.3 Validar Resposta do Codex

Apos receber resposta:
1. Concordar / discordar com cada ponto
2. Identificar nuances
3. Propor formulacao final (preserva trail v1, v2, v3...)
4. Pedir confirmacao operador antes de inserir no CANDIDATES_REVIEW

---

## 4. Insercao no CANDIDATES_REVIEW

### 4.1 Estrutura Padrao (3-4 blocos por dia)

**BLOCO 1 - Tabela (9 linhas):**
Procurar ultima linha "2026-MM-(D-1)" e inserir APOS.

Formato linha:
**BLOCO 2 - Notas Dia X:**
Procurar "## Inconsistencias Detectadas" e inserir APOS o bloco anterior, ANTES dessa linha.

Estrutura:
**BLOCO 3 - Sintese Codex:**
Inserir ANTES de "## Inconsistencias Detectadas", APOS bloco anterior.

Estrutura:
**BLOCO 4 (opcional) - Refinement, Rule Candidate, Taxonomia:**
Inserir em seccao especifica do CANDIDATES_REVIEW ou Rules Candidate Backlog.

### 4.2 Mensagem Padrao para Codex Editar
---

## 5. Commit Git (Padrao)

### 5.1 Sequencia Standard

```powershell
cd "C:\Users\andre\Desktop\EURU TOS MAIN"

git status --short

git add "00_MASTER/EURU_FASE1_CANDIDATES_REVIEW.md"

git status --short

git commit -m "Euru OS - 2026-MM-DD - DIA X FASE 2: [evento principal] + [findings/rule updates] + [taxonomia novas] + cross-check Claude+Codex 9/9 ([N]/[N] total)"

git push origin main

git log --oneline -5
```

### 5.2 Template Mensagem Commit
---

## 6. Encerramento Diario

### 6.1 Checklist Final

Apos commit:

- [ ] Frase do dia (Codex) preservada
- [ ] Watch points para D+1 listados
- [ ] Severidades Findings actualizadas
- [ ] Operacional ainda 100% (sem alertas)
- [ ] CANDIDATES_REVIEW > 14 dias + Fase 2 inicia
- [ ] Sistema READ_ONLY mantido

### 6.2 Mensagem para Codex (opcional)
---

## 7. Troubleshooting

### 7.1 Task nao correu

**Causa frequente:** PC adormeceu.

**Verificar:**
```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TaskScheduler/Operational'} -MaxEvents 50 |
    Where-Object { $_.Message -like "*Euru*" } | Format-Table TimeCreated, Id, LevelDisplayName
```

**StartWhenAvailable:** se task tem este flag, deve recuperar quando PC voltar activo.

**Operational Note:** se task recuperou tarde, documenta como Operational Note no CANDIDATES_REVIEW.

### 7.2 Git push falhou

```powershell
git pull origin main --rebase
git push origin main
```

Se conflito, investigar antes de force push.

### 7.3 Codex perdeu contexto

Se Codex re-iniciar sessao (perdeu contexto da nossa conversa):
### 7.4 Ficheiro nao foi criado (Codex falhou silenciosamente)

**Verificar:**
```powershell
Get-Item "00_MASTER\[FICHEIRO]" -ErrorAction SilentlyContinue
```

**Se falhou:** usar PowerShell direct write com `@'...'@` here-string + `[System.IO.File]::WriteAllText` em UTF-8 sem BOM.

### 7.5 Encoding errado (caracteres especiais)

PowerShell pode escrever em UTF-16. Forcar UTF-8 sem BOM:

```powershell
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($path, $content, $utf8NoBom)
```

---

## 8. Checkpoints Periodicos

### 8.1 T+21D (2026-05-21) - Revisao Informal

- Verificar evolucao watch points (INJ blow-off, BTC trend, ARB)
- Esboco preliminar Fase 2 design 3-dimensional
- Atualizar CANDIDATES_REVIEW com sintese 7 dias
- Cross-check Codex sobre progresso

### 8.2 T+28D (2026-05-28) - Revisao Formal

- Decidir: continuar Fase 2 / transitar Fase 3 / prolongar
- Documento revisao standalone (similar a T+7D / T+14D)
- Type 2 Decision adicional se mudanca de scope

---

## 9. Quando Escalar / Pausar

### 9.1 Triggers para PAUSE

| Trigger | Acao |
|---|---|
| Falha critica sistema (task nao recupera) | PAUSE + investigacao + Type 2 nova |
| Operational Note grave (alem D7 sleep) | PAUSE + investigacao |
| Drift conceptual significativo | PAUSE + cross-check Claude+Codex |
| Codex/Claude declara inconsistencia | PAUSE + revisao |
| Score directionality gap revela-se falsa | REVERT + Type 2 nova |
| Tentacao de violar EXCLUDE list | REJECT + manter disciplina |

### 9.2 EXCLUDE List Fase 2 (NUNCA fazer sem nova Type 2)

- Ativacao paper trading
- Reactivacao tasks Disabled (GitHub_Sync, Friday_Cycle, EuruLearningEngine)
- Codigo execucao automatica
- Modificacoes Core executavel
- Sinais SHORT_CANDIDATE accionaveis
- Expansao watchlist alem 18 ativos
- Validacao RC001-R1 sem revisao operador
- Promocao RC001 a "regra oficial" sem 2-3 ocorrencias adicionais

---

## 10. Frases Guarda-Corpo (CRITICAL)

> "Andre decide. Documentos lembram. Claude tensiona governance. Codex tensiona execucao tecnica. O repositorio canonico arbitra a memoria."

> "Trust is built when there are no surprises." (slogan pessoal Marcal)

> "O checkpoint nao deve transformar-se em permissao de mudanca." (Codex T+7D)

> "A Avaliacao Final nao deve transformar-se em permissao de execucao." (Codex T+14D)

> "A Type 2 Decision Fase 2 nao deve transformar-se em permissao de implementacao." (Type 2)

---

## 11. Estrutura de Folders Importantes
---

## 12. Comandos Quick Reference

### Verificar git status
```powershell
git status --short
git log --oneline -10
```

### Verificar tasks
```powershell
Get-ScheduledTask | Where-Object { $_.TaskName -like "Euru_*" } | Format-Table TaskName, State
```

### Contar linhas ficheiro
```powershell
(Get-Content "00_MASTER\[FILE].md").Count
```

### Ver ultimas N linhas
```powershell
Get-Content "00_MASTER\[FILE].md" -Tail 50
```

### Procurar texto em ficheiro
```powershell
Select-String -Path "00_MASTER\[FILE].md" -Pattern "[PATTERN]" | Select-Object LineNumber, Line
```

### Verificar reports do dia
```powershell
Get-ChildItem "08_DADOS_E_JOURNAL" -Recurse -Filter "*$(Get-Date -Format 'yyyy-MM-dd')*"
```

---

## Fim do Runbook

Este documento e referencia operacional viva. Atualizar quando processos evoluirem.

**"Trust is built when there are no surprises."**
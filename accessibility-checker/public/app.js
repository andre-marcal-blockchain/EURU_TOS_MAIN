/**
 * Frontend do Verificador de Acessibilidade Digital.
 * Padrões de acessibilidade aplicados:
 * - mensagens de progresso/erro em regiões aria-live (role=status / role=alert)
 * - gerenciamento de foco ao exibir o resultado e ao ocorrer erro
 * - todo o conteúdo dinâmico usa HTML semântico (details/summary, listas, headings)
 */
(function () {
  'use strict';

  const form = document.getElementById('form-scan');
  const campoUrl = document.getElementById('url');
  const erroUrl = document.getElementById('url-erro');
  const status = document.getElementById('status');
  const btn = document.getElementById('btn-scan');
  const secResultado = document.getElementById('resultado');
  const tituloResultado = document.getElementById('titulo-resultado');
  const elResumo = document.getElementById('resumo');
  const elFalhas = document.getElementById('lista-falhas');
  const elRecos = document.getElementById('lista-recomendacoes');
  const elLeis = document.getElementById('lista-leis');
  const elAviso = document.getElementById('aviso-legal');
  const btnBaixar = document.getElementById('btn-baixar');

  let relatorioAtual = null;

  function esc(s) {
    const div = document.createElement('div');
    div.textContent = s == null ? '' : String(s);
    return div.innerHTML;
  }

  function definirErro(msg) {
    if (msg) {
      erroUrl.textContent = msg;
      erroUrl.hidden = false;
      campoUrl.setAttribute('aria-invalid', 'true');
      campoUrl.focus();
    } else {
      erroUrl.textContent = '';
      erroUrl.hidden = true;
      campoUrl.removeAttribute('aria-invalid');
    }
  }

  form.addEventListener('submit', async function (ev) {
    ev.preventDefault();
    definirErro('');
    const url = campoUrl.value.trim();
    if (!url) {
      definirErro('Informe o endereço do site que deseja analisar.');
      return;
    }

    btn.disabled = true;
    status.textContent =
      'Analisando a página… isso costuma levar de 15 a 60 segundos. O resultado será anunciado aqui.';
    secResultado.hidden = true;

    try {
      const resp = await fetch('/api/scan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });
      const dados = await resp.json();
      if (!resp.ok) {
        throw new Error(dados.erro || 'Falha ao escanear a página.');
      }
      relatorioAtual = dados;
      renderizar(dados);
      status.textContent = `Análise concluída: ${dados.totais.violacoes} tipo(s) de falha encontrados. Pontuação ${dados.score} de 100.`;
      secResultado.hidden = false;
      tituloResultado.setAttribute('tabindex', '-1');
      tituloResultado.focus();
    } catch (err) {
      status.textContent = '';
      definirErro(err.message);
    } finally {
      btn.disabled = false;
    }
  });

  function renderizar(r) {
    // ----- resumo -----
    const imp = r.totais.porImpacto || {};
    const nomes = { critical: 'críticas', serious: 'sérias', moderate: 'moderadas', minor: 'leves' };
    const contadores = ['critical', 'serious', 'moderate', 'minor']
      .filter((k) => imp[k])
      .map((k) => `<li class="c-${k}">${imp[k]} ${nomes[k]}</li>`)
      .join('');

    elResumo.innerHTML = `
      <div class="painel-resumo">
        <div class="score" role="img" aria-label="Pontuação de acessibilidade: ${r.score} de 100">
          <span class="num" aria-hidden="true">${r.score}</span>
          <span class="de" aria-hidden="true">de 100</span>
        </div>
        <div class="risco">
          <h3>${esc(r.titulo || r.url)}</h3>
          <p><a href="${esc(r.url)}" rel="noopener noreferrer" target="_blank">${esc(r.url)} <span class="sr-only">(abre em nova aba)</span></a></p>
          <p><span class="badge-risco risco-${esc(r.risco.nivel)}">${esc(r.risco.rotulo)}</span></p>
          <p>${esc(r.risco.descricao)}</p>
          ${contadores ? `<ul class="contadores" aria-label="Falhas por gravidade">${contadores}</ul>` : '<p><strong>Nenhuma falha automática detectada.</strong></p>'}
        </div>
      </div>`;

    // ----- falhas -----
    if (!r.violacoes.length) {
      elFalhas.innerHTML =
        '<p>Nenhuma violação detectada pela auditoria automática. Excelente! Ainda assim, realize os testes manuais recomendados abaixo.</p>';
    } else {
      elFalhas.innerHTML = r.violacoes
        .map((v, i) => {
          const leis = v.leis
            .map(
              (l) =>
                `<li><strong>${esc(l.nome)}</strong> (${esc(l.jurisdicao)}) — ${esc(l.sancoes)}</li>`
            )
            .join('');
          const exemplos = v.exemplos
            .map(
              (ex) => `
                <li>
                  <p>Elemento: <code>${esc(ex.seletor)}</code></p>
                  <code class="exemplo-html">${esc(ex.html)}</code>
                </li>`
            )
            .join('');
          const wcag = v.criteriosWcag.length
            ? `<p>Critérios WCAG: ${v.criteriosWcag.map(esc).join(', ')}</p>`
            : '';
          return `
            <details class="falha" ${i === 0 ? 'open' : ''}>
              <summary>
                <span class="badge-impacto i-${esc(v.impacto)}">${esc(v.impactoRotulo)}</span>
                <span>${esc(v.ajuda)}</span>
                <span>(${v.ocorrencias} ocorrência${v.ocorrencias > 1 ? 's' : ''})</span>
              </summary>
              <div class="falha-corpo">
                <p>${esc(v.descricao)}</p>
                ${wcag}
                <h4>Como corrigir</h4>
                <p class="correcao">${esc(v.correcao)}</p>
                <h4>Risco legal</h4>
                <ul class="leis-falha">${leis}</ul>
                <h4>Onde ocorre (até 5 exemplos)</h4>
                <ul>${exemplos}</ul>
                <p><a href="${esc(v.referencia)}" rel="noopener noreferrer" target="_blank">Documentação técnica da regra "${esc(v.id)}" <span class="sr-only">(abre em nova aba)</span></a></p>
              </div>
            </details>`;
        })
        .join('');
    }

    // ----- recomendações -----
    elRecos.innerHTML = r.recomendacoes.map((t) => `<li>${esc(t)}</li>`).join('');

    // ----- legislações -----
    elLeis.innerHTML = r.legislacoes
      .map(
        (l) => `
          <div class="lei">
            <h4>${esc(l.nome)}</h4>
            <p>${esc(l.resumo)}</p>
            <p class="sancao"><strong>Sanções:</strong> ${esc(l.sancoes)}</p>
          </div>`
      )
      .join('');

    elAviso.textContent = r.avisoLegal;
  }

  // ----- exportação de relatório autônomo -----
  btnBaixar.addEventListener('click', function () {
    if (!relatorioAtual) return;
    const r = relatorioAtual;
    const doc = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relatório de Acessibilidade — ${esc(r.url)}</title>
<style>
  body{font-family:system-ui,sans-serif;max-width:56rem;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#1a2233}
  h1,h2,h3{line-height:1.25} code{background:#f2f4f8;padding:.1rem .3rem;border-radius:4px;word-break:break-word}
  .bloco{border:1px solid #8d99ae;border-radius:8px;padding:1rem;margin:.8rem 0}
  .correcao{background:#f2f4f8;border-left:4px solid #1d4ed8;padding:.6rem .9rem}
  @media print{.bloco{break-inside:avoid}}
</style>
</head>
<body>
<h1>Relatório de Conformidade em Acessibilidade Digital</h1>
<p><strong>Página analisada:</strong> ${esc(r.url)}<br>
<strong>Data:</strong> ${new Date(r.dataScan).toLocaleString('pt-BR')}<br>
<strong>Motor de auditoria:</strong> ${esc(r.motor)} (WCAG 2.2)</p>
<h2>Resultado geral</h2>
<p><strong>Pontuação:</strong> ${r.score} de 100 — <strong>${esc(r.risco.rotulo)}</strong></p>
<p>${esc(r.risco.descricao)}</p>
<h2>Falhas encontradas (${r.totais.violacoes})</h2>
${r.violacoes
  .map(
    (v) => `<div class="bloco">
<h3>${esc(v.impactoRotulo)}: ${esc(v.ajuda)} (${v.ocorrencias} ocorrência(s))</h3>
<p>${esc(v.descricao)}</p>
${v.criteriosWcag.length ? `<p><strong>WCAG:</strong> ${v.criteriosWcag.map(esc).join(', ')}</p>` : ''}
<p><strong>Como corrigir:</strong></p><p class="correcao">${esc(v.correcao)}</p>
<p><strong>Leis afetadas:</strong></p>
<ul>${v.leis.map((l) => `<li>${esc(l.nome)} — ${esc(l.sancoes)}</li>`).join('')}</ul>
<p><strong>Exemplos:</strong></p>
<ul>${v.exemplos.map((ex) => `<li><code>${esc(ex.seletor)}</code>: <code>${esc(ex.html)}</code></li>`).join('')}</ul>
</div>`
  )
  .join('')}
<h2>Recomendações adicionais</h2>
<ul>${r.recomendacoes.map((t) => `<li>${esc(t)}</li>`).join('')}</ul>
<h2>Legislação de referência</h2>
${r.legislacoes
  .map((l) => `<div class="bloco"><h3>${esc(l.nome)}</h3><p>${esc(l.resumo)}</p><p><strong>Sanções:</strong> ${esc(l.sancoes)}</p></div>`)
  .join('')}
<p><em>${esc(r.avisoLegal)}</em></p>
</body>
</html>`;

    const blob = new Blob([doc], { type: 'text/html;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    const nomeArquivo = r.url.replace(/https?:\/\//, '').replace(/[^\w.-]+/g, '_').slice(0, 60);
    a.download = `relatorio-acessibilidade-${nomeArquivo}.html`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(a.href);
    status.textContent = 'Relatório baixado com sucesso.';
  });
})();

/**
 * Motor de escaneamento: carrega a página em Chromium headless (Playwright),
 * injeta o axe-core com locale pt_BR e consolida o resultado em um relatório
 * com contexto jurídico e sugestões de correção.
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');
const {
  LEGISLACOES,
  leisAplicaveis,
  correcaoPara,
  avaliarRisco,
  IMPACTO_LABEL,
} = require('./legal');

const AXE_SOURCE = fs.readFileSync(
  require.resolve('axe-core/axe.min.js'),
  'utf8'
);
const AXE_LOCALE_PT_BR = JSON.parse(
  fs.readFileSync(require.resolve('axe-core/locales/pt_BR.json'), 'utf8')
);

function encontrarChromium() {
  const candidatos = [
    process.env.CHROME_PATH,
    '/opt/pw-browsers/chromium',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/usr/bin/google-chrome',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  ].filter(Boolean);
  for (const p of candidatos) {
    try {
      fs.accessSync(p, fs.constants.X_OK);
      return p;
    } catch {
      /* tenta o próximo */
    }
  }
  return undefined; // deixa o playwright-core resolver via PLAYWRIGHT_BROWSERS_PATH
}

function validarUrl(entrada) {
  let url;
  try {
    url = new URL(/^https?:\/\//i.test(entrada) ? entrada : `https://${entrada}`);
  } catch {
    throw Object.assign(new Error('URL inválida. Informe um endereço como https://exemplo.com.br'), { status: 400 });
  }
  if (!['http:', 'https:'].includes(url.protocol)) {
    throw Object.assign(new Error('Apenas endereços http(s) são suportados.'), { status: 400 });
  }
  return url.toString();
}

/** Verificações complementares de boas práticas (informativas). */
async function boasPraticas(page) {
  return page.evaluate(() => {
    const texto = document.body ? document.body.innerText.toLowerCase() : '';
    const html = document.documentElement.outerHTML.toLowerCase();
    return {
      linkDeclaracaoAcessibilidade:
        /acessibilidade/.test(texto) &&
        Array.from(document.querySelectorAll('a')).some((a) =>
          /acessibilidade/i.test(a.textContent || '')
        ),
      widgetLibras: /vlibras|handtalk|hand talk/.test(html),
      skipLink: Array.from(document.querySelectorAll('a[href^="#"]')).some((a) =>
        /pular|ir para( o)? conte|skip to/i.test(a.textContent || '')
      ),
    };
  });
}

async function escanear(entradaUrl) {
  const url = validarUrl(entradaUrl);
  const executablePath = encontrarChromium();

  const browser = await chromium.launch({
    headless: true,
    executablePath,
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    const context = await browser.newContext({
      viewport: { width: 1366, height: 900 },
      userAgent:
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/122.0 Safari/537.36 VerificadorAcessibilidade/1.0',
      locale: 'pt-BR',
    });
    const page = await context.newPage();
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    // dá tempo para conteúdo dinâmico essencial renderizar
    await page.waitForLoadState('load', { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(1000);

    await page.evaluate(AXE_SOURCE);
    const axeResult = await page.evaluate((locale) => {
      window.axe.configure({ locale });
      return window.axe.run(document, {
        runOnly: {
          type: 'tag',
          values: [
            'wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice',
          ],
        },
        resultTypes: ['violations', 'passes', 'incomplete'],
      });
    }, AXE_LOCALE_PT_BR);

    const praticas = await boasPraticas(page).catch(() => null);
    const titulo = await page.title().catch(() => '');

    return montarRelatorio({ url, titulo, axeResult, praticas });
  } finally {
    await browser.close();
  }
}

function extrairCriteriosWcag(tags) {
  return tags
    .filter((t) => /^wcag\d+$/.test(t))
    .map((t) => {
      const d = t.replace('wcag', '');
      return d.length >= 3 ? `${d[0]}.${d[1]}.${d.slice(2)}` : d;
    });
}

function montarRelatorio({ url, titulo, axeResult, praticas }) {
  const contagemPorImpacto = {};
  let penalidade = 0;

  const violacoes = axeResult.violations
    .map((v) => {
      const impacto = v.impact || 'minor';
      contagemPorImpacto[impacto] = (contagemPorImpacto[impacto] || 0) + 1;
      const peso = (IMPACTO_LABEL[impacto] || IMPACTO_LABEL.minor).peso;
      // peso por regra + parcela pelo nº de ocorrências (com teto)
      penalidade += peso + Math.min(v.nodes.length - 1, 5) * (peso / 4);

      return {
        id: v.id,
        impacto,
        impactoRotulo: (IMPACTO_LABEL[impacto] || IMPACTO_LABEL.minor).pt,
        descricao: v.description,
        ajuda: v.help,
        referencia: v.helpUrl,
        criteriosWcag: extrairCriteriosWcag(v.tags),
        ocorrencias: v.nodes.length,
        exemplos: v.nodes.slice(0, 5).map((n) => ({
          seletor: Array.isArray(n.target) ? n.target.join(' ') : String(n.target),
          html: (n.html || '').slice(0, 300),
          detalhe: n.failureSummary || '',
        })),
        correcao: correcaoPara(v),
        leis: leisAplicaveis(v.id, v.tags).map((sigla) => LEGISLACOES[sigla]),
      };
    })
    .sort((a, b) => (IMPACTO_LABEL[b.impacto]?.peso || 0) - (IMPACTO_LABEL[a.impacto]?.peso || 0));

  const score = Math.max(0, Math.round(100 - penalidade));
  const risco = avaliarRisco(score, contagemPorImpacto);

  const recomendacoes = [];
  if (praticas) {
    if (!praticas.skipLink) {
      recomendacoes.push(
        'Adicione um "skip link" ("Pular para o conteúdo") como primeiro elemento focável da página.'
      );
    }
    if (!praticas.linkDeclaracaoAcessibilidade) {
      recomendacoes.push(
        'Publique uma Declaração de Acessibilidade com canal de contato — exigida pelo EAA na UE e forte evidência de boa-fé em fiscalizações no Brasil.'
      );
    }
    if (!praticas.widgetLibras) {
      recomendacoes.push(
        'Considere oferecer tradução para Libras (ex.: VLibras, gratuito do governo federal) — a LBI reconhece Libras como meio legal de comunicação.'
      );
    }
  }
  recomendacoes.push(
    'Complemente esta auditoria automática com testes manuais: navegação 100% por teclado, leitor de tela (NVDA/VoiceOver) e zoom de 200%. Ferramentas automáticas detectam de 30% a 50% das barreiras.'
  );

  return {
    url,
    titulo,
    dataScan: new Date().toISOString(),
    motor: `axe-core ${axeResult.testEngine ? axeResult.testEngine.version : ''}`.trim(),
    score,
    risco,
    totais: {
      violacoes: violacoes.length,
      ocorrencias: violacoes.reduce((s, v) => s + v.ocorrencias, 0),
      porImpacto: contagemPorImpacto,
      aprovadas: axeResult.passes.length,
      inconclusivas: axeResult.incomplete.length,
    },
    violacoes,
    boasPraticas: praticas,
    recomendacoes,
    legislacoes: Object.values(LEGISLACOES),
    avisoLegal:
      'Relatório gerado por auditoria automatizada (axe-core/WCAG). Não constitui parecer jurídico; ' +
      'valores de sanção são referências das leis citadas e da prática dos órgãos fiscalizadores.',
  };
}

module.exports = { escanear, validarUrl };

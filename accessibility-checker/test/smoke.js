/**
 * Teste de fumaça: sobe o servidor, escaneia
 *  1) a página de demonstração (deve encontrar muitas falhas conhecidas), e
 *  2) a própria interface do app (deve estar limpa — o verificador precisa
 *     passar no próprio teste).
 */
const { spawn } = require('child_process');
const path = require('path');

const PORT = 3457;
const BASE = `http://localhost:${PORT}`;

function esperar(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function aguardarServidor(tentativas = 30) {
  for (let i = 0; i < tentativas; i++) {
    try {
      const r = await fetch(`${BASE}/api/health`);
      if (r.ok) return;
    } catch {
      /* ainda subindo */
    }
    await esperar(500);
  }
  throw new Error('Servidor não subiu a tempo');
}

async function scan(url) {
  const resp = await fetch(`${BASE}/api/scan`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url }),
  });
  const dados = await resp.json();
  if (!resp.ok) throw new Error(`scan de ${url} falhou: ${dados.erro}`);
  return dados;
}

function assert(cond, msg) {
  if (!cond) {
    console.error(`FALHOU: ${msg}`);
    process.exitCode = 1;
  } else {
    console.log(`ok: ${msg}`);
  }
}

(async () => {
  const servidor = spawn('node', [path.join(__dirname, '..', 'server.js')], {
    env: { ...process.env, PORT: String(PORT) },
    stdio: 'inherit',
  });

  try {
    await aguardarServidor();

    // 1) página de demonstração: deve reprovar
    const demo = await scan(`${BASE}/demo/pagina-inacessivel.html`);
    console.log(
      `\nDemo: score=${demo.score}, risco=${demo.risco.nivel}, ` +
        `violações=${demo.totais.violacoes} (${JSON.stringify(demo.totais.porImpacto)})\n`
    );
    assert(demo.totais.violacoes >= 8, 'demo tem pelo menos 8 tipos de falha');
    assert(demo.score < 50, 'demo tem pontuação reprovada (< 50)');
    assert(['alto', 'critico'].includes(demo.risco.nivel), 'demo tem risco alto/crítico');

    const ids = demo.violacoes.map((v) => v.id);
    for (const esperado of ['image-alt', 'html-has-lang', 'document-title', 'label', 'link-name', 'meta-viewport']) {
      assert(ids.includes(esperado), `demo detecta a falha "${esperado}"`);
    }
    const comLeis = demo.violacoes.every((v) => v.leis.length > 0 && v.correcao);
    assert(comLeis, 'toda violação traz leis aplicáveis e sugestão de correção');

    // 2) a própria interface do app: deve passar
    const propria = await scan(`${BASE}/index.html`);
    console.log(
      `\nInterface do app: score=${propria.score}, risco=${propria.risco.nivel}, ` +
        `violações=${propria.totais.violacoes}\n`
    );
    if (propria.totais.violacoes > 0) {
      for (const v of propria.violacoes) {
        console.error(`  - [${v.impacto}] ${v.id}: ${v.ajuda} (${v.ocorrencias}x)`);
        for (const ex of v.exemplos) console.error(`      ${ex.seletor}`);
      }
    }
    assert(propria.totais.violacoes === 0, 'a interface do próprio app não tem violações');
    assert(propria.score === 100, 'a interface do próprio app tem pontuação 100');

    console.log(process.exitCode ? '\nTESTE REPROVADO' : '\nTESTE APROVADO');
  } catch (err) {
    console.error('Erro no teste:', err.message);
    process.exitCode = 1;
  } finally {
    servidor.kill('SIGTERM');
  }
})();

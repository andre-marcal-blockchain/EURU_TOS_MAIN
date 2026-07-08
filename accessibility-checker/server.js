/**
 * Verificador de Conformidade em Acessibilidade Digital
 * Servidor HTTP: interface web acessível + API de escaneamento.
 *
 * Uso: node server.js  →  http://localhost:3400
 */
const express = require('express');
const path = require('path');
const { escanear } = require('./lib/scanner');

const app = express();
const PORT = process.env.PORT || 3400;

app.use(express.json({ limit: '100kb' }));
app.use(express.static(path.join(__dirname, 'public')));
app.use('/demo', express.static(path.join(__dirname, 'demo')));

// Evita scans concorrentes ilimitados no mesmo processo
let scansAtivos = 0;
const MAX_SCANS = 2;

app.post('/api/scan', async (req, res) => {
  const { url } = req.body || {};
  if (!url || typeof url !== 'string') {
    return res.status(400).json({ erro: 'Informe o endereço do site no campo "url".' });
  }
  if (scansAtivos >= MAX_SCANS) {
    return res
      .status(429)
      .json({ erro: 'Há escaneamentos em andamento. Aguarde alguns segundos e tente novamente.' });
  }
  scansAtivos++;
  try {
    const relatorio = await escanear(url);
    res.json(relatorio);
  } catch (err) {
    const status = err.status || 500;
    const mensagem =
      status === 400
        ? err.message
        : /Timeout|net::|ERR_NAME_NOT_RESOLVED|ERR_CONNECTION/.test(String(err.message))
          ? 'Não foi possível carregar a página. Verifique se o endereço está correto e acessível publicamente.'
          : 'Falha inesperada ao escanear a página. Tente novamente.';
    console.error(`[scan] ${url}:`, err.message);
    res.status(status).json({ erro: mensagem });
  } finally {
    scansAtivos--;
  }
});

app.get('/api/health', (_req, res) => res.json({ ok: true }));

app.listen(PORT, () => {
  console.log(`Verificador de Acessibilidade rodando em http://localhost:${PORT}`);
  console.log(`Página de demonstração (com falhas intencionais): http://localhost:${PORT}/demo/pagina-inacessivel.html`);
});

# Verificador de Acessibilidade Digital

Aplicativo que audita sites e landing pages de empresas quanto à conformidade com as
leis de acessibilidade digital, apontando:

- **Falhas técnicas** (motor axe-core, critérios WCAG 2.2, mensagens em português);
- **Leis afetadas e risco de sanção** — LBI (Lei 13.146/2015, art. 63), CDC (arts. 56-57),
  eMAG/Decreto 5.296/2004, European Accessibility Act (Diretiva UE 2019/882) e ADA/Unruh Act;
- **Correções recomendadas** para cada falha, em linguagem prática;
- **Pontuação 0-100 e classificação de risco jurídico** (baixo → crítico);
- **Relatório completo exportável em HTML** para compartilhar com o time ou clientes.

A própria interface do app é referência de acessibilidade: HTML semântico com landmarks,
skip link, rótulos e mensagens de erro associados aos campos, regiões `aria-live` para
status, gerenciamento de foco, contraste AA nos temas claro e escuro, foco sempre visível,
alvos de toque ≥ 44 px, unidades relativas (zoom 200% seguro) e suporte a
`prefers-reduced-motion`. O smoke test **escaneia o próprio app** e exige nota 100.

## Requisitos

- Node.js 18+ (usa `fetch` nativo nos testes)
- Chromium/Chrome instalado. O app procura automaticamente em caminhos comuns
  (Linux e Windows); se necessário, informe o caminho pela variável `CHROME_PATH`.

## Como usar

```bash
cd accessibility-checker
npm install
npm start            # http://localhost:3400
```

Abra `http://localhost:3400`, informe a URL (ex.: `https://www.suaempresa.com.br`)
e clique em **Analisar site**.

Para ver o app em ação sem depender de internet, escaneie a página de demonstração
com falhas intencionais: `http://localhost:3400/demo/pagina-inacessivel.html`.

## API

`POST /api/scan` com corpo `{ "url": "https://exemplo.com.br" }` retorna o relatório
completo em JSON: `score`, `risco`, `totais`, `violacoes[]` (cada uma com impacto,
critérios WCAG, ocorrências, exemplos de elementos, correção sugerida e leis
aplicáveis), `recomendacoes[]` e `legislacoes[]`.

## Testes

```bash
npm test
```

O smoke test sobe o servidor e verifica:

1. A página de demonstração reprova (score < 50, risco alto/crítico, falhas
   clássicas detectadas: `image-alt`, `label`, `link-name`, `html-has-lang`,
   `document-title`, `meta-viewport`), e toda violação traz leis e correção;
2. A interface do próprio app passa com **0 violações e nota 100**.

## Limitações honestas

Auditoria automática detecta tipicamente de 30% a 50% das barreiras de acessibilidade.
O relatório recomenda sempre a complementação com testes manuais (navegação por teclado,
leitor de tela, zoom 200%) e **não constitui parecer jurídico** — os valores de sanção
citados são referências das próprias leis e da prática dos órgãos fiscalizadores.

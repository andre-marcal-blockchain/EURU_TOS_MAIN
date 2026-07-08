/**
 * Base de conhecimento jurídico do Verificador de Acessibilidade.
 *
 * Mapeia falhas técnicas (regras do axe-core / critérios WCAG) para as
 * legislações de acessibilidade aplicáveis, riscos de sanção e sugestões
 * de correção em português.
 *
 * Nota: os valores de multa são referências públicas das próprias leis e
 * da prática dos órgãos fiscalizadores. Este app não substitui parecer
 * jurídico — ele aponta riscos para priorização técnica.
 */

const LEGISLACOES = {
  LBI: {
    sigla: 'LBI',
    nome: 'Lei Brasileira de Inclusão — Lei nº 13.146/2015, art. 63',
    jurisdicao: 'Brasil',
    resumo:
      'Obriga a acessibilidade nos sites da internet mantidos por empresas com sede ou ' +
      'representação comercial no Brasil, conforme as melhores práticas e diretrizes ' +
      'de acessibilidade adotadas internacionalmente (WCAG).',
    sancoes:
      'Descumprimento sujeita a empresa a ação civil pública pelo Ministério Público, ' +
      'obrigação judicial de adequação, indenização por danos morais individuais e ' +
      'coletivos, além de sanções administrativas.',
  },
  CDC: {
    sigla: 'CDC',
    nome: 'Código de Defesa do Consumidor — Lei nº 8.078/1990, arts. 6º, 56 e 57',
    jurisdicao: 'Brasil',
    resumo:
      'Site inacessível restringe o direito de acesso à informação e à contratação por ' +
      'consumidores com deficiência, caracterizando prática abusiva fiscalizável por ' +
      'Procons e Senacon.',
    sancoes:
      'Multa administrativa graduada conforme a gravidade da infração, a vantagem ' +
      'auferida e a condição econômica do fornecedor — na prática, de centenas de reais ' +
      'a valores na casa dos milhões para empresas de grande porte.',
  },
  EMAG: {
    sigla: 'eMAG/Decreto 5.296',
    nome: 'Decreto nº 5.296/2004 + eMAG (Modelo de Acessibilidade em Governo Eletrônico)',
    jurisdicao: 'Brasil (setor público)',
    resumo:
      'Portais e serviços digitais da administração pública brasileira devem seguir o ' +
      'eMAG, alinhado às WCAG.',
    sancoes:
      'Responsabilização do gestor público, recomendações e Termos de Ajustamento de ' +
      'Conduta (TAC) pelo Ministério Público.',
  },
  EAA: {
    sigla: 'EAA',
    nome: 'European Accessibility Act — Diretiva (UE) 2019/882 (exigível desde 28/06/2025)',
    jurisdicao: 'União Europeia',
    resumo:
      'E-commerce, serviços bancários, e-books, transporte e outros serviços digitais ' +
      'oferecidos a consumidores na UE devem cumprir requisitos de acessibilidade ' +
      '(norma técnica EN 301 549, baseada nas WCAG 2.1 AA).',
    sancoes:
      'Sanções definidas por cada Estado-membro: multas que podem chegar a centenas de ' +
      'milhares de euros, retirada do serviço do mercado e proibição de comercialização.',
  },
  ADA: {
    sigla: 'ADA',
    nome: 'Americans with Disabilities Act (EUA) + Unruh Act (Califórnia)',
    jurisdicao: 'Estados Unidos',
    resumo:
      'Tribunais americanos aplicam o ADA Title III a sites de empresas que atendem ' +
      'consumidores nos EUA; a Califórnia (Unruh Act) prevê indenização mínima de ' +
      'US$ 4.000 por violação.',
    sancoes:
      'Processos judiciais com acordos tipicamente entre US$ 5.000 e US$ 100.000+ ' +
      'somados aos honorários advocatícios; milhares de ações são movidas por ano.',
  },
  WCAG: {
    sigla: 'WCAG',
    nome: 'WCAG 2.1/2.2 nível AA — W3C',
    jurisdicao: 'Referência técnica internacional',
    resumo:
      'Padrão técnico referenciado por praticamente todas as legislações de ' +
      'acessibilidade digital (LBI, EAA/EN 301 549, ADA, eMAG).',
    sancoes:
      'Não é lei por si só, mas é o critério objetivo usado por peritos e ' +
      'fiscalizações para caracterizar o descumprimento legal.',
  },
};

/**
 * Sugestões de correção em português para as regras mais comuns do axe-core.
 * A descrição da falha em si já vem traduzida pelo locale pt_BR do axe.
 */
const CORRECOES = {
  'image-alt':
    'Adicione o atributo alt a todas as imagens: descritivo quando a imagem transmite ' +
    'informação (ex.: alt="Gráfico de vendas do 1º trimestre") ou vazio (alt="") quando ' +
    'for puramente decorativa.',
  'input-image-alt':
    'Adicione alt descritivo aos botões de imagem (<input type="image">) indicando a ação executada.',
  'color-contrast':
    'Ajuste as cores para contraste mínimo de 4,5:1 em texto normal e 3:1 em texto grande ' +
    '(18pt ou 14pt em negrito). Use um verificador de contraste antes de publicar a paleta.',
  'color-contrast-enhanced':
    'Para nível AAA, eleve o contraste para 7:1 em texto normal e 4,5:1 em texto grande.',
  label:
    'Associe cada campo de formulário a um rótulo visível usando <label for="id-do-campo"> ' +
    'ou, quando impossível, aria-label/aria-labelledby. Placeholder não substitui rótulo.',
  'select-name':
    'Dê um rótulo acessível a cada <select> com <label for> ou aria-label.',
  'link-name':
    'Garanta que todo link tenha texto perceptível. Links com apenas ícone precisam de ' +
    'aria-label ou texto oculto acessível. Evite textos genéricos como "clique aqui".',
  'button-name':
    'Todo botão precisa de nome acessível: texto interno, aria-label ou aria-labelledby. ' +
    'Botões só com ícone devem receber aria-label descrevendo a ação.',
  'html-has-lang':
    'Declare o idioma da página no elemento raiz: <html lang="pt-BR">. Leitores de tela ' +
    'usam esse atributo para escolher a voz e a pronúncia corretas.',
  'html-lang-valid':
    'Corrija o valor do atributo lang para um código BCP 47 válido (ex.: "pt-BR", "en").',
  'valid-lang':
    'Use códigos de idioma válidos (BCP 47) nos trechos com lang diferente do idioma da página.',
  'document-title':
    'Defina um <title> único e descritivo para cada página (ex.: "Carrinho — Loja X"). ' +
    'É a primeira informação anunciada por leitores de tela.',
  'meta-viewport':
    'Remova user-scalable=no e maximum-scale do meta viewport. Impedir o zoom bloqueia ' +
    'pessoas com baixa visão — use <meta name="viewport" content="width=device-width, initial-scale=1">.',
  'heading-order':
    'Organize os títulos em hierarquia lógica (h1 → h2 → h3) sem pular níveis. Títulos são ' +
    'o principal mecanismo de navegação de quem usa leitor de tela.',
  'empty-heading':
    'Remova títulos vazios ou insira texto neles — títulos sem conteúdo confundem a navegação por cabeçalhos.',
  'page-has-heading-one':
    'Inclua exatamente um <h1> descrevendo o conteúdo principal da página.',
  region:
    'Envolva todo o conteúdo em landmarks HTML5/ARIA (<header>, <nav>, <main>, <footer>), ' +
    'permitindo pular direto para cada região da página.',
  'landmark-one-main':
    'Adicione um único elemento <main> envolvendo o conteúdo principal.',
  bypass:
    'Ofereça um "skip link" ("Pular para o conteúdo") como primeiro elemento focável da ' +
    'página, permitindo que usuários de teclado saltem menus repetitivos.',
  'frame-title':
    'Adicione title descritivo a todo <iframe> (ex.: title="Mapa da loja no Google Maps").',
  list:
    'Dentro de <ul>/<ol> use apenas <li> (e script/template). Estruturas de lista quebradas ' +
    'confundem a contagem de itens anunciada pelos leitores de tela.',
  listitem: 'Coloque todos os <li> dentro de um <ul>, <ol> ou role="list".',
  'definition-list': 'Estruture <dl> apenas com grupos de <dt> e <dd> corretamente ordenados.',
  tabindex:
    'Evite tabindex maior que 0 — ele quebra a ordem natural de navegação. Use a ordem do ' +
    'DOM e tabindex="0"/"−1" apenas quando necessário.',
  'duplicate-id-aria':
    'Elimine IDs duplicados referenciados por ARIA/labels — cada id deve ser único na página.',
  'aria-allowed-attr': 'Remova atributos ARIA não permitidos para a role do elemento.',
  'aria-required-attr': 'Adicione os atributos ARIA obrigatórios da role utilizada (ex.: aria-checked em role="checkbox").',
  'aria-required-children': 'Inclua os elementos filhos obrigatórios da role (ex.: role="list" exige filhos role="listitem").',
  'aria-required-parent': 'Coloque o elemento dentro do pai exigido pela sua role.',
  'aria-roles': 'Corrija valores de role inválidos — use apenas roles definidas na especificação ARIA.',
  'aria-valid-attr': 'Corrija atributos aria-* com nomes inexistentes (provável erro de digitação).',
  'aria-valid-attr-value': 'Corrija valores inválidos de atributos ARIA (ex.: aria-hidden="yes" → "true").',
  'aria-hidden-body': 'Nunca aplique aria-hidden="true" ao <body> — isso oculta a página inteira da tecnologia assistiva.',
  'aria-hidden-focus':
    'Elementos com aria-hidden="true" não podem conter itens focáveis. Remova-os do fluxo ' +
    'de foco (tabindex="-1") ou retire o aria-hidden.',
  'aria-command-name': 'Dê nome acessível (texto, aria-label ou aria-labelledby) a elementos com role de botão/link/menuitem.',
  'aria-input-field-name': 'Dê nome acessível aos campos ARIA (combobox, listbox, searchbox etc.).',
  'nested-interactive':
    'Não aninhe controles interativos (ex.: botão dentro de link). Separe-os — controles ' +
    'aninhados ficam inoperáveis por teclado e leitores de tela.',
  'scrollable-region-focusable':
    'Regiões com rolagem precisam ser alcançáveis por teclado: adicione tabindex="0" ou ' +
    'coloque elementos focáveis dentro delas.',
  'autocomplete-valid':
    'Use valores válidos de autocomplete (ex.: "email", "name", "tel") — eles permitem ' +
    'preenchimento assistido para pessoas com deficiência motora ou cognitiva.',
  'video-caption': 'Forneça legendas sincronizadas (<track kind="captions">) para todo vídeo com áudio.',
  'audio-caption': 'Forneça transcrição ou legenda para conteúdo de áudio pré-gravado.',
  blink: 'Remova o elemento <blink> — conteúdo piscante é proibido e pode provocar crises convulsivas.',
  marquee: 'Remova o elemento <marquee> — texto em movimento contínuo é inacessível.',
  'meta-refresh': 'Remova o redirecionamento/refresh automático por <meta http-equiv="refresh"> ou dê controle ao usuário.',
  'object-alt': 'Forneça texto alternativo para elementos <object>.',
  'svg-img-alt': 'Adicione <title> ou aria-label a SVGs com role="img".',
  'td-headers-attr': 'Corrija o atributo headers das células para referenciar apenas IDs de <th> da mesma tabela.',
  'th-has-data-cells': 'Garanta que cada cabeçalho <th> descreva células de dados na tabela.',
  'form-field-multiple-labels': 'Deixe apenas um <label> por campo — múltiplos rótulos são anunciados de forma imprevisível.',
  'link-in-text-block':
    'Diferencie links do texto ao redor com sublinhado ou contraste de cor de pelo menos ' +
    '3:1 — cor sozinha não pode ser o único indicador.',
  'target-size':
    'Aumente áreas de toque para no mínimo 24×24 px (WCAG 2.2) — idealmente 44×44 px — ' +
    'ou garanta espaçamento suficiente entre alvos.',
};

/** Grupos de regras → legislações mais diretamente implicadas. */
function leisAplicaveis(ruleId, tags) {
  const leis = new Set(['WCAG', 'LBI']); // toda falha WCAG afeta LBI no Brasil
  const t = new Set(tags);

  // Falhas que bloqueiam compra/contratação → CDC e EAA com força total
  const bloqueiaTransacao = [
    'label', 'select-name', 'button-name', 'link-name', 'autocomplete-valid',
    'nested-interactive', 'aria-input-field-name', 'form-field-multiple-labels',
  ];
  if (bloqueiaTransacao.includes(ruleId)) {
    leis.add('CDC');
    leis.add('EAA');
  }
  if (t.has('wcag2a') || t.has('wcag2aa') || t.has('wcag21aa') || t.has('wcag22aa')) {
    leis.add('EAA');
    leis.add('ADA');
  }
  // Conteúdo essencial inacessível → CDC (informação adequada e clara)
  if (['image-alt', 'color-contrast', 'video-caption', 'meta-viewport', 'document-title'].includes(ruleId)) {
    leis.add('CDC');
  }
  return [...leis];
}

function correcaoPara(violation) {
  return (
    CORRECOES[violation.id] ||
    `${violation.help}. Consulte o guia técnico oficial: ${violation.helpUrl}`
  );
}

/** Classificação de risco jurídico global a partir do resultado do scan. */
function avaliarRisco(score, contagemPorImpacto) {
  const criticas = contagemPorImpacto.critical || 0;
  const serias = contagemPorImpacto.serious || 0;

  if (score >= 95 && criticas === 0 && serias === 0) {
    return {
      nivel: 'baixo',
      rotulo: 'Risco jurídico baixo',
      descricao:
        'A página está substancialmente aderente às WCAG. Mantenha auditorias periódicas ' +
        'e valide também com testes manuais (teclado e leitor de tela), pois ferramentas ' +
        'automáticas cobrem apenas parte dos critérios.',
    };
  }
  if (score >= 75 && criticas === 0) {
    return {
      nivel: 'moderado',
      rotulo: 'Risco jurídico moderado',
      descricao:
        'Há falhas de conformidade que podem fundamentar reclamações em Procon e ' +
        'notificações extrajudiciais. A correção é geralmente simples — priorize as ' +
        'falhas sérias antes que gerem registro formal.',
    };
  }
  if (score >= 45) {
    return {
      nivel: 'alto',
      rotulo: 'Risco jurídico alto',
      descricao:
        'O volume de falhas caracteriza descumprimento do art. 63 da LBI. A empresa está ' +
        'exposta a multas administrativas (CDC, arts. 56-57), ação civil pública e dano ' +
        'reputacional — casos de inacessibilidade viralizam com frequência nas redes.',
    };
  }
  return {
    nivel: 'critico',
    rotulo: 'Risco jurídico crítico',
    descricao:
      'A página exclui na prática usuários com deficiência — cenário típico das ações ' +
      'civis públicas e condenações por dano moral coletivo já registradas no Brasil, ' +
      'além de multas que escalam com o porte da empresa. Recomenda-se plano de ' +
      'remediação imediato com prazos e responsáveis definidos.',
  };
}

const IMPACTO_LABEL = {
  critical: { pt: 'Crítica', peso: 12 },
  serious: { pt: 'Séria', peso: 7 },
  moderate: { pt: 'Moderada', peso: 3 },
  minor: { pt: 'Leve', peso: 1 },
};

module.exports = { LEGISLACOES, leisAplicaveis, correcaoPara, avaliarRisco, IMPACTO_LABEL };

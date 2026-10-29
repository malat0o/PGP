// Gera os slides da apresentação da Etapa 1
// Uso: node slides.js <pasta etapa1> <saida.pptx> <grupo>
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");
// apply_theme.js (opcional) escreve as cores do tema no .pptx; sem ele usa-se a paleta por omissão
let applyTheme = async () => {};
try { ({ applyTheme } = require("./apply_theme.js")); } catch (e) { console.warn("apply_theme.js não encontrado: tema por omissão"); }

const [E, OUT, GRUPO] = process.argv.slice(2);

const THEME = {
  name: "Vinil",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "18181B", lt1: "FFFFFF", dk2: "3F3F46", lt2: "F4F4F5",
    accent1: "B91C1C", accent2: "F59E0B", accent3: "15803D", accent4: "1D4ED8", accent5: "7E22CE", accent6: "71717A",
    hlink: "B91C1C", folHlink: "7F1D1D",
  },
};
const T = THEME.colors;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "PGP 2026/27 · Etapa 1";
const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: "CAPA",
  background: { color: T.dk1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.2, w: 8.6, h: 1.9, fontSize: 40, bold: true, color: C.background1, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.3, w: 8.6, h: 2.2, fontSize: 18, color: "D4D4D8", valign: "top", align: "left", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTEUDO",
  background: { color: T.lt1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 10.6, h: 0.9, fontSize: 32, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: `PGP 2026/27 · Grupo ${GRUPO} · Etapa 1`, options: { x: 0.6, y: 7.05, w: 6, h: 0.3, fontSize: 10, color: "71717A", margin: 0 } } },
  ],
  slideNumber: { x: 12.3, y: 7.05, w: 0.5, h: 0.3, fontSize: 10, color: "71717A", align: "right" },
});

function png(p) { const b = fs.readFileSync(p); return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) }; }
function fit(slide, rel, x, y, w, h, name) {
  const p = path.join(E, rel); const s = png(p);
  const r = Math.min(w / s.w, h / s.h); const iw = s.w * r, ih = s.h * r;
  slide.addImage({ path: p, x: x + (w - iw) / 2, y: y + (h - ih) / 2, w: iw, h: ih, objectName: name,
    shadow: { type: "outer", color: "000000", opacity: 0.18, blur: 6, offset: 2, angle: 90 } });
}
// Motivo visual: um "disco" (círculo escuro com centro vermelho) com o nome de quem apresenta
function presenter(slide, nome) {
  slide.addShape(pres.shapes.OVAL, { x: 11.55, y: 0.45, w: 0.7, h: 0.7, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "disco" });
  slide.addShape(pres.shapes.OVAL, { x: 11.77, y: 0.67, w: 0.26, h: 0.26, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "disco-centro" });
  slide.addText(nome, { x: 10.3, y: 1.2, w: 2.5, h: 0.3, fontSize: 12, color: C.text2, align: "right", italic: true, isTextBox: true, margin: 0, objectName: "apresentador" });
}
function card(slide, x, y, w, h, title, body, color) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: C.background2 }, line: { color: "E4E4E7" }, objectName: "cartao" });
  slide.addShape(pres.shapes.OVAL, { x: x + 0.25, y: y + 0.28, w: 0.22, h: 0.22, fill: { color }, line: { color }, objectName: "marca" });
  slide.addText(title, { x: x + 0.6, y: y + 0.18, w: w - 0.8, h: 0.42, fontSize: 16, bold: true, color: C.text1, isTextBox: true, margin: 0, valign: "middle" });
  slide.addText(body, { x: x + 0.6, y: y + 0.62, w: w - 0.8, h: h - 0.75, fontSize: 16, color: C.text2, isTextBox: true, margin: 0, valign: "top" });
}
function steps(slide, x, y, w, items, gap = 0.95) {
  items.forEach((t, i) => {
    slide.addShape(pres.shapes.OVAL, { x, y: y + i * gap, w: 0.5, h: 0.5, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "passo" });
    slide.addText(String(i + 1), { x, y: y + i * gap, w: 0.5, h: 0.5, fontSize: 16, bold: true, color: C.background1, align: "center", valign: "middle", isTextBox: true, margin: 0 });
    slide.addText(t, { x: x + 0.7, y: y + i * gap - 0.05, w: w - 0.7, h: 0.6, fontSize: 15, color: C.text1, valign: "middle", isTextBox: true, margin: 0 });
  });
}
function stat(slide, x, y, num, label) {
  slide.addText(num, { x, y, w: 2.6, h: 1.0, fontSize: 60, bold: true, color: C.accent1, fontFace: "Cambria", isTextBox: true, margin: 0 });
  slide.addText(label, { x, y: y + 1.0, w: 2.6, h: 0.5, fontSize: 14, color: C.text2, isTextBox: true, margin: 0 });
}
const sec = t => pres.addSection({ title: t });

// 1 Capa
sec("Abertura");
let s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Abertura" });
s.addText("Gestão de coleções de álbuns físicos", { placeholder: "title" });
s.addText([
  { text: "Etapa 1 — Desenho inicial e pesquisa de tecnologias", options: { breakLine: true } },
  { text: " ", options: { breakLine: true } },
  { text: `Grupo ${GRUPO} · Rodrigo, Reis, Miguel, Ze, Edson`, options: { breakLine: true } },
  { text: "Planeamento e Gestão de Projeto 2026/27" },
], { placeholder: "body" });
s.addShape(pres.shapes.OVAL, { x: 9.6, y: 1.6, w: 4.6, h: 4.6, fill: { color: "27272A" }, line: { color: "3F3F46", width: 2 }, objectName: "disco-grande" });
s.addShape(pres.shapes.OVAL, { x: 10.3, y: 2.3, w: 3.2, h: 3.2, fill: { color: "27272A" }, line: { color: "3F3F46", width: 1 }, objectName: "sulco" });
s.addShape(pres.shapes.OVAL, { x: 11.35, y: 3.35, w: 1.1, h: 1.1, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "rotulo" });
s.addShape(pres.shapes.OVAL, { x: 11.83, y: 3.83, w: 0.14, h: 0.14, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "furo" });
s.addNotes("Reis abre a apresentação: apresenta o grupo e diz que vão mostrar o desenho inicial da aplicação e a pesquisa de tecnologias. Cada pessoa apresenta a parte que fez.");

// 2 O problema
sec("Casos de uso");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Casos de uso" });
s.addText("Uma loja de música que também gere coleções", { placeholder: "title" });
presenter(s, "Reis");
s.addText([
  { text: "Os utilizadores registam os álbuns físicos que têm (CD, vinil, cassete), compram na loja e organizam listas.", options: { bullet: true, breakLine: true } },
  { text: "O gestor gere o catálogo, o stock e os pedidos de novas versões.", options: { bullet: true, breakLine: true } },
  { text: "Aplicação web de três camadas, com a stack MEAN: Angular, Express, Node.js e MongoDB.", options: { bullet: true } },
], { x: 0.6, y: 1.7, w: 6.4, h: 3.6, fontSize: 18, color: C.text1, paraSpaceAfter: 14, valign: "top", isTextBox: true, margin: 0 });
stat(s, 7.6, 1.8, "29", "user stories");
stat(s, 10.3, 1.8, "21", "casos de uso");
stat(s, 7.6, 4.0, "2", "atores humanos");
stat(s, 10.3, 4.0, "5", "serviços externos");
s.addNotes("Reis: explica o problema em duas frases e a escolha da stack MEAN (a sugerida no enunciado). Os números à direita resumem a dimensão do projeto: 29 user stories agrupadas em 21 casos de uso.");

// 2b Âmbito e modelo de processo
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Casos de uso" });
s.addText("Âmbito do produto e porquê Scrum", { placeholder: "title" });
presenter(s, "Reis");
s.addText("Pressupostos (estimativas da equipa)", { x: 0.6, y: 1.6, w: 5.6, h: 0.4, fontSize: 18, bold: true, color: C.text1, isTextBox: true, margin: 0 });
s.addText([
  { text: "1 000 utilizadores registados, até 50 em simultâneo", options: { bullet: true, breakLine: true } },
  { text: "2 000 álbuns e 4 000 versões no catálogo", options: { bullet: true, breakLine: true } },
  { text: "Páginas em até 2 s; sugestões da pesquisa em até 300 ms (RNF-08)", options: { bullet: true, breakLine: true } },
  { text: "Backend sem estado, para poder acrescentar nós (RNF-10)", options: { bullet: true, breakLine: true } },
  { text: "Restrições: MEAN, custo gratuito, Nominatim a 1 pedido/s, pagamentos só em teste", options: { bullet: true } },
], { x: 0.6, y: 2.1, w: 5.6, h: 4.2, fontSize: 15, color: C.text1, paraSpaceAfter: 10, valign: "top", isTextBox: true, margin: 0 });
card(s, 6.6, 1.6, 3.0, 2.3, "Cliente", "Participativo: demonstrações no fim de março, abril e maio.", C.accent1);
card(s, 9.75, 1.6, 3.0, 2.3, "Pessoas", "Equipa de 5, dentro dos 3 a 9 do Scrum.", C.accent1);
card(s, 6.6, 4.1, 3.0, 2.3, "Produto", "Requisitos podem mudar: o cliente pode pedir alterações.", C.accent1);
card(s, 9.75, 4.1, 3.0, 2.3, "Ambiente", "Semestre com 3 sprints de cerca de um mês.", C.accent1);
s.addText("A cascata exige requisitos estáveis e só entrega no fim; o Scrum entrega em cada sprint e reordena o backlog.", { x: 6.6, y: 6.5, w: 6.15, h: 0.45, fontSize: 12, italic: true, color: C.text2, isTextBox: true, margin: 0 });
s.addNotes("Reis: o enunciado não dá volumes nem tempos, por isso a equipa assumiu valores (são estimativas, a confirmar com o cliente) que servem de referência às RNF-08 e RNF-10. Porquê Scrum: cliente participativo com demonstrações em cada sprint, equipa de 5, requisitos que podem mudar e um semestre com 3 sprints de cerca de um mês. A cascata não serve porque exige requisitos estáveis e só entrega no fim. O gestor de projeto faz parcialmente de Product Owner: ordena as user stories e distribui-as pelos sprints.");

// 3 Casos de uso
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Casos de uso" });
s.addText("Casos de uso: um diagrama por ator", { placeholder: "title" });
presenter(s, "Reis");
fit(s, "casos-uso/img/casos-uso-utilizador.png", 0.6, 1.4, 4.3, 5.5, "diagrama-utilizador");
fit(s, "casos-uso/img/casos-uso-gestor.png", 5.2, 1.6, 4.4, 2.7, "diagrama-gestor");
s.addText([
  { text: "Um só diagrama com 21 casos de uso tinha linhas cruzadas por todo o lado: dividimos por ator.", options: { bullet: true, breakLine: true } },
  { text: "Serviços externos ligados aos casos de uso que os usam: mapas, geocodificação e pagamentos.", options: { bullet: true, breakLine: true } },
  { text: "As 29 user stories estão todas cobertas (matriz US↔UC).", options: { bullet: true } },
], { x: 5.2, y: 4.6, w: 7.5, h: 2.2, fontSize: 15, color: C.text1, paraSpaceAfter: 8, valign: "top", isTextBox: true, margin: 0 });
s.addNotes("Reis: o utilizador tem 16 casos de uso, o gestor 7; 'Iniciar sessão' e 'Visualizar página de álbum' são comuns. User stories sobre os mesmos dados foram agrupadas (ex.: Gerir coleção = US10 + US11). Duas relações «extend»: Gerir artista favorito estende Visualizar página de artista, e Gerir stock estende Visualizar página de álbum (o gestor altera o stock a partir dessa página, US25 a).");

// 4 Modelo: visão geral
sec("Modelo de dados");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Modelo de dados" });
s.addText("Modelo de dados: 19 classes em 5 grupos", { placeholder: "title" });
presenter(s, "Rodrigo");
fit(s, "classes/img/01-topo.png", 0.6, 1.5, 12.1, 4.7, "diagrama-topo");
s.addText([
  { text: "A classe central é a ", options: {} },
  { text: "VersaoAlbum", options: { bold: true, color: C.accent1 } },
  { text: ": o álbum num suporte concreto, com EAN-13. É o que se compra, coleciona e tem stock." },
], { x: 0.6, y: 6.3, w: 12.1, h: 0.6, fontSize: 16, color: C.text1, isTextBox: true, margin: 0 });
s.addNotes("Rodrigo: diagrama de topo, só classes e associações, com uma cor por grupo (catálogo azul, loja verde, utilizadores amarelo, coleções roxo, pedidos vermelho). Sublinhar que a VersaoAlbum é o centro do modelo.");

// 5 Modelo: decisões
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Modelo de dados" });
s.addText("Quatro decisões que explicam o modelo", { placeholder: "title" });
presenter(s, "Rodrigo");
fit(s, "classes/img/02-catalogo.png", 0.6, 1.5, 4.6, 5.4, "diagrama-catalogo");
card(s, 5.6, 1.6, 3.4, 2.4, "Solista e Grupo", "Subclasses de Artista. Os membros de um grupo só podem ser solistas, por isso um grupo nunca contém grupos.", C.accent4);
card(s, 9.3, 1.6, 3.4, 2.4, "Faixa", "Classe própria: a mesma canção aparece em vários álbuns, com números diferentes.", C.accent4);
card(s, 5.6, 4.3, 3.4, 2.4, "Versão ≠ Álbum", "O mesmo álbum existe em CD, vinil e várias edições. Coleção e carrinho guardam versões; listas guardam álbuns.", C.accent3);
card(s, 9.3, 4.3, 3.4, 2.4, "Disponibilidade", "Opcional: distingue \"nunca esteve na loja\", \"disponível\" e \"esgotado\".", C.accent3);
s.addNotes("Rodrigo: explicar as quatro decisões. Exemplo do enunciado: 'Last Resort' está no 'Infest' e no 'Now 4' — por isso a Faixa é uma classe. Se perguntarem pelo preço na fatura: guarda-se o preço pago porque o preço na loja pode mudar.");

// 6 Restrições
sec("Restrições e serviços");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Restrições e serviços" });
s.addText("Restrições de integridade", { placeholder: "title" });
presenter(s, "Ze");
stat(s, 0.6, 1.7, "30", "do enunciado");
stat(s, 0.6, 3.6, "+21", "novas, cada uma com origem");
s.addTable([
  [{ text: "ID", options: { bold: true, fill: { color: "E4E4E7" } } }, { text: "Restrição nova", options: { bold: true, fill: { color: "E4E4E7" } } }, { text: "Origem", options: { bold: true, fill: { color: "E4E4E7" } } }],
  ["RI-31", "Um grupo só tem solistas como membros", "Universo do discurso"],
  ["RI-40", "No máximo um artista favorito", "US7 c)"],
  ["RI-41", "Cada versão só uma vez na coleção", "US10 c)"],
  ["RI-44", "Estados do pedido: em análise, aceite, recusado", "US13 d), US24 b)"],
  ["RI-46", "Só vai para o carrinho o que tem stock", "US26 a)"],
], { x: 3.8, y: 1.7, w: 8.9, colW: [1.1, 5.0, 2.8], fontSize: 14, color: C.text1, border: { type: "solid", pt: 0.75, color: "D4D4D8" }, rowH: 0.55, valign: "middle", objectName: "tabela-restricoes" });
s.addText("Todas as 51 restrições estão associadas a uma classe do modelo (Anexo A do relatório).", { x: 3.8, y: 5.4, w: 8.9, h: 0.5, fontSize: 14, italic: true, color: C.text2, isTextBox: true, margin: 0 });
s.addNotes("Ze: as 30 restrições do enunciado estão nas notas dos diagramas. Encontrámos mais 21 lendo os critérios de aceitação das user stories — nenhuma foi inventada, cada uma tem a frase de origem. Exemplos na tabela.");

// 7 Serviços externos
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Restrições e serviços" });
s.addText("Serviços externos escolhidos", { placeholder: "title" });
presenter(s, "Ze");
card(s, 0.6, 1.8, 3.9, 3.7, "Mapas: Leaflet + OSM", "Gratuito, sem cartão de crédito e de código aberto (RNF-05).\n\nComparado com Google Maps (10 000 carregamentos grátis/mês) e Mapbox.", C.accent3);
card(s, 4.72, 1.8, 3.9, 3.7, "Geocodificação: Nominatim", "O único que deixa guardar as coordenadas na base de dados de graça.\n\nCuidados: 1 pedido por morada, sem auto-complete, sem enviar o nome.", C.accent3);
card(s, 8.84, 1.8, 3.9, 3.7, "Pagamentos: Stripe + PayPal", "A US28 obriga a deixar o utilizador escolher o serviço.\n\nStripe: 1,5% + 0,25 € e MB WAY. PayPal: para quem paga com a conta. Ambos com modo de testes.", C.accent1);
s.addText([
  { text: "Também pesquisados: ", options: { bold: true } },
  { text: "imagens de capa no Cloudinary, com sugestão do Cover Art Archive pelo MBID; faixas e canções importadas da API do MusicBrainz (dados CC0)." },
], { x: 0.6, y: 5.8, w: 12.1, h: 0.6, fontSize: 15, color: C.text1, isTextBox: true, margin: 0, objectName: "outros-servicos" });
s.addNotes("Ze: cada escolha foi comparada com concorrentes, com preços consultados a 27/out/2026. Argumento principal do Nominatim: o modelo guarda as coordenadas na Morada, e Google/Mapbox restringem ou cobram isso. Dois serviços de pagamento porque a US28 b) pede escolha.");

// 8 Fluxo de compra
sec("Fluxos");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Fluxos" });
s.addText("Fluxo de compra: o pagamento", { placeholder: "title" });
presenter(s, "Edson");
fit(s, "atividades/img/01-1-pagar.png", 0.6, 1.4, 3.6, 5.55, "diagrama-pagar");
steps(s, 4.8, 1.8, 7.9, [
  "Reserva as unidades; se uma versão esgotou entretanto, sai do carrinho",
  "O utilizador escolhe Stripe ou PayPal e paga na página do serviço",
  "Espera pelo resultado (US28 c); sem resposta no tempo limite, liberta a reserva",
  "Sucesso: emite a fatura; coleção e stock atualizados em paralelo (fork/join)",
  "Falha: tentar com outro serviço ou cancelar (US28 g)",
]);
s.addNotes("Edson: a compra tem um diagrama de alto nível (pesquisa → carrinho → pagar) e o pagamento está decomposto numa subatividade, como pede o enunciado. Raias: utilizador, aplicação, serviço de pagamentos. Notação UML: decisões em losango com guardas [ ], barras de fork/join. A reserva das unidades resolve o caso de dois utilizadores a comprarem a última unidade ao mesmo tempo.");

// 9 Pedido de nova versão
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Fluxos" });
s.addText("Pedido de nova versão: três atores", { placeholder: "title" });
presenter(s, "Edson");
fit(s, "atividades/img/02-pedido-nova-versao.png", 0.6, 1.4, 4.0, 5.55, "diagrama-pedido");
steps(s, 5.1, 1.9, 7.6, [
  "O utilizador pede uma versão nova de um álbum (US12)",
  "O pedido fica \"em análise\" até o gestor decidir",
  "O gestor aceita (a versão é criada) ou recusa (US24)",
  "O utilizador recebe uma notificação no dashboard (US14)",
], 1.15);
s.addNotes("Edson: este fluxo junta quatro user stories e três atores. Se aceite, a versão aparece logo na página do álbum e o utilizador pode adicioná-la à coleção. Há mais dois fluxos no relatório: criar conta/iniciar sessão e gerir o catálogo.");

// 10 Esboço: página de álbum
sec("Esboços");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Esboços" });
s.addText("Página de álbum: cinco user stories num ecrã", { placeholder: "title" });
presenter(s, "Miguel");
fit(s, "esbocos/img/E01-pagina-album.png", 0.6, 1.5, 8.2, 5.4, "esboco-album");
s.addText([
  { text: "Uma linha por versão, com o estado na loja: disponível, esgotada ou nunca vendida", options: { bullet: true, breakLine: true } },
  { text: "Carrinho só ativo com stock", options: { bullet: true, breakLine: true } },
  { text: "Coluna extra só para o gestor alterar unidades", options: { bullet: true, breakLine: true } },
  { text: "Notas amarelas ligam cada elemento à sua user story", options: { bullet: true } },
], { x: 9.1, y: 1.7, w: 3.6, h: 5.0, fontSize: 15, color: C.text1, paraSpaceAfter: 12, valign: "top", isTextBox: true, margin: 0 });
s.addNotes("Miguel: fizemos 12 esboços de baixa fidelidade; este é o mais complexo. Os botões 'Coleção' e 'Carrinho' atuam sobre a versão; 'Adicionar a uma lista' atua sobre o álbum.");

// 11 Esboço: carrinho + telemóvel
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Esboços" });
s.addText("Carrinho, pagamento e telemóvel", { placeholder: "title" });
presenter(s, "Miguel");
fit(s, "esbocos/img/E02-carrinho-pagamento.png", 0.6, 1.5, 8.6, 5.4, "esboco-carrinho");
fit(s, "esbocos/img/E12-telemovel-carrinho.png", 9.6, 1.5, 3.1, 5.4, "esboco-telemovel");
s.addNotes("Miguel: no carrinho os itens mais recentes aparecem primeiro; ao pagar escolhe-se o serviço e aparecem mensagens de sucesso ou falha. À direita a versão para telemóvel (RNF-04): tabelas passam a cartões e o botão Pagar fica fixo no fundo.");

// 12 Dúvidas e suposições
sec("Fecho");
s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Fecho" });
s.addText("O que perguntámos e o que assumimos", { placeholder: "title" });
presenter(s, "Reis");
s.addTable([
  [{ text: "Questão", options: { bold: true, fill: { color: "E4E4E7" } } }, { text: "Suposição até haver resposta", options: { bold: true, fill: { color: "E4E4E7" } } }],
  ["US28 f) está incompleta", "Regista-se a data da última venda (RI-17)"],
  ["\"Recusado\" (US13/14) ou \"rejeitado\" (US24)?", "Usamos \"recusado\""],
  ["US3 mostra a palavra-passe, a RNF-12 manda cifrá-la", "Guardada cifrada, mostrada mascarada"],
  ["Nenhuma user story regista as canções", "Importação em bloco (nota 12)"],
  ["Sem quantidades no carrinho", "Cada linha é uma unidade de uma versão"],
], { x: 0.6, y: 1.7, w: 12.1, colW: [6.0, 6.1], fontSize: 15, color: C.text1, border: { type: "solid", pt: 0.75, color: "D4D4D8" }, rowH: 0.62, valign: "middle", objectName: "tabela-suposicoes" });
s.addNotes("Reis: mostrar que lemos o enunciado com atenção — encontrámos pontos ambíguos, perguntámos ao professor e documentámos o que assumimos.");

// 13 Fim
s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Fecho" });
s.addText("Obrigado", { placeholder: "title" });
s.addText([{ text: "Perguntas?", options: { breakLine: true } }, { text: " ", options: { breakLine: true } }, { text: "Relatório completo e todos os diagramas no repositório do grupo." }], { placeholder: "body" });
s.addShape(pres.shapes.OVAL, { x: 9.6, y: 1.6, w: 4.6, h: 4.6, fill: { color: "27272A" }, line: { color: "3F3F46", width: 2 }, objectName: "disco-grande" });
s.addShape(pres.shapes.OVAL, { x: 10.3, y: 2.3, w: 3.2, h: 3.2, fill: { color: "27272A" }, line: { color: "3F3F46", width: 1 }, objectName: "sulco" });
s.addShape(pres.shapes.OVAL, { x: 11.35, y: 3.35, w: 1.1, h: 1.1, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "rotulo" });
s.addShape(pres.shapes.OVAL, { x: 11.83, y: 3.83, w: 0.14, h: 0.14, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "furo" });
s.addNotes("Todos: perguntas. Cada pessoa responde sobre a sua parte.");

pres.writeFile({ fileName: OUT }).then(async () => { await applyTheme(OUT, THEME); console.log("ok", OUT); });

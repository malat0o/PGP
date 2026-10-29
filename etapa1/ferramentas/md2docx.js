// Converte o relatório em Markdown (subconjunto simples) para .docx
// Uso: node md2docx.js relatorio.md saida.docx grupo
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, PageBreak, TableOfContents, Footer, Header, PageNumber, LevelFormat,
  ExternalHyperlink,
} = require("docx");

const [mdPath, outPath, grupo] = process.argv.slice(2);
const baseDir = path.dirname(mdPath);
const lines = fs.readFileSync(mdPath, "utf8").replace(/\r/g, "").split("\n");

const FONT = "Calibri";
const CONTENT_W = 9026; // A4 com margens de 2,54 cm, em DXA
const MAX_W_PX = 600, MAX_H_PX = 820;

function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20), data: b };
}

// **negrito**, *itálico*, `código`, URLs
function inline(text, base = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|https?:\/\/\S+)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith("**")) runs.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith("`")) runs.push(new TextRun({ text: t.slice(1, -1), font: "Consolas", ...base }));
    else if (t.startsWith("http")) runs.push(new ExternalHyperlink({ link: t, children: [new TextRun({ text: t, style: "Hyperlink", ...base })] }));
    else runs.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...base }));
  return runs;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: "9CA3AF" };
const borders = { top: border, bottom: border, left: border, right: border };

function table(rows) {
  const cells = rows.map(r => r.replace(/^\||\|$/g, "").split("|").map(c => c.trim()));
  const header = cells[0], body = cells.slice(2);
  const n = header.length;
  const lens = header.map((_, i) => Math.max(...[header, ...body].map(r => (r[i] || "").length)));
  const weights = lens.map(l => Math.max(9, Math.min(l + 3, 60)));
  const sum = weights.reduce((a, b) => a + b, 0);
  const widths = weights.map(w => Math.floor((w / sum) * CONTENT_W));
  widths[n - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const mk = (r, head) => new TableRow({
    tableHeader: head,
    children: r.map((c, i) => new TableCell({
      borders, width: { size: widths[i], type: WidthType.DXA },
      shading: head ? { fill: "E5E7EB", type: ShadingType.CLEAR, color: "auto" } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: inline(c, { size: 19, bold: head || undefined }) })],
    })),
  });
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, rows: [mk(header, true), ...body.map(r => mk(r, false))] });
}

const children = [];
let h1 = 0, h2 = 0, numInst = 0, lastNumLine = -2;
for (let i = 0; i < lines.length; i++) {
  const l = lines[i];
  if (!l.trim()) continue;
  if (l.startsWith("# ")) {
    const t = l.slice(2);
    const numbered = !/^(Anexo|Referências)/.test(t);
    if (numbered) { h1++; h2 = 0; }
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun(numbered ? `${h1}  ${t}` : t)] }));
  } else if (l.startsWith("## ")) {
    h2++;
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`${h1}.${h2}  ${l.slice(3)}`)] }));
  } else if (l.startsWith("|")) {
    const rows = [];
    while (i < lines.length && lines[i].startsWith("|")) rows.push(lines[i++]);
    i--;
    children.push(table(rows));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  } else if (/^!\[/.test(l)) {
    const m = l.match(/^!\[(.*)\]\((.*)\)$/);
    const img = pngSize(path.resolve(baseDir, m[2]));
    let w = MAX_W_PX, h = Math.round(img.h * (MAX_W_PX / img.w));
    if (h > MAX_H_PX) { h = MAX_H_PX; w = Math.round(img.w * (MAX_H_PX / img.h)); }
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 120, after: 60 }, children: [new ImageRun({ type: "png", data: img.data, transformation: { width: w, height: h } })] }));
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [new TextRun({ text: m[1], italics: true, size: 19, color: "374151" })] }));
  } else if (/^\d+\. /.test(l)) {
    children.push(new Paragraph({ numbering: { reference: "num", level: 0, instance: (lastNumLine === i - 1 ? numInst : ++numInst) + 0 * (lastNumLine = i) }, children: inline(l.replace(/^\d+\. /, "")) }));
  } else if (l.startsWith("- ")) {
    children.push(new Paragraph({ numbering: { reference: "bul", level: 0 }, children: inline(l.slice(2)) }));
  } else if (/^\*\*Tabela/.test(l)) {
    children.push(new Paragraph({ keepNext: true, spacing: { before: 160, after: 80 }, children: [new TextRun({ text: l.replace(/\*\*/g, ""), italics: true, size: 19, color: "374151" })] }));
  } else {
    children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, children: inline(l) }));
  }
}

const membros = ["Rodrigo", "Reis", "Miguel", "Ze", "Edson"];
const capa = [
  new Paragraph({ spacing: { before: 2400 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Planeamento e Gestão de Projeto", size: 32, color: "374151" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "2026/2027", size: 26, color: "6B7280" })] }),
  new Paragraph({ spacing: { before: 1200 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Gestão de coleções de álbuns de música em formato físico", bold: true, size: 44 })] }),
  new Paragraph({ spacing: { before: 400 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Etapa 1 — Desenho inicial e pesquisa de tecnologias", size: 30 })] }),
  new Paragraph({ spacing: { before: 1600 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: `Grupo ${grupo}`, bold: true, size: 26 })] }),
  ...membros.map(n => new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: n, size: 24 })] })),
  new Paragraph({ spacing: { before: 1600 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Novembro de 2026", size: 24, color: "6B7280" })] }),
  new Paragraph({ children: [new PageBreak()] }),
  new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: "Índice", bold: true, size: 34, color: "1F2937" })] }),
  new TableOfContents("Índice", { hyperlink: true, headingStyleRange: "1-2" }),
];

const doc = new Document({
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: FONT, size: 22 }, paragraph: { spacing: { after: 120, line: 276 } } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 34, bold: true, color: "1F2937" }, paragraph: { spacing: { before: 0, after: 240 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, color: "1F2937" }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 1, keepNext: true } },
    ],
  },
  numbering: { config: [
    { reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
    { reference: "num", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] },
  ] },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } }, titlePage: true },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: `PGP 2026/27 · Grupo ${grupo} · Etapa 1`, size: 18, color: "6B7280" })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "6B7280" })] })] }) },
    children: [...capa, ...children],
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(outPath, b); console.log("ok", outPath, children.length, "blocos"); });

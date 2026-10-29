# Ferramentas

Scripts usados para gerar as imagens, o relatório e a apresentação a partir das fontes do repositório.

| Ficheiro | Para quê |
|---|---|
| `../classes/fonte/modelo.py` | Diagramas de classes por grupo (Graphviz: `dot` tem de estar instalado) |
| `../classes/fonte/topo.py` | Diagrama de classes de topo (SVG) |
| `../casos-uso/fonte/casos_uso.py` | Diagramas de casos de uso (SVG) |
| `build_export.py` + `template-atividades.html` | Página que desenha os diagramas de atividades (blocos Mermaid de `../atividades/atividades.md`) e grava SVG e PNG |
| `server.py` | Servidor local que serve o repositório e grava os ficheiros exportados pelas páginas |
| `raster.html` | Converte SVG em PNG: `/…/raster.html?svg=etapa1/x/img/a.svg,…` |
| `esbocos-export.html` | Converte cada esboço de `../esbocos/esbocos.html` em PNG |
| `md2docx.js` | Gera o relatório Word a partir de `../relatorio/relatorio.md` (`npm install docx`) |
| `slides.js` | Gera a apresentação (`npm install pptxgenjs`) |

Exemplos:

```bash
python etapa1/classes/fonte/modelo.py && python etapa1/classes/fonte/topo.py
python etapa1/casos-uso/fonte/casos_uso.py
python etapa1/ferramentas/server.py .    # depois abrir http://localhost:8765/etapa1/ferramentas/raster.html?svg=...
node etapa1/ferramentas/md2docx.js etapa1/relatorio/relatorio.md etapa1/relatorio/PGP-2627-G12-E1-relatorio.docx 12
node etapa1/ferramentas/slides.js etapa1 etapa1/relatorio/PGP-2627-G12-E1-apresentacao.pptx 12
```

O PDF do relatório é exportado a partir do Word (atualizar o índice antes de exportar).

"""Diagrama de classes de topo (UML): só classes e associações, com um fundo
colorido por agrupamento. Lê as classes e associações de modelo.py e desenha
um SVG com posições fixas, para não haver multiplicidades sobrepostas.

Uso:  python topo.py   ->  ../img/01-topo.svg
"""
import html
import math
import os

from modelo import CLASSES, GRUPOS, REL

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "..", "img", "01-topo.svg")
W, H = 1480, 1010
FONTE = "Segoe UI, Arial, sans-serif"

# centro de cada classe
POS = {
    "Conta": (760, 100), "Utilizador": (650, 210), "Gestor": (880, 210),
    "PedidoNovaVersao": (195, 385), "Notificacao": (195, 500),
    "ListaPersonalizada": (515, 385), "ItemLista": (515, 500), "ItemColecao": (735, 440),
    "ItemCarrinho": (985, 385), "Fatura": (1215, 385), "LinhaFatura": (1215, 500), "DisponibilidadeLoja": (1250, 610),
    "Album": (560, 745), "VersaoAlbum": (965, 745), "Faixa": (560, 850), "Cancao": (560, 945),
    "Artista": (255, 850), "Grupo": (360, 945), "Solista": (150, 945),
}
# retângulo de fundo de cada grupo: (x0, y0, x1, y1)
FUNDOS = {
    "utilizadores": (560, 40, 970, 245),
    "pedidos": (60, 300, 330, 545),
    "colecoes": (390, 300, 840, 545),
    "loja": (890, 300, 1440, 645),
    "catalogo": (60, 690, 1100, 990),
}
# associações desenhadas como linha quebrada (pontos intermédios)
DESVIOS = {
    ("Utilizador", "Artista"): [(30, 210), (30, 850)],
    ("PedidoNovaVersao", "VersaoAlbum"): [(350, 385), (350, 665), (835, 665)],
}
# deslocamento do ponto de chegada à caixa (para as pontas não ficarem juntas): (de, para, ponta)
DESLOC = {
    ("PedidoNovaVersao", "Album", "b"): (-70, 0),
    ("ItemLista", "Album", "b"): (15, 0),
    ("PedidoNovaVersao", "VersaoAlbum", "b"): (-130, 0),
    ("ItemColecao", "VersaoAlbum", "b"): (-55, 0),
    ("ItemCarrinho", "VersaoAlbum", "b"): (20, 0),
    ("LinhaFatura", "VersaoAlbum", "b"): (85, 0),
    ("VersaoAlbum", "DisponibilidadeLoja", "a"): (140, 0),
    ("PedidoNovaVersao", "Album", "a"): (55, 0),
    ("Utilizador", "PedidoNovaVersao", "b"): (-35, 0),
    ("Utilizador", "ItemCarrinho", "b"): (35, 0),
    ("Utilizador", "Fatura", "b"): (25, 0),
}
# títulos de grupo encostados à direita (para não ficarem por baixo de linhas)
TITULO_DIREITA = {"loja"}
# só estas associações mostram o nome (as outras percebem-se pelas classes)
COM_NOME = {"favorito", "membros", "versão criada"}
E = html.escape


LARGURAS = {"VersaoAlbum": 330, "Album": 210, "Utilizador": 240}


def tamanho(nome):
    est = CLASSES[nome][1]
    w = LARGURAS.get(nome, max(96, len(nome) * 8.6 + 30))
    h = 50 if est else 34
    return w, h


def borda(nome, alvo, desloc=(0, 0)):
    """Ponto na borda da caixa de `nome` na direção de `alvo` (a partir do centro deslocado)."""
    cx, cy = POS[nome][0] + desloc[0], POS[nome][1] + desloc[1]
    w, h = tamanho(nome)
    # a caixa continua centrada em POS; desloc só muda o ponto de saída
    x0, x1 = POS[nome][0] - w / 2, POS[nome][0] + w / 2
    y0, y1 = POS[nome][1] - h / 2, POS[nome][1] + h / 2
    dx, dy = alvo[0] - cx, alvo[1] - cy
    if dx == 0 and dy == 0:
        return cx, cy
    ts = []
    if dx:
        ts += [(x0 - cx) / dx, (x1 - cx) / dx]
    if dy:
        ts += [(y0 - cy) / dy, (y1 - cy) / dy]
    s = min(t for t in ts if t > 0)
    return cx + dx * s, cy + dy * s


def _borda_antiga(nome, alvo):
    cx, cy = POS[nome]
    w, h = tamanho(nome)
    dx, dy = alvo[0] - cx, alvo[1] - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (w / 2) / abs(dx) if dx else math.inf
    sy = (h / 2) / abs(dy) if dy else math.inf
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1
    return dx / n, dy / n


def ponta(tipo, p, d, cor):
    """Desenha a ponta em p; d aponta de p para fora da classe (ao longo da linha)."""
    ux, uy = d
    nx, ny = -uy, ux
    if tipo == "diamante":
        pts = [p, (p[0] + ux * 9 + nx * 6, p[1] + uy * 9 + ny * 6), (p[0] + ux * 18, p[1] + uy * 18),
               (p[0] + ux * 9 - nx * 6, p[1] + uy * 9 - ny * 6)]
        return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{cor}" stroke="{cor}"/>'
    if tipo == "triangulo":
        pts = [p, (p[0] + ux * 15 + nx * 8, p[1] + uy * 15 + ny * 8), (p[0] + ux * 15 - nx * 8, p[1] + uy * 15 - ny * 8)]
        return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="white" stroke="{cor}" stroke-width="1.3"/>'
    if tipo == "seta":
        a = (p[0] + ux * 12 + nx * 6, p[1] + uy * 12 + ny * 6)
        b = (p[0] + ux * 12 - nx * 6, p[1] + uy * 12 - ny * 6)
        return f'<polyline points="{a[0]:.1f},{a[1]:.1f} {p[0]:.1f},{p[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="none" stroke="{cor}" stroke-width="1.3"/>'
    return ""


def rotulo_mult(texto, p, d, classe):
    """Multiplicidade junto à ponta p, do lado da linha mais afastado da caixa."""
    ux, uy = d
    cands = [(p[0] + ux * 30 + s * -uy * 16, p[1] + uy * 30 + s * ux * 16) for s in (1, -1)]
    x, y = max(cands, key=lambda c: math.dist(c, POS[classe]))
    return f'<text x="{x:.1f}" y="{y + 4:.1f}" font-size="12" text-anchor="middle" fill="#1f2937">{E(texto)}</text>'


def main():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONTE}">',
         f'<rect width="{W}" height="{H}" fill="white"/>']
    for g, (x0, y0, x1, y1) in FUNDOS.items():
        nome, cor, bord = GRUPOS[g]
        s.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="12" fill="{cor}" stroke="{bord}" stroke-width="1.6"/>')
        if g in TITULO_DIREITA:
            s.append(f'<text x="{x1 - 14}" y="{y0 + 22}" font-size="15" font-weight="bold" text-anchor="end" fill="{bord}">{E(nome)}</text>')
        else:
            s.append(f'<text x="{x0 + 14}" y="{y0 + 22}" font-size="15" font-weight="bold" fill="{bord}">{E(nome)}</text>')
    cor = "#334155"
    camadas_texto = []
    for a, b, tipo, ma, mb, nome in REL:
        meio = DESVIOS.get((a, b), [])
        oa = DESLOC.get((a, b, "a"), (0, 0))
        ob = DESLOC.get((a, b, "b"), (0, 0))
        alvo_b = (POS[b][0] + ob[0], POS[b][1] + ob[1])
        alvo_a = (POS[a][0] + oa[0], POS[a][1] + oa[1])
        pa = borda(a, meio[0] if meio else alvo_b, oa)
        pb = borda(b, meio[-1] if meio else alvo_a, ob)
        pts = [pa, *meio, pb]
        s.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{cor}" stroke-width="1.3"/>')
        da = unit(pa, pts[1])
        db = unit(pb, pts[-2])
        if tipo == "gen":
            s.append(ponta("triangulo", pa, da, cor))
        elif tipo == "comp":
            s.append(ponta("diamante", pa, da, cor))
        elif tipo == "nav":
            s.append(ponta("seta", pb, db, cor))
        if ma:
            camadas_texto.append(rotulo_mult(ma, pa, da, a))
        if mb:
            camadas_texto.append(rotulo_mult(mb, pb, db, b))
        if nome in COM_NOME:
            segs = range(len(pts) - 1)
            horiz = [i for i in segs if abs(pts[i][1] - pts[i + 1][1]) < 1]
            seg = max(horiz or segs, key=lambda i: math.dist(pts[i], pts[i + 1]))
            mx = (pts[seg][0] + pts[seg + 1][0]) / 2
            my = (pts[seg][1] + pts[seg + 1][1]) / 2
            camadas_texto.append(f'<text x="{mx + 6:.1f}" y="{my + 18:.1f}" font-size="12" font-style="italic" fill="#475569">{E(nome)}</text>')
    for n, (cx, cy) in POS.items():
        g, est, _ = CLASSES[n]
        bord = GRUPOS[g][2]
        w, h = tamanho(n)
        s.append(f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h}" fill="white" stroke="{bord}" stroke-width="1.5"/>')
        if est:
            s.append(f'<text x="{cx}" y="{cy - 6}" font-size="11" text-anchor="middle" fill="#334155">«{E(est)}»</text>')
            s.append(f'<text x="{cx}" y="{cy + 13}" font-size="14" font-weight="bold" font-style="italic" text-anchor="middle" fill="#0f172a">{E(n)}</text>')
        else:
            s.append(f'<text x="{cx}" y="{cy + 5}" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{E(n)}</text>')
    s.extend(camadas_texto)
    s.append("</svg>")
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(s))
    print("01-topo.svg ok")


if __name__ == "__main__":
    main()

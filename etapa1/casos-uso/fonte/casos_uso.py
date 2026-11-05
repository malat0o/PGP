"""Fonte dos diagramas de casos de uso (UML). Gera em ../img:
- casos-uso-00-topo.svg: diagrama de topo, com um package por agrupamento lógico e os atores de cada um;
- casos-uso-01-conta.svg a casos-uso-06-estatisticas.svg: um diagrama por package.

Uso:  python casos_uso.py
"""
import sys, os, html
RX, RY, STEP, CX, TOP = 165, 30, 80, 520, 110
W = 1220
COR = {"Utilizador": ("#dbeafe", "#1d4ed8"), "Gestor": ("#fee2e2", "#b91c1c"), "Ambos": ("#ede9fe", "#6d28d9")}

# Agrupamentos lógicos: (ficheiro, nome, [(UC, nome, atores humanos)], [(sistema, descrição, [UCs], y opcional)], extends, referências, nota)
# Uma referência é um caso de uso de outro package, desenhado a tracejado.
# Cada «extend» tem a condição; o caso de uso base mostra o ponto de extensão (PONTOS).
PONTOS = {"UC-07": "favorito", "UC-09": "gerir stock"}
PACKAGES = [
 ("01-conta", "Conta e perfil",
  [("UC-03", "Aceder ao dashboard", "U"), ("UC-04", "Visualizar perfil", "U"), ("UC-01", "Criar conta", "U"),
   ("UC-05", "Gerir perfil", "U"), ("UC-02", "Iniciar sessão", "UG")],
  [("Serviço de Mapas", "(Leaflet + OpenStreetMap)", ["UC-04"]), ("Serviço de Geocodificação", "(Nominatim)", ["UC-01", "UC-05"])],
  [], {}, "UC-02 (Iniciar sessão) é usado pelos dois atores."),
 ("02-catalogo", "Catálogo de música",
  [("UC-06", "Pesquisar artistas e álbuns", "U"), ("UC-07", "Visualizar página de artista", "U"), ("UC-08", "Gerir artista favorito", "U"),
   ("UC-09", "Visualizar página de álbum", "UG"), ("UC-17", "Gerir artistas", "G"), ("UC-18", "Gerir álbuns e versões", "G")],
  [("Cover Art Archive", "(sugestão da capa pelo MBID)", ["UC-18"], TOP + 20 + 3.2 * STEP), ("Cloudinary", "(armazenamento das capas)", ["UC-18"], TOP + 20 + 4.6 * STEP),
   ("MusicBrainz", "(importação das faixas)", ["UC-18"], TOP + 20 + 6.0 * STEP)],
  [("UC-08", "UC-07", "[Favorito]")], {}, "O utilizador consulta o catálogo; o gestor regista e altera artistas, álbuns e versões."),
 ("03-colecao-listas", "Coleção e listas",
  [("UC-10", "Gerir coleção", "U"), ("UC-11", "Gerir listas personalizadas", "U"), ("UC-12", "Gerir conteúdo de uma lista", "U")],
  [], [], {}, None),
 ("04-pedidos", "Pedidos de nova versão",
  [("UC-13", "Submeter pedido de nova versão", "U"), ("UC-14", "Consultar pedidos e notificações", "U"), ("UC-19", "Responder a pedido de nova versão", "G")],
  [], [], {}, None),
 ("05-loja", "Loja",
  [("UC-15", "Gerir carrinho de compras", "U"), ("UC-16", "Pagar carrinho", "U"), ("UC-09", "Visualizar página de álbum", ""), ("UC-20", "Gerir stock", "G")],
  [("Serviço de Pagamentos", "(Stripe / PayPal)", ["UC-16"])],
  [("UC-20", "UC-09", "[gestor]")], {"UC-09": "Catálogo de música"}, "UC-09 pertence ao package Catálogo de música; aparece aqui por causa do «extend»."),
 ("06-estatisticas", "Estatísticas",
  [("UC-21", "Visualizar estatísticas", "G")],
  [("Serviço de Mapas", "(Leaflet + OpenStreetMap)", ["UC-21"])],
  [], {}, None),
]


def ator(a, x, y, nome):
    a(f'<circle cx="{x}" cy="{y-70}" r="16" fill="#fff" stroke="#0f172a" stroke-width="2"/>')
    for l in [(x, y-54, x, y), (x-25, y-35, x+25, y-35), (x, y, x-20, y+35), (x, y, x+20, y+35)]:
        a('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#0f172a" stroke-width="2"/>' % l)
    a(f'<text x="{x}" y="{y+60}" text-anchor="middle" font-size="16" font-weight="bold" fill="#0f172a">{nome}</text>')


def sistema(a, sx, sy, nome, sub):
    a(f'<rect x="{sx-125}" y="{sy-40}" width="250" height="80" rx="4" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>')
    a(f'<text x="{sx}" y="{sy-19}" text-anchor="middle" font-size="12" fill="#15803d">«sistema externo»</text>')
    a(f'<text x="{sx}" y="{sy+2}" text-anchor="middle" font-size="15" font-weight="bold" fill="#0f172a">{html.escape(nome)}</text>')
    a(f'<text x="{sx}" y="{sy+22}" text-anchor="middle" font-size="13" fill="#334155">{html.escape(sub)}</text>')


def cabecalho(a, H):
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif">')
    a('<defs><marker id="open" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#333" stroke-width="1.2"/></marker></defs>')
    a(f'<rect width="{W}" height="{H}" fill="#fff"/>')


def pasta(a, x, y, w, h, titulo, fundo="#f8fafc", traco="#334155", tamanho=18):
    """Símbolo UML de package: separador em cima à esquerda e corpo."""
    tw = min(w * 0.55, 30 + 9.5 * len(titulo))
    a(f'<rect x="{x}" y="{y-28}" width="{tw}" height="28" fill="{fundo}" stroke="{traco}" stroke-width="2"/>')
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fundo}" stroke="{traco}" stroke-width="2"/>')
    a(f'<text x="{x+12}" y="{y-9}" font-size="{tamanho-3}" font-weight="bold" fill="#0f172a">{html.escape(titulo)}</text>')


def diagrama_package(out, nome, ucs, sistemas, extends, refs, nota):
    n = len(ucs)
    pos = {k: (CX, TOP + 20 + i*STEP) for i, (k, _, _) in enumerate(ucs)}
    # atores humanos: centrados nos seus casos de uso, afastados se ficarem muito perto
    y_de = lambda letra: [pos[k][1] for k, _, q in ucs if letra in q]
    atores = {}
    for letra, nomeator in (("U", "Utilizador"), ("G", "Gestor")):
        ys = y_de(letra)
        if ys:
            atores[nomeator] = sum(ys) / len(ys)
    if len(atores) == 2 and atores["Gestor"] - atores["Utilizador"] < 200:
        meio = (atores["Gestor"] + atores["Utilizador"]) / 2
        atores["Utilizador"], atores["Gestor"] = meio - 100, meio + 100
    if len(atores) == 1:
        k = next(iter(atores)); atores[k] = max(atores[k], TOP + 40)
    H = max(TOP + n*STEP + 70, int(max(atores.values()) + 110)) + (20 if nota else 0)
    s = []; a = s.append
    cabecalho(a, H)
    pasta(a, CX-RX-60, 70, 2*RX+120, H-100 - (20 if nota else 0), nome)
    ax = 110
    for nomeator, ay in atores.items():
        letra = nomeator[0]
        for k, _, q in ucs:
            if letra in q:
                cx, cy = pos[k]
                a(f'<line x1="{ax+25}" y1="{ay-30}" x2="{cx-RX}" y2="{cy}" stroke="#64748b" stroke-width="1.3"/>')
    sx = CX + RX + 60 + 190
    for sis in sistemas:
        nm, sub, alvos = sis[:3]
        ys = [pos[t][1] for t in alvos]
        sy = sis[3] if len(sis) > 3 else sum(ys)/len(ys)
        for t in alvos:
            cx, cy = pos[t]
            a(f'<line x1="{sx-125}" y1="{sy}" x2="{cx+RX}" y2="{cy}" stroke="#15803d" stroke-width="1.3"/>')
        sistema(a, sx, sy, nm, sub)
    for f, t, cond in extends:
        x1, y1 = pos[f]; x2, y2 = pos[t]
        if y1 > y2:
            a(f'<line x1="{x1+95}" y1="{y1-RY+2}" x2="{x2+95}" y2="{y2+RY-2}" stroke="#333" stroke-width="1.3" stroke-dasharray="6,4" marker-end="url(#open)"/>')
        else:
            a(f'<line x1="{x1+95}" y1="{y1+RY-2}" x2="{x2+95}" y2="{y2-RY+2}" stroke="#333" stroke-width="1.3" stroke-dasharray="6,4" marker-end="url(#open)"/>')
        a(f'<text x="{x1+105}" y="{(y1+y2)/2+5}" font-size="12" fill="#333">«extend» {cond}</text>')
    bases = {t for _, t, _ in extends}
    for k, nm, q in ucs:
        cx, cy = pos[k]
        ponto = PONTOS.get(k) if k in bases else None
        d = 8 if ponto else 0
        if k in refs:
            fundo, traco, cor_id, cor_nome = "#fff", "#64748b", "#64748b", "#475569"
            a(f'<ellipse cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="{fundo}" stroke="{traco}" stroke-width="1.5" stroke-dasharray="5,4"/>')
            rotulo = f"{k} (de {html.escape(refs[k])})"
        else:
            fundo, traco = COR["Ambos" if q == "UG" else ("Utilizador" if q == "U" else "Gestor")]
            cor_id, cor_nome = "#334155", "#0f172a"
            a(f'<ellipse cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="{fundo}" stroke="{traco}" stroke-width="1.5"/>')
            rotulo = k
        a(f'<text x="{cx}" y="{cy-5-d}" text-anchor="middle" font-size="12" font-weight="bold" fill="{cor_id}">{rotulo}</text>')
        a(f'<text x="{cx}" y="{cy+13-d}" text-anchor="middle" font-size="14" fill="{cor_nome}">{html.escape(nm)}</text>')
        if ponto and k not in refs:
            a(f'<line x1="{cx-RX+22}" y1="{cy+10}" x2="{cx+RX-22}" y2="{cy+10}" stroke="{traco}" stroke-width="0.8"/>')
        if ponto:
            a(f'<text x="{cx}" y="{cy+22}" text-anchor="middle" font-size="10.5" font-style="italic" fill="{cor_nome if k in refs else "#334155"}">pontos de extensão: {ponto}</text>')
    for nomeator, ay in atores.items():
        ator(a, ax, ay, nomeator)
    if nota:
        a(f'<text x="{CX}" y="{H-12}" text-anchor="middle" font-size="12" fill="#64748b">{html.escape(nota)}</text>')
    a('</svg>')
    open(out, "w", encoding="utf-8").write("\n".join(s))


def diagrama_topo(out):
    PW, PH, PSTEP, PX, PY = 440, 74, 120, 390, 120
    n = len(PACKAGES)
    H = PY + n*PSTEP + 10
    s = []; a = s.append
    cabecalho(a, H)
    a(f'<text x="{W/2}" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#0f172a">Aplicação web: casos de uso por package</text>')
    caixa = {}
    ORDEM_TOPO = ["Coleção e listas", "Conta e perfil", "Catálogo de música", "Pedidos de nova versão", "Loja", "Estatísticas"]
    for _, nome, ucs, _, _, refs, _ in PACKAGES:
        i = ORDEM_TOPO.index(nome)
        y = PY + i*PSTEP
        caixa[nome] = (PX, y, PX + PW, y + PH/2)
    # atores humanos à esquerda
    humanos = {"Utilizador": PY + 1.5*PSTEP, "Gestor": PY + 4.0*PSTEP}
    ax = 120
    for nomeator, ay in humanos.items():
        letra = nomeator[0]
        for _, nome, ucs, _, _, refs, _ in PACKAGES:
            if any(letra in q for k, _, q in ucs if k not in refs):
                x0, y0, x1, ym = caixa[nome]
                yy = ym - 22 if letra == "U" else ym + 22
                a(f'<line x1="{ax+25}" y1="{ay-30}" x2="{x0}" y2="{yy}" stroke="#64748b" stroke-width="1.4"/>')
    # sistemas externos à direita, ligados aos packages onde aparecem
    lig = {}
    for _, nome, _, sistemas, _, _, _ in PACKAGES:
        for sis in sistemas:
            lig.setdefault((sis[0], sis[1]), []).append(nome)
    sx = PX + PW + 100 + 125
    ordem = ["Serviço de Geocodificação", "Serviço de Mapas", "Cover Art Archive", "Cloudinary", "MusicBrainz", "Serviço de Pagamentos"]
    for j, chave in enumerate(sorted(lig, key=lambda c: ordem.index(c[0]))):
        sy = PY + 10 + j*(n*PSTEP - 60)/(len(lig)-1)
        for nome in lig[chave]:
            x0, y0, x1, ym = caixa[nome]
            a(f'<line x1="{sx-125}" y1="{sy}" x2="{x1}" y2="{ym}" stroke="#15803d" stroke-width="1.4"/>')
        sistema(a, sx, sy, *chave)
    for _, nome, ucs, _, _, refs, _ in PACKAGES:
        x0, y0, x1, ym = caixa[nome]
        pasta(a, x0, y0, PW, PH, nome, fundo="#f8fafc", tamanho=17)
        ids = sorted(k for k, _, _ in ucs if k not in refs)
        a(f'<text x="{x0+PW/2}" y="{y0+PH/2+6}" text-anchor="middle" font-size="14" fill="#334155">{", ".join(ids)}</text>')
    for nomeator, ay in humanos.items():
        ator(a, ax, ay, nomeator)
    a('</svg>')
    open(out, "w", encoding="utf-8").write("\n".join(s))


d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
diagrama_topo(d + "/casos-uso-00-topo.svg")
for f, nome, ucs, sistemas, extends, refs, nota in PACKAGES:
    diagrama_package(f"{d}/casos-uso-{f}.svg", nome, ucs, sistemas, extends, refs, nota)
print("ok")

"""Fonte dos diagramas de casos de uso (UML). Gera ../img/casos-uso-utilizador.svg e casos-uso-gestor.svg.

Uso:  python casos_uso.py
"""
import sys, html
RX, RY, STEP, CX, TOP = 165, 30, 80, 480, 150
def diagram(out, title, actor, ucs, systems, links, extend=None, color=("#dbeafe", "#1d4ed8"), note=None):
    n = len(ucs)
    H = TOP + n*STEP + 70
    W = 1180
    pos = {k: (CX, TOP + 20 + i*STEP) for i, (k, _) in enumerate(ucs)}
    names = dict(ucs)
    s = []; a = s.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif">')
    a('<defs><marker id="open" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#333" stroke-width="1.2"/></marker></defs>')
    a(f'<rect width="{W}" height="{H}" fill="#fff"/>')
    a(f'<rect x="{CX-RX-60}" y="70" width="{2*RX+120}" height="{H-100}" fill="#f8fafc" stroke="#334155" stroke-width="2"/>')
    a(f'<text x="{CX}" y="100" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">{html.escape(title)}</text>')
    ay = TOP + 20 + (n-1)*STEP/2
    ax = 110
    for k, _ in ucs:
        cx, cy = pos[k]
        a(f'<line x1="{ax+25}" y1="{ay-30}" x2="{cx-RX}" y2="{cy}" stroke="#64748b" stroke-width="1.3"/>')
    sx = CX + RX + 60 + 190
    for name, sub, targets in systems:
        ys = [pos[t][1] for t in targets]
        sy = sum(ys)/len(ys)
        for t in targets:
            cx, cy = pos[t]
            a(f'<line x1="{sx-125}" y1="{sy}" x2="{cx+RX}" y2="{cy}" stroke="#15803d" stroke-width="1.3"/>')
        a(f'<rect x="{sx-125}" y="{sy-40}" width="250" height="80" rx="4" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>')
        a(f'<text x="{sx}" y="{sy-19}" text-anchor="middle" font-size="12" fill="#15803d">«sistema externo»</text>')
        a(f'<text x="{sx}" y="{sy+2}" text-anchor="middle" font-size="15" font-weight="bold" fill="#0f172a">{html.escape(name)}</text>')
        a(f'<text x="{sx}" y="{sy+22}" text-anchor="middle" font-size="13" fill="#334155">{html.escape(sub)}</text>')
    if extend:
        f, t = extend
        x1, y1 = pos[f]; x2, y2 = pos[t]
        a(f'<line x1="{x1+95}" y1="{y1-RY+2}" x2="{x2+95}" y2="{y2+RY-2}" stroke="#333" stroke-width="1.3" stroke-dasharray="6,4" marker-end="url(#open)"/>')
        a(f'<text x="{x1+105}" y="{(y1+y2)/2+5}" font-size="12" fill="#333">«extend»</text>')
    for k, (cx, cy) in pos.items():
        a(f'<ellipse cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="{color[0]}" stroke="{color[1]}" stroke-width="1.5"/>')
        a(f'<text x="{cx}" y="{cy-5}" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">{k}</text>')
        a(f'<text x="{cx}" y="{cy+13}" text-anchor="middle" font-size="14" fill="#0f172a">{html.escape(names[k])}</text>')
    x, y = ax, ay
    a(f'<circle cx="{x}" cy="{y-70}" r="16" fill="#fff" stroke="#0f172a" stroke-width="2"/>')
    for l in [(x, y-54, x, y), (x-25, y-35, x+25, y-35), (x, y, x-20, y+35), (x, y, x+20, y+35)]:
        a('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#0f172a" stroke-width="2"/>' % l)
    a(f'<text x="{x}" y="{y+60}" text-anchor="middle" font-size="16" font-weight="bold" fill="#0f172a">{actor}</text>')
    if note:
        a(f'<text x="{CX}" y="{H-12}" text-anchor="middle" font-size="12" fill="#64748b">{html.escape(note)}</text>')
    a('</svg>')
    open(out, "w", encoding="utf-8").write("\n".join(s))
d = sys.argv[1] if len(sys.argv) > 1 else __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "img")
diagram(d + "/casos-uso-utilizador.svg", "Aplicação web: casos de uso do Utilizador", "Utilizador",
  [("UC-02","Iniciar sessão"),("UC-03","Aceder ao dashboard"),("UC-06","Pesquisar artistas e álbuns"),("UC-07","Visualizar página de artista"),("UC-08","Gerir artista favorito"),("UC-09","Visualizar página de álbum"),("UC-10","Gerir coleção"),("UC-11","Gerir listas personalizadas"),("UC-12","Gerir conteúdo de uma lista"),("UC-13","Submeter pedido de nova versão"),("UC-14","Consultar pedidos e notificações"),("UC-15","Gerir carrinho de compras"),("UC-16","Pagar carrinho"),("UC-04","Visualizar perfil"),("UC-05","Gerir perfil"),("UC-01","Criar conta")],
  [("Serviço de Pagamentos","(Stripe / PayPal)",["UC-16"]),("Serviço de Mapas","(Leaflet + OpenStreetMap)",["UC-04"]),("Serviço de Geocodificação","(Nominatim)",["UC-05","UC-01"])],
  None, extend=("UC-08","UC-07"), note="UC-02 e UC-09 são partilhados com o Gestor (ver diagrama do Gestor).")
diagram(d + "/casos-uso-gestor.svg", "Aplicação web: casos de uso do Gestor", "Gestor",
  [("UC-02","Iniciar sessão"),("UC-17","Gerir artistas"),("UC-18","Gerir álbuns e versões"),("UC-19","Responder a pedido de nova versão"),("UC-09","Visualizar página de álbum"),("UC-20","Gerir stock"),("UC-21","Visualizar estatísticas")],
  [("Serviço de Mapas","(Leaflet + OpenStreetMap)",["UC-21"])],
  None, extend=("UC-20","UC-09"), color=("#fee2e2","#b91c1c"), note="UC-02 e UC-09 são partilhados com o Utilizador.")
print("ok")

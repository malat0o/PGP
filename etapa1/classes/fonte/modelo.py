"""Fonte dos diagramas de classes (UML) do modelo de dados.

Gera um ficheiro .dot (Graphviz) por diagrama e, se o Graphviz estiver
instalado, as imagens SVG e PNG em ../img/.

Uso:  python modelo.py
"""
import html
import os
import shutil
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "..", "img")

# ---------------------------------------------------------------- grupos
GRUPOS = {
    "catalogo": ("Catálogo", "#dbeafe", "#1d4ed8"),
    "loja": ("Loja e vendas", "#dcfce7", "#15803d"),
    "utilizadores": ("Utilizadores", "#fef9c3", "#a16207"),
    "colecoes": ("Coleções e listas", "#f3e8ff", "#7e22ce"),
    "pedidos": ("Pedidos", "#fee2e2", "#b91c1c"),
}

# ---------------------------------------------------------------- classes
# nome: (grupo, estereótipo, [atributos])
CLASSES = {
    "Artista": ("catalogo", "abstract", ["isni : String «id»", "nome : String", "anoInicioAtividade : Integer"]),
    "Solista": ("catalogo", None, []),
    "Grupo": ("catalogo", None, []),
    "Album": ("catalogo", None, ["mbid : String «id»", "titulo : String", "anoLancamento : Integer", "tipo : TipoAlbum", "imagemCapa : URL [0..1]"]),
    "Cancao": ("catalogo", None, ["isrc : String «id»", "titulo : String", "duracao : Integer"]),
    "Faixa": ("catalogo", None, ["numero : Integer"]),
    "VersaoAlbum": ("catalogo", None, ["ean13 : String «id»", "suporte : SuporteFisico", "designacao : String [0..1]"]),
    "DisponibilidadeLoja": ("loja", None, ["dataInicio : Date", "unidades : Integer", "preco : Decimal", "dataUltimaVenda : Date [0..1]"]),
    "ItemCarrinho": ("loja", None, ["dataAdicao : DateTime"]),
    "Fatura": ("loja", None, ["numero : Integer «id»", "data : Date", "nifFaturacao : String", "nomeFaturacao : String", "moradaFaturacao : Morada"]),
    "LinhaFatura": ("loja", None, ["preco : Decimal"]),
    "Conta": ("utilizadores", "abstract", ["username : String «id»", "email : String «único»", "passwordHash : String"]),
    "Utilizador": ("utilizadores", None, ["nif : String", "nome : String", "genero : Genero", "morada : Morada", "dataNascimento : Date"]),
    "Gestor": ("utilizadores", None, []),
    "ItemColecao": ("colecoes", None, ["dataRegisto : Date"]),
    "ListaPersonalizada": ("colecoes", None, ["nome : String", "dataUltimaModificacao : DateTime"]),
    "ItemLista": ("colecoes", None, ["dataAdicao : Date"]),
    "PedidoNovaVersao": ("pedidos", None, ["id : Integer «id»", "dataPedido : DateTime", "estado : EstadoPedido", "ean13 : String", "suporte : SuporteFisico", "designacao : String [0..1]", "dataResposta : DateTime [0..1]"]),
    "Notificacao": ("pedidos", None, ["dataEmissao : DateTime", "lida : Boolean"]),
}
TIPOS = {
    "TipoAlbum": ("enumeration", ["single", "EP", "LP"]),
    "SuporteFisico": ("enumeration", ["CD", "vinil", "cassete"]),
    "Genero": ("enumeration", ["feminino", "masculino"]),
    "EstadoPedido": ("enumeration", ["emAnalise", "aceite", "recusado"]),
    "Morada": ("dataType", ["texto : String", "latitude : Decimal [0..1]", "longitude : Decimal [0..1]"]),
}

# ---------------------------------------------------------------- relações
# (de, para, tipo, mult_de, mult_para, nome)
# tipo: "gen" (de é a superclasse), "comp" (de é o todo), "nav" (seta para "para"), "assoc"
REL = [
    ("Artista", "Solista", "gen", "", "", ""),
    ("Artista", "Grupo", "gen", "", "", ""),
    ("Grupo", "Solista", "assoc", "0..*", "0..*", "membros"),
    ("Album", "Artista", "nav", "0..*", "0..1", "interpretado por"),
    ("Cancao", "Artista", "nav", "0..*", "1..*", "interpretada por"),
    ("Album", "Faixa", "comp", "1", "0..*", "faixas"),
    ("Faixa", "Cancao", "nav", "0..*", "1", ""),
    ("Album", "VersaoAlbum", "comp", "1", "1..*", "versões"),
    ("VersaoAlbum", "DisponibilidadeLoja", "comp", "1", "0..1", "disponibilidade"),
    ("Utilizador", "ItemCarrinho", "comp", "1", "0..*", "carrinho"),
    ("ItemCarrinho", "VersaoAlbum", "nav", "0..*", "1", ""),
    ("Utilizador", "Fatura", "assoc", "0..1", "0..*", "compras"),
    ("Fatura", "LinhaFatura", "comp", "1", "1..*", "linhas"),
    ("LinhaFatura", "VersaoAlbum", "nav", "0..*", "1", ""),
    ("Conta", "Utilizador", "gen", "", "", ""),
    ("Conta", "Gestor", "gen", "", "", ""),
    ("Utilizador", "Artista", "nav", "0..*", "0..1", "favorito"),
    ("Utilizador", "ItemColecao", "comp", "1", "0..*", "coleção"),
    ("ItemColecao", "VersaoAlbum", "nav", "0..*", "1", ""),
    ("ItemColecao", "LinhaFatura", "nav", "0..1", "0..1", "origem"),
    ("Utilizador", "ListaPersonalizada", "comp", "1", "0..*", "listas"),
    ("ListaPersonalizada", "ItemLista", "comp", "1", "0..*", "álbuns"),
    ("ItemLista", "Album", "nav", "0..*", "1", ""),
    ("Utilizador", "PedidoNovaVersao", "assoc", "1", "0..*", "pedidos"),
    ("PedidoNovaVersao", "Album", "nav", "0..*", "1", "álbum"),
    ("PedidoNovaVersao", "VersaoAlbum", "nav", "0..1", "0..1", "versão criada"),
    ("PedidoNovaVersao", "Notificacao", "comp", "1", "0..1", "resposta"),
]

# lado da caixa onde cada associação sai/entra no diagrama de topo (evita multiplicidades sobrepostas)
PORTAS_TOPO = {
    ("Utilizador", "ItemColecao"): ("w", "n"),
    ("Utilizador", "ListaPersonalizada"): ("sw", "n"),
    ("Utilizador", "PedidoNovaVersao"): ("s", "n"),
    ("Utilizador", "ItemCarrinho"): ("se", "n"),
    ("Utilizador", "Fatura"): ("e", "n"),
    ("Utilizador", "Artista"): ("ne", "e"),
    ("Album", "VersaoAlbum"): ("s", "n"),
    ("ItemColecao", "VersaoAlbum"): ("s", "w"),
    ("PedidoNovaVersao", "VersaoAlbum"): ("s", "ne"),
    ("ItemCarrinho", "VersaoAlbum"): ("s", "e"),
    ("LinhaFatura", "VersaoAlbum"): ("s", "se"),
    ("VersaoAlbum", "DisponibilidadeLoja"): ("s", "w"),
    ("PedidoNovaVersao", "Album"): ("sw", "e"),
    ("ItemLista", "Album"): ("s", "n"),
    ("Album", "Artista"): ("w", "nw"),
}
LARGOS = {"Utilizador", "VersaoAlbum", "Album"}
# portas nos diagramas por grupo, onde várias associações chegam à mesma classe
PORTAS_GRUPO = {
    ("ItemCarrinho", "VersaoAlbum"): ("s", "nw"),
    ("LinhaFatura", "VersaoAlbum"): ("s", "n"),
    ("VersaoAlbum", "DisponibilidadeLoja"): ("ne", "s"),
}

# ---------------------------------------------------------------- notas (restrições)
NOTAS = {
    "Artista": ["RI-07: isni tem 16 dígitos", "RI-08: anoInicioAtividade entre 1900 e 2100", "RI-35: isni único"],
    "Grupo": ["RI-31: membros só podem ser solistas"],
    "Album": ["RI-01: mbid tem 36 carateres", "RI-02: tipo é single, EP ou LP", "RI-09: anoLancamento entre 1900 e 2100",
              "RI-06, RI-10, RI-11: coerência com os artistas", "RI-32: no máximo 1 artista", "RI-33: mbid único"],
    "Cancao": ["RI-04: isrc tem 12 carateres", "RI-05: duracao (segundos) positiva", "RI-34: isrc único"],
    "Faixa": ["RI-03: numero começa em 1", "RI-38: numero único no álbum"],
    "VersaoAlbum": ["RI-12: suporte é CD, vinil ou cassete", "RI-13: ean13 tem 13 dígitos", "RI-36: ean13 único",
                    "RI-39: versões no mesmo suporte", "com designações distintas"],
    "DisponibilidadeLoja": ["RI-14: ano de dataInicio ≥ anoLancamento", "RI-15: unidades ≥ 0", "RI-16: preco positivo, 2 casas decimais",
                            "RI-17: dataUltimaVenda = data de fim", "de disponibilidade", "RI-47: dataInicio preenchida se houver unidades"],
    "Fatura": ["numero = ano + sequencial (ex.: 20270001)", "RI-27: ano de data ≥ anoLancamento dos álbuns",
               "RI-28: sequencial recomeça em 1 cada ano", "RI-37: numero único",
               "RI-48: dados de faturação copiados do utilizador", "na emissão e nunca alterados"],
    "ItemCarrinho": ["RI-46: só versões com unidades disponíveis"],
    "Conta": ["RI-18, RI-20: username e email únicos", "RI-19: username só com letras e dígitos",
              "RI-21: palavra-passe com 8+ carateres, 1 maiúscula,", "1 minúscula e 1 algarismo (validada antes de cifrar)"],
    "Utilizador": ["RI-22: nif com 9 dígitos, positivo", "RI-23: genero feminino ou masculino", "RI-24: pelo menos 16 anos",
                   "RI-40: no máximo 1 artista favorito"],
    "ItemColecao": ["RI-25: ano de dataRegisto ≥ anoLancamento", "RI-26: dataRegisto ≥ data em que fez 16 anos",
                    "RI-41: cada versão só uma vez por utilizador",
                    "RI-51: se tiver origem numa LinhaFatura, é a mesma",
                    "versão, do utilizador da fatura, e dataRegisto = data da fatura"],
    "ListaPersonalizada": ["RI-29: nome com no máximo 100 carateres", "RI-30: nome único para cada utilizador"],
    "ItemLista": ["RI-42: cada álbum só uma vez por lista"],
    "PedidoNovaVersao": ["RI-12: suporte é CD, vinil ou cassete", "RI-13: ean13 tem 13 dígitos", "RI-43: id único",
                         "RI-44: estado inicial emAnalise", "RI-45: só aceite se o ean13 ainda não existir",
                         "RI-49: dataResposta existe só se aceite ou recusado,", "e é ≥ dataPedido"],
    "Notificacao": ["RI-50: criada com lida = falso"],
}

# ---------------------------------------------------------------- diagramas por grupo
# grupo: (classes do grupo a mostrar, classes de outros grupos a cinzento, tipos, direção)
DIAGRAMAS = {
    "02-catalogo": (["Artista", "Solista", "Grupo", "Album", "Cancao", "Faixa", "VersaoAlbum"], [], ["TipoAlbum", "SuporteFisico"], "TB"),
    "03-loja-vendas": (["DisponibilidadeLoja", "ItemCarrinho", "Fatura", "LinhaFatura"], ["VersaoAlbum", "Utilizador"], [], "LR"),
    "04-utilizadores": (["Conta", "Utilizador", "Gestor"], ["Artista"], ["Morada", "Genero"], "TB"),
    "05-colecoes-listas": (["ItemColecao", "ListaPersonalizada", "ItemLista"], ["Utilizador", "VersaoAlbum", "Album", "LinhaFatura"], [], "LR"),
    "06-pedidos": (["PedidoNovaVersao", "Notificacao"], ["Utilizador", "Album", "VersaoAlbum"], ["EstadoPedido"], "LR"),
}

FONTE = "Segoe UI"
E = html.escape


def caixa(nome, cor, borda, atributos=True, estereotipo=None, attrs=None, tipo=False, largura=None):
    cab = ""
    if estereotipo:
        cab = f'<font point-size="10">«{E(estereotipo)}»</font><br/>'
    nome_fmt = f"<i>{E(nome)}</i>" if estereotipo == "abstract" else E(nome)
    w = f' width="{largura}"' if largura else ""
    linhas = [f'<tr><td bgcolor="{cor}" cellpadding="6"{w}>{cab}<b>{nome_fmt}</b></td></tr>']
    if atributos:
        corpo = "".join(f"{E(a)}<br align=\"left\"/>" for a in (attrs or [])) or " "
        linhas.append(f'<tr><td align="left" balign="left" cellpadding="6">{corpo}</td></tr>')
        if not tipo:
            linhas.append('<tr><td height="8"> </td></tr>')
    return (f'<<table border="0" cellborder="1" cellspacing="0" color="{borda}" bgcolor="white">'
            + "".join(linhas) + "</table>>")


def aresta(a, b, tipo, ma, mb, nome, mostrar_nome=True, portas=None):
    attrs = {"fontname": FONTE, "fontsize": "10", "color": "#334155", "labelfontsize": "10",
             "labeldistance": "2.4", "labelangle": "28"}
    if tipo == "gen":
        # a é a superclasse: seta (triângulo vazio) aponta para a
        attrs.update(dir="back", arrowtail="onormal", arrowsize="1.3")
    elif tipo == "comp":
        attrs.update(dir="both", arrowtail="diamond", arrowhead="none", arrowsize="1.1")
    elif tipo == "nav":
        attrs.update(dir="forward", arrowhead="vee")
    else:
        attrs.update(dir="none")
    if ma:
        attrs["taillabel"] = ma
    if mb:
        attrs["headlabel"] = mb
    if nome and mostrar_nome:
        attrs["label"] = f" {nome} "
    if portas:
        attrs["tailport"], attrs["headport"] = portas
    s = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f'  "{a}" -> "{b}" [{s}];'


def cabecalho(rankdir, sep="0.9"):
    return [
        "digraph G {",
        f'  graph [rankdir={rankdir}, fontname="{FONTE}", nodesep="{sep}", ranksep="0.9", pad="0.3", bgcolor="white", newrank=true];',
        f'  node [shape=plain, fontname="{FONTE}", fontsize="11"];',
        f'  edge [fontname="{FONTE}"];',
    ]


def topo():
    L = cabecalho("TB", "0.6")
    for g, (rotulo, cor, borda) in GRUPOS.items():
        L.append(f'  subgraph "cluster_{g}" {{ label=<<b>{E(rotulo)}</b>>; fontsize="14"; style="filled,rounded"; fillcolor="{cor}"; color="{borda}"; penwidth="1.5"; margin="16";')
        for n, (gr, est, _) in CLASSES.items():
            if gr == g:
                larg = 190 if n in LARGOS else None
                L.append(f'    "{n}" [label={caixa(n, "white", borda, atributos=False, estereotipo=est, largura=larg)}];')
        L.append("  }")
    for r in REL:
        L.append(aresta(*r, mostrar_nome=r[5] in ("favorito", "versão criada", "membros"), portas=PORTAS_TOPO.get((r[0], r[1]))))
    L.append("}")
    return "\n".join(L)


def grupo(nome_ficheiro):
    proprias, externas, tipos, rankdir = DIAGRAMAS[nome_ficheiro]
    g = CLASSES[proprias[0]][0]
    rotulo, cor, borda = GRUPOS[g]
    L = cabecalho(rankdir)
    L.append(f'  subgraph "cluster_{g}" {{ label=<<b>{E(rotulo)}</b>>; fontsize="14"; style="filled,rounded"; fillcolor="{cor}"; color="{borda}"; penwidth="1.5"; margin="18";')
    for n in proprias:
        _, est, attrs = CLASSES[n]
        L.append(f'    "{n}" [label={caixa(n, cor, borda, estereotipo=est, attrs=attrs)}];')
    for t in tipos:
        est, vals = TIPOS[t]
        L.append(f'    "{t}" [label={caixa(t, cor, borda, estereotipo=est, attrs=vals, tipo=True)}];')
    L.append("  }")
    for n in externas:
        larg = 200 if n in LARGOS else None
        L.append(f'  "{n}" [label={caixa(n, "#f1f5f9", "#94a3b8", atributos=False, estereotipo=CLASSES[n][1], largura=larg)}];')
    vis = set(proprias) | set(externas)
    for r in REL:
        if r[0] in vis and r[1] in vis and (r[0] in proprias or r[1] in proprias):
            L.append(aresta(*r, portas=PORTAS_GRUPO.get((r[0], r[1]))))
    for n in proprias:
        if n in NOTAS:
            txt = "".join(f"{E(t)}<br align=\"left\"/>" for t in NOTAS[n])
            L.append(f'  "nota_{n}" [shape=note, style=filled, fillcolor="#fef3c7", color="#a16207", fontsize="10", margin="0.12,0.06", label=<{txt}>];')
            L.append(f'  "nota_{n}" -> "{n}" [style=dashed, arrowhead=none, color="#a16207"];')
    L.append("}")
    return "\n".join(L)


def main():
    os.makedirs(IMG, exist_ok=True)
    # o diagrama de topo é desenhado por topo.py (posições fixas); aqui só os de grupo
    fontes = {n: grupo(n) for n in DIAGRAMAS}
    dot = shutil.which("dot")
    for nome, src in fontes.items():
        caminho = os.path.join(AQUI, nome + ".dot")
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(src + "\n")
        if dot:
            subprocess.run([dot, "-Tsvg", caminho, "-o", os.path.join(IMG, nome + ".svg")], check=True)
            subprocess.run([dot, "-Tpng", "-Gdpi=150", caminho, "-o", os.path.join(IMG, nome + ".png")], check=True)
        print(nome, "ok" if dot else "(.dot gerado; Graphviz não encontrado)")


if __name__ == "__main__":
    main()

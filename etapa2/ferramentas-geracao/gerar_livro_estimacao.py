"""Gera etapa2/estimacao/estimacao-etapa2.xlsx a partir do backlog (etapa2/backlog/backlog-wbs.md).

Folhas: Equipa (nomes e papéis, num só sítio), Disponibilidade, Planning poker, Esforço (três valores, T06),
Sprints, Pessoas e MS Project. Os valores da equipa (horas, story points, estimativas) ficam em branco.
O responsável e o sprint de cada item vêm pré-preenchidos com uma PROPOSTA (papéis A a E e ordem por
dependências do backlog), que a equipa confirma ou altera.

Uso: python etapa2/ferramentas-geracao/gerar_livro_estimacao.py   (precisa de openpyxl)
Atenção: voltar a gerar o livro apaga o que já tiver sido preenchido.
"""
import os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter as L

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BACKLOG = os.path.join(RAIZ, "etapa2", "backlog", "backlog-wbs.md")
SAIDA = os.path.join(RAIZ, "etapa2", "estimacao", "estimacao-etapa2.xlsx")

# Pessoas provisórias (trocar os nomes na folha Equipa quando a equipa decidir os papéis)
EQUIPA = [
    ("Pessoa A", "Gestor de projeto + responsável de testes com utilizadores"),
    ("Pessoa B", "Programador de frontend"),
    ("Pessoa C", "Programador de backend + arquiteto e consultor de dados"),
    ("Pessoa D", "Especialista de segurança e redes + técnico de manutenção"),
    ("Pessoa E", "Administrador da base de dados + apoio ao backend e a Redes"),
]
SPRINTS = ["S1", "S2", "S3"]
CONTINUO = "Todos"  # item que se repete em todos os sprints: o esforço divide-se por 3
# Semanas por sprint: aproximação (sprints de cerca de um mês, demos no fim de março, abril e maio).
SEMANAS = ["S1"] * 4 + ["S2"] * 4 + ["S3"] * 5

# ---------- Proposta de responsável (índice da pessoa: 0=A ... 4=E), por papel
RESP = {}
for i in ["GES.%02d" % n for n in range(1, 9)]:
    RESP[i] = 0
RESP.update({"INF.01": 3, "INF.02": 1, "INF.03": 2, "INF.04": 4, "INF.05": 2, "INF.06": 2, "INF.07": 4,
             "INF.08": 3, "INF.09": 3, "INF.10": 2, "INF.11": 1})
for u in [3, 5, 6, 8, 9, 11, 16, 18, 19, 27]:
    RESP["US.%02d" % u] = 1          # B: ecrãs e consultas
for u in [1, 2, 4, 12, 22, 23, 24, 28, 29]:
    RESP["US.%02d" % u] = 2          # C: lógica de negócio e formulários do gestor
for u in [7, 13, 14, 15, 17]:
    RESP["US.%02d" % u] = 0          # A: todos programam
for u in [10, 20, 21, 25, 26]:
    RESP["US.%02d" % u] = 4          # E: apoio ao backend
RESP.update({"INT.01": 2, "INT.02": 1, "INT.03": 2, "INT.04": 4, "INT.05": 4, "INT.06": 4})
RESP.update({"QUA.01": 3, "QUA.02": 2, "QUA.05": 0, "QUA.06": 0, "QUA.07": 1, "QUA.08": 4, "QUA.09": 0, "QUA.11": 1})
for n in range(1, 23):
    RESP["RED.%02d" % n] = 3
RESP.update({"RED.11": 4, "RED.18": 4, "RED.20": 2, "RED.21": 4})

# ---------- Proposta de sprint, a partir da ordem por níveis do backlog (Tabela 8)
CONT = {"GES.02", "GES.03", "GES.04", "GES.05", "GES.06", "GES.07", "GES.08", "INF.10", "QUA.01", "QUA.02", "QUA.11"}
S1 = {"INF.%02d" % n for n in range(1, 9)} | {"INF.11", "GES.01", "US.02", "US.19", "US.20", "US.22", "INT.05"} \
     | {"RED.%02d" % n for n in range(1, 10)} | {"RED.13", "RED.16"}
S2 = {"US.01", "US.05", "US.06", "US.08", "US.09", "US.10", "US.11", "US.25", "US.26", "US.27", "INT.01", "INT.06",
      "RED.10", "RED.11", "RED.12", "RED.14", "RED.15",
      "US.12", "US.13", "US.24", "US.14", "US.03", "US.04", "INT.02", "QUA.05", "INF.09"}
S3 = {"US.28", "INT.03", "INT.04", "US.07", "US.15", "US.16", "US.17", "US.18", "US.21", "US.23",
      "RED.17", "RED.18", "RED.19", "US.29", "QUA.06", "QUA.07", "QUA.08", "QUA.09", "RED.20", "RED.21", "RED.22"}

CAB = Font(bold=True, color="FFFFFF")
FUNDO_CAB = PatternFill("solid", fgColor="374151")
ENTRADA = PatternFill("solid", fgColor="FEF9C3")   # a equipa preenche
PROPOSTA = PatternFill("solid", fgColor="DBEAFE")  # pré-preenchido como proposta; a equipa confirma
CALC = PatternFill("solid", fgColor="E5E7EB")      # calculado
FINO = Side(style="thin", color="9CA3AF")
BORDA = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)


def ler_backlog():
    t = open(BACKLOG, encoding="utf-8").read()
    def tabela(titulo, fim):
        s = t[t.index(titulo):t.index(fim, t.index(titulo))]
        return [[c.strip() for c in l.strip().strip("|").split("|")] for l in s.splitlines()
                if re.match(r"^\| (US|GES|INF|INT|QUA|RED)\.\d\d \|", l)]
    itens = []
    for c in tabela("**Tabela 3", "## 4."):
        itens.append(dict(id=c[0], nome=c[1], pacote=c[2], tipo="User story", dep=c[4]))
    for c in tabela("**Tabela 4", "## 5."):
        itens.append(dict(id=c[0], nome=c[1], pacote=c[2], tipo="Técnica", dep=c[4]))
    for c in tabela("**Tabela 5", "Consequências"):
        itens.append(dict(id=c[0], nome=c[1], pacote="WP.11", tipo="Redes", dep=c[4]))
    return itens


def sprint_de(i):
    if i in CONT:
        return CONTINUO
    for s, conj in (("S1", S1), ("S2", S2), ("S3", S3)):
        if i in conj:
            return s
    raise SystemExit(f"item sem sprint proposto: {i}")


def expandir(dep):
    ids = set(re.findall(r"(?:US|GES|INF|INT|QUA|RED)\.\d\d", dep))
    for p, a, b in re.findall(r"(US|GES|INF|INT|QUA|RED)\.(\d\d) a (?:US|GES|INF|INT|QUA|RED)\.(\d\d)", dep):
        ids |= {f"{p}.{i:02d}" for i in range(int(a), int(b) + 1)}
    return sorted(ids)


def cabecalho(ws, nomes, larguras):
    for i, (n, w) in enumerate(zip(nomes, larguras), 1):
        c = ws.cell(row=1, column=i, value=n)
        c.font, c.fill, c.alignment, c.border = CAB, FUNDO_CAB, Alignment(wrap_text=True, vertical="center"), BORDA
        ws.column_dimensions[L(i)].width = w
    ws.freeze_panes = "A2"


def pintar(ws, linhas, colunas, fill):
    for r in linhas:
        for c in colunas:
            ws.cell(row=r, column=c).fill = fill
            ws.cell(row=r, column=c).border = BORDA


def main():
    itens = ler_backlog()
    faltam = [i["id"] for i in itens if i["id"] not in RESP]
    if faltam:
        raise SystemExit(f"itens sem responsável proposto: {faltam}")
    wb = Workbook()
    NOME = [f"Equipa!$A${k}" for k in range(2, 7)]  # células com os nomes

    # ---------------- Instruções
    ws = wb.active; ws.title = "Instruções"
    texto = [
        "Livro de estimação da Etapa 2 (PGP 2026/27, grupo 12)",
        "",
        "Cores: amarelo = a equipa preenche; azul = proposta pré-preenchida, a confirmar ou alterar; cinzento = calculado.",
        "",
        "0. Equipa: trocar 'Pessoa A' a 'Pessoa E' pelos nomes reais quando os papéis estiverem decididos (o livro todo atualiza).",
        "1. Disponibilidade: horas por semana de cada pessoa (TP5, exercício 1). Acertar a coluna Sprint com o calendário de PTIR.",
        "2. Planning poker: rondas e story points finais das 29 user stories (T06; sequência 1, 2, 3, 5, 8, 13, 21).",
        "3. Esforço: três valores em horas por item (otimista, provável, pessimista); esperado = (O + 4M + P) / 6 (T06).",
        "   Responsável e sprint vêm propostos (papéis e ordem por dependências do backlog). 'Todos' = item contínuo, dividido pelos 3 sprints.",
        "4. Sprints: verifica que cada sprint é fazível (planeado ≤ disponível × 0,85) e que estão equilibrados.",
        "5. Pessoas: tabela de esforço total previsto por pessoa, pedida no enunciado junto com o Gantt.",
        "6. MS Project: folha pronta a importar (Ficheiro > Abrir > Excel): nome, trabalho, predecessoras, recurso e sprint.",
        "",
        "Estimativa de controlo (pontos de função com a produtividade histórica de PTI): 1 400 a 1 870 h só para o software",
        "(etapa2/estimacao/estimativa-controlo.md).",
        "Gerado por etapa2/ferramentas-geracao/gerar_livro_estimacao.py a partir do backlog. Voltar a gerar apaga o que foi preenchido.",
    ]
    for i, l in enumerate(texto, 1):
        ws.cell(row=i, column=1, value=l)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 125

    # ---------------- Equipa
    weq = wb.create_sheet("Equipa")
    cabecalho(weq, ["Pessoa", "Papel (proposta)", "Reserva"], [16, 62, 16])
    for k, (n, p) in enumerate(EQUIPA, 2):
        weq.cell(row=k, column=1, value=n); weq.cell(row=k, column=2, value=p)
    pintar(weq, range(2, 7), [1, 2, 3], PROPOSTA)
    weq.cell(row=8, column=1, value="Nomes provisórios: trocar pelos nomes reais. Papéis segundo a matriz de competências (T09) e a preferência de cada um.")
    dv_eq = DataValidation(type="list", formula1="=Equipa!$A$2:$A$6", allow_blank=True)

    # ---------------- Disponibilidade
    ws = wb.create_sheet("Disponibilidade")
    cabecalho(ws, ["Semana", "Sprint", "", "", "", "", "", "Total (h)"], [9, 8] + [12] * 5 + [11])
    for j in range(5):
        c = ws.cell(row=1, column=3 + j, value=f"={NOME[j]}")
        c.font, c.fill, c.border = CAB, FUNDO_CAB, BORDA
    ultima = len(SEMANAS) + 1
    for i, s in enumerate(SEMANAS, 2):
        ws.cell(row=i, column=1, value=i - 1)
        ws.cell(row=i, column=2, value=s)
        ws.cell(row=i, column=8, value=f"=SUM(C{i}:G{i})")
    pintar(ws, range(2, ultima + 1), [2, 3, 4, 5, 6, 7], ENTRADA)
    pintar(ws, range(2, ultima + 1), [8], CALC)
    r = ultima + 1
    ws.cell(row=r, column=1, value="Total").font = Font(bold=True)
    for c in range(3, 9):
        ws.cell(row=r, column=c, value=f"=SUM({L(c)}2:{L(c)}{ultima})")
    pintar(ws, [r], range(3, 9), CALC)
    TOTAL_LINHA = r
    r += 2
    for c, t in enumerate(["Sprint", "Disponível (h)", "Para planear (× 0,85)", "Pessoa.mês (÷ 176)"], 1):
        ws.cell(row=r, column=c, value=t).font = Font(bold=True)
    DISP = {}
    for k, s in enumerate(SPRINTS + ["Total"], 1):
        rr = r + k
        ws.cell(row=rr, column=1, value=s)
        ws.cell(row=rr, column=2, value=f"=SUM(B{r+1}:B{r+3})" if s == "Total"
                else f'=SUMIF($B$2:$B${ultima},"{s}",$H$2:$H${ultima})')
        ws.cell(row=rr, column=3, value=f"=B{rr}*0.85")
        ws.cell(row=rr, column=4, value=f"=B{rr}/176"); ws.cell(row=rr, column=4).number_format = "0.0"
        DISP[s] = rr
        pintar(ws, [rr], [2, 3, 4], CALC)
    ws.cell(row=r + 6, column=1, value="Margem de 15%: mitigação do risco R01 (estimativas baixas). 176 h = 22 dias × 8 h (TP5).")

    # ---------------- Planning poker
    wp = wb.create_sheet("Planning poker")
    cabecalho(wp, ["US", "User story", "Ronda 1", "Ronda 2", "Ronda 3", "SP final", "Notas (porquê)"], [8, 36, 14, 14, 14, 9, 50])
    us = [i for i in itens if i["tipo"] == "User story"]
    dv_sp = DataValidation(type="list", formula1='"1,2,3,5,8,13,21"', allow_blank=True)
    wp.add_data_validation(dv_sp)
    for k, i in enumerate(us, 2):
        wp.cell(row=k, column=1, value="US" + str(int(i["id"][3:])))
        wp.cell(row=k, column=2, value=i["nome"])
        dv_sp.add(wp.cell(row=k, column=6))
    fim_poker = len(us) + 1
    pintar(wp, range(2, fim_poker + 1), [3, 4, 5, 6, 7], ENTRADA)
    wp.cell(row=fim_poker + 1, column=2, value="Total").font = Font(bold=True)
    wp.cell(row=fim_poker + 1, column=6, value=f"=SUM(F2:F{fim_poker})")
    pintar(wp, [fim_poker + 1], [6], CALC)
    wp.cell(row=fim_poker + 3, column=1, value="Rondas: cartas de cada pessoa pela ordem da folha Equipa (A/B/C/D/E), ex. 3/5/3/8/5. Referência: US15 = 2 pontos.")

    # ---------------- Esforço
    we = wb.create_sheet("Esforço")
    cabecalho(we, ["ID", "Item", "Pacote", "Tipo", "Depende de", "SP", "Otimista (h)", "Provável (h)", "Pessimista (h)",
                   "Esperado (h)", "Responsável", "Sprint"], [9, 48, 8, 11, 26, 6, 11, 11, 11, 12, 13, 8])
    dv_s = DataValidation(type="list", formula1='"' + ",".join(SPRINTS + [CONTINUO]) + '"', allow_blank=True)
    we.add_data_validation(dv_eq); we.add_data_validation(dv_s)
    for k, i in enumerate(itens, 2):
        for c, v in enumerate([i["id"], i["nome"], i["pacote"], i["tipo"], i["dep"]], 1):
            we.cell(row=k, column=c, value=v)
        if i["tipo"] == "User story":
            uid = "US" + str(int(i["id"][3:]))
            ref = f"INDEX('Planning poker'!$F$2:$F${fim_poker},MATCH(\"{uid}\",'Planning poker'!$A$2:$A${fim_poker},0))"
            we.cell(row=k, column=6, value=f'=IFERROR(IF({ref}="","",{ref}),"")')
        we.cell(row=k, column=10, value=f'=IF(COUNT(G{k}:I{k})=3,(G{k}+4*H{k}+I{k})/6,"")')
        we.cell(row=k, column=10).number_format = "0.0"
        we.cell(row=k, column=11, value=f"={NOME[RESP[i['id']]]}")
        we.cell(row=k, column=12, value=sprint_de(i["id"]))
        dv_eq.add(we.cell(row=k, column=11)); dv_s.add(we.cell(row=k, column=12))
    fim_e = len(itens) + 1
    pintar(we, range(2, fim_e + 1), [7, 8, 9], ENTRADA)
    pintar(we, range(2, fim_e + 1), [11, 12], PROPOSTA)
    pintar(we, range(2, fim_e + 1), [6, 10], CALC)
    we.cell(row=fim_e + 1, column=2, value="Total").font = Font(bold=True)
    we.cell(row=fim_e + 1, column=10, value=f"=SUM(J2:J{fim_e})")
    we.cell(row=fim_e + 2, column=2, value="Itens ainda sem estimativa")
    we.cell(row=fim_e + 2, column=10, value=f"=COUNTBLANK(G2:G{fim_e})")
    pintar(we, [fim_e + 1, fim_e + 2], [10], CALC)
    we.cell(row=fim_e + 4, column=2, value="Responsável: escolher na lista; trocar um nome na folha Equipa atualiza todas as linhas que o usam.")
    we.auto_filter.ref = f"A1:L{fim_e}"
    E_J, E_K, E_L, E_F = (f"'Esforço'!${c}$2:${c}${fim_e}" for c in "JKLF")

    # ---------------- Sprints
    wsp = wb.create_sheet("Sprints")
    cabecalho(wsp, ["Sprint", "Para planear (h)", "Planeado (h)", "Ocupação", "Story points", "N.º de itens", "Fazível?"],
              [10, 16, 14, 11, 13, 12, 12])
    for k, s in enumerate(SPRINTS, 2):
        wsp.cell(row=k, column=1, value=s)
        wsp.cell(row=k, column=2, value=f"=Disponibilidade!C{DISP[s]}")
        wsp.cell(row=k, column=3, value=f'=SUMIF({E_L},"{s}",{E_J})+SUMIF({E_L},"{CONTINUO}",{E_J})/3')
        wsp.cell(row=k, column=4, value=f'=IF(B{k}>0,C{k}/B{k},"")'); wsp.cell(row=k, column=4).number_format = "0%"
        wsp.cell(row=k, column=5, value=f'=SUMIF({E_L},"{s}",{E_F})')
        wsp.cell(row=k, column=6, value=f'=COUNTIF({E_L},"{s}")')
        wsp.cell(row=k, column=7, value=f'=IF(B{k}=0,"sem dados",IF(C{k}<=B{k},"Sim","Não"))')
    wsp.cell(row=5, column=1, value="Total").font = Font(bold=True)
    for c, f in [(2, "=SUM(B2:B4)"), (3, "=SUM(C2:C4)"), (5, "=SUM(E2:E4)"), (6, f'=SUM(F2:F4)+COUNTIF({E_L},"{CONTINUO}")')]:
        wsp.cell(row=5, column=c, value=f)
    wsp.cell(row=5, column=4, value='=IF(B5>0,C5/B5,"")'); wsp.cell(row=5, column=4).number_format = "0%"
    wsp.cell(row=5, column=7, value='=IF(B5=0,"sem dados",IF(C5<=B5,"Sim","Não"))')
    pintar(wsp, range(2, 6), range(2, 8), CALC)
    wsp.cell(row=7, column=1, value="Itens contínuos (Todos), divididos pelos 3 sprints")
    wsp.cell(row=7, column=3, value=f'=COUNTIF({E_L},"{CONTINUO}")')
    wsp.cell(row=8, column=1, value="Itens sem sprint")
    wsp.cell(row=8, column=3, value=f"=COUNTBLANK('Esforço'!L2:L{fim_e})")
    wsp.cell(row=9, column=1, value="Equilíbrio: diferença entre o sprint mais e o menos ocupado")
    wsp.cell(row=9, column=3, value='=IFERROR(MAX(D2:D4)-MIN(D2:D4),"")'); wsp.cell(row=9, column=3).number_format = "0%"
    wsp.cell(row=10, column=1, value="Estimativa de controlo (software, produtividade histórica de PTI): 1 400 a 1 870 h")
    wsp.cell(row=11, column=1, value="A distribuição proposta segue as dependências do backlog; equilibrar quando houver estimativas.")
    vermelho = PatternFill("solid", fgColor="FECACA")
    wsp.conditional_formatting.add("G2:G5", CellIsRule(operator="equal", formula=['"Não"'], fill=vermelho))

    # ---------------- Pessoas
    wpe = wb.create_sheet("Pessoas")
    cabecalho(wpe, ["Pessoa"] + SPRINTS + ["Total (h)", "Disponível (h)", "Ocupação", "N.º de itens"],
              [12, 10, 10, 10, 11, 14, 11, 12])
    for k in range(2, 7):
        j = k - 2
        wpe.cell(row=k, column=1, value=f"={NOME[j]}")
        for c, s in enumerate(SPRINTS, 2):
            wpe.cell(row=k, column=c, value=f'=SUMIFS({E_J},{E_K},$A{k},{E_L},"{s}")+SUMIFS({E_J},{E_K},$A{k},{E_L},"{CONTINUO}")/3')
        wpe.cell(row=k, column=5, value=f"=SUM(B{k}:D{k})")
        wpe.cell(row=k, column=6, value=f"=Disponibilidade!{L(3 + j)}{TOTAL_LINHA}")
        wpe.cell(row=k, column=7, value=f'=IF(F{k}>0,E{k}/F{k},"")'); wpe.cell(row=k, column=7).number_format = "0%"
        wpe.cell(row=k, column=8, value=f"=COUNTIF({E_K},$A{k})")
    wpe.cell(row=7, column=1, value="Total").font = Font(bold=True)
    for c in range(2, 7):
        wpe.cell(row=7, column=c, value=f"=SUM({L(c)}2:{L(c)}6)")
    wpe.cell(row=7, column=8, value="=SUM(H2:H6)")
    pintar(wpe, range(2, 8), range(2, 9), CALC)
    wpe.cell(row=9, column=1, value="Tabela de esforço total previsto por pessoa, pedida no enunciado. Ocupação acima de 100% indica sobreutilização (T07).")

    # ---------------- MS Project
    wm = wb.create_sheet("MS Project")
    cabecalho(wm, ["Id", "Nome", "Trabalho (h)", "Predecessoras", "Recurso", "Sprint", "Dependências não mapeadas"],
              [6, 56, 12, 18, 12, 8, 34])
    linha_de = {i["id"]: n for n, i in enumerate(itens, 1)}
    for n, i in enumerate(itens, 1):
        k = n + 1
        deps = expandir(i["dep"])
        resto = re.sub(r"(?:US|GES|INF|INT|QUA|RED)\.\d\d( a (?:US|GES|INF|INT|QUA|RED)\.\d\d)?", "", i["dep"]).strip(" ,—")
        wm.cell(row=k, column=1, value=n)
        wm.cell(row=k, column=2, value=f'{i["id"]} {i["nome"]}')
        wm.cell(row=k, column=3, value=f"='Esforço'!J{k}")
        wm.cell(row=k, column=4, value=";".join(str(linha_de[d]) for d in deps if d in linha_de))
        wm.cell(row=k, column=5, value=f"=IF('Esforço'!K{k}=\"\",\"\",'Esforço'!K{k})")
        wm.cell(row=k, column=6, value=f"=IF('Esforço'!L{k}=\"\",\"\",'Esforço'!L{k})")
        wm.cell(row=k, column=7, value=resto)
    pintar(wm, range(2, len(itens) + 2), [3, 5, 6], CALC)
    nota = len(itens) + 3
    wm.cell(row=nota, column=1, value="Importar no MS Project: Ficheiro > Abrir > Excel, mapear Nome, Trabalho, Predecessoras e Nomes dos recursos.")
    wm.cell(row=nota + 1, column=1, value="Acrescentar no Project as milestones M.1 a M.3 (demos) e M.R1 a M.R4 (Redes), e as dependências da última coluna.")

    wb.save(SAIDA)
    from collections import Counter
    print(f"ok: {SAIDA} ({len(itens)} itens)")
    print("por sprint:", Counter(sprint_de(i["id"]) for i in itens))
    print("por pessoa:", Counter(EQUIPA[RESP[i["id"]]][0] for i in itens))


if __name__ == "__main__":
    main()

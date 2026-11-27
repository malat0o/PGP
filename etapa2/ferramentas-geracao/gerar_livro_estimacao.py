"""Gera etapa2/estimacao/estimacao-etapa2.xlsx a partir do backlog (etapa2/backlog/backlog-wbs.md).

O livro tem folhas para a disponibilidade, o planning poker, o esforço por item (três valores, T06),
o equilíbrio dos sprints, o esforço por pessoa e uma folha pronta a importar no MS Project.
Os valores da equipa ficam em branco; as fórmulas calculam o resto.
Uso: python etapa2/ferramentas-geracao/gerar_livro_estimacao.py   (precisa de openpyxl)
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
PESSOAS = ["Rodrigo", "Reis", "Miguel", "Ze", "Edson"]
SPRINTS = ["S1", "S2", "S3"]
# Semanas por sprint: aproximação (sprints de cerca de um mês, demos no fim de março, abril e maio).
# Confirmar com o calendário de PTIR e acertar a coluna "Sprint" da folha Disponibilidade.
SEMANAS = ["S1"] * 4 + ["S2"] * 4 + ["S3"] * 5

CAB = Font(bold=True, color="FFFFFF")
FUNDO_CAB = PatternFill("solid", fgColor="374151")
ENTRADA = PatternFill("solid", fgColor="FEF9C3")   # células que a equipa preenche
CALC = PatternFill("solid", fgColor="E5E7EB")      # células calculadas
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


def expandir(dep):
    """Converte 'US.20, RED.17 a RED.19' numa lista de identificadores."""
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
    wb = Workbook()

    # ---------------- Instruções
    ws = wb.active; ws.title = "Instruções"
    texto = [
        "Livro de estimação da Etapa 2 (PGP 2026/27, grupo 12)",
        "",
        "Células amarelas: a equipa preenche. Células cinzentas: calculadas automaticamente.",
        "",
        "1. Disponibilidade: horas por semana de cada pessoa (TP5, exercício 1). Acertar a coluna Sprint com o calendário de PTIR.",
        "2. Planning poker: rondas e story points finais das 29 user stories (T06; sequência 1, 2, 3, 5, 8, 13, 21).",
        "3. Esforço: para cada item do backlog, três valores em horas (otimista, provável, pessimista); o esperado é (O + 4M + P) / 6 (T06).",
        "   Preencher também o responsável e o sprint de cada item.",
        "4. Sprints: verifica que cada sprint é fazível (planeado ≤ disponível × 0,85) e que estão equilibrados.",
        "5. Pessoas: tabela de esforço total previsto por pessoa, pedida no enunciado junto com o Gantt.",
        "6. MS Project: folha pronta a importar (Ficheiro > Abrir > Excel): nome, trabalho, predecessoras e recurso.",
        "",
        "A estimativa de controlo (pontos de função com produtividade histórica de PTI) dá 1 400 a 1 870 h só para o software:",
        "ver etapa2/estimacao/estimativa-controlo.md.",
        "Este livro é gerado por etapa2/ferramentas-geracao/gerar_livro_estimacao.py a partir do backlog.",
    ]
    for i, l in enumerate(texto, 1):
        ws.cell(row=i, column=1, value=l)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 120

    # ---------------- Disponibilidade
    ws = wb.create_sheet("Disponibilidade")
    cabecalho(ws, ["Semana", "Sprint"] + PESSOAS + ["Total (h)"], [9, 8] + [11] * 5 + [11])
    n = len(SEMANAS)
    for i, s in enumerate(SEMANAS, 2):
        ws.cell(row=i, column=1, value=i - 1)
        ws.cell(row=i, column=2, value=s)
        ws.cell(row=i, column=8, value=f"=SUM(C{i}:G{i})")
    ultima = n + 1
    pintar(ws, range(2, ultima + 1), [2, 3, 4, 5, 6, 7], ENTRADA)
    pintar(ws, range(2, ultima + 1), [8], CALC)
    r = ultima + 1
    ws.cell(row=r, column=1, value="Total").font = Font(bold=True)
    for c in range(3, 9):
        ws.cell(row=r, column=c, value=f"=SUM({L(c)}2:{L(c)}{ultima})")
    pintar(ws, [r], range(3, 9), CALC)
    r += 2
    ws.cell(row=r, column=1, value="Sprint").font = Font(bold=True)
    ws.cell(row=r, column=2, value="Disponível (h)").font = Font(bold=True)
    ws.cell(row=r, column=3, value="Para planear (× 0,85)").font = Font(bold=True)
    ws.cell(row=r, column=4, value="Pessoa.mês (÷ 176)").font = Font(bold=True)
    DISP = {}
    for k, s in enumerate(SPRINTS + ["Total"], 1):
        rr = r + k
        ws.cell(row=rr, column=1, value=s)
        if s == "Total":
            ws.cell(row=rr, column=2, value=f"=SUM(B{r+1}:B{r+3})")
        else:
            ws.cell(row=rr, column=2, value=f'=SUMIF($B$2:$B${ultima},"{s}",$H$2:$H${ultima})')
        ws.cell(row=rr, column=3, value=f"=B{rr}*0.85")
        ws.cell(row=rr, column=4, value=f"=B{rr}/176")
        DISP[s] = rr
        pintar(ws, [rr], [2, 3, 4], CALC)
        ws.cell(row=rr, column=4).number_format = "0.0"
    ws.cell(row=r + 6, column=1, value="Margem de 15%: mitigação do risco R01 (estimativas baixas). 176 h = 22 dias × 8 h (TP5).")

    # ---------------- Planning poker
    wp = wb.create_sheet("Planning poker")
    cabecalho(wp, ["US", "User story", "Ronda 1", "Ronda 2", "Ronda 3", "SP final", "Notas (porquê)"], [8, 36, 14, 14, 14, 9, 50])
    us = [i for i in itens if i["tipo"] == "User story"]
    dv_sp = DataValidation(type="list", formula1='"1,2,3,5,8,13,21"', allow_blank=True)
    wp.add_data_validation(dv_sp)
    for k, i in enumerate(us, 2):
        wp.cell(row=k, column=1, value=i["id"])
        wp.cell(row=k, column=2, value=i["nome"])
        dv_sp.add(wp.cell(row=k, column=6))
    fim_poker = len(us) + 1
    pintar(wp, range(2, fim_poker + 1), [3, 4, 5, 6, 7], ENTRADA)
    wp.cell(row=fim_poker + 1, column=2, value="Total").font = Font(bold=True)
    wp.cell(row=fim_poker + 1, column=6, value=f"=SUM(F2:F{fim_poker})")
    pintar(wp, [fim_poker + 1], [6], CALC)
    wp.cell(row=fim_poker + 3, column=1, value="Rondas: cartas pela ordem Rodrigo/Reis/Miguel/Ze/Edson, ex. 3/5/3/8/5. Referência: US15 = 2 pontos.")

    # ---------------- Esforço
    we = wb.create_sheet("Esforço")
    cols = ["ID", "Item", "Pacote", "Tipo", "Depende de", "SP", "Otimista (h)", "Provável (h)", "Pessimista (h)",
            "Esperado (h)", "Responsável", "Sprint"]
    cabecalho(we, cols, [9, 48, 8, 11, 26, 6, 11, 11, 11, 12, 13, 8])
    dv_p = DataValidation(type="list", formula1='"' + ",".join(PESSOAS) + '"', allow_blank=True)
    dv_s = DataValidation(type="list", formula1='"' + ",".join(SPRINTS) + '"', allow_blank=True)
    we.add_data_validation(dv_p); we.add_data_validation(dv_s)
    for k, i in enumerate(itens, 2):
        we.cell(row=k, column=1, value=i["id"])
        we.cell(row=k, column=2, value=i["nome"])
        we.cell(row=k, column=3, value=i["pacote"])
        we.cell(row=k, column=4, value=i["tipo"])
        we.cell(row=k, column=5, value=i["dep"])
        if i["tipo"] == "User story":
            uid = "US" + str(int(i["id"][3:]))  # US.01 -> US1 na folha de poker
            ref = f"INDEX('Planning poker'!$F$2:$F${fim_poker},MATCH(\"{uid}\",'Planning poker'!$A$2:$A${fim_poker},0))"
            we.cell(row=k, column=6, value=f'=IFERROR(IF({ref}="","",{ref}),"")')
        we.cell(row=k, column=10, value=f'=IF(COUNT(G{k}:I{k})=3,(G{k}+4*H{k}+I{k})/6,"")')
        we.cell(row=k, column=10).number_format = "0.0"
        dv_p.add(we.cell(row=k, column=11)); dv_s.add(we.cell(row=k, column=12))
    fim_e = len(itens) + 1
    # na folha de poker os IDs são US1..US29
    for k, i in enumerate(us, 2):
        wp.cell(row=k, column=1, value="US" + str(int(i["id"][3:])))
    pintar(we, range(2, fim_e + 1), [7, 8, 9, 11, 12], ENTRADA)
    pintar(we, range(2, fim_e + 1), [6, 10], CALC)
    we.cell(row=fim_e + 1, column=2, value="Total").font = Font(bold=True)
    we.cell(row=fim_e + 1, column=10, value=f"=SUM(J2:J{fim_e})")
    we.cell(row=fim_e + 2, column=2, value="Itens ainda sem estimativa")
    we.cell(row=fim_e + 2, column=10, value=f'=COUNTBLANK(G2:G{fim_e})')
    pintar(we, [fim_e + 1, fim_e + 2], [10], CALC)
    we.auto_filter.ref = f"A1:L{fim_e}"

    # ---------------- Sprints
    wsp = wb.create_sheet("Sprints")
    cabecalho(wsp, ["Sprint", "Para planear (h)", "Planeado (h)", "Ocupação", "Story points", "Fazível?"], [10, 16, 14, 11, 13, 12])
    for k, s in enumerate(SPRINTS, 2):
        wsp.cell(row=k, column=1, value=s)
        wsp.cell(row=k, column=2, value=f"=Disponibilidade!C{DISP[s]}")
        wsp.cell(row=k, column=3, value=f"=SUMIF('Esforço'!$L$2:$L${fim_e},\"{s}\",'Esforço'!$J$2:$J${fim_e})")
        wsp.cell(row=k, column=4, value=f'=IF(B{k}>0,C{k}/B{k},"")')
        wsp.cell(row=k, column=4).number_format = "0%"
        wsp.cell(row=k, column=5, value=f"=SUMIF('Esforço'!$L$2:$L${fim_e},\"{s}\",'Esforço'!$F$2:$F${fim_e})")
        wsp.cell(row=k, column=6, value=f'=IF(B{k}=0,"sem dados",IF(C{k}<=B{k},"Sim","Não"))')
    wsp.cell(row=5, column=1, value="Total").font = Font(bold=True)
    for c, f in [(2, "=SUM(B2:B4)"), (3, "=SUM(C2:C4)"), (5, "=SUM(E2:E4)")]:
        wsp.cell(row=5, column=c, value=f)
    wsp.cell(row=5, column=4, value='=IF(B5>0,C5/B5,"")'); wsp.cell(row=5, column=4).number_format = "0%"
    wsp.cell(row=5, column=6, value='=IF(B5=0,"sem dados",IF(C5<=B5,"Sim","Não"))')
    pintar(wsp, range(2, 6), range(2, 7), CALC)
    wsp.cell(row=7, column=1, value="Itens sem sprint")
    wsp.cell(row=7, column=3, value=f"=COUNTBLANK('Esforço'!L2:L{fim_e})")
    wsp.cell(row=8, column=1, value="Equilíbrio: diferença entre o sprint mais e o menos ocupado")
    wsp.cell(row=8, column=3, value='=IFERROR(MAX(D2:D4)-MIN(D2:D4),"")'); wsp.cell(row=8, column=3).number_format = "0%"
    wsp.cell(row=9, column=1, value="Estimativa de controlo (software, produtividade histórica de PTI): 1 400 a 1 870 h")
    vermelho = PatternFill("solid", fgColor="FECACA")
    wsp.conditional_formatting.add("F2:F5", CellIsRule(operator="equal", formula=['"Não"'], fill=vermelho))

    # ---------------- Pessoas
    wpe = wb.create_sheet("Pessoas")
    cabecalho(wpe, ["Pessoa"] + SPRINTS + ["Total (h)", "Disponível (h)", "Ocupação"], [12, 10, 10, 10, 11, 14, 11])
    for k, p in enumerate(PESSOAS, 2):
        wpe.cell(row=k, column=1, value=p)
        for j, s in enumerate(SPRINTS, 2):
            wpe.cell(row=k, column=j, value=f"=SUMIFS('Esforço'!$J$2:$J${fim_e},'Esforço'!$K$2:$K${fim_e},\"{p}\",'Esforço'!$L$2:$L${fim_e},\"{s}\")")
        wpe.cell(row=k, column=5, value=f"=SUM(B{k}:D{k})")
        col_disp = L(3 + PESSOAS.index(p))
        wpe.cell(row=k, column=6, value=f"=Disponibilidade!{col_disp}{ultima + 1}")
        wpe.cell(row=k, column=7, value=f'=IF(F{k}>0,E{k}/F{k},"")'); wpe.cell(row=k, column=7).number_format = "0%"
    wpe.cell(row=7, column=1, value="Total").font = Font(bold=True)
    for c in range(2, 7):
        wpe.cell(row=7, column=c, value=f"=SUM({L(c)}2:{L(c)}6)")
    pintar(wpe, range(2, 8), range(2, 8), CALC)
    wpe.cell(row=9, column=1, value="Tabela de esforço total previsto por pessoa, pedida no enunciado. Ocupação acima de 100% indica sobreutilização (T07).")

    # ---------------- MS Project
    wm = wb.create_sheet("MS Project")
    cabecalho(wm, ["Id", "Nome", "Trabalho (h)", "Predecessoras", "Recurso", "Sprint", "Dependências não mapeadas"],
              [6, 56, 12, 18, 12, 8, 34])
    linha_de = {i["id"]: n for n, i in enumerate(itens, 1)}
    for n, i in enumerate(itens, 1):
        k = n + 1
        deps = expandir(i["dep"])
        preds = [str(linha_de[d]) for d in deps if d in linha_de]
        resto = re.sub(r"(?:US|GES|INF|INT|QUA|RED)\.\d\d( a (?:US|GES|INF|INT|QUA|RED)\.\d\d)?", "", i["dep"]).strip(" ,—")
        wm.cell(row=k, column=1, value=n)
        wm.cell(row=k, column=2, value=f'{i["id"]} {i["nome"]}')
        wm.cell(row=k, column=3, value=f"='Esforço'!J{k}")
        wm.cell(row=k, column=4, value=";".join(preds))
        wm.cell(row=k, column=5, value=f"=IF('Esforço'!K{k}=\"\",\"\",'Esforço'!K{k})")
        wm.cell(row=k, column=6, value=f"=IF('Esforço'!L{k}=\"\",\"\",'Esforço'!L{k})")
        wm.cell(row=k, column=7, value=resto)
    pintar(wm, range(2, len(itens) + 2), [3, 5, 6], CALC)
    nota = len(itens) + 3
    wm.cell(row=nota, column=1, value="Importar no MS Project: Ficheiro > Abrir > Excel, mapear Nome, Trabalho, Predecessoras e Nomes dos recursos.")
    wm.cell(row=nota + 1, column=1, value="Acrescentar no Project as milestones M.1 a M.3 (demos) e M.R1 a M.R4 (Redes), e as dependências da última coluna.")

    wb.save(SAIDA)
    print(f"ok: {SAIDA} ({len(itens)} itens, {len(us)} user stories)")


if __name__ == "__main__":
    main()

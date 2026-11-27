"""Proposta inicial de esforço (três valores, T06) para os 84 itens do backlog.

É um ponto de partida para a equipa rever, NÃO a estimativa da equipa. Usa classes de tamanho
(com base na decomposição das user stories e na complexidade de cada tarefa) e gera
etapa2/estimacao/proposta-esforco.md com a tabela, os totais por pacote e a comparação com o disponível.
"""
import os, re, importlib.util
from collections import OrderedDict, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = importlib.util.spec_from_file_location("g", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gerar_livro_estimacao.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

# Classes de tamanho: (otimista, provável, pessimista) em horas
T = OrderedDict([
    ("XS", (3, 5, 8)),
    ("S", (5, 8, 13)),
    ("M", (8, 13, 20)),
    ("L", (13, 20, 32)),
    ("XL", (20, 32, 50)),
])
CLASSE = {}
for u, c in {1: "M", 2: "S", 3: "S", 4: "M", 5: "S", 6: "S", 7: "XS", 8: "XS", 9: "L", 10: "XS", 11: "S", 12: "S",
             13: "S", 14: "S", 15: "XS", 16: "S", 17: "XS", 18: "S", 19: "XS", 20: "S", 21: "XS", 22: "L", 23: "M",
             24: "M", 25: "S", 26: "XS", 27: "S", 28: "L", 29: "L"}.items():
    CLASSE["US.%02d" % u] = c
CLASSE.update({"INF.01": "XS", "INF.02": "S", "INF.03": "S", "INF.04": "M", "INF.05": "M", "INF.06": "M", "INF.07": "S",
               "INF.08": "S", "INF.09": "M", "INF.10": "S", "INF.11": "S",
               "INT.01": "S", "INT.02": "S", "INT.03": "L", "INT.04": "M", "INT.05": "M", "INT.06": "M",
               "GES.01": "XS",
               "QUA.02": "M", "QUA.05": "S", "QUA.06": "M", "QUA.07": "M", "QUA.08": "S", "QUA.09": "S", "QUA.11": "S"})
for n, c in {1: "XS", 2: "S", 3: "S", 4: "XS", 5: "XS", 6: "XS", 7: "S", 8: "S", 9: "S", 10: "M", 11: "L", 12: "L",
             13: "S", 14: "S", 15: "M", 16: "XS", 17: "S", 18: "M", 19: "M", 20: "M", 21: "S", 22: "S"}.items():
    CLASSE["RED.%02d" % n] = c
# Itens de gestão e contínuos: estimados pelo número de ocorrências (5 pessoas, 3 sprints, 13 semanas)
DIRETO = {
    "GES.02": ((10, 15, 20), "3 sprint plannings × 5 pessoas × 1 h"),
    "GES.03": ((15, 25, 40), "1 reunião/semana × 20 a 30 min × 5 pessoas × 13 semanas"),
    "GES.04": ((10, 15, 25), "3 reviews × 5 pessoas × 1 h (demos nas aulas)"),
    "GES.05": ((5, 8, 12), "3 retrospetivas × 5 pessoas × 30 min"),
    "GES.06": ((8, 12, 20), "Gantt e earned value analysis, cerca de 1 h por semana"),
    "GES.07": ((5, 8, 12), "2 planning pokers de ajuste × 5 pessoas × 50 min"),
    "GES.08": ((5, 10, 20), "Relatórios e entregas de PTIR"),
    "QUA.01": ((20, 35, 55), "Testes unitários e de integração ao longo do projeto"),
}


def esperado(o, m, p):
    return (o + 4 * m + p) / 6


def main():
    itens = g.ler_backlog()
    linhas, por_wp, tot = [], defaultdict(float), 0.0
    for i in itens:
        if i["id"] in DIRETO:
            (o, m, p), base = DIRETO[i["id"]]
            classe = "—"
        else:
            classe = CLASSE[i["id"]]
            o, m, p = T[classe]
            base = ""
        e = esperado(o, m, p)
        tot += e
        wp = i["pacote"] if i["pacote"].startswith("WP") else i["pacote"]
        por_wp[wp] += e
        linhas.append((i, classe, o, m, p, e, base))

    out = []
    out.append("# Proposta inicial de esforço por item\n")
    out.append("**Isto é um ponto de partida para a equipa rever, não a estimativa da equipa.** O enunciado pede que o esforço seja estimado pela equipa. Na sessão de estimação, cada responsável revê os valores dos seus itens, altera os que não concordar e copia-os para a folha \"Esforço\" do livro (`estimacao-etapa2.xlsx`). No relatório deve aparecer a estimativa revista.\n")
    out.append("## Como foi feita\n")
    out.append("Segue a estimação por decomposição com três valores da T06. Cada item foi classificado numa classe de tamanho, a partir da decomposição das user stories (dados e API, ecrã, serviço externo, testes) e da complexidade da tarefa. Cada classe tem três valores, e o esforço esperado é (O + 4M + P) ÷ 6. Os valores contam com uma equipa que ainda está a aprender a stack MEAN e a infraestrutura distribuída (riscos R02 e R03).\n")
    out.append("**Tabela 1 — Classes de tamanho**\n")
    out.append("| Classe | Otimista (h) | Provável (h) | Pessimista (h) | Esperado (h) | Exemplo |\n|---|---|---|---|---|---|")
    ex = {"XS": "Criar lista (US15), dashboard (US19)", "S": "Iniciar sessão (US2), ver carrinho (US27)",
          "M": "Criar conta (US1), responder a pedido (US24)", "L": "Página de álbum (US9), registar álbum (US22), pagar o carrinho (US28), estatísticas (US29)",
          "XL": "Nenhum item, depois de separar a integração com os serviços de pagamento da US28"}
    for c, (o, m, p) in T.items():
        out.append(f"| {c} | {o} | {m} | {p} | {esperado(o,m,p):.1f} | {ex[c]} |")
    out.append("\nOs itens de gestão e os testes automáticos foram estimados pelo número de vezes que acontecem (coluna \"Base\").\n")
    out.append("## Esforço por item\n")
    out.append("**Tabela 2 — Proposta de esforço por item**\n")
    out.append("| ID | Item | Pacote | Classe | O | M | P | Esperado (h) | Base |\n|---|---|---|---|---|---|---|---|---|")
    for i, classe, o, m, p, e, base in linhas:
        out.append(f"| {i['id']} | {i['nome']} | {i['pacote']} | {classe} | {o} | {m} | {p} | {e:.1f} | {base} |")
    out.append(f"| | **Total** | | | | | | **{tot:.0f}** | |\n")

    out.append("## Totais por pacote de trabalho\n")
    out.append("**Tabela 3 — Esforço esperado por pacote**\n")
    out.append("| Pacote | Esforço esperado (h) | % |\n|---|---|---|")
    nomes = {"WP.1": "Gestão do projeto", "WP.2": "Infraestrutura e arquitetura", "WP.3": "Conta e perfil", "WP.4": "Catálogo de música",
             "WP.5": "Coleção e listas", "WP.6": "Pedidos de nova versão", "WP.7": "Loja", "WP.8": "Estatísticas",
             "WP.9": "Integrações externas", "WP.10": "Qualidade, testes e RNF", "WP.11": "Tecnologias de Redes"}
    for wp in sorted(por_wp, key=lambda w: int(w.split(".")[1])):
        out.append(f"| {wp} {nomes[wp]} | {por_wp[wp]:.0f} | {100*por_wp[wp]/tot:.0f}% |")
    out.append(f"| **Total** | **{tot:.0f}** | 100% |\n")

    us_tot = sum(e for i, _, _, _, _, e, _ in linhas if i["tipo"] == "User story")
    soft = sum(por_wp[w] for w in ["WP.2", "WP.3", "WP.4", "WP.5", "WP.6", "WP.7", "WP.8", "WP.9"])
    out.append("## Comparação com o esforço disponível\n")
    out.append("**Tabela 4 — Necessário vs. disponível**\n")
    out.append("| Cenário | Disponível para planear (h) | Necessário (h) | Diferença (h) |\n|---|---|---|---|")
    for nome, h in [("4,5 h por pessoa por semana", 5 * 4.5 * 13 * 0.85), ("12 h por pessoa por semana (PTIR = 6 ECTS ≈ 156 h)", 5 * 12 * 13 * 0.85), ("14 h por pessoa por semana (2 h por dia)", 5 * 14 * 13 * 0.85)]:
        out.append(f"| {nome} | {h:.0f} | {tot:.0f} | {h - tot:+.0f} |")
    out.append("")
    out.append(f"- As 29 user stories somam cerca de **{us_tot:.0f} h** e o software no seu conjunto (pacotes WP.2 a WP.9) cerca de **{soft:.0f} h**. É menos do que a estimativa de controlo (1 400 a 1 870 h), porque esta proposta conta com uma implementação simples de cada ecrã. A T06 manda perceber diferenças grandes entre estimativas: na sessão de estimação, a equipa deve decidir se os valores estão otimistas.")
    out.append("- Mesmo com 10 h por semana, o necessário passa do disponível. O enunciado não o permite, por isso o product owner tem de **reduzir o âmbito**: ficam nos 3 sprints as funcionalidades prioritárias, e as restantes passam para um incremento posterior (T07).\n")
    out.append("## Candidatos a sair do âmbito (decisão do product owner)\n")
    out.append("Itens que podem sair sem pôr em causa o fluxo principal (conta, catálogo, coleção, carrinho e pagamento) nem a parte obrigatória de Redes:\n")
    cands = ["INT.04", "US.29", "US.15", "US.16", "US.17", "US.18", "US.07", "INT.06", "US.21", "US.23", "QUA.09"]
    out.append("| ID | Item | Esperado (h) | Porque pode sair |\n|---|---|---|---|")
    razao = {"INT.04": "A US28 b) só exige poder escolher um serviço; o Stripe chega", "US.29": "Estatísticas do gestor, sem dependentes",
             "US.15": "Listas personalizadas não são precisas para comprar nem colecionar", "US.16": "Idem", "US.17": "Idem", "US.18": "Idem",
             "US.07": "Favorito não é usado por outras funcionalidades além do perfil", "INT.06": "As faixas podem ser introduzidas nos dados de teste",
             "US.21": "Alterar artista pode ser feito na base de dados nesta fase", "US.23": "Idem para o álbum",
             "QUA.09": "RNF-16 está em \"Outros\" (menos prioritário)"}
    soma = 0
    for c in cands:
        e = next(e for i, _, _, _, _, e, _ in linhas if i["id"] == c)
        nome = next(i["nome"] for i in itens if i["id"] == c)
        soma += e
        out.append(f"| {c} | {nome} | {e:.1f} | {razao[c]} |")
    out.append(f"| | **Total** | **{soma:.0f}** | |\n")
    out.append(f"Tirando todos estes, o necessário desce para cerca de **{tot - soma:.0f} h**.\n")
    out.append("## Correções feitas a esta proposta\n")
    out.append("- **US28 sem contagem a dobrar:** a integração com o Stripe e o PayPal está nos itens INT.03 e INT.04, por isso a US28 conta só a lógica da aplicação (classe L em vez de XL).")
    out.append("- **Scripts de Redes sem contagem a dobrar:** a infraestrutura é montada logo com os scripts, por isso RED.17 a RED.19 contam só o que falta (parametrizar, scripts de falha e de promoção, ensaios).")
    out.append("- **Gestão mais leve:** uma reunião curta por semana, sprint planning de 1 h, e demonstrações durante as aulas. A gestão fica em cerca de 10% do esforço.\n")
    out.append("## Horas por semana que o plano exige\n")
    out.append("| Cenário | Necessário (h) | Horas por pessoa por semana (com 15% de margem) |\n|---|---|---|")
    for nome, h in [("Âmbito completo", tot), ("Sem os candidatos acima", tot - soma)]:
        out.append(f"| {nome} | {h:.0f} | {h / 0.85 / (5 * 13):.1f} |")
    out.append(f"\nPTIR tem **6 ECTS**: 6 × 26 h ≈ 156 h por pessoa no semestre, incluindo as aulas, ou seja, cerca de **12 h por semana**. Com 5 pessoas são 780 h, das quais {5*12*13*0.85:.0f} h para planear. O âmbito completo ({tot:.0f} h) não cabe; sem os candidatos acima ({tot - soma:.0f} h) ainda faltam cerca de {tot - soma - 5*12*13*0.85:.0f} h. Para fechar o plano, o product owner tem de cortar mais âmbito e a equipa deve rever as estimativas, que contam com uma equipa a aprender a tecnologia.")
    p = os.path.join(RAIZ, "etapa2", "estimacao", "proposta-esforco.md")
    open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"total {tot:.0f} h | US {us_tot:.0f} | software {soft:.0f} | candidatos {soma:.0f} | sem eles {tot-soma:.0f}")
    for wp in sorted(por_wp, key=lambda w: int(w.split('.')[1])):
        print(wp, round(por_wp[wp]))


if __name__ == "__main__":
    main()

"""Renumera as tabelas do relatório pela ordem em que aparecem.

As legendas têm a forma "**Tabela X — ...**". As tabelas novas podem usar um
rótulo provisório (ex.: "Tabela N1"). O script dá a cada legenda o número da
sua posição e corrige todas as referências "Tabela X" no texto, no relatório e
nos ficheiros indicados a seguir.

Uso:  python renumerar_tabelas.py relatorio.md [outros.md ...]
"""
import re
import sys

rel = sys.argv[1]
t = open(rel, encoding="utf-8").read()
rotulos = re.findall(r"\*\*Tabela (\w+) —", t)
mapa = {r: str(i + 1) for i, r in enumerate(rotulos)}
assert len(mapa) == len(rotulos), "rótulos repetidos"


def troca(m):
    return m.group(1) + mapa.get(m.group(2), m.group(2))


padrao = re.compile(r"(Tabelas? )(\w+)(?![\w])")
for ficheiro in sys.argv[1:]:
    s = open(ficheiro, encoding="utf-8").read()
    s2 = padrao.sub(troca, s)
    # "Tabelas 4 e 5": o segundo número também é uma referência
    s2 = re.sub(r"(Tabelas \d+ e )(\w+)", troca, s2)
    if s2 != s:
        open(ficheiro, "w", encoding="utf-8").write(s2)
        print("atualizado:", ficheiro)
print("mapa:", ", ".join(f"{a}->{b}" for a, b in mapa.items() if a != b) or "sem alterações")

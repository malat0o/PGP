import sys, html, re
md, out = sys.argv[1], sys.argv[2]
t = open(md, encoding="utf-8").read()
blocks = re.findall(r"```mermaid\n(.*?)```", t, re.S)
names = sys.argv[4].split(",")
assert len(blocks) == len(names), len(blocks)
divs = "".join(f'<div class="d"><pre class="mermaid" data-name="{n}">{html.escape(b)}</pre></div>' for n, b in zip(names, blocks))
page = open(sys.argv[3], encoding="utf-8").read().replace("%DIVS%", divs)
open(out, "w", encoding="utf-8").write(page)
print(len(blocks), "diagramas")

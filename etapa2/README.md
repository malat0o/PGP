# Etapa 2 (até 4 de dezembro)

Planeamento do trabalho de PTIR do próximo semestre. A tabela liga cada ponto pedido no enunciado ao ficheiro onde está tratado e diz o que ainda depende da equipa.

| Pedido do enunciado | Ficheiro | Estado |
|---|---|---|
| Papéis da equipa | [equipa/papeis.md](equipa/papeis.md) | Estrutura, papéis e responsabilidades prontos; falta a matriz de competências e atribuir pessoas |
| Ferramentas de desenvolvimento e software da aplicação | [ferramentas/ferramentas-software.md](ferramentas/ferramentas-software.md) | Pronto; falta escolher a cloud (GCP, AWS ou Azure) |
| Esforço disponível por semana e total | [estimacao/estimacao-etapa2.xlsx](estimacao/estimacao-etapa2.xlsx), folha "Disponibilidade" | Falta preencher as horas de cada pessoa |
| Story points em planning poker | Livro, folha "Planning poker" | Falta a sessão |
| Esforço de cada item do backlog | [backlog/backlog-wbs.md](backlog/backlog-wbs.md) e livro, folha "Esforço" | Backlog e decomposição prontos; faltam as estimativas |
| Estimativa de controlo (pontos de função e COCOMO) | [estimacao/estimativa-controlo.md](estimacao/estimativa-controlo.md) | Pronto |
| Distribuição pelos 3 sprints | Livro, folhas "Esforço" (coluna Sprint) e "Sprints" | Depois das estimativas |
| Mapa de Gantt e esforço por pessoa | Livro, folhas "MS Project" e "Pessoas"; Gantt no MS Project | Depois da distribuição |
| Gestão de risco | [riscos/gestao-risco.md](riscos/gestao-risco.md) | Pronto; a equipa revê probabilidades e impactos |
| API REST em OpenAPI (YAML) | [api/api.yaml](api/api.yaml) | Pronto (validado como OpenAPI 3.0) |
| Relatório | [relatorio/relatorio.md](relatorio/relatorio.md) e `PGP-2627-G12-E2-relatorio.docx` | Rascunho com as partes prontas; marcas **[A PREENCHER]** onde entram os dados da equipa |
| Apresentação | [relatorio/slides.md](relatorio/slides.md) | Guião de 13 slides; o `.pptx` gera-se no fim |

**Reunião de equipa:** ordem de trabalhos em [equipa/reuniao-equipa.md](equipa/reuniao-equipa.md). Recolhe os dados que faltam: competências, papéis, horas, planning poker e revisão dos riscos.

**Ficheiros gerados:**
- O livro de estimação é gerado a partir do backlog por `ferramentas-geracao/gerar_livro_estimacao.py`. Atenção: voltar a gerá-lo apaga o que já tiver sido preenchido.
- O relatório em Word é gerado por `etapa1/ferramentas/md2docx.js relatorio.md saida.docx 12 2`. O último argumento é o número da etapa.

Ordem do que falta: reunião de equipa → estimativas → sprints → Gantt → completar o relatório → apresentação → `PGP-2627-G12-E2.ZIP`.

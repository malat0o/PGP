# Planning poker, esforço disponível e esforço necessário

Folhas para preencher na reunião de equipa, com os métodos das aulas:
- **planning poker:** T06, slides "Planning Poker" e "Sessão de Planning Poker";
- **esforço disponível:** TP5 (Métricas), exercício 1;
- **estimação por decomposição com três valores:** T06, "Estimação por decomposição do produto".

Nenhum valor desta folha deve ser inventado: os números saem da equipa.

## 1. Esforço disponível

O enunciado pede o esforço disponível **ao longo das semanas** do próximo semestre e o total. O cálculo segue o exercício 1 do TP5: esforço = duração × dedicação de cada pessoa. Aqui usam-se horas por semana, que são mais fáceis de estimar do que percentagens.

**Como preencher:**
1. Cada pessoa indica as horas por semana que pode dar a PTIR.
2. Nas semanas de avaliação de outras cadeiras, cada pessoa indica quanto reduz. Esta é a mitigação do risco R06.
3. O total por semana é a soma das cinco pessoas. O total do sprint é a soma das suas semanas.

Os sprints terminam nas demonstrações de **final de março, abril e maio** (secção 1 do enunciado). As datas de início das semanas dependem do calendário de PTIR (ponto em aberto no backlog).

**Tabela 1 — Esforço disponível por semana (horas)**

| Semana | Sprint | Rodrigo | Reis | Miguel | Ze | Edson | Total |
|---|---|---|---|---|---|---|---|
| 1 | S1 | | | | | | |
| 2 | S1 | | | | | | |
| 3 | S1 | | | | | | |
| 4 | S1 | | | | | | |
| 5 | S2 | | | | | | |
| 6 | S2 | | | | | | |
| 7 | S2 | | | | | | |
| 8 | S2 | | | | | | |
| 9 | S3 | | | | | | |
| 10 | S3 | | | | | | |
| 11 | S3 | | | | | | |
| 12 | S3 | | | | | | |
| 13 | S3 | | | | | | |
| **Total** | | | | | | | |

**Esforço disponível para planear** = total × 0,85. A margem de 15% é a mitigação do risco R01 (estimativas baixas). Convertido para pessoa.mês, como no TP5, é **total ÷ 176**, com 22 dias por mês e 8 horas por dia.

## 2. Planning poker das 29 user stories

**Regras (T06):**
1. Cada pessoa tem um baralho com a sequência de Fibonacci: **1, 2, 3, 5, 8, 13, 21 e café** (pausa). O 21 é raro, porque representa algo muito complexo.
2. Alguém lê a user story em voz alta e a equipa esclarece dúvidas. Ajuda ter à mão a decomposição da Tabela 6 do backlog e os esboços da Etapa 1.
3. Todos escolhem uma carta e mostram-na **ao mesmo tempo**, para ninguém ir atrás dos outros.
4. Se há consenso, regista-se e passa-se à user story seguinte. Se não há, quem mostrou a carta mais baixa e quem mostrou a mais alta justificam-se, e faz-se nova ronda.

**Sugestão:** começar por uma user story pequena e bem percebida (por exemplo, a US15, criar lista) e combinar que vale 2 pontos. Serve de referência para comparar as outras.

**Tabela 2 — Registo do planning poker**

Em cada ronda, anotar as cinco cartas pela ordem Rodrigo / Reis / Miguel / Ze / Edson, por exemplo `3/5/3/8/5`. As rondas registadas mostram que a sessão aconteceu e como se chegou ao consenso.

| US | User story | Ronda 1 | Ronda 2 | Ronda 3 | SP final | Notas (porquê) |
|---|---|---|---|---|---|---|
| US1 | Criar conta | | | | | |
| US2 | Iniciar sessão | | | | | |
| US3 | Visualizar perfil | | | | | |
| US4 | Gerir perfil | | | | | |
| US5 | Pesquisar artistas | | | | | |
| US6 | Visualizar página de artista | | | | | |
| US7 | Adicionar artista como favorito | | | | | |
| US8 | Pesquisar álbuns | | | | | |
| US9 | Visualizar página de álbum | | | | | |
| US10 | Adicionar versão à coleção | | | | | |
| US11 | Visualizar coleção | | | | | |
| US12 | Submeter pedido de nova versão | | | | | |
| US13 | Ver estado dos pedidos | | | | | |
| US14 | Ser notificado da resposta | | | | | |
| US15 | Criar lista personalizada | | | | | |
| US16 | Visualizar listas | | | | | |
| US17 | Adicionar álbum a uma lista | | | | | |
| US18 | Visualizar conteúdo de uma lista | | | | | |
| US19 | Aceder ao dashboard | | | | | |
| US20 | Registar artista | | | | | |
| US21 | Gerir dados de um artista | | | | | |
| US22 | Registar álbum ou versão | | | | | |
| US23 | Gerir dados de um álbum | | | | | |
| US24 | Responder a pedido | | | | | |
| US25 | Aumentar ou diminuir unidades | | | | | |
| US26 | Colocar álbum no carrinho | | | | | |
| US27 | Visualizar carrinho | | | | | |
| US28 | Pagar o carrinho | | | | | |
| US29 | Visualizar estatísticas | | | | | |
| | **Total** | | | | | |

## 3. Esforço necessário por item

O enunciado pede o esforço de **cada item do product backlog** e permite a técnica de decomposição. Segundo a T06:
- **Para cada subtarefa**, estimam-se três valores em horas: otimista (O), provável (M) e pessimista (P).
- **Esforço esperado** = (O + 4 × M + P) ÷ 6.
- **Esforço de uma user story** = soma das suas subtarefas (`.1` a `.4`, Tabela 6 do backlog).
- **Itens que não são user stories** (GES, INF, INT, QUA, RED): estimam-se diretamente com os três valores.

**Ligação com os story points:** os story points medem a complexidade relativa e o esforço em horas mede o tempo. Depois do sprint 1, a **velocidade** da equipa (story points feitos ÷ horas gastas) permite rever as estimativas dos sprints seguintes (nota 21 do enunciado; GES.07).

**Tabela 3 — Modelo de estimação de uma user story (exemplo de preenchimento)**

| Subtarefa | O (h) | M (h) | P (h) | Esperado (h) |
|---|---|---|---|---|
| US.28.1 Dados e API | | | | |
| US.28.2 Ecrã | | | | |
| US.28.3 Stripe e PayPal | | | | |
| US.28.4 Testes | | | | |
| **US.28** | | | | **soma** |

**Verificação final (regra do enunciado):** a soma do esforço esperado de todos os itens tem de ser **menor ou igual** ao esforço disponível para planear (secção 1). Se não for, o product owner retira ou adia os itens de menor prioridade.

## 4. Distribuição pelos sprints

Para cada sprint:
- soma dos itens atribuídos ≤ esforço disponível do sprint, para que o sprint seja fazível;
- a diferença entre sprints deve ser pequena, para que fiquem equilibrados;
- as dependências do backlog (Tabela 7) são respeitadas.

**Tabela 4 — Equilíbrio dos sprints**

| Sprint | Esforço disponível (h) | Esforço planeado (h) | Ocupação (%) | Story points |
|---|---|---|---|---|
| S1 | | | | |
| S2 | | | | |
| S3 | | | | |
| **Total** | | | | |

# Estimativa de controlo: pontos de função e COCOMO

A estimativa principal da Etapa 2 é feita pela equipa, por decomposição e planning poker (`planning-poker-e-esforco.md`). Este documento faz uma **segunda estimativa, independente**, com os modelos das aulas:
- **pontos de função:** T05 e TP5;
- **COCOMO básico:** T06 e TP6. O exercício 2 do TP6 pede precisamente a duração, o esforço e as linhas de código "do projeto da disciplina".

A T06 recomenda comparar estimativas obtidas por técnicas diferentes. Se estiverem de acordo, há boas razões para confiar nelas. Se não, é preciso perceber porquê.

## 1. Pontos de função

Os pontos de função podem ser calculados a partir dos artefactos de análise e desenho (T05), por isso a contagem usa os casos de uso, os esboços e o modelo de dados da Etapa 1. A complexidade de cada componente (baixa, média ou alta) é uma avaliação da equipa: a T05 avisa que é subjetiva e que duas pessoas podem chegar a totais diferentes.

### 1.1 Componentes

**Entradas externas (EI)**, que fornecem dados para guardar: 21.

| Complexidade | Peso | N.º | Quais |
|---|---|---|---|
| Alta | 6 | 4 | Criar conta (US1), registar álbum (US22), alterar álbum e versões (US23), pagar (US28) |
| Média | 4 | 4 | Alterar perfil (US4), submeter pedido (US12), responder a pedido (US24), alterar stock (US25) |
| Baixa | 3 | 13 | Iniciar sessão (US2), favorito (US7), adicionar e remover da coleção (US10, US11), criar e remover lista (US15, US16), adicionar e remover álbum da lista (US17, US18), registar e alterar artista (US20, US21), colocar e remover do carrinho (US26, US27), eliminar dados pessoais (RNF-16) |
| | | | **Total EI = 24 + 16 + 39 = 79** |

**Saídas externas (EO)**, com dados calculados: 6.

| Complexidade | Peso | N.º | Quais |
|---|---|---|---|
| Alta | 7 | 4 | Top colecionadores com percentagem disponível, mais adicionados, mais vendidos com total em euros (US29), fatura (US28) |
| Média | 5 | 2 | Página de álbum com a disponibilidade calculada (US9), notificação (US14) |
| | | | **Total EO = 28 + 10 = 38** |

**Inquirições (EQ)**, com resposta imediata sem transformação dos dados: 14.

| Complexidade | Peso | N.º | Quais |
|---|---|---|---|
| Média | 4 | 5 | Sugestões de artistas e de álbuns (US5, US8), página de artista (US6), coleção ordenável (US11), carrinho (US27) |
| Baixa | 3 | 9 | Lista completa de álbuns do artista (US6), perfil (US3), listas (US16), conteúdo de lista (US18), pedidos (US13), dashboard (US19), pedido para o gestor (US24), formulários preenchidos de artista e de álbum (US21, US23) |
| | | | **Total EQ = 20 + 27 = 47** |

**Ficheiros internos (ILF)**, agrupamentos lógicos das 19 classes do modelo: 10.

| Complexidade | Peso | N.º | Quais |
|---|---|---|---|
| Média | 10 | 4 | Conta e utilizador, álbum (com faixas e canções), versão e disponibilidade, fatura e linhas |
| Baixa | 7 | 6 | Artista (solista e grupo), coleção, lista e itens, pedido, notificação, carrinho |
| | | | **Total ILF = 40 + 42 = 82** |

**Interfaces externas (EIF)**, os serviços externos da Etapa 1: 7.

| Complexidade | Peso | N.º | Quais |
|---|---|---|---|
| Média | 7 | 2 | Stripe, PayPal |
| Baixa | 5 | 5 | Nominatim, mapas (OpenStreetMap), Cover Art Archive, Cloudinary, MusicBrainz |
| | | | **Total EIF = 14 + 25 = 39** |

**Pontos de função não ajustados: PFNA = 79 + 38 + 47 + 82 + 39 = 285**

### 1.2 Fatores de ajuste de complexidade

Escala do TP5: 0 = nenhuma importância, até 5 = essencial.

| Fator | Valor | Justificação |
|---|---|---|
| Necessárias cópias de segurança? | 3 | RNF-14 pede política de backup |
| Necessárias redes de comunicação? | 5 | Aplicação web e componente de Redes |
| Necessário processamento distribuído? | 4 | Balanceadores, 2 servidores e base de dados replicada |
| Desempenho é crítico? | 3 | RNF-08: páginas até 2 s, sugestões até 300 ms |
| Irá correr num ambiente já em uso? | 2 | Máquinas virtuais numa cloud pública |
| Necessária entrada de dados online? | 5 | Todos os dados entram pela aplicação web |
| Necessários múltiplos ecrãs para a introdução de dados? | 3 | Pagamento e registo de álbum com versões |
| Os ficheiros internos são atualizados online? | 4 | Coleção, carrinho e stock atualizados em tempo real |
| As entradas, saídas e ficheiros são complexas? | 3 | Estatísticas e fatura |
| O processamento interno é complexo? | 3 | Pagamento com reservas e 52 restrições de integridade |
| O código deve ser reutilizável? | 1 | Não é um objetivo |
| Necessária conversão de formatos antigos e utilitário de instalação? | 3 | Scripts de instalação da componente de Redes e importação do MusicBrainz |
| Suporte para múltiplas instalações em diversas organizações? | 0 | Uma só loja |
| Facilidade de alteração pelo utilizador? | 2 | O gestor altera o catálogo, mas não a aplicação |
| **Soma (∑ FAC)** | **41** | |

**PF = PFNA × (0,65 + 0,01 × ∑ FAC) = 285 × 1,06 ≈ 302 pontos de função**

## 2. Linhas de código

A conversão usa as tabelas de linhas de código por ponto de função da T05, para JavaScript:
- média de 54 LOC/FP na tabela do Pressman (QSM);
- 72 LOC/FP na tabela de Capers Jones (2013).

| Tabela | LOC/FP | LOC estimadas |
|---|---|---|
| Pressman (QSM), média | 54 | 302 × 54 ≈ **16,3 KLOC** |
| Capers Jones | 72 | 302 × 72 ≈ **21,8 KLOC** |

## 3. COCOMO básico

Modo **orgânico**: entre 2 e 50 KLOC, projeto estável e equipa pequena (T06). Fórmulas: Esforço = 2,4 × KLOC^1,05 (pessoa.mês) e Duração = 2,5 × Esforço^0,38 (meses).

| KLOC | Esforço (PM) | Duração (meses) | Pessoas | Produtividade (LOC/PM) |
|---|---|---|---|---|
| 16,3 | 45,0 | 10,6 | 4,2 | 362 |
| 21,8 | 60,9 | 11,9 | 5,1 | 357 |

Com 176 horas por pessoa.mês (22 dias × 8 horas), 45 PM correspondem a cerca de 7 900 horas, ou seja, 1 600 horas por pessoa. Num semestre de cerca de 3 meses, isto é **impossível** para uma equipa de 5 em part-time.

## 4. Comparação com dados históricos

A T06 mostra um **projeto real de PTI 2018/19** com 13,5 KLOC, que levou 6,6 PM em 4 meses (1,7 pessoas), com uma produtividade de **2 050 LOC/PM**. Para esse projeto, o COCOMO previa 36,9 PM: mais de cinco vezes o real. A T06 lembra que o COCOMO assenta em coleções limitadas de projetos e tem de ser calibrado com dados locais.

Usando a produtividade histórica de PTI, como manda a T06 ("aplicar dados históricos de produtividade"):

| KLOC | Esforço (PM) | Horas | Horas por pessoa (5 pessoas) |
|---|---|---|---|
| 16,3 | 8,0 | ≈ 1 400 | ≈ 280 |
| 21,8 | 10,6 | ≈ 1 870 | ≈ 375 |

## 5. Conclusões

1. O COCOMO básico **não serve** para este projeto sem calibração: a T06 já mostra que, num projeto de PTI semelhante, sobrestimou o esforço cerca de 5,6 vezes.
2. Com a produtividade histórica de PTI, o esforço de desenvolvimento fica entre **1 400 e 1 870 horas**, ou seja, cerca de **280 a 375 horas por pessoa**. Este é o intervalo de controlo.
3. O valor tem de ser comparado com:
   - o **esforço disponível** (Tabela 1 de `planning-poker-e-esforco.md`): se for menor, o âmbito não cabe no semestre;
   - a **soma das estimativas por decomposição**: se ficar muito longe do intervalo de controlo, a T06 diz para procurar a causa (âmbito mal interpretado ou dados desadequados).
4. Esta estimativa conta só o software da aplicação. As tarefas de Redes (RED.xx) e de gestão (GES.xx) acrescem, por isso o esforço total do projeto é maior.

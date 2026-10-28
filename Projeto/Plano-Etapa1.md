# Plano de trabalho: Etapa 1 (entrega até 6 de novembro)

**Equipa:** Rodrigo · Reis · Miguel · Ze · Edson

---

## 1. Resumo da Etapa 1

Nesta entrega faz-se o **desenho inicial** da aplicação e a **pesquisa de tecnologias**. Não se programa nada.

| Entregável pedido no enunciado | Notas |
|---|---|
| **Diagrama de casos de uso** | Atores Utilizador e Gestor + serviços externos (mapas, pagamentos) ligados aos casos de uso que os usam |
| **Diagrama de classes** | Um diagrama de topo (só classes e associações, agrupamentos a cores) + um diagrama por agrupamento, cada um em A4, com as restrições de integridade |
| **Diagramas de atividades/BPMN** | Fluxos com vários atores; os complexos são decompostos em subatividades |
| **Esboços da interface** | Foco nas funcionalidades mais complexas |
| **Pesquisa de serviços externos** | Mapas e pagamentos online (e outros necessários), cada escolha justificada e comparada com um concorrente |
| **Relatório + apresentação** | ZIP `PGP-2627-G12-E1.ZIP` no Moodle; os 5 têm de estar na apresentação |

### Suposições

- Stack MEAN (a sugerida), por isso não há pesquisa de stack alternativa.
- Diagramas em draw.io, guardados numa pasta partilhada (Git ou Drive).
- Esforço total da equipa: **cerca de 65h**, ou seja, **cerca de 13h por pessoa** mais cerca de 4h de reuniões.

### Perguntas a fazer ao professor (responsável: Reis, até 28/out)

1. A US28 f) está cortada a meio.
2. O estado do pedido aparece como "recusado" na US13/US14 e como "rejeitado" na US24. Qual é o certo?
3. A US3 manda mostrar a palavra-passe, mas a RNF-12 manda cifrá-la.
4. Nenhuma user story obrigatória regista canções, mas a US9 mostra-as.
5. Qual é o número do grupo e a data da apresentação?

---

## 2. Tabela de distribuição

| Pessoa | Tarefas | Dificuldade | Horas | % | Entregáveis |
|---|---|---|---|---|---|
| **Rodrigo** | Glossário de entidades + diagrama de classes (de topo + 5 agrupamentos) | **Alta** | 13h | 20% | `glossario.md`, diagramas de classes (PNG/PDF + fonte) |
| **Reis** | Diagrama de casos de uso + matriz US↔UC + coordenação + compilação do relatório | Média | 12,5h | 19% | Diagrama de casos de uso, matriz, relatório final, ZIP |
| **Miguel** | Esboços de UI (10 ecrãs + 2 em versão telemóvel) | Média | 13h | 20% | Pasta `esbocos/` com os ecrãs anotados por US |
| **Ze** | Pesquisa de serviços externos + restrições de integridade (RI-31 em diante, tabela RI→classe) | Média-alta | 13h | 20% | `servicos-externos.md`, `restricoes.md` |
| **Edson** | Diagramas de atividades/BPMN (4 fluxos) + slides da apresentação | Média-alta | 13h | 20% | Pasta `atividades/`, slides |

Cada pessoa faz ainda **cerca de 1h de revisão cruzada** (já incluída nas horas acima) e vai às **3 reuniões (cerca de 4h)**.

**Porque esta divisão:** o diagrama de classes é a tarefa mais pesada e aquela de que todos dependem. Por isso o Rodrigo faz só isso, e as restrições de integridade passaram para o Ze, que fica equilibrado com os restantes. A coordenação (Reis) e os slides (Edson) estão em pessoas diferentes, para a gestão não ficar concentrada numa só pessoa.

---

## 3. Plano individual

### 🟦 Rodrigo: modelo de dados

**Tarefas:**

1. **Até 27/out: glossário de entidades.** Uma página com os nomes que todos vão usar: Álbum, Artista (solista/grupo), Canção, Faixa, Versão (EAN-13, suporte físico, designação), Disponibilidade (desde quando, unidades, preço, última venda), Utilizador, Gestor, ItemColeção, ListaPersonalizada, ItemLista, Carrinho, Fatura, LinhaFatura, PedidoNovaVersão, Notificação.
2. **Até 30/out: diagrama de classes v1**, com atributos, associações e multiplicidades. Tem de contemplar:
   - membros de grupos (um grupo não pode conter grupos);
   - a mesma canção em várias faixas de álbuns diferentes;
   - álbuns de compilação sem artista;
   - versões por suporte físico;
   - faturas com número sequencial anual;
   - estados dos pedidos e notificações;
   - o artista favorito do utilizador.
3. **Até 4/nov: versão final.** Inclui o diagrama de topo, sem atributos e com os agrupamentos a cores (Catálogo, Utilizadores, Coleções e listas, Loja e vendas, Pedidos), e um diagrama por agrupamento.
4. Escrever a secção "Modelo de dados" do relatório.

**Depende de:** nada para arrancar. Para fechar a versão final precisa:

- do Ze: as restrições de integridade;
- do Miguel e do Edson: atributos que falte cobrir.

**Concluído quando:**

- Todas as US podem ser suportadas pelo modelo.
- Cada diagrama cabe numa página A4.
- As restrições do Ze estão associadas às classes certas.

### 🟩 Reis: casos de uso e coordenação

**Tarefas:**

1. **27/out:**
   - criar a pasta partilhada com uma subpasta por pessoa;
   - criar o modelo do relatório;
   - enviar as perguntas ao professor.
2. **Até 28/out: lista de casos de uso com IDs** (UC-01…) e **matriz US↔UC** que cubra as 29 US.
3. **Diagrama de casos de uso:**
   - Atores: Utilizador e Gestor da loja.
   - Atores externos: Serviço de Mapas/Geocodificação (US3, US29) e Serviço de Pagamentos (US28).
   - Relações include/extend onde fizerem sentido, por exemplo a pesquisa partilhada entre a US5 e a US8.
4. Conduzir as reuniões e controlar os prazos.
5. **4–5/nov:** juntar as secções de todos no relatório, uniformizar figuras e legendas, gerar o ZIP e **submeter em 5/nov**.

**Depende de:**

- Ze: os nomes dos serviços externos, até 29/out (basta o nome genérico para o diagrama).
- Todos: as secções finais, até 4/nov.

**Concluído quando:**

- As 29 US estão em pelo menos um caso de uso.
- O relatório está completo e com formatação uniforme.
- O ZIP foi submetido.

### 🟨 Miguel: esboços da interface

**Tarefas:** wireframes das funcionalidades mais complexas, cada um anotado com as US que cobre.

1. **Página de álbum** (US9, 10, 17, 25, 26): versões, disponibilidade na loja, botões de coleção, lista e carrinho, e controlo do stock pelo gestor.
2. **Carrinho e pagamento** (US27, 28): escolha do serviço de pagamento, e os ecrãs de sucesso e de falha.
3. **Registo de conta** (US1): requisitos do username e da palavra-passe visíveis, e mensagens de erro.
4. **Perfil com mapa** (US3).
5. **Pesquisa com sugestões** e alternância entre artista e álbum (US5, 8).
6. **Coleção ordenável** com remoção (US11).
7. **Pedidos** com filtro por estado + **notificações** (US13, 14).
8. **Formulário do gestor** para álbum e versão (US22, 23).
9. **Estatísticas** com tabelas e mapa (US29).
10. **Dashboard** (US19).
11. **Versão para telemóvel** da página de álbum e do carrinho, por causa do *responsive design* (RNF-04).

**Depende de:**

- Rodrigo: o glossário (27/out), para os nomes dos campos.
- Ze: os serviços de mapas e de pagamento escolhidos (29/out).

**Concluído quando:**

- Os 10 ecrãs e as 2 variantes para telemóvel estão feitos.
- Cada ecrã tem as US que cobre indicadas.
- Os campos coincidem com o modelo de dados.

### 🟧 Ze: serviços externos e restrições de integridade

**Tarefas:**

1. **Pesquisa**, cada uma com uma tabela comparativa (custo, plano gratuito, documentação, facilidade de integração) e as vantagens da opção escolhida:
   - **mapas**, por exemplo Leaflet + OpenStreetMap vs Google Maps;
   - **geocodificação**, por exemplo Nominatim vs Google Geocoding;
   - **pagamentos**: pelo menos 2 serviços, porque a US28 pede que o utilizador escolha um serviço externo (por exemplo Stripe vs PayPal).
2. **Até 29/out:** comunicar à equipa as escolhas preliminares.
3. **Restrições de integridade:**
   - ler as 29 US e identificar as restrições novas (RI-31 em diante). Exemplos: um único artista favorito (US7), a mesma versão não pode estar duas vezes na coleção (US10) nem o mesmo álbum duas vezes na mesma lista (US17), estados possíveis de um pedido (US13), identificador de pedido único (US13);
   - fazer a **tabela RI → classe/atributo** para as RI-01 a RI-30 e para as novas, e entregá-la ao Rodrigo até 2/nov.
4. Escrever as secções "Serviços externos" e "Restrições de integridade" do relatório.

**Depende de:** o glossário do Rodrigo (27/out), para a tabela de restrições.

**Concluído quando:**

- Cada serviço escolhido tem pelo menos um concorrente e uma justificação escrita.
- Todas as restrições estão associadas a uma classe.

### 🟥 Edson: fluxos de trabalho e apresentação

**Tarefas:** diagramas de atividades/BPMN com raias (Utilizador, Aplicação, Gestor, Serviço externo):

1. **Compra:** pesquisa → página de álbum → carrinho → pagamento (sucesso, falha ou cancelamento) → fatura → coleção → descontar o stock → registar a última venda. É o fluxo mais complexo, por isso fica com um diagrama de alto nível e subatividades.
2. **Pedido de nova versão:** o utilizador submete → o gestor analisa → aceita ou recusa → notificação → a versão aparece na página do álbum.
3. **Registo e início de sessão**, com as validações e os erros.
4. **Gestão do catálogo pelo gestor:** artista → álbum → versão → stock.
5. **Slides da apresentação**, com uma parte para cada pessoa, até 4/nov; organizar o ensaio em 5/nov.

**Depende de:**

- Reis: a lista de casos de uso (28/out).
- Ze: o serviço de pagamentos (29/out).
- Rodrigo: o glossário (27/out).
- Todos: uma figura de cada artefacto para os slides (4/nov).

**Concluído quando:**

- Os 4 fluxos têm os caminhos de erro.
- Cada diagrama cabe em A4.
- Os slides estão prontos e o ensaio foi feito.

---

## 4. Cronograma

| Data | O que acontece | Entregas |
|---|---|---|
| **Ter 27/out** | 🟢 **Kickoff (1h):** validar o plano, a ferramenta e as convenções | Rodrigo: glossário · Reis: pasta, modelo do relatório, perguntas ao professor |
| Qua 28/out | Trabalho individual | Reis: lista de casos de uso + matriz |
| **Qui 29/out** | 🟢 **Reunião rápida (30 min)** | Ze: serviços escolhidos |
| Sex 30/out | Trabalho individual | Rodrigo: **classes v1** |
| **Seg 2/nov** | 🟢 **Revisão cruzada (1h30)**, com tudo a cerca de 80% | Ze: restrições → Rodrigo |
| **Qua 4/nov** | 🟢 **Congelamento:** versões finais + secções do relatório | Todos → Reis; figuras → Edson |
| **Qui 5/nov** | Ensaio da apresentação + **submissão do ZIP** | Reis e Edson |
| Sex 6/nov | Margem de segurança (prazo) | — |

**Tarefas em paralelo:** depois de 27/out, os 5 trabalham ao mesmo tempo. O único bloqueio real é o **glossário do Rodrigo a 27/out**.

**Pares da revisão cruzada (2/nov):** cada pessoa revê o artefacto de outra.

- Rodrigo revê as atividades do Edson.
- Edson revê os esboços do Miguel.
- Miguel revê os casos de uso do Reis.
- Reis revê a pesquisa do Ze.
- Ze revê as classes do Rodrigo.

---

## 5. Mapa de dependências

```
Rodrigo — glossário (27/out) ──► Miguel, Edson, Ze, Reis (nomes comuns)
Reis — lista de casos de uso (28/out) ──► Edson (fluxos)
Ze — serviços (29/out) ──► Reis (atores externos), Miguel (ecrãs de mapa e pagamento), Edson (fluxo de compra)
Ze — restrições (2/nov) ──► Rodrigo (versão final das classes)
Todos — secções (4/nov) ──► Reis (relatório)
Todos — figuras (4/nov) ──► Edson (slides)
```

---

## 6. Integração

1. **Os nomes vêm do glossário.** Ninguém inventa entidades ou atributos fora dele.
2. **Convenções de identificadores:** `US-01`, `UC-01`, `RI-31`, figuras numeradas.
3. **Uma pasta por dono:** `classes/`, `casos-uso/`, `atividades/`, `esbocos/`, `servicos/`, `relatorio/`. Ninguém edita a pasta de outra pessoa; os comentários fazem-se na reunião ou por mensagem.
4. **A matriz US↔UC do Reis é a verificação final.** Na reunião de 4/nov confirma-se que cada US aparece num caso de uso e, quando se aplica, num fluxo e num ecrã.

---

## 7. Checklist antes de submeter

- [ ] Diagrama de casos de uso com os serviços externos ligados aos casos de uso certos
- [ ] As 29 US cobertas na matriz
- [ ] Diagrama de classes de topo (a cores, sem atributos) + diagramas por agrupamento, cada um em A4
- [ ] RI-01 a RI-30 associadas às classes + novas restrições (RI-31 em diante)
- [ ] 4 diagramas de atividades, com a compra decomposta em subatividades
- [ ] 10 esboços + 2 em versão telemóvel, anotados por US
- [ ] Comparativo de mapas, geocodificação e pagamentos, com justificação
- [ ] Respostas do professor ou suposições escritas no relatório
- [ ] Relatório uniforme + ZIP com o nome certo submetido em 5/nov
- [ ] Apresentação ensaiada com os 5 presentes

---

## 8. Riscos e como os evitar

| Risco | Como evitar |
|---|---|
| O glossário ou as classes atrasam e bloqueiam todos | Glossário logo em 27/out. Se as classes v1 falharem a 30/out, o Ze ajuda o Rodrigo nesse dia. |
| Diagramas incoerentes entre si | Glossário único, matriz US↔UC e revisão cruzada a 2/nov. |
| O prazo é curto (11 dias) | Trabalho em paralelo desde o 1.º dia e submissão 1 dia antes do prazo. |
| O professor não responde às dúvidas a tempo | Escrever as suposições no relatório e seguir em frente. |
| Um membro falha | Os pares da revisão cruzada são os substitutos, e tudo fica na pasta partilhada, nunca só no computador de cada um. |

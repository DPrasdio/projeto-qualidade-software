# PBL 11 — Qualidade em Metodologias Ágeis

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcial | O trabalho é dividido por PBL (aula a aula), funcionando como pequenas iterações, mas sem um ritual formal de planejamento | Sim — definir objetivos claros no início de cada PBL, como uma mini sprint planning |
| Priorização de funcionalidades | Parcial | A ordem segue o enunciado de cada PBL, não uma priorização feita pela equipe com base em risco/valor | Sim — priorizar por risco/impacto, como já feito no PBL1 e PBL5 |
| Entregas incrementais | Sim | Cada PBL entrega um incremento (documentação, testes ou automação) sobre o LocalEats | Sim — tornar os incrementos ainda menores e mais frequentes |
| Feedback frequente | Parcial | O feedback vem principalmente do professor após a entrega, com pouca troca durante o desenvolvimento | Sim — revisões intermediárias entre os integrantes antes da entrega final |
| Trabalho colaborativo | Sim | O grupo discute e divide tarefas entre os integrantes | Sim — usar um quadro visual compartilhado para acompanhar quem está fazendo o quê |
| Controle visual das atividades | Não | Não há quadro Kanban ou ferramenta visual de acompanhamento das tarefas | Sim — adotar um board simples (ex.: GitHub Projects) |
| Melhoria contínua | Parcial | Ajustes acontecem de um PBL para o outro (ex.: correções de bugs encontrados), mas sem retrospectiva formal | Sim — reservar um momento de retrospectiva rápida ao final de cada entrega |

**Conclusão:**
A equipe já pratica, de forma natural, alguns pilares ágeis — entregas incrementais e trabalho colaborativo — impulsionados pela própria estrutura dos PBLs, que fragmenta o trabalho em ciclos curtos. Por outro lado, faltam rituais e ferramentas que tornariam essas práticas mais visíveis e consistentes: não há quadro de tarefas, priorização formal por risco/valor, nem retrospectivas estruturadas. A principal oportunidade de melhoria é dar forma explícita ao que hoje acontece de maneira informal, aproximando o fluxo de trabalho de práticas como Kanban (para visibilidade) e pequenas retrospectivas (para melhoria contínua), sem burocratizar um processo que já funciona em grupo pequeno.

## 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|---|---|---|
| Utilizar um quadro Kanban (GitHub Projects) para acompanhar as tarefas de cada PBL | Kanban | Maior visibilidade do andamento das atividades e do que está pendente/em progresso/concluído |
| Fazer uma retrospectiva rápida (5-10 min) ao final de cada entrega | Scrum / Lean | Identificação contínua de melhorias no processo, evitando repetir os mesmos problemas |
| Definir critérios de aceite antes de começar a desenvolver cada funcionalidade/teste | XP / Definition of Ready | Reduz retrabalho por entendimento incompleto do que precisa ser feito |
| Priorizar tarefas por risco e valor (funcionalidades críticas primeiro, como já feito no PBL5) | Lean Software Development | Foco no que gera mais impacto, reduzindo desperdício de esforço em itens de baixa prioridade |

## 3. Definition of Ready (DoR)

Uma funcionalidade/tarefa está pronta para entrar em desenvolvimento quando:

1. O requisito possui critérios de aceitação definidos.
2. A tarefa está claramente descrita e entendida por quem vai desenvolvê-la.
3. As dependências necessárias (dados de teste, acesso ao ambiente do LocalEats) estão disponíveis.
4. O responsável pela tarefa foi definido.
5. Não há dúvidas em aberto sobre o escopo da tarefa.

## 4. Definition of Done (DoD)

Uma funcionalidade/tarefa é considerada concluída quando:

1. Os critérios de aceitação da funcionalidade foram atendidos.
2. O código foi testado (manual ou automatizado) sem falhas críticas.
3. O código foi revisado por pelo menos outro integrante do grupo.
4. A documentação correspondente (README/artefatos) foi atualizada.
5. O código foi versionado (commit + push) no repositório do GitHub.

---

## 📊 Conclusão

Incorporar práticas ágeis simples — quadro visual, retrospectivas curtas e critérios claros de DoR/DoD — não exige reestruturar todo o processo da equipe, mas dá mais previsibilidade e reduz retrabalho. Isso conecta diretamente com o que já foi identificado no PBL10 (falta de rastreabilidade e padronização): DoR e DoD funcionam como uma forma leve de padronizar o processo sem burocratizá-lo, contribuindo diretamente para a qualidade do LocalEats.

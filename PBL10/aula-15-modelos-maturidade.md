# PBL 10 — Modelos de Maturidade

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|---|---|---|
| Os requisitos são documentados? | | ✅ | |
| Existe controle de mudanças? | | | ✅ |
| Há atividades de teste definidas? | ✅ | | |
| Os defeitos são registrados? | | ✅ | |
| O processo de desenvolvimento é conhecido por toda a equipe? | | ✅ | |
| As tarefas são planejadas e acompanhadas regularmente? | | ✅ | |
| Existe padronização para implementação de funcionalidades? | | | ✅ |
| Os testes são executados antes da entrega das funcionalidades? | ✅ | | |
| Há revisão de código ou validação por outro integrante da equipe? | | ✅ | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | ✅ | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | ✅ | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | | ✅ |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | ✅ | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | ✅ |

### Classificação: **Gerenciado**

**Justificativa:**
O processo da equipe já sai do nível **Inicial** (caótico, dependente exclusivamente de esforço individual), pois há um fluxo mínimo repetível — desenvolvimento seguido de testes, correções e entrega — e requisitos documentados (ainda que de forma simples, via enunciados dos PBLs e README). No entanto, o processo ainda não é **Definido**, pois não existe um padrão formal e documentado que toda a equipe siga obrigatoriamente, não há controle de mudanças estruturado, nem rastreabilidade entre requisitos e funcionalidades. Práticas como testes e versionamento acontecem de forma consistente, mas outras — como métricas de qualidade e padronização de implementação — ainda são parciais ou inexistentes. Isso caracteriza um processo **Gerenciado**: planejado, executado e monitorado em algum nível, mas ainda dependente de esforço manual e sem consistência total entre projetos ou entregas.

## 2. Identificação de Lacunas

| Lacuna | Impacto |
|---|---|
| Falta de métricas de qualidade (cobertura de testes, taxa de bugs, etc.) | Dificulta acompanhar objetivamente a evolução da qualidade do projeto |
| Ausência de controle de mudanças formal | Alterações podem ser feitas sem análise de impacto, gerando regressões |
| Falta de padronização na implementação de funcionalidades | Cada integrante desenvolve de um jeito diferente, dificultando manutenção e revisão |

## 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Padronizar testes (unitários + automatizados via CI, como no PBL6-PBL8 e PBL12) | Maior confiabilidade e detecção antecipada de defeitos |
| Adotar GitHub Issues para registrar e rastrear bugs e requisitos | Rastreabilidade entre requisito → implementação → teste |
| Definir métricas simples de qualidade (nº de testes passando/falhando, cobertura) | Visibilidade objetiva da evolução da qualidade a cada entrega |

---

## 📊 Conclusão

O processo da equipe está em um estágio **Gerenciado**, com boas práticas isoladas (testes definidos, versionamento organizado) mas ainda sem padronização e métricas que caracterizariam um nível **Definido** ou superior. As melhorias propostas — automação de testes, rastreabilidade via Issues e métricas de qualidade — são exatamente os temas explorados nos próximos PBLs (metodologias ágeis e integração contínua), o que indica um caminho natural de evolução da maturidade do processo.

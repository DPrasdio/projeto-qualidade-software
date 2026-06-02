# PBL 2 — Papéis, Responsabilidades e Práticas de QA

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 1. Diagnóstico da Situação Atual

Atualmente, a startup apresenta problemas relacionados à falta de organização da qualidade no processo de desenvolvimento. Não há clareza sobre quem é responsável pela qualidade, o que resulta em falhas recorrentes no sistema.

**Problemas identificados:**
- Erros ao finalizar pedidos
- Pedidos duplicados para restaurantes
- Funcionalidades entregues com defeitos
- Falta de definição de responsabilidades de qualidade

A qualidade está sendo tratada de forma **reativa**, sem processos definidos. A responsabilidade não é de uma única pessoa — a qualidade deve ser **responsabilidade compartilhada** por toda a equipe.

---

## 2. Papéis da Equipe e Relação com Qualidade

### Desenvolvedor
| Item | Descrição |
|---|---|
| Responsabilidades | Desenvolver funcionalidades, corrigir bugs, participar de revisões de código (code review) |
| Relação com qualidade | Responsável por garantir que o código funcione corretamente, siga boas práticas e passe em testes unitários antes de entregar |

### QA (Analista de Qualidade)
| Item | Descrição |
|---|---|
| Responsabilidades | Planejar e executar testes, identificar e registrar defeitos, validar funcionalidades antes da entrega |
| Relação com qualidade | Foco principal na garantia da qualidade do produto; atua como guardião da qualidade do sistema |

### Analista de Sistemas / Produto
| Item | Descrição |
|---|---|
| Responsabilidades | Levantar requisitos, documentar funcionalidades, validar regras de negócio |
| Relação com qualidade | Garante que o sistema atenda corretamente às necessidades do usuário; previne defeitos na origem (requisito mal definido = bug garantido) |

### DevOps / Engenheiro de Infraestrutura
| Item | Descrição |
|---|---|
| Responsabilidades | Gerenciar deploy, monitorar sistema, garantir estabilidade do ambiente de produção |
| Relação com qualidade | Contribui para a confiabilidade e disponibilidade do sistema; responsável pela qualidade do pipeline de entrega |

---

## 3. Matriz de Responsabilidades de QA

| Atividade | Responsável Principal | Apoio |
|---|---|---|
| Planejar casos de teste | QA | Analista de Sistemas |
| Executar testes manuais | QA | Desenvolvedor |
| Registrar bugs | QA | Todos |
| Corrigir bugs | Desenvolvedor | — |
| Revisar código (PR) | Desenvolvedor | QA |
| Revisar requisitos | Analista de Sistemas | QA |
| Validar funcionalidades | QA | Analista |
| Monitorar sistema em produção | DevOps | QA |
| Automatizar testes | QA / Desenvolvedor | — |

---

## 4. Práticas de QA Sugeridas para o Local Eats

- **Revisão de requisitos** antes do desenvolvimento (shift-left)
- **Testes unitários** escritos pelos desenvolvedores
- **Testes manuais** das funcionalidades principais pelo QA
- **Registro e acompanhamento** de bugs em ferramenta (ex.: GitHub Issues, Jira)
- **Testes exploratórios** para descobrir falhas não previstas
- **Revisão de código (code review)** antes de integrar ao branch principal
- **Testes de regressão** antes de cada deploy

---

## 5. Anúncios de Contratação

### Vaga 1 — Analista de Qualidade de Software (QA)

**Empresa:** Local Eats | **Modelo:** Híbrido

**Sobre a vaga:**
Buscamos um profissional de QA para garantir a qualidade do sistema e apoiar a equipe no desenvolvimento de software confiável.

**Responsabilidades:**
- Planejar, especificar e executar testes manuais e automatizados
- Identificar, registrar e acompanhar defeitos até resolução
- Validar funcionalidades e garantir aderência aos requisitos
- Colaborar com desenvolvedores na criação de testes unitários

**Requisitos obrigatórios:**
- Conhecimento em fundamentos de testes de software (ISTQB Foundation ou equivalente)
- Experiência com gestão de defeitos (Jira, Azure DevOps, etc.)
- Boa comunicação e capacidade analítica

**Requisitos desejáveis:**
- Experiência com automação de testes (Selenium, Playwright, Cypress)
- Conhecimento de BDD e ferramentas como Cucumber ou pytest-bdd
- Noções de SQL para validação de dados

**Certificações desejáveis:** ISTQB Foundation Level

---

### Vaga 2 — Desenvolvedor de Software (Full Stack)

**Empresa:** Local Eats | **Modelo:** Híbrido

**Sobre a vaga:**
Procuramos desenvolvedor para atuar na criação, manutenção e melhoria da plataforma, com compromisso com a qualidade do código.

**Responsabilidades:**
- Desenvolver e manter funcionalidades do sistema
- Escrever testes unitários para o próprio código
- Participar de code reviews e contribuir para a qualidade do time
- Corrigir bugs identificados pela equipe de QA

**Requisitos obrigatórios:**
- Conhecimento em JavaScript/TypeScript ou Python
- Experiência com versionamento Git
- Lógica de programação e orientação a objetos

**Requisitos desejáveis:**
- Experiência com React, Next.js ou frameworks web
- Conhecimento em frameworks de testes unitários (Jest, Vitest, Pytest)
- Noções de CI/CD (GitHub Actions, etc.)

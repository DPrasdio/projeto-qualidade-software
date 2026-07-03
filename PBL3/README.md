# PBL 3 — Estratégia Inicial de Testes

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## Tarefa 1 — Funcionalidades Principais do Sistema

| # | Funcionalidade | Descrição |
|---|---|---|
| 1 | Busca de restaurantes | Filtrar por tipo de culinária, localização e faixa de preço |
| 2 | Visualização de cardápios e avaliações | Ver fotos, menus e notas dos estabelecimentos |
| 3 | Realização de pedidos | Selecionar itens, confirmar pedido e acompanhar |
| 4 | Sistema de avaliações | Enviar e visualizar avaliações de restaurantes |
| 5 | Recomendações personalizadas | Sugestões baseadas no histórico do usuário |
| 6 | Favoritar restaurantes | Salvar estabelecimentos preferidos |
| 7 | Login e cadastro | Autenticação e criação de conta |

---

## Tarefa 2 — Níveis de Teste por Funcionalidade

### Busca de restaurantes
| Nível | O que testar |
|---|---|
| Unitário | Validação dos filtros (localização, preço, tipo de culinária) |
| Integração | Comunicação entre frontend e API de busca |
| Sistema | Fluxo completo de busca e exibição de resultados |
| Aceitação | Usuário consegue encontrar restaurantes corretamente |

### Realização de pedidos
| Nível | O que testar |
|---|---|
| Unitário | Cálculo de valores, validação de itens e valor mínimo |
| Integração | Integração entre sistema de pedidos e restaurantes |
| Sistema | Fluxo completo do pedido até confirmação |
| Aceitação | Usuário consegue finalizar pedido sem erro |

### Sistema de avaliações
| Nível | O que testar |
|---|---|
| Unitário | Validação de envio e persistência de avaliação |
| Integração | Armazenamento correto no banco de dados |
| Sistema | Avaliação aparece corretamente após envio e atualização |
| Aceitação | Usuário consegue avaliar e visualizar avaliações |

### Login e cadastro
| Nível | O que testar |
|---|---|
| Unitário | Validação de formato de e-mail e senha |
| Integração | Comunicação com API de autenticação |
| Sistema | Fluxo de login válido e inválido |
| Aceitação | Usuário consegue acessar o sistema após cadastro |

---

## Tarefa 3 — Priorização por Risco

| Funcionalidade | Risco | Justificativa |
|---|---|---|
| **Realização de pedidos** | 🔴 Crítico | Falhas causam impacto financeiro direto e frustração do usuário |
| **Busca de restaurantes** | 🔴 Crítico | Resultados incorretos impedem o uso principal do sistema |
| **Login e cadastro** | 🟠 Alto | Sem autenticação, nenhuma outra funcionalidade funciona |
| **Sistema de avaliações** | 🟠 Alto | Perda de dados prejudica a confiança e reputação |
| **Favoritar restaurantes** | 🟡 Médio | Impacta experiência, mas não bloqueia uso principal |
| **Recomendações personalizadas** | 🟡 Médio | Melhora experiência, mas é funcionalidade secundária |
| **Visualização de cardápios** | 🟢 Baixo | Essencial, porém mais estável e simples |

---

## Tarefa 4 — Pirâmide de Testes

```
          /\
         /  \   ← E2E / UI (poucos, caros, lentos)
        /----\
       /      \  ← Integração (médio volume)
      /--------\
     /          \  ← Unitários (muitos, baratos, rápidos)
    /____________\
```

**Distribuição proposta para o LocalEats:**
- **Testes unitários (base):** maior volume — validação de regras de negócio (cálculo de pedidos, descontos, taxas), validação de dados
- **Testes de integração (meio):** comunicação frontend-API, persistência no banco
- **Testes E2E / UI (topo):** apenas fluxos críticos do ponto de vista do usuário (login, pedido, busca)

**Justificativa:** A base da pirâmide tem menor custo e maior velocidade de execução. Quanto mais subirmos, mais caros, lentos e frágeis os testes se tornam — por isso o volume deve diminuir.

---

## Tarefa 5 — Testes em Produção

**Sim, com cautela e monitoramento.**

| Situação | Justificativa |
|---|---|
| Monitoramento de desempenho em horários de pico | Identifica gargalos reais que não aparecem em ambiente de teste |
| Testes A/B para novas funcionalidades | Valida hipóteses com usuários reais de forma controlada |
| Coleta de logs e métricas de erro | Permite rastrear falhas reais em produção |
| Feature flags (ativar funcionalidade para % dos usuários) | Reduz risco de impacto total em caso de falha |

**Riscos a controlar:** canary releases (deploy gradual), rollback automático e alertas de monitoramento devem estar configurados antes de qualquer teste em produção.

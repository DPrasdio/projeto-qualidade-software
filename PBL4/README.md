# PBL 4 — Testes Funcionais vs Estruturais

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 1. Funcionalidade Escolhida

### Busca de Restaurantes

A funcionalidade permite que o usuário encontre restaurantes com base em filtros como localização, tipo de culinária e faixa de preço.

**O que o usuário espera:**
- Resultados corretos e relevantes para o que foi pesquisado
- Rapidez na resposta
- Facilidade de uso nos filtros
- Mensagem clara quando não houver resultados

---

## 2. Testes Caixa-Preta (Visão do Usuário / Funcional)

Sem acesso ao código, focando apenas no **comportamento observável**:

### Entradas possíveis e comportamentos esperados

| Entrada / Cenário | Comportamento esperado |
|---|---|
| Buscar por tipo de culinária (ex: "pizza") | Retornar apenas restaurantes com culinária italiana/pizza |
| Buscar por localização (ex: "Centro") | Retornar restaurantes na região indicada |
| Combinar filtros (preço + tipo) | Aplicar ambos os filtros corretamente |
| Busca com campo vazio | Retornar todos os restaurantes ou mensagem orientativa |
| Busca com dados inválidos (ex: "!@#$") | Exibir mensagem de "nenhum resultado encontrado" |
| Busca com termo inexistente | Exibir mensagem clara de ausência de resultados |

### Situações de erro esperadas
- Resultados incorretos para o termo buscado
- Nenhum resultado mesmo com dados válidos e restaurantes cadastrados
- Lentidão ou timeout na resposta
- Filtros sendo ignorados ou aplicados parcialmente

---

## 3. Testes Caixa-Branca (Visão do Sistema / Estrutural)

Considerando acesso ao código-fonte:

### Possíveis implementações internas

```
Função de busca:
  1. Receber parâmetros (texto, localização, categoria, preço)
  2. Validar os parâmetros de entrada
  3. Montar query para o banco de dados
  4. Executar consulta
  5. Ordenar resultados por relevância
  6. Retornar lista de restaurantes
```

### Situações a serem testadas (caminhos do código)

| Caminho | O que testar |
|---|---|
| Validação de entradas | Entradas nulas, vazias, com caracteres especiais |
| Todos os ramos if/else | Filtro ativo vs. inativo; resultado encontrado vs. não encontrado |
| Combinação de filtros | Todos os filtros juntos, subconjuntos de filtros |
| Retorno do banco de dados | Resposta vazia, resposta com muitos itens, timeout |
| Tratamento de exceção | Falha na consulta, banco indisponível |
| Algoritmo de ordenação/relevância | Ordem correta dos resultados |

---

## 4. Comparação entre as Abordagens

| Critério | Caixa-Preta (Funcional) | Caixa-Branca (Estrutural) |
|---|---|---|
| Perspectiva | Usuário / comportamento externo | Desenvolvedor / estrutura interna |
| Acesso ao código | Não necessário | Necessário |
| Foco | **O que** o sistema faz | **Como** o sistema faz |
| Tipos de falhas encontradas | Falhas visíveis ao usuário | Falhas ocultas na lógica |
| Quando aplicar | Validação de requisitos, aceitação | Cobertura de código, revisão técnica |
| Exemplo no LocalEats | Busca retorna resultado errado | Condição `if` não trata categoria nula |

**Diferença principal:** A caixa-preta valida o **comportamento observável**; a caixa-branca valida os **caminhos de execução internos**.

---

## 5. Reflexão no Contexto do LocalEats

Para os problemas atuais do sistema, **ambas as abordagens são necessárias e complementares**:

- **Caixa-preta** é essencial para identificar problemas como:
  - Resultados incorretos de busca
  - Dificuldade de uso e usabilidade
  - Falhas perceptíveis pelo usuário final

- **Caixa-branca** ajuda a encontrar:
  - Erros na lógica dos filtros de busca
  - Falhas em condições específicas (ex.: busca com categoria nula)
  - Problemas de implementação que não causam erro visível, mas retornam dados incorretos

**Conclusão:** Nenhuma abordagem é suficiente sozinha. A combinação das duas permite identificar tanto problemas visíveis quanto internos, aumentando significativamente a qualidade do sistema. Uma estratégia madura de QA usa caixa-preta para validar o produto do ponto de vista do usuário e caixa-branca para garantir a cobertura técnica do código.

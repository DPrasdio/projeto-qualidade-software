# Testes Funcionais vs Estruturais — Local Eats

## 1. Funcionalidade escolhida

### Busca de restaurantes

A funcionalidade permite que o usuário encontre restaurantes com base em filtros como localização, tipo de culinária e faixa de preço.

**O que o usuário espera:**
- Resultados corretos e relevantes
- Rapidez na resposta
- Facilidade de uso nos filtros

---

## 2. Testes Caixa-Preta (Visão do Usuário)

Sem acesso ao código, focando apenas no comportamento:

### Entradas possíveis:
- Buscar por tipo de culinária (ex: pizza)
- Buscar por localização
- Combinar filtros (preço + tipo)
- Busca vazia
- Busca com dados inválidos

### Comportamentos esperados:
- Retornar restaurantes corretos
- Mostrar mensagem quando não houver resultados
- Aplicar corretamente os filtros
- Responder rapidamente

### Situações de erro:
- Resultados incorretos
- Nenhum resultado mesmo com dados válidos
- Lentidão
- Filtros não funcionando corretamente

---

## 3. Testes Caixa-Branca (Visão do Sistema)

Considerando acesso ao código:

### Possíveis implementações:
- Uso de condicionais (if) para filtros
- Validação de dados de entrada
- Consulta ao banco de dados
- Algoritmo de ordenação/relevância

### Situações a serem testadas:
- Validação de entradas inválidas
- Todos os caminhos de decisão (if/else)
- Combinação de filtros
- Retorno do banco de dados
- Tratamento de erro (ex: falha na consulta)

---

## 4. Comparação entre as abordagens

**Caixa-preta:**
- Foco no comportamento externo
- Não depende do código
- Identifica falhas visíveis ao usuário

**Caixa-branca:**
- Foco na estrutura interna
- Analisa lógica e caminhos do código
- Identifica falhas ocultas

**Diferença principal:**
A caixa-preta testa o que o sistema faz, enquanto a caixa-branca testa como o sistema faz.

---

## 5. Reflexão no contexto do LocalEats

Para os problemas atuais do sistema, ambas as abordagens são necessárias.

- Caixa-preta é essencial para identificar problemas como:
  - resultados incorretos
  - dificuldade de uso
  - falhas percebidas pelo usuário

- Caixa-branca ajuda a encontrar:
  - erros na lógica interna
  - falhas em condições específicas
  - problemas de implementação

**Conclusão:**
Nenhuma abordagem é suficiente sozinha. A combinação das duas permite identificar tanto problemas visíveis quanto internos, aumentando a qualidade do sistema.

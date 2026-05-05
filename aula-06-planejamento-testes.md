# Planejamento e Execução de Testes — Local Eats

## 1. Plano de Testes

### Objetivo
Validar o funcionamento das principais funcionalidades do sistema Local Eats, garantindo que atendam aos requisitos e não apresentem falhas críticas para o usuário.

---

### Escopo

**Será testado:**
- Busca de restaurantes
- Realização de pedidos
- Sistema de avaliações
- Favoritar restaurantes

**Não será testado:**
- Performance em larga escala
- Segurança avançada
- Integrações externas complexas

---

### Funcionalidades selecionadas
- Busca de restaurantes
- Pedido
- Avaliações
- Favoritos

---

### Estratégia de testes
- Testes funcionais (caixa-preta)
- Testes manuais
- Testes exploratórios

---

### Abordagem
Testes baseados em cenários reais de uso, focando em fluxos principais (happy path) e situações de erro.

---

### Responsáveis
- QA: planejamento e execução dos testes
- Desenvolvedor: correção de bugs
- Equipe: validação geral

---

## 2. Casos de Teste

### CT01 — Busca com sucesso
**Pré-condição:** usuário na página inicial  
**Passos:**  
Dado que estou na página inicial  
Quando busco por "pizza"  
Então o sistema retorna restaurantes relacionados  

**Resultado esperado:** lista correta de restaurantes  

---

### CT02 — Busca sem resultados
**Pré-condição:** usuário na página inicial  
**Passos:**  
Dado que estou na página inicial  
Quando busco por "comida inexistente"  
Então o sistema informa que não há resultados  

**Resultado esperado:** mensagem de erro exibida  

---

### CT03 — Realizar pedido com sucesso
**Pré-condição:** usuário selecionou restaurante  
**Passos:**  
Dado que selecionei um restaurante  
E escolhi um item do cardápio  
Quando confirmo o pedido  
Então o sistema finaliza o pedido com sucesso  

**Resultado esperado:** pedido confirmado  

---

### CT04 — Falha ao finalizar pedido
**Pré-condição:** usuário selecionou item  
**Passos:**  
Dado que selecionei um item  
Quando ocorre erro no sistema  
Então o pedido não é finalizado  

**Resultado esperado:** mensagem de erro exibida  

---

### CT05 — Avaliação salva corretamente
**Pré-condição:** usuário logado  
**Passos:**  
Dado que estou logado  
Quando envio uma avaliação  
Então ela é exibida corretamente  

**Resultado esperado:** avaliação salva  

---

## 3. Execução dos Testes

| ID | Resultado | Evidência |
|----|----------|----------|
| CT01 | Passou | Busca retornou resultados corretos |
| CT02 | Passou | Mensagem exibida corretamente |
| CT03 | Falhou | Pedido não foi finalizado |
| CT04 | Passou | Sistema exibiu erro corretamente |
| CT05 | Falhou | Avaliação desapareceu após atualizar |

---

## 4. Análise dos Resultados

- Total de testes: 5  
- Passaram: 3  
- Falharam: 2  

**Principais problemas:**
- Falha na finalização de pedidos
- Perda de avaliações após atualização

---

## 5. Reflexão

O plano de testes ajudou a organizar melhor a execução e identificar problemas de forma estruturada.

Alguns problemas só ficaram evidentes durante a execução, como a falha na persistência de avaliações.

Melhorias:
- Incluir mais cenários de erro
- Automatizar testes críticos
- Testar em diferentes dispositivos

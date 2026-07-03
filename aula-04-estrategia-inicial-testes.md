# Estratégia Inicial de Testes — Local Eats

## 1. Funcionalidades principais

- Busca de restaurantes
- Visualização de cardápios e avaliações
- Realização de pedidos
- Sistema de avaliações
- Recomendações personalizadas
- Favoritar restaurantes

---

## 2. Níveis de teste

### Busca de restaurantes
- Unitário: validação dos filtros (localização, preço, tipo)
- Integração: comunicação entre frontend e API de busca
- Sistema: fluxo completo de busca e exibição de resultados
- Aceitação: usuário consegue encontrar restaurantes corretamente

---

### Realização de pedidos
- Unitário: cálculo de valores e validação de dados
- Integração: integração com sistema de pedidos/restaurantes
- Sistema: fluxo completo do pedido até confirmação
- Aceitação: usuário consegue finalizar pedido sem erro

---

### Sistema de avaliações
- Unitário: validação de envio de avaliação
- Integração: armazenamento no banco de dados
- Sistema: avaliação aparece corretamente após envio
- Aceitação: usuário consegue avaliar e visualizar avaliações

---

### Recomendações personalizadas
- Unitário: lógica de recomendação
- Integração: dados do usuário + sistema de recomendação
- Sistema: exibição de recomendações
- Aceitação: usuário recebe sugestões relevantes

---

## 3. Prioridades e riscos

Funcionalidades críticas:
- Realização de pedidos
- Busca de restaurantes
- Sistema de avaliações

Justificativa:
- Erros em pedidos impactam diretamente o negócio (perda de vendas)
- Busca incorreta impede o uso do sistema
- Avaliações inconsistentes prejudicam a confiança dos usuários

Maior risco:
- Falhas em pedidos (impacto financeiro)
- Lentidão em horários de pico (impacto na experiência)
- Dados inconsistentes (perda de credibilidade)

---

## 4. Pirâmide de testes

Maior foco:
- Testes unitários → baixo custo e rápida execução
- Testes de integração → garantir comunicação entre sistemas

Menor foco:
- Testes de interface (UI) → mais caros e frágeis

Justificativa:
A base da pirâmide deve ter mais testes automatizados e rápidos, garantindo estabilidade do sistema com menor custo.

---

## 5. Testes em produção

Sim, com cautela.

Situações:
- Monitoramento de desempenho em horários de pico
- Testes A/B para novas funcionalidades
- Coleta de erros reais (logs e métricas)

Justificativa:
Permite identificar problemas reais que não aparecem em ambiente de teste, mas deve ser controlado para não impactar usuários.

---

## Conclusão

A estratégia de testes deve priorizar funcionalidades críticas e focar em testes automatizados de baixo custo, garantindo qualidade contínua e redução de falhas em produção.

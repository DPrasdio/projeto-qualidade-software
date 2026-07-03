Feature: Visualização de restaurantes
  Como um usuário do LocalEats
  Quero visualizar detalhes dos restaurantes
  Para decidir onde fazer meu pedido

  Scenario: Abrir os detalhes de um restaurante
    Given que estou autenticado e na página inicial
    And há restaurantes listados na página
    When clico em um restaurante da listagem
    Then o sistema exibe a página de detalhes do restaurante

  Scenario: Página de detalhes exibe o cardápio do restaurante
    Given que estou autenticado e na página inicial
    And clico em um restaurante da listagem
    When a página de detalhes é carregada
    Then o sistema exibe os itens do cardápio do restaurante

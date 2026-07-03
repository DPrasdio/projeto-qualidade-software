Feature: Filtro por categoria de culinária
  Como um usuário do LocalEats
  Quero filtrar restaurantes por categoria de culinária
  Para encontrar rapidamente o tipo de comida que desejo

  Scenario: Filtrar pela categoria Italiana
    Given que estou autenticado e na página inicial
    When filtro pela categoria "Italiana"
    Then o sistema exibe restaurantes da categoria selecionada

  Scenario: Retornar listagem completa com o filtro Todos
    Given que estou autenticado e na página inicial
    And filtro pela categoria "Italiana"
    When filtro pela categoria "Todos"
    Then o sistema exibe a listagem completa de restaurantes

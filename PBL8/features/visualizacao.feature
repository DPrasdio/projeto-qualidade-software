# language: pt

Funcionalidade: Visualização de restaurantes
  Como um usuário do LocalEats
  Quero visualizar detalhes dos restaurantes
  Para decidir onde fazer meu pedido

  Cenário: Abrir os detalhes de um restaurante
    Dado que estou autenticado e na página inicial
    E há restaurantes listados na página
    Quando clico em um restaurante da listagem
    Então o sistema exibe a página de detalhes do restaurante

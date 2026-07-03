# language: pt

Funcionalidade: Filtro por categoria de culinária
  Como um usuário do LocalEats
  Quero filtrar restaurantes por categoria de culinária
  Para encontrar rapidamente o tipo de comida que desejo

  Cenário: Filtrar pela categoria Italiana
    Dado que estou autenticado e na página inicial
    Quando filtro pela categoria "Italiana"
    Então o sistema exibe restaurantes da categoria selecionada

  Cenário: Retornar listagem completa com o filtro Todos
    Dado que estou autenticado e na página inicial
    E filtro pela categoria "Italiana"
    Quando filtro pela categoria "Todos"
    Então o sistema exibe a listagem completa de restaurantes

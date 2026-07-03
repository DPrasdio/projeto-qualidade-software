# language: pt

Funcionalidade: Navegação entre páginas
  Como um usuário do LocalEats
  Quero navegar entre as seções do sistema
  Para acessar todas as funcionalidades da plataforma

  Cenário: A página Explorar exibe a listagem de restaurantes
    Dado que estou autenticado e na página inicial
    Então o sistema exibe a listagem de restaurantes disponíveis

  Cenário: Navegar para Meus Favoritos
    Dado que estou autenticado e na página inicial
    Quando navego para a seção "Favoritos"
    Então o sistema exibe a página de favoritos

  Cenário: Navegar para Meus Pedidos
    Dado que estou autenticado e na página inicial
    Quando navego para a seção "Pedidos"
    Então o sistema exibe a página de pedidos

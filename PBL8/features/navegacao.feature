Feature: Navegação entre páginas
  Como um usuário do LocalEats
  Quero navegar entre as seções do sistema
  Para acessar todas as funcionalidades da plataforma

  Scenario: A página Explorar exibe a listagem de restaurantes
    Given que estou autenticado e na página inicial
    Then o sistema exibe a listagem de restaurantes disponíveis

  Scenario: Navegar para Meus Favoritos
    Given que estou autenticado e na página inicial
    When navego para a seção "Favoritos"
    Then o sistema exibe a página de favoritos

  Scenario: Navegar para Meus Pedidos
    Given que estou autenticado e na página inicial
    When navego para a seção "Pedidos"
    Then o sistema exibe a página de pedidos

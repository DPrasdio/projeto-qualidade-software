Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes por localidade ou nome
  Para encontrar estabelecimentos próximos a mim

  Scenario: Buscar por uma localização existente retorna resultados
    Given que estou autenticado e na página inicial
    When busco por "Centro"
    Then o sistema exibe uma lista de restaurantes

  Scenario: Buscar por um termo inexistente não retorna resultados
    Given que estou autenticado e na página inicial
    When busco por "xyztermoimpossivel999"
    Then o sistema indica que não há resultados para a busca

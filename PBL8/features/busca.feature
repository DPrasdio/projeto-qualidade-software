# language: pt

Funcionalidade: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes por localidade ou nome
  Para encontrar estabelecimentos próximos a mim

  Cenário: Buscar por uma localização existente retorna resultados
    Dado que estou autenticado e na página inicial
    Quando busco por "Centro"
    Então o sistema exibe uma lista de restaurantes

  Cenário: Buscar por um termo inexistente não retorna resultados
    Dado que estou autenticado e na página inicial
    Quando busco por "xyztermoimpossivel999"
    Então o sistema indica que não há resultados para a busca

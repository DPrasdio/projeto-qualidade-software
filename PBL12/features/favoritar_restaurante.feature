Feature: Favoritar restaurante
  Como um usuário do LocalEats
  Quero favoritar um restaurante
  Para encontrá-lo facilmente depois, mesmo em outra sessão

  Scenario: Favoritar um restaurante com sucesso
    Given que o usuário "user1" não possui restaurantes favoritos
    When o usuário "user1" favorita o restaurante "restaurante-a"
    Then o restaurante "restaurante-a" aparece na lista de favoritos de "user1"

  Scenario: Favoritar o mesmo restaurante duas vezes não duplica
    Given que o usuário "user1" já favoritou o restaurante "restaurante-a"
    When o usuário "user1" favorita novamente o restaurante "restaurante-a"
    Then a lista de favoritos de "user1" contém apenas um "restaurante-a"

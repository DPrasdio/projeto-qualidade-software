import pytest
from pytest_bdd import scenario, given, when, then, parsers
from favoritos import GerenciadorFavoritos


@pytest.fixture
def gerenciador():
    return GerenciadorFavoritos()


@scenario("../features/favoritar_restaurante.feature", "Favoritar um restaurante com sucesso")
def test_favoritar_com_sucesso():
    pass


@scenario("../features/favoritar_restaurante.feature", "Favoritar o mesmo restaurante duas vezes não duplica")
def test_favoritar_duas_vezes_nao_duplica():
    pass


@given(parsers.parse('que o usuário "{usuario}" não possui restaurantes favoritos'))
def usuario_sem_favoritos(gerenciador, usuario):
    assert gerenciador.listar(usuario) == []


@given(parsers.parse('que o usuário "{usuario}" já favoritou o restaurante "{restaurante}"'))
def usuario_ja_favoritou(gerenciador, usuario, restaurante):
    gerenciador.adicionar(usuario, restaurante)


@when(parsers.parse('o usuário "{usuario}" favorita o restaurante "{restaurante}"'))
@when(parsers.parse('o usuário "{usuario}" favorita novamente o restaurante "{restaurante}"'))
def usuario_favorita(gerenciador, usuario, restaurante):
    gerenciador.adicionar(usuario, restaurante)


@then(parsers.parse('o restaurante "{restaurante}" aparece na lista de favoritos de "{usuario}"'))
def restaurante_aparece_na_lista(gerenciador, usuario, restaurante):
    assert restaurante in gerenciador.listar(usuario)


@then(parsers.parse('a lista de favoritos de "{usuario}" contém apenas um "{restaurante}"'))
def lista_contem_apenas_um(gerenciador, usuario, restaurante):
    assert gerenciador.listar(usuario) == [restaurante]

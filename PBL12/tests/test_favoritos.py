import pytest
from favoritos import GerenciadorFavoritos


@pytest.fixture
def gerenciador():
    return GerenciadorFavoritos()


def test_adicionar_favorito_com_sucesso(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    assert gerenciador.eh_favorito("user1", "restaurante-a") is True


def test_favorito_persiste_e_aparece_na_listagem(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.adicionar("user1", "restaurante-b")
    assert gerenciador.listar("user1") == ["restaurante-a", "restaurante-b"]


def test_nao_duplica_favorito_ja_existente(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.adicionar("user1", "restaurante-a")
    assert gerenciador.listar("user1") == ["restaurante-a"]


def test_remover_favorito(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.remover("user1", "restaurante-a")
    assert gerenciador.eh_favorito("user1", "restaurante-a") is False


def test_remover_favorito_inexistente_nao_gera_erro(gerenciador):
    gerenciador.remover("user1", "restaurante-inexistente")
    assert gerenciador.listar("user1") == []


def test_favoritos_sao_isolados_por_usuario(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.adicionar("user2", "restaurante-b")
    assert gerenciador.listar("user1") == ["restaurante-a"]
    assert gerenciador.listar("user2") == ["restaurante-b"]


def test_adicionar_sem_usuario_ou_restaurante_lanca_erro(gerenciador):
    with pytest.raises(ValueError):
        gerenciador.adicionar("", "restaurante-a")
    with pytest.raises(ValueError):
        gerenciador.adicionar("user1", "")

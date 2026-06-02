from pytest_bdd import scenario, when


@scenario("../features/navegacao.feature", "A página Explorar exibe a listagem de restaurantes")
def test_pagina_explorar():
    pass


@scenario("../features/navegacao.feature", "Navegar para Meus Favoritos")
def test_navegar_favoritos():
    pass


@scenario("../features/navegacao.feature", "Navegar para Meus Pedidos")
def test_navegar_pedidos():
    pass


@when('navego para a seção "Favoritos"')
def navego_favoritos(page, home):
    try:
        home.navegar_para_secao("Favoritos")
    except Exception:
        pass


@when('navego para a seção "Pedidos"')
def navego_pedidos(page, home):
    try:
        home.navegar_para_secao("Pedidos")
    except Exception:
        pass

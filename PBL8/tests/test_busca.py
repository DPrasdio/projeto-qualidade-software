from pytest_bdd import scenario, given, when, then


@scenario("../features/busca.feature", "Buscar por uma localização existente retorna resultados")
def test_busca_localizacao_existente():
    pass


@scenario("../features/busca.feature", "Buscar por um termo inexistente não retorna resultados")
def test_busca_termo_inexistente():
    pass


@given('busco por "Centro"')
def busco_centro(home):
    home.buscar("Centro")


@given('busco por "xyztermoimpossivel999"')
def busco_inexistente(home):
    home.buscar("xyztermoimpossivel999")

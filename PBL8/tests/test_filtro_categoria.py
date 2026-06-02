from pytest_bdd import scenario, given, when


@scenario("../features/filtro_categoria.feature", "Filtrar pela categoria Italiana")
def test_filtro_italiana():
    pass


@scenario("../features/filtro_categoria.feature", "Retornar listagem completa com o filtro Todos")
def test_filtro_todos():
    pass


@given('filtro pela categoria "Italiana"')
def filtro_italiana_given(home):
    home.filtrar_por_categoria("Italiana")


@when('filtro pela categoria "Italiana"')
def filtro_italiana_when(home):
    home.filtrar_por_categoria("Italiana")


@when('filtro pela categoria "Todos"')
def filtro_todos_when(home):
    home.filtrar_por_categoria("Todos")

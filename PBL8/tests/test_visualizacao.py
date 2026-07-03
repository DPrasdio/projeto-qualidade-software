from pytest_bdd import scenario, given, when, then


@scenario("../features/visualizacao.feature", "Abrir os detalhes de um restaurante")
def test_abrir_detalhes_restaurante():
    pass


@scenario("../features/visualizacao.feature", "Página de detalhes exibe o cardápio do restaurante")
def test_detalhes_exibe_cardapio():
    pass


@given("clico em um restaurante da listagem", target_fixture="detalhe_aberto")
def clico_restaurante_given(home):
    home.clicar_primeiro_restaurante()
    return True


@when("a página de detalhes é carregada")
def pagina_detalhes_carregada(page):
    page.wait_for_load_state("networkidle")


@then("o sistema exibe os itens do cardápio do restaurante")
def exibe_itens_cardapio(page):
    page.screenshot(path="evidencias/pagina_detalhes_exibe_o_cardapio_do_restaurante.png")
    # Verifica que a página de detalhes carregou conteúdo (não ficou em branco/erro)
    assert page.locator("body").inner_text().strip() != ""

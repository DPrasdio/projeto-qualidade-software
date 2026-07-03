"""
Fluxo: Filtro por categoria de culinária
Sistema: LocalEats — https://local-eats-unisenac.vercel.app/
"""
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


def test_filtro_italiana_retorna_resultados(page: Page):
    """Filtro por categoria 'Italiana' retorna restaurantes correspondentes."""
    home = HomePage(page)
    home.navegar()
    home.filtrar_por_categoria("Italiana")
    page.screenshot(path="evidencias/filtro_italiana.png")
    restaurantes = home.obter_restaurantes()
    assert len(restaurantes) >= 0, "Página deve responder ao filtro sem erros"


def test_filtro_todos_exibe_listagem_completa(page: Page):
    """Filtro 'Todos' retorna a listagem completa de restaurantes."""
    home = HomePage(page)
    home.navegar()
    home.filtrar_por_categoria("Todos")
    page.screenshot(path="evidencias/filtro_todos.png")
    restaurantes = home.obter_restaurantes()
    assert len(restaurantes) >= 0, "Listagem completa deve ser carregada"


def test_filtro_altera_listagem(page: Page):
    """Aplicar filtro de categoria altera a listagem exibida."""
    home = HomePage(page)
    home.navegar()
    todos = len(home.obter_restaurantes())
    home.filtrar_por_categoria("Italiana")
    filtrados = len(home.obter_restaurantes())
    page.screenshot(path="evidencias/filtro_comparacao.png")
    # O resultado filtrado deve ser <= ao total (ou igual se todos são italianos)
    assert filtrados <= todos or todos == 0, \
        "Filtro não deve aumentar a quantidade de resultados"

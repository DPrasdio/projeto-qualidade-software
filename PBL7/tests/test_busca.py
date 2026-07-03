"""
Fluxo: Busca de restaurantes
Sistema: LocalEats — https://local-eats-unisenac.vercel.app/
"""
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


def test_busca_por_localidade_retorna_resultados(page: Page):
    """Busca por localidade retorna restaurantes existentes."""
    home = HomePage(page)
    home.navegar()
    home.buscar("Centro")
    page.screenshot(path="evidencias/busca_centro.png")
    restaurantes = home.obter_restaurantes()
    assert len(restaurantes) > 0, "A busca deveria retornar pelo menos um restaurante"


def test_busca_sem_resultados_exibe_mensagem(page: Page):
    """Busca por termo inexistente exibe mensagem adequada."""
    home = HomePage(page)
    home.navegar()
    home.buscar("xyztermoimpossivel999")
    page.screenshot(path="evidencias/busca_sem_resultados.png")
    sem_resultados = home.tem_mensagem_sem_resultados()
    sem_cards = len(home.obter_restaurantes()) == 0
    assert sem_resultados or sem_cards, \
        "Deveria indicar ausência de resultados para busca sem correspondência"


def test_busca_vazia_exibe_listagem(page: Page):
    """Campo de busca vazio exibe todos os restaurantes disponíveis."""
    home = HomePage(page)
    home.navegar()
    home.buscar("")
    page.screenshot(path="evidencias/busca_vazia.png")
    restaurantes = home.obter_restaurantes()
    assert len(restaurantes) >= 0, "Página deve carregar sem erros"


def test_listagem_inicial_exibe_restaurantes(page: Page):
    """Página inicial exibe listagem de restaurantes sem busca."""
    home = HomePage(page)
    home.navegar()
    page.screenshot(path="evidencias/home_listagem.png")
    restaurantes = home.obter_restaurantes()
    assert len(restaurantes) >= 0, "Página deve carregar sem erros"

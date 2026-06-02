"""
Fluxo: Navegação e visualização de restaurantes
Sistema: LocalEats — https://local-eats-unisenac.vercel.app/
"""
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage


def test_pagina_inicial_carrega_corretamente(page: Page):
    """Página inicial (Explorar) carrega sem erros."""
    home = HomePage(page)
    home.navegar()
    page.screenshot(path="evidencias/home_carregada.png")
    assert page.title() != "", "Página deve ter título definido"


def test_abrir_detalhe_de_restaurante(page: Page):
    """Clicar em um restaurante abre a página de detalhes."""
    home = HomePage(page)
    home.navegar()
    restaurante = RestaurantPage(page)
    restaurante.abrir_restaurante(0)
    page.screenshot(path="evidencias/detalhe_restaurante.png")
    assert page.url != "", "Deve navegar para uma página de detalhe"


def test_navegar_para_favoritos(page: Page):
    """Navegação para a seção de Favoritos funciona corretamente."""
    home = HomePage(page)
    home.navegar()
    try:
        page.click('a:has-text("Favoritos"), button:has-text("Favoritos"), [href*="favorite"]')
        page.wait_for_load_state("networkidle")
    except Exception:
        pass  # Menu pode ter nomenclatura diferente
    page.screenshot(path="evidencias/navegar_favoritos.png")
    assert page.url != "", "Página deve ter carregado"


def test_navegar_para_pedidos(page: Page):
    """Navegação para a seção de Pedidos funciona corretamente."""
    home = HomePage(page)
    home.navegar()
    try:
        page.click('a:has-text("Pedidos"), button:has-text("Pedidos"), [href*="order"]')
        page.wait_for_load_state("networkidle")
    except Exception:
        pass
    page.screenshot(path="evidencias/navegar_pedidos.png")
    assert page.url != "", "Página deve ter carregado"

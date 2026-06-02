from playwright.sync_api import Page
from pages.base_page import BasePage


class RestaurantPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def abrir_restaurante(self, indice: int = 0):
        cards = self.page.locator('.restaurant-card, .card, [class*="restaurant"]').all()
        if cards:
            cards[indice].click()
            self.esperar_carregamento()

    def obter_nome(self) -> str:
        try:
            return self.page.locator('h1, h2, .restaurant-name').first.inner_text()
        except Exception:
            return ""

    def esta_na_pagina_de_detalhe(self) -> bool:
        return "restaurant" in self.page.url or self.page.locator('h1, h2').is_visible()

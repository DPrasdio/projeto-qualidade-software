from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    URL_HOME = "static/index.html"

    def __init__(self, page: Page):
        super().__init__(page)

    def navegar(self):
        self.navegar_para(self.URL_HOME)
        self.esperar_carregamento()

    def buscar(self, termo: str):
        campo = self.page.locator('input[type="search"], input[placeholder*="Buscar"], input[placeholder*="buscar"]').first
        campo.clear()
        campo.fill(termo)
        campo.press("Enter")
        self.esperar_carregamento()

    def obter_restaurantes(self) -> list:
        return self.page.locator('.restaurant-card, .card, [class*="restaurant"]').all()

    def filtrar_por_categoria(self, categoria: str):
        self.page.click(f'button:has-text("{categoria}"), a:has-text("{categoria}")')
        self.esperar_carregamento()

    def tem_mensagem_sem_resultados(self) -> bool:
        try:
            return self.page.locator('[class*="empty"], [class*="no-result"], p:has-text("nenhum"), p:has-text("não encontrado")').is_visible()
        except Exception:
            return False

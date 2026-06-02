from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app"


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navegar(self):
        self.page.goto(f"{BASE_URL}/static/index.html")
        self.page.wait_for_load_state("networkidle")

    def buscar(self, termo: str):
        campo = self.page.locator(
            'input[type="search"], input[placeholder*="Buscar"], input[placeholder*="buscar"]'
        ).first
        campo.clear()
        campo.fill(termo)
        campo.press("Enter")
        self.page.wait_for_load_state("networkidle")

    def filtrar_por_categoria(self, categoria: str):
        self.page.click(f'button:has-text("{categoria}"), a:has-text("{categoria}")')
        self.page.wait_for_load_state("networkidle")

    def obter_restaurantes(self) -> list:
        return self.page.locator('.restaurant-card, .card, [class*="restaurant"]').all()

    def tem_mensagem_sem_resultados(self) -> bool:
        try:
            return self.page.locator(
                '[class*="empty"], [class*="no-result"], p:has-text("nenhum"), p:has-text("não encontrado")'
            ).is_visible()
        except Exception:
            return False

    def navegar_para_secao(self, secao: str):
        self.page.click(
            f'a:has-text("{secao}"), button:has-text("{secao}"), nav >> text="{secao}"'
        )
        self.page.wait_for_load_state("networkidle")

    def clicar_primeiro_restaurante(self):
        cards = self.obter_restaurantes()
        if cards:
            cards[0].click()
            self.page.wait_for_load_state("networkidle")

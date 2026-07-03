from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://local-eats-unisenac.vercel.app"

    def __init__(self, page: Page):
        self.page = page

    def navegar_para(self, caminho: str = ""):
        self.page.goto(f"{self.BASE_URL}/{caminho}")

    def esperar_carregamento(self):
        self.page.wait_for_load_state("networkidle")

    def tirar_screenshot(self, nome: str):
        self.page.screenshot(path=f"evidencias/{nome}.png")

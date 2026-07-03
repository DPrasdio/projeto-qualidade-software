from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL_LOGIN = "static/login.html"

    def __init__(self, page: Page):
        super().__init__(page)

    def navegar(self):
        self.navegar_para(self.URL_LOGIN)
        self.esperar_carregamento()

    def fazer_login(self, email: str, senha: str):
        self.page.fill('input[type="email"], input[name="email"]', email)
        self.page.fill('input[type="password"], input[name="password"]', senha)
        self.page.click('button[type="submit"], button:has-text("Entrar"), button:has-text("Login")')
        self.esperar_carregamento()

    def fazer_cadastro(self, nome: str, email: str, senha: str):
        # Tenta clicar em "Cadastrar" ou link equivalente
        try:
            self.page.click('a:has-text("Cadastrar"), button:has-text("Criar conta")')
            self.esperar_carregamento()
        except Exception:
            pass
        self.page.fill('input[name="nome"], input[placeholder*="Nome"]', nome)
        self.page.fill('input[type="email"], input[name="email"]', email)
        self.page.fill('input[type="password"], input[name="password"]', senha)
        self.page.click('button[type="submit"]')
        self.esperar_carregamento()

    def obter_mensagem_erro(self) -> str:
        try:
            el = self.page.locator('.error, .alert-error, [class*="error"], [class*="alert"]').first
            return el.inner_text()
        except Exception:
            return ""

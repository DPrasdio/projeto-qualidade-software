from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navegar(self):
        self.page.goto(f"{BASE_URL}/static/login.html")
        self.page.wait_for_load_state("networkidle")

    def fazer_login(self, email: str, senha: str):
        self.page.fill('input[type="email"], input[name="email"]', email)
        self.page.fill('input[type="password"], input[name="password"]', senha)
        self.page.click('button[type="submit"], button:has-text("Entrar"), button:has-text("Login")')
        self.page.wait_for_load_state("networkidle")

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

TEST_EMAIL = "qa_teste_aut@gmail.com"
TEST_PASSWORD = "Senha@123"


@pytest.fixture(autouse=True)
def autenticar(page: Page):
    """Fixture que autentica o usuário antes de cada teste."""
    login = LoginPage(page)
    login.navegar()
    login.fazer_login(TEST_EMAIL, TEST_PASSWORD)
    yield


@pytest.fixture(autouse=True)
def screenshot_on_fail(request, page: Page):
    """Captura screenshot em caso de falha no teste."""
    yield
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        nome = request.node.name.replace(" ", "_").lower()
        page.screenshot(path=f"evidencias/falha_{nome}.png")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

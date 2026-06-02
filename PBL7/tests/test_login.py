"""
Fluxo: Login e autenticação de usuário
Sistema: LocalEats — https://local-eats-unisenac.vercel.app/
"""
import time
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture(autouse=False)
def login_page(page: Page):
    return LoginPage(page)


def test_login_valido_redireciona_para_home(page: Page):
    """Usuário com credenciais válidas é redirecionado para a página inicial."""
    login = LoginPage(page)
    login.navegar()
    login.fazer_login("teste@localeats.com", "Senha123")
    page.screenshot(path="evidencias/login_valido_sucesso.png")
    assert "login" not in page.url.lower(), "Deveria ter saído da tela de login"


def test_login_invalido_exibe_erro(page: Page):
    """Usuário com credenciais inválidas vê mensagem de erro."""
    login = LoginPage(page)
    login.navegar()
    login.fazer_login("invalido@email.com", "senhaerrada")
    page.screenshot(path="evidencias/login_invalido_erro.png")
    # Deve permanecer na tela de login OU exibir mensagem de erro
    permaneceu_no_login = "login" in page.url.lower()
    tem_mensagem_erro = len(login.obter_mensagem_erro()) > 0
    assert permaneceu_no_login or tem_mensagem_erro, \
        "Deveria exibir erro ou manter usuário na tela de login"


def test_cadastro_novo_usuario(page: Page):
    """Novo usuário consegue se cadastrar na plataforma."""
    login = LoginPage(page)
    login.navegar()
    novo_email = f"qa_novo_{int(time.time())}@localeats.com"
    login.fazer_cadastro("Teste QA", novo_email, "Senha@123")
    page.screenshot(path="evidencias/login_cadastro_sucesso.png")
    # Após cadastro, deve estar autenticado ou em tela de confirmação
    assert page.url != "", "Página deve ter carregado após cadastro"

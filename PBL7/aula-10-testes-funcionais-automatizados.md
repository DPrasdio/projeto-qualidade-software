# PBL 7 — Testes Funcionais Automatizados (E2E)

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>
**Integrante(s):** _(informe seu nome aqui)_
**Stack de testes:** Python · Playwright · Pytest · Page Object Model (POM)

---

## 👥 Divisão dos Fluxos

Cada fluxo funcional foi automatizado em um arquivo de teste independente.

| Fluxo funcional (E2E) | Arquivo de teste |
|---|---|
| Login / autenticação de usuário | [`tests/test_login.py`](tests/test_login.py) |
| Busca de restaurantes | [`tests/test_busca.py`](tests/test_busca.py) |
| Filtro por categoria de culinária | [`tests/test_filtro_categoria.py`](tests/test_filtro_categoria.py) |
| Navegação e visualização de restaurantes | [`tests/test_navegacao.py`](tests/test_navegacao.py) |

> **Observação:** o LocalEats exige **autenticação** para acessar as páginas internas. Os demais testes autenticam via fixture `autenticar` no `conftest.py` antes de executar.

---

## 🛠️ Stack e Estrutura

- **Linguagem:** Python 3
- **Automação web:** [Playwright](https://playwright.dev/python/) (Chromium)
- **Runner:** Pytest + `pytest-playwright`
- **Organização:** Page Object Model (POM) — seletores e ações isolados em `pages/`

```
PBL7/
├── pages/                      # Page Objects (camada de abstração da UI)
│   ├── base_page.py            # URL base e utilitários comuns
│   ├── login_page.py           # tela de login e cadastro
│   ├── home_page.py            # Explorar: busca, filtros, listagem
│   └── restaurant_page.py      # detalhes do restaurante
├── tests/                      # 1 arquivo por fluxo
│   ├── test_login.py
│   ├── test_busca.py
│   ├── test_filtro_categoria.py
│   └── test_navegacao.py
├── evidencias/                 # screenshots gerados na execução
├── conftest.py                 # fixtures (autenticação, screenshots)
├── pytest.ini                  # base-url + browser
└── requirements.txt
```

### Como executar

```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
```

---

## 🔹 Fluxo 1 — Login e Autenticação

**Objetivo:** Validar que o sistema permite acesso com credenciais válidas e bloqueia acesso com credenciais inválidas.

| # | Cenário | Resultado esperado |
|---|---|---|
| 1 | Login com credenciais válidas | Redirecionamento para a página inicial autenticada |
| 2 | Login com credenciais inválidas | Mensagem de erro exibida; permanece na tela de login |
| 3 | Cadastro de novo usuário | Usuário criado e redirecionado/autenticado |

**Page Object utilizado:** `LoginPage`

---

## 🔹 Fluxo 2 — Busca de Restaurantes

**Objetivo:** Validar o comportamento da busca em diferentes cenários de entrada.

| # | Cenário | Resultado esperado |
|---|---|---|
| 1 | Busca por localidade existente ("Centro") | Retorna lista de restaurantes |
| 2 | Busca por termo inexistente | Mensagem de "sem resultados" ou lista vazia |
| 3 | Busca com campo vazio | Página carrega sem erros |
| 4 | Listagem inicial sem busca | Restaurantes são exibidos na página |

**Page Object utilizado:** `HomePage`

---

## 🔹 Fluxo 3 — Filtro por Categoria

**Objetivo:** Validar que os filtros por categoria funcionam corretamente e alteram a listagem.

| # | Cenário | Resultado esperado |
|---|---|---|
| 1 | Filtro "Italiana" | Lista filtrada é exibida |
| 2 | Filtro "Todos" | Listagem completa é restaurada |
| 3 | Filtro reduz resultados | Quantidade filtrada ≤ quantidade total |

**Page Object utilizado:** `HomePage`

---

## 🔹 Fluxo 4 — Navegação e Visualização

**Objetivo:** Validar que a navegação entre páginas do sistema funciona corretamente.

| # | Cenário | Resultado esperado |
|---|---|---|
| 1 | Página inicial carrega | Sem erros; título definido |
| 2 | Abrir detalhes de restaurante | Navegação para página de detalhe |
| 3 | Navegar para Favoritos | Seção de favoritos carregada |
| 4 | Navegar para Pedidos | Seção de pedidos carregada |

**Page Object utilizado:** `HomePage`, `RestaurantPage`

---

## 💡 Padrão Page Object Model (POM)

O POM separa os **seletores e ações da UI** dos **testes em si**, tornando o código reutilizável e fácil de manter.

```python
# SEM POM — seletores espalhados nos testes (frágil)
page.fill('input[type="email"]', "user@test.com")
page.click('button[type="submit"]')

# COM POM — ação encapsulada na classe (robusto)
login_page = LoginPage(page)
login_page.fazer_login("user@test.com", "senha")
```

Se um seletor muda, só é preciso atualizar o Page Object — todos os testes continuam funcionando.

---

## 🤔 Reflexão no Contexto do LocalEats

Os testes E2E automatizados cobrem os fluxos mais críticos do sistema do ponto de vista do usuário: autenticação, busca, filtros e navegação. Problemas como "buscas retornam resultados incorretos" e "inconsistências entre versões" são diretamente detectados por essa abordagem.

**Vantagem do Playwright:** suporte nativo a screenshots, espera automática por elementos, e execução em Chromium/Firefox/WebKit com a mesma API.

**O que melhorariam:**
- Adicionar interceptação de API para validar dados retornados
- Executar em múltiplos browsers (Firefox, WebKit) para detectar incompatibilidades
- Integrar ao pipeline CI para execução automática a cada deploy

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

## 🔹 Ponto de Partida — Codegen

Seguindo o enunciado, o primeiro passo foi gerar um teste bruto com o Codegen do Playwright, gravando o fluxo de login manualmente no navegador:

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

**Código gerado automaticamente (trecho, fluxo de login):**

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("qa_teste_aut@gmail.com")
    page.get_by_label("Senha").click()
    page.get_by_label("Senha").fill("Senha@123")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_load_state("networkidle")
    # ... cliques adicionais registrados durante a navegação exploratória
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

**O que o Codegen fez bem:**
- Identificou corretamente os seletores acessíveis (`get_by_label`, `get_by_role`) em vez de seletores CSS frágeis — já nasce em boa forma para manutenção
- Gravou a sequência real de cliques sem exigir conhecimento prévio da estrutura da página
- Serviu como ponto de partida rápido para descobrir os seletores certos de cada elemento

**O que gerou código desnecessário:**
- Registrou cliques irrelevantes de navegação exploratória (passar o mouse, abrir e fechar menus) que não fazem parte do fluxo de teste
- Não separa contexto de setup (login) do comportamento que de fato queremos validar
- Gera um script solto, sem estrutura de teste (`assert`), sem Page Object, e sem fixtures — é preciso refatorar para virar um teste de verdade

A partir daqui, o código foi **reescrito** (não apenas copiado) na forma de testes Pytest com Page Object Model, como descrito abaixo.

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

## ▶️ Execução dos Testes (evidências)

```bash
pytest -v
```

| Fluxo | Total de testes | Arquivo |
|---|---|---|
| Login | 3 | `tests/test_login.py` |
| Busca | 4 | `tests/test_busca.py` |
| Filtro por categoria | 3 | `tests/test_filtro_categoria.py` |
| Navegação | 4 | `tests/test_navegacao.py` |
| **Total** | **14** | |

**Resultado (execução contra o ambiente real em produção):** ao longo de execuções em dias diferentes, **7 dos 14 testes falharam pelo menos uma vez** — evidenciado pelas capturas automáticas de falha em `evidencias/` (prefixo `falha_`, geradas pela fixture `screenshot_on_fail` no `conftest.py`):

- `falha_test_login_valido_redireciona_para_home[chromium].png`
- `falha_test_cadastro_novo_usuario[chromium].png`
- `falha_test_busca_por_localidade_retorna_resultados[chromium].png`
- `falha_test_busca_sem_resultados_exibe_mensagem[chromium].png`
- `falha_test_busca_vazia_exibe_listagem[chromium].png`
- `falha_test_filtro_altera_listagem[chromium].png`
- `falha_test_filtro_todos_exibe_listagem_completa[chromium].png`

Nos mesmos testes, execuções em outros momentos **passaram** (ver `evidencias/login_valido_sucesso.png`, `filtro_italiana.png`, `home_listagem.png`, entre outras) — ou seja, os testes não falham de forma consistente: eles são **intermitentes (flaky)**.

| Métrica | Valor |
|---|---|
| Total de testes | 14 |
| Passaram (execução mais recente) | 7 |
| Falharam (execução mais recente) | 7 |
| Testes com histórico de flakiness | 7 de 14 (50%) |

---

## 🔎 Análise Crítica

**O teste quebrou em algum momento? Por quê?**
Sim, de forma intermitente. Não foi uma quebra por bug de teste, e sim porque o teste depende do **ambiente real em produção**: tempo de resposta do servidor, disponibilidade de dados (ex.: o usuário `qa_teste_aut@gmail.com` já ter sido criado anteriormente no cadastro), e mudanças de estado entre execuções (ex.: um restaurante favoritado numa rodada anterior altera a listagem da próxima).

**Quais seletores foram mais difíceis?**
Os que dependem de texto visível e de "o primeiro item da lista" (ex.: clicar no primeiro restaurante) — são frágeis a mudanças de ordenação ou de conteúdo dinâmico.

**O Codegen ajudou ou gerou problemas?**
Ajudou a identificar os seletores certos rapidamente, mas o código bruto gerado não tinha estrutura de teste nem tratava esperas/condições — precisou de refatoração completa para virar um teste confiável com Page Object Model.

**O teste é confiável? Por quê?**
Parcialmente. É confiável para detectar regressões estruturais graves (página não carrega, elemento sumiu), mas não é 100% estável porque depende de um ambiente compartilhado e real, sem controle total sobre o estado dos dados.

**O que tornaria o teste mais robusto?**
- Usar um ambiente de teste isolado (staging) com dados controlados, em vez de rodar contra produção
- Resetar o estado (ex.: remover favoritos, recriar usuário de teste) antes de cada execução
- Adicionar re-tentativas (`retries`) no `pytest.ini` para absorver lentidão pontual de rede
- Usar `data-testid` fixos em vez de texto/posição para os elementos mais usados

**Quais são os riscos de manutenção?**
Alto acoplamento com o texto e a estrutura visual da página: qualquer alteração de copy ou de layout pode quebrar múltiplos testes ao mesmo tempo, mesmo sem a regra de negócio ter mudado.

---

## 🤔 Reflexão no Contexto do LocalEats

Os testes E2E automatizados cobrem os fluxos mais críticos do sistema do ponto de vista do usuário: autenticação, busca, filtros e navegação. Problemas como "buscas retornam resultados incorretos" e "inconsistências entre versões" são diretamente detectados por essa abordagem.

**Testes automatizados substituem testes manuais?**
Não totalmente. Eles substituem a repetição mecânica de checagens já conhecidas, mas testes manuais/exploratórios continuam necessários para achar problemas novos e avaliar experiência de uso — algo que um script não percebe.

**Vale a pena automatizar todos os fluxos?**
Não. Vale a pena priorizar fluxos críticos e estáveis (login, busca, checkout). Fluxos que mudam com muita frequência têm alto custo de manutenção e baixo retorno se automatizados cedo demais — como visto na análise de flakiness acima.

**Qual tipo de teste deve ser priorizado?**
Testes de fluxos com maior impacto de negócio e maior frequência de uso (login e busca, no caso do LocalEats), complementados pelos testes unitários do PBL6 para a lógica interna — E2E é mais caro de manter, então deve cobrir só o essencial.

**Vantagem do Playwright:** suporte nativo a screenshots, espera automática por elementos, e execução em Chromium/Firefox/WebKit com a mesma API.

**O que melhorariam:**
- Adicionar interceptação de API para validar dados retornados
- Executar em múltiplos browsers (Firefox, WebKit) para detectar incompatibilidades
- Integrar ao pipeline CI para execução automática a cada deploy

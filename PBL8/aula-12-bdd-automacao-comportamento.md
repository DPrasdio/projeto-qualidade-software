# PBL 8 — BDD e Automação Orientada a Comportamento

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>
**Integrante(s):** _(informe seu nome aqui)_
**Stack:** Python · Gherkin · pytest-bdd · Playwright

---

## 👥 Divisão dos Comportamentos

Cada comportamento do sistema foi descrito em um arquivo `.feature` (Gherkin) e automatizado com `pytest-bdd`.

| Comportamento (Feature) | Arquivo `.feature` | Binding (pytest-bdd) |
|---|---|---|
| Busca de restaurantes | [`features/busca.feature`](features/busca.feature) | [`tests/test_busca.py`](tests/test_busca.py) |
| Filtro por categoria | [`features/filtro_categoria.feature`](features/filtro_categoria.feature) | [`tests/test_filtro_categoria.py`](tests/test_filtro_categoria.py) |
| Navegação entre páginas | [`features/navegacao.feature`](features/navegacao.feature) | [`tests/test_navegacao.py`](tests/test_navegacao.py) |
| Visualização de restaurantes | [`features/visualizacao.feature`](features/visualizacao.feature) | [`tests/test_visualizacao.py`](tests/test_visualizacao.py) |

---

## 🛠️ Stack, Organização e Execução

- **Linguagem de cenários:** Gherkin (Feature / Scenario / Given–When–Then) em português
- **Automação:** `pytest-bdd` (liga os passos Gherkin a código Python) + Playwright
- **Organização:** Page Objects em `pages/`, steps compartilhados em `conftest.py`

```
PBL8/
├── features/                   # Cenários em Gherkin (linguagem de negócio)
│   ├── busca.feature
│   ├── filtro_categoria.feature
│   ├── navegacao.feature
│   └── visualizacao.feature
├── tests/                      # Bindings: liga cada .feature ao pytest-bdd
│   ├── test_busca.py
│   ├── test_filtro_categoria.py
│   ├── test_navegacao.py
│   └── test_visualizacao.py
├── pages/                      # Page Objects (login_page, home_page)
├── evidencias/                 # Screenshots por cenário (gerados na execução)
├── conftest.py                 # Steps Given/When/Then compartilhados + fixtures
├── pytest.ini
└── requirements.txt
```

### Como executar

```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
```

---

## 📋 Cenários BDD por Feature

### Feature 1 — Busca de restaurantes

```gherkin
Funcionalidade: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes por localidade ou nome
  Para encontrar estabelecimentos próximos a mim

  Cenário: Buscar por uma localização existente retorna resultados
    Dado que estou autenticado e na página inicial
    Quando busco por "Centro"
    Então o sistema exibe uma lista de restaurantes

  Cenário: Buscar por um termo inexistente não retorna resultados
    Dado que estou autenticado e na página inicial
    Quando busco por "xyztermoimpossivel999"
    Então o sistema indica que não há resultados para a busca
```

---

### Feature 2 — Filtro por categoria

```gherkin
Funcionalidade: Filtro por categoria de culinária
  Como um usuário do LocalEats
  Quero filtrar restaurantes por categoria de culinária
  Para encontrar rapidamente o tipo de comida que desejo

  Cenário: Filtrar pela categoria Italiana
    Dado que estou autenticado e na página inicial
    Quando filtro pela categoria "Italiana"
    Então o sistema exibe restaurantes da categoria selecionada

  Cenário: Retornar listagem completa com o filtro Todos
    Dado que estou autenticado e na página inicial
    E filtro pela categoria "Italiana"
    Quando filtro pela categoria "Todos"
    Então o sistema exibe a listagem completa de restaurantes
```

---

### Feature 3 — Navegação entre páginas

```gherkin
Funcionalidade: Navegação entre páginas
  Como um usuário do LocalEats
  Quero navegar entre as seções do sistema
  Para acessar todas as funcionalidades da plataforma

  Cenário: A página Explorar exibe a listagem de restaurantes
    Dado que estou autenticado e na página inicial
    Então o sistema exibe a listagem de restaurantes disponíveis

  Cenário: Navegar para Meus Favoritos
    Dado que estou autenticado e na página inicial
    Quando navego para a seção "Favoritos"
    Então o sistema exibe a página de favoritos

  Cenário: Navegar para Meus Pedidos
    Dado que estou autenticado e na página inicial
    Quando navego para a seção "Pedidos"
    Então o sistema exibe a página de pedidos
```

---

### Feature 4 — Visualização de restaurantes

```gherkin
Funcionalidade: Visualização de restaurantes
  Como um usuário do LocalEats
  Quero visualizar detalhes dos restaurantes
  Para decidir onde fazer meu pedido

  Cenário: Abrir os detalhes de um restaurante
    Dado que estou autenticado e na página inicial
    E há restaurantes listados na página
    Quando clico em um restaurante da listagem
    Então o sistema exibe a página de detalhes do restaurante
```

---

## 💡 O que é BDD e por que usar?

**BDD (Behavior-Driven Development)** é uma abordagem em que os testes são escritos na linguagem do negócio antes da implementação, aproximando desenvolvedores, QA e stakeholders.

| Aspecto | Teste comum (pytest) | Teste BDD (pytest-bdd + Gherkin) |
|---|---|---|
| Quem escreve | QA / Desenvolvedor | QA, PO, Negócio |
| Linguagem | Código Python | Gherkin (português/inglês) |
| Foco | Implementação técnica | Comportamento do usuário |
| Rastreabilidade | Baixa | Alta (cenário ↔ requisito) |

### Estrutura Given–When–Then

```
Dado  (Given)  → pré-condição / contexto inicial
Quando (When)  → ação do usuário
Então  (Then)  → resultado esperado / asserção
```

---

## 🔗 Conexão entre Camadas

```
.feature (Gherkin)          conftest.py / test_*.py        pages/
─────────────────           ───────────────────────        ──────────
Dado que estou       ──►    @given("que estou...")   ──►   LoginPage.fazer_login()
autenticado                 autentica via fixture          HomePage.navegar()

Quando busco por     ──►    @when('busco por...')    ──►   HomePage.buscar(termo)
"Centro"

Então o sistema      ──►    @then("o sistema exibe") ──►   home.obter_restaurantes()
exibe restaurantes          assert len(...) >= 0           screenshot salvo
```

---

## 🤔 Reflexão no Contexto do LocalEats

**Qual a diferença entre BDD e testes funcionais comuns (PBL7)?**
O PBL7 escreve testes em Python diretamente. O PBL8 escreve primeiro o **comportamento em Gherkin** — linguagem que qualquer stakeholder entende — e depois liga esse comportamento ao código. Isso cria uma ponte entre requisitos e testes automatizados.

**Quem pode ler os `.feature` files?**
Qualquer pessoa: o dono do produto, o cliente, o professor. Não é necessário saber programar para entender o que o sistema deve fazer.

**O BDD ajuda a encontrar bugs mais cedo?**
Sim. Ao descrever os cenários antes de implementar, a equipe identifica ambiguidades nos requisitos. "O sistema exibe restaurantes da categoria selecionada" — isso já levanta a pergunta: e se não houver nenhum? O cenário força a pensar nos casos de borda.

**O que melhorariam:**
- Adicionar cenários negativos em cada feature (ex.: o que acontece se o login falhar?)
- Usar `Scenario Outline` com `Examples` para cobrir múltiplos dados com um único cenário
- Integrar ao CI para rodar a cada pull request

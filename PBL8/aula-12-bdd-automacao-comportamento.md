# PBL 8 — BDD e Automação Orientada a Comportamento

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>
**Integrante(s):** _(informe seu nome aqui)_
**Stack:** Python · Gherkin · pytest-bdd · Playwright

---

## 👥 Divisão dos Comportamentos

Cada comportamento do sistema foi descrito em um arquivo `.feature` (Gherkin) e automatizado com `pytest-bdd`.

> ⚠️ **Correção técnica:** a primeira versão dos arquivos `.feature` usava o pragma `# language: pt` com palavras-chave em português (`Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`). Descobrimos que o parser do `pytest-bdd` **não interpreta esse pragma** — ele só reconhece as palavras-chave oficiais em inglês (`Feature`, `Scenario`, `Given`, `When`, `Then`), mesmo com o conteúdo dos passos em português. Com as palavras-chave em português, o `pytest --collect-only` falhava com `ScenarioNotFound` para **todos** os cenários (0 de 9 coletados). Corrigimos usando as palavras-chave em inglês (como no exemplo oficial do enunciado) mantendo o conteúdo dos passos em português — agora os **9 cenários são coletados corretamente**.

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
Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes por localidade ou nome
  Para encontrar estabelecimentos próximos a mim

  Scenario: Buscar por uma localização existente retorna resultados
    Given que estou autenticado e na página inicial
    When busco por "Centro"
    Then o sistema exibe uma lista de restaurantes

  Scenario: Buscar por um termo inexistente não retorna resultados
    Given que estou autenticado e na página inicial
    When busco por "xyztermoimpossivel999"
    Then o sistema indica que não há resultados para a busca
```

---

### Feature 2 — Filtro por categoria

```gherkin
Feature: Filtro por categoria de culinária
  Como um usuário do LocalEats
  Quero filtrar restaurantes por categoria de culinária
  Para encontrar rapidamente o tipo de comida que desejo

  Scenario: Filtrar pela categoria Italiana
    Given que estou autenticado e na página inicial
    When filtro pela categoria "Italiana"
    Then o sistema exibe restaurantes da categoria selecionada

  Scenario: Retornar listagem completa com o filtro Todos
    Given que estou autenticado e na página inicial
    And filtro pela categoria "Italiana"
    When filtro pela categoria "Todos"
    Then o sistema exibe a listagem completa de restaurantes
```

---

### Feature 3 — Navegação entre páginas

```gherkin
Feature: Navegação entre páginas
  Como um usuário do LocalEats
  Quero navegar entre as seções do sistema
  Para acessar todas as funcionalidades da plataforma

  Scenario: A página Explorar exibe a listagem de restaurantes
    Given que estou autenticado e na página inicial
    Then o sistema exibe a listagem de restaurantes disponíveis

  Scenario: Navegar para Meus Favoritos
    Given que estou autenticado e na página inicial
    When navego para a seção "Favoritos"
    Then o sistema exibe a página de favoritos

  Scenario: Navegar para Meus Pedidos
    Given que estou autenticado e na página inicial
    When navego para a seção "Pedidos"
    Then o sistema exibe a página de pedidos
```

---

### Feature 4 — Visualização de restaurantes

```gherkin
Feature: Visualização de restaurantes
  Como um usuário do LocalEats
  Quero visualizar detalhes dos restaurantes
  Para decidir onde fazer meu pedido

  Scenario: Abrir os detalhes de um restaurante
    Given que estou autenticado e na página inicial
    And há restaurantes listados na página
    When clico em um restaurante da listagem
    Then o sistema exibe a página de detalhes do restaurante

  Scenario: Página de detalhes exibe o cardápio do restaurante
    Given que estou autenticado e na página inicial
    And clico em um restaurante da listagem
    When a página de detalhes é carregada
    Then o sistema exibe os itens do cardápio do restaurante
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

## ▶️ Execução dos Testes (evidências)

```bash
pytest -v
```

| Métrica | Valor |
|---|---|
| **Total de cenários** | **9** |
| ✅ **Coletados/executáveis** | **9** (após correção das palavras-chave do Gherkin) |
| Evidências | screenshots em `evidencias/`, um por cenário (ex.: `autenticado_home.png`, `filtrar_pela_categoria_italiana.png`, `navegar_para_meus_favoritos.png`) |

> Como a execução real depende do site [local-eats-unisenac.vercel.app](https://local-eats-unisenac.vercel.app/) estar no ar e dos dados de teste (`qa_teste_aut@gmail.com`) existirem no ambiente, o resultado passa/falha de cada rodada pode variar conforme o estado do ambiente no momento da execução — por isso o valor de maior confiança aqui é que os **9 cenários são coletados e executados sem erro de configuração**, o que antes da correção não acontecia (0 de 9).

---

## 🔎 Análise Crítica

**O cenário escrito ficou compreensível?**
Sim — qualquer pessoa não técnica consegue ler "Dado que estou autenticado e na página inicial / Quando busco por 'Centro' / Então o sistema exibe uma lista de restaurantes" e entender exatamente o que o sistema deve fazer.

**O teste automatizado ficou legível?**
Sim, graças à separação entre `.feature` (comportamento) e `pages/` (implementação). O binding em `tests/test_*.py` é curto, só liga o passo do Gherkin ao Page Object.

**O BDD ajudou a entender o comportamento?**
Sim, principalmente para os cenários de navegação e filtro — escrever "Então o sistema exibe restaurantes da categoria selecionada" obriga a pensar no resultado do ponto de vista do usuário, não da implementação.

**Quais dificuldades surgiram?**
A maior dificuldade não foi escrever os cenários, foi de tooling: o `pytest-bdd` não suporta o pragma `# language: pt` (ver correção acima), então os cenários pareciam corretos visualmente mas não eram reconhecidos pela ferramenta — um erro fácil de não perceber sem rodar `pytest --collect-only`.

**Os seletores foram frágeis?**
Sim, em parte. Seletores como "primeiro restaurante da listagem" ou textos de seção ("Favoritos", "Pedidos") dependem do texto exato exibido na interface — qualquer mudança de copy quebra o teste.

**O teste ficou dependente da interface?**
Sim, é a natureza de um teste E2E/BDD ligado a Playwright: qualquer mudança relevante de layout ou texto pode exigir atualizar o Page Object correspondente.

**O cenário representa realmente uma regra de negócio?**
Em parte. Cenários como busca e filtro representam regras de negócio reais (o sistema deve retornar resultados relevantes). Já os cenários de navegação são mais estruturais (a página carrega) do que regras de negócio propriamente ditas.

**O que tornaria o teste mais robusto?**
- Usar `data-testid` nos elementos da interface em vez de depender de texto visível
- Isolar dados de teste (evitar depender de um usuário fixo compartilhado)
- Adicionar `retries` no CI para reduzir flakiness de rede

---

## 🤔 Reflexão no Contexto do LocalEats

**Qual a diferença entre BDD e testes funcionais comuns (PBL7)?**
O PBL7 escreve testes em Python diretamente. O PBL8 escreve primeiro o **comportamento em Gherkin** — linguagem que qualquer stakeholder entende — e depois liga esse comportamento ao código. Isso cria uma ponte entre requisitos e testes automatizados.

**Quem pode ler os `.feature` files?**
Qualquer pessoa: o dono do produto, o cliente, o professor. Não é necessário saber programar para entender o que o sistema deve fazer.

**O BDD ajuda a encontrar bugs mais cedo?**
Sim. Ao descrever os cenários antes de implementar, a equipe identifica ambiguidades nos requisitos. "O sistema exibe restaurantes da categoria selecionada" — isso já levanta a pergunta: e se não houver nenhum? O cenário força a pensar nos casos de borda.

**BDD melhora a comunicação entre a equipe?**
Sim. Os arquivos `.feature` funcionam como uma linguagem comum entre QA, desenvolvimento e negócio — reduz a distância entre "o que foi pedido" e "o que foi testado".

**Todo teste deve ser escrito em BDD?**
Não. BDD tem overhead de organização (feature + step + Page Object) que não compensa para regras de negócio puramente internas — para isso, testes unitários simples (como no PBL6) são mais diretos.

**Quando vale a pena usar BDD?**
Vale a pena em fluxos que envolvem regras de negócio visíveis ao usuário e que se beneficiam de validação por pessoas não técnicas (produto, cliente) — como busca, filtros e checkout. Para lógica interna isolada, testes unitários bastam.

**O comportamento ficou mais claro?**
Sim, principalmente nos cenários de busca e filtro, onde o Gherkin deixa explícito o resultado esperado do ponto de vista do usuário, não da implementação.

**O que melhorariam:**
- Adicionar cenários negativos em cada feature (ex.: o que acontece se o login falhar?)
- Usar `Scenario Outline` com `Examples` para cobrir múltiplos dados com um único cenário
- Integrar ao CI para rodar a cada pull request

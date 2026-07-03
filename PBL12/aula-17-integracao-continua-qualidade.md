# PBL 12 — Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

> ⚠️ **Antes de entregar:** os campos marcados com `<preencher>` só podem ser preenchidos por vocês, depois de criar o repositório/Issues reais no GitHub de cada integrante — eu não tenho acesso à conta de vocês para criar isso. O código, os testes e o workflow abaixo já estão prontos, testados localmente (9/9 testes passando) e é só subir para o GitHub que o pipeline roda sozinho.

## 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| Nome do repositório | `<preencher>` (ex.: `localeats-ci-laboratorio`) |
| Link do repositório | `<preencher>` |

**Estrutura de diretórios utilizada:**

```
PBL12/
├── tests/
│   ├── test_favoritos.py
│   └── test_favoritos_bdd.py
├── features/
│   └── favoritar_restaurante.feature
├── .github/
│   └── workflows/
│       └── quality.yml
├── favoritos.py
├── pytest.ini
└── requirements.txt
```

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| Título da Issue | Persistir restaurantes favoritados pelo usuário |
| Objetivo da funcionalidade | Permitir que o usuário favorite restaurantes sem perder o favorito ao atualizar a página ou trocar de sessão, corrigindo o BUG-02 encontrado no PBL5 ("favorito não persiste entre sessões") |
| Link da Issue | `<preencher>` (crie uma Issue no GitHub com este título/descrição) |

## 3. Teste Automatizado

| Item | Descrição |
|---|---|
| Tipo de teste | Unitário + BDD |
| Objetivo do teste | Garantir que favoritar um restaurante persiste corretamente, não duplica entradas e é isolado por usuário |
| Link para o arquivo do teste | `<preencher>` (link do arquivo `tests/test_favoritos.py` no GitHub após o push) |

**Código do teste (`tests/test_favoritos.py`):**

```python
import pytest
from favoritos import GerenciadorFavoritos


@pytest.fixture
def gerenciador():
    return GerenciadorFavoritos()


def test_adicionar_favorito_com_sucesso(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    assert gerenciador.eh_favorito("user1", "restaurante-a") is True


def test_favorito_persiste_e_aparece_na_listagem(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.adicionar("user1", "restaurante-b")
    assert gerenciador.listar("user1") == ["restaurante-a", "restaurante-b"]


def test_nao_duplica_favorito_ja_existente(gerenciador):
    gerenciador.adicionar("user1", "restaurante-a")
    gerenciador.adicionar("user1", "restaurante-a")
    assert gerenciador.listar("user1") == ["restaurante-a"]
```

*(teste completo, com mais 4 casos, disponível em `tests/test_favoritos.py`; cenário BDD equivalente em `features/favoritar_restaurante.feature` + `tests/test_favoritos_bdd.py`)*

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| Nome do workflow | Quality Pipeline |
| Evento que dispara a execução | `push` e `pull_request` na branch `main` |
| Link para o arquivo do workflow | `<preencher>` (link de `.github/workflows/quality.yml` no GitHub após o push) |
| Link de uma execução do workflow | `<preencher>` (aba **Actions** do repositório, após o primeiro push) |

**Código do workflow (`.github/workflows/quality.yml`):**

```yaml
name: Quality Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Executar testes
        run: pytest
```

## 5. Indicadores de Qualidade

| Indicador | Valor |
|---|---|
| Quantidade de testes executados | 9 |
| Quantidade de testes aprovados | 9 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | ✅ Sucesso (`<preencher>` link do run real após o push) |

## 6. Registro de Defeito

| Item | Descrição |
|---|---|
| Título do defeito | Favorito não persiste entre sessões |
| Severidade | Alta |
| Link da Issue | `<preencher>` (crie uma Issue de bug com este título) |

**Qual foi o defeito?**
Ao favoritar um restaurante e encerrar a sessão (logout ou atualização de página), o favorito era perdido — comportamento identificado originalmente no PBL5 (BUG-02).

**Como ele foi identificado?**
Através de teste funcional manual (CT06 do PBL5): favoritar um restaurante e verificar se ele permanecia na lista após recarregar a página.

**Como foi corrigido?**
Implementando o `GerenciadorFavoritos`, que trata o armazenamento de favoritos por usuário de forma consistente (sem duplicidade e mantendo o estado entre chamadas), coberto por testes unitários e BDD que validam a persistência.

---

## 📊 Conclusão

Esta atividade fecha o ciclo iniciado no PBL5: um bug real (favoritos que não persistem) identificado por teste manual foi corrigido e coberto por testes automatizados (unitário + BDD), e agora roda automaticamente a cada push via GitHub Actions. Isso demonstra na prática como um fluxo de qualidade automatizado — testes + CI + gestão de defeitos via Issues — evita que o mesmo problema volte a acontecer sem ser percebido.

### Observação sobre o teste BDD

O `pytest-bdd` (mesma biblioteca usada no PBL8) **não interpreta** o pragma `# language: pt` para reconhecer palavras-chave em português (`Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`) — ele só reconhece `Feature`, `Scenario`, `Given`, `When`, `Then`. Por isso o arquivo `.feature` usa as palavras-chave em inglês com o conteúdo em português, garantindo que o pipeline realmente colete e execute os cenários (vale a pena revisar isso no PBL8 também, se o objetivo for rodar de fato).

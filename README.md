# LocalEats — Qualidade de Software (Senac-RS)

Entregáveis dos PBLs de Qualidade de Software aplicados ao sistema **LocalEats** (<https://local-eats-unisenac.vercel.app/>).

**Grupo:** Natã Kuhn, Eduarda Prasdio, Gabriel Schimitd, Yan

---

## Entrega 1 — PBL 1 a 5 (Fundamentos e Planejamento)

A primeira entrega foca em planejar e entender qualidade de software antes de escrever testes.

| PBL | Tema | Link |
|---|---|---|
| PBL1 | Atributos de Qualidade da ISO 25000 | [Ver](PBL1/README.md) |
| PBL2 | Papéis, Responsabilidades e Práticas de QA | [Ver](PBL2/README.md) |
| PBL3 | Estratégia Inicial de Testes | [Ver](PBL3/README.md) |
| PBL4 | Testes Funcionais vs Estruturais | [Ver](PBL4/README.md) |
| PBL5 | Planejamento e Projeto de Testes | [Ver](PBL5/README.md) |

---

## Entrega 2 — PBL 6 a 8 (Automação e BDD)

Agora vem a parte prática: automação de testes reais.

| PBL | Tema | Stack | Status |
|---|---|---|---|
| PBL6 | Testes Unitários Automatizados e TDD | TypeScript · Vitest | ✅ 22 testes passando, 100% cobertura |
| PBL7 | Testes Funcionais Automatizados (E2E) | Python · Playwright · Pytest | 🔧 Page Object Model |
| PBL8 | BDD e Automação Orientada a Comportamento | Python · Gherkin · pytest-bdd | 🔧 Behavior-Driven Development |

Cada pasta contém o código dos testes + um documento com explicações de como rodar.

---

## Como rodar

### PBL6 (Node.js / TypeScript)
```bash
cd PBL6
npm install
npm test
```

### PBL7 e PBL8 (Python)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate

cd PBL7
pip install -r requirements.txt
playwright install chromium
pytest -v

# ou para PBL8:
cd ../PBL8
pip install -r requirements.txt
pytest -v
```
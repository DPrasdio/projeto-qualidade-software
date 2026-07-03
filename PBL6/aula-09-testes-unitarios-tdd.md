# PBL 6 — Testes Unitários Automatizados e TDD

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>
**Integrante(s):** _(informe seu nome aqui)_

---

## 🛠️ Stack e Ferramentas

O LocalEats está publicado na Vercel, indicando um projeto JavaScript/TypeScript. Para manter coerência com a stack do projeto, as regras de negócio e os testes foram escritos em:

- **Linguagem:** TypeScript (lógica pura, sem dependência de frontend)
- **Framework de testes:** [Vitest](https://vitest.dev/) — padrão de mercado no ecossistema Vite/Next, API compatível com Jest
- **Cobertura:** `@vitest/coverage-v8`

> Conforme orientado no enunciado, as regras de negócio foram **implementadas como módulos de lógica pura**, simulando o backend do LocalEats. O foco está nas **regras de negócio**, não na interface gráfica.

### Estrutura do projeto

```
PBL6/
├── package.json
├── tsconfig.json
├── vitest.config.ts
├── src/
│   ├── pedido.ts          # total do pedido + valor mínimo
│   ├── desconto.ts        # desconto percentual
│   ├── entrega.ts         # taxa de entrega por distância
│   └── tempoEntrega.ts    # tempo estimado de entrega
└── tests/
    ├── pedido.test.ts
    ├── desconto.test.ts
    ├── entrega.test.ts
    └── tempoEntrega.test.ts
```

### Como executar

```bash
npm install
npm test            # executa todos os testes
npm run coverage    # executa com relatório de cobertura
```

---

## 📋 Funcionalidades e Testes

### 🔹 Funcionalidade 1 — Cálculo do total do pedido com valor mínimo
**Arquivo:** [`src/pedido.ts`](src/pedido.ts) | [`tests/pedido.test.ts`](tests/pedido.test.ts)

**O que faz:** Soma os valores dos itens (preço × quantidade) e verifica se o pedido atinge o valor mínimo exigido pelo restaurante.

**Problema que resolve:** Evita pedidos inválidos que não atendem às regras do restaurante. É a regra central do fluxo de compra.

**Regras de negócio:**
- Total = soma de `preço × quantidade` de cada item
- Se `total < valor mínimo` → erro
- Pedido sem itens → erro
- Preço ou quantidade negativos → erro

| # | Nome do teste | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| 1 | deve calcular o total corretamente quando o valor mínimo é atingido | ✅ Sucesso | `[{preco:10},{preco:20}]`, min `15` | `30` |
| 2 | deve multiplicar preço pela quantidade de cada item | ✅ Sucesso | `[{preco:10,qtd:2},{preco:5,qtd:3}]`, min `10` | `35` |
| 3 | deve aceitar pedido quando total é exatamente igual ao mínimo | 🔵 Borda | `[{preco:25}]`, min `25` | `25` |
| 4 | deve lançar erro quando total fica abaixo do valor mínimo | ❌ Erro | `[{preco:5}]`, min `20` | lança `"Valor mínimo do pedido não atingido"` |
| 5 | deve lançar erro quando pedido não possui itens | ❌ Erro | `[]`, min `0` | lança `"deve conter pelo menos um item"` |
| 6 | deve lançar erro quando item possui preço negativo | ❌ Erro | `[{preco:-10}]`, min `0` | lança `"não podem ter preço ou quantidade negativos"` |

---

### 🔹 Funcionalidade 2 — Aplicação de desconto percentual
**Arquivo:** [`src/desconto.ts`](src/desconto.ts) | [`tests/desconto.test.ts`](tests/desconto.test.ts)

**O que faz:** Aplica um desconto percentual sobre o valor total do pedido, viabilizando promoções e campanhas.

**Regras de negócio:**
- Desconto deve estar entre 0% e 100%
- Valor final não pode ser negativo
- Valor base não pode ser negativo
- Resultado arredondado para 2 casas decimais

| # | Nome do teste | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| 1 | deve aplicar corretamente um desconto de 10% | ✅ Sucesso | `100`, `10` | `90` |
| 2 | deve arredondar o valor final para 2 casas decimais | ✅ Sucesso | `99.9`, `50` | `49.95` |
| 3 | deve manter o valor original quando o desconto é 0% | 🔵 Borda | `80`, `0` | `80` |
| 4 | deve zerar o valor quando o desconto é de 100% | 🔵 Borda | `50`, `100` | `0` |
| 5 | deve lançar erro quando o desconto é maior que 100% | ❌ Erro | `100`, `120` | lança `"O desconto deve estar entre 0% e 100%"` |
| 6 | deve lançar erro quando o desconto é negativo | ❌ Erro | `100`, `-5` | lança `"O desconto deve estar entre 0% e 100%"` |
| 7 | deve lançar erro quando o valor base é negativo | ❌ Erro | `-10`, `10` | lança `"O valor não pode ser negativo"` |

---

### 🔹 Funcionalidade 3 — Cálculo da taxa de entrega
**Arquivo:** [`src/entrega.ts`](src/entrega.ts) | [`tests/entrega.test.ts`](tests/entrega.test.ts)

**O que faz:** Calcula o valor da entrega com base na distância.

**Regras de negócio:**
- Distância até 3 km → taxa fixa (R$ 5,00)
- Acima de 3 km → taxa fixa + R$ 2,00/km extra (proporcional)
- Distância negativa ou inválida → erro

| # | Nome do teste | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| 1 | deve cobrar taxa fixa para distâncias de até 3 km | ✅ Sucesso | `2` km | `5.0` |
| 2 | deve cobrar valor proporcional para distâncias acima de 3 km | ✅ Sucesso | `5` km | `9.0` (5 + 2×2) |
| 3 | deve cobrar taxa fixa no limite exato de 3 km | 🔵 Borda | `3` km | `5.0` |
| 4 | deve cobrar taxa fixa quando a distância é zero | 🔵 Borda | `0` km | `5.0` |
| 5 | deve lançar erro quando a distância é negativa | ❌ Erro | `-1` km | lança `"Distância inválida"` |

---

### 🔹 Funcionalidade 4 — Cálculo do tempo estimado de entrega
**Arquivo:** [`src/tempoEntrega.ts`](src/tempoEntrega.ts) | [`tests/tempoEntrega.test.ts`](tests/tempoEntrega.test.ts)

**O que faz:** Calcula o tempo estimado de entrega com base na distância.

**Regras de negócio:**
- `tempo = 15 min (base) + (distância × 4 min/km)`
- Distância inválida (negativa) → erro

| # | Nome do teste | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| 1 | deve estimar o tempo somando o preparo e o deslocamento | ✅ Sucesso | `5` km | `35` min (15 + 5×4) |
| 2 | deve calcular o tempo para distâncias fracionadas | ✅ Sucesso | `2.5` km | `25` min |
| 3 | deve retornar apenas o tempo base quando a distância é zero | 🔵 Borda | `0` km | `15` min |
| 4 | deve lançar erro quando a distância é negativa | ❌ Erro | `-2` km | lança `"Distância inválida"` |

---

## 🔄 Aplicação do TDD (Red → Green → Refactor)

O ciclo completo de TDD foi aplicado sobre a funcionalidade **Cálculo da taxa de entrega** (`calcularTaxaEntrega`).

### 🔴 RED — escrever o teste antes da implementação

Começamos pelo comportamento mais simples: distâncias curtas pagam taxa fixa.

```ts
// tests/entrega.test.ts — escrito ANTES do código de produção
import { calcularTaxaEntrega } from '../src/entrega';

it('deve cobrar a taxa fixa para distâncias de até 3 km', () => {
  expect(calcularTaxaEntrega(2)).toBe(5.0);
});
```

Resultado: **FALHA** (a função ainda não existia) — confirmando que o teste realmente exercita algo inexistente.

### 🟢 GREEN — implementar o mínimo necessário para passar

```ts
// Mínimo para o primeiro teste passar
export function calcularTaxaEntrega(distanciaKm: number): number {
  return 5.0;
}
```

Em seguida, adicionamos o próximo teste (distância > 3 km) → RED → implementação mínima → GREEN.

```ts
export function calcularTaxaEntrega(distanciaKm: number): number {
  if (distanciaKm <= 3) return 5.0;
  return 5.0 + (distanciaKm - 3) * 2.0;
}
```

### 🔵 REFACTOR — melhorar sem quebrar

Com os testes passando, refatoramos:
- Números mágicos → constantes exportadas (`TAXA_FIXA`, `DISTANCIA_BASE_KM`, `VALOR_POR_KM_EXTRA`)
- Validação mais robusta: `Number.isNaN` além de `< 0`
- Arredondamento monetário para evitar ponto flutuante

```ts
export const TAXA_FIXA = 5.0;
export const DISTANCIA_BASE_KM = 3;
export const VALOR_POR_KM_EXTRA = 2.0;

export function calcularTaxaEntrega(distanciaKm: number): number {
  if (Number.isNaN(distanciaKm) || distanciaKm < 0) {
    throw new Error('Distância inválida');
  }
  if (distanciaKm <= DISTANCIA_BASE_KM) return TAXA_FIXA;
  const kmExtras = distanciaKm - DISTANCIA_BASE_KM;
  return Math.round((TAXA_FIXA + kmExtras * VALOR_POR_KM_EXTRA) * 100) / 100;
}
```

Após cada alteração, `npm test` continuou **verde** — é isso que o Refactor garante.

---

## 🔧 Refatorações Realizadas

| Melhoria | Antes | Depois | Por quê |
|---|---|---|---|
| Eliminação de números mágicos | `if (d <= 3)` / `* 2.0` | Constantes nomeadas | Legibilidade e ponto único de mudança |
| Nomes descritivos | `t`, `d` | `total`, `distanciaKm`, `kmExtras` | Código autoexplicativo |
| Tratamento de borda numérica | apenas `< 0` | `Number.isNaN(...) \|\| < 0` | Evita resultados silenciosamente errados com `NaN` |
| Arredondamento monetário | retorno bruto | `Math.round(x * 100) / 100` | Preços não podem ter resíduos de ponto flutuante |
| Constantes exportadas | valores embutidos | testes importam as constantes | Se a regra mudar, o teste acompanha automaticamente |

---

## ▶️ Execução dos Testes (evidências)

```bash
npm test
```

### Resultado

```
 RUN  v1.6.1 /projeto/PBL6

 ✓ tests/pedido.test.ts  (6 tests) 4ms
 ✓ tests/desconto.test.ts  (7 tests) 4ms
 ✓ tests/entrega.test.ts  (5 tests) 4ms
 ✓ tests/tempoEntrega.test.ts  (4 tests) 4ms

 Test Files  4 passed (4)
      Tests  22 passed (22)
   Start at  22:39:58
   Duration  1.39s
```

| Métrica | Valor |
|---|---|
| **Total de testes** | **22** |
| ✅ **Passaram** | **22** |
| ❌ **Falharam** | **0** |
| Arquivos de teste | 4 (todos passaram) |

---

## 🤔 Reflexão no Contexto do LocalEats

**Foi difícil escrever testes antes do código?**
No começo exige mudança de mentalidade — mas escrever o teste antes força a definir claramente a regra de negócio antes de programar, evitando ambiguidade e retrabalho.

**O TDD ajudou no desenvolvimento?**
Sim. O ciclo Red → Green → Refactor manteve cada passo pequeno e verificável. A fase Refactor foi a mais valiosa: foi possível melhorar o código com a certeza de que nada quebrou.

**Os testes aumentaram a confiança no código?**
Muito. Com 22 testes, qualquer alteração futura nas regras (ex.: mudar a taxa fixa) é validada imediatamente. Isso ataca diretamente os problemas de regressão citados no contexto do LocalEats.

**O que melhorariam:**
- Adicionar testes de integração ligando as regras (total → desconto → taxa → tempo)
- Usar `it.each` para cobrir mais faixas de forma compacta
- Integrar a suíte a um pipeline de CI (GitHub Actions) para rodar a cada push

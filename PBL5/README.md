# PBL 5 — Planejamento e Projeto de Testes

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 1. Plano de Testes

### Objetivo
Validar o funcionamento das principais funcionalidades do sistema Local Eats, garantindo que atendam aos requisitos e não apresentem falhas críticas para o usuário.

### Escopo

**Será testado:**
- Busca de restaurantes (filtros por culinária, localização e preço)
- Realização de pedidos (seleção de itens, confirmação)
- Sistema de avaliações (envio e persistência)
- Favoritar restaurantes
- Login e cadastro

**Não será testado:**
- Performance em larga escala (testes de carga)
- Segurança avançada (pentest)
- Integrações externas complexas (ex.: gateway de pagamento)

### Estratégia
- Testes funcionais manuais (caixa-preta)
- Testes exploratórios nas funcionalidades principais
- Cenários baseados em fluxos reais de uso

### Abordagem
Testes baseados em cenários reais de uso, cobrindo o **happy path** (fluxo principal com sucesso) e **cenários de erro** (entradas inválidas, falhas do sistema).

### Responsáveis
| Papel | Responsabilidade |
|---|---|
| QA | Planejamento, especificação e execução dos testes |
| Desenvolvedor | Correção dos bugs identificados |
| Equipe | Validação geral e aprovação |

### Critérios de entrada e saída
- **Entrada:** funcionalidade implementada e disponível em ambiente de teste
- **Saída:** todos os casos críticos executados; bugs de severidade alta corrigidos e retestados

---

## 2. Casos de Teste

### CT01 — Busca com sucesso
| Campo | Descrição |
|---|---|
| ID | CT01 |
| Funcionalidade | Busca de restaurantes |
| Pré-condição | Usuário autenticado, na página inicial |
| Passos | 1. Digitar "pizza" no campo de busca; 2. Confirmar a busca |
| Resultado esperado | Lista de restaurantes relacionados à busca é exibida corretamente |
| Prioridade | Alta |

**Formato Gherkin:**
```gherkin
Dado que estou na página inicial autenticado
Quando busco por "pizza"
Então o sistema retorna restaurantes relacionados à culinária italiana/pizza
```

---

### CT02 — Busca sem resultados
| Campo | Descrição |
|---|---|
| ID | CT02 |
| Funcionalidade | Busca de restaurantes |
| Pré-condição | Usuário autenticado, na página inicial |
| Passos | 1. Digitar "xyzabc123" no campo de busca; 2. Confirmar a busca |
| Resultado esperado | Sistema exibe mensagem informando que não há resultados |
| Prioridade | Média |

**Formato Gherkin:**
```gherkin
Dado que estou na página inicial autenticado
Quando busco por "xyzabc123"
Então o sistema exibe a mensagem "Nenhum resultado encontrado"
```

---

### CT03 — Login válido
| Campo | Descrição |
|---|---|
| ID | CT03 |
| Funcionalidade | Login |
| Pré-condição | Usuário cadastrado no sistema |
| Passos | 1. Acessar página de login; 2. Informar e-mail e senha válidos; 3. Clicar em "Entrar" |
| Resultado esperado | Usuário é redirecionado para a página inicial autenticado |
| Prioridade | Alta |

**Formato Gherkin:**
```gherkin
Dado que estou na página de login
Quando informo e-mail "usuario@teste.com" e senha "Senha123"
E clico em Entrar
Então sou redirecionado para a página inicial autenticado
```

---

### CT04 — Login inválido
| Campo | Descrição |
|---|---|
| ID | CT04 |
| Funcionalidade | Login |
| Pré-condição | Usuário na página de login |
| Passos | 1. Informar e-mail correto e senha incorreta; 2. Clicar em "Entrar" |
| Resultado esperado | Sistema exibe mensagem de credenciais inválidas; usuário permanece na página |
| Prioridade | Alta |

**Formato Gherkin:**
```gherkin
Dado que estou na página de login
Quando informo e-mail "usuario@teste.com" e senha incorreta "errado"
E clico em Entrar
Então o sistema exibe mensagem de erro de autenticação
E permaneço na página de login
```

---

### CT05 — Avaliação salva corretamente
| Campo | Descrição |
|---|---|
| ID | CT05 |
| Funcionalidade | Sistema de avaliações |
| Pré-condição | Usuário autenticado, visualizando página de um restaurante |
| Passos | 1. Clicar em "Avaliar"; 2. Selecionar nota; 3. Escrever comentário; 4. Enviar |
| Resultado esperado | Avaliação é salva e exibida na página do restaurante após atualização |
| Prioridade | Alta |

**Formato Gherkin:**
```gherkin
Dado que estou autenticado e na página de um restaurante
Quando envio uma avaliação com nota 5 e comentário "Ótimo!"
E atualizo a página
Então a avaliação é exibida corretamente
```

---

### CT06 — Favoritar restaurante
| Campo | Descrição |
|---|---|
| ID | CT06 |
| Funcionalidade | Favoritos |
| Pré-condição | Usuário autenticado, visualizando a listagem de restaurantes |
| Passos | 1. Clicar no ícone de favorito de um restaurante |
| Resultado esperado | Restaurante é adicionado aos favoritos do usuário; ícone muda de estado |
| Prioridade | Média |

**Formato Gherkin:**
```gherkin
Dado que estou autenticado na página inicial
Quando clico no ícone de favorito de um restaurante
Então o restaurante aparece na minha lista de favoritos
E o ícone de favorito indica o estado salvo
```

---

## 3. Execução dos Testes

| ID | Resultado | Observação |
|---|---|---|
| CT01 | ✅ Passou | Busca retornou restaurantes corretamente |
| CT02 | ✅ Passou | Mensagem de ausência de resultados exibida |
| CT03 | ✅ Passou | Login com credenciais válidas funcionou corretamente |
| CT04 | ✅ Passou | Mensagem de erro exibida para credenciais inválidas |
| CT05 | ❌ Falhou | Avaliação desaparece após atualizar a página |
| CT06 | ❌ Falhou | Favorito não persiste após encerrar sessão |

---

## 4. Análise dos Resultados

- **Total de testes:** 6
- **Passaram:** 4 (66%)
- **Falharam:** 2 (34%)

### Bugs identificados

| Bug | Severidade | Funcionalidade |
|---|---|---|
| BUG-01: Avaliação desaparece após atualização | 🔴 Alta | Avaliações |
| BUG-02: Favorito não persiste entre sessões | 🟠 Média | Favoritos |

---

## 5. Reflexão

O plano de testes ajudou a **organizar e sistematizar** a execução, tornando os resultados rastreáveis e comparáveis.

Dois problemas críticos foram identificados — um deles (perda de avaliações) já havia sido relatado pelos usuários, confirmando a validade dos casos de teste criados.

**Melhorias para próximas iterações:**
- Incluir mais cenários de erro e valores limite
- Automatizar os casos de teste mais críticos (CT01, CT03, CT04)
- Testar em diferentes dispositivos e navegadores (compatibilidade)
- Executar testes de regressão a cada nova versão

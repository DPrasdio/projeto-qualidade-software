# PBL 1 — Atributos de Qualidade da ISO 25000

**Centro Universitário Senac-RS**
**Curso:** ADS / SPI · **Unidade Curricular:** Qualidade de Software · **Prof.:** Luciano Zanuz
**Sistema:** LocalEats — <https://local-eats-unisenac.vercel.app/>

---

## 📌 Contexto

O sistema Local Eats foi desenvolvido para conectar usuários a restaurantes locais, permitindo busca, avaliações, recomendações e interação com estabelecimentos.

Após o lançamento, diversos problemas foram relatados, comprometendo a experiência do usuário e a confiabilidade da plataforma.

---

## ⚠️ Problemas Identificados e Análise de Qualidade

| Problema identificado | Atributo de qualidade afetado (ISO 25010) | Justificativa técnica |
|---|---|---|
| Lentidão em horários de pico | Eficiência de Desempenho (Performance Efficiency) | O tempo de resposta elevado indica falhas na capacidade do sistema de lidar com alta carga de usuários simultâneos. |
| Telas confusas e pouco intuitivas | Usabilidade (Usability) | Interfaces pouco claras dificultam a interação do usuário e aumentam a chance de erros. |
| Buscas retornam resultados incorretos | Adequação Funcional (Functional Suitability) | O sistema não entrega resultados corretos conforme esperado, comprometendo sua funcionalidade principal. |
| Falhas em determinados smartphones | Compatibilidade (Compatibility) | O sistema não funciona corretamente em diferentes dispositivos, indicando problemas de portabilidade/compatibilidade. |
| Dificuldade para concluir ações simples | Usabilidade (Usability) | A complexidade nas interações prejudica a experiência do usuário e reduz a eficiência. |
| Avaliações desaparecem após atualização | Confiabilidade (Reliability) | Perda de dados indica falhas na persistência e confiabilidade do sistema. |
| Inconsistência entre versão web e mobile | Compatibilidade / Consistência (Compatibility) | Diferenças entre plataformas geram confusão e prejudicam a experiência do usuário. |

---

## 📊 Conclusão

O sistema apresenta falhas em múltiplos atributos de qualidade da **ISO/IEC 25010**, especialmente:

- **Eficiência de Desempenho** — lentidão sob carga
- **Usabilidade** — interface confusa e ações difíceis
- **Confiabilidade** — perda de dados de avaliação
- **Compatibilidade** — falhas em dispositivos específicos
- **Adequação Funcional** — resultados de busca incorretos

Esses problemas impactam diretamente a experiência do usuário e a reputação da plataforma, sendo necessária priorização de correções antes da continuidade da operação em larga escala.

### Priorização sugerida

1. **Alta prioridade:** Confiabilidade (perda de dados) e Adequação Funcional (busca incorreta)
2. **Média prioridade:** Eficiência de Desempenho (lentidão em pico)
3. **Menor prioridade imediata:** Usabilidade e Compatibilidade (impactam experiência, mas não causam perda de dados)

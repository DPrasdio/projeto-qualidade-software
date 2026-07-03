/**
 * Regra de negócio: Aplicação de desconto percentual sobre o valor do pedido.
 * Viabiliza promoções e campanhas da plataforma LocalEats.
 */

/**
 * Aplica um desconto percentual sobre o valor informado.
 * @param valor Valor base do pedido (deve ser >= 0)
 * @param percentual Percentual de desconto (0 a 100)
 * @returns Valor final após desconto, arredondado para 2 casas decimais
 * @throws Error se os parâmetros forem inválidos
 */
export function aplicarDesconto(valor: number, percentual: number): number {
  if (valor < 0) {
    throw new Error('O valor não pode ser negativo');
  }
  if (percentual < 0 || percentual > 100) {
    throw new Error('O desconto deve estar entre 0% e 100%');
  }
  const valorFinal = valor - valor * (percentual / 100);
  return Math.round(valorFinal * 100) / 100;
}

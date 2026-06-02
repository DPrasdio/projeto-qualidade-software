/**
 * Regra de negócio: Cálculo do total do pedido com valor mínimo.
 * Soma os valores dos itens (preço × quantidade) e valida o mínimo exigido.
 */
export interface ItemPedido {
  nome?: string;
  preco: number;
  quantidade?: number;
}

/**
 * Calcula o total de um pedido e valida o valor mínimo.
 * @param itens Lista de itens do pedido
 * @param valorMinimo Valor mínimo exigido pelo restaurante
 * @returns Total calculado
 * @throws Error se o pedido for inválido
 */
export function calcularTotalPedido(itens: ItemPedido[], valorMinimo: number): number {
  if (!Array.isArray(itens) || itens.length === 0) {
    throw new Error('O pedido deve conter pelo menos um item');
  }

  const total = itens.reduce((acumulado, item) => {
    const quantidade = item.quantidade ?? 1;
    if (item.preco < 0 || quantidade < 0) {
      throw new Error('Itens não podem ter preço ou quantidade negativos');
    }
    return acumulado + item.preco * quantidade;
  }, 0);

  if (total < valorMinimo) {
    throw new Error('Valor mínimo do pedido não atingido');
  }

  return Math.round(total * 100) / 100;
}

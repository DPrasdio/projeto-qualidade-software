/**
 * Regra de negócio: Cálculo da taxa de entrega com base na distância.
 * Padroniza a cobrança e impacta o custo final do pedido.
 */

export const TAXA_FIXA = 5.0;
export const DISTANCIA_BASE_KM = 3;
export const VALOR_POR_KM_EXTRA = 2.0;

/**
 * Calcula a taxa de entrega com base na distância em km.
 * - Até 3 km: taxa fixa de R$ 5,00
 * - Acima de 3 km: taxa fixa + R$ 2,00/km extra
 * @param distanciaKm Distância em quilômetros
 * @returns Taxa de entrega em reais
 * @throws Error se a distância for inválida
 */
export function calcularTaxaEntrega(distanciaKm: number): number {
  if (Number.isNaN(distanciaKm) || distanciaKm < 0) {
    throw new Error('Distância inválida');
  }
  if (distanciaKm <= DISTANCIA_BASE_KM) {
    return TAXA_FIXA;
  }
  const kmExtras = distanciaKm - DISTANCIA_BASE_KM;
  const taxa = TAXA_FIXA + kmExtras * VALOR_POR_KM_EXTRA;
  return Math.round(taxa * 100) / 100;
}

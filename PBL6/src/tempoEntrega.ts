/**
 * Regra de negócio: Cálculo do tempo estimado de entrega.
 * Melhora a previsibilidade para o usuário e impacta a experiência do cliente.
 */

export const TEMPO_BASE_MIN = 15;
export const TEMPO_POR_KM_MIN = 4;

/**
 * Calcula o tempo estimado de entrega em minutos.
 * Fórmula: tempo base (15 min) + (distância × 4 min/km)
 * @param distanciaKm Distância em quilômetros
 * @returns Tempo estimado em minutos (arredondado)
 * @throws Error se a distância for inválida
 */
export function calcularTempoEntrega(distanciaKm: number): number {
  if (Number.isNaN(distanciaKm) || distanciaKm < 0) {
    throw new Error('Distância inválida');
  }
  const tempo = TEMPO_BASE_MIN + distanciaKm * TEMPO_POR_KM_MIN;
  return Math.round(tempo);
}

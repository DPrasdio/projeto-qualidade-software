import { describe, it, expect } from 'vitest';
import { calcularTempoEntrega, TEMPO_BASE_MIN } from '../src/tempoEntrega';

describe('calcularTempoEntrega', () => {
  it('deve estimar o tempo somando o preparo e o deslocamento', () => {
    expect(calcularTempoEntrega(5)).toBe(35); // 15 + 5*4
  });

  it('deve calcular o tempo para distâncias fracionadas', () => {
    expect(calcularTempoEntrega(2.5)).toBe(25); // 15 + 2.5*4
  });

  it('deve retornar apenas o tempo base quando a distância é zero', () => {
    expect(calcularTempoEntrega(0)).toBe(TEMPO_BASE_MIN);
  });

  it('deve lançar erro quando a distância é negativa', () => {
    expect(() => calcularTempoEntrega(-2)).toThrow('Distância inválida');
  });
});

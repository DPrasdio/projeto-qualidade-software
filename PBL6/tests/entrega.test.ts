import { describe, it, expect } from 'vitest';
import { calcularTaxaEntrega, TAXA_FIXA, DISTANCIA_BASE_KM } from '../src/entrega';

describe('calcularTaxaEntrega', () => {
  it('deve cobrar a taxa fixa para distâncias de até 3 km', () => {
    expect(calcularTaxaEntrega(2)).toBe(TAXA_FIXA);
  });

  it('deve cobrar valor proporcional para distâncias acima de 3 km', () => {
    expect(calcularTaxaEntrega(5)).toBe(9); // 5 + (5-3)*2
  });

  it('deve cobrar taxa fixa no limite exato de 3 km', () => {
    expect(calcularTaxaEntrega(DISTANCIA_BASE_KM)).toBe(TAXA_FIXA);
  });

  it('deve cobrar taxa fixa quando a distância é zero', () => {
    expect(calcularTaxaEntrega(0)).toBe(TAXA_FIXA);
  });

  it('deve lançar erro quando a distância é negativa', () => {
    expect(() => calcularTaxaEntrega(-1)).toThrow('Distância inválida');
  });
});

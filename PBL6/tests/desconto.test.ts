import { describe, it, expect } from 'vitest';
import { aplicarDesconto } from '../src/desconto';

describe('aplicarDesconto', () => {
  it('deve aplicar corretamente um desconto de 10%', () => {
    expect(aplicarDesconto(100, 10)).toBe(90);
  });

  it('deve arredondar o valor final para 2 casas decimais', () => {
    expect(aplicarDesconto(99.9, 50)).toBe(49.95);
  });

  it('deve manter o valor original quando o desconto é 0%', () => {
    expect(aplicarDesconto(80, 0)).toBe(80);
  });

  it('deve zerar o valor quando o desconto é de 100%', () => {
    expect(aplicarDesconto(50, 100)).toBe(0);
  });

  it('deve lançar erro quando o desconto é maior que 100%', () => {
    expect(() => aplicarDesconto(100, 120)).toThrow('O desconto deve estar entre 0% e 100%');
  });

  it('deve lançar erro quando o desconto é negativo', () => {
    expect(() => aplicarDesconto(100, -5)).toThrow('O desconto deve estar entre 0% e 100%');
  });

  it('deve lançar erro quando o valor base é negativo', () => {
    expect(() => aplicarDesconto(-10, 10)).toThrow('O valor não pode ser negativo');
  });
});

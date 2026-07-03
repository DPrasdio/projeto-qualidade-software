import { describe, it, expect } from 'vitest';
import { calcularTotalPedido } from '../src/pedido';

describe('calcularTotalPedido', () => {
  it('deve calcular o total corretamente quando o valor mínimo é atingido', () => {
    const itens = [{ preco: 10 }, { preco: 20 }];
    expect(calcularTotalPedido(itens, 15)).toBe(30);
  });

  it('deve multiplicar preço pela quantidade de cada item', () => {
    const itens = [{ preco: 10, quantidade: 2 }, { preco: 5, quantidade: 3 }];
    expect(calcularTotalPedido(itens, 10)).toBe(35);
  });

  it('deve aceitar pedido quando o total é exatamente igual ao mínimo', () => {
    const itens = [{ preco: 25 }];
    expect(calcularTotalPedido(itens, 25)).toBe(25);
  });

  it('deve lançar erro quando o total fica abaixo do valor mínimo', () => {
    const itens = [{ preco: 5 }];
    expect(() => calcularTotalPedido(itens, 20)).toThrow('Valor mínimo do pedido não atingido');
  });

  it('deve lançar erro quando o pedido não possui itens', () => {
    expect(() => calcularTotalPedido([], 0)).toThrow('deve conter pelo menos um item');
  });

  it('deve lançar erro quando um item possui preço negativo', () => {
    const itens = [{ preco: -10 }];
    expect(() => calcularTotalPedido(itens, 0)).toThrow('não podem ter preço ou quantidade negativos');
  });
});

'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de
três e que se encontram no intervalo de 1 até 500.'''
soma = cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')

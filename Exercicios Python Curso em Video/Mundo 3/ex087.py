'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[], [], []]
somapar = somater = maior = 0
for c in range(0,3):
    for l in range(0,3):
        n = int(input(f'Digite um valor para a posicao [{c} {l}]: '))
        if n %2 == 0:
            somapar += n
        matriz[c].append(n)
        if c == 2:
            somater += matriz[l][c]
print('-='*20)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somater}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

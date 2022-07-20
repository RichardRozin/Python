'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
n = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
c = 1
while c <= t:
    print(n, end= ' → ')
    n += r
    c += 1
print('FIM')
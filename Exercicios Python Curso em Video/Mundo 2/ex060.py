'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
from math import factorial
n = int(input('Digite um numero para ver seu fatorial: '))
c = n
print(f'Calculando o fatorial de {n}...')
while c > 0:
    if c > 1:
        print(f'{c} x',end=' ')
    else:
        print(f'{c} =',end=' ')
    c -= 1
print(f'{factorial(n)}')

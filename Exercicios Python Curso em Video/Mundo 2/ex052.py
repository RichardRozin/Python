'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[32m{c}',end=' ')
        cont += 1
    else:
        print(f'\033[31m{c}',end=' ')
print(f'\033[m\nO numero {n} foi divisivel {cont} vezes.')
if cont == 2:
    print(f'O numero {n} é primo.')
else:
    print(f'O numero {n} nao é primo.')

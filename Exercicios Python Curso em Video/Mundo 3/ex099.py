'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep


def maior(*num):
    print('=-=' * 20)
    print('Analizando os valores passados...')
    if num != ():
        for c in num:
            print(c, end=' ')
        print()
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
from time import sleep
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.25)
print('Acabou!')

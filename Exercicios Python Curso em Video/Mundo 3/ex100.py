'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando 5 valores da lista...')
    for c in range(0, 5):
        sleep(0.5)
        n = randint(0, 10)
        print(n, end=' ')
        lista.append(n)


def somapar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'\nSomando os valores pares de {lst}, temos {soma}. ')


lista = []
sorteio(lista)
somapar(lista)


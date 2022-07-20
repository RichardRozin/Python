'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = []
print('-='*15)
print('  SORTEIOS PARA A MEGA SENA')
print('-='*15)
n = int(input('Quantos jogos voce quer sortear? '))
print('-='*3, f'SORTEANDO {n} JOGOS', '=-'*3)
sleep(2)
for c in range(0, n):
    sleep(1)
    for l in range(0,6):
        num = randint(1, 60)
        if num in lista:
            num = randint(1, 60)
        lista.append(num)
    lista.sort()
    print(f'JOGO {c+1}: {lista}')
    lista.clear()
print('-='*4, f'BOA SORTE!!!', '=-'*4)




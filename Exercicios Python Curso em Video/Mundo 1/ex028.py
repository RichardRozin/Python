'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
print('\033[33m-='*30)
print(f'\033[36m  Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\033[33m-=\033[m'*30)
n = int(input('Em que numero eu pensei? '))
comp = randint(0,5)
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if comp == n:
    print('\033[32mPARABENS! Voce acertou o numero!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no numero {comp} e nao no {n}!\033[m')
    
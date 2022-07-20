'''Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
print('Prepare-se para a contagem regressiva!!!')
sleep(3)
for c in range(10, -1, -1):
    print(c,end=' ')
    sleep(1)
print('\nBUM! BUM! POOW!')

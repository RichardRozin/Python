'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('Olá, sou seu computador e acabei de pensar em um numero de 0 a 10.')
print('Sera que voce consegue adivinhar qual foi???')
comp = randint(0,10)
opc = ''
palp = 0
while opc != comp:
    opc = int(input('Qual o seu palpite? '))
    palp += 1
    if opc > comp:
        print('ERROU! Tente um numero menor.')
    if opc < comp:
        print('ERROU! Tente um numero maior')
print(f'PARABENS!!! Voce acertou com {palp} tentativas.')
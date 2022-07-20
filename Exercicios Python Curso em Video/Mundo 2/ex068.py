'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
print('-='*20)
print('       VAMOS JOGAR PAR OU IMPAR')
cont = soma = 0
resultado = ''
while True:
    print('-=' * 20)
    n = int(input('Diga um valor: '))
    opc = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print('-'*56)
    comp = randint(0, 10)
    soma = n + comp
    print(f'Voce jogou {n} e o computador jogou {comp} total de {soma}, ',end='')
    if soma %2 == 0:
        print('DEU PAR!')
        resultado = 'P'
    else:
        print('DEU IMPAR!')
        resultado = 'I'
    if opc == resultado:
        print('\033[32mVOCE VENCEU!!!')
        cont += 1
        print('\033[mVamos jogar novamente...')
    else:
        print('\033[31mVOCE PERDEU!\033[m')
        break
print('-='*20)
print(f'\033[33mGAMER OVER! Voce venceu {cont} vezes.')

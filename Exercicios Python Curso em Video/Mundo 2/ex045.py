'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
print('\033[31m|PEDRA|\033[32m|PAPEL|\033[33m|TESOURA|')
print('\033[mEscolha uma das opcoes abaixo: ')
print('''\033[31m[ 1 ] PEDRA
\033[32m[ 2 ] PAPEL
\033[33m[ 3 ] TESOURA''')
opc = int(input('\033[mSua escolha: '))
comp = randint(1, 3)
print('-='*12)
if opc == 1 and comp == 2:
    print('Computador jogou Papel')
    print('Jogador jogou Pedra')
    print('Computador venceu!!!')
elif opc == 1 and comp == 3:
    print('Computador jogou Tesoura')
    print('Jogador jogou Pedra')
    print('Jogador venceu!!!')
elif opc == 2 and comp == 1:
    print('Computador jogou Pedra')
    print('Jogador jogou Papel')
    print('Jogador venceu!!!')
elif opc == 2 and comp == 3:
    print('Computador jogou Tesoura')
    print('Jogador jogou Papel')
    print('Computador venceu!!!')
elif opc == 3 and comp == 1:
    print('Computador jogou Pedra')
    print('Jogador jogou Tesoura')
    print('Computador venceu!!!')
elif opc == 3 and comp == 2:
    print('Computador jogou Papel')
    print('Jogador jogou Tesoura')
    print('Jogador venceu!!!')
elif opc == comp:
    print('EMPATE!!!')
else:
    print('OPCAO INVALIDA! Tente novamente:')
print('-='*12)
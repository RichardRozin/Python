'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''


def ajuda(funcao):
    from time import sleep
    print(f'\033[7:32:40mAcessando o manual do comando {funcao}...')
    sleep(3)
    print(f'\033[7:30:42m')
    print({help(funcao)})


print('\033[32m~'*25)
print('SISTEMA DE AJUDA PyHELP'.center(25))
print('~'*25)
while True:
    a = str(input('\033[mFuncao ou Biblioteca > '))
    ajuda(a)

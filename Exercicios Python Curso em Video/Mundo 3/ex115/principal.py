'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''


import funcao
from time import sleep
arq = 'Cursoemvideo.txt'

if not funcao.arqexiste(arq):
    funcao.criararquivo(arq)
funcao.menu()
while True:
    try:
        opc = int(input('\033[33mSua opcao: \033[m'))
    except:
        print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
    else:
        if opc > 3 or opc < 1:
            print('\033[31mERRO! Digite uma opcao valida. \033[m')
            sleep(1)
            funcao.menu()
        else:
            funcao.opcao(opc, arq)
        if opc == 3:
            break


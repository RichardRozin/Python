'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAS\n[ 3 ] MAIOR\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR DO PROGRAMA''')
    opc = int(input('Qual a sua opcao: '))
    print('-='*16)
    if opc > 5 or opc < 1:
        print('Opcao invalida! Tente novamente.')
    if opc == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    if opc == 2:
        print(f'O multiplicaçao entre {n1} e {n2} é {n1 * n2}.')
    if opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero digitado foi {maior}.')
    if opc == 4:
        print('Informe os novos numeros')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opc == 5:
        print('Finalizando...')
    print('-=' * 16)
    sleep(2)
print('Fim do programa! Volte sempre.')



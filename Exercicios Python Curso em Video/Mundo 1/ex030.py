'''Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
n = int(input('Digite um numero: '))
if n % 2 == 0:
    print(f'O numero {n} é \033[36mPAR\033[m!')
else:
    print(f'O numero {n} é \033[36mIMPAR\033[m!')

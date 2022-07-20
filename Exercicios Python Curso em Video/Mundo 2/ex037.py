'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a conversao:
[ 1 ] BINARIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL''')
esc = int(input('Sua escolha: '))
if esc == 1:
    print(f'{n} convertido para BINARIO é {bin(n)[2:]}.')
elif esc == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}.')
else:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}.')

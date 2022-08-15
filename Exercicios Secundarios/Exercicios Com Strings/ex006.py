'''Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
Valida e corrige número de telefone:
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133'''
lista = []
cont = 0
num = str(input('Digite seu numero de telefone: ')).strip()
if len(num) < 9:
    for c in range(0, len(num)):
        if num[c].isnumeric():
            lista.append(num[c])
            cont += 1
    if cont == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        lista.insert(0, 3)
    print(f'Telefone corrigido sem formatação: ',end='')
    for c in lista:
        print(c, end='')
    if '-' not in lista:
        lista.insert(4, '-')
    print(f'\nTelefone corrigido com formatação: ',end='')
    for c in lista:
        print(c, end='')
else:
    print('Telefone ok.')




'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temp = []
lista = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ').title()))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp.copy())
    temp.clear()
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print(f'Ao todo voce cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {mai}Kg, peso de ',end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg, peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')




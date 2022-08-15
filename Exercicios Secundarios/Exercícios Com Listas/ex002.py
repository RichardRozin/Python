'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''
lista = []
cont = 0
for c in range(0, 10):
    lista.append(str(input('Digite uma letra: ')).strip().upper())
print('As Consoantes digitadas foram: ',end='')
for c in lista:
    if c not in 'AEIOU':
        cont += 1
        print(c, end=' ')
print(f'\nUm total de {cont} consoantes.')


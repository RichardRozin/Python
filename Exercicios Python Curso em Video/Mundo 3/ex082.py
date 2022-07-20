'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*20)
print(f'A lista completa é {lista}.')
print(f'A lista com os numeros PARES é {par}.')
print(f'A lista com os numeros IMPARES é {impar}.')




'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*20)
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}.')
if 5 in lista:
    print('O numero 5 esta na lista.')
else:
    print(f'Nenhum valor 5 encontrado na lista.')

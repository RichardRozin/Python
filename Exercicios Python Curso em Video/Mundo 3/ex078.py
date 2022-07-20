'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite o {c+1} valor: ')))
print(f'O maior valor digitado foi {max(lista)} na posicao {lista.index(max(lista))}.')
print(f'O menor valor digitado foi {min(lista)} na posicao {lista.index(min(lista))}.')


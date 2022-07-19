'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.'''
r = float(input('Quanto dinheiro voce tem na carteira? R$ '))
d = r / 3.27
print(f'Com R${r} voce consegue comprar US${d:.2f} dolares.')


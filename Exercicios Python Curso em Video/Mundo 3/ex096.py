'''Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(l, c):
    area = l * c
    print(f'A area de um terreno de {l} x {c} é de {area:.2f}m².')


print('CONTROLE DE TERRENOS')
print('-'*20)
lar = float(input('Largura (M) '))
com = float(input('Comprimeito (M) '))
area(lar, com)



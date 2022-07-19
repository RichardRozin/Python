'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print(f'Sua parede tem a dimensao de {l}X{a} e sua area é de {area:.2f}m².')
tinta = area / 2
print(f'Para pintar essa parede, sera necessario {tinta:.2f} litros de tinta.')

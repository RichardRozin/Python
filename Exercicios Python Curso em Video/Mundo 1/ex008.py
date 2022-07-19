'''Exercício Python 008: Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.'''
v = float(input('Digite uma distancia em metros: '))
cm = v * 100
mm = v * 1000
print(f'O medida de {v}m equivale a {cm:.0f}cm e {mm:.0f}mm.')

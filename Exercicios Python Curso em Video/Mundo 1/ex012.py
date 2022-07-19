'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
v = float(input('Informe o valor do produto: '))
d = v - (v * 5/100)
print(f'O produto que custava R${v}, com 5% de desconto passara a custar R${d:.2f}.')

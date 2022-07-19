'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodados? '))
precodia = d * 60
precokm = km * 0.15
total = precokm + precodia
print(f'O total a pagar é de R${total:.2f}.')


'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.'''
d = int(input('Qual é a distancia da viagem? '))
print(f'Voce esta prestes a comecar uma viagem de {d:.1f}Km.')
if d <= 200:
    valor = d * 0.50
else:
    valor = d * 0.45
print(f'E o preco da sua passagem sera de R${valor:.2f}.')
print(f'Tenha uma otima viagem!!!')

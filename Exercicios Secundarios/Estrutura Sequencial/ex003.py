'''Faça um Programa que pergunte quanto uma pessoa ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''
valor = float(input('Quantos reais voce recebe por horas trabalhadas? R$'))
hr = int(input('Quantas horas voce trabalha por mes? '))
print(f'Trabalhando {hr} horas por dia com um total de R${valor:.2f} por hora, voce ira receber R${valor * hr:.2f} por mes.')

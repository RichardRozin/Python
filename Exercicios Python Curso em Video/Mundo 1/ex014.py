'''Exercício Python 014: Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.
'''
t = float(input('Informe a temperatura: '))
k = (t * 9/5) + 32
print(f'A temperatura de {t} graus Celsius equivale a {k} graus Fahrenheit.')
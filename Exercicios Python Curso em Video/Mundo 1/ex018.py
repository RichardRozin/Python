'''Exercício Python 018: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
from math import sin, cos, tan, radians
a = int(input('Digite um angulo que voce deseja: '))
print(f'O angulo de {a} tem o SENO de {sin(radians(a)):.2f}.')
print(f'O angulo de {a} tem o COSSENO de {cos(radians(a)):.2f}.')
print(f'O angulo de {a} tem a TANGENTE de {tan(radians(a)):.2f}.')
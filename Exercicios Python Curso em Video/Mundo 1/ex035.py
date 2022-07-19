'''Exercício Python 035: Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-='*20)
print('        ANALISADOR DE TRIANGULOS')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('O segmento acima pode formar um triangulo! ')
else:
    print('O segmento acima nao pode formar um triangulo! ')

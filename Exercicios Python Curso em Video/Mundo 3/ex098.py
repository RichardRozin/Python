'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    print('=-=' * 15)
    if p < 0:
        p *= -1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if f < i:
        p *= -1
        f -= 1
    else:
        f += 1
    for c in range(i, f, p):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')
    print('=-=' * 15)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)









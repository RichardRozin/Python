'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
soma = cont = 0
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Voce digitou {cont} numeros PARES e a soma entre eles é {soma}.')

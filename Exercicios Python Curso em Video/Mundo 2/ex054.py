'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
maior = menor = 0
for c in range(0,7):
    ano = int(input(f'Em que ano a {c+1}o pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E tivemos {menor} pessoas menores de idade.')

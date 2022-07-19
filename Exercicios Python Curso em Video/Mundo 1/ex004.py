'''Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''
algo = str(input('Digite algo: '))
print(f'O tipo primitivo desse valor é {type(algo)};')
print(f'So tem espacos? {algo.isspace()};')
print(f'É um numero? {algo.isnumeric()};')
print(f'É alfabetico? {algo.isalpha()};')
print(f'É alfanumerico? {algo.isalnum()};')
print(f'Esta em maiusculo? {algo.isupper()};')
print(f'Esta em minusculo? {algo.islower()};')
print(f'Esta capitalizada? {algo.istitle()};')
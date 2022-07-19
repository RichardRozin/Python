'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Qual o seu nome completo: ')).strip().title()
separa = nome.split()
print(f'Seu nome tem silva? {"Silva" in separa}.')

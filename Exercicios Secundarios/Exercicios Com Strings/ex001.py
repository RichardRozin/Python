'''Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome
do usuário de trás para frente utilizando somente letras maiúsculas.'''
nome = str(input('Digite seu nome: ')).strip().upper()
for c in range(len(nome)-1, -1, -1):
    print(nome[c], end='')
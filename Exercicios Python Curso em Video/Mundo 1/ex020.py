'''Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a ordem sorteada.'''
from random import shuffle
a1 = str(input('Primeiro aluno: ')).capitalize()
a2 = str(input('Segundo aluno: ')).capitalize()
a3 = str(input('Terceiro aluno: ')).capitalize()
a4 = str(input('Quarto aluno: ')).capitalize()
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentacao sera: {lista}.')

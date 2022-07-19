'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos
e escrevendo na tela o nome do escolhido.'''
from random import choice
a1 = str(input('Primeiro aluno: ')).capitalize()
a2 = str(input('Segundo aluno: ')).capitalize()
a3 = str(input('Terceiro aluno: ')).capitalize()
a4 = str(input('Quarto aluno: ')).capitalize()
lista = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {choice(lista)}.')



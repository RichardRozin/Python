'''Faça um Programa que peça as quatro notas de 4 alunos, calcule e armazene num vetor a média de cada aluno, imprima o
número de alunos com média maior ou igual a 7.0.'''
lista = []
media = cont = 0
for c in range(0, 4):
    n1 = float(input(f'Digite a primeira nota do {c+1}o aluno: '))
    n2 = float(input(f'Digite a segunda nota do {c+1}o aluno: '))
    n3 = float(input(f'Digite a terceira nota do {c+1}o aluno: '))
    n4 = float(input(f'Digite a quarta nota do {c+1}o aluno: '))
    media = (n1 + n2 + n3 + n4) / 4
    lista.append(media)
for c in lista:
    if c >= 7:
        cont += 1
print(f'Foi um total de {cont} alunos com media maior que 7.0.')


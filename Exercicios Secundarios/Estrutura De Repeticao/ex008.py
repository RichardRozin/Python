'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''
soma = 0
turmas = int(input('Informe a quantidade de turmas: '))
for c in range(0, turmas):
    alunos = int(input(f'Quantos alunos na {c+1}° turma? '))
    while alunos > 40:
        print('As turmas nao podem ter mais de 40 alunos!')
        alunos = int(input('Informe a quantidade de alunos novamente: '))
    soma += alunos
media = soma / turmas
print(f'A media de alunos por turma é de {media:.0f} alunos.')

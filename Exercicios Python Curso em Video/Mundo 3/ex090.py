'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('=-='*10)
for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}.')













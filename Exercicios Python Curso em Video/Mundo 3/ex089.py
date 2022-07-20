'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
temp = []
lista = []
media = 0
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    media = (temp[1] + temp[2]) /2
    lista.append(temp.copy())
    temp.clear()
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*40)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*20)
for n, p in enumerate(lista):
    print(f'{n:<4}{p[0]:<10}{media:>8}')
aluno = int(input('Deseja ver as notas de qual aluno? [999 PARA FINALIZAR]: '))
if aluno != 999:
    print(f'Notas de {lista[aluno][0]} sao:',end=' ')
    for c in range(0,2):
        print({lista[aluno][c+1]},end=' ')
print('\nFinalizando...')

'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
y = 1
n = termo + (10)*razao
while y != 0:
    while termo != n:
        print(termo, end = ' → ')
        termo += razao
    print('Pausa')
    y = int(input('Mais quantos termos você deseja ver?: '))
    n = termo + y*razao
print('Fim!')
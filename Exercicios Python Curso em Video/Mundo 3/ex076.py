'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
tupla = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-'*30)
print(f'{"LISTAGEM DE PRECOS:":^30}')
print('-'*30)
for c in tupla:
    if type(c) == str:
        t = 20 - (len(c))
        print(f'{c}', end='')
        print('.' * t, end='')
    else:
        print(f'R${c:.2f}')
print('-'*30)
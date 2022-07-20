''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando
se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, cal=False):
    '''
    Funcao responsavel por calcular o fatorial de um numero.
    :param num: o numero a ser calculado
    :param cal: se vai ou nao mostrar o calculo
    :return: o resultado do fatorial
    '''
    f = 1
    for c in range(num, 0, -1):
        if cal:
            print(f'{c}', end='')
            if c > 1:
                print(' x ',end='')
            else:
                print('.', end='')
        f *= c

    return f


n = int(input('Digite um numero para ver seu fatorial: '))
resp = str(input('Deseja ver o calculo? ')).strip().upper()[0]
if resp == 'S':
    print(f'\nO fatorial de {n} é {fatorial(n, cal=True)}.')
else:
    print(f'O fatorial de {n} é {fatorial(n)}.')
ajuda = str(input('Deseja ver um resumo da funcao? ')).strip().upper()[0]
if ajuda == 'S':
    print('-='*50)
    help(fatorial)
    print('Fim do programa.')
else:
    print('Fim do programa.')


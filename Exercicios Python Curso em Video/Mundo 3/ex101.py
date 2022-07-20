'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano):
    '''
    funcao responsavel por indicar se uma pessoa vota ou nao.
    :param ano: ano de nascimento da pessoa
    :return: a situacao da pessoa.
    '''
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ',end='')
    if 18 <= idade < 65:
        return 'VOTO OBRIGATORIO!'
    elif idade < 16:
        return 'NAO VOTA!'
    else:
        return 'VOTO OPCIONAL'


n = int(input('Informe seu ano de nascimento: '))
print(f'{voto(n)}')





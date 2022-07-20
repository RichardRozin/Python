'''Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preco analisado: \t{moeda(preco)}.')
    print(f'Dobro do preco: \t{dobro(preco, True)}.')
    print(f'Metade do preco: \t{metade(preco, True)}.')
    print(f'Aumento de {taxaa}%: \t{aumentar(preco, taxaa, True)}.')
    print(f'Reducao de {taxar}%: \t{diminuir(preco, taxar, True)}.')
    print('-' * 30)
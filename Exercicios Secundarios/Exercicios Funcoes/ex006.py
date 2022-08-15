'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia
de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
valor de custo para incluir o imposto sobre vendas.'''


def somaImposto(taxaImposto=0, custo=0):
    imp = custo * taxaImposto/100
    return custo + imp


preco = float(input('Digite o preco do produto: R$'))
msg = str(input('Informe o percentual de imposto sobre o preco: ')).replace('%', '')
imposto = int(msg)
print(f'O valor de R${preco:.2f} com {imposto}% de imposto ficou em R${somaImposto(imposto, preco):.2f}')
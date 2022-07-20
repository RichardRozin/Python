'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('-'*40)
print('            MERCADO ROZIN')
total = cont = precobarato = 0
barato = ''
while True:
    print('-' * 40)
    n = str(input('Nome do produto: ')).strip().title()
    p = float(input('Preço: R$'))
    if cont == 0:
        barato = n
        precobarato = p
    else:
        if p < precobarato:
            barato = n
            precobarato = p
    if p >= 1000:
        cont += 1
    total += p
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc != 'S':
        break
print('-'*40)
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {cont} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} que custa R${precobarato:.2f}.')

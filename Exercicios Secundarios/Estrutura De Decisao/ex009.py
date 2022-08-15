'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites
para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''
print('=-='*10)
print('      Mercados Tabajara')
print('=-='*10)
quant = float(input('Informe o peso total em Kg: '))
carne = str(input('Informe o nome da carne: ')).strip().title()
preco = 0
if quant <= 5:
    if carne == 'File Duplo':
        preco = quant * 4.90
    elif carne == 'Alcatra':
        preco = quant * 5.90
    elif carne == 'Picanha':
        preco = quant * 6.90
    else:
        print(f'{carne} nao esta em promocao! Informe o nome da carne corretamente.')
else:
    if carne == 'File Duplo':
        preco = quant * 5.80
    elif carne == 'Alcatra':
        preco = quant * 6.80
    elif carne == 'Picanha':
        preco = quant * 7.80
    else:
        print(f'{carne} nao esta em promocao! Informe o nome da carne corretamente.')
cartao = str(input('Possui o cartao tabajara? ')).strip().upper()[0]
if cartao == 'S':
    preco -= (preco * 5/100)
print(f'O valor total da compra foi de R${preco:.2f}.')
print('Volte sempre!!!')

'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.'''
pesomorango = float(input('Informe o peso total dos morangos em Kg: '))
pesomaca = float(input('Informe o peso total das macas em Kg: '))
somapeso = pesomaca + pesomorango
preco = 0
if pesomorango <= 5:
    preco += pesomorango * 2.50
else:
    preco += pesomorango * 2.20
if pesomaca <= 5:
    preco += pesomaca * 1.80
else:
    preco += pesomaca * 1.50
if somapeso > 8 or preco > 25:
    preco -= (preco * 10/100)
print(f'O valor total da compra foi de R${preco:.2f}.')

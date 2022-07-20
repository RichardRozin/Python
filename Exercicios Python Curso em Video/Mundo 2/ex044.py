'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
print('-='*5,'LOjAS ROZIN', '=-'*5)
val = float(input('Informe o preco da compra: R$'))
print('Escolha uma forma de pagamento:')
print('''[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opc = int(input('Qual a sua opcao? '))
if opc == 1:
    desconto = val - (val * 10/100)
    print(f'Sua compra de R${val} com 10% de desconto vai ficar R${desconto:.2f}.')
elif opc == 2:
    desconto = val - (val * 5/100)
    print(f'Sua compra de R${val:.2f} com 5% de desconto vai ficar R${desconto:.2f}.')
elif opc == 3:
    print(f'Sua compra ficou parcelada em 2x de R${val / 2:.2f} sem juros. ')
elif opc == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = val + (val * 20/100)
    prestacao = juros / parcela
    print(f'Sua compra ficou parcelada em {parcela}x de R${prestacao:.2f} com juros.')
    print(f'Sua compra de R${val:.2f} vai custar R${juros:.2f} no final.')
else:
    print('OPCAO INVALIDA! Tente novamente!')




'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
val = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe o salario do comprador: R$'))
fin = int(input('Quantos anos de financiamento? ')) * 12
parcela = val / fin
print(f'Para pagar uma casa de R${val:.2f} em {fin / 12:.0f} anos a prestacao sera de R${parcela:.2f}.')
if parcela > sal * 30 / 100:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')



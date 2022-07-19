'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
s = float(input('Informe o salario do funcionario: R$'))
a = s + (s * 15/100)
print(f'Um funcionario que recebia R${s}, com 15% de aumento, passou a greceber R${a:.2f}.')

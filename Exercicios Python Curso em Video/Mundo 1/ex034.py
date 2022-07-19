'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Qual é o salario do funcionario? R$'))
if sal <= 1250:
    novosal = sal + (sal * 15/100)
else:
    novosal = sal + (sal * 10/100)
print(f'Quem ganhava R${sal} passa a ganhar R${novosal:.2f} agora.')

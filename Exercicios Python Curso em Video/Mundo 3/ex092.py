'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
pessoa = {}
atual = date.today().year
pessoa['nome'] = str(input('Nome: ')).title()
pessoa['idade'] = atual - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho: (digite 0 se nao tiver) '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de Contratacao: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = (pessoa['idade'] + pessoa['contratacao'] + 35) - atual
print('=-='*10)
for k, v in pessoa.items():
    print(f'* {k.capitalize()} tem o valor {v}.')

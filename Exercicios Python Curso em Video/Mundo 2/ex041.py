'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificacao: MIRIM')
elif 14 >= idade > 9:
    print('Classificacao: INFANTIL.')
elif 19 >= idade > 14:
    print('Classificacao: JUNIOR.')
elif 25 >= idade > 19:
    print('Classificacao: SENIOR.')
else:
    print('Classificacao: MASTER.')

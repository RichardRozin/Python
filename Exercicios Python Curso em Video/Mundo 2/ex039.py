'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento.')
    print(f'Seu alistamento sera em {atual + (18 - idade)}.')
elif idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE!!!')
else:
    print(f'Voce ja deveria ter se alistado ha {idade - 18} anos.')
    print(f'Seu alistamento foi em {atual - (idade - 18)}.')


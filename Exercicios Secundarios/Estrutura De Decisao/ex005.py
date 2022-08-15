from datetime import date
'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''
data = str(input('Digite uma data no formato dd/mm/aaaa: '))
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
if dia > 31:
    print('Data invalida!')
    print('Digite o dia corretamente.')
elif mes > 12:
    print('Data invalida!')
    print('Digite o mes corretamente.')
elif ano > date.today().year:
    print('Data invalida!')
    print('Digite o ano corretamente.')
else:
    print('Data Valida!!!')
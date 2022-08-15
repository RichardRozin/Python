'''Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato
D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.'''
meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
from datetime import date


def data(d, m, a):
    ms = meses[m-1]
    return d, ms, a


dt = str(input('Informe uma data no formato DD/MM/AAAA: '))
while dt[2] and dt[5] != '/':
    dt = str(input('ERRO! Informe uma data no formato DD/MM/AAAA: '))
dia = int((dt[0] + dt[1]))
while dia > 31 or dia < 1:
    dia = int(input('ERRO! Digite o DIA corretamente: '))
mes = int((dt[3] + dt[4]))
while mes > 12 or mes < 1:
    mes = int(input('ERRO! Digite o MES corretamente: '))
ano = int((dt[6] + dt[7] + dt[8] + dt[9]))
while ano > date.today().year:
    ano = int(input('ERRO! Digite o ANO corretamente: '))
print(data(dia, mes, ano))

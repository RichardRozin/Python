'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: ')).title()
num = str(input('Numero de gols: '))
if num.isnumeric():
    num = int(num)
else:
    num = 0
if nome.strip() == '':
    ficha(gols=num)
else:
    ficha(nome, num)





''''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
dado = {}
dado['Jogador1'] = randint(1, 6)
dado['Jogador2'] = randint(1, 6)
dado['Jogador3'] = randint(1, 6)
dado['Jogador4'] = randint(1, 6)
print('SORTEANDO O DADO...')
sleep(2)
for k, v in dado.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('=-='*10)
print('== RANKING DOS JOGADORES ==')
n = 1
for i in sorted(dado, key= dado.get, reverse=True):
    sleep(1)
    print(f'{n}o lugar: {i} com {dado[i]} pontos.')
    n += 1


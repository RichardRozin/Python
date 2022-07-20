'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = {}
lista = []
soma = 0
jogador['nome'] = str(input('Nome do jogador: ')).title()
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,n):
    lista.append(int(input(f'   Quantos gols na {c+1}o partida? ')))
    soma += lista[c]
jogador['gols'] = lista.copy()
jogador['total'] = soma
print('=-='*30)
print(jogador)
print('=-='*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-='*30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for c, v in enumerate(lista):
    print(f'=> Na {c+1}o partida, fez {v} gols.')

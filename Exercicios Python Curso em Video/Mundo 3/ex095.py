'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = {}
lista = []
time = []

while True:
    jogador.clear()
    lista.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,n):
        lista.append(int(input(f'   Quantos gols na {c+1}o partida? ')))
    jogador['gols'] = lista.copy()
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*50)
print(f'{"cod.":>4} ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for c, v in enumerate(time):
    print(f'{c} ',end='')
    for d in v.values():
        print(f'{str(d):<13}   ',end='')
    print()
print('=-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Jogador nao encontrado!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for c, v in enumerate(time[busca]['gols']):
            print(f'No jogo {c} fez {v} gols')
    print('-'*40)
print('VOLTE SEMPRE!!!')







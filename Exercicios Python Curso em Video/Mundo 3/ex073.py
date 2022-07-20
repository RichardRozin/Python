''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time do Flamengo.'''
times = ('Palmeiras', 'Corinthians', 'Atletico PR', 'Internacional', 'Atletico MG', 'Fluminense', 'Santos', 'Sao Paulo', 'Flamengo', 'Botafogo',
         'Avaí', 'Bragantino', 'Atletico GO', 'Goiás', 'Ceará', 'Coritiba', 'America MG', 'Cuiabá', 'Juvertude', 'Fortaleza')
print('-='*15)
print(f'Lista de times do Brasileirao: {times}')
print('-='*15)
print(f'Os 5 primeiros colocados sao: {times[0:5]}')
print('-='*15)
print(f'Os 4 ultimos colocados sao: {times[-4:]}')
print('-='*15)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Flamengo esta na {times.index("Flamengo")+1} posicao.')
print('-='*15)


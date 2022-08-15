'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
e ao final mostrar o número de votos de cada candidato.'''
bolsonaro = lula = dog = 0
eleitores = int(input('Informe o numero de eleitores: '))
print('''Escolha um caditado abaixo: \n[22] Bolsonaro\n[13] Lula\n[7] Dog caramelo\n''')
for c in range(0, eleitores):
    voto = int(input(f'{c+1}° voto: '))
    while voto != 22 and voto != 13 and voto != 7:
        print('Opcao invalida! Tente novamente.')
        voto = int(input(f'{c+1}° voto: '))
    if voto == 22:
        bolsonaro += 1
    elif voto == 13:
        lula += 1
    elif voto == 7:
        dog += 1
if bolsonaro > lula and bolsonaro > dog:
    print(f'Vencedor Bolsonaro com {bolsonaro} votos.')
elif lula > bolsonaro and lula > dog:
    print(f'Vencedor Lula com {lula} votos.')
elif dog > lula and dog > bolsonaro:
    print(f'Vencedor Dog caramelo com {dog} votos.')
else:
    print('Houve um empate.')

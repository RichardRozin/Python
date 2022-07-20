'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''
while True:
    n = int(input('Digite um numero para ver a sua tabuada: '))
    if n < 0:
        print('Programa finalizado com sucesso!')
        break
    print('-'*40)
    for c in range(1, 11):
        print(f'{n} X {c:>2} = {n * c}')
    print('-' * 40)

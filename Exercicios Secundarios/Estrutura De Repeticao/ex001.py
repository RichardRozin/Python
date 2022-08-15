'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.'''
while True:
    nota = float(input('Digite uma nota de 0 a 10: '))
    if 0 <= nota <= 10:
        break
    else:
        print('Nota invalida! Tente novamente.')
print(f'Sua nota é {nota}.')

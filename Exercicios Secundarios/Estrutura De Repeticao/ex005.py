'''Faça um programa que calcule o mostre a média aritmética de N notas.'''
cont = 1
media = soma = 0
while True:
    nota = float(input('Digite uma nota: '))
    soma += nota
    media = soma / cont
    cont += 1
    resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp != 'S':
        break
print(f'A media geral foi de {media:.2f}')

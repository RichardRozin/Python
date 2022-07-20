''' Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um
número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
tupla = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
         'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n = int(input('Digite um numero entre 0 e 20 para ve-lo por extenso: '))
    if 0 <= n <=20:
        print(f'O numero {n} por extenco é {tupla[n]}.')
    else:
        print('Numero invalido! O numero deve estar entre 0 e 20!')
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print('Programa finalizado. Volte sempre!')












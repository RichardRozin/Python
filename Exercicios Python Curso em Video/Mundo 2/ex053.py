'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
frase = str(input('Digite uma frase: ')).strip()
separa = frase.split()
junto = ''.join(separa)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if inverso == junto:
    print(f'{frase} é um POLINDROMO.')
else:
    print(f'{frase} nao é um POLINDROMO.')





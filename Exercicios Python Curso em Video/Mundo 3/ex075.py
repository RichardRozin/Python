'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.'''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
tupla = (n1, n2, n3, n4)
print(f'Voce digitou os valores {tupla}.')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posicao.')
else:
    print('Nenhum valor 3 digitado.')
print('Os valores PARES digitados foram: ', end='')
for c in tupla:
    if c %2 == 0:
        print(c, end=' ')






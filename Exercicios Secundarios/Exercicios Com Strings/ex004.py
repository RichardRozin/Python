'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
* Quantos espaços em branco existem na frase.
* Quantas vezes aparecem as vogais a, e, i, o, u.'''
frase = str(input('Digite uma frase: ')).strip().upper()
cont = 0
print(f'Na frase \"{frase}\" existem {frase.count(" ")} espacos em branco.')
for c in frase:
    if c in 'AEIOU':
        cont += 1
print(f'Existem {cont} vogais na frase.')


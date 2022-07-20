'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
           'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavra:
    print(f'\nNa palavra {p} temos: ',end='')
    for l in p:
        if l in 'AEIOU':
            print(l, end=' ')
'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase: ')).strip()
print(f'A letra \"A\" apareceu {frase.count("a")} vezes na frase.')
print(f'A primeira letra \"A\" apareceu na {frase.find("a")+1} posicao.')
print(f'A ultima letra \"A\" apareceu na posicao {frase.rfind("a")+1}.')

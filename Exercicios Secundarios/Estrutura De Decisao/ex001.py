'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
letra = str(input('Digite uma letra qualquer: ')).strip().upper()[0]
if letra in 'AEIOU':
    print(f'A letra \"{letra}\" é uma VOGAL.')
else:
    print(f'A letra \"{letra}\" é uma CONSOANTE.')

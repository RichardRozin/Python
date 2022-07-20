'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''
print('='*30)
print('10 TERMOS DE UMA PA'.center(30))
print('='*30)
p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
formula = p + (10-1) * r
for c in range(p, formula + 2, r):
    print(c,end=' -> ')
print('Acabou!')

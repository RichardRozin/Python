'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.'''
import moeda
while True:
    valor = float(input('Digite um preco: R$ '))
    print('='*45)
    print(f'Aumentando 10% de R${valor:.2f} temos R${moeda.aumentar(valor, 10):.2f}.')
    print(f'Diminuindo 20% de R${valor:.2f} temos R${moeda.diminuir(valor, 20)}.')
    print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor)}.')
    print(f'A metade de R${valor:.2f} é R${moeda.metade(valor)}.')
    print('='*45)
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont != 'S':
        break
print('='*45)
print('Volte sempre!!!')



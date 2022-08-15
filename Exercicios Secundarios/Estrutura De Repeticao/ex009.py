'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''
total = 0
cds = int(input('Informe a quantidade de cds comprados: '))
for c in range(0, cds):
    valor = float(input(f'Qual foi o preco do {c+1}° CD? R$'))
    total += valor
media = total / cds
print(f'O valor total gasto nessa colecao foi de R${total:.2f} e o valor medio foi de R${media:.2f}.')

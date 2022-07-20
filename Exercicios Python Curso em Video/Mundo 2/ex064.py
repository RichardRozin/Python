'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}.')

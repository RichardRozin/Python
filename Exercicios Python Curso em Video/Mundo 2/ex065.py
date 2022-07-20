'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
opc = 'S'
maior = menor = cont = soma = 0
while opc == 'S':
    n = int(input('Digite um numero: '))
    opc = str(input('Quer continuar? ')).strip().upper()[0]
    soma += n
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
media = soma / cont
print(f'Voce digitou {cont} numeros e a media foi {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')

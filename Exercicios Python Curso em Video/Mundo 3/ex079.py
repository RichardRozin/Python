''' Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []
while True:
    n = int(input('Digite um numero: '))
    if n in lista:
        print(f'Numero duplicado! Digite um numero diferente dos anteriores: ')
    else:
        lista.append(n)
        print(f'Numero {n} adicionado com sucesso!')
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*16)
lista.sort()
print(f'Voce digitou os valores {lista}.')


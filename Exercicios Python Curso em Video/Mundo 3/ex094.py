'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionárioe todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = {}
lista = []
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    sexo = str(input('Sexo: [M][F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo invalido! Use apenas [M] ou [F]: ').upper()[0])
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    cont = str(input('Deseja continuar? [S][N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('ERRO! Digite apenas [S] ou [N]: ').upper()[0])
    if cont == 'N':
        break
media = soma / len(lista)
print('=-='*30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'A media de idade é de {media} anos.')
print('As mulheres cadastradas foram: ',end=' ')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'])
print('Lista de pessoas que estao acima da media:')
for c in lista:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()


















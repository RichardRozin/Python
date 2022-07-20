'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
soma = idadevelho = cont = 0
homemvelho = ''
for c in range(0,4):
    print(f'-'*5, f'{c+1}o PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if c == 0 and sexo == 'M':
        homemvelho = nome
        idadevelho = idade
    else:
        if idade > idadevelho and sexo == 'M':
            idadevelho = idade
            homemvelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f'A media do grupo é de {soma / 4} anos.')
print(f'O homem mais velho tem {idadevelho} anos e se chama {homemvelho}.')
print(f'Ao todo sao {cont} mulheres com menos de 20 anos.')





'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
print('-='*20)
print('         CADASTRO DE PESSOAS')
maio = homem = mulher = 0
while True:
    print('-=' * 20)
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if s == 'M' or s == 'F':
        if i >= 18:
            maio += 1
        if s == 'M':
            homem += 1
        if s == 'F' and i < 20:
            mulher += 1
    else:
        print('Sexo invalido!')
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*20)
print(f'Ao todo tivemos {maio} pessoas maiores de idade.')
print(f'Ao todo tivemos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')

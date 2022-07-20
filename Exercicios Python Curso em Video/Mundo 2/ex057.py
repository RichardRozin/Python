'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Informe seu sexo [M, F]: ')).strip().upper()[0]
while 'M' != sexo != 'F':
    sexo = str(input('Dados invalidos! Informe seu sexo corretamente [M, F]: ')).strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso!')



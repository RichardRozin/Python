'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Digite seu nome completo: ')).strip().title()
separado = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separado[0]}.')
print(f'Seu ultimo nome é {separado[len(separado)-1]}.')

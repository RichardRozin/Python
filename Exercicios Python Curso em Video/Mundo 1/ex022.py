'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome: '))
print(f'Seu nome em letras maiusculas é {nome.upper()}.')
print(f'Seu nome em letras minusculas é {nome.lower()}.')
separado = nome.split()
junto = ''.join(separado)
print(f'Seu nome tem ao todo {len(junto)} letras.')
print(f'Seu primeiro nome é {separado[0].capitalize()} e ele tem {len(separado[0])} letras.')





'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''
cid = str(input('Digite o nome da sua cidade: ')).capitalize().strip()
separado = cid.split()
print(f'{"Santo" in separado[0]}')



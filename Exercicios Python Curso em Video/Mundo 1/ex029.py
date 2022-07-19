'''Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
vel = int(input('Qual é a velocidade atual do carro? '))
if vel <= 80:
    print(f'\033[32mVoce esta dentro do limite de velocidade da via!')
else:
    multa = (vel - 80) * 7
    print(f'\033[31mVOCE FOI MULTADO! Voce excedeu o limite permitido que é 80Km/h.')
    print(f'Voce deve pagar uma multa de \033[33mR${multa:.2f}!')
print('\033[32mTenha um bom dia! Dirija com seguranca!')

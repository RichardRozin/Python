'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''
cont = soma = 0
while True:
    cont += 1
    idade = int(input('Digite uma idade: '))
    soma += idade
    media = soma / cont
    resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp != 'S':
        break
print(f'A media de idade da turma é de {media} anos.')
print('Classificacao ',end='')
if 0 <= media <= 25:
    print('jovem.')
elif 26 <= media <= 60:
    print('adulto.')
else:
    print('idoso.')

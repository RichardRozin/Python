'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
cont = 0
p1 = str(input('Telefonou para a vítima? [S/N]')).strip().upper()[0]
if p1 == 'S':
    cont += 1
p2 = str(input('Esteve no local do crime? [S/N]')).strip().upper()[0]
if p2 == 'S':
    cont += 1
p3 = str(input('Mora perto da vítima? [S/N]')).strip().upper()[0]
if p3 == 'S':
    cont += 1
p4 = str(input('Devia para a vítima? [S/N]')).strip().upper()[0]
if p4 == 'S':
    cont += 1
p5 = str(input('Já trabalhou com a vítima? [S/N]')).strip().upper()[0]
if p5 == 'S':
    cont += 1
if cont < 2:
    print('Voce é Inocente!')
elif cont == 2:
    print('Voce é Suspeito(a)!')
elif 2 < cont <= 4:
    print('Voce é Cumplice!')
else:
    print('Voce é o Assassino(a)!')

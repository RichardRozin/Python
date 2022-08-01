'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
alt = float(input('Informe sua altura em metros: '))
masc = (72.7 * alt) - 58
fem = (62.1 * alt) - 44.7
print(f'Com uma altura de {alt}m, seu peso ideal é de {masc:.2f}Kg. [SEXO MASCULINO]')
print(f'Com uma altura de {alt}m, seu peso ideal é de {fem:.2f}Kg. [SEXO FEMININO]')

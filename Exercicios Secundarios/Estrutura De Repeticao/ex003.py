'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''
nome = str(input('Informe seu nome: ')).strip().title()
while len(nome) < 3:
    nome = str(input('Nome invalido! Digite o nome corretamente: ')).strip().title()
print('Nome OK')
idade = int(input('Informe a sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade invalida! Digite a sua idade corretamente: '))
print('Idade OK')
salario = float(input('Informe seu salario: R$'))
while salario < 0:
    salario = float(input('Salario invalido! Informe seu salario corretamente: R$'))
print('Salario OK')
sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo invalido! Informe seu sexo corretamente: ')).strip().upper()[0]
print('Sexo OK')
estasivil = str(input('Informe seu estado sivil: ')).strip().upper()[0]
while estasivil != 'S' and 'C' and 'V' and 'D':
    estasivil = str(input('Estado civil incorreto! Informe seu estado sivil corretamente: ')).strip().upper()[0]
print('Estado civil OK')




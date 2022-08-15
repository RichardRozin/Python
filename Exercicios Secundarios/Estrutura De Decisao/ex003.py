'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
sal = float(input('Informe seu salario atual: R$'))
novosal = percentual = aumento = 0
if sal <= 280:
    percentual = 20
    aumento = (sal * percentual/100)
    novosal = sal + aumento
elif 280 < sal <= 700:
    percentual = 15
    aumento = (sal * percentual/ 100)
    novosal = sal + aumento
elif 700 < sal <= 1500:
    percentual = 10
    aumento = (sal * percentual / 100)
    novosal = sal + aumento
else:
    percentual = 5
    aumento = (sal * percentual / 100)
    novosal = sal + aumento
print(f'O seu antigo salario era de R${sal:.2f}.')
print(f'O percentual de aumento aplicado foi de {percentual}%.')
print(f'O valor aumentado foi de R${aumento:.2f}.')
print(f'Seu novo salario agora é de R${novosal:.2f}.')

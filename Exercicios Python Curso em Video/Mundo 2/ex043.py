'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''
peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('QUal a sua altura? (m) '))
imc = peso / alt ** 2
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Voce esta abaixo do peso ideal!')
elif imc < 25:
    print('PARABENS! Voce esta no peso ideal.')
elif imc < 30:
    print('Voce esta com sobrepeso!')
elif imc < 40:
    print('Voce esta com obesidade!')
else:
    print('Voce esta com obesidade MORBIDA! Cuidado!')



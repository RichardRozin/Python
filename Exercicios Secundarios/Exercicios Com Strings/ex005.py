'''Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.'''
valido = False
while True:
    cpf = str(input('Digite seu cpf: '))
    if (cpf[0:3]).isnumeric() and (cpf[4: 7]).isnumeric() and (cpf[8: 11]).isnumeric() and (cpf[12:]).isnumeric():
        valido = True
        if cpf[3] and cpf[7] == '.':
            valido = True
            if cpf[11] == '-':
                valido = True
            else:
                valido = False
    if valido:
        print(f'CPF {cpf} validado com sucesso!')
        break
    else:
        print(f'CPF {cpf} invalido! Tente novamente! ')




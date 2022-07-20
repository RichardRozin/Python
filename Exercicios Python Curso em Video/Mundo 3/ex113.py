'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
'''


def leiaint(msg):
    print('-' * 40)
    while True:
        try:
            num = int(input(msg))
        except:
            print('\033[31mERRO! Digite um numero inteiro valido: \033[m')
        else:
            return num


def leiafloat(msg):
    print('-' * 40)
    while True:
        try:
            num = float(input(msg))
        except:
            print('\033[31mERRO! Digite um numero real valido: \033[m')
        else:
            return num


i = leiaint('Digite um numero inteiro: ')
f = leiafloat('Digite um numero real: ')
print('=-='*20)
print(f'O valor inteiro digitado foi {i} e o valor real foi {f}.')

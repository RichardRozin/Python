'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')'''


def leiaint(msg):
    '''
    funcao responsavel por indicar se um valor digitado realmente é um numero.
    :param msg: uma mensagem para o usuario
    :return: o numero em formato inteiro.
    '''
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
    return num


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')
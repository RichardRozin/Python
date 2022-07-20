'''Faça um programa que tenha uma função chamada frase(), que receba um
texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''


def frase(msm):
    tam = len(msm) + 4
    print('~'*tam)
    print(f'  {msm}')
    print('~' * tam)


frase('RICHARD ROZIN')
frase('CURSO DE PYTHON NO YOUTUBE')
frase('CEV')






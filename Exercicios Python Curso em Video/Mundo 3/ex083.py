'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite uma expressao: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressao esta CORRETA!')
else:
    print('Sua expressao esta INCORRETA!')


'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
print('=-='*10)
print('      EQUACAO DO 2 GRAU')
print('=-='*10)
print('FORMULA: ax2 + bx + c.')
x1 = x2 = delta = 0
a = int(input('Informe o valor de A: '))
if a != 0:
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de c: '))
    delta = b**2 -4*a*c
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f'X1 é igual a {x1}.')
    print(f'X2 é igual a {x2}.')
    print(f'O delta é igual a {delta}.')
    if delta < 0:
        print(f'A equacao {a}x² + {b}x + {c} nao possui raizes reais, pois o delta é negativo.')
    if delta == 0:
        print(f'A equacao {a}x² + {b}x + {c} possui rapenas uma raiz real, pois o delta é igual a 0.')
    if delta > 0:
        print(f'A equacao {a}x² + {b}x + {c} possui 2 raizer reais pois o delta é maior que 0.')
else:
    print('A equacao nao pode ser do 2 grau, pois o valor de A é igual a 0.')

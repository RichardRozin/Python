'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima podem formar um triangulo ',end='')
    if a != b and b != c and c != a:
        print('ESCALENO.')
    elif a == b != c or a == c != b or b == c != a:
        print('ISOCELES.')
    elif a == b and b == c:
        print('EQUILATERO.')
else:
    print('Os segmentos acima nao podem formar um triangulo!')

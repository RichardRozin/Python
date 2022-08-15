'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''
lista = []
soma = media = contmedia = menosdesete = 0
valor = float(input('Informe um valor: '))
while valor != -1:
    soma += valor
    lista.append(valor)
    valor = float(input('Informe outro valor: '))
media = soma / len(lista)
print(f'Ao todo foram {len(lista)} valores lidos.')
for c in lista:
    print(c, end=' ')
    if c > media:
        contmedia += 1
    if c < 7:
        menosdesete += 1
print(f'\nA soma de todos os valores é {soma}.')

print(f'A media de todos os valores é {media}.')
print(f'Ao todo temos {contmedia} valores acima da media.')
print(f'Ao todo temos {menosdesete} valores abaixo de 7.')



'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.'''
lista = []
media = soma = 0
while True:
    nome = str(input('Nome do atleta: ')).strip().title()
    if nome == '':
        break
    print(f'Atleta: {nome}')
    for c in range(0, 5):
        salto = float(input(f'{c+1}o Salto: '))
        soma += salto
        lista.append(salto)
    media = soma / 5
    print('=-='*12)
    print('Resultafo final: ')
    print(f'Atleta: {nome}')
    print(f'Saltos: {lista}')
    print(f'Media dos saltos: {media} m.')
    print('=-=' * 12)
print('=-=' * 6)
print('Fim do programa.')
print('=-=' * 6)
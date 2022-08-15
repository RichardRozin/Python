'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.'''
nome = str(input('Digite seu nome: ')).strip().upper()
for p in range(0, len(nome)):
    print(nome[:p+1])

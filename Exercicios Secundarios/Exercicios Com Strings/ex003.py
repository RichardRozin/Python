'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida'''
nome = str(input('Digite seu nome: ')).strip().upper()
c = len(nome)
while c > 0:
    print(nome[:c])
    c -= 1
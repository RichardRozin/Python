'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''


def menu():
    print('-' * 30)
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)
    print('''\033[33m1 -\033[34m Ver pessoas Cadastradas: \n\033[33m2 -\033[34m Cadastrar nova Pessoa: \n\033[33m3 -\033[34m Sair do Programa:\033[m''')
    print('-' * 30)


def opcao(n, nome):
    print('-' * 30)
    if n == 3:
        print('Saindo do Sistema... Ate logo!')
        print('-' * 30)
    else:
        if n == 1:
            print(f'PESSOAS CADASTRADAS'.center(30))
            print('-' * 30)
            lerarquivo(nome)
        else:
            print('NOVO CADASTRO'.center(30))
            print('-' * 30)
            pessoa = str(input('Nome: ')).capitalize().strip()
            idade = leiaint('Idade: ')
            cadastrar(nome, pessoa, idade)




def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def leiaint(idade):
    while True:
        try:
            i = int(input(idade))
        except:
            print('Erro! Digite uma idade valida.')
        else:
            return i


def cadastrar(nome, pessoa='desconhecido', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print('Ouve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {pessoa} adicionado.')
            a.close()
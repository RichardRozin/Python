'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.'''
while True:
    nome = str(input('Nome de usuario: ')).strip()
    senha = str(input('Senha: ')).strip()
    if nome != senha:
        break
    else:
        print('ERRO! A senha nao pode ser igual ao nome de usuario!')
print('Credenciais salvas com sucesso!')

'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''


def notas(*num, sit=False):
    '''
    funcao responsavel por informar os dados de um aluno.
    :param num: parametro que recebe varias notas de um aluno.
    :param sit: a situacao em que o aluno se encontra.
    :return: retorna um dicionario com as informacoes do aluno.
    '''
    dic = {}
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    media = sum(num) / dic['total']
    dic['media'] = f'{media:.2f}'
    if sit:
        if media >= 7:
            dic['situacao'] = 'BOA'
        elif 5 <= media < 7:
            dic['situacao'] = 'REGULAR'
        else:
            dic['situacao'] = 'RUIM'
    return dic


resp = notas(10, 10, 8, 4, 4, sit=True)
print(resp)
help(notas)


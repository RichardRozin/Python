'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função formatada(), desenvolvida no desafio 108.'''
import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, formato=True)}.')
print(f'Diminuindo 20%, temos {moeda.diminuir(p, 20, formato=True)}.')

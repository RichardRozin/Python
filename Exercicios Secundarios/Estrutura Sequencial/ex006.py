'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
MB = float(input('Informe o tamanho do arquivo em MB: '))
mb = float(input('Informe a velocidade da sua internet em mb/s: '))
calc = MB / (mb/8)
temp = calc / 60
print(f'Um arquivo de {MB}MB, baixando a {mb}mb/s levara {temp} minutos para finalizar.')

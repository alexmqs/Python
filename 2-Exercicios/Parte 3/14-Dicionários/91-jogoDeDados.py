'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from operator import itemgetter
from random import randint
from time import sleep

# declarando variáveis
jogadores = {}
ranking = []
# fim declarando variáveis

for c in range(1, 5):
    jogadores[f"jogador{c}"] = int(randint(1, 6))

print('Valores sorteados:')
for chaves, valores in jogadores.items():
    print(f'O {chaves} tirou {valores}')
    sleep(1)

print('---'*10)

# copiando lista e ordenando
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)

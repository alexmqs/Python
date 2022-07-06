''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
# declaração das variáveis
gerJog = {}
gols = []
# fim declaração das variáveis

# estrutura principal
gerJog['nome'] = str(input('Nome do Jogador: '))
contPart = int(input(f'Quantas partidas {gerJog["nome"]} jogou? '))

for c in range(0, contPart):
    gols.append(int(input(f'Quantos gol na partida {c}? ')))

gerJog['gols'] = gols[:]

# função interna de soma = sum
gerJog['total'] = sum(gols)
# fim estrutura principal


# exibindo resultados
print('=-='*30)
print(gerJog)
print('=-='*30)
for k, v in gerJog.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-='*30)
print(f'O jogador {gerJog["nome"]} jogou {contPart} partidas.')
for v in gerJog['gols']:
    print(f'=> Na partida {gerJog["gols"].index(v)}, fez {v} gols')
# fim exibindo resultados

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
# declarando váriaveis
time = []
jogadores = {}
gols = []
# fim declarando váriaveis

# estrutura principal
while True:
    print('---'*20)
    gols.clear()
    gols.clear()
    jogadores['nome'] = str(input('Nome do Jogador: '))
    contPart = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    # quantos gol na partida
    for c in range(0, contPart):
        gol = int(input(f'Quantos gol na partida {c}? '))
        gols.append(gol)
    # fim quantos gol na partida
    jogadores['gols'] = gols[:]

    # função interna de soma = sum
    jogadores['total'] = sum(gols)

    time.append(jogadores.copy())

    # pergunta
    while True:
        p = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if p in 'SN':
            break
        else:
            print('Sim ou não...')
    if p == 'S':
        print('continuando...')
    else:
        print('saindo do cadastro...')
        print('==='*20)
        break
    # fim pergunta
# fim estrutura principal

# organização da tabela que será exibida
'''print(f'{"cod":<4}{"nome":<20}{"gols":<15}{"total":>5}')

for e in cad:

    print(
        f'{cad.index(e):^4}{e["nome"]:<20}{str(e["gols"]):<15}{e["total"]:<5}')'''

print('cod ', end='')
for e in jogadores.keys():
    print(f'{e:<15}', end='')
print()
print('---'*20)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for vv in v.values():
        print(f'{str(vv):<15}', end='')
    print()
print('---'*20)
# fim organização da tabela que será exibida

# exibindo detalhes de cada jogo do jogador
while True:
    pp = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if pp == 999:
        print('Saindo...')
        break
    if pp >= len(time):
        print('Erro! Não existe Jogador com o código digitado.')
    else:
        print(f'---Levantamento do jogador {time[pp]["nome"]}')
        for i, e in enumerate(time[pp]["gols"]):
            print(f'No jogo {i+1} fez {e} gols.')
# exibindo detalhes de cada jogo do jogador

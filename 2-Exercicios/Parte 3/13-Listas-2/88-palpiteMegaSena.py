'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

# inicializando as variáveis
listaMega = []

print('-'*50)
print(f"{'MEGA SENA':^50}")
print('-'*50)

p = int(input('Quanto jogos você quer que eu sorteie? '))

print(f"{'-'*15} {'SORTEANDO':^} {p} {'JOGOS':^} {'-'*15}")

# estrutura principal
for c in range(p):
    while True:
        # gerando números aleatórios
        e = randint(0, 60)
        # testando nº repetido
        if e in listaMega:
            listaMega.remove(e)
            e = randint(0, 60)
            listaMega.append(e)
        else:
            listaMega.append(e)

        # saindo  da lista
        if len(listaMega) >= 6:
            print(f"{' '*5}{'Jogo '} {c+1}: {sorted(listaMega)}")
            listaMega.clear()
            break

    sleep(0.5)

print(f"{'-'*15} {'< BOA SORTE! >':^} {'-'*15}")

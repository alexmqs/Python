'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas no final do jogo.
'''
from random import randint, randrange
from time import sleep

vitoria = 0

while True:
    # Jogador
    jogadorNum = int(input('Digite um número: '))
    jogadorParOuImpar = str(input('Par ou Ímpar? ')).upper().strip()[0]
    pcNum = randrange(0, 1000)
    soma = jogadorNum + pcNum

    if jogadorParOuImpar == 'P':
        jogadorParOuImpar = 'Par'
        pcParOuImpar = 'Ímpar'
        print(
            f'O Jogador escolheu = {jogadorParOuImpar} e o Computador = {pcParOuImpar}')
    else:
        jogadorParOuImpar = 'Ímpar'
        pcParOuImpar = 'Par'
        print(
            f'O Jogador escolheu = {jogadorParOuImpar} e o Computador = {pcParOuImpar}')

    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'

    if resultado == jogadorParOuImpar:
        print(f'Jogador venceu! Soma = {soma} e o foi resultado {resultado}')
        print(f'Vamos jogar novamente...')
        vitoria += 1
        sleep(1)

    else:
        print(
            f'Computador venceu! Soma = {soma} e o foi resultado {resultado}')
        break


print(f'GAME OVER!!!, você obteu {vitoria} vitórias')

'''
    pc = randrange(0, 1000)



    if jogador % 2 == 0:
        j = 'Par'
        print(f'Você jogou {j}, {jogador}')
    else:
        j = 'Ímpar'
        print(f'Você jogou {j}, {jogador}')

    # PC
    if j == 'Par':
        while True:
            pc = randrange(0, 100)
            if pc % 2 == 0:
                p = 'Par'
            else:
                p = 'Ímpar'
                break
        print(f'O computador jogou {pc}, {p}')
    else:
        while True:
            pc = randrange(0, 100)
            if pc % 2 == 0:
                p = 'Par'
                break
            else:
                p = 'Ímpar'
        print(f'O computador jogou {pc}, {p}')

    final = pc + jogador'''

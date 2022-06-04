'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas no final do jogo.
'''
from random import randint
from time import sleep

vitoria = 0

while True:
    jogadorNum = int(input('Digite um número: '))
    pcNum = randint(0, 1000)
    soma = jogadorNum + pcNum

    while True:
        jogadorParOuImpar = str(input('Par ou Ímpar? ')).upper().strip()[0]
        if jogadorParOuImpar in ('PI'):
            break

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
        print(
            f'Jogador venceu! Você jogou {jogadorNum} e o computador jogou {pcNum}, somando = {soma} e o resultado foi {resultado}')
        print(f'Vamos jogar novamente...')
        vitoria += 1
        sleep(1)
    else:
        print(
            f'Computador venceu! Você jogou {jogadorNum} e o computador jogou {pcNum}, somando = {soma} e o resultado foi {resultado}')
        break

print(f'GAME OVER!!!, você obteu {vitoria} vitórias')

# outro modo
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador. Total de {total}', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!!, você obteu {v} vitórias')

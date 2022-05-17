'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from traceback import print_tb

print('---Pedra, papel e tesoura---\n1-Pedra\n2-Papel\n3-Tesoura')

eu = int(input('Digite uma das opções acima: '))
pc = int(randint(1, 3))
jpc = ''
jeu = ''

if pc == 1:
    jpc = 'Pedra'
elif pc == 2:
    jpc = 'Papel'
elif pc == 3:
    jpc = 'Tesoura'


if eu == 1:
    jeu = 'Pedra'
elif eu == 2:
    jeu = 'Papel'
elif eu == 3:
    jeu = 'Tesoura'



if eu and pc != (1, 2, 3):
    print('Erro')
else:
    if eu == pc:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Empate')
    elif eu == 1 and pc == 3:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Você Ganhou')
    elif eu == 2 and pc == 1:
        print('Você Ganhou')
    else:
        print('Você perdeu')

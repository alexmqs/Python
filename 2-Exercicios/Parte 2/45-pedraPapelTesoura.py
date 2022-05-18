'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint

print('''
Pedra, papel e tesoura
0-Pedra
1-Papel
2-Tesoura''')

eu = int(input('Digite uma das opções acima: '))
itens = ('Pedra', 'Papel', 'Tesoura')
pc = int(randint(0, 2))
jpc = itens[pc]
jeu = itens[eu]

print('-='*20)
if eu == 0 or eu == 1 or eu == 2:
    if eu == pc:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Empate')
    elif eu == 0 and pc == 2:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Você Ganhou')
    elif eu == 1 and pc == 0:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Você Ganhou')
    elif eu == 2 and pc == 1:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Você Ganhou')
    else:
        print(f'O computador jogou {jpc}')
        print(f'Você jogou {jeu}')
        print('Você perdeu')
else:
    print('A opção que foi digitada está incorreta.')
print('-='*20)

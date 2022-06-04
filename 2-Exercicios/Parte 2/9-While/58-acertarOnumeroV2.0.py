'''
Melhore o desafio 28, onde o computador pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
'''
# Código
# Importando


print('Pense em um número de 0 até 5.')
sorteio = randint(0, 5)
numero = int(input('Pensou em qual número? '))
print('Processando...')
sleep(2)
# Estrutura
if numero == sorteio:
    print('Acertou.')
else:
    print('Errou.')
# Exibindo
print(f'O número sorteado foi {sorteio}')
'''

from random import randint
from time import sleep
print('O PC irá pensar em um número!')
sorteio = randint(0, 10)
print(sorteio)
print('O PC está pensando...')
sleep(2)
print('Pronto!')

numero = int(input('Qual número o PC pensou? '))
palpite = 1

while numero != sorteio:
    numero = int(input('Errou, Digite novamente em qual número o PC pensou? '))
    palpite += 1
print(f'''Acertou!!!
O número que você digitou foi o {numero} e o número que o PC pensou foi {sorteio}.
Você precisou de {palpite} palpites para acertar!''')


'''Outra solução

computador = randint(0, 10)
print('O PC irá pensar em um número!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual número o PC pensou? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''

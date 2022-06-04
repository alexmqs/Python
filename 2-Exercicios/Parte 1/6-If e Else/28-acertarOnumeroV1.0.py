'''
Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

# Código
# Importando
from random import randint
from time import sleep

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

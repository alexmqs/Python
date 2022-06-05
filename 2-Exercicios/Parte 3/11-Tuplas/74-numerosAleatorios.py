'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint, sample

tupla = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
# ou
# tupla = tuple(sample(range(10), 5))

print(f'O números sorteados foram: {tupla}.')
print(f'O maior valor é {max(tupla)} e o menor é {min(tupla)}.')

'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from random import randint
from time import sleep


def linha():
    print('=-'*20)


def maior(*valores):
    linha()
    sleep(0.5)
    print('Analisando os valores informados...')
    sleep(0.5)
    contador = 0
    if len(valores) == 0:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')
    else:
        for c in valores:
            print(c, end=' ')
            contador += 1
            if contador == len(valores):
                print(f'Foram informados {len(valores)} valores ao todo.')
            sleep(0.5)
        print(f'O maior valor informado foi {max(valores)}')


maior(randint(0, 100), randint(0, 100), randint(
    0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior(randint(0, 100), randint(0, 100), randint(
    0, 100))
maior(randint(0, 100), randint(0, 100))
maior(randint(0, 100))
maior()
linha()

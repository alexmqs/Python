'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''


from random import randint
from time import sleep


def linha():
    print('=-'*30)


def sorteio(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        v = randint(1, 10)
        lista.append(v)
        print(v, end=' ')
        sleep(0.5)
    print('Pronto!')
    sleep(1)


def somaPar(valores):
    somando = 0

    sleep(1)
    for e in valores:
        if e % 2 == 0:
            somando += e
    print(f'Somando os valores pares de {valores}, temos {somando}.')


lista = []

sorteio(lista)
linha()
somaPar(lista)

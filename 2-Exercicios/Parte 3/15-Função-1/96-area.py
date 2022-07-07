'''
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def titulo():
    print('Controle de terreno!!!')


def linha():
    print('-'*30)


def area(a, b):
    r = a * b
    print(f'A área de um terreno {l}x{c} é de {r}m².')


titulo()
linha()

l = float(input('Largura (m): '))
c = float(input('Comprimento(m): '))
area(l, c)
linha()

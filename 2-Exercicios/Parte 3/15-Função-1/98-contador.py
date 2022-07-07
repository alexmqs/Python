'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep


def linha():
    print('=-'*15)


def contador1():
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ', flush=True)
        sleep(0.5)
        if c == 10:
            print('FIM!')


def contador2():
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.5)
        if c == 0:
            print('FIM!')


def contador3(a, b, c):
    if a > b and c > 0:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for cc in range(a, b-c, -c):
            print(cc, end=' ', flush=True)
            sleep(0.5)
            if cc == b:
                print('FIM!')
    elif a > b and c < 0:
        c *= -1
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for cc in range(a, b-c, -c):
            print(cc, end=' ', flush=True)
            sleep(0.5)
            if cc == b:
                print('FIM!')

    elif a > b and c == 0:
        print(f'Contagem de {a} até {b} de 1 em 1')
        for cc in range(a, b-1, -1):
            print(cc, end=' ', flush=True)
            sleep(0.5)
            if cc == b:
                print('FIM!')
    else:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for cc in range(a, b, c):
            print(cc, end=' ', flush=True)
            sleep(0.5)
            if cc == b:
                print('FIM!')


linha()
contador1()
linha()
contador2()
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador3(i, f, p)
print()

'''
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
'''


from random import randint


def linhaPersonalizada(msg):
    print('=-'*30)
    print(msg)
    print('-='*30)


linhaPersonalizada('PYTHON')
linhaPersonalizada('TESTANDO')
linhaPersonalizada('FIM DO TESTANDO')


def soma(a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(f'A soma de a + b é igual a {s} ')


soma(1, 2)
soma(a=23, b=45)
soma(b=4, a=24)

# vários parametros


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


contador(2, 1, 5)
contador(22, 13, 5, 56, 90)
contador(11, 11, 32, 87, 0)
# fim vários parametros


def mult2(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
print(valores)
mult2(valores)
print(valores)


def somando(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somando(5, 2)
somando(3, 7, 4)

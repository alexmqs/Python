'''
Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções,
argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
'''

# interactive help
'''help(print)
print(print.__doc__)'''
# end interactive help

# doc string




from random import randint
def contador(i, f, p):
    """Contagem de início até determinado número pulando determinados números

    Args:
        i: início da contagem
        f: final da contagem
        p: pular de quanto a quanto
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


'''contador(0, 100, 10)'''
'''help(contador)'''
# end doc string

# parâmetros opcionais

#parâm. formal


def somar(a=0, b=0, c=0):
    '''
    Soma de 3 valores

    Args:
        a (int, optional): 1º valor. Defaults to 0.
        b (int, optional): 2º valor. Defaults to 0.
        c (int, optional): 3º valor. Defaults to 0.
    '''
    s = a+b+c
    print(f'A soma é {s}')


help(somar)
# parâm. real
somar(2, 3)
somar(a=2, b=3, c=4)
# end parâmetros opcionais

# escopo de variáveis


def teste():
    # x tem o escopo local (dentro da função)
    x = 8
    print(f'Na função o n tem o valor {n}')
    print(f'Na função o x tem o valor {x}')


# n tem o escopo global (dentro da estrura principal)
n = 2
print(f'No programa principal o n tem o valor {n}.')
teste()


def teste2(f):
    # l tem o escopo local (dentro da função)
    y = 10
    f = 2
    print(f'Na função o l tem o valor {f}')
    print(f'Na função o y tem o valor {y}')


l = 12
print(f'No programa principal o l tem o valor {l}.')
teste2(l)


def teste3(f):
    global k
    k = 30
    y = 10
    f += 2
    print(f'Na função o f tem o valor {f}')
    print(f'Na função o k tem o valor {k}')
    print(f'Na função o y tem o valor {y}')


k = 12
teste3(k)
print(f'No programa principal o k tem o valor {k}.')


# end escopo de variáveis

# retorno de valores (return)


def somar2(a=0, b=0, c=0):
    '''
    Soma de 3 valores

    Args:
        a (int, optional): 1º valor. Defaults to 0.
        b (int, optional): 2º valor. Defaults to 0.
        c (int, optional): 3º valor. Defaults to 0.
    '''
    s = a+b+c
    return s


# parâm. real
print(somar2(randint(0, 10), randint(0, 10)))
r1 = somar2(randint(0, 10), randint(0, 10))
r2 = somar2(randint(0, 10), randint(0, 10))
r3 = somar2(randint(0, 10), randint(0, 10))
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

# end retorno de valores (return)

# prática


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')

'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
# inicializando as variáveis
lista = [[], [], []]
s = 0
ss = 0

# percorrendo a lista
for i in lista:
    # percorrendo o indíce 0 da lista
    if lista.index(i) == 0:
        for i0 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[0])}]: ')))
    # percorrendo o indíce 1 da lista
    if lista.index(i) == 1:
        for i1 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[1])}]: ')))
    # percorrendo o indíce 2 da lista
    if lista.index(i) == 2:
        for i2 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[2])}]: ')))

print('=-'*40)
# percorrendo a lista
for i in lista:
    # exibindo a lista
    print(f'[{i[0]}] [{i[1]}] [{i[2]}]')
print('=-'*40)

# percorrendo a lista
for i in lista:
    for ii in i:
        # testando se o elemento é par
        if ii % 2 == 0:
            # somando
            s += ii
    # somando elemento do indíce 2 dentro de um determinado índice da lista
    ss += i[2]

print(f'A soma dos números pares é {s}.')
print(f'A soma dos números da terceira coluna é {ss}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')

# outra code, com poucas linhas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna = maiorValor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]

    somaColuna += matriz[linha][2]
    print()

print(f'A soma dos números pares é {somaPar}.')
print(f'A soma dos números da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

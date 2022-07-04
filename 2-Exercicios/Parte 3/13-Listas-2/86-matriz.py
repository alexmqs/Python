'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
# variáveis
lista = [[], [], []]

for i in lista:
    if lista.index(i) == 0:
        for i0 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[0])}]: ')))
    if lista.index(i) == 1:
        for i1 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[1])}]: ')))
    if lista.index(i) == 2:
        for i2 in lista:
            lista[lista.index(i)].append(
                int(input(f'Digite um número: [{lista.index(i)},{len(lista[2])}]: ')))

for i in lista:
    print(f'[{i[0]}] [{i[1]}] [{i[2]}]')

# outra code, com poucas linhas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

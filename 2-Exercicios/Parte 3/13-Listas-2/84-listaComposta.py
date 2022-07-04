'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
# variáveis
# lista principal
lp = []
# lista temp
lt = []
# maior e menor
maior = menor = 0

while True:
    # incrementando na lista
    lt.append(str(input('Digite o nome: ')))
    lt.append(float(input('Digite o peso: ')))

    # identificando o peso maior e menor
    if len(lp) == 0:
        menor = maior = lt[1]
    else:
        if lt[1] > maior:
            maior = lt[1]
        if lt[1] < menor:
            menor = lt[1]

    # copiando elementos da lista temp
    lp.append(lt[:])
    # limpando a lista temp
    lt.clear()

    # pergunta
    while True:
        p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if p in 'SN':
            break

    # continuando e saindo
    if p == 'S':
        print('continuando...')
    else:
        print('saindo...')
        break

# quantidade de pessoas
print(f'Foram cadastradas {len(lp)} pessoas.')

# pessoa maior e menor
print(f'O maior peso foi {maior:.1f}Kg. Peso de ', end='')
# acessando as pessoas na lista, pl = pessoa na lista
for pl in lp:
    if maior == pl[1]:
        print(f'[{pl[0]}] ', end='')

print()

print(f'O menor peso foi {menor:.1f}Kg. Peso de ', end='')
# pl = pessoa na lista
for pl in lp:
    if menor == pl[1]:
        print(f'[{pl[0]}] ', end='')

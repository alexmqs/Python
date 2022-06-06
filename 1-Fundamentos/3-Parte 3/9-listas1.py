'''As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
Listas são mutáveis
'''
# criando uma lista
lista = [45, 1, 2, 3, 4, 5]

# modificando a lista pelo índice
lista[2] = 100
print(lista)

# adicionando elemento no final da lista
lista.append(45)
print(lista)

# inserindo um elemento, a partir de um determinado índice, o índice é modificado: nomeLista.insert(índice.elemento)
lista.insert(2, 1)
print(lista)
# ordenando a lista (menor ao maior), modificando os índices
lista.sort()
print(lista)

# ordenando a lista (maior ao menor), modificando os índices
lista.sort(reverse=True)
print(lista)

# removendo/deletando o último elemento
lista.pop()
print(lista)

# removendo/deletando determinado elemento por um determinado índice, modificando o índice: nomeLista.pop(índice)
lista.pop(0)
print(lista)

# removendo/deletando determinado elemento, se existir valores iguais, o elemento removido será o 1º pela ordem do índice, modificando o índice: nomeLista.remove(elemento)
lista.remove(45)
print(lista)

# simulando erro: o elemento digitado não está na lista
lista.remove(0)
print(lista)
# previnindo tal erro:
if 0 in lista:
    lista.remove(0)
else:
    print('Não achei o determinado elemento')
print(lista)

# exibindo o tamanho da lista
print(f'Essa lista tem {len(lista)} elementos.')

# outro modo de criar uma lista
lista2 = list()

# atribuindo elementos
lista2.append(2)
lista2.append(45)
lista2.append(210)

# outro modo de atribuir elementos
for indice in range(0, 5):
    lista2.append(int(input(f'Digite um valor:')))

# exibindo a lista
for elemento in lista2:
    print(f'{elemento}...')

# exibindo a lista, com índice
for indice, elemento in enumerate(lista2):
    print(f'Na posição {indice} encontrei o valor {elemento}!')
print('Cheguei ao final da lista.')

# criando uma lista
listaA = [2, 4, 7, 23]

# igualando listas
listaB = listaA

# adicionando elemento, tanto a ListaA e a ListaB são modificadas
listaB[2] = 2000

# copiando uma lista
listaC = listaB[:]

# adicionando elemento, adicionado somente na ListaC
listaC[2] = 742


print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
print(f'Lista C: {listaC}')

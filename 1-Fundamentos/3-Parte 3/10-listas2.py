'''
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''
# criando lista1
l1 = []
l1.append('Gustavo')
l1.append(40)
print(l1)

# criando lista2
l2 = []
# copiando a lista1
l2.append(l1[:])
# modificando a lista1
l1[0] = 'Maria'
l1[1] = 22
l2.append(l1[:])
print(l2)

# criando lista3
l3 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(l3)
# exibindo determinado índice
print(l3[0][1])
# exibindo determindo índice com for
for i in l3:
    print(i)
# exibindo determindo índice com for, com deteminada informação
for i in l3:
    print(f'{i[0]} tem {i[1]} anos de idade.')

# crinando duas listas
l4 = list()
l5 = list()
mai = men = 0
for c in range(0, 3):
    l5.append(str(input('Nome:')))
    l5.append(int(input('Idade:')))
    l4.append(l5[:])
    l4.clear()
# exibindo
print(l4)
for c in range(0, 3):
    if i[0] >= 18:
        print(f'{i[0]} é maior de idade.')
        mai += 1
    else:
        print(f'{i[0]} é menor de idade.')
        men += 1
# exibindo
print(f'Temos {mai} maiores e {men} menores de idade.')


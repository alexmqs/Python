'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
# atribuindo elementos
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print(lista)

# exibindo o maior
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for indice, elemento in enumerate(lista):
    if elemento == max(lista):
        print(indice, end='... ')

# exibindo o menor
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for indice, elemento in enumerate(lista):
    if elemento == min(lista):
        print(indice, end='... ')

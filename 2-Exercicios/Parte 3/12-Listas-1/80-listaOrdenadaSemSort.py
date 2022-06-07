'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''
# inicializando a variável
lista = []

for c in range(0, 5):

    # capturando o elemento
    e = int(input('Digite um valor: '))

    # adicionando na lista
    if c == 0 or e > lista[-1] or e > max(lista):
        lista.append(e)
        print('Adicionado no final da lista...')
    else:
        # percorrendo a lista
        i = 0
        while i < len(lista):
            # se o valor retornado for menor ou igual ele insere no índice retornado
            if e <= lista[i]:
                lista.insert(i, e)
                print(f'Adicionado no índice {i} da lista...')
                # saindo
                break
            i += 1

print('Fim')
print(f'Os valores digitados foram {lista}')

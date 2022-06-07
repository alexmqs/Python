'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
# iniciando a váriavel
lista = []

while True:
    # adicionado elementos
    e = int(input('Digite um valor: '))

    # verificando elemento
    if e not in lista:
        lista.append(e)
    else:
        print('Valor duplicado! Não vou adicionar...')

    # pergunta
    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Somente sim ou não...', end=' ')

    # saindo
    if continuar == 'N':
        print('Saindo...')
        break
    else:
        print('Continuando...')

# ordenando a lista
print(f'=-'*20)
print(f'Você digitou os valores: {sorted(lista)}')

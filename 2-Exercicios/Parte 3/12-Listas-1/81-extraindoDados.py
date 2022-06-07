'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
# iniciando as variáveis
lista = []

# estrutura de repetição
while True:

    # adicionando elemento na lista
    lista.append(int(input('Digite um número: ')))

    # estrutura da pergunta
    while True:

        # pergunta
        p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

        # saindo da pergunta
        if p in 'SN':
            break
        print('Somente Sim ou Não...')

    # continuando
    if p == 'S':
        print('Continuando...')

    # saindo
    else:
        print('Saindo...')
        break

# total de contagem
print(f'Você digitou {len(lista)} elementos.')

# ordem decrescente
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')

# verificando o 5 na lista
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

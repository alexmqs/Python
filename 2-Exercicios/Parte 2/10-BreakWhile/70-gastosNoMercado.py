'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
-Qual é o total gasto na compra.
-Quantos produtos custam mais de R$10,00.
-Qual o nome do produto mais barato.'''

t = maior1000 = c = 0
print('-'*15, 'Mercadinho da esquina', '-'*15)

while True:
    # contator
    c += 1
    # atribuindo valor nas variáveis
    n = str(input('Nome do produto: '))
    p = int(input('Valor do produto: R$'))
    # continuar
    while True:
        cont = str(input('Deseja continuar? ')).upper().strip()[0]
        if cont in 'SN':
            break
    # somando o total
    t += p
    # mais de R$10.00
    if p > 1000:
        maior1000 += 1
    # mais barato e mais caro
    if c == 1:
        maisBarato = maisCaro = p
        nomeBarato = nomeCaro = n
    # mais caro
    if p > maisCaro:
        maisCaro = p
        nomeCaro = n
    # mais barato
    if p < maisBarato:
        maisBarato = p
        nomeBarato = n
    # saindo do programa
    if cont == 'N':
        break

print('-'*3, 'Saindo do Mercadinho', '-'*3)
print(f'O valor total das compras foi R${t:.2f}')
print(f'{maior1000} produtos são mais de R$1000.00')
print(f'O produto mais caro é o {nomeCaro}, ele custou R${maisCaro:.2f}')
print(f'O produto mais barato é o {nomeBarato}, ele custou R${maisBarato:.2f}')

'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
tupla = ('Lapis', 1.50, 'Borracha', 2.50, 'Caneta', 1.50, 'Livro', 5.00,
         'Estojo', 10.60, 'Apostila', 20.45, 'Apontador', 0.40, 'Folha A4', 40.00)

print('='*50)
print(f"{'Lista de Preço':^50}")
print('='*50)


for item in range(0, len(tupla), 2):
    print(f"{tupla[item]:-<40}", f"> R${tupla[item+1]:>5.2f}")

''' Outro modo
for posicao, item in enumerate(tupla):

    if posicao % 2 == 0:
        print(f"{item:-<40}{'R$'}", end='')
    else:
        print(f"{item:>8.2f}")'''

print('='*50)

'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
# variáveis
lista = [[], []]

for i in range(1, 8):
    e = int(input(f'Digite o {i}º valor: '))
    if e % 2 == 0:
        lista[0].append(e)
    else:
        lista[1].append(e)

print(f'A lista com o valores pares é: {sorted(lista[0])}')
print(f'A lista com o valores ímpares é: {sorted(lista[1])}')

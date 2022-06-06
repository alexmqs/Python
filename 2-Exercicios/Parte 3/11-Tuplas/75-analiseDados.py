'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

tupla = (int(input('Digite o 1º valor: ')),
         int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')))

print(f'Você digitou os seguintes números: {tupla}')

quantos9 = tupla.count(9)
print(f'O número 9 apareceu {quantos9} vezes.')

if 3 in tupla:
    posicao3 = tupla.index(3)+1
    print(f'O valor 3 apareceu na {posicao3}ª posição.')
else:
    print('O valor 3 não aparece em nenhuma posição.')

print(f'Os números pares digitados foram: ', end=' ')

for cont in range(0, len(tupla)):

    if tupla[cont] % 2 == 0:
        print(tupla[cont], end=' ')

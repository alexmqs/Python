'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior 
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
'''
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))

if n1 > n2:
    print(f'O número {n1} é maior que o {n2}.')
elif n1 < n2:
    print(f'O número {n2} é maior que o {n1}.')
else:
    print(f'Os valores {n1} e {n2} são iguais.')

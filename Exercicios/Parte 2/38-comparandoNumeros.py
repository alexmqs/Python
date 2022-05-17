'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior 
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
'''
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))

if n1 > n2:
    print(f'O 1º número é maior.')
elif n1 < n2:
    print(f'O 2º número é maior.')
else:
    print(f'Os dois números são iguais.')

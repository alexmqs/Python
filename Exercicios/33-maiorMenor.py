'''
Escreva um programa que leia três números e mostre qual o maior e qual o menor.
'''

a = int(input('Digite o 1º número:'))
b = int(input('Digite o 2º número:'))
c = int(input('Digite o 3º número:'))
# Verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado é o {menor}')
print(f'O maior valor digitado é o {maior}')

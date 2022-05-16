'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('Podem formar um triângulo? ')
a = int(input('Digite o 1º segmento: '))
b = int(input('Digite o 2º segmento: '))
c = int(input('Digite o 3º segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Estes segmentos podem formar um triângulo.')
else:
    print('Estes segmentos não podem formar um triângulo.')

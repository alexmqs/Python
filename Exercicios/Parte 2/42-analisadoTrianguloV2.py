'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
print('Podem formar um triângulo? ')
a = int(input('Digite o 1º segmento: '))
b = int(input('Digite o 2º segmento: '))
c = int(input('Digite o 3º segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Estes segmentos podem formar um triângulo.')
    if a == b == c:
        print('Equilátero')
    elif a == b or b == c or c == a:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Estes segmentos não podem formar um triângulo.')

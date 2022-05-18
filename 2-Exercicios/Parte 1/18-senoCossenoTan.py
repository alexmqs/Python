'''
18
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse ângulo.
'''

from math import radians, sin, cos, tan

angulo = float(input('Qual o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    f'O valor do ângulo é {angulo:.2f}, tem o seno {seno:.2f}, seu cosseno é {cosseno:.2f}  e a tangente é {tangente:.2f} ')

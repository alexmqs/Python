''' 
17
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot

catetooposto = float(input('Qual o comprimento do cateto oposto: '))
catetoAdj = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoAdj)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

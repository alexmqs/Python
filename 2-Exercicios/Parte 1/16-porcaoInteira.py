# 16
'''Crie um programa que leia um número Real qual quer pelo teclado e mostre na tela a sua porção inteira'''
# import "Biblioteca"
# from "Biblioteca" import "módulo necessário"

from math import trunc

valor = float(input('Digite o número: '))
valorConvertido = trunc(valor)

print(f'O valor digitado foi {valor} e sua porção inteira é {valorConvertido}')

'''Outra método de fazer'''

outroValor = float(input('Digite um valor: '))
valorOutroConvertido = int(outroValor)
print(
    f'O valor digitado foi {outroValor} e sua porção inteira é {valorOutroConvertido}')

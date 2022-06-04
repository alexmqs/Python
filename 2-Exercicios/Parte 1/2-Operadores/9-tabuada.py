# 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

val = int(input('Digite seu valor: '))
valini = 0
print(f'Tabuada do {val}')
while(valini <= 10):
    print(f'{valini} x {val} = {valini*val}')
    valini = valini + 1

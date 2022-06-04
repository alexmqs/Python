'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
from time import sleep
c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    sleep(0.5)
    if n >= 0:
        while c < 10:
            c += 1
            print(f'{n} x {c} = {n*c}')
    else:
        break
    c = 0
print('Saiu')

# outro modo
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')
    else:
        break
print('Saiu')

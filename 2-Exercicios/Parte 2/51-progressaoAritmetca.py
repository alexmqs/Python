'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

for c in range(0, 10):
    if c == 0:
        print(f'{p}', end='->')
    else:
        p += r
        print(f'{p}', end='->')

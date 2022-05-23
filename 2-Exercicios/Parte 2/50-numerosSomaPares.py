'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
'''
cont = 0
s = 0
for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont += 1
        s += num

print(f'A soma dos {cont} números pares é {s}')

'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros números elementos de uma sequência de Fibonacci.
ex 0 1 1 2 3 5 8
'''
n = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1

print(f'{t1} -> {t2}', end='')
while c <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> Fim')
